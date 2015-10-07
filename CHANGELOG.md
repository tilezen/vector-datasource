v0.4.0
------
* Fix regression in v0.3.0 where zooms 0 to zoom 8 country and region (state, province) features from OpenStreetMap were dropped from tiles.
* Greater diversity of label placements for POIs, landuse, and buildings result in more balanced selection of features visible at mid and high (neighborhood) zooms. The feature's minimum recommended visible zoom is now included as a property (eg: `min_zoom=10.7763`), useful for determining feature priority in client-side label collisions. Currently visibility should be calculated combined with area filters, we'll move that serverside in later releases.
* Add label positions for water bodies to the `water` layer noted as `label_position=yes`.
* Add label positions for buildings to the `buildings` layer noted as `label_position=yes`.
* Landuse label positions are now additionally available in the `landuse` layer directly, noted with `label_position=yes`.
* WARNING: The existing `landuse-labels` layer will be depreciated in a later release.
* Add `location` and `level` tags to buildings features in the `buildings` layer to determine if something is "location=underground" or `level=-1` (like BART stations in San Francisco).
* Administrative boundary line improvements are back in the `boundaries` layer: now based on OSM relations, includes localized left- and right-names, and adds `maritime_boundary=yes` when the boundary is out in the deep sea. Note that this is slightly different than the `maritime=yes` tag that comes directly from OSM as we're calculating it using a custom spatial mask that will be improved over time.
* Add `ferry` lines starting at zoom 8 to `road` layer.
* Add airport `runway` lines starting at zoom 9 in the `roads` layer. Can be combined with `landuse_kind` attributes to throttle visibility.

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
