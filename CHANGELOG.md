v1.0.0-pre1
-------
* **Release date**: 2016-07-22 on dev as public preview
* See detailed Breaking changes, New features, Bug fixes, and Internal Changes sections below.
* **Requires:** [tileserver v0.7.0](https://github.com/mapzen/tileserver/releases/tag/v0.7.0) and [tilequeue v0.10.0](https://github.com/mapzen/tilequeue/releases/tag/v0.10.0)

  #### BREAKING CHANGES (v1.0.0-pre1)

- **new url scheme**: Mapzen now offers several different types of tiles in vector and raster formats and we combine data from multiple sources. The URL scheme has been updated to reflect this, and emphasize versions. The old URL will continue to work (~1 year), but updates will stop once v1.0.0 is released to production. ([#652](https://github.com/tilezen/vector-datasource/issues/652))

  - **New dev URL:** `http://tile.dev.mapzen.com/vector/v1/all/{z}/{x}/{y}.topojson`

  - Old dev URL was: `http://vector.dev.mapzen.com/osm/all/{z}/{x}/{y}.topojson`

  - **New prod URL will be:** `https://tile.mapzen.com/vector/v1/all/{z}/{x}/{y}.topojson`

  - Old prod URL is still: `https://vector.mapzen.com/osm/all/{z}/{x}/{y}.topojson`

  - **New dev TileJSON is:** `http://tile.dev.mapzen.com/vector/v1/tilejson/mapbox.json`

  - New prod TileJSON will be: `https://tile.mapzen.com/vector/v1/tilejson/mapbox.json`

  - Old prod TileJSON is still: `https://vector.mapzen.com/osm/tilejson/mapbox.json`

- **roads** layer: Reclassify airport runway and taxiways as new `aeroway` kind (was `minor_road`), and change their sort order to be under equivelant landuse polygons. ([#895](https://github.com/tilezen/vector-datasource/issues/895))

- **roads** layer: Reclassify road layer kind values sourced from Natural Earth to use OpenStreetMap style kind values. ([#890](https://github.com/tilezen/vector-datasource/issues/890))

- **roads** layer: Normalize several kind values to remove `-` and replace with `_`, including `drive_through`, `j_bar`, and `t_bar`. ([#843](https://github.com/tilezen/vector-datasource/issues/843))

- **boundaries** layer: Reclassify boundary layer `kind` values for some OpenStreetMap, including `region` (was `state`), `locality` (was `municipality`), and many country related kind changes from Natural Earth at low zooms. ([#841](https://github.com/tilezen/vector-datasource/issues/841))

- **places** layer: Normalize place layer kinds coming from OpenStreetMap and Natural Earth to more closely match Who's On First (mostly using `locality` kind, with new `kind_detail` storing the original OSM and NE values). See this [lookup table](https://github.com/tilezen/vector-datasource/blob/master/yaml/places.yaml) for details. ([#840](https://github.com/tilezen/vector-datasource/issues/840))

- **places** layer: Remove country labels from zoom 0, 1 to reduce tile file size. ([#837](https://github.com/tilezen/vector-datasource/issues/837))

- **places** layer: Remove some types of OpenStreetMap neighbourhoods (`borough`, `suburb`, and `quarter`) in favor of Who's On First neighbourhoods. ([#744](https://github.com/tilezen/vector-datasource/issues/744))

- **pois** layer: Rename several kinds to distinguish `aeroway_gate` from `gate`, specify `gas_canister` shops (was `gas` which was confusing with automotive gas stations), and split off `ski_rental` if a `ski` feature was primarily a rental facility. ([#844](https://github.com/tilezen/vector-datasource/issues/844))

- **landuse** layer: Rename several kinds to distinguish `natural_wood` from `wood` parks, `natural_forest` from `forest` parks, and `natural_park` from `natural` parks. ([#844](https://github.com/tilezen/vector-datasource/issues/844))

- **transit** layer: `route_name` on line geometries is now simply `name`. ([#729](https://github.com/tilezen/vector-datasource/issues/729))

- **landuse** layer: Normalize `urban_area` landuse kinds from Natural Earth (was `urban area`). ([#713](https://github.com/tilezen/vector-datasource/issues/713))

- **landuse** and **boundaries** layers: Move barrier lines from boundaries layer into landuse layer. Includes `city_wall`, `dam`, `fence`, `retaining_wall`, and `snow_fence`. Watch out for `dam` which is now both a polygon and line in the same landuse layer. ([#857](https://github.com/tilezen/vector-datasource/issues/857))

- **buildings** layer: Reclassify building layer kind values to only have `building` or `building_part`, moved the earlier kind values to newnew `kind_detail` property with a whitelist of values. ([#842](https://github.com/tilezen/vector-datasource/issues/842))

- **buildings** layer: Reduce building payloads by merging buildings of similar type at zooms 13, 14, and 15 by dropping some properties like `name`, `addr_housenumber`, and `addr_street`, and quantizing others like `height` to 10 meters (zoom 13), 5 meters (zoom 14), and nearest meter (zoom 15). Also added new `scalerank` property with large buildings at 1 and small buildings at 5 to improve client-side style filtering & draw performance. ([#845](https://github.com/tilezen/vector-datasource/issues/845))

- Remove **landuse-labels** layer in favor of label placements in `landuse` layer and `pois` features. ([#852](https://github.com/tilezen/vector-datasource/issues/852))

- Use boolean values instead of 'yes' for properties like`osm_relation` and `label_placement`. ([#778](https://github.com/tilezen/vector-datasource/issues/778))

- Names that have been localized now use the _l10n_ language codes (ala Who's On First) for all data sources. For example: `name:en` imported from OpenStreetMap is exported as `name:eng`. ([#418](https://github.com/tilezen/vector-datasource/issues/418))


  #### NEW FEATURES (v1.0.0-pre1)

- **roads** layer: Add racetracks as type of `minor_road` sourced from OpenStreetMap's `highway=raceway`. See  [#664](https://github.com/tilezen/vector-datasource/issues/664))

- **roads** layer: Add indoor corridors as type of `path` sourced from OpenStreetMap's `highway=corridor`. ([#605](https://github.com/tilezen/vector-datasource/issues/605))

- **roads** layer: Add properties for `crossing=*`, `sidewalk=*` to all road layer features. ([#605](https://github.com/tilezen/vector-datasource/issues/605))

- **roads** layer: Add `bridleway` as type of `path`. ([#859](https://github.com/tilezen/vector-datasource/issues/859))

- **pois** layer: Add `toll_booth` sourced from OpenStreetMap's `barrier=toll_booth`. ([#479](https://github.com/tilezen/vector-datasource/issues/479))

- **pois** and **landuse** layers: Add `rest_area` and `service_area` kinds sourced from OpenStreetMap's `highway=rest_area` and `highway=services`. ([#480](https://github.com/tilezen/vector-datasource/issues/480))

- **places** layer: Add localized names for Who's On First sourced neighbourhoods using _l10n_ conventions. ([#418](https://github.com/tilezen/vector-datasource/issues/418))

- **places** layer: Add `borough` features from Who's On First (e.g.: Manhattan in New York City). ([#654](https://github.com/tilezen/vector-datasource/issues/654))



  #### BUG FIXES (v1.0.0-pre1)

- **pois** layer: Some walking network points were wrongly classified as `rwn` when they were actually `iwn`. ([#844](https://github.com/tilezen/vector-datasource/issues/844))

- **pois** and **landuse** layers: `garden` kind should win over `attraction`, and add garden point geometries (was previously limited to polygon features). ([#829](https://github.com/tilezen/vector-datasource/issues/829))

- **pois** layer: Show `windmill` features earlier, especially if they are a tourist attraction. ([#830](https://github.com/tilezen/vector-datasource/issues/830))

- **pois** layer: Show `lighthouse` features earlier, especially if they are a tourist attraction, as lighthouses. ([#860](https://github.com/tilezen/vector-datasource/issues/860))

- **pois** layer: Show camp grounds (`camp_site`) earlier. ([#875](https://github.com/tilezen/vector-datasource/issues/875))

- Update JSON encoding to handle invalid geometries (use the python `round` function), improves but does not completely solve invalid geometries in other formats like MVT. ([#698](https://github.com/tilezen/vector-datasource/issues/698))

- Drop all internal properties with a custom `mz` prefix, affected `mz_is_building` in **landuse** layer, but could have affected more layers. ([#622](https://github.com/tilezen/vector-datasource/issues/622))



  #### INTERNAL CHANGES (v1.0.0-pre1)

- **pois** layer: Remove several redundant filters for `boat_storage`, `firepit`, `dry_cleaning`, `toilets`, `theatre`, and `picnic_site`. ([#844](https://github.com/tilezen/vector-datasource/issues/844))

- Make pixel size threshold configurable for layers like **landuse** and **water**. ([#202](https://github.com/tilezen/vector-datasource/issues/202))

- For label placements, enable configurable pixel size threshold. ([#810](https://github.com/tilezen/vector-datasource/issues/810))

- Use json types and functions compatible with postgresql 9.3 to support better hstore tag usage. ([#826](https://github.com/tilezen/vector-datasource/issues/826))

- Migrate more pois layer transform functions to yaml (leisure, transit station states, aeroway gates). ([#754](https://github.com/tilezen/vector-datasource/issues/754).

- Add ability to set configurable buffer for MVT format per layer and geometry type. The default MVT config remains clipped (un-buffered), however. ([#106](https://github.com/tilezen/vector-datasource/issues/106))

- Remove **TileStache** dependency, moving Python transforms into **vector-datasource** repo. ([#211](https://github.com/tilezen/vector-datasource/issues/211))



v0.10.4
-------
* **Release date**: 2016-06-28
* Update tilejson layers. See [#874](https://github.com/tilezen/vector-datasource/issues/872).

v0.10.3
-------
* **Release date**: 2016-05-20.
* Limit addresses to points. See [#834](https://github.com/mapzen/vector-datasource/issues/834).

v0.10.2
-------
* **Release date**: 2016-05-10.
* Add test to verify building heights and properties use the `_` separator. See [#806](https://github.com/mapzen/vector-datasource/issues/806).
* **Requires:** [tileserver v0.6.1](https://github.com/mapzen/tileserver/releases/tag/v0.6.1) and [tilequeue v0.9.0](https://github.com/mapzen/tilequeue/releases/tag/v0.9.0) and [TileStache v0.10.1](https://github.com/mapzen/TileStache/releases/tag/v0.10.1)

v0.10.1
-------
* **Release date**: 2016-05-06.
* Update state boundaries from NE to include statistical boundaries. See [#797](https://github.com/mapzen/vector-datasource/issues/797).
* **Requires:** [tileserver v0.6.1](https://github.com/mapzen/tileserver/releases/tag/v0.6.1) and [tilequeue v0.9.0](https://github.com/mapzen/tilequeue/releases/tag/v0.9.0) and [TileStache v0.10.0](https://github.com/mapzen/TileStache/releases/tag/v0.10.0)

v0.10.0
-------
* **Release date**: 2016-05-04.
* **Paths get a significant makeover** in the `roads` layer:
  * Many `path`, `footway`, and `cycleway` features are visible earlier up to zoom 11, based on their designation as or inclusion in walking and cycling networks.
  * If a track, major road, or minor road is part of a walking or cycling network it is also visible earlier.
  * Some `footway` and `stair` features are visible later than before at zoom 15.
  * Add `footway` property to disentangle `sidewalk` and `crossing` features from other footways.
  * Add `walking_network` property with values in `iwn`, `nwn`, `rwn`, and `lwn` to indicate features's international to local significance.
  * Add other additional properties: `bicycle`, `foot`, `horse`, `tracktype`, `incline`, `trail_visibility` and `sac_scale`.
  * Most paths are now named on introduction, before they were only available at zoom 14+.
  * See [#593](https://github.com/mapzen/vector-datasource/issues/593), [#596](https://github.com/mapzen/vector-datasource/issues/596), and [#775](https://github.com/mapzen/vector-datasource/issues/775).
* **Add bicycle properties** to the `roads` layer:
  * Add `is_bicycle_related` property, set to `true` when road is a cycleway, part of a cycling network, or has bicyle lanes or other cycling related infrastrucure.
  * Add `bicycle_network` property with values in `icn`, `ncn`, `rcn`, and `lcn` to indicate features's international to local significance.
  * Add properties for `cycleway`, `cycleway_left`, `cycleway_right`, `oneway_bicycle`, and `segregated`.
  * See [#647](https://github.com/mapzen/vector-datasource/issues/647).
* **Add new outdoors related polygons** to the `landuse` layer:
  * `battlefield`, `beach_resort`, `boat_storage`, `caravan_site`, `dam`, `dog_park`, `firepit`, `fishing_area`, `fort`, `monument`, `picnic_site`, `recreation_track`, `rock`, `scree`, `stone`, `summer_camp`, `swimming_area`, and `water_park`.
  * See [#663](https://github.com/mapzen/vector-datasource/issues/663) and [#655](https://github.com/mapzen/vector-datasource/issues/655).
* **Add new natural lines** to the `landuse` layer:
  * `tree_row` and `hedge`.
  * See [#566](https://github.com/mapzen/vector-datasource/issues/566).
* **Add outdoor related points** to the `pois` layer:
  * `adit`, `battlefield`, `bbq`, `beach_resort`, `beacon`, `bicycle_repair_station`, `boat_rental`, `boat_storage`, `caravan_site`, `communications_tower`, `cross`, `dam`, `dive_centre`, `dog_park`, `dune`, `egress`, `firepit`, `fishing_area`, `fishing`, `fort`, `gas`, `geyser`, `hazard`, `hot_spring`, `hunting`, `life_ring`, `mast`, `mineshaft`, `monument`, `motorcycle`, `observatory`, `offshore_platform`, `outdoor`, `petroleum_well`, `picnic_site`, `picnic_table`, `power_pole`, `power_tower`, `put_in_egress`, `putin`, `pylon`, `ranger_station`, `rapid`, `recreation_track`, `rock`, `saddle`, `scuba_diving`, `shower`, `sinkhole`, `stone`, `summer_camp`, `swimming_area`, `telescope`, `trailhead`, `waterfall`, `waste_disposal`, `water_park`, `water_point`, `water_tower`, `water_well`, and `watering_place`.
  * See [#594](https://github.com/mapzen/vector-datasource/issues/594), [#599](https://github.com/mapzen/vector-datasource/issues/599), [#602](https://github.com/mapzen/vector-datasource/issues/602), [#657](https://github.com/mapzen/vector-datasource/issues/657), [#662](https://github.com/mapzen/vector-datasource/issues/662), [#663](https://github.com/mapzen/vector-datasource/issues/663), [#671](https://github.com/mapzen/vector-datasource/issues/671), [#674](https://github.com/mapzen/vector-datasource/issues/674), and [#675](https://github.com/mapzen/vector-datasource/issues/675).
* **Add outdoor related lines** to the `roads` layer.
  * `portage_way`
  * See [#677](https://github.com/mapzen/vector-datasource/issues/677).
* Add `dam` to the `boundaries` layer, and removed it from the `water` layer. See [#663](https://github.com/mapzen/vector-datasource/issues/663) and [#773](https://github.com/mapzen/vector-datasource/issues/773).
* Add `waterfall` features to the `pois` layer:
  * Includes `height` value in integer meters.
  * Zoom visibility is based on waterfall height: taller than 300 meters are visible at zoom 12 and waterfalls with height less than 50 meters are visible at zoom 14.
  * See
[#677](https://github.com/mapzen/vector-datasource/issues/677).
* Modified `peak` features in the `pois` layer:
  * Add new `elevation` value in integer meters.
  * Show some tall peaks at earlier zooms.
  * Add `tile_kind_rank` for peaks to throttle visibility of dense peak clusters.
  * See [#523](https://github.com/mapzen/vector-datasource/issues/523) and [#524](https://github.com/mapzen/vector-datasource/issues/524).
* Add `intermittent` property to `water` layer features:
  * Value of `yes` allows styling to distingish streams that do not run year round.
  * See
[#668](https://github.com/mapzen/vector-datasource/issues/668).
* Add **whitewater** related points to the `pois` layer:
  * `putin`, `egress`, `put_in_egress`, `hazard` and `rapid`.
  * Related: `portage_way` features added in the `roads` layer.
  * See [#599](https://github.com/mapzen/vector-datasource/issues/599).
* Add `bicycle_junction` features in `pois` layer:
  * A common European feature in signed bicycle routes with named junctions, these features are added at zoom 16.
  * The cycle network reference point's `ref` value is derived from one of `icn_ref`, `ncn_ref`, `rcn_ref` or `lcn_ref`, in descending order and is suitable for naming or use in a shield.
  * See [#592](https://github.com/mapzen/vector-datasource/issues/592).
* Add `cycle_barrier` features to the `pois` layer at zoom 18. See [#592](https://github.com/mapzen/vector-datasource/issues/592).
* Modify existing bicycle related features in `pois` layer:
  * `bicycle` shops are now visible earlier at zoom 15.
  * `bicycle_rental` is now visible at zoom 16.
  * `bicycle_rental_station` are split off from `bicycle_rental` shops and are visible at zoom 17. They include additional properties for `capacity` (an integer value), `network`, `operator`, and `ref`.
  * Features of kind `bicycle_parking` gain additional properties for `access`, `capacity`, `covered`, `fee`, `operator`, `maxstay`, and `surveillance`.
  * See [#592](https://github.com/mapzen/vector-datasource/issues/592).
* Add features of kind `walking_junction` to the `pois` layer:
  * Walking junctions are common in Europe for signed walking routes with named junctions, added at zoom 16.
  * The walking network reference point's `ref` value is derived from one of `iwn_ref`, `nwn_ref`, `rwn_ref` or `lwn_ref`, in descending order and is suitable for naming or use in a shield.
  * See [#592](https://github.com/mapzen/vector-datasource/issues/592).
* Add `island`, `islet`, and `archipelago` label placement points to the `earth` layer. See [#399](https://github.com/mapzen/vector-datasource/issues/399).
* Add `cliff` and `arete` lines to `earth` layer. See [#601](https://github.com/mapzen/vector-datasource/issues/601).
* Add label placement lines for `ridge` and `valley` to the `earth` layer. See [#601](https://github.com/mapzen/vector-datasource/issues/601).
* Move `continent` label placements to the `earth` layer from the `places` layer, a breaking change. See [#703](https://github.com/mapzen/vector-datasource/issues/703).
* Move `ocean` and `sea` label positions to the `water` layer from the `places` layer, a breaking change. See [#148](https://github.com/mapzen/vector-datasource/issues/148).
* Normalize `kind` values in the `boundaries` layer, a breaking change:
  * Match Natural Earth `kind` values to those coming from OpenStreetMap.
  * Remove junk statistical boundaries.
  * Remove Natural Earth's `type` property.
  * See [#517](https://github.com/mapzen/vector-datasource/issues/517) and [#687](https://github.com/mapzen/vector-datasource/issues/687).
* Normalize `kind` values in the `water` layer, a breaking change:
  * Match Natural Earth `kind` valeus to those coming from OpenStreetMap.
  * Example 1: use kind `ocean` instead of `Ocean`
  * Example 2: use kind `lake` with `reservoir:yes` instead of `Reservoir`.
  * Example 3: use kind `ocean` with `boundary:yes` instead of `Coastline`.
  * See [#628](https://github.com/mapzen/vector-datasource/issues/628) and
[#680](https://github.com/mapzen/vector-datasource/issues/680)
* Add `sources` to the `earth` layer:
  * Indicate `naturalearth.com`, `openstreetmapdata.com`, or `openstreetmap.org` as source.
  * See [#737](https://github.com/mapzen/vector-datasource/pull/737)
* Bug fixes:
  * Identify `yes` kind `pois` to their respective values, including generic `office`. See [#705](https://github.com/mapzen/vector-datasource/issues/705).
  * Don't merging lines in the `roads` layer at zoom 16 (the max zoom). See [#766](https://github.com/mapzen/vector-datasource/issues/766).
  * Line merging in the `roads` layer should produce long lines, not many 2 segment lines. See [#768](https://github.com/mapzen/vector-datasource/issues/768).
  * Removed reference to non-existant `highway=minor` and `highway=footpath` in `roads` layer queries. See [#680](https://github.com/mapzen/vector-datasource/issues/680).
* Refactor how we calculate `kind` values using YAML config files across all layers to provide more determinism and eliminate `yes` values. Follow on to v0.9 changes in [#580](https://github.com/mapzen/vector-datasource/issues/580) and [#282](https://github.com/mapzen/vector-datasource/issues/282). See [#646](https://github.com/mapzen/vector-datasource/issues/646) and [#687](https://github.com/mapzen/vector-datasource/issues/687)
* Update how we handle OpenStreetMap data updates via planet_osm_rels triggers. See [#711](https://github.com/mapzen/vector-datasource/issues/711).
* **Requires:** [tileserver v0.6.1](https://github.com/mapzen/tileserver/releases/tag/v0.6.1) and [tilequeue v0.9.0](https://github.com/mapzen/tilequeue/releases/tag/v0.9.0) and [TileStache v0.10.0](https://github.com/mapzen/TileStache/releases/tag/v0.10.0)


v0.9.1
------
* **Release date**: 2016-03-28. _Live in prod: 2015-03-30._
* Ensure all `transit` layer features are included at zoom 16+. See [commit](https://github.com/mapzen/vector-datasource/commit/9a279d9c29dc63e4e7270a3d846e96a7843bb86b).
* **Requires:** [tileserver v0.6.1](https://github.com/mapzen/tileserver/releases/tag/v0.6.1) and [tilequeue v0.8.0](https://github.com/mapzen/tilequeue/releases/tag/v0.8.0) and [TileStache v0.9.0](https://github.com/mapzen/TileStache/releases/tag/v0.9.0)

v0.9.0
------
* **Release date**: 2016-03-24. _Live in prod: 2015-03-30._
* Adjust tile rank for `station` features in the `pois` layer, emphasizing rail stations over other types of transit. See [#506](https://github.com/mapzen/vector-datasource/issues/506).
* Remove long tail of less important `station` features from mid-zooms in the `pois` layer. See [#506](https://github.com/mapzen/vector-datasource/issues/506).
* Show more `station` features in the `pois` layer by limiting "merging" to zooms less than 15. See [#506](https://github.com/mapzen/vector-datasource/issues/506).
* Show existing aerialway `station` & railway `tram_stop` features in the `pois` layer earlier at zoom 13. See [#587](https://github.com/mapzen/vector-datasource/issues/587).
* Add several boolean values to indicate `station` transit service types in `pois` layer. See [#352](https://github.com/mapzen/vector-datasource/issues/352).
* Add `state` property to `station` features in the `pois` layer to indicate planned and under construction features. See [#484](https://github.com/mapzen/vector-datasource/issues/484).
* Add optional `root_relation_id` ID value on transit `station` features in the `pois` layer. See [#590](https://github.com/mapzen/vector-datasource/issues/590). **CORRECTED 9/31:** earlier documentation said `osm_site_relation`.
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
* Document recommended **overlay** and **underlay** sort_key orders. See [#586](https://github.com/mapzen/vector-datasource/issues/586).
* Move much of the `kind` calculation logic from pure SQL to CSV spreadsheets for easier config and address outstanding SQL coalesce bugs. See [#580](https://github.com/mapzen/vector-datasource/issues/580) and [#282](https://github.com/mapzen/vector-datasource/issues/282).
* Normalize `source` property across all layers. If you have custom place filters, this will be a breaking change. See [#503](https://github.com/mapzen/vector-datasource/issues/503).
* **Requires:** [tileserver v0.6.1](https://github.com/mapzen/tileserver/releases/tag/v0.6.1) and [tilequeue v0.8.0](https://github.com/mapzen/tilequeue/releases/tag/v0.8.0) and [TileStache v0.9.0](https://github.com/mapzen/TileStache/releases/tag/v0.9.0)


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
