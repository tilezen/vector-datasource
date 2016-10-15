# Use the vector tile service

To use the vector tile service, you first need to obtain an API key from Mapzen. Sign in at https://mapzen.com/developers to create and manage your API keys.

Now, just append your API key into this URL pattern to get started, where `mapzen-xxxxxxx` represents your key.

`https://tile.mapzen.com/mapzen/vector/v1/{layers}/{z}/{x}/{y}.{format}`

The [OpenStreetMap Wiki](http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames) has more information on this url scheme.

Here’s a sample tile in GeoJSON:

`https://tile.mapzen.com/mapzen/vector/v1/all/16/19293/24641.json`

## Specify layers in the service

Layers to return can specified as `all`, or as one or more layer names separated by commas. The `all` layer is more performant.


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
