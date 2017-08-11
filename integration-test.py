import runpy
import requests
import json
import traceback
from os import walk, environ, makedirs
from os.path import join as path_join
from os.path import exists as path_exists
from os.path import dirname
from os.path import abspath
from os.path import split as path_split
from os.path import splitext as path_splitext
import sys
from yaml import load as load_yaml
from appdirs import AppDirs
from contextlib import contextmanager
import re
import lxml.etree as ET
import time
from tilequeue.command import parse_layer_data
from vectordatasource.meta import find_yaml_path
from vectordatasource.meta.python import parse_layers
from vectordatasource.meta.python import output_kind
from vectordatasource.meta.python import make_function_name_props
from vectordatasource.meta.python import output_min_zoom
from vectordatasource.meta.python import make_function_name_min_zoom
from tilequeue.query import make_fixture_data_fetcher
from tilequeue.query.fixture import LayerInfo
import glob
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
from collections import namedtuple


# the Overpass server is used to download data about OSM elements. the
# environment allows us to override the default public Overpass server to take
# the load off it.
OVERPASS_SERVER = environ.get('OVERPASS_SERVER', 'overpass-api.de')

# the fixture cache stores generated GeoJSON fixtures. these can be somewhat
# expensive to generate (running `osm2pgsql` and so forth), so it seems worth
# caching them for everyone to reuse.
FIXTURE_CACHE = environ.get('FIXTURE_CACHE', 'http://localhost:8000')

##
# App configuration:
#
# Put a YAML file in the appropriate config directory (it's
# $HOME/.config/vector-datasource/config.yaml on Linux, but will be different on
# other systems) with keys for each config and values with the URL parameters,
# e.g:
#
#     ---
#     local:
#       url: http://localhost:8080/%(layer)s/%(z)d/%(x)d/%(y)d.json
#       use_all_layers: false
#
# Then you will be able to run `integration-test.py local` and it will run against the local
# server defined above. You can define as many different servers as you like.
#
# Note that setting `use_all_layers` to `true` will cause the test to fetch all
# the layers, which may take more time than just the layers it needs. However,
# this makes it possible to run against the raw storage.
#
def get_config():
    dirs = AppDirs("vector-datasource", "Mapzen")
    config_file = path_join(dirs.user_config_dir, 'config.yaml')
    config_url = environ.get('VECTOR_DATASOURCE_CONFIG_URL')
    config_all_layers = environ.get('VECTOR_DATASOURCE_CONFIG_ALL_LAYERS')

    print>>sys.stderr, "config_url=%r" % config_url
    if config_url is None and path_exists(config_file):
        config_data = load_yaml(open(config_file).read())
        if len(sys.argv) < 2:
            print>>sys.stderr, "Usage: integration-test.py <server name>. See integration-test.py for more information."
            sys.exit(1)
        config = config_data[sys.argv[1]]
        config_url = config.get('url', None)
        if config_url is None:
            print>>sys.stderr, "A URL is not configured for server %r, please check your config at %r." % (sys.argv[1], config_file)
            sys.exit(1)
        config_all_layers = config.get('use_all_layers', False)

    elif config_url is None:
        print>>sys.stderr, "A config URL can be set up using either a config file at %r, or using the environment variable VECTOR_DATASOURCE_CONFIG_URL. Neither of these was found." % config_file
        sys.exit(1)

    return (config_url, config_all_layers)


# yuck. global variables. TODO: refactor
config_url = None
config_all_layers = None


##
# Match properties, returning true if all of the expected properties can be
# matched with actual properties. There are 4 kinds of matches available:
#
#   {'key': None}     - The key must exist, but its value is not checked.
#   {'key': set(...)} - The key must exist and its value must be a member of the
#                       given set.
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


class GatewayTimeout(Exception):
    pass


def tile_url(z, x, y, layer):
    assert config_url, "Tile URL is not configured, is your config file set up?"
    request_layer = 'all' if config_all_layers else layer
    url = config_url % {'layer': request_layer, 'z': z, 'x': x, 'y': y}
    return url


def fetch_tile_http(url):
    r = requests.get(url)

    if r.status_code == 504:
        raise GatewayTimeout("Timeout for tile %r" % url)
    elif r.status_code != 200:
        raise Exception("Tile %r: error while fetching, status=%d"
                        % (url, r.status_code))

    return r


def fetch_tile_http_json(z, x, y, layer):
    url = tile_url(z, x, y, layer)
    r = fetch_tile_http(url)

    if r.headers['content-type'] != 'application/json':
        raise Exception("Tile %r: expected JSON, but content-type is %r"
                        % (url, r.headers['content-type']))

    return r


def fetch_tile_http_mvt(z, x, y, layer):
    url = tile_url(z, x, y, layer)
    url = url.replace(".json", ".mvt")
    r = fetch_tile_http(url)

    if r.headers['content-type'] != 'application/x-protobuf':
        raise Exception("Tile %r: expected application/x-protobuf, but "
                        "content-type is %r"
                        % (url, r.headers['content-type']))

    return r


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


class HttpFeatureFetcher(object):

    @contextmanager
    def features_in_tile_layer(self, z, x, y, layer):
        r = fetch_tile_http_json(z, x, y, layer)
        data = json.loads(r.text)

        if config_all_layers:
            layer_data = data.get(layer, None)
            if layer_data is not None:
                features = layer_data['features']
            else:
                features = []
        else:
            features = data['features']

        try:
            yield features

        except Exception as e:
            raise Exception, "Tile %r: %s" % (r.url, e.message), sys.exc_info()[2]

    @contextmanager
    def layers_in_tile(self, z, x, y):
        r = fetch_tile_http_json(z, x, y, 'all')
        data = json.loads(r.text)
        layers = data.keys()
        yield layers

    @contextmanager
    def features_in_mvt_layer(self, z, x, y, layer):
        r = fetch_tile_http_mvt(z, x, y, layer)

        from mapbox_vector_tile import decode as mvt_decode
        msg = mvt_decode(r.content)

        try:
            data = msg[layer]
            features = data['features']
            yield features

        except Exception as e:
            raise Exception, "Tile %r: %s" % (r.url, e.message), sys.exc_info()[2]


class Assertions(object):

    def __init__(self, feature_fetcher):
        self.ff = feature_fetcher

    def assert_has_feature(self, z, x, y, layer, properties):
        with self.ff.features_in_tile_layer(z, x, y, layer) as features:
            num_features, num_matching = count_matching(
                features, properties)

            if num_features == 0:
                raise Exception, "Did not find feature including properties " \
                    "%r (because layer %r was empty)" % (properties, layer)

            if num_matching == 0:
                closest, misses = closest_matching(features, properties)
                raise Exception, "Did not find feature including properties " \
                    "%r. The closest match was %r: missed %r." \
                    % (properties, closest['properties'], misses)


    def assert_at_least_n_features(self, z, x, y, layer, properties, n):
        """
        Downloads a tile and checks that it contains at least `n` features which
        match the given `properties`.
        """
        with self.ff.features_in_tile_layer(z, x, y, layer) as features:
            num_features, num_matching = count_matching(
                features, properties)

            if num_features < n:
                raise Exception, "Found fewer than %d features including " \
                    "properties %r (because layer %r had %d features)" % \
                    (n, properties, layer, num_features)

            if num_matching < n:
                raise Exception, "Did not find %d features including properties " \
                    "%r, found only %d" % (n, properties, num_matching)


    def assert_less_than_n_features(self, z, x, y, layer, properties, n):
        """
        Downloads a tile and checks that it contains less than `n` features which
        match the given `properties`.
        """
        with self.ff.features_in_tile_layer(z, x, y, layer) as features:
            num_features, num_matching = count_matching(
                features, properties)

            if num_matching >= n:
                raise Exception, "Did not find %d features including properties " \
                    "%r, found only %d" % (n, properties, num_matching)


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

                raise Exception, "Found feature matching properties %r in " \
                    "layer %r, but was supposed to find none. For example: " \
                    "%r" % (properties, layer, feature['properties'])


    def assert_feature_geom_type(self, z, x, y, layer, feature_id, exp_geom_type):
        with self.ff.features_in_tile_layer(z, x, y, layer) as features:
            for feature in features:
                if feature['properties']['id'] == feature_id:
                    shape = make_shape(feature['geometry'])
                    assert shape.type == exp_geom_type, \
                        'Unexpected geometry type: %s' % shape.type
                    break
            else:
                assert 0, 'No feature with id: %d found' % feature_id


def print_coord(z, x, y, *ignored):
    print '%d/%d/%d' % (z, x, y)


def fail(msg):
    raise Exception(msg)


def assertTrue(condition, msg=None):
    if msg is None:
        assert condition
    else:
        assert condition, msg


def noop(*args, **kwargs):
    pass


@contextmanager
def print_coord_with_context(z, x, y, *ignored):
    """
    This function only exists to allow tests which call `features_in_tile_layer`
    directly, and need to use it in a `with` context.
    """
    print_coord(z, x, y, *ignored)
    yield []


def make_function_table(feature_fetcher, assertions):
    function_table = {
        'assert_has_feature': assertions.assert_has_feature,
        'assert_no_matching_feature': assertions.assert_no_matching_feature,
        'assert_at_least_n_features': assertions.assert_at_least_n_features,
        'assert_less_than_n_features': assertions.assert_less_than_n_features,
        'features_in_tile_layer': feature_fetcher.features_in_tile_layer,
        'assert_feature_geom_type': assertions.assert_feature_geom_type,
        'layers_in_tile': feature_fetcher.layers_in_tile,
        'features_in_mvt_layer': feature_fetcher.features_in_mvt_layer,
        'fail': fail,
        'assertTrue': assertTrue,
    }
    return function_table


class TestAPI(object):

    def __init__(self, function_table):
        self.function_table = function_table

    def __getattribute__(self, name):
        assert name != 'function_table'
        function_table = object.__getattribute__(self, 'function_table')
        return function_table[name]


class NoLoader(object):
    """
    Shim class to make remote tests pass. Since these are against a remote
    server, there is nothing to load, and the API gets passed back as-is.
    """

    def __init__(self, api):
        self.api = api

    def load(self, urls):
        return self.api


class TestRunner(object):

    def __init__(self, mode):
        if mode == 'print':
            function_table = {
                'assert_has_feature': print_coord,
                'assert_no_matching_feature': print_coord,
                'assert_at_least_n_features': print_coord,
                'assert_less_than_n_features': print_coord,
                'features_in_tile_layer': print_coord_with_context,
                'assert_feature_geom_type': print_coord,
                'layers_in_tile': print_coord_with_context,
                'features_in_mvt_layer': print_coord_with_context,
                'fail': noop,
                'assertTrue': noop,
            }

        else:
            assert mode == 'test'
            self.feature_fetcher = HttpFeatureFetcher()
            self.assertions = Assertions(self.feature_fetcher)
            function_table = make_function_table(
                self.feature_fetcher, self.assertions)
        self.test_api = TestAPI(function_table)
        self.mode = mode

    def __call__(self, f, log, idx, num_tests):
        fails = 0

        try:
            fixtures = NoLoader(self.test_api)
            runpy.run_path(f, init_globals=dict(fixtures=fixtures))
            if self.mode == 'test':
                print "[%4d/%d] PASS: %r" % (idx, num_tests, f)
        except GatewayTimeout, e:
            if self.mode == 'test':
                fails = 1
                print "[%4d/%d] SLOW: %r" % (idx, num_tests, f)
                print>>log, "[%4d/%d] SLOW: %r" % (idx, num_tests, f)
                print>>log, "Gateway timeout: %s" % e.message
                print>>log, ""
        except:
            if self.mode == 'test':
                fails = 1
                print "[%4d/%d] FAIL: %r" % (idx, num_tests, f)
                print>>log, "[%4d/%d] FAIL: %r" % (idx, num_tests, f)
                print>>log, traceback.format_exc()
                print>>log, ""

        return fails


def make_runner(mode):
    return TestRunner(mode)


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
                # "200 OK is sent when the query has been successfully answered.
                # The payload of the response is the result data."
                # quote from http://overpass-api.de/command_line.html
                # so response is usable
                break

            if r.status_code not in (429, 504):
                # "429 Too Many Requests is sent if you pass multiple queries from one IP"
                # regularly happens with multiple sequential querries
                # "504 Gateway Timeout is sent if the server has already so much
                # load that the request cannot be executed. In most cases,
                # it is best to try again later"
                # quotes from http://overpass-api.de/command_line.html

                # in cases of 429 and 504 waiting and retrying is typically enough to get an expected response
                break

            print "%d code returned instead of overpass response - request will be repeated after %d seconds" % (r.status_code, wait_time_in_s)
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

    def test_function(self):
        def dump_data(f, log, idx, num_tests):
            fails = 0

            try:
                with open(f) as fh:
                    for line in fh:
                        m = self.pattern.search(line)
                        if m:
                            self.add_object(m.group(1), m.group(3))
                        else:
                            m = self.raw_pattern.search(line)
                            if m:
                                self.add_query(m.group(1).rstrip())
            except:
                print "[%4d/%d] FAIL: %r" % (idx, num_tests, f)
                fails = 1
                print>>log, "[%4d/%d] FAIL: %r" % (idx, num_tests, f)
                print>>log, traceback.format_exc()
                print>>log, ""

            return fails

        return dump_data


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
                            "not %r." % (url,))
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


class FixtureEnvironment(object):

    def __init__(self):
        src_directory = dirname(abspath(__file__))
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
            'Invalid query config path'
        with open(config_file) as query_cfg_fp:
            query_cfg = load_yaml(query_cfg_fp)
        all_layer_data, layer_data, post_process_data = parse_layer_data(
                query_cfg, buffer_cfg, dirname(config_file))

        yaml_path = find_yaml_path()
        layer_props = parse_layer_dict(yaml_path, output_kind, make_function_name_props)
        layer_min_zoom = parse_layer_dict(yaml_path, output_min_zoom, make_function_name_min_zoom)

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
            self.sources.download(urls, geojson_file)

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


class FixtureAPI(object):

    def __init__(self, env):
        self.env = env

    def load(self, urls):
        geojson_file = self.env.ensure_fixture_file(urls)
        feature_fetcher = FixtureFeatureFetcher([geojson_file], self.env)
        assertions = Assertions(feature_fetcher)
        function_table = make_function_table(feature_fetcher, assertions)
        test_api = TestAPI(function_table)
        return test_api


# Runs tests against local fixtures rather than going to the network.
class FixtureRunner(object):

    def __init__(self):
        self.env = FixtureEnvironment()
        self.fixture_api = FixtureAPI(self.env)

    def __call__(self, f, log, idx, num_tests):
        fails = 0

        try:
            runpy.run_path(f, init_globals=dict(fixtures=self.fixture_api))
            print "[%4d/%d] PASS: %r" % (idx, num_tests, f)

        except:
            fails = 1
            print "[%4d/%d] FAIL: %r" % (idx, num_tests, f)
            print>>log, "[%4d/%d] FAIL: %r" % (idx, num_tests, f)
            print>>log, traceback.format_exc()
            print>>log, ""

        return fails


data_dumper = None

if len(sys.argv) > 1 and sys.argv[1] == '-printcoords':
    tests = sys.argv[2:]
    mode = 'print'
    runner = make_runner(mode)
elif len(sys.argv) > 1 and sys.argv[1] == '-dumpdata':
    tests = sys.argv[2:]
    mode = 'dump'
    data_dumper = DataDumper()
    runner = data_dumper.test_function()
elif len(sys.argv) > 1 and sys.argv[1] == '-server':
    # delete the -server argument so that the get_config method sees the
    # arguments that it expects
    del sys.argv[1]
    config_url, config_all_layers = get_config()
    assert config_url, "Tile URL not configured, but is necessary for " \
        "running the tests. Please check your configuration file."
    tests = sys.argv[1:]
    mode = 'test'
    runner = make_runner(mode)
else:
    tests = sys.argv[1:]
    mode = 'test'
    runner = FixtureRunner()

fail_count = 0
with open('test.log', 'w') as log:

    if not tests:
        for (dirpath, dirs, files) in walk('integration-test'):
            for f in files:
                if f.endswith('.py'):
                    tests.append(path_join(dirpath, f))

    num_tests = len(tests)
    for i, t in enumerate(sorted(tests)):
        fails = runner(t, log, i + 1, num_tests)
        fail_count = fail_count + fails

if mode == 'test':
    if fail_count > 0:
        print "FAILED %d TESTS. For more information, see 'test.log'" % fail_count
        sys.exit(1)

    else:
        print "PASSED ALL TESTS."

if mode == 'dump':
    if fail_count > 0:
        print "FAILED %d TESTS, NOT DUMPING. For more information, " \
            "see 'test.log'" % fail_count
        sys.exit(1)

    with open('data.osc', 'w') as fh:
        data_dumper.download_to(fh)

    print "DATA DOWNLOADED OK."
