import runpy
import requests
import json
import traceback
from os import walk, environ
from os.path import join as path_join
from os.path import exists as path_exists
import sys
from yaml import load as load_yaml
from appdirs import AppDirs
from contextlib import contextmanager
import shapely.geometry
import re
import lxml.etree as ET

OVERPASS_SERVER = environ.get('OVERPASS_SERVER', 'overpass-api.de')

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


@contextmanager
def features_in_tile_layer(z, x, y, layer):
    assert config_url, "Tile URL is not configured, is your config file set up?"
    request_layer = 'all' if config_all_layers else layer
    url = config_url % {'layer': request_layer, 'z': z, 'x': x, 'y': y}
    r = requests.get(url)

    if r.status_code != 200:
        raise Exception("Tile %r: error while fetching, status=%d"
                        % (url, r.status_code))

    if r.headers['content-type'] != 'application/json':
        raise Exception("Tile %r: expected JSON, but content-type is %r"
                        % (url, r.headers['content-type']))

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
        raise Exception, "Tile %r: %s" % (url, e.message), sys.exc_info()[2]


@contextmanager
def layers_in_tile(z, x, y):
    assert config_url, "Tile URL is not configured, is your config file set up?"
    url = config_url % {'layer': 'all', 'z': z, 'x': x, 'y': y}
    r = requests.get(url)

    if r.status_code != 200:
        raise Exception("Tile %r: error while fetching, status=%d"
                        % (url, r.status_code))

    if r.headers['content-type'] != 'application/json':
        raise Exception("Tile %r: expected JSON, but content-type is %r"
                        % (url, r.headers['content-type']))

    data = json.loads(r.text)
    layers = data.keys()
    yield layers


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


def assert_has_feature(z, x, y, layer, properties):
    with features_in_tile_layer(z, x, y, layer) as features:
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


def assert_at_least_n_features(z, x, y, layer, properties, n):
    """
    Downloads a tile and checks that it contains at least `n` features which
    match the given `properties`.
    """
    with features_in_tile_layer(z, x, y, layer) as features:
        num_features, num_matching = count_matching(
            features, properties)

        if num_features < n:
            raise Exception, "Found fewer than %d features including " \
                "properties %r (because layer %r had %d features)" % \
                (n, properties, layer, num_features)

        if num_matching < n:
            raise Exception, "Did not find %d features including properties " \
                "%r, found only %d" % (n, properties, num_matching)


def assert_no_matching_feature(z, x, y, layer, properties):
    with features_in_tile_layer(z, x, y, layer) as features:
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


def assert_feature_geom_type(z, x, y, layer, feature_id, exp_geom_type):
    with features_in_tile_layer(z, x, y, layer) as features:
        for feature in features:
            if feature['properties']['id'] == feature_id:
                shape = shapely.geometry.shape(feature['geometry'])
                assert shape.type == exp_geom_type, \
                    'Unexpected geometry type: %s' % shape.type
                break
        else:
            assert 0, 'No feature with id: %d found' % feature_id


def print_coord(z, x, y, *ignored):
    print '%d/%d/%d' % (z, x, y)


@contextmanager
def print_coord_with_context(z, x, y, *ignored):
    """
    This function only exists to allow tests which call `features_in_tile_layer`
    directly, and need to use it in a `with` context.
    """
    print_coord(z, x, y, *ignored)
    yield []


def print_coords(f, log, idx, num_tests):
    try:
        runpy.run_path(f, init_globals={
            'assert_has_feature': print_coord,
            'assert_no_matching_feature': print_coord,
            'features_in_tile_layer': print_coord_with_context,
            'assert_feature_geom_type': print_coord,
            'layers_in_tile': print_coord_with_context,
        })
    except:
        pass
    return 0


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

    def add_query(self, query):
        r = requests.get("http://%s/api/interpreter" % OVERPASS_SERVER,
                         params=dict(data=query))

        if r.status_code != 200:
            raise RuntimeError("Unable to fetch data from Overpass: %r"
                               % r.status_code)

        if r.headers['content-type'] != 'application/osm3s+xml':
            raise RuntimeError("Expected XML, but got %r"
                               % r.headers['content-type'])

        root = ET.fromstring(r.content)
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


def run_test(f, log, idx, num_tests):
    fails = 0

    try:
        runpy.run_path(f, init_globals={
            'assert_has_feature': assert_has_feature,
            'assert_no_matching_feature': assert_no_matching_feature,
            'features_in_tile_layer': features_in_tile_layer,
            'assert_feature_geom_type': assert_feature_geom_type,
            'layers_in_tile': layers_in_tile,
        })
        print "[%4d/%d] PASS: %r" % (idx, num_tests, f)
    except:
        print "[%4d/%d] FAIL: %r" % (idx, num_tests, f)
        fails = 1
        print>>log, "[%4d/%d] FAIL: %r" % (idx, num_tests, f)
        print>>log, traceback.format_exc()
        print>>log, ""

    return fails


data_dumper = None

if len(sys.argv) > 1 and sys.argv[1] == '-printcoords':
    tests = sys.argv[2:]
    mode = 'print'
    runner = print_coords
elif len(sys.argv) > 1 and sys.argv[1] == '-dumpdata':
    tests = sys.argv[2:]
    mode = 'dump'
    data_dumper = DataDumper()
    runner = data_dumper.test_function()
else:
    config_url, config_all_layers = get_config()
    assert config_url, "Tile URL not configured, but is necessary for " \
        "running the tests. Please check your configuration file."
    tests = sys.argv[2:]
    mode = 'test'
    runner = run_test

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
