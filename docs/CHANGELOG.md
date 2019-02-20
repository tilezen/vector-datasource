v1.7.0
------
* **Release date:** 2019-02-15.
* **Requires:** [tileserver v2.2.0](https://github.com/tilezen/tileserver/releases/tag/v2.2.0) and [tilequeue v2.3.0](https://github.com/tilezen/tilequeue/releases/tag/v2.3.0) and [rawr_tiles v1.0.0](https://github.com/tilezen/raw_tiles/releases/tag/v1.0.0) and [coanacatl v1.0.0](https://github.com/tilezen/coanacatl/releases/tag/v1.0.0).

  #### ENHANCEMENTS

  * **all layers**: Add `collision_rank` property for label collisions for **pois** layer, and other layers for features with `name` properties, or `ref`, `shield_text`, `bicycle_shield_text`, `bus_shield_text`, or `walking_shield_text`. We now recommend colliding labels client side first with `min_zoom`, and then to tie break with the new `collision_rank` values. (Issue [#988](https://github.com/tilezen/vector-datasource/issues/988))
  * **boundaries**: Adds support for alternate points of view in boundaries layer with `kind:*` properties (like `kind:iso`). Currently this is only for zooms 5, 6 and 7 from Natural Earth. We plan to add more lower zoom data from Natural Earth, and high-zoom data from OpenStreetMap in the next release. (Issue [#1552](https://github.com/tilezen/vector-datasource/issues/1552)) The following country and international organizations worldviews are supported: 
    * Argentina (`ar`), Bangladesh (`bd`), Brazil (`br`), China (`cn`), Egypt (`eg`), France (`fr`), Germany (`de`), Greece (`gr`), India (`in`), Indonesia (`id`), Israel (`il`), Italy (`it`), Japan (`jp`), Morocco (`ma`), Nepal (`np`), Netherlands (`nl`), Pakistan (`pk`), Palestine (`ps`), Poland (`pl`), Portugal (`pt`), Russia (`ru`), Saudi Arabia (`sa`), South Korea (`ko`), Spain (`es`), Sweden (`se`), Taiwan (`tw`), Turkey (`tr`), United Kingdom (`gb`), United States (`us`), Vietnam (`vn`), ISO (`iso`)
  * **boundaries**: Add new disputed boundary lines with kind values of `disputed_breakaway`, `disputed_claim`, `disputed_elusive`, `disputed_reference_line`, from Natural Earth at low zooms, for alternate points of view (Issue [#1552](https://github.com/tilezen/vector-datasource/issues/1552))
  * **landuse**: Remap landuse kinds at mid- and low-zooms to improve merging. This is similar to what we already did for roads. (Issue [#1779](https://github.com/tilezen/vector-datasource/issues/1779))
  * **landuse**: Additional landuse kind merging at low- and mid-zooms, including to `urban_area` which was previously low-zoom only. (Issues [#1721](https://github.com/tilezen/vector-datasource/issues/1721) and [#1795](https://github.com/tilezen/vector-datasource/issues/1795))
  * **landuse**: Add new kinds for `grassland`, `vineyard`, `bare_rock`, `barren` (low- and mid-zooms only), `desert`, `heath`, `sand`, `shingle`, and other natural "landcover" features, starting at zoom 9 (Issue [#1259](https://github.com/tilezen/vector-datasource/issues/1259))
  * **landuse**: Add `kind_detail` property for `wetland` features. If available, value will be one of: `bog`, `fen`, `mangrove`, `marsh`, `mud`, `reedbed`, `saltern`, `saltmarsh`, `string_bog`, `swamp`, `tidalflat`, `wet_meadow`. (Issue [#1253](https://github.com/tilezen/vector-datasource/issues/1253))
  * **landuse**: Add `low_emission_zone` kind data, added to schema in v1.6. (Issue [#1553](https://github.com/tilezen/vector-datasource/issues/1553))
  * **pois**: Add `wetland` kind, with `kind_detail`, see landuse item above for values.
  * **pois**: Add `common` kind, to match the existing landuse layer polygons.
  * **roads**: Populate data for truck `hgv` routing restriction properties and related shields (whitelisted: `agricultural`, `delivery`, `designated`, `destination`, `local`, `no`), added to schema in v1.6, including `maxweight`, `maxheight`, `maxwidth`, `maxlength`, `maxaxleload`, `hazmat`. (Issue [#1553](https://github.com/tilezen/vector-datasource/issues/1553))
  * **roads**: Add `toll` and `toll_hgv` boolean properties. (Issue [#1553](https://github.com/tilezen/vector-datasource/issues/1553)
  * **places**: Add `population_rank` property to `locality`, `region`, `country`, and other kinds useful for setting text size and colliding labels. An integar value from 0 (no population) up to 18 (over 1 billion people). See documentation for more details.
  * **traffic_flow**: Add `road_kind_detail` property to enable data-driven client-side traffic line offseting, thanks [@zaczkows](https://github.com/zaczkows)! (Issue [#1829](https://github.com/tilezen/vector-datasource/issues/1829))
  * **traffic_flow**: Add `is_hov_lane` property to enable client-side filtering, thanks [@conor-ettinoffe-here](https://github.com/conor-ettinoffe-here)! (PR [#1831](https://github.com/tilezen/vector-datasource/issues/1831))
  * **traffic_incidents**: Add `is_hov_lane` property to enable client-side filtering, thanks [@conor-ettinoffe-here](https://github.com/conor-ettinoffe-here)! (PR [#1831](https://github.com/tilezen/vector-datasource/issues/1831))

  #### BUG FIXES

  * **landuse**: Fix v1.6 regression where `aerodrome` polygons sorted above `runway` and `taxiway` polygons in error, thanks [@bcamper](https://github.com/bcamper)! (Issue [#1814](https://github.com/tilezen/vector-datasource/issues/1814))
  * **landuse**: Add additional filter for newer OSM `area:aeroway` tagging of `runway`, `taxiway`, and `apron` polygons to restore features from prior year's tile builds. (Issue [#1814](https://github.com/tilezen/vector-datasource/issues/1814))
  * **landuse**: Better differentiate between parks that should be `common` instead of `national_park` (Issue [#1082](https://github.com/tilezen/vector-datasource/issues/1082))
  * **landuse**: Better differentiate between parks that should be `park` instead of `national_park` (Issue [#1728](https://github.com/tilezen/vector-datasource/issues/1728))
  * **landuse**: Features of kind `mud` now sorts above `water` and below `wetland` (Issue [#1753](https://github.com/tilezen/vector-datasource/issues/1753))
  * **landuse**: Deal with US National Forest, US National Park server side performance (Issue [#475](https://github.com/tilezen/vector-datasource/issues/475))
    * Harmonise kind assignment for `national_park`, `forest`, and other low-zoom green areas.
    * Add `protection_title` based filtering for `national_park`.
    * BLM managed `protected_areas` are now filtered separately in the United States.
  * **landuse**: Change area grading of `nature_reserve` to start zoom 8+, but demote most zoom 10 features to zoom 15. (Issue [#1749](https://github.com/tilezen/vector-datasource/issues/1749))
  * **landuse**: Show all landcover kinds consistently starting at zoom 9. (Issue [#1813](https://github.com/tilezen/vector-datasource/issues/1813))
    * Limit generic `forest` and `natural_wood` to zoom 9+.
    * Promote some landcover-ish landuses up a few zooms to zoom 9+, like `farm` and `farmland`, `orchard`.
    * Limit `residential` areas to zoom 9+.
  * **landuse**: Adjust earliest `min_zoom` for many landcover kinds (Issue [#1794](https://github.com/tilezen/vector-datasource/issues/1794))
    * Pushed `dam`, `prison`, `fort`, `range`, and `danger_area` kinds down to z11+.
    * Push down `aquarium`, `recreation_ground`, `track`, `sports_centre`, `wastewater_plant`, `caravan_site` to zoom 12+.
    * Promote some `camp_site` to zoom 12+, and area grade the rest.
    * Push down `harbour`, `port`, `port_terminal`, `ferry_terminal`, `container_terminal` to zoom 13+.
    * Push down `enclosure`, `petting_zoo`, `aviary`, `animal`, `summer_toboggan`, `winery`, `allotments`, `pedestrian`, `playground` to zoom 13+.
    * Push down `bridge`, `tower`, `breakwater`, `groyne`, `dike`, `cutline` to zoom 13+.
    * Push down `footway`, `library`, `fuel`, `cinema`, `theatre`, `runway`, `taxiway`, `apron`, `trail_riding_station`, `water_park`, `dog_park`, `picnic_site`, `tree_row`, `hedge`, to zoom 13+.
    * Limit `quarry` to zoom 13+, area graded down to zoom 16.
    * Limit `amusement_ride`, `carousel`, `water_slide`, `roller_coaster` to zoom 15+.
    * Limit `marsh` to z15.
  * **landuse**: Whitelist `kind_detail` values:
    * For _crane_ related kinds: `portal_crane`, `gantry_crane`, `travel_lift`, `floor-mounted_crane`, `shiploader`, `tower_crane`.
    * For _religion_ related kinds: `animist`, `bahai`, `buddhist`, `caodaism`, `catholic`, `christian`, `confucian`, `hindu`, `jain`, `jewish`, `multifaith`, `muslim`, `pagan`, `pastafarian`, `scientologist`, `shinto`, `sikh`, `spiritualist`, `taoist`, `tenrikyo`, `unitarian_universalist`, `voodoo`, `yazidi`, and `zoroastrian`.
    * For _wall_ related kinds: `dry_stone`, `noise_barrier`, `brick`, `stone`, `pise`, `castle_wall`, `seawall`, `jersey_barrier`, `flood_wall`, `concrete`, `gabion`.
  * **pois**: Fix junk `healthcare` values and kinds introduced in v1.5. Added: `chiropractor`, `hospice`, `occupational_therapist`, `optometrist`, `paediatrics`, `physiotherapist`, `podiatrist`, `psychotherapist`, `rehabilitation`, and `speech_therapist` kinds. (Issue [#1596](https://github.com/tilezen/vector-datasource/issues/1596))
  * **pois**: Better differentiate between parks that should be `common` instead of `national_park` (Issue [#1082](https://github.com/tilezen/vector-datasource/issues/1082))
  * **pois**: Better differentiate between parks that should be `park` instead of `national_park` (Issue [#1728](https://github.com/tilezen/vector-datasource/issues/1728))
  * **pois**: Deal with US National Forest, US National Park server side performance, same as landcover (Issue [#475](https://github.com/tilezen/vector-datasource/issues/475))
  * **pois**: Prefer `forest` labels over wilderness at zoom 7 (Issue [#1608](https://github.com/tilezen/vector-datasource/issues/1608))
  * **pois**: Add `public_transport=station` with `railway=halt` as a synonym for `station` kind. Require names on `station` features. (Issue [#1747](https://github.com/tilezen/vector-datasource/issues/1747))
  * **pois**: Match new landuse kind and `min_zoom` changes in **landuse** layer for "parks" at low-zooms.
  * **pois**: Clamp POIs with unlimited `min_zoom` ranges to min 13. Technically affected most kinds, though actual occurrence was rare. (Issue [#1750](https://github.com/tilezen/vector-datasource/issues/1750))
  * **pois**: Limit `min_zoom` for POIs to at least match their landuse AOIs.
  * **pois**: POIs for `park` labels shown too soon (Issue [#1767](https://github.com/tilezen/vector-datasource/issues/1767))
  * **pois**: POI labels for `park` show up too late / too early (Issue [#1081](https://github.com/tilezen/vector-datasource/issues/1081))
  * **pois**: Too many `park` and `nature_reserve` labeled at zoom 10 (Issue [#1609](https://github.com/tilezen/vector-datasource/issues/1609))
  * **pois**: Hide early `cafe`, `restaurant` kinds to zoom 15 (Issue [#1632](https://github.com/tilezen/vector-datasource/issues/1632))
  * **pois**: Hide early `post_office` (Issue [#1631](https://github.com/tilezen/vector-datasource/issues/1631))
  * **pois**: Hide early `museums` and `landmarks`, show z12+. (Issue [#1630](https://github.com/tilezen/vector-datasource/issues/1630))
  * **pois**: Hide early `prison`, show z13+. (Issue [#1630](https://github.com/tilezen/vector-datasource/issues/1630))
  * **pois**: Hide early `atm`, `bus_stop`, `drinking_water`, `post_box`, `telephone` to zoom 18. (Issue [#1626](https://github.com/tilezen/vector-datasource/issues/1626))
  * **pois**: Hide early `parking` when no area, show large parking lots and garages earlier based on estimated capacity (Issue [#1625](https://github.com/tilezen/vector-datasource/issues/1625))
  * **pois**: Modify `min_zoom` of `bicycle` to area grades from zoom 15 to 17. (Issue [#1627](https://github.com/tilezen/vector-datasource/issues/1627))
  * **pois**: Push `water_tower` zoom down depending on height: zoom 15 if taller than 20 meters, zoom 16 if taller than 10 meters, else zoom 17. (Issue [#1627](https://github.com/tilezen/vector-datasource/issues/1627))
  * **pois**: Push `theatre` down to z15 min. (Issue [#1627](https://github.com/tilezen/vector-datasource/issues/1627))
  * **pois**: Hide early `bicycle_parking` and `car_sharing` to z19, unless `car_sharing` has name (Issue [#1624](https://github.com/tilezen/vector-datasource/issues/1624))
  * **pois**: Hide early `military` POIs (Issue [#1623](https://github.com/tilezen/vector-datasource/issues/1623))
  * **pois**: Hide early `university`, `college` (Issue [#1622](https://github.com/tilezen/vector-datasource/issues/1622))
  * **pois**: Hide early `school`, `kindergarten` (default 17 for point geoms, arae grade polyons zoom 13+) (Issue [#1621](https://github.com/tilezen/vector-datasource/issues/1621))
  * **pois**: Hide some earlier `golf_course` (Issue [#1619](https://github.com/tilezen/vector-datasource/issues/1619))
  * **pois**: Hide early `cemetery`  (Issue [#1611](https://github.com/tilezen/vector-datasource/issues/1611))
  * **pois**: Limit zoom range of `range` to zoom 11+.
  * **pois**: Limit zoom range of `quarry` to zoom 13+ (Issue [#1799](https://github.com/tilezen/vector-datasource/issues/1799))
  * **pois**: Limit zoom range of `marsh` to zoom 15+ (Issue [#1800](https://github.com/tilezen/vector-datasource/issues/1800))
  * **pois**: Limit zoom range of `substations` (varies by area) (Issue [#1612](https://github.com/tilezen/vector-datasource/issues/1612))
  * **pois**: Consolidate `graveyard` and `cemetery` to share same zoom ranges (Issue [#1780](https://github.com/tilezen/vector-datasource/issues/1780))
  * **pois**: Use same tier 2 zoom range for `nature_reserve` POIs as the landuse polygons.
  * **pois**: Fix tier 1, 3, and 4 area thresholds to not duplicate zoom 12 test.
  * **pois**: Fix tier3 POIs zoom 12 area threshold to 200000 (Issue [#1769](https://github.com/tilezen/vector-datasource/issues/1769))
  * **pois**: Simplify most tier 1 & 2 POI min zooms to area-based thresholds.
  * **pois**: Default `fitness_station` to zoom 18 instead of 17.
  * **pois**: Whitelist `kind_detail` values:
    * For _crane_ relaed kind: `portal_crane`, `gantry_crane`, `travel_lift`, `floor-mounted_crane`, `shiploader`, `tower_crane`.
    * For _cuisine_ related kinds: `american`, `asian`, `barbecue`, `breakfast`, `burger`, `cake`, `chicken`, `chinese`, `coffee_shop`, `crepe`, `donut`, `fish`, `fish_and_chips`, `french`, `friture`, `georgian`, `german`, `greek`, `ice_cream`, `indian`, `international`, `italian`, `japanese`, `kebab`, `korean`, `lebanese`, `local`, `mediterranean`, `mexican`, `noodle`, `pizza`, `ramen`, `regional`, `sandwich`, `seafood`, `spanish`, `steak_house`, `sushi`, `tapas`, `thai`, `turkish`, `vegetarian`, `vietnamese`.
    * For _health_facility_ related kinds: `CSCom`, `chemist_dispensing`, `clinic`, `counselling_centre`, `dispensary`, `first_aid`, `health_center`, `health_centre`, `hospital`, `laboratory`, `medical_clinic`, `office`, `pharmacy`.
    * For _religion_ related kinds: `animist`, `bahai`, `buddhist`, `caodaism`, `catholic`, `christian`, `confucian`, `hindu`, `jain`, `jewish`, `multifaith`, `muslim`, `pagan`, `pastafarian`, `scientologist`, `shinto`, `sikh`, `spiritualist`, `taoist`, `tenrikyo`, `unitarian_universalist`, `voodoo`, `yazidi`, and `zoroastrian`.
    * For _sports_ related kinds: `10pin`, `9pin`, `american_football`, `archery`, `athletics`, `badminton`, `baseball`, `basketball`, `beachvolleyball`, `billiards`, `bmx`, `boules`, `bowls`, `canoe`, `chess`, `climbing`, `cricket`, `cricket_nets`, `cycling`, `equestrian`, `exercise`, `field_hockey`, `fitness`, `football`, `free_flying`, `futsal`, `gaelic_games`, `golf`, `gymnastics`, `handball`, `hockey`, `horse_racing`, `ice_hockey`, `ice_skating`, `karting`, `model_aerodrome`, `motocross`, `motor`, `multi`, `netball`, `padel`, `pelota`, `rugby`, `rugby_league`, `rugby_union`, `running`, `scuba_diving`, `shooting`, `skateboard`, `skating`, `skiing`, `soccer`, `soccer;basketball`, `softball`, `swimming`, `table_tennis`, `team_handball`, `tennis`, `trampoline`, `volleyball`, `yoga`.
    * For _wall_ related kinds: `dry_stone`, `noise_barrier`, `brick`, `stone`, `pise`, `castle_wall`, `seawall`, `jersey_barrier`, `flood_wall`, `concrete`, `gabion`.
  * **boundaries**: Drop `name`, `name:left`, and `name:right` from `locality` lines at zoom 11 and 12 (Issue [#1738](https://github.com/tilezen/vector-datasource/issues/1738))
  * **boundaries**: Fix boundary `name:left` and `name:right` values that were sometimes flipped, especially for `country` and `region` features (Issue [#1770](https://github.com/tilezen/vector-datasource/issues/1770))
  * **boundaries**: Made `min_zoom` of `country` lines depend on the data.
  * **roads**: Fix v1.6 regression where `runway` and `taxiway` lines were sorted below **landuse** layer polygons for the same in error, thanks [@bcamper](https://github.com/bcamper)! (Issue [#1814](https://github.com/tilezen/vector-datasource/issues/1814))
  * **roads**: Expand `is_bridge` logic to include viaduct and any other not "no" bridges (Issue [#1314](https://github.com/tilezen/vector-datasource/issues/1314))
  * **earth**: Add `min_zoom` properties. (Issue [#1073](https://github.com/tilezen/vector-datasource/issues/1073))
  * **water**: 0/0/0 tile has clipped water content (Issues [#1806](https://github.com/tilezen/vector-datasource/issues/1806) and [#1107](https://github.com/tilezen/vector-datasource/issues/1107))
  * **water**: Drop all `lake` name variants zooms 0-4 (again). Drop additional lake names and variants at mid- and high-zooms (zooms 5-15) based on area. (Issue [#1730](https://github.com/tilezen/vector-datasource/issues/1730))
  * **water**: Update `min_zoom` of label placement points based on their inclusion in tiles, not just their raw NE data value.
  * **water**: Extract water boundaries at zoom 8, with the switch to OSM data from NE.
  * **places**: Don't emit `area=0` on point labels (Issue [#1825](https://github.com/tilezen/vector-datasource/issues/1825))
  * **places**: Default `country` labels to **zoom 6** instead of 1 when there isn't Natural Earth match (Issue [#1826](https://github.com/tilezen/vector-datasource/issues/1826))
  * **places**: Default `region` labels to **zoom 8** instead of 1 when there isn't Natural Earth match (Issue [#1826](https://github.com/tilezen/vector-datasource/issues/1826))

  #### DOCUMENTATION CHANGES

  * Updated TileJSON for v1.7 schema changes.
  * Updated Layers documentation for v1.7 schema changes.
  * Publish docs to [tilezen.readthedocs.io](https://tilezen.readthedocs.io).
  * Update documentation formatting for ReadTheDocs.io Markdown requirements.
  * Restructure some file layout for ReadTheDocs.io build system, including: `CHANGELOG`, `LICENSE`, `CONTRIBUTING`, `MIGRATION_GUIDE`, `PERFORMANCE`, `SEMANTIC-VERSIONING`, and `TEST` files.
  * Corrected order of `low_emission_zone` in list.
  * Generalized `hgv_restriction` property units to mostly meters for heavy goods vehicle truck access restrictions.

  #### INTERNAL CHANGES

  * Add `gunicorn` to dependencies, thanks [@rwrx](https://github.com/rwrx). [PR #1690](https://github.com/tilezen/vector-datasource/pull/1690)
  * Bump `PyYAML` version for CVE-2017-18342.
  * Stop using `tags->` in YAML (Issue [#1199](https://github.com/tilezen/vector-datasource/issues/1199))
  * Add ability to make tests from relations
  * Estimate `capacity` for parking lots and garages based on area and parking type with new `tz_estimate_parking_capacity` function.
  * Protect against `None` shapes in way area calculation.
  * Add `all_the_kinds` script to output all the `kind` and `kind_detail` values per `$layer`, with their `min_zoom` from the YAML files.
  * Add whitelists to `kind_detail` in each layer YAML so that we can enumerate all possible values for the script.
  * Extend Natural Earth test generator to support polygons.
  * Use new `drop_names` post-process function to drop _all_ the localized names (not just the default name)
  * Add `CollisionRanker` to support YAML-based spreadsheets for `collision_rank` logic, including reserved, gaps, and filters across layers.
  * Add `safe_int` implementation for SQL.
  * Expose a test method that can return the whole tile. Used in new `collision_rank` tests.
  * Clip to Mercator world bounds before projecting shapefiles.
  * Deal with 'download only' test mode.
  * Skip download only tests after downloading fixtures (if any).
  * Update assets bundle for #1552 & #1809, and updated OSMdata.com land, water.
  * Guard against future airport runway polygons in landuse versus runway lines in roads `sort_rank` errors with a test.
  * Don't create a zero area property on points in SQL templating.
  * Support for multiple shapefiles in a single ZIP for asset bundle creation. (Issue [#1809](https://github.com/tilezen/vector-datasource/issues/1809))
  * Add support for `==` operator in YAML evaluation.
  * Add new `drop_names` function to drop all name variant properties.
  * Add new `remap` function to remap landuse kind values at low- and mid-zooms.
  * Add new `remap_viewpoint_kinds` function remap Natural Earth's points of view to kinds (and drop null values).
  * Add new `add_vehicle_restrictions` function for hgv (heavy good vehicles) trucks.
  * Add new `add_collision_rank` function.
  * Add new `update_min_zoom` function.
  * Refactor order of landuse layer property dropping, and small inner geometry dropping for merging.


v1.6.0
------
* **Release date:** 2018-12-26.
* **Requires:** [tileserver v2.2.0](https://github.com/tilezen/tileserver/releases/tag/v2.2.0) and [tilequeue v2.2.1](https://github.com/tilezen/tilequeue/releases/tag/v2.2.1) and [rawr_tiles v1.0.0](https://github.com/tilezen/raw_tiles/releases/tag/v1.0.0) and [coanacatl v1.0.0](https://github.com/tilezen/coanacatl/releases/tag/v1.0.0).

  #### ENHANCEMENTS

  * **Significant file size reductions** of between 23% (p50) and 30% (p90) globally by additional geometry simplification, dropping features, dropping properties, and more aggressive merging to multi-lines and multi-polygons in low- and mid-zooms. _Chart shows sizes in bytes (logarithmic scale), based on top 100,000 tiles from openstreetmap.org logs at 512 pixel zoom. NOTE: all other zooms in this document use nominal 256 pixel zooms, offset by 1)._
![tilezen_size_v1d5_versus_v1d6](https://github.com/tilezen/vector-datasource/raw/master/docs/images/tilezen-v1d5-versus-v1d6-size-zooms.gif)
  * **boundaries**: Merge lines with same properties into multi-lines, at most zooms. [Issue #1683](https://github.com/tilezen/vector-datasource/issues/1683).
  * **boundaries**: Strip long `name`, `name:left`, and `name:right` properties from boundaries when geometry length can't fit the text, at mid-zooms (<11), to enable merging. [Issue #1683](https://github.com/tilezen/vector-datasource/issues/1683).
  * **boundaries**: Remove `id`, `id:left` and `id:right` properties at low- and mid-zooms (<13), to enable merging. [Issue #1715](https://github.com/tilezen/vector-datasource/issues/1715).
  * **boundaries**: Push `locality` lines down to `min_zoom` **11** (was 10), to reduce file size. [Issue #1715](https://github.com/tilezen/vector-datasource/issues/1715).
  * **boundaries**: Double simplification tolerance. [Issue #641](https://github.com/tilezen/vector-datasource/issues/641) and [PR #1718](https://github.com/tilezen/vector-datasource/pull/1718).
  * **buildings:** Improve polygon merging at zooms 13, 14, and 15 including via [aggregation](https://en.wikipedia.org/wiki/Cartographic_generalization#Aggregation) of adjacent features. Remove some mid-zoom content at zoom 13 and 14, and refactor `min_zoom`. Issues [#1686](https://github.com/tilezen/vector-datasource/issues/1686) and [#1732](https://github.com/tilezen/vector-datasource/issues/1732) [PR #1689](https://github.com/tilezen/vector-datasource/pull/1689), [#1704](https://github.com/tilezen/vector-datasource/pull/1704), and [PR #1739](https://github.com/tilezen/vector-datasource/pull/1739)
  * **earth**: Simplify at zoom 8 to match the transition from Natural Earth to OpenStreetMap, significantly reducing file size at that zoom. [Issue #1477](https://github.com/tilezen/vector-datasource/issues/1477) and [PR #1714](https://github.com/tilezen/vector-datasource/pull/1714).
  * **earth**: Truncate `min_zoom` floats to tenths place (and often just ints), to improve merging. [Issue #1477](https://github.com/tilezen/vector-datasource/issues/1477) and [PR #1714](https://github.com/tilezen/vector-datasource/pull/1714).
  * **landuse**: Add `allotments` (community gardens), was already in POIs layer. [PR #1742](https://github.com/tilezen/vector-datasource/pull/1742)
  * **landuse**: Add `boatyard` and military firing `range` polygons, they already had POIs. [PR #1720](https://github.com/tilezen/vector-datasource/pull/1720).
  * **places**: Use the Natural Earth v4.1 `min_zoom` property to cull more places at low-zooms, and reduce tile overpacking. [Issue #1687](https://github.com/tilezen/vector-datasource/issues/1687) and [PR #1693](https://github.com/tilezen/vector-datasource/pull/1693) and [PR #1734](https://github.com/tilezen/vector-datasource/pull/1734). [Issue #1729](https://github.com/tilezen/vector-datasource/issues/1729)
  * **pois**: Add `turning_circle` and `turning_loop`, thanks [@westnordost](https://github.com/westnordost). [Issue #1695](https://github.com/tilezen/vector-datasource/issues/1695).
  * **roads**: Add cross-junction and multi-pass merging to remove more vertices and reduce overall feature count, thanks [@bcamper](https://github.com/bcamper). [Issue #1227](https://github.com/tilezen/vector-datasource/issues/1227), [PR #1703](https://github.com/tilezen/vector-datasource/pull/1703), [PR #1706](https://github.com/tilezen/vector-datasource/pull/1706), [PR #1708](https://github.com/tilezen/vector-datasource/pull/1708), [PR #1718](https://github.com/tilezen/vector-datasource/pull/1718).
  * **roads**: Double simplification tolerance. [Issue #641](https://github.com/tilezen/vector-datasource/issues/641) and [PR #1718](https://github.com/tilezen/vector-datasource/pull/1718).
  * **roads**: Reduce precision of `surface` tags at mid-zooms to just `paved`, `compacted`, and `unpaved` to increase road merging. Thanks [@matkoniecz](https://github.com/matkoniecz). [Issue #1716](https://github.com/tilezen/vector-datasource/issues/1716).
  * **roads**: Drop some properties from `minor_road` kind features at mid zooms to increase merging, including: `colour`, `cutting`, `embankment`, `motor_vehicle`, `operator`, `route`, `route_name`, `state`, `symbol`, `type`. [Issue #1331](https://github.com/tilezen/vector-datasource/issues/1331) and [PR #1710](https://github.com/tilezen/vector-datasource/pull/1710).
  * **roads**: Drop `all_networks` and `all_shield_texts` properties from roads at low- and mid-zooms, to increase merging. [Issue #1642](https://github.com/tilezen/vector-datasource/issues/1642).
  * **roads**: Drop `all_bicycle_networks` and `all_bicyle_shield_texts` until the max zoom, for all network types, to increase merging. [Issue #1331](https://github.com/tilezen/vector-datasource/issues/1331) and [PR #1707](https://github.com/tilezen/vector-datasource/pull/1707).
  * **roads**: Drop `bicycle_network` and `bicycle_shield_text` from some mid-zooms depending on network type, to increase merging. [Issue #1331](https://github.com/tilezen/vector-datasource/issues/1331) and [PR #1707](https://github.com/tilezen/vector-datasource/pull/1707).
  * **water**: Merge water lines with same properties to improve labeling and rendering, thanks [@sensescape](https://github.com/sensescape). [Issue #1135](https://github.com/tilezen/vector-datasource/issues/1135).
  * **water**: Simplify at zoom 8 to match the transition from Natural Earth to OpenStreetMap, significantly reducing file size at that zoom. [Issue #1477](https://github.com/tilezen/vector-datasource/issues/1477) and [PR #1714](https://github.com/tilezen/vector-datasource/pull/1714).
  * **water**: Drop `name` property when it doesn't fit on feature at all zooms but max, to improve merging. [Issue #1477](https://github.com/tilezen/vector-datasource/issues/1477) and [PR #1714](https://github.com/tilezen/vector-datasource/pull/1714).
  * **water**: Drop smaller water polygons across at all zooms but max. [Issue #1477](https://github.com/tilezen/vector-datasource/issues/1477) and [PR #1714](https://github.com/tilezen/vector-datasource/pull/1714).
  * **water**: Truncate `min_zoom` floats to tenths place (and often just ints), to improve merging. [Issue #1477](https://github.com/tilezen/vector-datasource/issues/1477) and [PR #1714](https://github.com/tilezen/vector-datasource/pull/1714).

  #### BUG FIXES

  * **boundaries**: Drop buffered land polygons from low zooms introduced in v1.5 in error. [PR #1699](https://github.com/tilezen/vector-datasource/pull/1699).
  * **landuse**: Update and/or add **sort_rank** for `airfield`, `boatyard`, `container_terminal`, `danger_area`, `embankment` lines, `ferry_terminal`, `natural_forest`, `natural_park`, `natural_wood`, `naval_base`, `port_terminal`, `quay`, `range`, `shipyard`, `wetland`, and `wharf`. Some other kinds are also affected due to sort_rank ordering. Issues [#1096](https://github.com/tilezen/vector-datasource/issues/1096), [#1588](https://github.com/tilezen/vector-datasource/issues/1588), [#1574](https://github.com/tilezen/vector-datasource/issues/1574), and [#1569](https://github.com/tilezen/vector-datasource/issues/1569).
  * **pois**: Allow no-name `drinking_water` and `playground` features.
  * **pois**: Remove bogus `service_area` and `rest_area` features at mid zooms. [Issue #1698](https://github.com/tilezen/vector-datasource/issues/1698).
  * **pois**: Refine `min_zoom` for `pitch`, `playground`, and `bicycle_parking` if they have a name, and push back no-name to a later zoom. Modify `min_zoom` for `drinking_water` and `traffic_signals`. [Issue #1638](https://github.com/tilezen/vector-datasource/issues/1638) and [PR #1727](https://github.com/tilezen/vector-datasource/pull/1727)
  * **pois**: Modify `min_zoom` of `nursing_home` until z15. [Issue #1634](https://github.com/tilezen/vector-datasource/issues/1634).
  * **pois**: Modify default `min_zoom` of `garden`, `allotments`, and `university`. [Issue #1636](https://github.com/tilezen/vector-datasource/issues/1636).
  * **pois**: Modify default `min_zoom` of tram stops, railway stops, and railway halts down to zoom 16. [Issue #1635](https://github.com/tilezen/vector-datasource/issues/1635)
  * **pois**: Modify default `min_zoom` of early `wood` & `platform`. [Issue #1637](https://github.com/tilezen/vector-datasource/issues/1637)
  * **water**: Remove water point labels generated from lines. [Issue #1702](https://github.com/tilezen/vector-datasource/issues/1702).

  #### DOCUMENTATION CHANGES

  * Updated Layers documentation for v1.6 schema changes.
  * **roads**: Document new heavy good vehicle (hgv, or truck) properties in schema (but not yet added to tile content), thanks [@musculman](https://github.com/musculman) at HERE! [Issue #1553](https://github.com/tilezen/vector-datasource/issues/1553).
  * **traffic_flow**: Add new optional layer definition, thanks [@conor-ettinoffe-here](https://github.com/conor-ettinoffe-here) at HERE! [Issue #1598](https://github.com/tilezen/vector-datasource/pull/1598) and [PR #1705](https://github.com/tilezen/vector-datasource/pull/1705).
  * **traffic_incidents**: Add new optional layer definition, thanks [@conor-ettinoffe-here](https://github.com/conor-ettinoffe-here) at HERE! [Issue #1598](https://github.com/tilezen/vector-datasource/pull/1598) and [PR #1705](https://github.com/tilezen/vector-datasource/pull/1705) and [PR #1719](https://github.com/tilezen/vector-datasource/pull/1719).
  * Updated `tilejson` for **v1.5** and **v1.6** schema changes.

  #### INTERNAL CHANGES

  * Add gunicorn to dependencies, thanks [@rwrx](https://github.com/rwrx). [PR #1690](https://github.com/tilezen/vector-datasource/pull/1690)
  * Use raw strings for regular expressions containing regular expression. [4b2075](https://github.com/tilezen/vector-datasource/commit/4b20755b289ee3158f5cd8677f40b17622464fe6).
  * Refactor common properties for `{bi|motor}cycle_parking` in YAML code.
  * Represent numbers as numbers (not strings), and allow strings not just Unicode strings. [PR #1744](https://github.com/tilezen/vector-datasource/pull/1744)
  * Update simplification process, address bugs. [d66f43](https://github.com/tilezen/vector-datasource/commit/d66f438ed0c86446e5f671dc036e786a5909d3ab)
  * NOTE: No **database migrations** were provided, v1.5 was the last version that included those, as we've migrated to global RAWR tile builds.


v1.5.0
------
* **Release date:** 2018-09-21.
* **Requires:** [tileserver v2.2.1](https://github.com/tilezen/tileserver/releases/tag/v2.1.1) and [tilequeue v2.1.0](https://github.com/tilezen/tilequeue/releases/tag/v2.1.0)  and [rawr_tiles v1.0.0](https://github.com/tilezen/raw_tiles/releases/tag/v1.0.0) and [coanacatl v1.0.0](https://github.com/tilezen/coanacatl/releases/tag/v1.0.0).

  #### ENHANCEMENTS

  * **buildings**: add `entrance` points, with optional **kind_detail** property with values: `garage`, `home`, `main`, `private`, `residence`, `secondary`, `service`, `staircase`, or `unisex`.
  * **buildings**: add `exit` points, with optional **kind_detail** property with values: `emergency` or `fire_exit`.
  * **buildings**: all building polygons are now clipped to tile boundaries, which fixes missing **landuse_kind** values. [Issue #1226](https://github.com/tilezen/vector-datasource/issues/1226) and [#1142](https://github.com/tilezen/vector-datasource/issues/1142) and [#487](https://github.com/tilezen/vector-datasource/issues/487).
  * **buildings**: Add **building_material** optional property to describe the material covering the outside of the building or building part. Common values are: `brick`, `cement_block`, `clay`, `concrete`, `glass`, `masonry`, `metal`, `mud`, `other`, `permanent`, `plaster`, `sandstone`, `semi-permanent`, `steel`, `stone`, `timber-framing`, `tin`, `traditional` and `wood`. [Issue #1408](https://github.com/tilezen/vector-datasource/issues/1408).
  * **landuse**: Add new kind values (listed below) to support full compatibility with OSM.org [#1425](https://github.com/tilezen/vector-datasource/issues/1425) map style.
  * **landuse**: Add **kind_detail** for `wood` and `forest` kinds with values indicating _leaftype_: `broadleaved`, `leafless`, `mixed`, `needleleaved`.
  * **landuse**: Add **kind_detail** optional property for `beach` kind to indicate _surface_ values of: `grass`, `gravel`, `pebbles`, `pebblestone`, `rocky`, `sand`.
  * **landuse**: Add **kind_detail** optional property for `wetland` when _wetland_ is `bog`, `fen`, `mangrove`, `marsh`, `mud`, `reedbed`, `saltern`, `saltmarsh`, `string_bog`, `swamp`, `tidalflat`, `wet_meadow`.
  * **landuse**: Add **kind_detail** optional property for `cemetery` and `grave_yard` kinds, with common values: `animist`, `bahai`, `buddhist`, `caodaism`, `catholic`, `christian`, `confucian`, `hindu`, `jain`, `jewish`, `multifaith`, `muslim`, `pagan`, `pastafarian`, `scientologist`, `shinto`, `sikh`, `spiritualist`, `taoist`, `tenrikyo`, `unitarian_universalist`, `voodoo`, `yazidi`, and `zoroastrian`.
  * **landuse**: Add **denomination** optional property for `cemetery` and `grave_yard` kinds, with common values: `adventist`, `anglican`, `armenian_apostolic`, `assemblies_of_god`, `baptist`, `buddhist`, `bulgarian_orthodox`, `catholic`, `christian`, `church_of_scotland`, `episcopal`, `evangelical`, `greek_catholic`, `greek_orthodox`, `iglesia_ni_cristo`, `jehovahs_witness`, `lutheran`, `mennonite`, `methodist`, `mormon`, `new_apostolic`, `nondenominational`, `orthodox`, `pentecostal`, `presbyterian`, `protestant`, `quaker`, `reformed`, `roman_catholic`, `romanian_orthodox`, `russian_orthodox`, `salvation_army`, `serbian_orthodox`, `seventh_day_adventist`, `shia`, `shingon_shu`, `sunni`, `theravada`, `tibetan`, `united`, `united_methodist`, `united_reformed`, `uniting`, and `曹洞宗`.
  * **landuse**: Add `airfield` kind for military airfields.
  * **landuse**: Add `container_terminal` kind.
  * **landuse**: Add `crane` kind as line geometry. [Issue #1417](https://github.com/tilezen/vector-datasource/issues/1417).
  * **landuse**: Add `cutting` kind.
  * **landuse**: Add `danger_area` kind for military.
  * **landuse**: Add `ditch` kind as line geometry.
  * **landuse**: Add `embankment` kind.
  * **landuse**: Add `fence` kind lines with optional **kind_detail** `avalanche`, `barbed_wire`, `bars`, `brick`, `chain`, `chain_link`, `concrete`, `drystone_wall`, `electric`, `grate`, `hedge`, `metal`, `metal_bars`, `net`, `pole`, `railing`, `railings`, `split_rail`, `steel`, `stone`, `wall`, `wire`, `wood`.
  * **landuse**: Add `ferry_terminal` kind.
  * **landuse**: Add `guard_rail` kind as line geometry.
  * **landuse**: Add `harbour` kind.
  * **landuse**: Add `kerb` kind as line geometry.
  * **landuse**: Add `mud` kind.
  * **landuse**: Add `naval_base` kind for military.
  * **landuse**: Add `orchard` kind with optional **kind_detail** values: `agave_plants`, ` almond_trees`, ` apple_trees`, ` avocado_trees`, ` banana_plants`, ` cherry_trees`, ` coconut_palms`, ` coffea_plants`, ` date_palms`, ` hazel_plants`, ` hop_plants`, ` kiwi_plants`, ` macadamia_trees`, ` mango_trees`, ` oil_palms`, ` olive_trees`, ` orange_trees`, ` papaya_trees`, ` peach_trees`, ` persimmon_trees`, ` pineapple_plants`, ` pitaya_plants`, ` plum_trees`, ` rubber_trees`, ` tea_plants`, ` walnut_trees`.
  * **landuse**: Add `pier` polygon when's used for mooring.
  * **landuse**: Add `plant_nursery` kind.
  * **landuse**: Add `port_terminal` kind.
  * **landuse**: Add `port` kind.
  * **landuse**: Add `power_line` kind as line geometry. [Issue #232](https://github.com/tilezen/vector-datasource/issues/232)
  * **landuse**: Add `power_minor_line` kind as line geometry. [Issue #232](https://github.com/tilezen/vector-datasource/issues/232)
  * **landuse**: Add `quay` kind
  * **landuse**: Add `shipyard` kind.
  * **landuse**: Add `wall` kind as line geometry. [Issue #1403](https://github.com/tilezen/vector-datasource/issues/1403).
  * **landuse**: Add `wharf` kind
  * **places**: Add locality **name** translations for ~21 languages at low zooms from Natural Earth. [Issue #977](https://github.com/tilezen/vector-datasource/issues/977).
  * **places**: Lookup **min_zoom** for `country`, `map_unit`, and `region` from Natural Earth while continue sourcing feature names from OpenStreetMap.
  * **pois**: Add over hundred new kind values (listed below) to support full compatibility with OSM.org and iD [#1425](https://github.com/tilezen/vector-datasource/issues/1425), Maki [#1423](https://github.com/tilezen/vector-datasource/issues/1423), and Humanitarian OpenStreetMap (HOT) [#1424](https://github.com/tilezen/vector-datasource/issues/1424) icon libraries. A continuation of work started in v1.4.3.
  * **pois**: Add **attraction** optional property for all kinds.
  * **pois**: Add **drives_on_left** optional boolean property for `mini_roundabout` kind features. [Issue #1498](https://github.com/tilezen/vector-datasource/issues/1498).
  * **pois**: Add **exit_to** optional property for all kinds.
  * **pois**: Add **kind_detail** optional property for kind `beach` with surface values of: `grass`, ` gravel`, ` pebbles`, ` pebblestone`, ` rocky`, ` sand`.
  * **pois**: Add **kind_detail** optional property for kinds `cemetery` and `grave_yard` to indicate the _religion_. See landuse description above for values.
  * **pois**: Add **denomination** optional property for kinds `cemetery` and `grave_yard` to indicate the _denomination_. See landuse description above for values.
  * **pois**: Add **kind_detail** optional property for kinds `clinic`, `dentist`, `doctors`, `healthcare`, `hospital`, `nursing_home`, `pharmacy`, `social_facility`, and `veterinary` with values: `office`, `dispensary`, `clinic`, `laboratory`, `health_centre`, `hospital`, `health_center`, `CSCom`, `first_aid`, `pharmacy`, `chemist_dispensing`, `counselling_centre`, `medical_clinic`.
  * **pois**: Add **kind_detail** optional property for kind `generator` to indicate method of `anaerobic_digestion`, `barrage`, `combustion`, `fission`, `gasification`, `photovoltaic`, `run-of-the-river`, `stream`, `thermal`, `water-pumped-storage`, `water-storage`, `wind_turbine`.
  * **pois**: Add **kind_detail** optional property for kind `toilet` to indicate `pit_latrine`, ` flush`, ` chemical`, ` pour_flush`, ` bucket`.
  * **pois**: Add **kind_detail** optional property for kind `water_well` with optional values: `drinkable_powered`, `drinkable_manual`, `drinkable_no_pump`, `drinkable`, `not_drinkable_powered`, `not_drinkable_manual`, `not_drinkable_no_pump`, `not_drinkable`.
  * **pois**: Add **ref** optional property for all kinds.
  * **pois**: Add **sanitary_dump_station** optional property on existing `marina`, `camp_site`, and `caravan_site` kind features with values: `yes`, `customers`, or `public`.
  * **pois**: Add **zoo** optional property for all kinds.
  * **pois**: Add `adult_gaming_centre` kind.
  * **pois**: Add `airfield` kind for military features.
  * **pois**: Add `ambulatory_care` kind.
  * **pois**: Add `arts_centre` kind.
  * **pois**: Add `atv` kind for shops.
  * **pois**: Add `baby_hatch` kind.
  * **pois**: Add `blood_bank` kind.
  * **pois**: Add `boat_lift` kind.
  * **pois**: Add `boatyard` kind.
  * **pois**: Add `bookmaker` kind.
  * **pois**: Add `border_control` kind.
  * **pois**: Add `bunker` kind for military features, with optional **kind_detail** values: `pillbox`, `munitions`, `gun_emplacement`, `hardened_aircraft_shelter`, `blockhouse`, `technical`, `mg_nest`, `missile_silo`
  * **pois**: Add `bureau_de_change` kind.
  * **pois**: Add `camera` kind for shops.
  * **pois**: Add `car_parts` kind for shops.
  * **pois**: Add `car_rental` kind.
  * **pois**: Add `car_wash` kind.
  * **pois**: Add `casino` kind.
  * **pois**: Add `charging_station` kind and indicate boolean properties for **bicycle**, **car**, **truck**, and **scooter** usage.
  * **pois**: Add `charity` kind.
  * **pois**: Add `chemist` kind for shops.
  * **pois**: Add `container_terminal` kind.
  * **pois**: Add `copyshop` kind.
  * **pois**: Add `cosmetics` kind for shops.
  * **pois**: Add `crane` kind with optional **kind_detail** to indicate the type of crane, including: `container_crane`, `floor_mounted_crane`, `gantry_crane`, `portal_crane`, `travellift`.  [Issue #1417](https://github.com/tilezen/vector-datasource/issues/1417).
  * **pois**: Add `customs` kind.
  * **pois**: Add `danger_area` kind for military features.
  * **pois**: Add `defibrillator` kind.
  * **pois**: Add `dispensary` kind.
  * **pois**: Add `elevator` kind.
  * **pois**: Add `field_hospital` kind with optional **kind_detail** to indicate heath care facility type.
  * **pois**: Add `fire_hydrant` kind
  * **pois**: Add `fishmonger` kind.
  * **pois**: Add `funeral_directors` kind.
  * **pois**: Add `gambling` kind.
  * **pois**: Add `garden_centre` kind.
  * **pois**: Add `golf` kind.
  * **pois**: Add `grocery` kind.
  * **pois**: Add `harbourmaster` kind.
  * **pois**: Add `health_centre` kind.
  * **pois**: Add `healthcare_alternative` kind.
  * **pois**: Add `healthcare_centre` kind.
  * **pois**: Add `healthcare_laboratory` kind.
  * **pois**: Add `heliport` kind.
  * **pois**: Add `horse_riding` kind.
  * **pois**: Add `hunting_stand` kind.
  * **pois**: Add `karaoke_box` kind.
  * **pois**: Add `karaoke` kind.
  * **pois**: Add `lottery` kind.
  * **pois**: Add `love_hotel` kind at zoom 18+.
  * **pois**: Add `marketplace` kind.
  * **pois**: Add `miniature_golf` kind.
  * **pois**: Add `money_transfer` kind.
  * **pois**: Add `mooring` kind with optional **kind_detail** values of `commercial`, ` cruise`, ` customers`, ` declaration`, ` ferry`, ` guest`, ` pile`, ` waiting`, ` yacht`, ` yachts` and optional **access** property with values: `private` or `public`.
  * **pois**: Add `motorcycle_parking` kind.
  * **pois**: Add `naval_base` kind for military features.
  * **pois**: Add `nightclub` kind.
  * **pois**: Add `obelisk` kind with a variable zoom according to it's height. This kind takes precidence over `artwork`, `monument`, and `memorial`. Optional **kind_detail** indicates if feature is also a `monument` or `memorial`.
  * **pois**: Add `parking_garage` kind by subdividing existing `parking`, when parking type is `multi-storey`, `underground`, or `rooftop`.
  * **pois**: Add `photo` kind.
  * **pois**: Add `plaque` kind.
  * **pois**: Add `port_terminal` kind.
  * **pois**: Add `quay` kind.
  * **pois**: Add `range` kind for military features.
  * **pois**: Add `sanitary_dump_station` kind.
  * **pois**: Add `ship_chandler` kind.
  * **pois**: Add `shipyard` kind.
  * **pois**: Add `slaughterhouse` kind.
  * **pois**: Add `slipway` kind with optional **mooring** property.
  * **pois**: Add `snowmobile` kind.
  * **pois**: Add `street_lamp` kind.
  * **pois**: Add `studio` kind, with optional **kind_detail** values `audio`, ` cinema`, ` photography`, ` radio`, ` television`, ` video`.
  * **pois**: Add `taxi` kind for taxi stands.
  * **pois**: Add `tyres` kind.
  * **pois**: Add `waterway_fuel` kind.
  * **pois**: Add `wayside_cross` kind.
  * **pois**: Add `wharf` kind.
  * **pois**: Add additional `ferry_terminal` kind features by expanding upstream filters.
  * **pois**: Add catchall `craft` kind when there isn't a more specific kind.
  * **pois**: Add catchall `industrial` kind when there isn't a more specific kind.
  * **pois**: Add catchall `office` kind when there isn't a more specific kind.
  * **pois**: Add catchall `shop` kind when there isn't a more specific kind.
  * **pois**: Allow additional kind values to show up on the map when they lack a name: `boat_lift`, `boatyard`, `border_control`, `bunker`, `bureau_de_change`, `car_rental`, `car_wash`, `charging_station`, `crane`, `customs`, `defibrillator`, `field_hospital`, `fire_hydrant`, `harbour_master`, `harbourmaster`, `health_centre`, `hunting_stand`, `karaoke_box`, `money_transfer`, `motorcycle_parking`, `obelisk`, `power_generator`, `sanitary_dump_station`, `street_lamp`, `taxi`, `waterway_fuel`, and `wayside_cross`.
  * **pois**: Modify **min_zoom** of `alpine_hut` kind to reveal them two zooms earlier at zoom 13. [Issue #1407](https://github.com/tilezen/vector-datasource/issues/1407).
  * **pois**: Modify **min_zoom** of `lighthouse` kind when they are ruins but also attractions.
  * **pois**: Modify **min_zoom** of `watermill` kind when they are ruins but also attractions.
  * **pois**: Remove abandoned or disused `watermill` kind features (but keep the majority of features).
  * **pois**: Stop emitting **covered** boolean property when the value was false on `bicycle_parking` and `motorcycle_parking` kind features.
  * **roads**: Add **access** optional property with common values: `private`, `yes`, `no`, `permissive`, `customers`, `destination`. [Issue #1273](https://github.com/tilezen/vector-datasource/issues/1273).
  * **roads**: Add **cutting** optional property with values: `yes`, `right`, and `left`.
  * **roads**: Add **embankment** optional property with values: `yes`, `right`, and `left`.
  * **roads**: Add **mooring** optional property for new `quay` and existing `pier` kinds with values: ['no', 'yes', commercial, cruise, customers, declaration, ferry, guest, private, public, waiting, yacht, yachts]
  * **roads**: Add `quay` kind lines.
  * **roads**: Major changes to **network** and **shield_text** to support localized road shields globally, including (but not limited to), with uppercase 2-char country code prefixes: `AM:AM`, `AR:national`, `AR:provincial`, `AsianHighway`, `AT:A-road`, `AU:A-road`, `AU:B-road`, `AU:C-road`, `AU:M-road`, `AU:Metro-road`, `AU:N-route`, `AU:R-route`, `AU:S-route`, `AU:T-drive`, `BE:A-road`, `BE:N-road`, `BE:R-road`, `BR:AC`, `BR:AL`, `BR:AM`, `BR:AP`, `BR:BA`, `BR:BR`, `BR:CE`, `BR:DF`, `BR:ES`, `BR:GO`, `BR:MA`, `BR:MG:local`, `BR:MG`, `BR:MS`, `BR:MT`, `BR:PA`, `BR:PB`, `BR:PE`, `BR:PI`, `BR:PR`, `BR:RJ`, `BR:RN`, `BR:RO`, `BR:RR`, `BR:RS`, `BR:SC`, `BR:SE`, `BR:SP:PLN`, `BR:SP:SCA`, `BR:SP`, `BR:TO`, `BR:Trans-Amazonian`, `BR`, `CA:AB:primary`, `CA:AB:trunk`, `CA:AB`, `CA:BC:primary`, `CA:BC:trunk`, `CA:BC`, `CA:MB:PTH`, `CA:MB`, `CA:NB2`, `CA:NB3`, `CA:NB`, `CA:NS:R`, `CA:NS:T`, `CA:NT`, `CA:ON:primary`, `CA:ON:secondary`, `CA:PEI`, `CA:QC:A`, `CA:QC:R`, `CA:SK:primary`, `CA:SK:secondary`, `CA:SK:tertiary`, `CA:transcanada`, `CA:yellowhead`, `CA:YT`, `CD:RRIG`, `CH:motorway`, `CH:national`, `CH:regional`, `CL:national`, `CL:regional`, `CN:expressway:regional`, `CN:expressway`, `CN:JX`, `CN:road`, `CZ:national`, `CZ:regional`, `DE:BAB`, `DE:BS`, `DE:Hamburg:Ring`, `DE:KS`, `DE:LS`, `DE:STS`, `DE`, `DK:national`, `e-road`, `ES:A-road`, `ES:autonoma`, `ES:city`, `ES:N-road`, `ES:province`, `ES`, `FR:A-road`, `FR:D-road`, `FR:N-road`, `FR`, `GA:L-road`, `GA:national`, `GB:A-road-green`, `GB:A-road-white`, `GB:B-road`, `GB:M-road`, `GB`, `GR:motorway`, `GR:national`, `GR:provincial`, `GR`, `HU:national`, `ID:national`, `IN:MDR`, `IN:NH`, `IN:SH`, `IR:freeway`, `IR:national`, `IT:A-road`, `IT:B-road`, `IT`, `JP:expressway`, `JP:national`, `JP:prefectural`, `JP`, `KR:expressway`, `KR:local`, `KR:metropolitan`, `KR:national`, `KZ:national`, `KZ:regional`, `LA:national`, `MX:AGU`, `MX:BCN`, `MX:BCS`, `MX:CAM`, `MX:CHH`, `MX:CHP`, `MX:CMX:EXT`, `MX:CMX:INT`, `MX:COA`, `MX:COL`, `MX:DUR`, `MX:GRO`, `MX:GUA`, `MX:HID`, `MX:JAL`, `MX:MEX`, `MX:MIC`, `MX:MOR`, `MX:NAY`, `MX:NLE`, `MX:OAX`, `MX:PUE`, `MX:QUE`, `MX:ROO`, `MX:SIN`, `MX:SLP`, `MX:SON`, `MX:TAB`, `MX:TAM`, `MX:VER`, `MX:YUC`, `MX:ZAC`, `MY:expressway`, `MY:federal`, `MY:JHR`, `MY:KDH`, `MY:KTN`, `MY:MLK`, `MY:NSN`, `MY:PHG`, `MY:PLS`, `MY:PNG`, `MY:PRK`, `MY:SBH`, `MY:SGR:municipal`, `MY:SGR`, `MY:SWK`, `MY:TRG`, `NL:A-road`, `NL:N-road`, `NO:fylkesvei`, `NO:oslo:ring`, `NO:riksvei`, `NZ:SH`, `NZ:SR`, `PE:AM`, `PE:AN`, `PE:AP`, `PE:AR`, `PE:AY`, `PE:CA`, `PE:CU`, `PE:HU`, `PE:HV`, `PE:IC`, `PE:JU`, `PE:LA`, `PE:LI`, `PE:LM`, `PE:LO`, `PE:MD`, `PE:MO`, `PE:PA`, `PE:PE`, `PE:PI`, `PE:PU`, `PE:SM`, `PE:TA`, `PE:TU`, `PE:UC`, `PH:NHN`, `PK`, `PL:expressway`, `PL:motorway`, `PL:national`, `PL:regional`, `PT:express`, `PT:motorway`, `PT:municipal`, `PT:national`, `PT:primary`, `PT:rapid`, `PT:regional`, `PT:secondary`, `PT`, `RO:county`, `RO:local`, `RO:motorway`, `RO:national`, `RU:national`, `RU:regional`, `SG:expressway`, `TR:highway`, `TR:motorway`, `TR:provincial`, `UA:international`, `UA:national`, `UA:regional`, `UA:territorial`, `VN:expressway`, `VN:national`, `VN:provincial`, `VN:road`, `ZA:kruger`, `ZA:metropolitan`, `ZA:national`, `ZA:provincial`, `ZA:regional`, and `ZA:S-road`.
  * **roads**: Major changes to **network** and **shield_text** to support fallback international road shields. When no network is provided by a ref is, a 2-char country code will be exported as the network value based on the location of the road, like `AM` or `US`. [Issue #135](https://github.com/tilezen/vector-datasource/issues/135).
  * **roads**: Minor changes to **network** and **shield_text** to support USA road shields, including _modifier_ postfix: `US:AK`, `US:AL`, `US:AR`, `US:AZ`, `US:BIA`, `US:BLM`, `US:CA`, `US:CO`, `US:CT`, `US:DC`, `US:DE`, `US:FL`, `US:FSH`, `US:FSR`, `US:GA`, `US:HI`, `US:I:Alternate`, `US:I:Business`, `US:I:Bypass`, `US:I:Connector`, `US:I:Historic`, `US:I:Scenic`, `US:I:Spur`, `US:I:Toll`, `US:I:Truck`, `US:I`, `US:IA`, `US:ID`, `US:IL`, `US:IN`, `US:KS`, `US:KY`, `US:LA`, `US:MA`, `US:MD`, `US:ME`, `US:MI`, `US:MN`, `US:MO`, `US:MS`, `US:MT`, `US:NC`, `US:ND`, `US:NE`, `US:NH`, `US:NJ`, `US:NM`, `US:NV`, `US:NY`, `US:OH`, `US:OK`, `US:OR`, `US:PA`, `US:RI`, `US:SC`, `US:SD`, `US:TN`, `US:TX`, `US:US:Alternate`, `US:US:Business`, `US:US:Bypass`, `US:US:Connector`, `US:US:Historic`, `US:US:Scenic`, `US:US:Spur`, `US:US:Toll`, `US:US:Truck`, `US:US`, `US:UT`, `US:VA`, `US:VT`, `US:WA`, `US:WI`, `US:WV`, and `US:WY`. [Issue #1387](https://github.com/tilezen/vector-datasource/issues/1387).
  * **roads**: Modify **min_zoom** of `track` kind to show 1 zooms earlier by default when **surface** is `gravel` or **tracktype** is not `grade3`, `grade4`, or `grade5`. [Issue #1251](https://github.com/tilezen/vector-datasource/issues/1251).
  * **roads**: Modify **min_zoom** of `track` kind to show 2 zooms earlier by default when **surface** is `paved`, `asphalt`, `concrete` or **tracktype** is `grade1` (but not for **access** `private`). [Issue #1251](https://github.com/tilezen/vector-datasource/issues/1251).
  * **roads**: Modify **min_zoom** of `unclassified` kind to show 1 zoom earlier by default. [Issue #1250](https://github.com/tilezen/vector-datasource/issues/1250).
  * **roads**: Show important cycling and walking routes at earlier zooms by adjusting the `min_zoom` of `path`, `major_road`, and `minor_road` kinds. This means that `min_zoom` values are now variable for features of the same kind, depending on their importance in the bicycle and walking networks; in earlier releases they all shared the same `min_zoom`. See [#1172](https://github.com/tilezen/vector-datasource/issues/1172).
  * **water**: Add `fountain` kind.
  * **water**: Add `reef` kind, with optional **kind_detail** values of `coral`, `rock`, and `sand`.

  #### BUG FIXES

  * **boundaries**: Restore full border to Gaza Strip. [Issue #1257](https://github.com/tilezen/vector-datasource/issues/1257).
  * **landuse**: MVT format now includes many more polygons that were dropped in earlier versions that used different format driver.
  * **places**: Fix spelling of ~60 **locality** (city) names at low-zooms in **places** layer by taking Natural Earth update. [#1140](https://github.com/tilezen/vector-datasource/issues/1140).
  * **roads**: European primary network calculation now prefers local networks instead of e-road. [Issue #1483](https://github.com/tilezen/vector-datasource/issues/1483).
  * **roads**: Add **surface** property at more zooms. [Issue #1252](https://github.com/tilezen/vector-datasource/issues/1252).
  * **water**: Fix missing ocean water by making Natural Earth `ne_10m_ocean` features OGC valid in PostGIS.

  #### DOCUMENTATION CHANGES

  * Correct the **Greek** language 2-char code from `gr` to `el` in the Semantic Versioning statement.
  * Change references to **Mapzen** (RIP) to **Tilezen**.
  * **Update MapboxGL demo**, thanks to Apollo Mapping
  * Use service wording changes (Less > Fewer)
  * Updated Layers documentation for v1.5 schema changes.
  * Updated tilejson/tilejson.json.erb for v1.5 schema changes.


  #### INTERNAL CHANGES

  * Change references to **Who's On First** gazetteer source to `whosonfirst.org` from `whosonfirst.mapzen.com`.
  * Refactors to support **RAWR tile** builds in queries/jinja and elsewhere.
  * Add support for multiple **localized names** from Natural Earth 4.x by adding new transform `convert_ne_l10n_name` for 2-char language codes.
  * Use a Tilezen curated **country admin polygon** layer to determine country codes PIP for intermediate processing (this layer is not exported in final tiles).
  * Add new function to **calculate linear overlap with polygons**, useful for road in country calculation.
  * Add new function to **calculate point in polygon (PIP)**, useful in POI in country calculation.
  * Updates to Tilezen curated **buffered_land** layer for marine boundary lines.
  * Be more robust to only add database columns when they don't already exist.
  * Support easier creation of **generative tests** for points, lines, and polygons.
  * Continued migration to generative tests instead of live-data OpenStreetMap tests via Overpass.
  * Switch to generating MVT format with **Coanacatl**, which wraps Wagyu and VTZero.
  * Requires Postgresql 9.5. [Issue #1319](https://github.com/tilezen/vector-datasource/issues/1319).
  * Upgrade to **CircleCI 2.0** for continuous integration.
  * Refactor all OpenStreetMap to Tilezen ETL logic for `network` and `ref` > `shield_text` to support international road shields based on fuzzy data and missing country code data, including specific functions per country.
  * Add `max_zoom_filter` to remove features with a `max_zoom` if it's < `nominal` zoom.
  * Add whitelist for **fence** `kind_detail` values.
  * This will be the last set of **database migrations** provided. All future releases will assume "global" RAWR tile builds.

v1.4.3
------
* **Release date:** 2018-01-08.
* RAWR internal pre-release round 2.
* Clip buildings to tile boundaries. See #1142.
* Allow some kinds of non-numeric `shield_text`. See #1452.
* Add shops from osm.org and iD. See #1447.
* Clip buildings to tiles. See #1446.
* Include all name variants. See #1454.
* Add building material tag to output. See #1455.
* Add route modifier information to network. See #1460.
* Add wetland detail to `kind_detail`. See #1461.
* Remove unused wooded area tags + natural=park and add _leaf_type_ **kind_detail** to wooded areas. See #1459.
* Guard against TopologicalError. See #1471.

v1.4.2
------
* **Release date:** 2017-12-04.
* RAWR internal pre-release.

v1.4.1
------
* **Release date:** 2017-10-23.
* **Requires:** [tileserver v2.1.1](https://github.com/mapzen/tileserver/releases/tag/v2.1.1) and [tilequeue v1.8.1](https://github.com/mapzen/tilequeue/releases/tag/v1.8.1) and [mapbox-vector-tile v1.2.0](https://pypi.python.org/pypi/mapbox-vector-tile/v1.2.0).
* Backport fix for including VERSION file in package. See [#265](https://github.com/tilezen/vector-datasource/pull/1411).
* Point tilequeue/tileserver to specific versions in requirements.

v1.4.0-docs1
------
* **Release date**: 2017-06-28. _Live on prod 2017-06-??._
* **Requires:** [tileserver v2.1.0](https://github.com/mapzen/tileserver/releases/tag/v2.1.0) and [tilequeue v1.8.0](https://github.com/mapzen/tilequeue/releases/tag/v1.8.0) and [mapbox-vector-tile v1.2.0](https://pypi.python.org/pypi/mapbox-vector-tile/v1.2.0).
- [docs] Update link to pois.jinja2. See [#1268](https://github.com/tilezen/vector-datasource/pull/1268).
- [docs] Update `your-mapzen-api-key` URL query strings to enable key substitution. See [#1275](https://github.com/tilezen/vector-datasource/pull/1275).
- [docs] Spelling, grammar, writing style fixes. See [#1275](https://github.com/tilezen/vector-datasource/pull/1275).
- [docs] Add documentation for 512 pixel tile sizes. See [#1284](https://github.com/tilezen/vector-datasource/pull/1284).
- [docs] Add documentation to suggest max zoom (per tile size). See [#1161](https://github.com/tilezen/vector-datasource/pull/1161).
- [docs] Add documentation for tile x, y coordinates (versus latitude and longitude). See [#1111](https://github.com/tilezen/vector-datasource/pull/1111).
- [docs] Add documentation for HTTP status codes. See [#1266](https://github.com/tilezen/vector-datasource/pull/1266).
- [tests] Update tests for upstream OpenStreetMap data churn. See [#1267](https://github.com/tilezen/vector-datasource/pull/1267), [#1282](https://github.com/tilezen/vector-datasource/pull/1282), and [#1286](https://github.com/tilezen/vector-datasource/pull/1286).
- Remove duplicate symbol output. See [#1265](https://github.com/tilezen/vector-datasource/pull/1265).
- Fixed release notes on 2017-07-19 with corrected **Requires** section.

v1.4.0
------
* **Release date**: 2017-05-31.
* **Requires:** [tileserver v2.1.0](https://github.com/mapzen/tileserver/releases/tag/v2.1.0) and [tilequeue v1.8.0](https://github.com/mapzen/tilequeue/releases/tag/v1.8.0) and [mapbox-vector-tile v1.2.0](https://pypi.python.org/pypi/mapbox-vector-tile/v1.2.0).
- [tests] Add support to capture all test coordinates with `-printcoords`. This also namespaces all the test assertion functions using `test`. See [#1245](https://github.com/tilezen/vector-datasource/issues/1245).
- [tests] Publish all test coordinates for master CircleCI builds. See [#1246](https://github.com/tilezen/vector-datasource/pull/1246).
- [docs] Remove rate limiting note (for Mapzen hosted service).

v1.3.0-docs1
------
* **Release date**: 2017-05-05.
* **Requires:** [tileserver v2.0.0](https://github.com/mapzen/tileserver/releases/tag/v2.0.0) and [tilequeue v1.7.0](https://github.com/mapzen/tilequeue/releases/tag/v1.7.0) and [mapbox-vector-tile v1.2.0](https://pypi.python.org/pypi/mapbox-vector-tile/v1.2.0).
- [docs] Delete api-keys-and-rate-limits.md page
- [docs] Update attribution.md page with less Mapzen
- [docs] Add `your_mapzen_api_key` URL query strings to URL endpoint examples
- [changelog] Update mapbox-vector-tile pypi urls
- [tests] island > islet for OSM data change

v1.3.0
------
* **Release date**: 2017-05-04. _Live on prod 2017-05-08._
* **Requires:** [tileserver v2.0.0](https://github.com/mapzen/tileserver/releases/tag/v2.0.0) and [tilequeue v1.7.0](https://github.com/mapzen/tilequeue/releases/tag/v1.7.0) and [mapbox-vector-tile v1.2.0](https://pypi.python.org/pypi/mapbox-vector-tile/1.2.0).

  #### ENHANCEMENTS

  * Show important cycling and walking routes at earlier zooms by adjusting the `min_zoom` of `path`, `major_road`, and `minor_road` cycling and walking related features in the **roads** layer. This means that `min_zoom` values are now variable for features of the same kind, depending on their importance in the bicycle and walking networks; in earlier releases they all shared the same `min_zoom`. See [#1172](https://github.com/tilezen/vector-datasource/issues/1172).
  * Add shields for bicycle, walking, and bus networks with new `bicycle_network`, `walking_network`, `bus_network`, `bicycle_shield_text`, `walking_shield_text`, `bus_shield_text`, and `all_*` variants onto **road** layer features. See [#775](https://github.com/tilezen/vector-datasource/issues/775), [#1175](https://github.com/tilezen/vector-datasource/issues/1175), and [#1214](https://github.com/tilezen/vector-datasource/issues/1214).
  * Add `bicycle` property to non-path **road** layer features to more accurately reflect `is_bicycle_related` routes (eg for ways tagged `bicycle=designated`). See [#1171](https://github.com/tilezen/vector-datasource/issues/1171).
  * Add `surface` property to **roads** layer features. See [#1020](https://github.com/tilezen/vector-datasource/issues/1020).
  * Add `ramp` and `ramp_bicycle` property to **roads** layer features. See  [#1147](https://github.com/tilezen/vector-datasource/issues/1147).
  * Remove `motor_vehicle`, `horse` and some other properties at low- and mid-zooms in **roads** layer. See [#1224](https://github.com/tilezen/vector-datasource/issues/1224) and [#1214](https://github.com/tilezen/vector-datasource/issues/1214).
  * Improve line merging in **roads** and other layers to reduce tile file size and improve rendering performance. See [#1191](https://github.com/tilezen/vector-datasource/issues/1191).
  * Add `colour_name` property for **transit** layer features. See [#1190](https://github.com/tilezen/vector-datasource/issues/1190).
  * Show large piers earlier in **landuse** layer. See [#1178](https://github.com/tilezen/vector-datasource/issues/1178).
  * Remove many **pois** layer features when they lack a name (but many others are whitelisted as no-name okay). See [#1186](https://github.com/tilezen/vector-datasource/issues/1186) and [#1218](https://github.com/tilezen/vector-datasource/issues/1218).

  #### BUG FIXES

  * Fix spelling of ~60 locality (city) names at low-zooms in **places** layer. [#1140](https://github.com/tilezen/vector-datasource/issues/1140).
  * Small gardens (in Edinburgh and elsewhere) should not be visible at mid-zooms in **pois** layer. [#1185](https://github.com/tilezen/vector-datasource/issues/1185).
  * Some **pois** layer features were missing their `tier` property. See [#1208](https://github.com/tilezen/vector-datasource/issues/1208).
  * Remove `natural_forest`, `natural_wood`, and `village_green` from **pois** layer, a documented breaking bug fix associated with the v1.0 release. Their label points are now found in the **landuse** layer. See [#1103](https://github.com/tilezen/vector-datasource/issues/1103).
  * Fix test failures based on upstream OpenStreetMap data changes.
  * _NOTE: while the v1.3.0 release was tagged correctly the VERSION file was stuck at v1.2.0 leading to the incorrectly report in Python installs as v1.2.0._



v1.2.0
------
* **Release date**: 2017-03-23. _Live on prod 2017-03-27._
* **Requires:** [tileserver v1.4.0](https://github.com/mapzen/tileserver/releases/tag/v1.4.0) and [tilequeue v1.6.0](https://github.com/mapzen/tilequeue/releases/tag/v1.6.0) and [mapbox-vector-tile v1.2.0](https://pypi.python.org/pypi/mapbox-vector-tile/1.2.0).
* Generate less-complex MultiPolygons by limiting the number of features that can be merged into a single MultiPolygon (defaults to 1000). This can have a large impact on geometric topology checks for file formats like MVT. See [#1176](https://github.com/tilezen/vector-datasource/pull/1176).
* Move merging of landuse polygons after roads intercut, to improve intercut performance. See [#1177]( https://github.com/tilezen/vector-datasource/pull/1177).
* Drop small inner polygons, to improve downstream performance. See [#1180](https://github.com/tilezen/vector-datasource/pull/1180).
* Fix test failures based on OpenStreetMap data changes and 2x2 metatiles where unit of work for some operations like `tile_kind_rank` is now 512px instead of 256px. See [#1182](https://github.com/tilezen/vector-datasource/pull/1182).

v1.1.0
------
* **Release date**: 2017-02-17.
* **Requires:** [tileserver v1.3.0](https://github.com/mapzen/tileserver/releases/tag/v1.3.0) and [tilequeue v1.4.0](https://github.com/mapzen/tilequeue/releases/tag/v1.4.0) and [mapbox-vector-tile v1.1.0](https://pypi.python.org/pypi/mapbox-vector-tile/1.1.0).
* Replace usage of tile coordinate with usage of nominal zoom. (See https://github.com/tilezen/vector-datasource/pull/1166)

v1.0.3
------
* **Release date**: 2017-01-24.
* **Requires:** [tileserver v1.1.0](https://github.com/mapzen/tileserver/releases/tag/v1.1.0) and [tilequeue v1.2.0](https://github.com/mapzen/tilequeue/releases/tag/v1.2.0) and [mapbox-vector-tile v1.0.0](https://pypi.python.org/pypi/mapbox-vector-tile/1.0.0).
* Clarify documentation license as CC-BY. See [#1136](https://github.com/tilezen/vector-datasource/issues/1136).
* Fix test failures. See [#1148](https://github.com/tilezen/vector-datasource/issues/1148), [#1150](https://github.com/tilezen/vector-datasource/pull/1150), [#1152](https://github.com/tilezen/vector-datasource/pull/1152), [#1157](https://github.com/tilezen/vector-datasource/pull/1157).


v1.0.2
------
* **Release date**: 2016-11-17. _Live on prod 2016-11-21._
* **Requires:** [tileserver v1.0.0](https://github.com/mapzen/tileserver/releases/tag/v1.0.0) and [tilequeue v1.0.1](https://github.com/mapzen/tilequeue/releases/tag/v1.0.1) and [mapbox-vector-tile v1.0.0](https://pypi.python.org/pypi/mapbox-vector-tile/1.0.0).
* Merge water and earth polygons. See [#1106](https://github.com/tilezen/vector-datasource/issues/1106).
* Improve maritime_boundary tagging in Europe and globally by updating buffered_land shapefile. See [#294](https://github.com/tilezen/vector-datasource/issues/294).

v1.0.1
------
* **Release date**: 2016-11-04. _Live on prod 2016-11-04._
* **Requires:** [tileserver v1.0.0](https://github.com/mapzen/tileserver/releases/tag/v1.0.0) and [tilequeue v1.0.1](https://github.com/mapzen/tilequeue/releases/tag/v1.0.1) and [mapbox-vector-tile v1.0.0](https://pypi.python.org/pypi/mapbox-vector-tile/1.0.0).
* Update boundaries query to use overlaps filter to improve performance.

v1.0.0
------
* **Release date**: 2016-10-04. _Live on prod 2016-10-13._
* **Requires:** [tileserver v1.0.0](https://github.com/mapzen/tileserver/releases/tag/v1.0.0) and [tilequeue v1.0.0](https://github.com/mapzen/tilequeue/releases/tag/v1.0.0) and [mapbox-vector-tile v1.0.0](https://pypi.python.org/pypi/mapbox-vector-tile/1.0.0).

---

* **New production URLs:**
    * **GeoJSON:**
      `http://tile.mapzen.com/mapzen/vector/v1/all/{z}/{x}/{y}.json?api_key=mapzen-xxxxxxx`
    * **TopoJSON:**
      `http://tile.mapzen.com/mapzen/vector/v1/all/{z}/{x}/{y}.topojson?api_key=mapzen-xxxxxxx`
    * **Mapbox Vector Tile:**
      `http://tile.mapzen.com/mapzen/vector/v1/all/{z}/{x}/{y}.mvt?api_key=mapzen-xxxxxxx`

---

* Guard against intersecting with same ids during admin boundary processing.
* Rank only features within the unpadded bounds of the tile. Drop unranked features within the unpadded bounds.
* Drop linear boundaries (preferring relation boundaries only), as linear boundaries break the admin boundary processing code.
* Add pyclipper dependency to requirements.
* Include name:short as a tag name alternate.
* Fixed bug to restore some missing low-zoom region boundary lines.
* Fixed bug to fully enable new map_unit boundary lines at low-zooms.
* Low-zoom boundary lines now have custom min_zoom values.
* All features in place layer now have custom min_zoom values.
* Update data query to adapt to upstream OpenStreetMap healthcare speciality bulk edit.
* Fixed typo for protction_title to protection_title for National Forest features in pois layers.
* [docs] Cleanup docs generally, clarify relationship between pois and landuse layers, and remove promise about tier property (which will probably be deprecated).
* [docs] Migrate docs to reference generic Mapzen API keys.


v1.0.0-pre3
-------

* **Release date**: 2016-09-16 (dev build only as public preview)
* **Requires:** [tileserver v0.8.0-pre2](https://github.com/mapzen/tileserver/releases/tag/v0.8.0-pre2) and [tilequeue v0.11.0-pre2](https://github.com/mapzen/tilequeue/releases/tag/v0.11.0-pre2) and [mapbox-vector-tile v0.5.0](https://pypi.python.org/pypi/mapbox-vector-tile/0.5.0).

---

* **Developer preview URLs:** API endpoints have generalized for multiple tile sets, accounts, and versions:
    * **GeoJSON:** http://tile.dev.mapzen.com/mapzen/vector/v1/all/{z}/{x}/{y}.json
    * **TopoJSON:** http://tile.dev.mapzen.com/mapzen/vector/v1/all/{z}/{x}/{y}.topojson
    * **Mapbox Vector Tile:** http://tile.dev.mapzen.com/mapzen/vector/v1/all/{z}/{x}/{y}.mvt
* **Production URLs will be (not yet live):**
    * **GeoJSON:** http://tile.mapzen.com/mapzen/vector/v1/all/{z}/{x}/{y}.json
    * **TopoJSON:** http://tile.mapzen.com/mapzen/vector/v1/all/{z}/{x}/{y}.topojson
    * **Mapbox Vector Tile:** http://tile.mapzen.com/mapzen/vector/v1/all/{z}/{x}/{y}.mvt

---

* Removed "not equals" YAML rule, which can be expressed using the other "equals" and "not" operators. [PR #1044](https://github.com/tilezen/vector-datasource/pull/1044).
* **BREAKING** Rename `sort_key` to `sort_rank`. [PR #1049](https://github.com/tilezen/vector-datasource/pull/1049).
* **BREAKING** Add `/mapzen` prefix to tilejson tiles URL. [PR #1047](https://github.com/tilezen/vector-datasource/pull/1047).
* New version of "static" Natural Earth and OSM shapefiles. [PR #1046](https://github.com/tilezen/vector-datasource/pull/1046).
* Restore buildings to zoom 13. [PR #1036](https://github.com/tilezen/vector-datasource/pull/1036).
* **BREAKING** Fix scalerank 0 region boundaries. Drop name properties on boundaries at zoom <= 6. Add region boundaries sourced from Natural Earth "map_unit" data. [PR #1037](https://github.com/tilezen/vector-datasource/pull/1037).
* Add `min_zoom` parameter to all features. [PR #1031](https://github.com/tilezen/vector-datasource/pull/1031).
* Allow null refs in shield text. Attempt to sanitize shield text by omitting leading text such as `A` or `M` before numeric references. [PR #1039](https://github.com/tilezen/vector-datasource/pull/1039).
* **BREAKING** Update Natural Earth road properties. Removes `level`, `namealt` and `namealtt`. Adds `network` and `shield_text` for some countries. [PR #1035](https://github.com/tilezen/vector-datasource/pull/1035).
* **BREAKING** Fix filters for national forests and parks. Features are now required to have additional parameters (e.g: `operator`, `protect_class`, ...) to classify as a `kind: national_park`. [PR #1034](https://github.com/tilezen/vector-datasource/pull/1034).
* Fix missing localized names on boundaries. Boundaries now include localized `name:left:*` and `name:right:*` where the data is available. [PR #1022](https://github.com/tilezen/vector-datasource/pull/1022).
* Change min zoom for landuse, POIs to be closer to Bubble Wrap. Adds `tier` parameter to simplify client-side rendering rules. [PR #997](https://github.com/tilezen/vector-datasource/pull/997).

v1.0.0-pre2
-------
* **Release date**: 2016-08-31 (dev build only as public preview)
* See detailed Breaking changes, New features, Bug fixes, and Internal Changes sections below.
* **Requires:** [tileserver v0.8.0-pre2](https://github.com/mapzen/tileserver/releases/tag/v0.8.0-pre2) and [tilequeue v0.11.0-pre2](https://github.com/mapzen/tilequeue/releases/tag/v0.11.0-pre2)

  #### BREAKING CHANGES (v1.0.0-pre2)

- **all** layers: Revert to 2 letter language codes to remove client 3-char to 2-char shim logic, with better fallbacks. ([#972](https://github.com/tilezen/vector-datasource/issues/972))

- **boundaries**, **places**, and **roads** layers: Remove raw Natural Earth `scalerank` (see `min_zoom` instead) and `labelrank` properties. ([#992](https://github.com/tilezen/vector-datasource/issues/992))

- **buildings** layer: remove label placements from low- and mid-zooms, keep at zoom 16+. ([#679](https://github.com/tilezen/vector-datasource/issues/679))

- **landuse** layer: Low- and mid-zoom landuse polygons are now merged within the same `kind` values to significantly reduce file size. Some properties, like `name`, `id`, `sport`, `religion`, and `surface` are dropped, and the `area` is recalculated for new combo polygons. [Planned work](https://github.com/tilezen/vector-datasource/issues/473) will add back some detail by adding `scale_rank` classes pre-merge (matching **buildings** layer behavior). ([#583](https://github.com/tilezen/vector-datasource/issues/583))

- **landuse** layer: Remove label placements for `cemetery`, `farm`, `forest`, `forest`, `golf_course`, `grave_yard`, `military`, `national_park`, `natural_forest`, `natural_wood`, `nature_reserve`, `park`, `pitch`, `plant`, `protected_area`, `quarry`, `recreation_ground`, `substation`, `village_green`, `wastewater_plant`, `water_works`, `winter_sports`, `wood`, `works` features, moving them to **pois** layer. Remaining label placements are recommended for text only label treatment.([#742](https://github.com/tilezen/vector-datasource/issues/742))

- **landuse** layer: remove label placements from low- and mid-zooms, keep at zoom 15+. ([#679](https://github.com/tilezen/vector-datasource/issues/679))

- **places** layer: Additional locality changes for places layer to normalize place layer kinds: `capital` changes to `country_capital`, `state_capital` changes to `region_capital`, `scientific_station` localities get their own `kind_detail`, and other bug fixes for ([#840](https://github.com/tilezen/vector-datasource/issues/840)). ([#931](https://github.com/tilezen/vector-datasource/issues/931))

- **pois** layer: Remove the `cuisine` property (see new `kind_detail` instead). ([#719](https://github.com/tilezen/vector-datasource/issues/719))

- **pois** layer: Modify default min_zoom for `gate` features. Gates on major roads are now visible at zoom 14, gates on intermediate roads at zoom 15, gates on minor roads at zoom 16, and gates not on roads at zoom 17 (was all zoom 15). ([#820](https://github.com/tilezen/vector-datasource/issues/820))

- **roads** layer: Remove `aerialway`, `highway`, `piste_type`, `railway`,  in favor of coalescing their values into a new `kind_detail` property (and change incorrect `subkind` reference in documentation to `kind_detail`). ([#970](https://github.com/tilezen/vector-datasource/issues/970))

- **transit** layer: rename `root_relation_id` property to `root_id`, matching new **building** layer configuration. ([#969](https://github.com/tilezen/vector-datasource/pull/969) and [#653](https://github.com/tilezen/vector-datasource/issues/653))

- **water** layer: Remove duplicative and poor resolution `sea` polygons (but keep their label centroids) to save Venice and other cities from early global warming! This also addressed excessive sea labels in most Mapzen house styles. ([#951](https://github.com/tilezen/vector-datasource/issues/951))

  #### NEW FEATURES (v1.0.0-pre2)

- **tilejson**: Major upgrade to reflect all layers and properties. ([#938](https://github.com/tilezen/vector-datasource/issues/938))

- **versioning**: Add semantic versioning (semver) document detailing the promises Tilezen makes about major, minor, and patch versions and data model changes. ([#948](https://github.com/tilezen/vector-datasource/issues/948))

- **buildings** layer: Building parts may receive a `root_id` corresponding to the building feature, if any, with which they intersect. ([#653](https://github.com/tilezen/vector-datasource/issues/653))

- **landuse** layer: Add `graveyard` features. ([#742](https://github.com/tilezen/vector-datasource/issues/742))

- **landuse** layer: Add `camp_site` features for camp grounds. ([#875](https://github.com/tilezen/vector-datasource/issues/875))

- **pois** layer: Add `cemetery`, `farm`, `forest`, `forest`, `golf_course`, `military`, `national_park`, `natural_forest`, `natural_wood`, `nature_reserve`, `park`, `pitch`, `plant`, `protected_area`, `quarry`, `recreation_ground`, `substation`, `village_green`, `wastewater_plant`, `water_works`, `winter_sports`, `wood`, `works` features with adjusted zoom ranges over their previous availability in the **landuse** layer as label placements. All remaining label placements in the **landuse** layer are no longer recommended for icon label treatment. ([#742](https://github.com/tilezen/vector-datasource/issues/742))

- **pois** layer: Add `graveyard` features. ([#742](https://github.com/tilezen/vector-datasource/issues/742))

- **pois** layer: Add art `gallery` features. ([#990](https://github.com/tilezen/vector-datasource/issues/990))

- **pois** layer: Add `kind_detail` property sourced from `sport` for `pitch` features and sourced from `cuisine` for `biergarten`, `pub`, `bar`, `restaurant`, `fast_food`, `cafe` kinds (removing the `cuisine` property). ([#719](https://github.com/tilezen/vector-datasource/issues/719))

- **roads** layer: To support highway shields a new `shield_text` property has been added, `network` values have been normalized (and bicycle networks are now excluded). An example: for "US 101" we now store `network` of  **US:US** and `shield_text` of **101**. Multiple shields are supported via optional `all_networks` and `all_shield_texts` lists (which work in GeoJSON and TopoJSON but not MVT formats, follow [mapbox-vector-tile/#64](https://github.com/tilezen/mapbox-vector-tile/issues/64) for a fix). The `ref` property remains available but is less useful for shield construction. ([#192](https://github.com/tilezen/vector-datasource/issues/192) and [#896](https://github.com/tilezen/vector-datasource/issues/896))

  #### BUG FIXES (v1.0.0-pre2)

- **all** layers: Support fractional zoom for POIs, places, and other featues which were only appearing at the next whole integer tile, and rounds min_zoom values to 2 decimal places. For example: a feature with `min_zoom` of **14.8** was only appearing in zoom **15** tiles when it should have appeared in the zoom **14** tile. ([#976](https://github.com/tilezen/vector-datasource/issues/976))

- **boundaries** layer: Correct bug where `sort_key` mapping wasn't updated for new boundary `kind` values from v1.0.0-pre1. ([#1012](https://github.com/tilezen/vector-datasource/issues/1012))

- **places** layer: Adjust default zoom ranges for Natural Earth localities at the low-zooms and Natural Earth and OpenStreetMap localities at mid- and high-zooms. ([#981](https://github.com/tilezen/vector-datasource/issues/981) and [#982](https://github.com/tilezen/vector-datasource/issues/982))

- **places** layer: Exclude `region_capital=false` properties. ([#1003](https://github.com/tilezen/vector-datasource/pull/1003) and [#931](https://github.com/tilezen/vector-datasource/issues/931))

- **pois** layer: Add OpenStreetMap `source` attribution per feature. ([#922](https://github.com/tilezen/vector-datasource/issues/922))

- **pois** layer: Start querying for pois at z4, not z2 (matching the **landuse** layer). ([#994](https://github.com/tilezen/vector-datasource/pull/994))

- **pois** layer: Show large `camp_site` features at earlier zooms. ([#875](https://github.com/tilezen/vector-datasource/issues/875))

- **pois** layer: Removed transit `halt`, `station`, `stop`, and `tram_stop` features marked as historic. ([#661](https://github.com/tilezen/vector-datasource/issues/661))

- **pois** and **landuse** layers: Normalize `operator` values for `United States National Park Service`, `United States Forest Service`, and `National Parks & WildlWildlifeife Service NSW` in the U.S.A. and Australia. ([#927](https://github.com/tilezen/vector-datasource/issues/927))

- **roads** layer: Pedestrian paths and piers were missing `bicycle: designated` and related tags. Now that they are exported, they are correctly also decorated as `is_bicycle_related: True`. ([#832](https://github.com/tilezen/vector-datasource/issues/832))

- **roads** layer: Add additional properties `sidewalk_left` and `sidewalk_right` to all road layer features. ([#605](https://github.com/tilezen/vector-datasource/issues/605) and [#986](https://github.com/tilezen/vector-datasource/issues/986))

- **roads** layer: Remove `crossing`, `sidewalk`, `sidewalk_left` and `sidewalk_right` properties for road merge. ([#993](https://github.com/tilezen/vector-datasource/issues/993))

- **roads** layer: Drop meaningless `id` property on merged features. ([#952](https://github.com/tilezen/vector-datasource/issues/952))

- **transit** layer: Add OpenStreetMap `source` attribution per feature. ([#935](https://github.com/tilezen/vector-datasource/issues/935))

  #### DOCUMENTATION CHANGES (v1.0.0-pre2)

- **documentation**: Update **earth** layer documentation to reflect additional `line` and `point` geometry types. ([#808](https://github.com/tilezen/vector-datasource/issues/808))

- **documentation**: Update **boundaries** and **landuse** layer documentation to reflect barriers moving into the landuse layer. ([#932](https://github.com/tilezen/vector-datasource/issues/932))

- **documentation**: Update **places** layer documentation to reflect new `kind` and `kind_detail` values, locality, suburb, quarter, state, province, region, capital, and other changes. ([#934](https://github.com/tilezen/vector-datasource/issues/934))

- **documentation**: Update **buildings** layer documentation to reflect new `kind` and `kind_detail` values and `building_part` changes. ([#933](https://github.com/tilezen/vector-datasource/issues/933)) and related ([#842](https://github.com/tilezen/vector-datasource/issues/842))

- **documentation**: Update **roads** layer documentation to reflect new `kind` and `kind_detail` values, and remove erroneous reference to `exit`. ([#936](https://github.com/tilezen/vector-datasource/issues/936))

- **contributing**: Adding a step to create a `test_config.yaml` file. ([#1001](https://github.com/tilezen/vector-datasource/pull/1001))


  #### INTERNAL CHANGES (v1.0.0-pre2)

- **performance**: Move label centroid calculation to database to reduce network pressure on the database (post processing transform needed too much geometry) in **landuse**, **water**, **earth**, and **buildings** layers. ([#965](https://github.com/tilezen/vector-datasource/issues/965))

- **performance**: Add pois indexes for OpenStreetMap polygon and point tables to improve query time. ([#983](https://github.com/tilezen/vector-datasource/issues/983))

- **database**: Convert Postgres PostGIS database to utilize osm2pgsql's `--hstore-all` option. ([#876](https://github.com/tilezen/vector-datasource/issues/876))

- **database**: Convert Postgres PostGIS database projection to `EPSG:3857`. ([#908](https://github.com/tilezen/vector-datasource/issues/908))

- **database**: Convert `min_zoom` properties to REAL from INT to support fractional values. ([#976](https://github.com/tilezen/vector-datasource/issues/976))

- **import**: Remove default `-W UTF-8` from data import config for shp2pgsql. ([#946](https://github.com/tilezen/vector-datasource/issues/946))

- **import**: Add shim in apply non planet sql to better accommodate invalid geometries. Track longer term fix in #979. ([#1003](https://github.com/tilezen/vector-datasource/pull/1003))

- **indexes**: Update road indexes to refer to `mz_road_level` alone. ([#956](https://github.com/tilezen/vector-datasource/pull/956))

- **tests**: Correct test failure for hotels as upstream data had changed. ([#959](https://github.com/tilezen/vector-datasource/pull/959))

- **tests**: Ensure that when `config_all_layers` is set, the **all** layer is requested. ([#974](https://github.com/tilezen/vector-datasource/pull/974))


v1.0.0-pre1
-------
* **Release date**: 2016-07-22 (dev build only as public preview)
* See detailed Breaking changes, New features, Bug fixes, and Internal Changes sections below.
* **Requires:** [tileserver v0.8.0.dev0](https://github.com/mapzen/tileserver/releases/tag/v0.8.0.dev0) and [tilequeue v0.11.0.dev0](https://github.com/mapzen/tilequeue/releases/tag/v0.11.0.dev0)

  #### BREAKING CHANGES (v1.0.0-pre1)

- **new url scheme**: Mapzen now offers several different types of tiles in vector and raster formats and we combine data from multiple sources. The URL scheme has been updated to reflect this, and emphasize versions. The old URL will continue to work (~1 year), but updates will stop once v1.0.0 is released to production. ([#652](https://github.com/tilezen/vector-datasource/issues/652))

  - **New dev URL:** `http://tile.dev.mapzen.com/vector/v1/all/{z}/{x}/{y}.topojson`

  - Old dev URL was: `http://vector.dev.mapzen.com/osm/all/{z}/{x}/{y}.topojson`

  - **New prod URL will be:** `https://tile.mapzen.com/vector/v1/all/{z}/{x}/{y}.topojson`

  - Old prod URL is still: `https://vector.mapzen.com/osm/all/{z}/{x}/{y}.topojson`

  - **New dev TileJSON is:** `http://tile.dev.mapzen.com/vector/v1/tilejson/mapbox.json`

  - New prod TileJSON will be: `https://tile.mapzen.com/vector/v1/tilejson/mapbox.json`

  - Old prod TileJSON is still: `https://vector.mapzen.com/osm/tilejson/mapbox.json`

- **roads** layer: Reclassify airport runway and taxiways as new `aeroway` kind (was `minor_road`), and change their sort order to be under equivalent landuse polygons. ([#895](https://github.com/tilezen/vector-datasource/issues/895))

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

- **buildings** layer: Reclassify building layer kind values to only have `building` or `building_part`, moved the earlier kind values to new `kind_detail` property with a whitelist of values. ([#842](https://github.com/tilezen/vector-datasource/issues/842))

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


v0.10.5
-------
* **Release date**: 2016-08-17
* Backport moving label generation to database. See [#965](https://github.com/tilezen/vector-datasource/issues/965).

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
