v0.5.3
------
* **Release date**: 2015-12-07. _Live in prod: 2015-12-07._
* Fix bug where school points were not being exported as POIs. [Ticket](https://github.com/mapzen/vector-datasource/issues/417).
* **Requires:** [tileserver v0.4.1](https://github.com/mapzen/tileserver/releases/tag/v0.4.2) and [tilequeue v0.5.1](https://github.com/mapzen/tilequeue/releases/tag/v0.5.1) and [TileStache v0.5.1](https://github.com/mapzen/TileStache/releases/tag/v0.5.1)

v0.5.2
------
* **Release date**: 2015-12-04. _Live in prod: 2015-12-04._
* Make hospital POIs visible at zoom 14 by default, instead of 15. [Ticket](https://github.com/mapzen/vector-datasource/issues/420).
* Fix regression which dropped parking aisles. [Ticket](https://github.com/mapzen/vector-datasource/issues/412).
* **Requires:** [tileserver v0.4.1](https://github.com/mapzen/tileserver/releases/tag/v0.4.2) and [tilequeue v0.5.1](https://github.com/mapzen/tilequeue/releases/tag/v0.5.1) and [TileStache v0.5.1](https://github.com/mapzen/TileStache/releases/tag/v0.5.1)

v0.5.1
------
* **Release date**: 2015-11-24. _Live in prod: 2015-11-24._
* Update landuse query to use existing index
* **Requires:** [tileserver v0.4.1](https://github.com/mapzen/tileserver/releases/tag/v0.4.2) and [tilequeue v0.5.1](https://github.com/mapzen/tilequeue/releases/tag/v0.5.1) and [TileStache v0.5.1](https://github.com/mapzen/TileStache/releases/tag/v0.5.1)

v0.5.0
------
* **Release date**: 2015-11-13. _Live in prod: 2015-11-20._
* Filter out duplicate POIs in `pois`, `landuse`, and `buildings` layers, preferring poi layer features. Includes density filter.
* Add neighbourhoods (and macrohoods and microhoods) from Who's On First in the `places` layer. New properties: `min_zoom`, `max_zoom`, `kind_tile_rank`, `is_landuse_aoi`.
* Remove neighbourhoods from OpenStreetMap.
* Add `kind_tile_rank` to `kind=station` features to enable filtering out of less important transit stations at low zooms (to reduce crowding). Weights stations that are shown at lower zoom levels by lines going through them. Lower numbers = more important.
* Stop duplicating building footprints into the landuse layer, and exclude building=no features. Include all building properties at all zooms (was limited to high zooms).
* Use addr:housename as building name if feature is a POI
* Add aerialway line features into the `roads` layer.
* Add back missing roads on park and other landuse boundaries that went missing when `landuse_kind` intercut was added.
* Add service levels to railroads features in `roads` layer to distinguish importance.
* Updated High Road classifier (zoom range, sort order) for `service` roads, including pedestrian streets, paths, and forest tracks so they are visible earlier.
* Add `volume` on `building` layer polygons to enable more sophisticated client-side filtering at mid zooms.
* Add `city_wall` lines and `barrier` lines to `boundaries` layer.
* Fix minor bug around missing `water` layer boundary lines.
* Add `area` to water boundary lines (so filtering of boundary lines can match polygons).
* Add `townhall`, `laundry`, `dry_cleaner`, and `ferry_terminal` to `pois` layer.
* Move centroid calculation out of database to post-processing step
* Updated formats to contain `api_key` parameter in tilejson metadata URL
* **Requires:** [tileserver v0.4.1](https://github.com/mapzen/tileserver/releases/tag/v0.4.1) and [tilequeue v0.5.0](https://github.com/mapzen/tilequeue/releases/tag/v0.5.0) and [TileStache v0.5.0](https://github.com/mapzen/TileStache/releases/tag/v0.5.0)

v0.4.2
------
* **Release date:** 2015-10-14. _Live in prod: 2015-10-20._
* Fix invalid Antarctica polygon in buffered land.
* **Requires:** [tileserver v0.4.0](https://github.com/mapzen/tileserver/releases/tag/v0.4.0) and [tilequeue v0.4.1](https://github.com/mapzen/tilequeue/releases/tag/v0.4.1) and [TileStache v0.4.1](https://github.com/mapzen/TileStache/releases/tag/v0.4.1)

v0.4.1
------
* **Release date:** 2015-10-13. _Live in prod: 2015-10-20._
* Create new indexes to speed up query times
* Reduce `boundaries` query payload size
* **Requires:** [tileserver v0.4.0](https://github.com/mapzen/tileserver/releases/tag/v0.4.0) and [tilequeue v0.4.1](https://github.com/mapzen/tilequeue/releases/tag/v0.4.1) and [TileStache v0.4.1](https://github.com/mapzen/TileStache/releases/tag/v0.4.1)

v0.4.0
------
* **Release date:** 2015-10-06. _Live in prod: 2015-10-20._
* Fix regression in v0.3.0 where zooms 0 to zoom 8 country and region (state, province) features from OpenStreetMap were dropped from tiles (rolling back a change in v0.2.0)
* Greater diversity of label placements for POIs, landuse, and buildings result in more balanced selection of features visible at mid and high (neighborhood) zooms. The feature's minimum recommended visible zoom is now included as a property (eg: `min_zoom=10.7763`), useful for determining feature priority in client-side label collisions. Currently visibility should be calculated combined with area filters, we'll move that serverside in later releases.
* Add label positions for water bodies to the `water` layer noted as `label_position=yes`.
* Add label positions for buildings to the `buildings` layer noted as `label_position=yes`.
* Landuse label positions are now additionally available in the `landuse` layer directly, noted with `label_position=yes`.
* **WARNING:** The existing `landuse-labels` layer will be depreciated in a later release.
* Add `location` and `layer` tags to buildings features in the `buildings` layer to determine if something is `location=underground` or `layer=-1` (like BART stations in San Francisco).
* Administrative boundary line improvements are back in the `boundaries` layer: now based on OSM relations, includes localized left- and right-names, and adds `maritime_boundary=yes` when the boundary is out in the deep sea. Note that this is slightly different than the `maritime=yes` tag that comes directly from OSM as we're calculating it using a custom spatial mask that will be improved over time.
* Add `ferry` lines starting at zoom 8 to `road` layer.
* Add airport `runway` lines starting at zoom 9 in the `roads` layer. Can be combined with `landuse_kind` attributes to throttle visibility.
* **Requires:** [tileserver v0.4.0](https://github.com/mapzen/tileserver/releases/tag/v0.4.0) and [tilequeue v0.4.0](https://github.com/mapzen/tilequeue/releases/tag/v0.4.0) and [TileStache v0.4.0](https://github.com/mapzen/TileStache/releases/tag/v0.4.0)

v0.3.0
------
* **Release date:** 2015-09-25
* Source `national_park`, `protected_area` and other significant landuse boundaries from OpenStreetMap to generate AOI polygons and labels earlier starting at zoom 4 globally (was zoom 9). These features also gain  `protect_class` and `operator` properties.
* Add OSM roads and other features starting at zoom 8 (transition from Natural Earth data was zoom 9 in earlier releases). Natural Earth urban areas remain until zoom 9, though.
* Add water boundaries for low zooms (from Natural Earth), to match earlier `v0.2.0` work for OSM water boundaries at mid and high zooms.
* Landuse AOI polygons now include a `sort_key` hint from the server for easier client side styling. The `sort_key` is used server side to make the `landuse_kind` predictable on roads.
* Underground streams are now marked such with a additional `is_tunnel` property (zooms 11+)
* Temporarily reverted changes to administrative boundary lines in `v0.2.x` that dropped some boundary lines and their `kind` attributes. They'll be back soon, better than ever.
* Other minor bug fixes and optimizations.
* **Requires:** [tileserver v0.3.0](https://github.com/mapzen/tileserver/releases/tag/v0.3.0) and [tilequeue v0.3.0](https://github.com/mapzen/tilequeue/releases/tag/v0.3.0) and [TileStache v0.3.0](https://github.com/mapzen/TileStache/releases/tag/v0.3.0)

v0.2.0
-----
* **Release date:** 2015-09-18
* Add `landuse_kind` to features in `roads` and `buildings` layers based on the intersection with `landuse` layer features. **TIP:** custom style roads and buildings over parks and other area features to improves contrast.
* Add calculated water `boundary=yes` line features to `water` layer to resolve funky "coastlines" crossing water polygons (where river and ocean polygons meet, and where adjacent river polygons meet). There are already stream lines in the water layer, but this might require an style update. **TIP:** In D3.js, set `fill: none` on linear features like streams and `boundary=yes` feeatures. 
* Added power station polygons to `landuse` layer with `kind` = `plant`, `generator`, or `substation`.
* Add house addresses points to `buildings` layer with `kind` = `address`.
* Resolve duplicate populated places from `places` layer. Natural Earth only used in low zooms, OSM only used in mid and high zooms.
* Stop generating tiny invalid geoms that were making D3.js cry.
* **Requires:** [tileserver v0.2.0](https://github.com/mapzen/tileserver/releases/tag/v0.2.0) and [tilequeue v0.2.0](https://github.com/mapzen/tilequeue/releases/tag/v0.2.0) and [TileStache v0.2.0](https://github.com/mapzen/TileStache/releases/tag/v0.2.0)

v0.2.0-prehistory
------
* **Release date:** July-August 2015
* Add missing OSM `city` features to `places` layer in mid and high zooms.
* Add `kind` = `aerodrome` (airport AOI), `military`, `zoo`; man made features of `kind` = `pier`, `wastewater_plant`, `works`, `bridge`, `tower`, `breakwater`, `water_works`, `groyne`, `dike`, `cutline`; and `urban` & `rural` polygons to `landuse` and points to `landuse-labels` layers.
* Add `sport` and `religion` tags to `landuse` layer polygon and `landuse-labels` point features to distinguish different kinds of sport pitches and places of worship. **TIP:** use these to stylize custom icons.
* Add `cuisine`, `sport` and `religion` tags to `pois` layer point features to distinguish different kinds of restaurants, sport pitches, and places of worship.  **TIP:** use these to stylize custom icons.
* Add more POIs with **`craft`** set to `kind` = `brewery`, `carpenter`, `confectionery`, `dressmaker`, `electrician`, `gardener`, `handicraft`, `hvac`, `metal_construction`, `painter`, `photographer`, `photographic_laboratory`, `plumber`, `pottery`, `sawmill`, `shoemaker`, `stonemason`, `tailor`, `winery` and with **`office`** set to `kind` = `accountant`, `administrative`, `advertising_agency`, `architect`, `association`, `company`, `consulting`, `educational_institution`, `employment_agency`, `estate_agent`, `financial`, `foundation`, `government`, `insurance`, `it`, `lawyer`, `newspaper`, `ngo`, `notary`, `physician`, `political_party`, `religion`, `research`, `tax_advisor`, `telecommunication`, `therapist`, `travel_agent`, `yes`) so more business icons are included in tiles.
* Stop including `parking` and `bus_stop` point features in `pois` layer until zoom 17.
* Stop including `parking` polygon features in `landuse-labels` layer until zoom 17.
* Less linework geometry simplification on Natural Earth geometries at low zooms.
* Move to query templates to reduce code complexity.
* Start [managing issues](https://waffle.io/mapzen/vector-datasource) across all Mapzen vector tile repos with Waffle.io.

v0.1.0
------
* **Release date:** 2015-05-12
* See also: [inaugural Mapzen Vector Tiles blog post](https://mapzen.com/blog/look-upon-our-squares-of-math-in-three-dimensions)

NOTE: Release dates reflect date repo was tagged or otherwise released. Date that production tiles reflect same changes may lag (around a week, usually less).
