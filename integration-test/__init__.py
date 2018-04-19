import unittest
from os.path import dirname
from os import listdir
from os.path import join as path_join
from os.path import getsize as path_getsize
import fnmatch
from importlib import import_module
from collections import namedtuple
from vectordatasource.meta.python import parse_layers
from vectordatasource.meta.python import output_kind
from vectordatasource.meta.python import make_function_name_props
from vectordatasource.meta.python import output_min_zoom
from vectordatasource.meta.python import make_function_name_min_zoom
from tilequeue.query import make_fixture_data_fetcher
from tilequeue.query.common import LayerInfo
from ModestMaps.Core import Coordinate
from tilequeue.tile import coord_to_mercator_bounds
from tilequeue.tile import coord_to_bounds
from tilequeue.process import convert_source_data_to_feature_layers
from tilequeue.process import process_coord_no_format
from tilequeue.tile import reproject_lnglat_to_mercator
from tilequeue.tile import reproject_mercator_to_lnglat
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
import urllib
import shapefile
from tilequeue import wof
from itertools import izip_longest


# the Overpass server is used to download data about OSM elements. the
# environment allows us to override the default public Overpass server to take
# the load off it.
OVERPASS_SERVER = environ.get('OVERPASS_SERVER', 'overpass-api.de')


# the fixture cache stores generated GeoJSON fixtures. these can be somewhat
# expensive to generate (running `osm2pgsql` and so forth), so it seems worth
# caching them for everyone to reuse.
FIXTURE_CACHE = environ.get(
    'FIXTURE_CACHE',
    'http://s3.amazonaws.com/mapzen-tiles-assets/integration-test-fixtures')


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


def load_tests(loader, standard_tests, test_instance, pattern=None):
    test_dir = dirname(__file__)

    # can't load modules if there's a ".." in the path to them
    assert ".." not in test_dir

    if pattern is None:
        pattern = '*.py'

    for path in listdir(test_dir):
        if pattern and not fnmatch.fnmatch(path, pattern):
            continue

        # don't recurse on ourselves.
        if path == '__init__.py':
            continue

        # don't load hidden files
        if path.startswith('.'):
            continue

        mod = import_module(test_dir + '.' + path.rsplit('.', 1)[0])

        # pass a parameter to FixtureTest telling it whether or not to
        # actually run the tests. setting download_only=True means it only
        # downloads the fixtures and stubs out all the test methods to pass.
        #
        # this is useful when forcing the tests to pre-download, as we need
        # to do with CircleCI, as the cache is only saved after the
        # dependencies step, not after the test step itself.
        for name in dir(mod):
            # skip any "special" names, as these won't contain any tests.
            if name.startswith('__'):
                continue

            klass = getattr(mod, name)
            if isinstance(klass, type) and \
               issubclass(klass, unittest.TestCase):
                names = loader.getTestCaseNames(klass)
                for name in names:
                    # TODO: when not instanceof FixtureTest, don't add the
                    # download_only parameter.
                    standard_tests.addTest(klass(name, test_instance))

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


class OverpassObject(namedtuple("OverpassObject", "raw_query")):

    def canonical_url(self):
        query = urllib.urlencode(dict(data=self.raw_query))
        url = urlparse.urlunparse((
            'http', 'overpass-api.de', '/api/interpreter',
            None, query, None))
        return url


class FixtureShapeDataObject(
        namedtuple("FixtureShapeDataObject", "table name")):

    def canonical_url(self):
        path = "/".join(["", "fixtures", self.table, self.name])
        url = urlparse.urlunparse((
            'file', 'integration-tests', path, None, None, None))
        return url


class WOFDataObject(namedtuple("WOFDataObject", "wof_id")):

    def canonical_url(self):
        slashed = ""
        # get digits in groups of 3
        for digits in izip_longest(*([iter(str(self.wof_id))]*3)):
            if slashed:
                slashed += "/"
            for d in digits:
                if d is not None:
                    slashed += d
        url = "https://whosonfirst.mapzen.com/data/%s/%d.geojson" \
              % (slashed, self.wof_id)
        return url


# minimal implementation of the WOF metadata class to be passed into
# the WOF data fetcher.
WOFMeta = namedtuple("WOFMeta", "wof_id hash")


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
    # default installs of PostgreSQL limit the number of connections to a
    # low enough value that it causes problems for osm2pgsql. this shouldn't
    # be too much of a problem, since individual fixtures _should_ be quite
    # small.
    osm2pgsql_args.append('--number-processes=1')

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


def dump_table(conn, typ, clip, simplify):
    features = []
    all_relation_ids = set()
    cur = conn.cursor()
    rel = conn.cursor()
    way = conn.cursor()

    # allow the way to be simplified for large geometries where we don't need
    # positional accuracy (e.g: when testing tag transforms).
    geom = "way"
    if simplify:
        geom = "ST_SimplifyPreserveTopology(%s, %f)" % (geom, simplify)

    query = """
    SELECT
    osm_id,
      ST_AsGeoJSON(ST_Transform(%(geom)s, 4326)) AS geom,
      to_json(tags) AS tags
    FROM planet_osm_%(typ)s
    WHERE akeys(tags - ARRAY['created_by', 'source']) <> ARRAY[]::text[]
    """ % dict(typ=typ, geom=geom)

    # since we will clip objects to the intersection anyway, we don't need to
    # query anything outside of the clipping shape.
    if clip:
        query += " AND way && ST_Transform(ST_GeomFromText('%s', " \
                 "4326), 3857)" % (clip.wkt,)

    cur.execute(query)
    for osm_id, geom, tags in cur:
        # this is usually because something (e.g: ST_Simplify) has turned the
        # geometry column to NULL.
        if not isinstance(geom, (str, buffer)):
            continue

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
          SELECT id
          FROM planet_osm_rels r
          WHERE parts && ARRAY[%(osm_id)d::bigint]
          AND parts[%(slice)s] && ARRAY[%(osm_id)d::bigint]
          ORDER BY id ASC
        """ % dict(osm_id=osm_id, slice=parts_slice))
        rels = [int(r[0]) for r in rel]

        # keep track of all relation IDs so that we can build a list of them
        # all at the top level object.
        all_relation_ids |= set(rels)

        # HACK!
        tags['source'] = 'openstreetmap.org'

        feature = dict(
            type='Feature',
            id=osm_id,
            geometry=geom,
            properties=tags,
        )

        if rels:
            feature['relation_ids'] = rels

        if typ == 'point':
            way.execute("""
              SELECT id
              FROM planet_osm_ways w
              WHERE nodes && ARRAY[%s::bigint]
            """, (osm_id,))
            ways = [int(w[0]) for w in way]
            feature['used_in_ways'] = ways

        features.append(feature)

    return features, all_relation_ids


def dump_geojson(dbname, target_file, log, clip, simplify):
    import psycopg2

    conn = psycopg2.connect("dbname=%s" % dbname)
    features = []
    relations = []

    try:
        relation_ids = set()

        for typ in ('point', 'line', 'polygon'):
            new_features, new_relation_ids = dump_table(
                conn, typ, clip, simplify)

            features.extend(new_features)
            relation_ids |= new_relation_ids

        if relation_ids:
            with conn.cursor() as cur:
                # this complex query grabs all the relations using any feature
                # that the query has seen so far, and the relations using
                # those, and so on recursively. this data is used to discover
                # the root relation ID for railway stations.
                cur.execute("""
WITH RECURSIVE upward_search(level,path,id,parts,rel_off,cycle) AS (
    SELECT 0,ARRAY[id],id,parts,rel_off,false
    FROM planet_osm_rels WHERE id IN %s
  UNION
    SELECT
      level + 1,
      path || r.id,
      r.id,
      r.parts,
      r.rel_off,
      r.id = ANY(path)
    FROM
      planet_osm_rels r JOIN upward_search s
    ON
      ARRAY[s.id] && r.parts
    WHERE
      ARRAY[s.id] && r.parts[r.rel_off+1:array_upper(r.parts,1)] AND
      NOT cycle
  )
  SELECT json_agg(row_to_json(r.*))
  FROM planet_osm_rels r
  WHERE r.id IN (SELECT DISTINCT id FROM upward_search)
                """, (tuple(relation_ids),))

                relations = cur.fetchone()[0]

    finally:
        conn.close()

    geojson = dict(type='FeatureCollection', features=features,
                   relations=relations)
    with open(target_file, 'w') as fh:
        json.dump(geojson, fh)


def _download_from_overpass(objs, target_file, clip, simplify, base_dir):
    with tempdir() as tmp:
        osc_file = path_join(tmp, 'data.osc')
        log_file = path_join(tmp, 'log.txt')

        try:
            with open(log_file, 'w') as log:
                with open(osc_file, 'w') as fh:
                    dumper = DataDumper()
                    dumper.dump_data(objs, log)
                    dumper.download_to(fh)

                with tempdb(log) as dbname:
                    shell = withlog(log)
                    load_data_into_database(
                        osc_file, base_dir, dbname, shell)
                    dump_geojson(dbname, target_file, log, clip, simplify)

        except Exception:
            # TODO: is there some way of attaching this to the stack frame
            # for easier reading?
            import sys
            with open(log_file, 'r') as log:
                sys.stderr.write(log.read())
            raise


def _convert_shape_to_geojson(shpfile, jsonfile, override_properties, clip,
                              simplify):
    dbffile = shpfile.replace(".shp", ".dbf")
    features = []

    with open(shpfile, "rb") as shp:
        with open(dbffile, "rb") as dbf:
            sf = shapefile.Reader(shp=shp, dbf=dbf)
            field_names = [f[0].lower() for f in sf.fields[1:]]
            gid = 0

            for row in sf.iterShapeRecords():
                geom_mercator = make_shape(row.shape.__geo_interface__)
                geom_lnglat = shapely.ops.transform(
                    reproject_mercator_to_lnglat, geom_mercator)
                props = dict(zip(field_names, row.record))
                props.update(override_properties)
                gid += 1

                if clip:
                    geom_lnglat = geom_lnglat.intersection(clip)

                if simplify:
                    geom_lnglat = geom_lnglat.simplify(simplify)

                if geom_lnglat.is_empty:
                    continue

                feature = dict(
                    type='Feature',
                    id=gid,
                    geometry=mapping(geom_lnglat),
                    properties=props
                )
                features.append(feature)

    geojson = dict(type='FeatureCollection', features=features)
    with open(jsonfile, 'w') as fh:
        json.dump(geojson, fh)


class OverpassDataSource(object):

    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.hosts = ('overpass-api.de',)

    def parse(self, url):
        assert url.path == '/api/interpreter', \
            "Overpass URL paths should be /api/interpreter, not %r" \
            % (url.path,)
        url_query = urlparse.parse_qs(url.query)
        raw_query = "".join(url_query['data'])
        return OverpassObject(raw_query)

    def download(self, objs, target_file, clip, simplify):
        _download_from_overpass(objs, target_file, clip, simplify,
                                self.base_dir)


class OSMDataSource(object):

    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.hosts = ('osm.org', 'openstreetmap.org')

    def parse(self, url):
        parts = url.path.split("/")
        if len(parts) != 3:
            raise Exception("OSM URLs should look like "
                            "\"http://openstreetmap.org/node/1234\", "
                            "not %r." % (url.path,))
        typ = parts[1]
        fid = int(parts[2])
        if typ not in ('node', 'way', 'relation'):
            raise Exception("OSM URLs should be for a node, way or "
                            "relation. I didn't understand %r"
                            % (typ,))

        return OSMDataObject(typ, fid)

    def download(self, objs, target_file, clip, simplify):
        _download_from_overpass(objs, target_file, clip, simplify,
                                self.base_dir)


class FixtureShapeSource(object):

    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.hosts = ('integration-test',)

    def parse(self, url):
        parts = url.path.split("/")
        if len(parts) != 4:
            raise Exception(
                "Fixture shape URLs should look like: "
                "file://integration-test/fixtures/ne_10m_ocean/"
                "1030-invalid-wkb-polygon.shp, not %r" %
                (url,))
        if parts[0] != "" or parts[1] != "fixtures":
            raise Exception("Malformed fixture shapefile URL")
        table = parts[2]
        name = parts[3]

        return FixtureShapeDataObject(table, name)

    def download(self, objs, target_file, clip, simplify):
        with tempdir() as tmp:
            jsonfiles = []
            for obj in objs:
                jsonfile = path_join(
                    tmp, "%s_%s.geojson" % (obj.table, obj.name))
                shpfile = path_join(
                    self.base_dir, "integration-test", "fixtures",
                    obj.table, obj.name)
                if obj.table.startswith("ne_"):
                    override_properties = dict(source="naturalearthdata.com")
                elif obj.table in ("buffered_land"):
                    # have to add the maritime_boundary setting here, as the
                    # name is too long to be a field in the shapefile!
                    override_properties = dict(
                        source="tilezen.org",
                        maritime_boundary=True,
                    )
                else:
                    override_properties = dict(source="openstreetmapdata.com")
                _convert_shape_to_geojson(
                    shpfile, jsonfile, override_properties, clip, simplify)
                jsonfiles.append(jsonfile)

            combine_geojson_files(jsonfiles, target_file)


class WOFSource(object):

    def __init__(self):
        self.hosts = ('whosonfirst.mapzen.com',)

    def parse(self, url):
        parts = url.path.split("/")
        if len(parts) != 6:
            raise Exception(
                "Fixture shape URLs should look like: "
                "https://whosonfirst.mapzen.com/data/858/260/37/"
                "85826037.geojson, not %r" %
                (url,))
        if parts[0] != "" or parts[1] != "data":
            raise Exception("Malformed fixture shapefile URL")
        id_str = "".join(parts[2:5])
        name = id_str + ".geojson"
        if name != parts[5]:
            raise Exception("Expected URL to be redundant, but %r doesn't "
                            "look like %r" % (parts[2:5], parts[5]))

        return WOFDataObject(int(id_str))

    def download(self, objs, target_file, clip, simplify):
        with tempdir() as tmp:
            jsonfiles = []
            for obj in objs:
                # fake the hash; sadness
                meta = WOFMeta(obj.wof_id, None)
                url = obj.canonical_url()

                n = wof.fetch_url_raw_neighbourhood(url, meta, 1)
                if isinstance(n, wof.NeighbourhoodFailure):
                    raise Exception("Failed to get WOF data: %s"
                                    % n.reason)

                geometry = shapely.ops.transform(
                    reproject_mercator_to_lnglat, n.label_position)

                properties = {
                    'source': 'whosonfirst.mapzen.com',
                    'name': n.name,
                    'min_zoom': n.min_zoom,
                    'max_zoom': n.max_zoom,
                    'placetype': n.placetype,
                }
                properties.update(n.l10n_names)

                features = [dict(
                    id=obj.wof_id,
                    type='Feature',
                    geometry=mapping(geometry),
                    properties=properties
                )]
                geojson = dict(type='FeatureCollection', features=features)

                jsonfile = path_join(tmp, "%d.geojson" % (obj.wof_id))
                with open(jsonfile, 'w') as fh:
                    json.dump(geojson, fh)
                jsonfiles.append(jsonfile)

            combine_geojson_files(jsonfiles, target_file)


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
    relations = []
    for input_file in inputs:
        with open(input_file) as fh:
            geojson = json.load(fh)
            assert geojson['type'] == 'FeatureCollection', \
                "combine_geojson_files can only handle FeatureCollections, " \
                "sorry."
            features.extend(geojson['features'])
            relations.extend(geojson.get('relations', []))

    geojson = dict(type='FeatureCollection', features=features,
                   relations=relations)
    with open(output, 'w') as fh:
        json.dump(geojson, fh)


class FixtureDataSources(object):

    def __init__(self, base_dir):
        self.sources = [
            OSMDataSource(base_dir),
            OverpassDataSource(base_dir),
            FixtureShapeSource(base_dir),
            WOFSource(),
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
            return source.parse(p)

        raise Exception("Unable to load fixtures for host %r, used "
                        "in request for %r." % (p.netloc, url))

    def download(self, urls, output_file, clip, simplify):
        groups = defaultdict(list)

        for url in urls:
            p = urlparse.urlsplit(url)
            source = self._source_for(p)
            if not source:
                raise Exception("Unknown source for url %r", (url,))
            groups[source].append(source.parse(p))

        with tempdir() as tmp:
            geojson_files = []
            for source, group in groups.iteritems():
                source_name = source.__class__.__name__
                target_file = path_join(tmp, '%s.geojson' % (source_name,))
                source.download(group, target_file, clip, simplify)
                assert path_exists(target_file), \
                    "Failed to download target %r" % (target_file,)
                geojson_files.append(target_file)

            combine_geojson_files(geojson_files, output_file)

        assert path_exists(output_file), \
            "Failed to make target %r" % (output_file)


class FixtureEnvironment(object):

    def __init__(self, regenerate):
        self.regenerate = regenerate
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

        # TODO: move this to queries.yaml?
        allowed_shapes = {
            'boundaries': set(['linestring', 'polygon']),
            'buildings': set(['point', 'polygon']),
            'earth': set(['point', 'linestring', 'polygon']),
            'landuse': set(['linestring', 'polygon']),
            'places': set(['point']),
            'pois': set(['point', 'polygon']),
            'roads': set(['linestring']),
            'transit': set(['linestring', 'polygon']),
            'water': set(['point', 'linestring', 'polygon']),
        }

        layers = {}
        for layer_name in layer_props.keys():
            min_zoom_fn = layer_min_zoom[layer_name]
            props_fn = layer_props[layer_name]
            allowed = allowed_shapes.get(layer_name)
            layers[layer_name] = LayerInfo(min_zoom_fn, props_fn, allowed)

        # TODO: move this to queries.yaml?
        label_placement_layers = {
            'point': set(['earth', 'water']),
            'polygon': set(['buildings', 'earth', 'landuse', 'water']),
            'linestring': set(['earth', 'landuse', 'water']),
        }

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

    def ensure_fixture_file(self, urls, clip, simplify):
        canonical_urls = sorted(self._canonicalise(url) for url in urls)
        test_uuid = _hash(canonical_urls, clip, simplify)
        geojson_file = path_join(self.cache_dir, test_uuid + '.geojson')

        # if we want to regenerate from scratch, skip all the cache checking
        # steps.
        if not self.regenerate:
            # if the file exists, use it
            if path_exists(geojson_file):
                return geojson_file

            # first try - download it from the global fixture cache
            try:
                r = requests.get("%s/%s.geojson" % (FIXTURE_CACHE, test_uuid))

                if r.status_code == 200:
                    with open(geojson_file, 'wb') as fh:
                        fh.write(r.text)
                    return geojson_file

            except StandardError:
                pass

        # second try - generate it from the URLs
        self.data_sources.download(urls, geojson_file, clip, simplify)
        assert path_exists(geojson_file), \
            "Ooops, something went wrong downloading %r" % (geojson_file,)

        return geojson_file

    def _canonicalise(self, url):
        data_source = self.data_sources.parse(url)
        return data_source.canonical_url()


def _load_fixtures(geojson_files):
    rows = []
    rels = []
    for geojson_file in geojson_files:
        with open(geojson_file, 'rb') as fh:
            new_rows, new_rels = _load_fixture(fh)
            rows.extend(new_rows)
            rels.extend(new_rels)
    return rows, rels


WAY_TYPES = ('LineString', 'MultiLineString', 'Polygon', 'MultiPolygon')


def _load_fixture(fh):
    js = json.load(fh)
    relations = js['relations']
    rows = []
    ways = {}
    nodes_to_update = []
    for feature in js['features']:
        fid = feature['id']
        props = feature['properties']
        rel_ids = set(feature.get('relation_ids', []))
        if rel_ids:
            rels = []
            for r in relations:
                if r['id'] in rel_ids:
                    rels.append(r)
            if rels:
                props['__relations__'] = rels
        geom_lnglat = make_shape(feature['geometry'])
        geom_mercator = shapely.ops.transform(
            reproject_lnglat_to_mercator, geom_lnglat)

        # save ways that this node is used in to make the connection in a
        # second pass. this connection allows us to do things such as look up
        # what kind of highway a gate node is part of.
        way_ids = feature.get('used_in_ways', [])
        if way_ids:
            nodes_to_update.append((props, way_ids))

        row = (fid, geom_mercator, props)
        if geom_mercator.geom_type in WAY_TYPES and fid >= 0:
            ways[fid] = row

        rows.append(row)

    # go back over the saved nodes to update and ways, making the links back
    # to the way features.
    for node_props, way_ids in nodes_to_update:
        node_ways = []
        for way_id in way_ids:
            way = ways.get(way_id)
            if way:
                node_ways.append(way)
        if node_ways:
            node_props['__ways__'] = node_ways

    return rows, relations


class FixtureFeatureFetcher(object):

    def __init__(self, rows, rels, fixture_env):
        self.fetcher = make_fixture_data_fetcher(
            fixture_env.layer_functions, rows,
            fixture_env.label_placement_layers,
            relations=rels)
        self.fixture_env = fixture_env

    def _generate_feature_layers(self, z, x, y):
        coord = Coordinate(zoom=z, column=x, row=y)

        nominal_zoom = coord.zoom
        unpadded_bounds = coord_to_mercator_bounds(coord)

        source_rows = self.fetcher(nominal_zoom, unpadded_bounds)
        feature_layers = convert_source_data_to_feature_layers(
            source_rows, self.fixture_env.layer_data, unpadded_bounds,
            nominal_zoom)
        return process_coord_no_format(
            feature_layers, nominal_zoom, unpadded_bounds,
            self.fixture_env.post_process_data,
            self.fixture_env.output_calc_spec())

    def _generate_tile(self, z, x, y):
        processed_feature_layers, extra_data = self._generate_feature_layers(
            z, x, y)
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

    def layers_in_tile(self, z, x, y):
        @contextmanager
        def inner(z, x, y):
            tile_layers = self._generate_tile(z, x, y)
            yield tile_layers.keys()
        return inner(z, x, y)

    def features_in_mvt_layer(self, z, x, y, layer):
        @contextmanager
        def inner(z, x, y, layer):
            pfl, extra = self._generate_feature_layers(z, x, y)

            coord = Coordinate(zoom=z, column=x, row=y)
            bounds_merc = coord_to_mercator_bounds(coord)
            bounds_lnglat = coord_to_bounds(coord)

            from cStringIO import StringIO
            io = StringIO()

            from tilequeue.format import format_mvt
            extent = 4096
            format_mvt(io, pfl, z, bounds_merc, bounds_lnglat, extent)

            from mapbox_vector_tile import decode as mvt_decode
            msg = mvt_decode(io.getvalue())

            data = msg[layer]
            features = data['features']
            yield features

        return inner(z, x, y, layer)


def _hash(urls, clip, simplify):
    m = hashlib.sha256()
    for url in urls:
        m.update(url)
    if clip:
        m.update(clip.wkt)
    if simplify:
        m.update("simplify=%f" % (simplify,))
    return m.hexdigest()


class Assertions(object):

    def __init__(self, feature_fetcher, test):
        self.ff = feature_fetcher
        self.test = test

    def assert_has_feature(self, z, x, y, layer, properties):
        with self.ff.features_in_tile_layer(z, x, y, layer) as features:
            num_features, num_matching = count_matching(
                features, properties)

            if num_features == 0:
                self.test.fail(
                    "Did not find feature including properties %r (because "
                    "layer %r was empty)" % (properties, layer))

            if num_matching == 0:
                closest, misses = closest_matching(features, properties)
                self.test.fail(
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
                self.test.fail(
                    "Found fewer than %d features including properties %r "
                    "(because layer %r had %d features)" %
                    (n, properties, layer, num_features))

            if num_matching < n:
                self.test.fail(
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
                self.test.fail(
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

                self.test.fail(
                    "Found feature matching properties %r in "
                    "layer %r, but was supposed to find none. For example: "
                    "%r" % (properties, layer, feature['properties']))

    def assert_feature_geom_type(self, z, x, y, layer, feature_id,
                                 exp_geom_type):
        with self.ff.features_in_tile_layer(z, x, y, layer) as features:
            for feature in features:
                if feature['properties']['id'] == feature_id:
                    shape = make_shape(feature['geometry'])
                    if shape.type != exp_geom_type:
                        self.test.fail('Unexpected geometry type: %s'
                                       % shape.type)
                    break
            else:
                self.test.fail('No feature with id: %d found' % feature_id)


def memoize(f):
    result = {}

    def wrapped(*args, **kwargs):
        cache_key = tuple(args)
        if not result:
            result[cache_key] = f(*args, **kwargs)
        return result[cache_key]

    return wrapped


@memoize
def make_fixture_environment(regenerate):
    return FixtureEnvironment(regenerate)


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


class EmptyContext(object):

    def __enter__(self):
        return []

    def __exit__(self, type, value, traceback):
        pass


class RunTestInstance(object):

    def __init__(self, regenerate=False):
        self.regenerate = regenerate

    def setUp(self, test):
        self.env = make_fixture_environment(self.regenerate)
        self.test = test

    def load_fixtures(self, urls, clip, simplify):
        geojson_file = self.env.ensure_fixture_file(urls, clip, simplify)

        if environ.get('VERBOSE'):
            geojson_size = path_getsize(geojson_file)
            if geojson_size > (100 * 1024):
                import sys
                print>>sys.stderr, "WARNING: %s: GeoJSON fixture is " \
                    "very large, %d bytes." \
                    % (geojson_file, geojson_size)

        rows, rels = _load_fixtures([geojson_file])
        feature_fetcher = FixtureFeatureFetcher(rows, rels, self.env)
        self.assertions = Assertions(feature_fetcher, self.test)

    def generate_fixtures(self, objs):
        # features in rows will be dsl.Feature objects (which are namedtuples)
        # or tuples of (fid, shape, properties). the rels should be dicts with
        # keys for id, tags, way and rel offsets and "parts" array of IDs, as
        # if they had come from osm2pgsql's planet_osm_rels table.
        rows = []
        rels = []
        for o in objs:
            if isinstance(o, tuple):
                rows.append(o)
            elif isinstance(o, dict):
                rels.append(o)

        feature_fetcher = FixtureFeatureFetcher(rows, rels, self.env)
        self.assertions = Assertions(feature_fetcher, self.test)

    def assert_has_feature(self, z, x, y, layer, props):
        self.assertions.assert_has_feature(z, x, y, layer, props)

    def assert_no_matching_feature(self, z, x, y, layer, props):
        self.assertions.assert_no_matching_feature(z, x, y, layer, props)

    def assert_feature_geom_type(self, z, x, y, layer, feature_id,
                                 exp_geom_type):
        self.assertions.assert_feature_geom_type(
            z, x, y, layer, feature_id, exp_geom_type)

    def assert_less_than_n_features(self, z, x, y, layer, properties, n):
        self.assertions.assert_less_than_n_features(
            z, x, y, layer, properties, n)

    def features_in_tile_layer(self, z, x, y, layer):
        return self.assertions.ff.features_in_tile_layer(z, x, y, layer)

    def layers_in_tile(self, z, x, y):
        return self.assertions.ff.layers_in_tile(z, x, y)

    def features_in_mvt_layer(self, z, x, y, layer):
        return self.assertions.ff.features_in_mvt_layer(z, x, y, layer)

    def assertTrue(self, *args, **kwargs):
        self.test.assertTrue(*args, **kwargs)

    def assertFalse(self, *args, **kwargs):
        self.test.assertFalse(*args, **kwargs)


class DownloadOnlyInstance(object):

    def __init__(self, regenerate=False):
        self.regenerate = regenerate

    def setUp(self, test):
        self.env = make_fixture_environment(self.regenerate)
        self.test = test

    def load_fixtures(self, urls, clip, simplify):
        self.env.ensure_fixture_file(urls, clip, simplify)

    def generate_fixtures(self, objs):
        # there is nothing to download for a generated fixture.
        pass

    def assert_has_feature(self, z, x, y, layer, props):
        pass

    def assert_no_matching_feature(self, z, x, y, layer, props):
        pass

    def assert_feature_geom_type(self, z, x, y, layer, feature_id,
                                 exp_geom_type):
        pass

    def assert_less_than_n_features(self, z, x, y, layer, properties, n):
        pass

    def features_in_tile_layer(self, z, x, y, layer):
        return EmptyContext()

    def layers_in_tile(self, z, x, y):
        return EmptyContext()

    def features_in_mvt_layer(self, z, x, y, layer):
        return EmptyContext()

    def assertTrue(self, *args, **kwargs):
        pass

    def assertFalse(self, *args, **kwargs):
        pass


class CollectTilesInstance(object):

    def __init__(self):
        self.tiles = set()

    def _add_tile(self, z, x, y):
        self.tiles.add((z, x, y))

    def setUp(self, test):
        self.test = test

    def load_fixtures(self, urls, clip, simplify):
        pass

    def generate_fixtures(self, objs):
        pass

    def assert_has_feature(self, z, x, y, layer, props):
        self._add_tile(z, x, y)

    def assert_no_matching_feature(self, z, x, y, layer, props):
        self._add_tile(z, x, y)

    def assert_feature_geom_type(self, z, x, y, layer, feature_id,
                                 exp_geom_type):
        self._add_tile(z, x, y)

    def assert_less_than_n_features(self, z, x, y, layer, properties, n):
        self._add_tile(z, x, y)

    def features_in_tile_layer(self, z, x, y, layer):
        self._add_tile(z, x, y)
        return EmptyContext()

    def layers_in_tile(self, z, x, y):
        self._add_tile(z, x, y)
        return EmptyContext()

    def features_in_mvt_layer(self, z, x, y, layer):
        self._add_tile(z, x, y)
        return EmptyContext()

    def assertTrue(self, *args, **kwargs):
        pass

    def assertFalse(self, *args, **kwargs):
        pass


class FixtureTest(unittest.TestCase):

    def __init__(self, methodName='runTest', test_instance=None):
        super(FixtureTest, self).__init__(methodName)
        self.test_instance = test_instance

    def setUp(self):
        test = super(FixtureTest, self)
        self.test_instance.setUp(test)

    def load_fixtures(self, urls, clip=None, simplify=None):
        self.test_instance.load_fixtures(urls, clip, simplify)

    def generate_fixtures(self, *objs):
        self.test_instance.generate_fixtures(objs)

    def assert_has_feature(self, z, x, y, layer, props):
        self.test_instance.assert_has_feature(z, x, y, layer, props)

    def assert_no_matching_feature(self, z, x, y, layer, props):
        self.test_instance.assert_no_matching_feature(z, x, y, layer, props)

    def assert_feature_geom_type(self, z, x, y, layer, feature_id,
                                 exp_geom_type):
        self.test_instance.assert_feature_geom_type(
            z, x, y, layer, feature_id, exp_geom_type)

    def assert_less_than_n_features(self, z, x, y, layer, properties, n):
        self.test_instance.assert_less_than_n_features(
            z, x, y, layer, properties, n)

    def features_in_tile_layer(self, z, x, y, layer):
        return self.test_instance.features_in_tile_layer(z, x, y, layer)

    def layers_in_tile(self, z, x, y):
        return self.test_instance.layers_in_tile(z, x, y)

    def features_in_mvt_layer(self, z, x, y, layer):
        return self.test_instance.features_in_mvt_layer(z, x, y, layer)

    def assertTrue(self, *args, **kwargs):
        self.test_instance.assertTrue(*args, **kwargs)

    def assertFalse(self, *args, **kwargs):
        self.test_instance.assertFalse(*args, **kwargs)

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
                if isinstance(obj, OSMDataObject):
                    self.add_object(obj.typ, obj.fid)
                elif isinstance(obj, OverpassObject):
                    self.add_query(obj.raw_query)
                else:
                    raise Exception("Unknown data object type: %r" % (obj,))

            except Exception:
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
    import argparse
    import os

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filter', nargs='*', help='Only run tests which match at least one '
        'of these filters. Without any filters, all tests are run.')
    parser.add_argument(
        '--download-only', dest='download_only', action='store_const',
        const=True, default=False, help='Only download the fixtures, do not '
        'actually run the tests.')
    parser.add_argument(
        '--print-coords', dest='print_coords', action='store_const',
        const=True, default=False, help='Print out the coordinates used by '
        'the tests.')
    parser.add_argument(
        '--regenerate', action='store_const', const=True, default=False,
        help='Always regenerate the fixture, even if it exists in the cache.')
    args = parser.parse_args()

    test_stdout = sys.stderr
    if args.download_only:
        test_instance = DownloadOnlyInstance(regenerate=args.regenerate)
    elif args.print_coords:
        test_instance = CollectTilesInstance()
        test_stdout = open(os.devnull, 'w')
    else:
        test_instance = RunTestInstance(regenerate=args.regenerate)

    loader = unittest.TestLoader()
    suite = load_tests(loader, unittest.TestSuite(),
                       test_instance=test_instance)

    # convert filenames such as 'integration-test/1234-my-test.py' to the
    # equivalent module name. this can be helpful on the command line, when
    # using auto-complete to name the modules. to filter classes and
    # individual tests within the file, it's still necessary to use the
    # dotted module notation.
    filters = []
    for f in args.filter:
        if f.endswith('.py'):
            f = f[:-3]
        f = f.replace('/', '.')
        filters.append(f)

    tests = []
    if filters:
        for t in flatten_tests(suite):
            test_name = strclass(t.__class__) + "." + t._testMethodName
            for prefix in filters:
                if test_name.startswith(prefix):
                    tests.append(t)
                    break
    else:
        tests = flatten_tests(suite)

    suite = unittest.TestSuite()
    suite.addTests(tests)

    runner = unittest.TextTestRunner(stream=test_stdout)
    result = runner.run(suite)

    if not result.wasSuccessful():
        sys.exit(1)

    if isinstance(test_instance, CollectTilesInstance):
        for z, x, y in test_instance.tiles:
            print "%d/%d/%d" % (z, x, y)
