# Mapzen Vector Tile Tests

There is a suite of tests which can be run against a tile server. You will need to install the [AppDirs](https://pypi.python.org/pypi/appdirs) Python package. First, set up a configuration file telling the test suite which server URL to use. The location of the configuration file will vary depending on your platform. To find out, either run the test suite and read the error message, or read the docs for [AppDirs](https://pypi.python.org/pypi/appdirs). This file should be a YAML dictionary of name to URL pattern pairs. An example config file is included as `test_config.example.yaml`. For example:

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
python test.py local
```

Or against the proxy:

```
python test.py proxy
```

Note that you can configure as many servers as you like. Remember to include any necessary API keys as part of the URL. You can run subsets of the tests, or single tests, by listing them after the server name like this:

```
python test.py local test/160-motorway-junctions.py
```

Verbose test output is placed in a file called `test.log` in the current directory.