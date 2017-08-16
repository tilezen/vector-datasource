import unittest
from os.path import dirname
from os import listdir
from os.path import join as path_join
import fnmatch
from importlib import import_module
from collections import namedtuple
from vectordatasource.meta.python import parse_layers
from vectordatasource.meta.python import output_kind
from vectordatasource.meta.python import make_function_name_props
from vectordatasource.meta.python import output_min_zoom
from vectordatasource.meta.python import make_function_name_min_zoom
from tilequeue.query import make_fixture_data_fetcher
from tilequeue.query.fixture import LayerInfo
from ModestMaps.Core import Coordinate
from tilequeue.tile import coord_to_mercator_bounds
from tilequeue.tile import coord_to_bounds
from tilequeue.process import convert_source_data_to_feature_layers
from tilequeue.process import process_coord_no_format
from tilequeue.tile import reproject_lnglat_to_mercator
from shapely.geometry import shape as make_shape
import shapely.ops
from shapely.geometry import mapping
import hashlib
import urlparse
import requests
from tilequeue.command import parse_layer_data
from vectordatasource.meta import find_yaml_path
import json
from os import environ, makedirs
from os.path import abspath
from os.path import exists as path_exists
from os import getpid
from yaml import load as load_yaml
from contextlib import contextmanager
import re
import lxml.etree as ET
import time
from collections import defaultdict
import subprocess


# the Overpass server is used to download data about OSM elements. the
# environment allows us to override the default public Overpass server to take
# the load off it.
OVERPASS_SERVER = environ.get('OVERPASS_SERVER', 'overpass-api.de')


# the fixture cache stores generated GeoJSON fixtures. these can be somewhat
# expensive to generate (running `osm2pgsql` and so forth), so it seems worth
# caching them for everyone to reuse.
FIXTURE_CACHE = environ.get('FIXTURE_CACHE', 'http://localhost:8000')


def make_acceptable_module_name(path):
    # remove extension
    stem = path.rsplit('.', 1)[0]

    # replace all dashes with underscores
    nodash = stem.replace("-", "_")

    # put an alphabetic prefix to ensure no leading digits
    return "test_" + nodash


##
# Match properties, returning true if all of the expected properties can be
# matched with actual properties. There are 4 kinds of matches available:
#
#   {'key': None}     - The key must exist, but its value is not checked.
#   {'key': set(...)} - The key must exist and its value must be a member of
#                       the given set.
#   {'key': type}     - The key must exist and its value must be an instance of
#                       the given type.
#   {'key': callable} - The key must exist and its value is passed to the
#                       callable predicate, usually a lambda. If that returns
#                       falsey, the match fails.
#   {'key': obj}      - The key must exist and its value must be equal to the
#                       given object.
#
# This allows us to write some reasonably flexible rules.
#
def match_properties(actual, expected):
    for exp_k, exp_v in expected.iteritems():
        v = actual.get(exp_k, None)
        # normalise unicode values
        if isinstance(v, unicode):
            v = v.encode('utf-8')

        if exp_v is not None:
            if isinstance(exp_v, set):
                if v not in exp_v:
                    return False

            elif isinstance(exp_v, type):
                if not isinstance(v, exp_v):
                    return False

            elif callable(exp_v):
                if not exp_v(v):
                    return False

            elif isinstance(exp_v, unicode):
                if v != exp_v.encode('utf-8'):
                    return False

            elif v != exp_v:
                return False

        else:
            if v is None:
                return False

    return True


# quantify how different a feature is from the expected feature properties.
# this metric can be used to figure out what is a "near miss" in terms of
# the match and output a more helpful error message.
#
# returns a pair of:
#   - a numeric metric of the distance, where 0 is a match and larger
#     numbers are further from a match.
#   - an explanation of the "miss".
def match_distance(actual, expected):
    distance = 0
    misses = dict()

    for exp_k, exp_v in expected.iteritems():
        v = actual.get(exp_k, None)
        # normalise unicode values
        if isinstance(v, unicode):
            v = v.encode('utf-8')
        if isinstance(exp_v, unicode):
            exp_v = exp_v.encode('utf-8')

        if exp_v is not None:
            if isinstance(exp_v, set):
                if v not in exp_v:
                    misses[exp_k] = "%r not in %r" % (v, exp_v)
                    distance += 1

            elif isinstance(exp_v, type):
                if not isinstance(v, exp_v):
                    misses[exp_k] = "%r not an instance of %r" % (v, exp_v)
                    distance += 1

            elif v != exp_v:
                misses[exp_k] = "%r != %r" % (v, exp_v)
                distance += 1

        else:
            if v is None:
                misses[exp_k] = "missing"
                distance += 1

    return (distance, misses)


def count_matching(features, properties):
    """
    Returns a tuple containing the total number of features in the argument
    `features` and the number of features matching the properties.
    """

    num_features = len(features)
    num_matching = 0

    for f in features:
        if match_properties(f['properties'], properties):
            num_matching += 1

    return (num_features, num_matching)


def closest_matching(features, properties):
    """
    Returns a pair containing the feature which most closely matches the
    properties and a dict explaining the ways in which it didn't match.
    """

    min_distance = None
    min_feature = None
    min_misses = None

    for f in features:
        distance, misses = match_distance(f['properties'], properties)
        if min_distance is None or distance < min_distance:
            min_distance = distance
            min_feature = f
            min_misses = misses

    return (min_feature, min_misses)


def load_tests(loader, standard_tests, pattern=None):
    test_dir = dirname(__file__)
    if pattern is None:
        pattern = '*.py'

    for path in listdir(test_dir):
        if pattern and not fnmatch.fnmatch(path, pattern):
            continue

        # don't recurse on ourselves.
        if path == '__init__.py':
            continue

        pathname = path_join(test_dir, path)

        try:
            f = open(pathname, 'U')

            # TODO: take this out after all the tests have been converted!
            line = f.readline()
            f.seek(0)
            if line != 'import unittest\n':
                continue
        finally:
            if f:
                f.close()

        mod = import_module(test_dir + '.' + path.rsplit('.', 1)[0])
        tests = loader.loadTestsFromModule(mod)
        standard_tests.addTests(tests)

    return standard_tests


def parse_layer_dict(yaml_path, output_fn, fn_name_fn):
    layer_parse_result = parse_layers(yaml_path, output_fn, fn_name_fn)

    layers = {}
    for l in layer_parse_result.layer_data:
        layers[l.layer] = l.fn

    return layers


class OSMDataObject(namedtuple("OSMDataObject", "typ fid")):

    def canonical_url(self):
        return "http://www.openstreetmap.org/%s/%d" % (self.typ, self.fid)


class withlog(object):

    def __init__(self, log):
        self.log = log

    def __call__(self, *args):
        return subprocess.check_call(
            args, stdout=self.log, stderr=subprocess.STDOUT)


def load_data_into_database(osc_file, base_dir, dbname, shell):
    style_file = path_join(base_dir, 'osm2pgsql.style')
    empty_osm = path_join(base_dir, 'scripts', 'empty.osm')

    assert path_exists(style_file), "Could not find osm2pgsql style file"
    assert path_exists(empty_osm), "Could not find empty OSM file"

    for ext in ('postgis', 'hstore'):
        shell('psql', '-d', dbname, '-c', 'CREATE EXTENSION %s' % ext)

    osm2pgsql_args = '-E 3857 -s -C 1024'.split(' ')
    osm2pgsql_args.extend(['-S', style_file])
    osm2pgsql_args.extend(['-d', dbname, '--hstore-all'])

    dbhost = environ.get('PGHOST')
    if dbhost:
        osm2pgsql_args.extend(['-H', dbhost])

    dbuser = environ.get('PGUSER')
    if dbuser:
        osm2pgsql_args.extend(['-U', dbuser])

    shell('osm2pgsql', '--create', empty_osm, *osm2pgsql_args)
    shell('osm2pgsql', '--append', osc_file, *osm2pgsql_args)

    # TODO: do we really need to run any extra stuff? we don't need the
    # indexes, and nothing really touches `tags`, right?


def dump_geojson(dbname, target_file, log, clip):
    import psycopg2

    conn = psycopg2.connect("dbname=%s" % dbname)
    features = []

    for typ in ('point', 'line', 'polygon'):
        cur = conn.cursor()
        rel = conn.cursor()

        cur.execute("""
        SELECT
          osm_id,
          ST_AsGeoJSON(ST_Transform(way, 4326)) AS geom,
          to_json(tags) AS tags
        FROM planet_osm_%(typ)s
        """ % dict(typ=typ))

        for osm_id, geom, tags in cur:
            geom = json.loads(geom)
            if clip:
                shape = make_shape(geom)
                shape = shape.intersection(clip)

                # skip if the intersection removed all parts of the geometry
                if shape.is_empty:
                    continue

                geom = mapping(shape)

            if typ == 'point':
                parts_slice = '1:way_off'
            elif osm_id >= 0:
                parts_slice = 'way_off+1:rel_off'
            else:
                parts_slice = 'rel_off+1:array_upper(parts,1)'

            rel.execute("""
              SELECT json_agg(row_to_json(r.*))
              FROM planet_osm_rels r
              WHERE parts && ARRAY[%(osm_id)d::bigint]
                AND parts[%(slice)s] && ARRAY[%(osm_id)d::bigint]
            """ % dict(osm_id=osm_id, slice=parts_slice))
            rels = (rel.fetchone() or ([]))[0]

            # HACK!
            tags['source'] = 'openstreetmap.org'

            feature = dict(
                type='Feature',
                id=osm_id,
                geometry=geom,
                properties=tags,
            )
            if rels:
                feature['relations'] = rels
            features.append(feature)

    geojson = dict(type='FeatureCollection', features=features)
    with open(target_file, 'w') as fh:
        json.dump(geojson, fh)


class OSMDataSource(object):

    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.hosts = ('osm.org', 'openstreetmap.org')

    def parse(self, path):
        parts = path.split("/")
        if len(parts) != 3:
            raise Exception("OSM URLs should look like "
                            "\"http://openstreetmap.org/node/1234\", "
                            "not %r." % (path,))
        typ = parts[1]
        fid = int(parts[2])
        if typ not in ('node', 'way', 'relation'):
            raise Exception("OSM URLs should be for a node, way or "
                            "relation. I didn't understand %r"
                            % (typ,))

        return OSMDataObject(typ, fid)

    def download(self, objs, target_file, clip):
        with tempdir() as tmp:
            osc_file = path_join(tmp, 'data.osc')
            log_file = path_join(tmp, 'log.txt')

            with open(log_file, 'w') as log:
                with open(osc_file, 'w') as fh:
                    dumper = DataDumper()
                    dumper.dump_data(objs, log)
                    dumper.download_to(fh)

                with tempdb(log) as dbname:
                    shell = withlog(log)
                    load_data_into_database(
                        osc_file, self.base_dir, dbname, shell)
                    dump_geojson(dbname, target_file, log, clip)

            # TODO: on error, print the log file?


class tempdb(object):

    def __init__(self, log):
        self.name = "vector_datasource_%d" % (getpid(),)
        self.log = log

    def __enter__(self):
        subprocess.check_call(
            ["createdb", "-E", "UTF8", "-T", "template0", self.name],
            stdout=self.log, stderr=subprocess.STDOUT)
        return self.name

    def __exit__(self, type, value, traceback):
        subprocess.call(
            ["dropdb", "--if-exists", self.name],
            stdout=self.log, stderr=subprocess.STDOUT)


class tempdir(object):

    def __enter__(self):
        import tempfile
        self.tempdir = tempfile.mkdtemp()
        return self.tempdir

    def __exit__(self, type, value, traceback):
        import shutil
        shutil.rmtree(self.tempdir)


def combine_geojson_files(inputs, output):
    features = []
    for input_file in inputs:
        with open(input_file) as fh:
            geojson = json.load(fh)
            assert geojson['type'] == 'FeatureCollection', \
                "combine_geojson_files can only handle FeatureCollections, " \
                "sorry."
            features.extend(geojson['features'])

    geojson = dict(type='FeatureCollection', features=features)
    with open(output, 'w') as fh:
        json.dump(geojson, fh)


class FixtureDataSources(object):

    def __init__(self, base_dir):
        self.sources = [
            OSMDataSource(base_dir),
        ]

    def _source_for(self, p):
        host = p.netloc.lower()
        if host.startswith('www.'):
            host = host[len('www.'):]

        for source in self.sources:
            if host in source.hosts:
                return source

        return None

    def parse(self, url):
        p = urlparse.urlsplit(url)
        source = self._source_for(p)
        if source:
            return source.parse(p.path)

        raise Exception("Unable to load fixtures for host %r, used "
                        "in request for %r." % (p.netloc, url))

    def download(self, urls, output_file, clip):
        groups = defaultdict(list)

        for url in urls:
            p = urlparse.urlsplit(url)
            source = self._source_for(p)
            if not source:
                raise Exception("Unknown source for url %r", (url,))
            groups[source].append(source.parse(p.path))

        with tempdir() as tmp:
            geojson_files = []
            for source, group in groups.iteritems():
                source_name = source.__class__.__name__
                target_file = path_join(tmp, '%s.geojson' % (source_name,))
                source.download(group, target_file, clip)
                assert path_exists(target_file), \
                    "Failed to download target %r" % (target_file,)
                geojson_files.append(target_file)

            combine_geojson_files(geojson_files, output_file)

        assert path_exists(output_file), \
            "Failed to make target %r" % (output_file)


class FixtureEnvironment(object):

    def __init__(self):
        src_directory = abspath(path_join(dirname(__file__), '..'))
        config_file = path_join(src_directory, 'queries.yaml')
        buffer_cfg = {}

        # TODO: surely there's a Python module for handling this already? i
        # didn't find one on a quick search of pypi, but "cache" is such a
        # common term that it's easy to miss a relevant package amongst all
        # the irrelevant ones.
        cache_dir = environ.get('CACHE_DIR')
        if not cache_dir:
            cache_dir = path_join(environ['HOME'], '.cache',
                                  'vector-datasource')
        if not path_exists(cache_dir):
            makedirs(cache_dir)

        assert path_exists(config_file), \
            'Invalid query config path: %r' % config_file
        with open(config_file) as query_cfg_fp:
            query_cfg = load_yaml(query_cfg_fp)
        all_layer_data, layer_data, post_process_data = parse_layer_data(
                query_cfg, buffer_cfg, dirname(config_file))

        yaml_path = find_yaml_path()
        layer_props = parse_layer_dict(
            yaml_path, output_kind, make_function_name_props)
        layer_min_zoom = parse_layer_dict(
            yaml_path, output_min_zoom, make_function_name_min_zoom)

        assert set(layer_props.keys()) == set(layer_min_zoom.keys())

        layers = {}
        for layer_name in layer_props.keys():
            min_zoom_fn = layer_min_zoom[layer_name]
            props_fn = layer_props[layer_name]
            layers[layer_name] = LayerInfo(min_zoom_fn, props_fn)

        # TODO: move this to queries.yaml?
        label_placement_layers = set([
            'buildings', 'earth', 'landuse', 'water'])

        self.layer_data = layer_data
        self.post_process_data = post_process_data
        self.layer_functions = layers
        self.label_placement_layers = label_placement_layers
        self.cache_dir = cache_dir
        self.data_sources = FixtureDataSources(src_directory)

    def output_calc_spec(self):
        output_calc_spec = {}
        for name, info in self.layer_functions.items():
            output_calc_spec[name] = info.props_fn
        return output_calc_spec

    def ensure_fixture_file(self, urls, clip):
        canonical_urls = sorted(self._canonicalise(url) for url in urls)
        test_uuid = _hash(canonical_urls, clip)
        geojson_file = path_join(self.cache_dir, test_uuid + '.geojson')

        # first try - download it from the global fixture cache
        if not path_exists(geojson_file):
            try:
                r = requests.get("%s/%s.geojson" % (FIXTURE_CACHE, test_uuid))

                if r.status_code == 200:
                    with open(geojson_file, 'wb') as fh:
                        fh.write(r.text)

            except StandardError:
                pass

        # second try - generate it from the URLs
        if not path_exists(geojson_file):
            self.data_sources.download(urls, geojson_file, clip)
            assert path_exists(geojson_file), \
                "Ooops, something went wrong downloading %r" % (geojson_file,)

        return geojson_file

    def _canonicalise(self, url):
        data_source = self.data_sources.parse(url)
        return data_source.canonical_url()


def _load_fixtures(geojson_files):
    rows = []
    for geojson_file in geojson_files:
        with open(geojson_file, 'rb') as fh:
            rows.extend(_load_fixture(fh))
    return rows


def _load_fixture(fh):
    js = json.load(fh)
    rows = []
    for feature in js['features']:
        fid = feature['id']
        props = feature['properties']
        rels = feature.get('relations')
        if rels:
            props['__relations__'] = rels
        geom_lnglat = make_shape(feature['geometry'])
        geom_mercator = shapely.ops.transform(
            reproject_lnglat_to_mercator, geom_lnglat)

        rows.append((fid, geom_mercator, props))
    return rows


class FixtureFeatureFetcher(object):

    def __init__(self, geojson_files, fixture_env):
        rows = _load_fixtures(geojson_files)
        self.fetcher = make_fixture_data_fetcher(
            fixture_env.layer_functions, rows,
            fixture_env.label_placement_layers)
        self.fixture_env = fixture_env

    def _generate_tile(self, z, x, y):
        coord = Coordinate(zoom=z, column=x, row=y)

        nominal_zoom = coord.zoom
        unpadded_bounds = coord_to_mercator_bounds(coord)

        source_rows = self.fetcher(nominal_zoom, unpadded_bounds)
        feature_layers = convert_source_data_to_feature_layers(
            source_rows, self.fixture_env.layer_data, unpadded_bounds,
            nominal_zoom)
        processed_feature_layers, extra_data = process_coord_no_format(
            feature_layers, nominal_zoom, unpadded_bounds,
            self.fixture_env.post_process_data,
            self.fixture_env.output_calc_spec())

        tile = {}
        for pfl in processed_feature_layers:
            features = []
            for shape, props, fid in pfl['features']:
                feature = dict(
                    geometry=mapping(shape),
                    properties=props,
                    id=fid,
                )
                features.append(feature)
            tile[pfl['name']] = features
        return tile

    def features_in_tile_layer(self, z, x, y, layer):
        @contextmanager
        def inner(z, x, y, layer):
            tile_layers = self._generate_tile(z, x, y)
            yield tile_layers.get(layer, [])
        return inner(z, x, y, layer)

    @contextmanager
    def layers_in_tile(self, z, x, y):
        @contextmanager
        def inner(z, x, y):
            tile_layers = self._generate_tile(z, x, y)
            yield tile_layers.keys()
        return inner(z, x, y)

    @contextmanager
    def features_in_mvt_layer(self, z, x, y, layer):
        raise Exception("unimplemented")


def _hash(urls, clip):
    m = hashlib.sha256()
    for url in urls:
        m.update(url)
    if clip:
        m.update(clip.wkt)
    return m.hexdigest()


class Assertions(object):

    def __init__(self, feature_fetcher):
        self.ff = feature_fetcher

    def assert_has_feature(self, z, x, y, layer, properties):
        with self.ff.features_in_tile_layer(z, x, y, layer) as features:
            num_features, num_matching = count_matching(
                features, properties)

            if num_features == 0:
                raise Exception(
                    "Did not find feature including properties %r (because "
                    "layer %r was empty)" % (properties, layer))

            if num_matching == 0:
                closest, misses = closest_matching(features, properties)
                raise Exception(
                    "Did not find feature including properties %r. The "
                    "closest match was %r: missed %r." %
                    (properties, closest['properties'], misses))

    def assert_at_least_n_features(self, z, x, y, layer, properties, n):
        """
        Downloads a tile and checks that it contains at least `n` features
        which match the given `properties`.
        """
        with self.ff.features_in_tile_layer(z, x, y, layer) as features:
            num_features, num_matching = count_matching(
                features, properties)

            if num_features < n:
                raise Exception(
                    "Found fewer than %d features including properties %r "
                    "(because layer %r had %d features)" %
                    (n, properties, layer, num_features))

            if num_matching < n:
                raise Exception(
                    "Did not find %d features including properties "
                    "%r, found only %d" % (n, properties, num_matching))

    def assert_less_than_n_features(self, z, x, y, layer, properties, n):
        """
        Downloads a tile and checks that it contains less than `n` features
        which match the given `properties`.
        """
        with self.ff.features_in_tile_layer(z, x, y, layer) as features:
            num_features, num_matching = count_matching(
                features, properties)

            if num_matching >= n:
                raise Exception(
                    "Did not find %d features including properties "
                    "%r, found only %d" % (n, properties, num_matching))

    def assert_no_matching_feature(self, z, x, y, layer, properties):
        with self.ff.features_in_tile_layer(z, x, y, layer) as features:
            num_features, num_matching = count_matching(
                features, properties)

            if num_matching > 0:
                feature = None
                for f in features:
                    if match_properties(f['properties'], properties):
                        feature = f
                        break

                raise Exception(
                    "Found feature matching properties %r in "
                    "layer %r, but was supposed to find none. For example: "
                    "%r" % (properties, layer, feature['properties']))

    def assert_feature_geom_type(self, z, x, y, layer, feature_id,
                                 exp_geom_type):
        with self.ff.features_in_tile_layer(z, x, y, layer) as features:
            for feature in features:
                if feature['properties']['id'] == feature_id:
                    shape = make_shape(feature['geometry'])
                    assert shape.type == exp_geom_type, \
                        'Unexpected geometry type: %s' % shape.type
                    break
            else:
                assert 0, 'No feature with id: %d found' % feature_id


def memoize(f):
    result = {}

    def wrapped(*args, **kwargs):
        cache_key = tuple(args)
        if not result:
            result[cache_key] = f(*args, **kwargs)
        return result[cache_key]

    return wrapped


@memoize
def make_fixture_environment():
    return FixtureEnvironment()


def expand_bbox(bounds, padding):
    minx, miny, maxx, maxy = bounds
    deltax = maxx - minx
    deltay = maxy - miny
    minx -= padding * deltax
    maxx += padding * deltax
    miny -= padding * deltay
    maxy += padding * deltay
    minx = max(minx, -180)
    miny = max(miny, -90)
    maxx = min(maxx, 180)
    maxy = min(maxy, 90)
    return (minx, miny, maxx, maxy)


class OsmFixtureTest(unittest.TestCase):

    def setUp(self):
        self.env = make_fixture_environment()

    def load_fixtures(self, urls, clip=None):
        geojson_file = self.env.ensure_fixture_file(urls, clip)
        feature_fetcher = FixtureFeatureFetcher([geojson_file], self.env)
        self.assertions = Assertions(feature_fetcher)

    def assert_has_feature(self, z, x, y, layer, props):
        self.assertions.assert_has_feature(z, x, y, layer, props)

    def assert_no_matching_feature(self, z, x, y, layer, props):
        self.assertions.assert_no_matching_feature(z, x, y, layer, props)

    def features_in_tile_layer(self, z, x, y, layer):
        return self.assertions.ff.features_in_tile_layer(z, x, y, layer)

    def tile_bbox(self, z, x, y, padding=0.0):
        coord = Coordinate(zoom=z, column=x, row=y)
        bounds = coord_to_bounds(coord)
        if padding:
            bounds = expand_bbox(bounds, padding)
        return shapely.geometry.box(*bounds)


def chunks(length, iterable):
    """
    Converts an iterable into a generator of chunks of size up to length.
    """

    chunk = []
    for obj in iterable:
        chunk.append(obj)
        if len(chunk) >= length:
            yield chunk
            del chunk[:]
    if chunk:
        yield chunk


class OsmChange(object):
    def __init__(self, fh):
        self.fh = fh
        self.fh.write("<?xml version='1.0' encoding='utf-8'?>\n")
        self.fh.write("<osmChange version=\"0.6\">\n")

    def flush(self):
        self.fh.write("</osmChange>\n")

    def query_result(self, query):
        retry_count = 4
        wait_time_in_s = 100
        r = None
        for _ in range(retry_count):
            r = requests.get("http://%s/api/interpreter" % OVERPASS_SERVER,
                             params=dict(data=query))
            if r.status_code == 200:
                # "200 OK is sent when the query has been successfully
                # answered.
                # The payload of the response is the result data."
                # quote from http://overpass-api.de/command_line.html
                # so response is usable
                break

            if r.status_code not in (429, 504):
                # "429 Too Many Requests is sent if you pass multiple queries
                # from one IP"
                # regularly happens with multiple sequential querries
                # "504 Gateway Timeout is sent if the server has already so
                # much load that the request cannot be executed. In most
                # cases, it is best to try again later"
                # quotes from http://overpass-api.de/command_line.html

                # in cases of 429 and 504 waiting and retrying is typically
                # enough to get an expected response
                break

            print "%d code returned instead of overpass response - request " \
                "will be repeated after %d seconds" % \
                (r.status_code, wait_time_in_s)
            time.sleep(wait_time_in_s)

        if r.status_code != 200:
            raise RuntimeError("Unable to fetch data from Overpass: %r"
                               % r.status_code)
        if r.headers['content-type'] != 'application/osm3s+xml':
            raise RuntimeError("Expected XML, but got %r"
                               % r.headers['content-type'])
        return r.content

    def add_query(self, query):
        data = self.query_result(query)
        root = ET.fromstring(data)
        root.tag = 'modify'
        del root.attrib['version']
        del root.attrib['generator']
        root.remove(root.find('note'))
        root.remove(root.find('meta'))
        xml = ET.ElementTree(root)
        xml.write(self.fh, encoding='utf8', xml_declaration=False)


class DataDumper(object):
    def __init__(self):
        self.nodes = set()
        self.ways = set()
        self.relations = set()
        self.pattern = re.compile('#.*(node|way|rel(ation)?)[ /]+([0-9]+)')

        self.raw_queries = list()
        self.raw_pattern = re.compile('#.*RAW QUERY:(.*)')

    def add_object(self, typ, id_str):
        id = int(id_str)
        if typ == 'node':
            self.nodes.add(id)

        elif typ == 'way':
            self.ways.add(id)

        else:
            assert typ.startswith('rel'), \
                "Expected 'rel' or 'relation', got %r" % typ
            self.relations.add(id)

    def add_query(self, raw):
        self.raw_queries.append(raw)

    def build_query(self, fmt, ids):
        query = "("
        for id in ids:
            query += fmt % id
        query += ");out;"
        return query

    def download_to(self, fh):
        osc = OsmChange(fh)

        for n_ids in chunks(1000, self.nodes):
            osc.add_query(self.build_query("node(%d);", n_ids))
        for w_ids in chunks(100, self.ways):
            osc.add_query(self.build_query("way(%d);>;", w_ids))
        for r_ids in chunks(10, self.relations):
            osc.add_query(self.build_query("relation(%d);>;",  r_ids))
        for raw_query in self.raw_queries:
            osc.add_query("(" + raw_query + ");out;")

        osc.flush()

    def dump_data(self, objs, log):
        for obj in objs:
            try:
                self.add_object(obj.typ, obj.fid)
                # TODO: handle "raw" queries.

            except:
                print>>log, "FAIL: fetching OSM data for %r" % (obj,)
                raise


def flatten_tests(suite):
    tests = []
    for t in suite:
        if isinstance(t, unittest.TestSuite):
            tests.extend(flatten_tests(t))
        elif isinstance(t, unittest.TestCase):
            tests.append(t)
        else:
            raise Exception("Didn't understand type %s" % (t.__class__,))
    return tests


if __name__ == '__main__':
    from unittest.util import strclass
    import sys

    loader = unittest.TestLoader()
    suite = load_tests(loader, unittest.TestSuite())

    tests = []
    if sys.argv:
        for t in flatten_tests(suite):
            test_name = strclass(t.__class__) + "." + t._testMethodName
            for prefix in sys.argv:
                if test_name.startswith(prefix):
                    tests.append(t)
                    break
    else:
        tests = flatten_tests(suite)

    suite = unittest.TestSuite()
    suite.addTests(tests)

    runner = unittest.TextTestRunner()
    runner.run(suite)
