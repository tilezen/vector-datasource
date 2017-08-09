# Mapzen Vector Tile Tests

## Code / Unit Tests

The `vector-datasource` project comes with some unit tests for the code in the `vectordatasource/` directory. These can be run with the command:

```
python setup.py test
```

From within the `vector-datasource` directory.

## Data / Integration Tests

The output of the tests can be confusing, as it may be interleaved with other output from other bits of code. An indicator of a successful run is the `PASSED ALL TESTS` message, which may be several lines before the end of the output, for example:

```
127.0.0.1 - - [07/Jul/2016 14:52:44] "GET /buildings/16/10493/22885.json HTTP/1.1" 200 -
127.0.0.1 - - [07/Jul/2016 14:52:45] "GET /landuse/16/10493/22885.json HTTP/1.1" 200 -
[ 104/104] PASS: 'integration-test/834-park-building.py'
PASSED ALL TESTS.
SUCCESS
scripts/setup_and_run_tests.sh: line 144:  9436 Hangup                  python scripts/test_server.py "${dbname}" "${USER}" "${test_server_port}"
=== Killing test server ===
scripts/setup_and_run_tests.sh: line 29: kill: (9436) - No such process
=== Dropping database "vector_datasource_8765" and cleaning up...
```

If the tests failed, with the message `FAILED n TESTS` for some value of `n`, then there will be a file `test.log` left in the `vector-datasource` directory containing more information on the failed tests.

### Running with local fixture data

The `vector-datasource` repository comes bundled with a set of fixture data in `integration-tests/geojson-fixtures/` for each test. Unless you are adding new tests, or want to test against a running tile server, then you generally will not need to alter any of these files. To run the tests:

```
python integration-test.py
```

Or individual tests may be run by listing them on the command line:

```
python integration-test.py integration-test/160-motorway-junctions.py
```

### Running against an existing tile server

The rest of this guide assumes that you have already set up `vector-datasource`, `tileserver` and `tilequeue` according to the [installation guide](https://github.com/tilezen/vector-datasource/wiki/Mapzen-Vector-Tile-Service), including steps to download and install all the necessary data.

You will need to install the [AppDirs](https://pypi.python.org/pypi/appdirs) Python package. First, set up a configuration file telling the test suite which server URL to use. The location of the configuration file will vary depending on your platform. To find out, either run the test suite and read the error message, or read the docs for [AppDirs](https://pypi.python.org/pypi/appdirs). This file should be a YAML dictionary of name to URL pattern pairs. An example config file is included as `test_config.example.yaml`. For example:

```yaml
---
local:
  url: http://localhost:8080/%(layer)s/%(z)d/%(x)d/%(y)d.json
  use_all_layers: false
```

Each top-level key, in this example `local` requires a `url` sub-key which gives a pattern for creating valid tile URLs. There are four variables available, `layer`, `z`, `x` and `y`, which indicate the layer within the tile, zoom level and x, y coordinate respectively. The result should be a valid GeoJSON file without layers. If the data source is not able to filter layers, for example if you're reading the layered-GeoJSON directly from storage (i.e: S3), and do not use the `layer` parameter then you should set the optional `use_all_layers` parameter to `true`. By default, if left unspecified, it's false.

For example, to read against a local server [proxying](https://github.com/mapzen/tile-hash-proxy) from storage such as S3, you might need a config something like this:

```yaml
---
proxy:
  url: http://localhost:8081/all/%(z)d/%(x)d/%(y)d.json
  use_all_layers: true
```

This defines a server called `local` which should be running on port 8080 of your local machine. This is suitable for testing against a locally-running instance of [tileserver](https://github.com/mapzen/tileserver). It also defines a server called `proxy` which should be running on port 8081 and proxies from raw, layered GeoJSON.

You can now run the tests, either against your local server:

```
python integration-test.py -server local
```

Or against the proxy:

```
python integration-test.py -server proxy
```

Note that you can configure as many servers as you like. Remember to include any necessary API keys as part of the URL. You can run subsets of the tests, or single tests, by listing them after the server name like this:

```
python test.py local -server test/160-motorway-junctions.py
```

Verbose test output is placed in a file called `test.log` in the current directory.

## Writing tests

Tests should either be unit tests or integration tests. The difference between the two is whether any data is required for them to work. The unit tests do not load any data and do not access the database. The integration tests load up a set of "fixture" data and require a database and a running tile server.

### Unit tests

Unit tests go in the `tests/` subdirectory. Each should be a Python file, and use the `unittest` package to make assertions about the behaviour of code in the `vectordatasource` package. Tests here generally test specific behaviour of transformation functions in isolation from other parts of the stack.

### Integration tests

Integration tests go in the `integration-tests/` subdirectory. Each should be a Python file, but uses a custom test harness which can be found in the `integration-test.py` file in the root directory of the project. Tests are generally named starting with the issue number of any issue which led to the test being written and a short description of the issue. It can he helpful if the description is the same as the git branch on which the issue is being addressed.

The integration test harness has functions such as:

* `assert_has_feature(z, x, y, layer, properties)` fails the test if the tile with coordinate `z/x/y` doesn't contain a feature matching `properties` in layer `layer`.
* `assert_at_least_n_features(z, x, y, layer, properties, n)` fails the test if the tile layer doesn't contain at least `n` matching features.
* `assert_less_than_n_features(z, x, y, layer, properties, n)` fails the test if the tile layer doesn't contain less than `n` matching features.
* `assert_no_matching_feature(z, x, y, layer, properties)` fails the test if the tile **does** contain a matching feature.
* `features_in_tile_layer(z, x, y, layer)` is a context manager, to be used in a `with` statement. This will iterate over all the features in the given `layer` in the tile `z/x/y`. This can be useful for writing more general tests than the assertions above allow.
* `layers_in_tile(z, x, y)` is a context manager, to be used in a `with` statement. This will iterate over all the layers in the tile `z/x/y`. This can be used to write very general tests about the existence or absence of features in certain layers.

There are two ways to add integration test data:

1. For data which comes from OpenStreetMap, add the URL of the object to the `integration-test/geojson-fixtures/<name of test>/urls.txt` file, prefixing it with a hash `#`. (TODO: move this back into the test file with `@decorator` syntax?)
2. For other data, add shapefiles under the `integration-test/fixtures/` subdirectory. (TODO: unify this with the OSM pathway.)

NOTE: z/x/y coordinates [are describing location and zoom level](https://mapzen.com/documentation/vector-tiles/use-service/#specify-z-x-and-y-tile-coordinates).

#### Adding OpenStreetMap data

The easiest way to add a fixture from OSM is to run `scripts/fixture.sh add <name of test> <URL>`, where the URL is the address of the OSM node, way or relation. After that, the geojson fixtures need to be updated by running `scripts/fixture.sh update <name of test>`. Note that, because this updates all the data for that test to the latest verions from OSM, it may cause other parts of the test to fail due to different data.

#### Adding shapefile fixture data

Any shapefiles under `integration-test/fixtures/` are loaded into the database by interpreting the subdirectory as the table name to load into. For example, `integration-test/fixtures/water_polygons/502-water-boundaries.shp` will be loaded into the `water_polygons` table.

Note that these are loaded in without any projection transform. The shapefiles should already be in EPSG:3857. Also, the shapefiles are loaded as-is, so it's important to make sure that the columns of the shapefile match the columns of the table they're loaded into - except for any `mz_*` columns which are added later.
