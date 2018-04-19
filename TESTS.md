# Tilezen Vector Tile Tests

## Code / Unit Tests

The `vector-datasource` project comes with some unit tests for the code in the `vectordatasource/` directory. These can be run with the command:

```
python setup.py test
```

From within the `vector-datasource` directory.

## Data / Integration Tests

The integration tests use the `unittest` framework, and should end with either a message saying `OK` or one saying `FAILED (failures=N)` with `N` being how many tests failed. For each failed test, there should be a stack trace indicating which assertion failed and the test file and function that it was called from.

### Running with local fixture data

The `vector-datasource` project maintains a set of fixture data which will be downloaded as part of the test and cached locally in your `~/.cache/vector-datasource` directory. If you need to clear the cache for any reason, it's safe to completely delete that directory.

Run the integration test suite with:

```
python integration-test/__init__.py
```

Or individual tests may be run by listing them on the command line:

```
python integration-test/__init__.py integration-test/160-motorway-junctions.py
```

Individual test functions can be run by specifying the function or module on the command line. Note that this is not a path, so the module separator '.' is used rather than the path separator '/'!

```
python integration-test/__init__.py integration-test.160-motorway-junctions.MotorwayJunctions.test_motorway_junctions
```

This can be extremely useful when debugging a unit test with `pdb`, as running a single unit test function can help you pinpoint the failure without having to step through a lot of irrelevant preamble.

### Running against an existing tile server

TODO! This hasn't been (re-)implemented yet for the new tests!

## Writing tests

Tests should either be unit tests or integration tests. The difference between the two is whether any data is required for them to work. The unit tests do not load any data and do not access the database. The integration tests load up a set of "fixture" data which they use to mock the database.

### Unit tests

Unit tests go in the `tests/` subdirectory. Each should be a Python file, and use the `unittest` package to make assertions about the behaviour of code in the `vectordatasource` package. Tests here generally test specific behaviour of transformation functions in isolation from other parts of the stack.

### Integration tests

Integration tests go in the `integration-tests/` subdirectory. Each should be a Python file, but uses a custom test harness which can be found in the `integration-test/__init__.py` file. Tests are generally named starting with the issue number of any issue which led to the test being written and a short description of the issue. It can he helpful if the description is the same as the git branch on which the issue is being addressed.

The integration test defines a `unittest` compatible class called `FixtureTest` which provides useful tile-related test functions such as:

* `assert_has_feature(z, x, y, layer, properties)` fails the test if the tile with coordinate `z/x/y` doesn't contain a feature matching `properties` in layer `layer`.
* `assert_at_least_n_features(z, x, y, layer, properties, n)` fails the test if the tile layer doesn't contain at least `n` matching features.
* `assert_less_than_n_features(z, x, y, layer, properties, n)` fails the test if the tile layer doesn't contain less than `n` matching features.
* `assert_no_matching_feature(z, x, y, layer, properties)` fails the test if the tile **does** contain a matching feature.
* `features_in_tile_layer(z, x, y, layer)` is a context manager, to be used in a `with` statement. This will iterate over all the features in the given `layer` in the tile `z/x/y`. This can be useful for writing more general tests than the assertions above allow.
* `layers_in_tile(z, x, y)` is a context manager, to be used in a `with` statement. This will iterate over all the layers in the tile `z/x/y`. This can be used to write very general tests about the existence or absence of features in certain layers.

Fixture data should be loaded in each test that needs it; either once for the class in the `setUp()` method (but remember to call `super.setUp()` too!) or for each test individually. The function to call is `load_fixtures([urls])`, where each URL defines an element to load. Several schemes are supported at the moment:

1. `https://www.openstreetmap.org/...` to load OSM nodes, ways and relations.
2. `http://overpass-api.de/api/interpreter?data=...` to make a query against Overpass API.
3. `https://whosonfirst.mapzen.com/data/...` to load data from WhosOnFirst.
4. `file://integration-test/fixtures/...` to load data from a bundled shapefile. This is useful to handle fixtures from Natural Earth data, or pre-packaged shapefiles from OpenStreetMapData.

Additionally, optional arguments can be provided to `load_fixtures`:

* `clip=...` applies a clipping mask to the fixture data, keeping only the data which is within the Shapely shape passed as the argument. There is a utility function `tile_bbox(z, x, y)` so that it's easy to clip to a tile bounding box. Clipping can be very useful when working with relations, as they can be very large and this makes the fixtures large and processing slower. If it is possible to make the test pass with a clipped relation fixture, then please use the clip option.
* `simplify=...` generalises the geometry to the tolerance given as the argument. This is also useful for reducing the size of fixtures and the complexity of the processing when the test does not need the geometry to be accurate.

NOTE: z/x/y coordinates [are describing location and zoom level](https://mapzen.com/documentation/vector-tiles/use-service/#specify-z-x-and-y-tile-coordinates).
