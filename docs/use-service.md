# Use the vector tile service

Request a single tile with this URL pattern to get started:

`https://tile.mapzen.com/mapzen/vector/v1/{layers}/{z}/{x}/{y}.{format}`

To learn more about the URL pattern or if you're new to a web tile service, read a quick [overview of what tiles are](what-are-tiles.md).

Here’s a sample tile in GeoJSON:

`https://tile.mapzen.com/mapzen/vector/v1/all/16/19293/24641.json`

To use the vector tile service in a project, [obtain an API key from Mapzen](https://mapzen.com/documentation/overview/).

## Specify layers in the service

Layers to return can specified as `all`, or as one or more layer names separated by commas. Using the `all` layer is more performant.


`buildings`: https://tile.mapzen.com/mapzen/vector/v1/buildings/16/19293/24641.json

`earth,landuse`: https://tile.mapzen.com/mapzen/vector/v1/earth,landuse/16/19293/24641.json

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

## Security

Mapzen Vector Tiles works over HTTPS, in addition to HTTP. You are strongly encouraged to use HTTPS for all requests, especially for queries involving potentially sensitive information.
