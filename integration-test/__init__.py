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
from yaml import load as load_yaml
from contextlib import contextmanager


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


class OSMDataSource(object):

    def __init__(self):
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


class FixtureDataSources(object):

    def __init__(self):
        self.sources = [
            OSMDataSource(),
        ]

    def parse(self, url):
        p = urlparse.urlsplit(url)
        host = p.netloc.lower()
        if host.startswith('www.'):
            host = host[len('www.'):]

        for source in self.sources:
            if host in source.hosts:
                return source.parse(p.path)

        raise Exception("Unable to load fixtures for host %r, used "
                        "in request for %r." % (host, url))

    def download(self, urls, target_file):
        raise Exception("unimplemented")


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
        self.data_sources = FixtureDataSources()

    def output_calc_spec(self):
        output_calc_spec = {}
        for name, info in self.layer_functions.items():
            output_calc_spec[name] = info.props_fn
        return output_calc_spec

    def ensure_fixture_file(self, urls):
        canonical_urls = sorted(self._canonicalise(url) for url in urls)
        test_uuid = _hash(canonical_urls)
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
            self.data_sources.download(urls, geojson_file)

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


def _hash(urls):
    m = hashlib.sha256()
    for url in urls:
        m.update(url)
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


class OsmFixtureTest(unittest.TestCase):

    def setUp(self):
        self.env = FixtureEnvironment()

    def load_fixtures(self, urls):
        geojson_file = self.env.ensure_fixture_file(urls)
        feature_fetcher = FixtureFeatureFetcher([geojson_file], self.env)
        self.assertions = Assertions(feature_fetcher)

    def assert_has_feature(self, z, x, y, layer, props):
        self.assertions.assert_has_feature(z, x, y, layer, props)


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
