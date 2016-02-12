# Use the vector tile service

To use the vector tile service, you first need to obtain an API key from Mapzen. Sign in at https://mapzen.com/developers to create and manage your API keys.

Now, just append your API key into this URL pattern to get started, where `vector-tiles-xxxxxxx` represents your key.

`http://vector.mapzen.com/osm/{layers}/{z}/{x}/{y}.{format}?api_key=vector-tiles-xxxxxxx`

The [OpenStreetMap Wiki](http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames) has more information on this url scheme.

Here’s a sample tile in GeoJSON:

`http://vector.mapzen.com/osm/all/16/19293/24641.json?api_key=vector-tiles-xxxxxxx`

## Specify layers in the service

Layers to return can specified as `all`, or as one or more layer names separated by commas.

`buildings`: http://vector.mapzen.com/osm/buildings/16/19293/24641.json?api_key=vector-tiles-xxxxxxx

`earth,landuse`: http://vector.mapzen.com/osm/earth,landuse/16/19293/24641.json?api_key=vector-tiles-xxxxxxx

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
* [OpenScienceMap-format binary tiles](https://github.com/opensciencemap/vtm): use the `.vtm` extension. This is a compact format using protocol buffers that is used in the [OpenScienceMap](http://www.opensciencemap.org/) vector rendering library for Android.
