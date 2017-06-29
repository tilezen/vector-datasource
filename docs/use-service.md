# Get started with Mapzen Vector tiles

Mapzen Vector Tiles provide basemap coverage of the world in several vector tile formats. Tiles are available for zooms 0 through 16 and are available in several spatial data formats including MVT and GeoJSON. Learn more about the [various data formats](#available-tile-formats) offered.

## Get an API key

To use Mapzen's hosted vector tile service in a project, [obtain an API key from Mapzen](https://mapzen.com/documentation/overview/).

Once you have your Mapzen API key you'll need include it with Vector Tile requests as a [URL query string](https://en.wikipedia.org/wiki/Query_string) like:

```
?api_key=your-mapzen-api-key
```

# Use the Vector Tile service

Request a single tile with this URL pattern to get started:

```
https://tile.mapzen.com/mapzen/vector/v1/{layers}/{z}/{x}/{y}.{format}?api_key=your-mapzen-api-key
```

The [OpenStreetMap Wiki](http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames) has more information on this url scheme.

Here’s a sample tile in GeoJSON:

```
https://tile.mapzen.com/mapzen/vector/v1/all/16/19293/24641.json?api_key=your-mapzen-api-key
```

## Specify z, x, and y tile coordinates

Tiled geographic data enables fast fetching and display of "[slippy maps](https://en.wikipedia.org/wiki/Tiled_web_map)".

Tiling is the process of cutting raw map data from latitude and longitude geographic coordinates ([EPSG:4329](http://spatialreference.org/ref/epsg/4329/)) into a smaller data files using a file naming scheme based on zoom, x, and y in the Web Mercator ([EPSG:3857](http://spatialreference.org/ref/sr-org/6864/)) projection.

### Tile coordinate components

- `{z}` **zoom** ranges from 0 to 20 (but no new information is added after zoom 15)
- `{x}` **horizontal position**, counting from the "left", ranges from 0 to variable depending on the zoom
- `{y}` **vertical position**, counting from the "top", ranges from 0 to variable depending on the zoom

### Tile coordinate resources

- MapTiler.org's [Tiles à la Google Maps: Coordinates, Tile Bounds and Projection](http://www.maptiler.org/google-maps-coordinates-tile-bounds-projection/) has a great visualization that overlays tile coordinates on an interactive map
- GeoFabrik's [Tile Calculator](http://tools.geofabrik.de/calc/) charts number of tiles per zoom with a customizable bounding box


## Specify layers in the service

Layers to return can specified as `all`, or as one or more layer names separated by commas. Using the `all` layer is more performant.

`buildings`: https://tile.mapzen.com/mapzen/vector/v1/buildings/16/19293/24641.json?api_key=your-mapzen-api-key

`earth,landuse`: https://tile.mapzen.com/mapzen/vector/v1/earth,landuse/16/19293/24641.json?api_key=your-mapzen-api-key

### Layers in the service's response

When requesting a single layer, the response will be a single FeatureCollection, without any layer name prefix:

```json
{
   "type":"FeatureCollection",
   "features": [...],
   ...
}
```

When requesting multiple layers in GeoJSON, a dictionary of FeatureCollections will be returned, keyed by layer name:

```json
{
   "earth": {
      "type":"FeatureCollection",
      "features": [...],
      ...
   },
   "landuse": {
      "type":"FeatureCollection",
      "features": [...],
      ...
   }
}
```

## Available tile formats

Mapzen vector tiles can be returned in the following formats.

* [GeoJSON](http://geojson.org): use the `.json` extension. GeoJSON is easy to get started with, human-readable, and compatible with many tools
* [TopoJSON](https://github.com/mbostock/topojson): use the `.topojson` extension. TopoJSON is an optimized form of JSON that saves space by encoding topology and reducing replication of shared geometry.
* [Mapbox-format binary tiles](https://github.com/mapbox/vector-tile-spec): use the `.mvt` extension. This is a compact format using protocol buffers that is used for raster tile rendering in TileMill2 and vector rendering in MapboxGL

## Specify tile size

Optionally a 256 or 512 pixel tile size may be specified. When not specified, the size defaults to 256.

```
https://tile.mapzen.com/mapzen/vector/v1/{tilesize}/{layers}/{z}/{x}/{y}.{format}?api_key=your-mapzen-api-key
```

### 256 tile size (default)

The suggested max `{z}` value for 256 pixel tiles is zoom **16**. Requesting `{z}` coordinates up to 20 will return a smaller geographic area, but the tile will not include any additional data over the zoom 16 tile.

**Default:**

Including tile size in the path is not required. When not specified the default size of 256 is returned.

```
https://tile.mapzen.com/mapzen/vector/v1/{layers}/{z}/{x}/{y}.{format}?api_key=your-mapzen-api-key
```

**256 in path:**

```
https://tile.mapzen.com/mapzen/vector/v1/256/{layers}/{z}/{x}/{y}.{format}?api_key=your-mapzen-api-key
```

**Example Tangram YAML:**

```
sources:
    mapzen:
        type: MVT
        url:  https://tile.mapzen.com/mapzen/vector/v1/all/{z}/{x}/{y}.mvt
        url_params:
            api_key: your-mapzen-api-key
        max_zoom: 16
```

### 512 tile size

The suggested max `{z}` value for 512 pixel tiles is zoom **15**. Requesting `{z}` coordinates up to 20 will return a smaller geographic area, but the tile will not include any additional data over the zoom 15 tile.

**512 in path:**

```
https://tile.mapzen.com/mapzen/vector/v1/512/{layers}/{z}/{x}/{y}.{format}?api_key=your-mapzen-api-key
```

**Example Tangram YAML:**

```
sources:
    mapzen:
        type: MVT
        url:  https://tile.mapzen.com/mapzen/vector/v1/512/all/{z}/{x}/{y}.mvt
        url_params:
            api_key: your-mapzen-api-key
        max_zoom: 15
```


## Security

Mapzen Vector Tiles works over HTTPS, in addition to HTTP. You are strongly encouraged to use HTTPS for all requests, especially for queries involving potentially sensitive information.
