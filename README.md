Mapzen provides a free & open vector tile service for OpenStreetMap base layer data, with worldwide coverage updated daily, available in GeoJSON, TopoJSON, and binary data [formats](#formats).

Making OpenStreetMap and other open geo data more accessible to developers is central to Mapzen’s mission. We don’t want you to have to struggle with installing PostGIS, building osm2pgsql, or downloading a planet file to start playing with OSM data.

Vector tiles make real-time rendering possible by sending the underlying OSM geometry and tags directly to the client, whether that’s a browser or a native mobile app. Check out [Tangram, our work-in-progress WebGL rendering library](https://mapzen.com/tangram) for an example.

But we also believe that vector tiles will enable other, yet-to-be-invented types of OpenStreetMap-powered applications. Use this service to experiment with ideas!

Please note: this service is in active development and is subject to change! Questions, feedback, requests? [Let us know](https://github.com/mapzen/vector-datasource/issues).

# Getting Started
This service is freely available for all developers to use.

## API Key sign-up

First, you'll need to sign up for an account. You'll need a github account to continue, and Mapzen will read your email address from your github profile.

1. Navigate to https://mapzen.com/developers
1. Click on `continue with github`.
1. Click through to create your account.
1. Click on the `new key` button.
1. Name your project.

## Using the service

Now, just plug that api key into this URL pattern to get started:

`http://vector.mapzen.com/osm/{layers}/{z}/{x}/{y}.{format}?api_key={api_key}`

The [OpenStreetMap Wiki](http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames) has more information on this url scheme.

Here’s a sample tile in GeoJSON:

http://vector.mapzen.com/osm/all/16/19293/24641.json?api_key={api_key}

Layers to return can specified as `all`, or as one or more layer names separated by commas, e.g.:

`buildings`: http://vector.mapzen.com/osm/buildings/16/19293/24641.json?api_key={api_key}

`earth,landuse`: http://vector.mapzen.com/osm/earth,landuse/16/19293/24641.json?api_key={api_key}

## Multiple layers in GeoJSON
When requesting multiple layers in GeoJSON, a dictionary of FeatureCollections will be returned, keyed by layer name, e.g.:

```
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

When requesting a single layer, the response will simply be a single FeatureCollection, without any layer name prefix, e.g.:

```
{
   "type":"FeatureCollection",
   "features": [...],
   ...
}
```

The currently supported binary formats can handle single vs. multiple layers directly.

# Layers
Data is organized into several layers comprising the elements typically used for base map rendering. This is a simplified view of OSM data for easier consumption, with common tags often condensed into a single field as noted below.

## Water
Polygons representing oceans, riverbanks and lakes. Derived from a combination of the `waterway`, `natural`, and `landuse` tags. Includes coastline-derived water polygons from [openstreetmapdata.com](http://openstreetmapdata.com) at higher zoom levels, and [Natural Earth](http://naturalearthdata.com) polygons at lower zoom levels.

Layer name: `water`

Properties:
* `name`
* `kind`: one of `ocean`, `riverbank`, `dock`, `water`, `basin`, `reservoir`, `lake`, `playa`, `canal`, `dam`, `ditch`, `drain`, `river`, `stream`
* `area`: polygon area
* `source`: one of `naturalearthdata.com`, `openstreetmapdata.com`, `openstreetmap.org`

## Earth
Polygons representing landmass. Uses coastline-derived land polygons from [openstreetmapdata.com](http://openstreetmapdata.com).

Layer name: `earth`

Properties:
* `land`: `base`

## Landuse
Polygons from OpenStreetMap representing parks, forests, residential, commercial, industrial, cemetery, golf course, university, schools, sports and other areas. Includes OSM data at higher zoom levels, and [Natural Earth](http://naturalearthdata.com) polygons at lower zoom levels.

Layer name: `landuse`

Properties:
* `name`
* `kind`: combination of the `landuse`, `leisure`, `natural`, `highway`, `aeroway`, and `amenity` OSM tags, or `urban area` and `park or protected land` for Natural Earth areas.
* `area`: polygon area

The possible kind values can be:

`allotments`, `apron`, `cemetery`, `cinema`, `college`, `commercial`, `common`, `farm`, `farmland`, `farmyard`, `footway`, `forest`, `fuel`, `garden`, `glacier`, `golf_course`, `grass`, `hospital`, `industrial`, `land`, `library`, `meadow`, `nature_reserve`, `park`, `parking`, `pedestrian`, `pitch`, `place_of_worship`, `playground`, `quarry`, `railway`, `recreation_ground`, `residential`, `retail`, `runway`, `school`, `scrub`, `sports_centre`, `stadium`, `taxiway`, `theatre`, `university`, `village_green`, `wetland`, `wood`, `urban area`, `park or protected land`

## Landuse labels
Polygons from OpenStreetMap representing parks, forests, residential, commercial, industrial, cemetery, golf course, university, schools, sports and other areas. Includes OSM data at higher zoom levels, and [Natural Earth](http://naturalearthdata.com) polygons at lower zoom levels.

Layer name: `landuse_labels`

Properties:
* `name`
* `kind`: combination of the `landuse`, `leisure`, `natural`, `highway`, `aeroway`, and `amenity` OSM tags, or `urban area` and `park or protected land` for Natural Earth areas.
* `area`: polygon area

The possible kind values can be:

`allotments`, `apron`, `cemetery`, `cinema`, `college`, `commercial`, `common`, `farm`, `farmland`, `farmyard`, `footway`, `forest`, `fuel`, `garden`, `glacier`, `golf_course`, `grass`, `hospital`, `industrial`, `land`, `library`, `meadow`, `nature_reserve`, `park`, `parking`, `pedestrian`, `pitch`, `place_of_worship`, `playground`, `quarry`, `railway`, `recreation_ground`, `residential`, `retail`, `runway`, `school`, `scrub`, `sports_centre`, `stadium`, `taxiway`, `theatre`, `university`, `village_green`, `wetland`, `wood`, `urban area`, `park or protected land`

The geometry in this layer will be a point, and is meant to be used for labels.

## Roads
OpenStreetMap roads, highways, railways and paths matching the selection found in High Road. Sort them with `sort_key` to correctly represent layered overpasses, bridges and tunnels. Use the `kind` property for a classification of roads into `highway`, `major_road`, `minor_road`, `path`, `rail`

Layer name: `roads`

Properties:
* `name`
* `kind`: one of `highway`, `major_road`, `minor_road`, `rail`, `path`
* `highway`: the original OSM highway tag value
* `railway`: the original OSM railway tag value
* `is_bridge`: `yes` or `no`
* `is_tunnel`: `yes` or `no`
* `is_link`: `yes` or `no`
* `sort_key`: numeric value indicating correct rendering order

## Buildings
Polygons from OpenStreetMap representing building outlines. Includes the building footprint at lower zoom levels, and individual building:part geometries following the [Simple 3D Buildings](http://wiki.openstreetmap.org/wiki/Simple_3D_Buildings) tags at higher zoom levels.

Layer name: `buildings`

Properties:
* `name`
* `kind`: original value of the OSM `building` or `building:part` tag where it is a value other than `yes` (which is implicit)
* `height`: OSM building `height` tag (meters) where available, estimated from `building:levels` if present
* `min_height`: OSM building `min_height` tag (meters) where available, estimated from `building:min_levels` if present
* `addr_housenumber`: OSM `addr:housenumber` tag
* `addr_street`: OSM `addr:street` tag
* `roof_color`: OSM `roof:color` tag
* `roof_material`: OSM `roof:material` tag
* `roof_shape`: OSM `roof:shape` tag
* `roof_height`: OSM `roof:height` tag
* `roof_orientation`: OSM `roof:orientation` tag


## Points of Interest
Points of Interest from OpenStreetMap, with per-zoom selections similar to the primary [OSM.org Mapnik stylesheet](https://trac.openstreetmap.org/browser/subversion/applications/rendering/mapnik).

Layer name: `pois`

Properties:
* `name`
* `kind`: combination of the `aerialway`, `aeroway`, `amenity`, `barrier`, `highway`, `historic`, `leisure`, `lock`, `man_made`, `natural`, `power`, `railway`, `shop`, `tourism`, and `waterway` tags

## Places
Combination of OpenStreetMap `place` points, natural earth populated places, and administrative boundary polygons.

Layer name: `places`

Properties:
* `name`
* `kind`: the original value of the OSM `place` tag, or `boundary` for administrative boundaries
* `admin_level`: the original value of the OSM `admin_level` tag for administrative boundaries
* `scalerank`: scalerank value from natural earth populated places dataset
* `labelrank`: labelrank value from natural earth populated places dataset
* `population`: population value from natural earth populated places dataset

# Formats<a href="formats"></a>
Tiles can be returned in the following formats.

* [GeoJSON](http://geojson.org)
   * Easiest to get started with, human readable & compatible with many tools
   * Use the `.json` extension
* [TopoJSON](https://github.com/mbostock/topojson)
   * An optimized form of JSON that saves space by encoding topology, reducing replication of shared geometry
   * Use the `.topojson` extension
* [Mapbox-format binary tiles](https://github.com/mapbox/vector-tile-spec)
   * A compact format using protocol buffers
   * Used for raster tile rendering in TileMill 2 & vector rendering in Mapbox GL
   * Use the `.mvt` extension
* [OpenScienceMap-format binary tiles](https://github.com/opensciencemap/vtm)
   * A compact format using protocol buffers
   * Used in the [OpenScienceMap](http://www.opensciencemap.org/) vector rendering library for Android
   * Use the `.vtm` extension

# How it Works
Vector tiles are served by clipping geometries to the tile bounding box, and then simplified to match the zoom level (to avoid unnecessary complexity at lower zoom levels). These geometries and features are also further processed to facilitate styling.

This is based on the work of [Michal Migurski](http://mike.teczno.com/), and extends his [OSM.US-hosted vector tile service](http://openstreetmap.us/~migurski/vector-datasource/) with additional data and format support.

If you are interested in setting up your own version of this service, look at our [installation instructions](https://github.com/mapzen/vector-datasource/wiki/Mapzen-Vector-Tile-Service), or you can also try this [Vagrant VM](https://github.com/mapzen/vagrant-tiles), which will additionally set up other tile components as well. You may also be interested in our [Metro Extracts](https://mapzen.com/metro-extracts), which provide weekly, city-sized chunks of OSM data in several formats for over 200 cities.

# How to Display Vector Tiles
You can use Mapzen’s vector tile service with a variety of browser-based rendering software packages. According to the syntax of the library you are using, you need to specify the URL to the Mapzen vector tile service, the layers that you want to draw on the map, and styling information about how to draw the features. 

## Tangram
[Tangram](https://mapzen.com/projects/tangram) is a WebGL mapping engine designed for real-time rendering of 2D and 3D maps from vector tiles. More details are available on the [Tangram home  page](https://mapzen.com/projects/tangram) as well as [the Tangram Github wiki](https://github.com/tangrams/tangram/wiki).

## D3
D3 is a JavaScript visualization library that you can use to render to SVG format in your browser. [Mike Bostock](http://bl.ocks.org/mbostock) adapated d3.geo.til [to show OpenStreetMap vector tiles](http://bl.ocks.org/mbostock/5593150). To use D3 with Mapzen vector tiles, use either GeoJSON or TopoJSON format, which have similar syntax, or the Mapbox Vector Tiles format. The layer styling can be inline or referenced from a CSS file. 

With D3, specifying the URL to the Mapzen vector tile service takes the form of 

`d3.json("https://vector.mapzen.com/osm/{layers}/{zoom}/{x}/{y}.{format}", function(error, json)` 

where .{format} can be .json for GeoJSON, .topojson for TopoJSON, or .mvt for Mapbox Vector Tiles.

D3 uses a different zoom level than the maptiles you may be used to. Default zoom for a map is set using `d3.geo.mercator` and `.scale()` – in this example, 21 is roughly equivalent to z13.

```var projection = d3.geo.mercator()
    .scale((1 << 21) / 2 / Math.PI)```
    
Upper and lower zoom levels are set using `d3.behavior.zoom()` and `.scaleExtent()` – in this example, the scale extent of 12 to 25 is roughly z4-z5 to z17:

```.scaleExtent([1 << 12, 1 << 25])```

See also the [D3 documentation on zoom behavior](https://github.com/mbostock/d3/wiki/Zoom-Behavior).

See the examples at https://github.com/mapzen/d3-vector-tiles for more information. This repository has samples using each input format (see geojson.html, topojson.html, or index.html for .mvt).

## MapboxGL
[MapboxGL](https://www.mapbox.com/mapbox-gl/) is a JavaScript library used to render the Mapbox Vector Tiles protocol buffer format through OpenGL on both web and native platforms. 

To specify Mapzen vector tile server as the source, use the following URL string, where .mvt is the file format.
```  "sources": {
    "osm": {
      "type": "vector",
      "tiles": ["https://vector.mapzen.com/osm/{layers}/{zoom}/{x}/{y}.mvt"]```

See https://github.com/mapzen/mapboxgl-vector-tiles for a sample map of Mapzen vector tiles displayed in MapboxGL.

## Hoverboard
[Hoverboard](https://libraries.io/bower/hoverboard/v1.0.1) is a JavaScript library created by Tristan Davies to draw vector tiles as a Leaflet tile layer on the <canvas> HTML element of a webpage. Hoverboard supports the Mapzen vector tiles in GeoJSON, TopoJSON, or Mapbox Vector Tiles format. 

```window.xyz_tile_source_url = 'https://vector.mapzen.com/osm/{layers}/{zoom}/{x}/{y}.json';```

See https://github.com/mapzen/hoverboard for more information. This repository has samples using each input format (see geojson.html, topojson.html, or index.html for .mvt). The Leaflet tile layer is defined in example.js, where you specify the Mapzen vector tile layers you want to render and the colors and symbols used to draw them.

