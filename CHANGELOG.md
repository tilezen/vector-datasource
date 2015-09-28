v0.3.0
------
* Source `national_park`, `protected_area` and other significant landuse boundaries from OpenStreetMap to generate AOI polygons and labels earlier starting at zoom 4 globally (was zoom 9). These features also gain  `protect_class` and `operator` properties.
* Add OSM roads and other features starting at zoom 8 (transition from Natural Earth data was zoom 9 in earlier releases). Natural Earth urban areas remain until zoom 9, though.
* Add water boundaries for low zooms (from Natural Earth), to match earlier `v0.2.0` work for OSM water boundaries at mid and high zooms.
* Landuse AOI polygons now include a `sort_key` hint from the server for easier client side styling. The `sort_key` is used server side to make the `landuse_kind` predictable on roads.
* Underground streams are now marked such with a additional `is_tunnel` property (zooms 11+)
* Temporarily reverted changes to administrative boundary lines in `v0.2.x` that dropped some boundary lines and their `kind` attributes. They'll be back soon, better than ever.
* Other minor bug fixes and optimizations.
* Requires: [tileserver v0.3.0](https://github.com/mapzen/tileserver/releases/tag/v0.3.0) and [tilequeue v0.3.0](https://github.com/mapzen/tilequeue/releases/tag/v0.3.0) and [TileStache v0.3.0](https://github.com/mapzen/TileStache/releases/tag/v0.3.0)

0.2.0
-----
* Stable
