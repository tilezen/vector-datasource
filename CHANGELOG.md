v0.9.0
------
* **Release date**: 2016-03-24.
* Adjust tile rank for `station` features in the `pois` layer, emphasizing rail stations over other types of transit. See [#506](https://github.com/mapzen/vector-datasource/issues/506).
* Remove long tail of less important `station` features from mid-zooms in the `pois` layer. See [#506](https://github.com/mapzen/vector-datasource/issues/506).
* Show more `station` features in the `pois` layer by limiting "merging" to zooms less than 15. See [#506](https://github.com/mapzen/vector-datasource/issues/506).
* Show existing aerialway `station` & railway `tram_stop` features in the `pois` layer earlier at zoom 13. See [#587](https://github.com/mapzen/vector-datasource/issues/587).
* Add several boolean values to indicate `station` transit service types in `pois` layer. See [#352](https://github.com/mapzen/vector-datasource/issues/352).
* Add `state` property to `station` features in the `pois` layer to indicate planned and under construction features. See [#484](https://github.com/mapzen/vector-datasource/issues/484).
* Add optional `osm_site_relation` ID value on transit `station` features in the `pois` layer. See [#590](https://github.com/mapzen/vector-datasource/issues/590).
* Add optional `uic_ref` to `station` features in the `pois` layer.
* Add additional transit points to `pois` layer and lines to the `transit` layer for grab bag of stops, halts, stop areas, and platforms. See [#469](https://github.com/mapzen/vector-datasource/issues/469).
* Show `transit` layer features at earlier zoom levels, including international `train`, `subway`, `light_rail`, and `tram`. See [#472](https://github.com/mapzen/vector-datasource/issues/472).
* Add `funicular` and `monorail` features to the `transit` layer. See [#588](https://github.com/mapzen/vector-datasource/issues/588).
* Remove physical `railway` from the `transit` layer; they don't have passenger service. See [#501](https://github.com/mapzen/vector-datasource/issues/501).
* Add `service` values to `transit` layer line features to indicate international, national, and regional importance. See [#471](https://github.com/mapzen/vector-datasource/issues/471).
* Add a new boolean `is_bus_route` property to features in the `roads` layer starting at zoom 12 if any `bus` or `trolley_bus` route passes along the way. No indication is provided for which bus routes at this time. See [#611](https://github.com/mapzen/vector-datasource/issues/611).
* Add `subway` and `funicular` lines to `roads` layer as a type of `rail`. See [#549](https://github.com/mapzen/vector-datasource/issues/549) and [#510](https://github.com/mapzen/vector-datasource/issues/510).
* Remove `disused` features from the `pois` layer, for instance disused railway stations. See [#368](https://github.com/mapzen/vector-datasource/issues/368).
* Limit visibility of `closed` and `historical` features to zoom 17+ in the `pois` and `buildings` layers. See [#291](https://github.com/mapzen/vector-datasource/issues/291) and [#483](https://github.com/mapzen/vector-datasource/issues/483).
* Remove internal `mz_is_building` property from features in the `landuse` layer. See [#333](https://github.com/mapzen/vector-datasource/issues/333).
* Document recommended **overlay** and **underlay** sort_key orders. See [#586](https://github.com/mapzen/vector-datasource/issues/586)
* Move much of the `kind` calculation logic from pure SQL to CSV spreadsheets for easier config and address outstanding SQL coalesce bugs. See [#580](https://github.com/mapzen/vector-datasource/issues/580) and [#282](https://github.com/mapzen/vector-datasource/issues/282).
* Normalize `source` property across all layers. If you have custom place filters, this will be a breaking change. See [#503](https://github.com/mapzen/vector-datasource/issues/503)


v0.8.0
------
* **Release date**: 2016-03-04. _Live in prod: 2015-03-08._
* Add new label placements in the `water` layer for `bay`, `strait`, and `fjord`. [Issue #400](https://github.com/mapzen/vector-datasource/issues/400)
* Add new kinds in the `pois` layer for `hardware` and `trade` to capture more types of "big box" stores. [Issue #520](https://github.com/mapzen/vector-datasource/issues/520)
* Additions to the `pois` layer to celebrate [International Women's Day](http://www.internationalwomensday.com). [Issue #526](https://github.com/mapzen/vector-datasource/issues/526)
     * Basic mappings: `childcare`, `clinic`, `dentist`, `doctors`, `kindergarten`, `midwife`, `phone`, `social_facility`, and `toilets`. 
     * Most social facility are indicated by their detailed kind. Common kinds: `ambulatory_care`, `assisted_living`, `food_bank`, `group_home`, `outreach`, `shelter`, `workshop`, see [TagInfo](https://taginfo.openstreetmap.org/keys/social_facility#values) for full set. 
* Large hotels and "big box" stores now appear at earlier zooms in the `pois` layer. Issues [520](https://github.com/mapzen/vector-datasource/issues/520) and [522](https://github.com/mapzen/vector-datasource/issues/522)
* The `pois` layer now inludels all features at zoom 16 that were only available in zoom 17 and 18 previously. But we now include a recommended `min_zoom` to replicate the earlier behavior. [Issue #478](https://github.com/mapzen/vector-datasource/issues/478)
* Improved station `tile_kind_rank` values in the `pois` layer by including more data. Railway route extraction no longer relies on the `planet_osm_nodes` table, which may be missing if flat nodes is enabled. [Issue #507](https://github.com/mapzen/vector-datasource/issues/507)
* The `buildings` layer now includes all buildings (no filter) at zoom 16, with `min_zoom` properties being added at zoom >= 16. Addresses are included at zoom 16 but are marked `min_zoom:17`. [Issue #557](https://github.com/mapzen/vector-datasource/issues/557)
* In the `boundaries` layer `fences` are now included at zoom 16 (was 17). [Issue #478](https://github.com/mapzen/vector-datasource/issues/478)
* The `roads` and `landuse` layers receive a significant overhall to `sort_key` values. The `sort_key` value is a suggestion for which order to draw features. The value is an integer where smaller numbers suggest that features should be "behind" features with larger numbers. Issues [364](https://github.com/mapzen/vector-datasource/issues/364) and [546](https://github.com/mapzen/vector-datasource/issues/546)
* More layers include `sort_key` values including `boundaries`, `buildings`, `earth`, `transit`, and `water` that are compatible with the values in the `roads` and `landuse` layers. [Issue #550](https://github.com/mapzen/vector-datasource/pull/550)
* Fixed migration loop to handle the case where there are no explicit migrations to run. [Issue #514](https://github.com/mapzen/vector-datasource/issues/514)
* **Requires:** [tileserver v0.6.0](https://github.com/mapzen/tileserver/releases/tag/v0.6.0) and [tilequeue v0.8.0](https://github.com/mapzen/tilequeue/releases/tag/v0.8.0) and [TileStache v0.8.0](https://github.com/mapzen/TileStache/releases/tag/v0.8.0)

v0.7.0
------

* **Release date**: 2016-01-19. _Live in prod: 2015-01-25._
* At mid and low zooms, roads have some properties dropped and are then merged together. This produces a huge reduction in the number of features in a tile and helps reduce both tile size and rendering time. [Issue](https://github.com/mapzen/vector-datasource/issues/358), [Issue](https://github.com/mapzen/vector-datasource/issues/489).
* Gym / fitness POIs are now available with `kind: fitness` in the `pois` layer. [Issue](https://github.com/mapzen/vector-datasource/issues/465).
* Swimming pools are now available with `kind: swimming_pool` in the `water` layer. [Issue](https://github.com/mapzen/vector-datasource/issues/443).
* Prisons are now available with `kind: prison` in both the `pois` and `landuse` layers. [Issue](https://github.com/mapzen/vector-datasource/issues/370).
* Electronics shops are now available with `kind: electronics` in the `pois` layer. [Issue](https://github.com/mapzen/vector-datasource/issues/374).
* Aeroway gates are now available with `kind: gate` and `aeroway: gate` in the `pois` layer. [Issue](https://github.com/mapzen/vector-datasource/issues/454).
* Motorway links no longer show at zooms 10 and below. [Issue](https://github.com/mapzen/vector-datasource/issues/488).
* Buildings are now clipped to a 3x expanded tile boundary. This limits the maximum extent of buildings and can help if you've been experiencing rendering artefacts with very large buildings. [Issue](https://github.com/mapzen/vector-datasource/issues/490), [Issue](https://github.com/mapzen/vector-datasource/issues/197).
* Zoos and other tourist attractions have been "fixed up", and now contain a much wider range of features, as well as including more attributes such as surface type. [Issue](https://github.com/mapzen/vector-datasource/issues/440).
* **Requires:** [tileserver v0.5.0](https://github.com/mapzen/tileserver/releases/tag/v0.5.0) and [tilequeue v0.7.0](https://github.com/mapzen/tilequeue/releases/tag/v0.7.0) and [TileStache v0.7.0](https://github.com/mapzen/TileStache/releases/tag/v0.7.0)

v0.6.0
------
* **Release date**: 2015-12-16. _Live in prod: 2015-01-08._
* Highway exits are now present in the `pois` layer, with `kind:motorway_junction` and, if the data is available, properties for `exit_to` directions and `ref` reference number. [Issue](https://github.com/mapzen/vector-datasource/issues/160).
* Beach polygons are now present in the `landuse` layer. [Issue](https://github.com/mapzen/vector-datasource/issues/366).
* Military (and rural) `landuse` areas were not being output due to a bug. This has been fixed and both landuse types are now being output. [Issue](https://github.com/mapzen/vector-datasource/issues/367).
* Railway platforms are now present in the `transit` layer. [Issue](https://github.com/mapzen/vector-datasource/issues/244).
* Features related to winter sports are now present; with pistes in the `roads` layer as `kind:piste`, winter sports areas / resorts in the `landuse` layer with `kind:winter_sports` and various `pois` related to ski/snowboard hire available in the `pois` layer. [Pistes ticket](https://github.com/mapzen/vector-datasource/issues/342). [Areas ticket](https://github.com/mapzen/vector-datasource/issues/343), [POIs ticket](https://github.com/mapzen/vector-datasource/issues/344).
* IATA codes are included as the `iata` property on airports for which the data is available in the `pois` and `landuse` layers. [Issue](https://github.com/mapzen/vector-datasource/issues/398).
* Pier lines are now included in the `roads` layer with `kind:path, man_made:pier`. [Issue](https://github.com/mapzen/vector-datasource/issues/382).
* Subway stations show at zoom 12 in the `pois` layer. [Issue](https://github.com/mapzen/vector-datasource/issues/369).
* Zoos now show up by zoom 13 at the latest in the `pois` layer. [Issue](https://github.com/mapzen/vector-datasource/issues/421).
* Ice cream shops and stands are now included in the `pois` layer. [Issue](https://github.com/mapzen/vector-datasource/issues/447)
* Toy shops are now included in the `pois` layer. [Issue](https://github.com/mapzen/vector-datasource/issues/404).
* Wine shops are now included in the `pois` layer. [Issue](https://github.com/mapzen/vector-datasource/issues/448)
* Alcohol shops are now included in the `pois` layer. [Issue](https://github.com/mapzen/vector-datasource/issues/448)
* The `population` attribute in the `places` layer is now always an integer. [Issue](https://github.com/mapzen/vector-datasource/issues/230).
* **Requires:** [tileserver v0.5.0](https://github.com/mapzen/tileserver/releases/tag/v0.5.0) and [tilequeue v0.6.0](https://github.com/mapzen/tilequeue/releases/tag/v0.6.0) and [TileStache v0.6.0](https://github.com/mapzen/TileStache/releases/tag/v0.6.0)

v0.5.3
------
* **Release date**: 2015-12-07. _Live in prod: 2015-12-07._
* Fix bug where school points were not being exported as POIs. [Issue](https://github.com/mapzen/vector-datasource/issues/417).
* **Requires:** [tileserver v0.4.1](https://github.com/mapzen/tileserver/releases/tag/v0.4.2) and [tilequeue v0.5.1](https://github.com/mapzen/tilequeue/releases/tag/v0.5.1) and [TileStache v0.5.1](https://github.com/mapzen/TileStache/releases/tag/v0.5.1)

v0.5.2
------
* **Release date**: 2015-12-04. _Live in prod: 2015-12-04._
* Make hospital POIs visible at zoom 14 by default, instead of 15. [Issue](https://github.com/mapzen/vector-datasource/issues/420).
* Fix regression which dropped parking aisles. [Issue](https://github.com/mapzen/vector-datasource/issues/412).
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
