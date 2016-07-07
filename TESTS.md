# Mapzen Vector Tile Tests

## Code / Unit Tests

The `vector-datasource` project comes with some unit tests for the code in the `vectordatasource/` directory. These can be run with the command:

```
python setup.py test
```

From within the `vector-datasource` directory.

## Data / Integration Tests

There is also suite of integration tests which can be run in one of two ways:

* Against an existing tile server, which can be local or remote. This is useful for testing against a version of `tileserver` or `tilequeue` which has been locally modified, or against a freshly-deployed server to check its correct operation.
* Against a "testing" server which contains the minimum amount of data to run the tests. This is useful in a continuous integration environment, or for running local checks while developing `vector-datasource`.

The tests run against data from all over the world, which can be an onerous amount of data to load on a local machine, and is probably too much for a laptop. For these situations, it can be much easier to use the "testing server" method to download only the data which is necessary.

### Running against a testing server

This is the recommended method for running local tests on a laptop or desktop machine. It parses annotations in the tests to find the elements required for the test to complete, and downloads these from an [Overpass API](http://wiki.openstreetmap.org/wiki/Overpass_API) server.

Before running the tests, make sure that you have installed `tileserver` and `tilequeue` either from git or by running `pip install -r requirements.txt`, and that you have the programs `osm2pgsql` and `shp2pgsql` installed. You will need a recent version of `osm2pgsql`, for example 0.91.0, which may not be available from your operating systems default packages, especially on Debian or Ubuntu systems. In the case that you can't get a recent version from default packages, you may need to install [from source](https://github.com/openstreetmap/osm2pgsql) or [other package sources](https://launchpad.net/~ubuntugis/+archive/ubuntu/ppa).

Note that the tests require a _lot_ of data, and can result in errors like these from public Overpass instances:

```
RuntimeError: Unable to fetch data from Overpass: 429
```

This error code means that the Overpass server has rejected a request because too much has been downloaded. If you get these errors, then you may want to run your own Overpass instance to avoid stressing the public instances.

To run the tests, from within `vector-datasource/`:

```
./scripts/setup_and_run_tests.sh
```

This will create a new database, download data and fill the database, run the tests against it and finally destroy the database. Downloading the data and setting up the database can take some time, so if you don't want the database to be destroyed, set the `$NOCLEANUP` environment variable, for example:

```
NOCLEANUP=1 ./scripts/setup_and_run_tests.sh
```

If you want to use a specific Overpass server rather than the default public instance, set the environment variable `$OVERPASS_SERVER` to its hostname. For example:

```
OVERPASS_SERVER=localhost ./scripts/setup_and_run_tests.sh
```

The output of the tests can be confusing, as it is interleaved with the output of the test tile server. An indicator of a successful run is the `PASSED ALL TESTS` message, which may be several lines before the end of the output, for example:

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

### Re-running against a testing server

If you originally ran with `$NOCLEANUP` then you can re-run the tests against that database as long as you know the database name which was created. This should be available in the logs, or can be found by listing the databases in postgresql - it will have a name like `vector_datasource_XXXX`.

In one window, or a background `screen`, run the tests server:

```
python scripts/test_server.py vector_datasource_15651 `whoami` test_server.port
```

Replacing `vector_datasource_15651` with the name of your local database. In another window, run:

```
VECTOR_DATASOURCE_CONFIG_URL="http://localhost:`cat test_server.port`/%(layer)s/%(z)d/%(x)d/%(y)d.json" python integration-test.py
```

This will re-run the tests, but without any data updates. If you changed the tests and need to download new data then you may need to re-run the whole download process.

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
python integration-test.py local
```

Or against the proxy:

```
python integration-test.py proxy
```

Note that you can configure as many servers as you like. Remember to include any necessary API keys as part of the URL. You can run subsets of the tests, or single tests, by listing them after the server name like this:

```
python test.py local test/160-motorway-junctions.py
```

Verbose test output is placed in a file called `test.log` in the current directory.