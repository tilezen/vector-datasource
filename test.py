import runpy
import requests
import json
import traceback
from os import walk
from os.path import join as path_join
import sys
from yaml import load as load_yaml
from appdirs import AppDirs
from contextlib import contextmanager


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
# Then you will be able to run `test.py local` and it will run against the local
# server defined above. You can define as many different servers as you like.
#
# Note that setting `use_all_layers` to `true` will cause the test to fetch all
# the layers, which may take more time than just the layers it needs. However,
# this makes it possible to run against the raw storage.
#
dirs = AppDirs("vector-datasource", "Mapzen")
config_file = path_join(dirs.user_config_dir, 'config.yaml')
config_data = load_yaml(open(config_file).read())
if len(sys.argv) < 2:
    print>>sys.stderr, "Usage: test.py <server name>. See test.py for more information."
    sys.exit(1)
config = config_data[sys.argv[1]]
config_url = config.get('url', None)
if config_url is None:
    print>>sys.stderr, "A URL is not configured for server %r, please check your config at %r." % (sys.argv[1], config_file)
    sys.exit(1)
config_all_layers = config.get('use_all_layers', False)


##
# Match properties, returning true if all of the expected properties can be
# matched with actual properties. There are 4 kinds of matches available:
#
#   {'key': None}     - The key must exist, but its value is not checked.
#   {'key': set(...)} - The key must exist and its value must be a member of the
#                       given set.
#   {'key': type}     - The key must exist and its value must be an instance of
#                       the given type.
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
            v = str(v)

        if exp_v is not None:
            if isinstance(exp_v, set):
                if v not in exp_v:
                    return False

            elif isinstance(exp_v, type):
                if not isinstance(v, exp_v):
                    return False

            elif v != exp_v:
                return False

        else:
            if v is None:
                return False

    return True


@contextmanager
def features_in_tile_layer(z, x, y, layer):
    url = config_url % {'layer': layer, 'z': z, 'x': x, 'y': y}
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


def assert_has_feature(z, x, y, layer, properties):
    with features_in_tile_layer(z, x, y, layer) as features:
        if len(features) == 0:
            raise Exception, "Did not find feature including properties " \
                "%r (because layer %r was empty)" % (properties, layer)

        for f in features:
            if match_properties(f['properties'], properties):
                return

        raise Exception, "Did not find feature including properties %r" \
            % properties


def assert_no_matching_feature(z, x, y, layer, properties):
    with features_in_tile_layer(z, x, y, layer) as features:
        for f in features:
            if match_properties(f['properties'], properties):
                raise Exception, "Found feature matching properties " \
                    "%r in layer %r, but was supposed to find none." \
                    % (properties, layer)


def run_test(f, log, idx, num_tests):
    fails = 0

    try:
        runpy.run_path(f, init_globals={
            'assert_has_feature': assert_has_feature,
            'assert_no_matching_feature': assert_no_matching_feature,
            'features_in_tile_layer': features_in_tile_layer
        })
        print "[%4d/%d] PASS: %r" % (idx, num_tests, f)
    except:
        print "[%4d/%d] FAIL: %r" % (idx, num_tests, f)
        fails = 1
        print>>log, "[%4d/%d] FAIL: %r" % (idx, num_tests, f)
        print>>log, traceback.format_exc()
        print>>log, ""

    return fails


fail_count = 0
with open('test.log', 'w') as log:
    tests = []

    if len(sys.argv) > 2:
        tests = sys.argv[2:len(sys.argv)]

    else:
        for (dirpath, dirs, files) in walk('test'):
            for f in files:
                if f.endswith('.py'):
                    tests.append(path_join(dirpath, f))

    num_tests = len(tests)
    for i, t in enumerate(sorted(tests)):
        fails = run_test(t, log, i + 1, num_tests)
        fail_count = fail_count + fails

if fail_count > 0:
    print "FAILED %d TESTS. For more information, see 'test.log'" % fail_count
    sys.exit(1)

else:
    print "PASSED ALL TESTS."
