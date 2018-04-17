# Layers in Mapzen's vector tiles

![image](images/mapzen-vector-tile-docs-all-layers.png)

The [Mapzen vector tile service](https://mapzen.com/projects/vector-tiles) provides worldwide basemap coverage sourced from [OpenStreetMap](www.openstreetmap.org) and other open data projects, updated daily as a free & shared service.

Data is organized into several thematic layers, each of which is named, for example; `buildings`, `pois`, and `water`. A selection of these layers are typically used for base map rendering, and are provided under the short-hand name `all`. Each layer includes a simplified view of OpenStreetMap data for easier consumption, with common tags often condensed into a single `kind` field as noted below.

Need help displaying vector tiles in a map? Here are several [examples](display-tiles.md) using Mapzen vector tiles to style in your favorite graphics library including Tangram, Mapbox GL, D3, and OpenLayers.

### Overview

#### Data sources and attribution

Mapzen primarily sources from OpenStreetMap, but includes a variety of other open data. For a full listing, view the [data sources](data-sources.md). Each source may require [attribution](https://github.com/tilezen/vector-datasource/blob/master/docs/attribution.md) in your project.

#### Feature names

Most Mapzen vector tile features include a basic name property (`common`):

* `name` - Generally the name the locals call the feature, in the local script.

It supports several additional name related properties (`optional`):

* `alt_name`
* `int_name`
* `loc_name`
* `name:short` - For example: `CA` for California. _See planned bug fix [#1102](https://github.com/tilezen/vector-datasource/issues/1102) and see planned bug fix [#1094](https://github.com/tilezen/vector-datasource/issues/1094) for abbreviated names._
* `name_left`
* `name_right`
* `nat_name`
* `official_name`
* `old_name`
* `reg_name`
* `short_name`

#### Name localization

Mapzen includes all language variants of the `name:*` values to enable full internationalization (when different from `name`).

Language variants are identified by an ISO 639-1 two-letter language code and optional country code, for example `en` for English and less commonly `en_GB` for British English. Mapzen [house styles](https://mapzen.com/products/maps/) designed in Tangram support displaying all language scripts.

We additionally localize `alt_name:*` and `old_name:*` properties for features across all layers.

For features in the `boundaries` layer, there are two additional variants `name:left` and `name:right` to support oriented labeling on the appropriate side of the boundary line (so the labeled polygon's text can appear inside that polygon consistently). _See planned bug fix [#1102](https://github.com/tilezen/vector-datasource/issues/1102)._

**Localized name properties** (`common-optional`)**:**

* `name:*`
* `alt_name:*`
* `old_name:*`
* `name:left:*` _See planned bug fix [#1102](https://github.com/tilezen/vector-datasource/issues/1102)._
* `name:right:*` _See planned bug fix [#1102](https://github.com/tilezen/vector-datasource/issues/1102)._

#### Geometry types

Individual Mapzen vector tile layers can include mixed geometry types. This is common in the `landuse`, `water`, and `buildings` layers.

A tile geometry can be one of three types:

* Point, MultiPoint
* LineString, MultiLineString
* Polygon, MultiPolygon

In Tangram, Mapzen's GL graphics library, the keyword `$geometry` matches the feature's geometry type, for cases when a FeatureCollection includes more than one type of kind of geometry. Valid geometry types are:

* `point`: matches Point, MultiPoint
* `line`: matches LineString, MultiLineString
* `polygon`: matches Polygon, MultiPolygon

**Tangram scene file examples:**

```
filter: { $geometry: polygon }            # matches polygons only
filter: { $geometry: [point, line] }      # matches points & lines
filter: function() { return $geometry === 'line' }  # matches lines
```

Mapnik supports geometry filtering via the special `mapnik::geometry_type` keyword.

**CartoCSS Examples:**

```
#layer['mapnik::geometry_type'=1] { /* point styles */ }
#layer['mapnik::geometry_type'=2] { /* line styles */ }
#layer['mapnik::geometry_type'=3] { /* polygon styles */ }
```

#### Data updates

Most Mapzen vector tile content is updated minutely from OpenStreetMap. Low and mid-zoom tiles are updated approximately monthly. Some source data rarely updates – Natural Earth updates approximately yearly.

#### Changelog

The current version of Mapzen vector tile "Tilezen" data model is **v1.2.0**.

Tiles are still in active development, but Mapzen promises to minimize backwards incompatible breaking changes. Data model promises are listed in the Tilezen [SEMANTIC VERSIONING](https://github.com/mapzen/vector-datasource/tree/master/SEMANTIC-VERSIONING.md) statement.

If you're signed up for a [Mapzen API key](https://mapzen.com/developers) you should receive an email notifying you of upcoming changes before they are rolled out to production. You can also send your feedback at hello@mapzen.com!

Read the full details in the project [CHANGELOG](https://github.com/mapzen/vector-datasource/tree/v1.0.0/CHANGELOG.md).

#### Feature ordering

Ordering of features - which ones draw "on top of" other features - can be an important feature of display maps. To help out with this, there is a `sort_rank` property on some features which suggests in what order the features should appear. Lower numbers mean that features should appear "towards the back" and higher numbers mean "towards the front". These numbers are consistent across layers. The layers which include `sort_rank` on their features are: `boundaries`, `buildings`, `earth`, `landuse`, `roads`, `transit` and `water`.

To facilitate **data visualization** overlays and underlays, the following client-side `order` ranges are suggested:

* `0-9`: Under everything. _Tip: disable earth layer._
* `190-199`: Under water. Above earth and most landuse.
* `290-299`: Under roads. Above borders, water, landuse, and earth. **Your classic "underlay".**
* `490-499`: Over all line and polygon features. Under map labels (icons and text), under UI elements (like routeline and search result pins). **Your classic raster map overlay.**

**Tangram scene file example:**

```
draw:
    polygons:
        order: 490
```

### Layer reference

Mapzen vector tiles include 9 layers:

* `boundaries`, `buildings`, `earth`, `landuse`, `places`, `pois`, `roads`, `transit`, and `water`

These individual layers are grouped into an `all` layer – use this special layer for all your general purpose mapping needs.

While the service can return just a single layer or combination of layers, the `all` layer is more performant.

## Boundaries

![image](images/mapzen-vector-tile-docs-boundaries.png)

* Layer name: `boundaries`
* Geometry types: `line`

Combination of OpenStreetMap administrative boundaries (zoom >= 8) and Natural Earth boundaries (zoom < 8).


#### Boundaries properties (common):

* `name`
* `id`
* `kind`: mapping of OpenStreetMap's `admin_level` int values to strings like `country` and `state`, plus `aboriginal_lands` boundary type, and also includes normalized Natural Earth values.
* `kind_detail`: mapping of OpenStreetMap's `admin_level` values. `2` for countries, `4` for regions, and `6`, `8` (zoom 10+)
* `source`: `openstreetmap.org` or `naturalearthdata.com`
* `sort_rank`: a suggestion for which order to draw features. The value is an integer where smaller numbers suggest that features should be "behind" features with larger numbers.
* `min_zoom`: a suggested minimum zoom at which the boundary line should become visible based on scalerank value from Natural Earth, and invented for OpenStreetMap, a float.

#### Boundaries properties (common optional):

* `id:left`: For the relation on the left side of the boundary line.
* `id:right`: For the relation on the right side of the boundary line.
* `name:left`: See name section above, other variants like `old_name` also supported. _See planned bug fix in [#1102](https://github.com/tilezen/vector-datasource/issues/1102)._
* `name:right`: See name section above, other variants like `old_name` also supported. _See planned bug fix in [#1102](https://github.com/tilezen/vector-datasource/issues/1102)._
* `maritime_boundary`: a special Mapzen calculated value loosely coupled with OpenStreetMap's maritime tag, but with spatial buffer processing for lines falling in the ocean.

#### Boundaries properties (optional):

* `osm_relation`: `true`, which can also be deduced from negative `id` values.

#### Boundary `kind` values:

* `aboriginal_lands`
* `country`
* `county`
* `disputed`
* `indefinite`
* `indeterminate`
* `lease_limit`
* `line_of_control`
* `locality`
* `macroregion`
* `map_unit`
* `overlay_limit`
* `region`

## Buildings and Addresses

![image](images/mapzen-vector-tile-docs-buildings.png)

* Layer name: `buildings`
* Geometry types: `point` and `polygon`

Polygons from OpenStreetMap representing building footprints, building label placement points, building_part features, and address points. Starts at zoom 13 by including huge buildings, progressively adding all buildings at zoom 16+. Address points are available at zoom 16+, but marked with `min_zoom: 17` to suggest that they are suitable for display at zoom level 17 and higher.

Individual `building_part` geometries from OpenStreetMap following the [Simple 3D Buildings](http://wiki.openstreetmap.org/wiki/Simple_3D_Buildings) tags at higher zoom levels. Building parts may receive a `root_id` corresponding to the building feature, if any, with which they intersect.

Mapzen calculates the `landuse_kind` value by intercutting `buildings` with the `landuse` layer to determine if a building is over a parks, hospitals, universities or other landuse features. Use this property to modify the visual appearance of buildings over these features. For instance, light grey buildings look great in general, but aren't legible over most landuse colors unless they are darkened (or colorized to match landuse styling).

Label position points may also have `closed` or `historical` kind_detail values if the original building name ended in "(closed)" or "(historical)", respectively. These points will have a `min_zoom` of 17, suggesting that they are suitable for display only at high zooms. _See related bug fix in [#1026](https://github.com/tilezen/vector-datasource/issues/1026)._

Values for `kind_detail`  are sourced from OpenStreetMap's `building` tag for building footprints and from `building:part` tag for building parts.

Note that building geometries, like most geometries in Tilezen tiles, are clipped to the bounds of the tile, even if the building extends beyond the tile. This means that it might be necessary to assemble geometry from several neighbouring tiles to recreate the full building. Some buildings are exceptionally large and span many tiles, so this can be tricky.

#### Building properties (common):

* `name`
* `id`: from OpenStreetMap
* `kind`: see below
* `kind_detail`: see below
* `source`: `openstreetmap.org`
* `landuse_kind`: See description above, values match values in the `landuse` layer.
* `sort_rank`: a suggestion for which order to draw features. The value is an integer where smaller numbers suggest that features should be "behind" features with larger numbers.
* `min_zoom`: a suggested minimum zoom at which the building should become visible based on area and volume limits.

#### Building properties (common optional):

* `addr_housenumber`: value from OpenStreetMap's `addr:housenumber` tag
* `addr_street`: value from OpenStreetMap's `addr:street` tag
* `area`: in square meters (spherical Mercator, no real-world), `polygon` features only. _See planned bug fix in [#1095](https://github.com/tilezen/vector-datasource/issues/1095)._
* `building_material`: A description of the material covering the outside of the building or building part, if the information is available. Common values are: `brick`, `cement_block`, `clay`, `concrete`, `glass`, `masonry`, `metal`, `mud`, `other`, `permanent`, `plaster`, `sandstone`, `semi-permanent`, `steel`, `stone`, `timber-framing`, `tin`, `traditional` and `wood`, and there are many other less common values.
* `height`: in meters, where available
* `layer`
* `location`: from OpenStreetMap to indicate if building is underground, similar to `layer`.
* `min_height`: value from `min_height` in meters, where available, otherwise estimated from `building:min_levels` if present
* `roof_color`: from `roof:color` tag
* `roof_height`: from `roof:height` tag
* `roof_material`: from `roof:material` tag
* `roof_orientation`: from `roof:orientation` tag
* `roof_shape`: from `roof:shape` tag
* `scale_rank`: calculation of a feature's importance
* `volume`: calculated on feature's `area` and `height`, when `height` or `min_height` is available. _See planned bug fix in [#1095](https://github.com/tilezen/vector-datasource/issues/1095)._

#### Building layer `kind` values:

* `building`
* `building_part`
* `address`

#### Building footprint and label placement `kind_detail` values:

* `abandoned`
* `administrative`
* `agricultural`
* `airport`
* `allotment_house`
* `apartments`
* `arbour`
* `bank`
* `barn`
* `basilica`
* `beach_hut`
* `bell_tower`
* `boathouse`
* `brewery`
* `bridge`
* `bungalow`
* `bunker`
* `cabin`
* `carport`
* `castle`
* `cathedral`
* `chapel`
* `chimney`
* `church`
* `civic`
* `clinic`
* `closed`. _See planned bug fix in [#1026](https://github.com/tilezen/vector-datasource/issues/1026)._
* `clubhouse`
* `collapsed`
* `college`
* `commercial`
* `construction`
* `container`
* `convent`
* `cowshed`
* `dam`
* `damaged`
* `depot`
* `destroyed`
* `detached`
* `disused`
* `dormitory`
* `duplex`
* `factory`
* `farm`
* `farm_auxiliary`
* `fire_station`
* `garage`
* `garages`
* `gazebo`
* `ger`
* `glasshouse`
* `government`
* `grandstand`
* `greenhouse`
* `hangar`
* `healthcare`
* `hermitage`
* `historical`. _See planned bug fix in [#1026](https://github.com/tilezen/vector-datasource/issues/1026)._
* `hospital`
* `hotel`
* `house`
* `houseboat`
* `hut`
* `industrial`
* `kindergarten`
* `kiosk`
* `library`
* `mall`
* `manor`
* `manufacture`
* `mixed_use`
* `mobile_home`
* `monastery`
* `mortuary`
* `mosque`
* `museum`
* `office`
* `outbuilding`
* `parking`
* `pavilion`
* `power`
* `prison`
* `proposed`
* `pub`
* `public`
* `residential`
* `restaurant`
* `retail`
* `roof`
* `ruin`
* `ruins`
* `school`
* `semidetached_house`
* `service`
* `shed`
* `shelter`
* `shop`
* `shrine`
* `silo`
* `slurry_tank`
* `stable`
* `stadium`
* `static_caravan`
* `storage`
* `storage_tank`
* `store`
* `substation`
* `summer_cottage`
* `summer_house`
* `supermarket`
* `synagogue`
* `tank`
* `temple`
* `terrace`
* `tower`
* `train_station`
* `transformer_tower`
* `transportation`
* `university`
* `utility`
* `veranda`
* `warehouse`
* `wayside_shrine`
* `works`

Additional `kind_detail` values are provided from POI `kind`s where one is not available from the building feature. This means that you could see any POI `kind` value as a building `kind_detail` value.

#### Building part `kind_detail` values:

* `arch`
* `balcony`
* `base`
* `column`
* `door`
* `elevator`
* `entrance`
* `floor`
* `hall`
* `main`
* `passageway`
* `pillar`
* `porch`
* `ramp`
* `roof`
* `room`
* `steps`
* `stilobate`
* `tier`
* `tower`
* `verticalpassage`
* `wall`
* `window`

## Earth

![image](images/mapzen-vector-tile-docs-earth.png)

* Layer name: `earth`
* Geometry types: `polygon`, `line`, `point`.

Polygons representing earth landmass and natural feature lines. Uses coastline-derived land polygons from [openstreetmapdata.com](http://openstreetmapdata.com). Natural lines from OpenStreetMap representing cliffs, aretes. This layer also includes earth `label_placement` lines for ridges and valleys (which should not otherwise be symbolized).

_Uses Natural Earth until zoom 7, then switches to OSM land at zoom 8+._

**Earth properties:**

* `name`: generally only for lines or label placement points
* `id`: The `osm_id` **or** funky value when from Natural Earth or OpenStreetMapData.com
* `kind`: either `earth` or "natural" value from OSM tag.
* `source`: `openstreetmap.org` or `naturalearthdata.com`
* `sort_rank`: a suggestion for which order to draw features. The value is an integer where smaller numbers suggest that features should be "behind" features with larger numbers.
* `min_zoom`: a suggestion for which zoom to draw a feature. The value is a float. _See planned bug fix in [#1073](https://github.com/tilezen/vector-datasource/issues/1073)._

#### Earth `kind` values:

* `archipelago` - point, intended for label placement only
* `arete` - line
* `cliff` - line, intended for label placement only
* `continent` - point, intended for label placement only
* `earth` - polygon
* `island` - point, intended for label placement only
* `islet` - point, intended for label placement only
* `ridge` - line, intended for label placement only
* `valley` - line, intended for label placement only

## Landuse

![image](images/mapzen-vector-tile-docs-landuse.png)

* Layer name: `landuse`
* Geometry types: `point` and `polygon`

Landuse polygons from OpenStreetMap representing parks, forests, residential, commercial, industrial, university, sports and other areas. Includes OpenStreetMap data at higher zoom levels, and [Natural Earth](http://naturalearthdata.com) polygons at lower zoom levels. This layer also includes landuse `label_placement` points for labeling polygons de-duplicated across tile boundaries.

Zooms 4 and 5, 6 and 7 includes a mix of Natural Earth `urban_area` (zooms 0-9 only) features and OpenStreetMap data for `national_park`, `protected_area`, and `nature_reserve` only. After that more more feature kinds are included, and they have a richer set of properties including `sport`, `religion`, `surface`, `attraction`, `zoo`, and `natural`. Feature selection is filtered per zoom until zoom 15.

At mid- and low-zooms, between 4-12, some landuse polygons are merged to reduce payload size. To facilitate this, the name of the landuse area may be dropped for small polygons. When polygons are merged, the original `id` properties are dropped, and the `area` is re-calculated for the new size.

_TIP: Some `landuse` features only exist as point features in OpenStreetMap. Find those in the `pois` layer._

(below) Fence lines around the petting zoo in San Francisco are included in the `landuse` layer.

![image](images/mapzen-vector-tile-docs-barriers.png)

#### Landuse properties (common):

* `name`
* `id`: From OpenStreetMap or Natural Earth. Dropped at low- and mid-zooms when features are merged. _See planned bug fix [#1033](https://github.com/tilezen/vector-datasource/issues/1033)._
* `kind`: combination of the `landuse`, `leisure`, `natural`, `highway`, `aeroway`, `amenity`, `tourism`, `zoo`, `attraction`, `man_made`, `power`, and `boundary` OSM tags, or `urban_area` for Natural Earth features. Also includes of some `barrier` and `waterway` tags: `city_wall` (zoom 12+), `dam` (zoom 12+), `power_line` (zoom 14+), `retaining_wall`, `snow_fence` (zoom 15+), `fence`, `gate`, `wall` (zoom 16+ only), and `power_minor_line` (zoom 17+).
* `source`: `openstreetmap.org` or `naturalearthdata.com`
* `sort_rank`: a suggestion for which order to draw features. The value is an integer where smaller numbers suggest that features should be "behind" features with larger numbers.
* `area`: in square meters (spherical Mercator, no real-world), `polygon` features only
* `min_zoom`: a suggestion for which zoom to draw a feature. The value is a float.

#### Landuse properties (common optional):

* `protect_class`: Common values include `1`, `2`, `3`, `4`, `5`, `6`. See [OSM wiki](https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dprotected_area#Protect_classes_for_various_countries) for more information.
* `operator`: e.g. `United States National Park Service`, `United States Forest Service`, `National Parks & Wildlife Service NSW`.

#### Landuse `kind` values:

* `aerodrome`
* `allotments`
* `amusement_ride`
* `animal`
* `apron`
* `aquarium`
* `artwork`
* `attraction`
* `aviary`
* `battlefield`
* `beach`
* `breakwater`
* `bridge`
* `camp_site`
* `caravan_site`
* `carousel`
* `cemetery`
* `cinema`
* `city_wall`
* `college`
* `commercial`
* `common`
* `cutline`
* `dam` - polygon, line
* `dike`
* `dog_park`
* `enclosure`
* `farm`
* `farmland`
* `farmyard`
* `fence`
* `footway`
* `forest`
* `fort`
* `fuel`
* `garden`
* `gate`
* `generator`
* `glacier`
* `golf_course`
* `grass`
* `grave_yard`
* `groyne`
* `hanami`
* `hospital`
* `industrial`
* `land`
* `library`
* `maze`
* `meadow`
* `military`
* `national_park`
* `nature_reserve`
* `natural_forest` - _See planned bug fix in [#1096](https://github.com/tilezen/vector-datasource/issues/1096)._
* `natural_park` - _See planned bug fix in [#1096](https://github.com/tilezen/vector-datasource/issues/1096)._
* `natural_wood` - _See planned bug fix in [#1096](https://github.com/tilezen/vector-datasource/issues/1096)._
* `park`
* `parking`
* `pedestrian`
* `petting_zoo`
* `picnic_site`
* `pier`
* `pitch`
* `place_of_worship`
* `plant`
* `playground`
* `power_line`
* `power_minor_line`
* `prison`
* `protected_area`
* `quarry`
* `railway`
* `recreation_ground`
* `recreation_track`
* `residential`
* `resort`
* `rest_area`
* `retail`
* `retaining_wall`
* `rock`
* `roller_coaster`
* `runway`
* `rural`
* `school`
* `scree`
* `scrub`
* `service_area`
* `snow_fence`
* `sports_centre`
* `stadium`
* `stone`
* `substation`
* `summer_toboggan`
* `taxiway`
* `theatre`
* `theme_park`
* `tower`
* `trail_riding_station`
* `university`
* `urban_area`
* `urban`
* `village_green`
* `wall`
* `wastewater_plant`
* `water_park`
* `water_slide`
* `water_works`
* `wetland`
* `wilderness_hut`
* `wildlife_park`
* `winery`
* `winter_sports`
* `wood`
* `works`
* `zoo`

#### Cemetery and grave_yard `kind_detail` values:

The value of the OpenStreetMap `religion` tag is used for `kind_detail` on `cemetery` and `grave_yard` features. Common values include `animist`, `bahai`, `buddhist`, `caodaism`, `catholic`, `christian`, `confucian`, `hindu`, `jain`, `jewish`, `multifaith`, `muslim`, `pagan`, `pastafarian`, `scientologist`, `shinto`, `sikh`, `spiritualist`, `taoist`, `tenrikyo`, `unitarian_universalist`, `voodoo`, `yazidi`, and `zoroastrian`.

NOTE: A `denomination` attribute is also available with the value of the OpenStreetMap denomination tag. Common values include `adventist`, `anglican`, `armenian_apostolic`, `assemblies_of_god`, `baptist`, `buddhist`, `bulgarian_orthodox`, `catholic`, `christian`, `church_of_scotland`, `episcopal`, `evangelical`, `greek_catholic`, `greek_orthodox`, `iglesia_ni_cristo`, `jehovahs_witness`, `lutheran`, `mennonite`, `methodist`, `mormon`, `new_apostolic`, `nondenominational`, `orthodox`, `pentecostal`, `presbyterian`, `protestant`, `quaker`, `reformed`, `roman_catholic`, `romanian_orthodox`, `russian_orthodox`, `salvation_army`, `serbian_orthodox`, `seventh_day_adventist`, `shia`, `shingon_shu`, `sunni`, `theravada`, `tibetan`, `united`, `united_methodist`, `united_reformed`, `uniting`, and `曹洞宗`.

#### Fence `kind_detail` values:

The value of the OpenStreetMap `fence_type` tag. Common values include `avalanche`, `barbed_wire`, `bars`, `brick`, `chain`, `chain_link`, `concrete`, `electric`, `hedge`, `metal`, `metal_bars`, `net`, `pole`, `railing`, `split_rail`, `stone`, `wall`, `wire`, and `wood`.

#### Wall `kind_detail` values:

The value of the OpenStreetMap `wall` tag. Common values include `brick`, `castle_wall`, `concrete`, `dry_stone`, `drystone`, `flood_wall`, `gabion`, `jersey_barrier`, `noise_barrier`, `pise`, `retaining_wall`, `seawall`, `stone`, and `stone_bank`.

##### Wetland `kind_detail` values:

The value of the OpenStreetMap `wetland` tag. Common values include `bog`, `fen`, `mangrove`, `marsh`, `reedbed`, `saltmarsh`, `string_bog`, `swamp`, `tidalflat`, and `wet_meadow`.

#### Wood and forest `kind_detail` values

* The value of the OpenStreetMap `leaf_type` tag. [Common values](https://taginfo.openstreetmap.org/keys/leaf_type#values) include `broadleaved`, `needleleaved`, or `mixed`.

## Places

![image](images/mapzen-vector-tile-docs-places.png)

* Layer name: `places`
* Geometry types: `point`

Combination of OpenStreetMap `place` points, Natural Earth populated places, and Who's On First neighbourhoods.

Places with `kind` values of `continent`, `country`, with others added starting at zoom 4 for `region` and starting at zoom 8 for `locality`. Specific `locality` and `region` types are added to the `kind_detail` tag.

![image](images/mapzen-vector-tile-docs-places-neighbourhoods.png)

**Neighbourhoods:** [Who's On First](http://whosonfirst.mapzen.com) `neighbourhood` and `macrohood` features are added starting at zoom 12. Neighbourhoods are included one zoom earlier than their `min_zoom`, and stay included 1 zoom past their `max_zoom`.


#### Place properties (common):

* `name`
* `id`: The `osm_id` from OpenStreetMap or Natural Earth id
* `kind`: normalized values between OpenStreetMap and Natural Earth
* `population`: population integer values from OpenStreetMap or Natural Earth's maximum population value.
* `source`: `openstreetmap`, `naturalearthdata.com`, or  `whosonfirst.mapzen.com`
* `min_zoom`: a suggested minimum zoom at which the place should become visible based on scalerank and population values from Natural Earth, and invented for OpenStreetMap. Note that this is not an integer, and may contain fractional parts.

#### Place properties (common optional):

* `country_capital`: a `true` value normalizes values between OpenStreetMap and Natural Earth for kinds of `Admin-0 capital`, `Admin-0 capital alt`, and `Admin-0 region capital`.
* `region_capital`: a `true` value normalizes values between OpenStreetMap and Natural Earth for kinds of `Admin-1 capital` and `Admin-1 region capital`.
* `max_zoom`: a suggested maximum zoom beyond which the place should not be visible. Currently neighbourhoods only, from Who's On First.
* `is_landuse_aoi`: Currently neighbourhoods only, from Who's On First
* `kind_detail`: the original value of the OSM `place` tag and Natural Earth `featurecla`, see below.

#### Place `kind` values:

* `borough`
* `country`
* `locality`
* `macrohood`
* `microhood`
* `neighbourhood`
* `region`

#### Place `kind_detail` values:

Primarily these are available for features of kind `locality` or `region`.

* `city`
* `farm`
* `hamlet`
* `isolated_dwelling`
* `locality`
* `province`
* `scientific_station`
* `state`
* `town`
* `village`

## Points of Interest

![image](images/mapzen-vector-tile-docs-pois.png)

* Layer name: `pois`
* Geometry types: `point`

Over 200 points of interest (POI) kinds are supported. POIs are included starting at zoom 4 for `national_park`, zoom 9 for `park`, and zoom 12 for other major features like `airport`, `hospital`, `zoo`, and `motorway_junction`. Progressively more features are added at each additional zoom based on a combination of feature area (if available) and `kind` value. For instance, by zoom 15 most `police`, `library`, `university`, and `beach` features are included, and by zoom 16 things like `car_sharing`, `picnic_site`, and `tree` are added. By zoom 16 all local features are added, like `amusement_ride`, `atm`, and `bus_stop`, but may be marked with a `min_zoom` property to suggest at which zoom levels they are suitable for display. For example, `bench` and `waste_basket` features may be marked `min_zoom: 18` to suggest that they are displayed at zoom 18 and higher.  Note that `min_zoom` is not an integer, and may contain a fractional component.

NOTE: The `pois` layer includes point "labels" for most polygon features otherwise found in the `landuse` layer (eg: `national_park` and `park`); these points are suitable for drawing as icon-and-text labels. The remaining `label_position` points in the `landuse` layer and `buildings` layer are suitable for text-only labels.

Points of interest from OpenStreetMap, with per-zoom selections similar to the primary [OSM.org Mapnik stylesheet](https://trac.openstreetmap.org/browser/subversion/applications/rendering/mapnik).

Features from OpenStreetMap which are tagged `disused=*` for any other value than `disused=no` are not included in the data. Features which have certain parenthetical comments after their name are suppressed until zoom 17 and have their `kind` property set to that comment. Currently anything with a name ending in '(closed)' or '(historical)' will be suppressed in this manner. Railway stops, halts, stations and tram stops from OpenStreetMap tagged with a `historic` tag are also not included in the data.

To resolve inconsistency in data tagging in OpenStreetMap we normalize several operator values for United States National Parks as `United States National Park Service`, several United States Forest Service values as `United States Forest Service`, and several values for New South Wales National Parks in Australia as `National Parks & Wildlife Service NSW`.

#### POI properties (common):

* `name`
* `id`
* `source`: `openstreetmap.org`
* `kind`: combination of the `aerialway`, `aeroway`, `amenity`, `attraction`, `barrier`, `craft`, `highway`, `historic`, `leisure`, `lock`, `man_made`, `natural`, `office`, `power`, `railway`, `rental`, `shop`, `tourism`, `waterway`, and `zoo` tags. Can also be one of `closed` or `historical` if the original feature was parenthetically commented as closed or historical.
* `min_zoom`: a suggested minimum zoom at which the POI should become visible. Note that this is not an integer, and may contain fractional parts.

#### POI properties (common optional):

* `kind_detail`: cuisine, sport
* `attraction`:
* `exit_to`: only for highway exits
* `ref`: generally only for `aeroway_gate` and `station_entrance` features
* `religion`:
* `zoo`:

#### POI properties (only on `kind:station`):

* `state`: only on `kind:station`, status of the station. Values include: `proposed`, `connection`, `inuse`, `alternate`, `temporary`.
* `*_routes`: a list of the reference name/number or full name (if there is no `ref`) of the OSM route relations which are reachable by exploring the local public transport relations or site relations. These are:
  * `train_routes` a list of train routes, generally above-ground and commuter or inter-city "heavy" rail.
  * `subway_routes` a list of subway or underground routes, generally underground commuter rail.
  * `light_rail_routes` a list of light rail or rapid-transit passenger train routes.
  * `tram_routes` a list of tram routes.
* `is_*` a set of boolean flags indicating whether this station has any routes of the given type. These are: `is_train`, `is_subway`, `is_light_rail`, `is_tram`, corresponding to the above `*_routes`. This is provided as a convenience for styling.
* `root_id` an integer ID (of an OSM relation) which can be used to link or group together features which are related by being part of a larger feature. A full explanation of [relations](http://wiki.openstreetmap.org/wiki/Relation) wouldn't fit here, but the general idea is that all the station features which are part of the same [site](http://wiki.openstreetmap.org/wiki/Relation:site), [stop area](http://wiki.openstreetmap.org/wiki/Tag:public_transport%3Dstop_area) or [stop area group](http://wiki.openstreetmap.org/wiki/Relation:public_transport) should have the same ID to show they're related. Note that this information is only present on some stations.

#### POI properties (only on `kind:bicycle_rental_station`):

* `capacity`: Approximate number of total rental bicycles at the bike share station.
* `network`: The common (sometimes branded) name of the bike share network, eg: "Citi Bike".
* `operator`: Who actually runs the bike share station, eg: "NYC Bike Share".
* `ref`: The reference of this rental station, if one is available.

#### POI properties (only on `kind:bicycle_parking` and `kind:motorcycle_parking`):

* `access`: Whether the parking is for general public use (`yes`, `permissive`, `public`) or for customers only (`customers`) or private use only (`private`, `no`).
* `capacity`: Approximate number of total bicycle parking spots.
* `covered`: Is the parking area covered.
* `fee`: If present, indicates whether a fee must be paid to use the parking. A value of `true` means a fee must be paid, a value of `false` means no fee is required. If the property is not present, then it is unknown whether a fee is required or not.
* `operator`: Who runs the parking lot.
* `maxstay`: A duration indicating the maximum time a bike is allowed to be parked.
* `surveillance`: If present, then indicates whether there is surveillance. A value of `true` means the parking is covered by surveillance, a value of `false` means it is not. If the property is not present, then it is unknown whether surveillance is in place or not.

#### POI properties (only on `kind:peak` and `kind:volcano`):

* `elevation`: Elevation of the peak or volcano in meters, where available.
* `kind_tile_rank`: A rank of each peak or volcano, with 1 being the most important. Both peaks and volcanos are scored in the same scale. When the zoom is less than 16, only five of these features are included in each tile. At zoom 16, all the features are - although it's rare to have more than 5 peaks in a zoom 16 tile.

#### POI properties (only on `charging_station`):

* `bicycle`, `scooter`, `car`, `truck`: True, false, or omitted based on if that type of vehicle can be charged, or if the information is not present

#### POI `kind` values:

* `art`
* `accountant`
* `adit`
* `administrative`
* `advertising_agency`
* `aerodrome`
* `aeroway_gate`
* `airport`
* `alcohol`
* `alpine_hut`
* `ambulatory_care`
* `amusement_ride`
* `animal`
* `aquarium`
* `archaeological_site`
* `architect`
* `artwork`
* `assisted_living`
* `association`
* `atm`
* `attraction`
* `aviary`
* `bakery`
* `bank`
* `bar`
* `battlefield`
* `bbq`
* `beach_resort`
* `beach`
* `beacon`
* `beauty`
* `bed_and_breakfast`
* `bench`
* `bicycle_parking`
* `bicycle_rental` - Bicycle rental shop.
* `bicycle_rental_station` - Bike share station offering free or low cost bicycle rentals as part of a public bike scheme.
* `bicycle_repair_station`
* `bicycle` - Bicycle sales shop, often with bike repair service.
* `bicycle_junction` - Common in Europe for signed bicycle routes with named junctions. The cycle network reference point's `ref` value is derived from one of `icn_ref`, `ncn_ref`, `rcn_ref` or `lcn_ref`, in descending order and is suitable for naming or use in a shield.
* `biergarten`
* `block`
* `boat_rental`
* `boat_storage`
* `bollard`
* `books`
* `brewery`
* `bus_station`
* `bus_stop`
* `butcher`
* `cafe` - _See planned bug fixes in [#1085](https://github.com/tilezen/vector-datasource/issues/1085)._
* `camp_site`
* `car`
* `car_repair`
* `car_sharing`
* `car_wash`
* `caravan_site`
* `care_home`
* `carousel`
* `carpenter`
* `cave_entrance`
* `cemetery`
* `chalet`
* `charging_station` - May also have `bicycle`, `scooter`, `car`, and `truck` set to true or false
* `childcare`
* `childrens_centre`
* `cinema`
* `clinic`
* `closed`. _See planned bug fix in [#1026](https://github.com/tilezen/vector-datasource/issues/1026)._
* `clothes`
* `club`
* `coffee`
* `college`
* `communications_tower`
* `community_centre`
* `company`
* `computer`
* `confectionery`
* `consulting`
* `convenience`
* `courthouse`
* `cross`
* `cycle_barrier` - Barrier for bicycles.
* `dairy_kitchen`
* `dam`
* `day_care`
* `deli`
* `dentist`
* `department_store`
* `dive_centre`
* `doctors`
* `dog_park`
* `doityourself`
* `dressmaker`
* `drinking_water`
* `dry_cleaning`
* `dune`
* `educational_institution`
* `egress`
* `electrician`
* `electronics`
* `embassy`
* `emergency_phone`
* `employment_agency`
* `enclosure` - at a zoo
* `estate_agent`
* `farm`
* `fashion`
* `fast_food`
* `ferry_terminal`
* `financial`
* `fire_station` - _See planned bug fixes in [#1085](https://github.com/tilezen/vector-datasource/issues/1085)._
* `firepit`
* `fishing`
* `fishing_area`
* `fitness_station`
* `fitness`
* `florist`
* `food_bank`
* `ford`
* `forest`
* `fort`
* `foundation`
* `fuel` - Fuel stations provide liquid gas (or diesel) for automotive use.
* `furniture`
* `gallery` - An art gallery.
* `garden` - _See planned bug fixes in [#1085](https://github.com/tilezen/vector-datasource/issues/1085)._
* `gardener`
* `gas_canister` - Shop selling bottled gas for cooking. Some offer gas canister refills.
* `gate`
* `generator`
* `geyser`
* `gift`
* `golf_course`
* `government`
* `greengrocer`
* `group_home`
* `guest_house`
* `hairdresser`
* `halt`
* `hanami`
* `handicraft`
* `hardware`
* `hazard`
* `healthcare`
* `helipad`
* `hifi`
* `historical` – _See planned bug fix in [#1026](https://github.com/tilezen/vector-datasource/issues/1026)._
* `hospital`
* `hostel`
* `hot_spring`
* `hotel`
* `hunting`
* `hunting_stand`
* `hvac`
* `ice_cream` - _See planned bug fix in [#532](https://github.com/tilezen/vector-datasource/issues/532)._
* `information`
* `insurance`
* `it`
* `jewelry`
* `kindergarten`
* `landmark`
* `laundry`
* `lawyer`
* `level_crossing`
* `library`
* `life_ring`
* `lifeguard_tower`
* `lift_gate`
* `lighthouse`
* `lock`
* `mall`
* `marina`
* `mast`
* `maze`
* `memorial`
* `marketplace`
* `metal_construction`
* `midwife`
* `military`
* `mineshaft`
* `mini_roundabout`
* `mobile_phone`
* `monument`
* `motel`
* `motorcycle`
* `motorcycle_parking`
* `motorway_junction`
* `museum`
* `music`
* `national_park`
* `nature_reserve`
* `newsagent`
* `newspaper`
* `ngo`
* `nightclub`
* `notary`
* `nursing_home` - _See planned bug fixes in [#1085](https://github.com/tilezen/vector-datasource/issues/1085)._
* `observatory`
* `offshore_platform`
* `optician`
* `outdoor`
* `outreach`
* `painter`
* `park` - _See planned bug fixes in [#1081](https://github.com/tilezen/vector-datasource/issues/1081)._
* `parking` - _See planned bug fixes in [#1085](https://github.com/tilezen/vector-datasource/issues/1085)._
* `peak` A mountain peak. See above for properties available on peaks and volcanos.
* `perfumery`
* `pet`
* `petroleum_well`
* `petting_zoo`
* `pharmacy`
* `phone`
* `photographer`
* `photographic_laboratory`
* `physician`
* `picnic_site`
* `picnic_table`
* `pitch`
* `place_of_worship` - _See planned bug fixes in [#1085](https://github.com/tilezen/vector-datasource/issues/1085)._
* `plant` - _See planned bug fixes in [#1085](https://github.com/tilezen/vector-datasource/issues/1085)._
* `playground` - _See planned bug fixes in [#1085](https://github.com/tilezen/vector-datasource/issues/1085)._
* `plumber`
* `police` - _See planned bug fixes in [#1085](https://github.com/tilezen/vector-datasource/issues/1085)._
* `political_party`
* `post_box`
* `post_office`
* `pottery`
* `power_pole`
* `power_tower`
* `power_wind`
* `prison`
* `protected_area`
* `pub`
* `put_in_egress`
* `put_in`
* `pylon`
* `quarry`
* `ranger_station`
* `rapid`
* `recreation_ground`
* `recreation_track`
* `recycling`
* `refugee_camp`
* `religion`
* `research`
* `residential_home`
* `resort`
* `rest_area`
* `restaurant` - _See planned bug fixes in [#1085](https://github.com/tilezen/vector-datasource/issues/1085)._
* `rock`
* `roller_coaster`
* `saddle`
* `sawmill`
* `school` - _See planned bug fixes in [#1085](https://github.com/tilezen/vector-datasource/issues/1085)._
* `scuba_diving`
* `service_area`
* `shelter`
* `shoemaker`
* `shoes`
* `shower`
* `sinkhole`
* `ski_rental`
* `ski_school`
* `ski`
* `slipway`
* `snow_cannon`
* `social_facility`
* `soup_kitchen`
* `sports_centre`
* `sports`
* `spring`
* `stadium`
* `station` - _See planned bug fix in [#532](https://github.com/tilezen/vector-datasource/issues/532)._
* `stationery`
* `stone`
* `stonemason`
* `substation` - _See planned bug fixes in [#1085](https://github.com/tilezen/vector-datasource/issues/1085)._
* `subway_entrance`
* `summer_camp`
* `summer_toboggan`
* `supermarket`
* `swimming_area`
* `tailor`
* `tax_advisor`
* `telecommunication`
* `telephone`
* `telescope`
* `theatre`
* `theme_park`
* `therapist`
* `tobacco`
* `toilets`
* `toll_booth`
* `townhall`
* `toys`
* `trade`
* `traffic_signals`
* `trail_riding_station`
* `trailhead`
* `tram_stop`
* `travel_agency`
* `travel_agent`
* `tree`
* `university`
* `variety_store`
* `veterinary`
* `viewpoint`
* `volcano` The peak of a volcano. See above for properties available on peaks and volcanos.
* `walking_junction` - Common in Europe for signed walking routes with named junctions. The walking network reference point's `ref` value is derived from one of `iwn_ref`, `nwn_ref`, `rwn_ref` or `lwn_ref`, in descending order and is suitable for naming or use in a shield.
* `waste_basket`
* `waste_disposal`
* `wastewater_plant` - _See planned bug fixes in [#1085](https://github.com/tilezen/vector-datasource/issues/1085)._
* `water_park`
* `water_point`
* `water_slide`
* `water_tower`
* `water_well`
* `water_works` - _See planned bug fixes in [#1085](https://github.com/tilezen/vector-datasource/issues/1085)._
* `waterfall`
* `watering_place`
* `wilderness_hut`
* `wildlife_park`
* `windmill`
* `wine`
* `winery` - _See planned bug fix in [#532](https://github.com/tilezen/vector-datasource/issues/532)._
* `winter_sports`
* `wood`
* `works`
* `workshop`
* `zoo`

## Roads (Transportation)

![image](images/mapzen-vector-tile-docs-roads.png)

* Layer name: `roads`
* Geometry types: `line`

More than just roads, this OpenStreetMap and Natural Earth based transportation layer includes highways, major roads, minor roads, paths, railways, ferries, and ski pistes matching the selection found in High Road. Sort them with `sort_rank` to correctly represent layered overpasses, bridges and tunnels. Natural Earth roads at zooms < 8 and OpenStreetMap at zooms 8+. See zoom ranges section below for more information per kind.

Road names are **abbreviated** so directionals like `North` is replaced with `N`, `Northeast` is replaced with `NE`, and common street suffixes like `Avenue` to `Ave.` and `Street` to `St.`. Full details in the [StreetNames](https://github.com/nvkelso/map-label-style-manual/blob/master/tools/street_names/StreetNames/__init__.py) library.

Mapzen calculates the `landuse_kind` value by intercutting `roads` with the `landuse` layer to determine if a road segment is over a parks, hospitals, universities or other landuse features. Use this property to modify the visual appearance of roads over these features. For instance, light grey minor roads look great in general, but aren't legible over most landuse colors unless they are darkened.

To improve performance, some road segments are merged at low and mid-zooms. To facilitate this, certain properties are dropped at those zooms. Examples include `is_bridge` and `is_tunnel`, `name`, `network`, `oneway`, and `ref`. The exact zoom varies per feature class (major roads keep this properties over a wider range, minor roads drop them starting at zoom 14). When roads are merged, the original OSM `id` values are dropped.

#### Road properties (common):

* `name`: From OpenStreetMap, but transformed to abbreviated names as detailed above.
* `id`: From OpenStreetMap or Natural Earth. Dropped at low- and mid-zooms when features are merged. _See planned bug fix [#1002](https://github.com/tilezen/vector-datasource/issues/1002)._
* `source`: `openstreetmap` or `naturalearthdata.com`
* `kind`: one of High Road's values for `highway`, `major_road`, `minor_road`, `rail`, `path`, `ferry`, `piste`, `aerialway`, `aeroway`, `racetrack`, `portage_way`.
* `kind_detail`: See kind detail list below, sourced from the OpenStreetMap values.
* `landuse_kind`: See description above, values match values in the `landuse` layer.
* `sort_rank`: a suggestion for which order to draw features. The value is an integer where smaller numbers suggest that features should be "behind" features with larger numbers. At zooms >= 15, the `sort_rank` is adjusted to realistically model bridge, tunnel, and layer ordering.
* `min_zoom`: a suggestion for which zoom to draw a feature. The value is a float.
* `ref`: Commonly-used reference for roads, for example "I 90" for Interstate 90. To use with shields, see `network` and `shield_text`. Related, see `symbol` for pistes.
* `all_networks` and `all_shield_texts`: All the networks of which this road is a part, and all of the shield texts. See `network` and `shield_text` below. **Note** that these properties will not be present on MVT format tiles, as we cannot currently encode lists as values.
* `network`: eg: `US:I` for the United States Interstate network, useful for shields and road selections. This only contains _road_ network types. Please see `bicycle_network` and `walking_network` for bicycle and walking networks, respectively. Note that networks may include "modifier" information, for example `US:I:Business` for a business route or `US:I:Truck` for a truck route. The whitelist of "modifier" values is; `Alternate`, `Business`, `Bypass`, `Connector`, `Historic`, `Scenic`, `Spur`, `Toll` and `Truck`.
* `shield_text`: Contains text to display on a shield. For example, I 90 would have a `network` of `US:I` and a `shield_text` of `90`. The `ref`, `I 90`, is less useful for shield display without further processing. For some roads, this can include non-numeric characters, for example the M1 motorway in the UK will have a `shield_text` of `M1`, rather than just `1`.

#### Road properties (common optional):

* `cycleway`: `cycleway` tag from feature. If no `cycleway` tag is present but `cycleway:both` exists, we source from that tag instead.
* `cycleway_left`: `cycleway_left` tag from feature
* `cycleway_right`: `cycleway_right` tag from feature
* `sidewalk`: `sidewalk` tag from feature. If no `sidewalk` tag is present but `sidewalk:both` exists, we source from that tag instead.
* `sidewalk_left`: `sidewalk:left` tag from feature
* `sidewalk_right`: `sidewalk:right` tag from feature
* `ferry`: See kind list below.
* `footway`: sidewalk or crossing
* `is_bicycle_related`: Present and `true` when road features is a dedicated cycleway, part of an OSM bicycle network route relation, or includes cycleway infrastructure like bike lanes, or tagged bicycle=yes or bicycle=designated for shared use.
* `is_bridge`: `true` if the road is part of a bridge. The property will not be present if the road is not part of a bridge.
* `is_bus_route`: If present and `true`, then buses or trolley-buses travel down this road. This property is determined based on whether the road is part of an OSM bus route relation, and is only present on roads at zoom 12 and higher.
* `is_link`: `true` if the road is part of a highway link or ramp. The property will not be present if the road is not part of a highway link or ramp.
* `is_tunnel`: `true` if the road is part of a tunnel. The property will not be present if the road is not part of a tunnel.
* `leisure`: See kind list below.
* `man_made`: See kind list below.
* `oneway_bicycle`: `oneway:bicycle` tag from feature. _See bug fix planned in [#1028](https://github.com/tilezen/vector-datasource/issues/1028)._
* `oneway`: `yes` or `no`. _See bug fix planned in [#1028](https://github.com/tilezen/vector-datasource/issues/1028)._
* `segregated`: Set to `true` when a path allows both pedestrian and bicycle traffic, but when pedestrian traffic is segregated from bicycle traffic.
* `service`: See value list below, provided for `railway` and `kind_detail=service` roads.
* `all_walking_networks` and `all_walking_shield_texts`: All of the walking networks of which this road is a part, and each corresponding shield text. See `walking_network` and `walking_shield_text` below. **Note** that these properties will not be present on MVT format tiles, as we cannot currently encode lists as values.
* `walking_network`: e.g: `nwn` for a "National Walking Network". Other common values include `iwn` for international, `rwn` for regional and `lwn` for local walking networks.
* `walking_shield_text`: Contains text intended to be displayed on a shield related to the walking network. This is the value from the `ref` tag and is _not_ guaranteed to be numeric, or even concise.
* `all_bicycle_networks` and `all_bicycle_shield_texts`: All of the bicycle networks of which this road is a part, and each corresponding shield text. See `bicycle_network` and `bicycle_shield_text` below. **Note** that these properties will not be present on MVT format tiles, as we cannot currently encode lists as values.
* `bicycle_network`: Present if the feature is part of a cycling network. If so, the value will be one of `icn` for International Cycling Network, `ncn` for National Cycling Network, `rcn` for Regional Cycling Network, `lcn` for Local Cycling Network.
* `bicycle_shield_text`: Contains text intended to be displayed on a shield related to the bicycle network. This is the value from the `ref` tag and is _not_ guaranteed to be numeric, or even concise.
* `all_bus_networks` and `all_bus_shield_texts`: All of the bus and trolley-bus routes of which this road is a part, and each corresponding shield text. See `bus_network` and `bus_shield_text` below. **Note** that these properties will not be present on MVT format tiles, as we cannot currently encode lists as values.
* `bus_network`: Note that this is often not present for bus routes / networks. This may be replaced with `operator` in the future, see [issue 1194](https://github.com/tilezen/vector-datasource/issues/1194).
* `bus_shield_text`: Contains text intended to be displayed on a shield related to the bus or trolley-bus network. This is the value from the `ref` tag and is _not_ guaranteed to be numeric, or even concise.
* `surface`: Common values include `asphalt`, `unpaved`, `paved`, `ground`, `gravel`, `dirt`, `concrete`, `grass`, `paving_stones`, `compacted`, `sand`, and `cobblestone`. `cobblestone:flattened`, `concrete:plates` and `concrete:lanes` values are transformed to `cobblestone_flattened`, `concrete_plates` and `concrete_lanes` respectively.

#### Road properties (optional):

* `ascent`: ski pistes from OpenStreetMap
* `access`: `private`, `yes`, `no`, `permissive`, `customers`, `destination`, and other values from OpenStreetMap
* `bicycle`: `yes`, `no`, `designated`, `dismount`, and other values from OpenStreetMap
* `colour`: ski pistes from OpenStreetMap
* `descent`: ski pistes from OpenStreetMap
* `description`: OpenStreetMap features
* `distance`: ski pistes from OpenStreetMap
* `motor_vehicle`: OpenStreetMap features
* `operator`: OpenStreetMap features
* `piste_difficulty`: ski pistes from OpenStreetMap
* `piste_grooming`: ski pistes from OpenStreetMap
* `piste_name`: ski pistes from OpenStreetMap
* `ramp`: OpenStreetMap features
* `ramp_bicycle`: OpenStreetMap features
* `roundtrip`: OpenStreetMap features
* `route_name`: OpenStreetMap features
* `ski`: ski pistes from OpenStreetMap
* `snowshoe`: ski pistes from OpenStreetMap
* `sport`: OpenStreetMap features
* `state`: OpenStreetMap features
* `symbol`: ski pistes from OpenStreetMap

#### Road transportation `kind` values (lines):

* `aerialway`
* `aeroway`
* `ferry`
* `highway`
* `major_road`
* `minor_road`
* `path`
* `piste`
* `racetrack`
* `rail`

#### Road Transportation `kind_detail` values and zoom ranges:

**Roads** from **Natural Earth**  are used at low zooms below 8. Road `kind_detail` values are limited to `motorway`, `trunk`, `primary`, `secondary`, `tertiary`.

**Roads** from **OpenStreetMap** are shown starting at zoom 8 with `motorway`, `trunk`, `primary`. `secondary` are added starting at zoom 10, with `motorway_link`, `tertiary` added at zoom 11. Zoom 12 sees addition of `trunk_link`, `residential`, `unclassified`, and `road`. Zoom 13 adds `primary_link`, `secondary_link`, `raceway`, `track`, `pedestrian`, `living_street`, `cycleway` and `bridleway`. Zoom 14 adds `tertiary_link`, all remaining `path`, `footway`, and `steps`, `corridor`, and `alley` service roads. By zoom 15 all remaining service roads are added, including `driveway`, `parking_aisle`, `drive_through`. Internationally and nationally significant paths (`path`, `footway`, `steps`) are added at zoom 9, regionally significant paths are added at zoom 11, locally significant at zoom 12, and named or designated paths at zoom 13. Internationally and nationally significant bicycle routes are added at zoom 8, regionally significant bike routes at zoom 10, and locally significant at zoom 11.

**Ferries** from both Natural Earth and OpenStreetMap are shown starting at zoom 5 with `kind` values of `ferry`.

![image](images/mapzen-vector-tile-docs-roads-railway.png)

**Rail** is added starting at zoom 11, with minor railroad `spur` added at zoom 12+ (based on "service" values), and further detail for `yard` and `crossover` and 13 and 14 respectively with all railroads shown by zoom 15. Features for rail tracks are included in this layer, whereas geometries and further information about rail lines or routes is available in the `transit` layer.

Railway `kind_detail` values in this layer include: `rail`, `tram`, `light_rail`, `narrow_gauge`, `monorail`, `subway`, and `funicular`.

Railway `service` values are:

* `spur`
* `siding`
* `yard`
* `crossover`
* `branch`
* `connector`
* `wye`
* `runaway`
* `interchange`
* `switch`
* `industrial`
* `disused`
* `driveway`
* `passing_loop`

![image](images/mapzen-vector-tile-docs-roads-airport.png)

**Airport** aeroways with `kind_detail` values of `runway` show up at zoom 9, with `taxiway` at zoom 11+.

![image](images/mapzen-vector-tile-docs-roads-aerialways.png)

**Aerialways** with `kind_detail` values of `gondola`, `cable_car` show up zoom 12+. `chair_lift` is added at zoom 13+, and by zoom 15 all are visible adding `drag_lift`, `platter`, `t_bar`, `goods`, `magic_carpet`, `rope_tow`, `zip_line`, `j_bar`, `unknown`, `mixed_lift`, and `canopy`.

**Racetrack** lines for various recreation tracks start showing up at zoom 14  with `kind_detail` values of sport_values of `athletics`, `running`, `horse_racing`, `bmx`, `disc_golf`, `cycling`, `ski_jumping`, `motor`, `karting`,`obstacle_course`, `equestrian`, `alpine_slide`, `soap_box_derby`,`mud_truck_racing`, `skiing`, `drag_racing`, `archery`.

![image](images/mapzen-vector-tile-docs-roads-pistes.png)

**Piste** type with `kind_detail` values of `nordic`, `downhill`, `sleigh`, `skitour`, `hike`, `sled`, `yes`, `snow_park`, `playground`, `ski_jump`. Abandoned pistes are not included in tiles.

![image](images/mapzen-vector-tile-docs-roads-piers.png)

**Piers** start showing up at zoom 13+ with `kind_detail` values of `pier`.

## Transit

![image](images/mapzen-vector-tile-docs-transit.png)

* Layer name: `transit`
* Geometry types: `line`, `polygon`

Transit line features from OpenStreetMap start appearing at zoom 5+ for national trains, with regional trains addded at zoom 6+. Then `subway`,`light_rail`, and `tram` are added at zoom 10+. `funicular` and `monorail` features are added at zoom 12+. Platform polygons are added zoom 14+.

_TIP: If you're looking for transit `station` and `station_entrance` features, look in the `pois` layer instead._

#### Transit properties (common):

* `name`: including localized name variants
* `id`: OpenStreetMap feature `osm_id`
* `kind`: detailed below, per geometry type
* `source`: `openstreetmap.org`
* `sort_rank`: a suggestion for which order to draw features. The value is an integer where smaller numbers suggest that features should be "behind" features with larger numbers.
* `min_zoom`: a suggestion for which zoom to draw a feature. The value is a float.

#### Transit properties (common optional):

Depending on upstream OpenStreetMap tagging, the following properties may be present:

* `ref`
* `network`
* `operator`
* `railway`
* `route`

A smaller set is also available for non-`platform` features:

* `colour`: either a `#rrggbb` hex value, or a CSS colour name (like `red`)
* `colour_name`: A colour name from a fixed palette, see description below.
* `layer`
* `state`
* `symbol`
* `type`

#### Transit properties (optional):

Depending on OpenStreetMap tagging, the following properties may be present for non-`platform` features.

* `ascent`
* `descent`
* `description`
* `distance`
* `roundtrip`

#### Transit `kind` values (line, polygon):

* `light_rail`
* `platform`
* `railway`
* `subway`
* `train`
* `tram`

#### Transit `colour_name` values:

Transit lines may have their colours mapped onto one of these CSS colours. The intention is that designers can take this limited palette set and remap them onto a set which is more appropriate and in keeping with the other colours in the design. Inspired by [py-cooperhewitt-swatchbook](https://github.com/cooperhewitt/py-cooperhewitt-swatchbook).

* aqua
* aquamarine
* black
* blue
* brown
* crimson
* darkgrey
* darkorchid
* darkred
* darkseagreen
* dodgerblue
* fuchsia
* gainsboro
* gold
* goldenrod
* green
* grey
* hotpink
* indigo
* khaki
* lightblue
* lightcoral
* lightgreen
* lightteal
* lime
* limegreen
* mediumpurple
* mediumseagreen
* mediumturquoise
* navy
* olivedrab
* orange
* orangered
* peru
* pink
* plum
* purple
* red
* royalblue
* sandybrown
* silver
* steelblue
* tan
* teal
* tomato
* violet
* white
* yellow
* yellowgreen


## Water

![image](images/mapzen-vector-tile-docs-water.png)

* Layer name: `water`
* Geometry types: `point`, `line`, and `polygon`

Water `polygons` representing oceans, riverbanks and lakes. Derived from a combination of the `waterway`, `natural`, and `landuse` OpenStreetMap tags. Includes coastline-derived water polygons from [openstreetmapdata.com](http://openstreetmapdata.com) and inland water directly from OpenStreetMap at higher zoom levels 8+, and [Natural Earth](http://naturalearthdata.com) polygons at lower zoom levels (0-7). Water polygons are progressively added based on an area filter until all water is shown at zoom 16+.

Also includes water `line` geometries for river and stream centerlines and "label_position" `points` for labeling polygons de-duplicated across tile boundaries. OpenStreetMap sourced waterway lines kinds of `river`, `canal`, and `stream` are included starting at zoom 11 and `ditch`, `drain` (zoom 16+).

Mapzen calculates the composite exterior edge for overlapping water polygons and marks the resulting line `boundary=true`. Set to `true` when present on `line` geometry, or from Natural Earth line source.

#### Water properties (common):

* `name`: including localized name variants
* `kind`: detailed below, per geometry type
* `source`: one of `naturalearthdata.com`, `openstreetmapdata.com`, `openstreetmap.org`
* `boundary`: `true`, on lines only. See description above. _See proposed bug fix in [#735](https://github.com/tilezen/vector-datasource/issues/735)._
* `sort_rank`: a suggestion for which order to draw features. The value is an integer where smaller numbers suggest that features should be "behind" features with larger numbers.
* `min_zoom`: a suggestion for which zoom to draw a feature. The value is a float.

#### Water properties (common optional):

* `area`: in square meters (spherical Mercator, no real-world), `polygon` features only
* `id`: OpenStreetMap feature `osm_id`, when sourced from `openstreetmap.org`
* `is_tunnel`: for `line` features only (`true` values only)

#### Water `kind` values:

* `basin` - polygon
* `bay` - point, intended for label placement only
* `canal` - line
* `ditch` - line
* `dock` - polygon
* `drain` - line
* `fjord` - point, intended for label placement only
* `lake` - polygon
* `ocean` - polygon, point is intended for label placement only
* `playa` - polygon
* `river` - line
* `riverbank` - polygon
* `sea` - point, intended for label placement only
* `stream` - line
* `strait` - point, intended for label placement only
* `swimming_pool` - polygon
* `water` - polygon

Additionally, a `reservoir: true` or `alkaline: true` value can be present on the appropriate `kind=lake` features. Intermittent water features that sometimes run dry or disappear seasonally are marked `intermittent: true`.

**Gotchas:**

* `lake` features with `alkaline: true` and `playa` features are sourced solely from Natural Earth. Zooming in, your feature may disappear (there is no equivalent in OpenStreetMap). Beware the desert around Great Salt Lake in Utah!
* `lake` features from Natural Earth sometimes change to `water` features on zoom into OpenStreetMap data. _See planned bug fix in [#984](https://github.com/tilezen/vector-datasource/issues/984)._
* Some of the minor kinds (like `bay`, `strait`, and `fjord`) are used for label_placement points only, as their area would duplicate water polygons already present from openstreetmapdata.com.
