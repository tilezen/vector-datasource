# Layers in Mapzen's vector tiles

![image](images/mapzen-vector-tile-docs-all-layers.png)

The [Mapzen vector tile service](https://mapzen.com/projects/vector-tiles) provides worldwide basemap coverage sourced from [OpenStreetMap](www.openstreetmap.org) and other open data projects, updated daily as a free & shared service.

Data is organized into several thematic layers, each of which is named, for example; `buildings`, `pois`, and `water`. A selection of these layers are typically used for base map rendering, and are provided under the short-hand name `all`. Each layer includes a simplified view of OpenStreetMap data for easier consumption, with common tags often condensed into a single `kind` field as noted below.

Need help displaying vector tiles in a map? We have several [examples](display-tiles.md) using Mapzen vector tiles to style in your favorite graphics library including Tangram, Mapbox GL, D3, and Hoverboard.

### Overview

#### Data sources and attribution

Mapzen primarily sources from OpenStreetMap, but includes a variety of other open data. For a full listing, view the [data sources](data-sources.md). Each source may require [attribution](attribution.md) in your project.

#### Name localization

Mapzen vector tile features include the default `name` property. We include all language variants of the `name:*`, `alt_name:*`, `alt_name_`, `old_name:*` values to enable full internationalization (when different than `name`). Tangram supports all language scripts. Language variants are identified by an ISO 639-1 two-letter language code and optional country, for example `en_GB` for British English.

For features in the `boundaries` layer, we support two additional variants `left:name:*` and `right:name:*` to support oriented labeling on the appropriate side of the boundary line (so the labeled polygon's text can appear inside that polygon consistently).

#### Geometry types

Individual Mapzen vector tile layers can include mixed geometry types. This is common in the `landuse`, `water`, and `buildings` layers.

A tile geometry can be one of 3 types:

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

The current version of Mapzen vector tiles is **v0.10.0**. Our tiles are still in active development, but we try to minimize backwards incompatable breaking changes. We're also interested in your feedback at hello@mapzen.com!

If you're signed up for a [Mapzen Vector Tiles API key](https://mapzen.com/developers) you should receive an email notifying you of upcoming changes before they are rolled out to production.

Read the full details in the project [CHANGELOG](https://github.com/mapzen/vector-datasource/tree/v0.10.0/CHANGELOG.md).

#### Feature ordering

Ordering of features - which ones draw "on top of" other features - can be an important feature of display maps. To help out with this, we export a `sort_key` property on some features which suggests in what order the features should appear. Lower numbers mean that features should appear "towards the back" and higher numbers mean "towards the front". These numbers are consistent across layers. The layers which include `sort_key` on their features are: `boundaries`, `buildings`, `earth`, `landuse`, `roads`, `transit` and `water`.

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

These individual layers are grouped into an `all` layer – use this special layer for all your general purpose mapping needs.

We include one deprecated layer, `landuse-labels`, for backwards compatibility. Please don't build new maps against this layer, it will be removed in the v1.0 version of tiles.

## Boundaries

![image](images/mapzen-vector-tile-docs-boundaries.png)

* Layer name: `boundaries`
* Geometry types: `line`

Combination of OpenStreetMap administrative boundaries (zoom >= 8) and Natural Earth boundaries (zoom < 8).


#### Boundary properties (common):

* `name`
* `id`
* `kind`: mapping of OpenStreetMap's `admin_level` int values to strings like `country` and `state`, plus `aboriginal_lands` boundary type, and also includes raw Natural Earth values.
* `sort_key`: a suggestion for which order to draw features. The value is an integer where smaller numbers suggest that features should be "behind" features with larger numbers.

#### Boundary properties (common optional):

* `admin_level`: values of `2` for countries, `4` for states (zoom 8+), and `6`, `8` (zoom 10+)
* `id:left`: For the relation on the left side of the boundary line.
* `id:right`: For the relation on the right side of the boundary line.
* `name:left`: See name section above, other variants like `old_name` also supported.
* `name:right`: See name section above, other variants like `old_name` also supported.
* `maritime_boundary`: a special Mapzen calculated value loosely coupled with OpenStreetMap's maritime tag, but with spatial buffer processing for lines falling in the ocean.

#### Boundary properties (optional):

* `labelrank`: from Natural Earth
* `scalerank`: from Natural Earth
* `osm_relation`: `true`, which can also be deduced from negative `id` values.

#### Boundary kind values:

* `aboriginal lands`
* `country`
* `county`
* `disputed`
* `indefinite`
* `indeterminate`
* `lease_limit`
* `line_of_control`
* `macroregion`
* `municipality`
* `overlay_limit`
* `state`

## Buildings and Addresses

![image](images/mapzen-vector-tile-docs-buildings.png)

* Layer name: `buildings`
* Geometry types: `point` and `polygon`

Polygons from OpenStreetMap representing building footprint, building label_placement points, building_part features, and address points. Starts at zoom 13 by including huge buildings, progressively adding all buildings at zoom 16+. Address points are available at zoom 16+, but marked with `min_zoom: 17` to suggest that they are suitable for display at zoom level 17 and higher.

Individual `building:part` geometries from OSM following the [Simple 3D Buildings](http://wiki.openstreetmap.org/wiki/Simple_3D_Buildings) tags at higher zoom levels are now exported as `building_part` features with specified `kind_detail`. Building parts may receive a `root_id` corresponding to the building feature, if any, with which they intersect.

Mapzen calculates the `landuse_kind` value by intercutting `buildings` with the `landuse` layer to determine if a building is over a parks, hospitals, universities or other landuse features. Use this property to modify the visual appearance of buildings over these features. For instance, light grey buildings look great in general, but aren't legible over most landuse colors unless they are darkened (or colorized to match landuse styling).

#### Building properties (common):

* `name`
* `id`: from OpenStreetMap
* `kind`: see below
* `source`: `openstreetmap.org`
* `landuse_kind`: See description above, values match values in the `landuse` layer.
* `sort_key`: a suggestion for which order to draw features. The value is an integer where smaller numbers suggest that features should be "behind" features with larger numbers.

#### Building properties (common optional):

* `addr_housenumber`: value from OpenStreetMap's `addr:housenumber` tag
* `addr_street`: value from OpenStreetMap's `addr:street` tag
* `area`: in square meters (spherical Mercator, no real-world), `polygon` features only
* `height`: in meters, where available
* `layer`
* `location`: from OpenStreetMap to indicate if building is underground, similar to `layer`.
* `min_height`: value from `min_height` in meters, where available, otherwise estimated from `building:min_levels` if present
* `min_zoom`: a suggested minimum zoom at which the building should become visible based on area and volume limits. This is only present on buildings in tiles at zoom 16 and below.
* `roof_color`: from `roof:color` tag
* `roof_height`: from `roof:height` tag
* `roof_material`: from `roof:material` tag
* `roof_orientation`: from `roof:orientation` tag
* `roof_shape`: from `roof:shape` tag
* `volume`: calculated on feature's `area` and `height`, when `height` or `min_height` is available
* `kind_detail`: value from OpenStreetMap's `building:part` tag.

#### Building kind values:

* Buildings polygons and label_position points, have `kind` values that are either `building` or `building_part`, if `building=*` or `building:part` is `yes` respectively. Label position points may also be one of `closed` or `historical` if the original building name ended in "(closed)" or "(historical)", respectively. These points will have a `min_zoom` of 17, suggesting that they are suitable for display only at high zooms.
* If the raw OpenStreetMap `building:part` tag exists with a value, a `kind_detail` tag is added to describe the `building:part` value.
* Address points are `kind` of value `address`.

#### Address properties and kind value:

* `name`
* `id`: osm_id
* `source`: `openstreetmap.org`
* `kind`: `address`
* `addr_housenumber`: value from OpenStreetMap's `addr:housenumber` tag
* `addr_street`: value from OpenStreetMap's `addr:street` tag

## Earth

![image](images/mapzen-vector-tile-docs-earth.png)

* Layer name: `earth`
* Geometry types: `polygon`, `line`, `point`.

Polygons representing earth landmass and natural feature lines. Uses coastline-derived land polygons from [openstreetmapdata.com](http://openstreetmapdata.com). Natural lines from OpenStreetMap representing cliffs, aretes. This layer also includes earth `label_placement` lines for ridges and valleys (which should not otherwise be symbolized).

_Uses Natural Earth until zoom 8, then switches to OSM land at zoom 9+._

**Earth properties:**

* `id`: osm_id **or** funky value when from Natural Earth or OpenStreetMapData.com
* `kind`: either `earth` or "natural" value from OSM tag.
* `sort_key`: a suggestion for which order to draw features. The value is an integer where smaller numbers suggest that features should be "behind" features with larger numbers.

#### Earth kind values:

* `arete`
* `cliff`
* `earth`
* `ridge`
* `valley`

#### Earth kind values (point only):

These are intended for label placement, and are included as points only.

* `archipelago`
* `island`
* `islet`


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
* `id`: osm_id
* `kind`: combination of the `landuse`, `leisure`, `natural`, `highway`, `aeroway`, `amenity`, `tourism`, `zoo`, `attraction`, `man_made`, `power`, and `boundary` OSM tags, or `urban_area` for Natural Earth features. Also includes of some `barrier` and `waterway` tags: `city_wall` (zoom 12+), `dam` (zoom 12+), `retaining_wall` (zoom 15+), `snow_fence` (zoom 15+), `fence` (zoom 16+ only) and `gate` (zoom 16+ only).
* `sort_key`: a suggestion for which order to draw features. The value is an integer where smaller numbers suggest that features should be "behind" features with larger numbers.
* `area`: in square meters (spherical Mercator, no real-world), `polygon` features only

#### Landuse properties (common optional):

* `protect_class`: Common values include `1`, `2`, `3`, `4`, `5`, `6`. See [OSM wiki](https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dprotected_area#Protect_classes_for_various_countries) for more information.
* `operator`: e.g. `United States National Park Service`, `United States Forest Service`, `National Parks & Wildlife Service NSW`.

#### Landuse kind values:

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
* `dam`
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


## Places

![image](images/mapzen-vector-tile-docs-places.png)

* Layer name: `places`
* Geometry types: `point`

Combination of OpenStreetMap `place` points, Natural Earth populated places, and Who's On First neighbourhoods.

Places with `kind` values of `continent`, `country`, with others added starting at zoom 4 for `region` and starting at zoom 8 for `locality`. Specific `locality` types are added to the `kind_detail` tag.

![image](images/mapzen-vector-tile-docs-places-neighbourhoods.png)

**Neighbourhoods:** [Who's On First](http://whosonfirst.mapzen.com) `neighbourhood` and `macrohood` features are added starting at zoom 12. Neighbourhoods are included one zoom earlier than their `min_zoom`, and stay included 1 zoom past their `max_zoom`.


#### Place properties (common):

* `name`
* `id`: osm_id from OpenStreetMap or Natural Earth id
* `kind`: normalized values between OpenStreetMap and Natural Earth
* `population`: population integer values from OpenStreetMap or Natural Earth (`pop_max`)
* `scalerank`: scalerank value from Natural Earth, and invented for OpenStreetMap
* `source`: `openstreetmap` or `naturalearthdata.com`

#### Place properties (common optional):

* `capital`: a `true` value normalizes values between OpenStreetMap and Natural Earth for kinds of `Admin-0 capital`, `Admin-0 capital alt`, and `Admin-0 region capital`.
* `region_capital`: a `true` value normalizes values between OpenStreetMap and Natural Earth for kinds of `Admin-1 capital` and `Admin-1 region capital`.
* `labelrank`: labelrank value from Natural Earth
* `min_zoom`: Currently neighbourhoods only, from Who's On First
* `max_zoom`: Currently neighbourhoods only, from Who's On First
* `is_landuse_aoi`: Currently neighbourhoods only, from Who's On First
* `kind_detail`: the original value of the OSM `place` tag and Natural Earth `featurecla`, see below.

#### Place kind values:

* `borough`
* `continent`
* `country`
* `locality`
* `macrohood`
* `microhood`
* `neighbourhood`
* `region`

#### Place kind_detail values:

* `city`
* `farm`
* `hamlet`
* `isolated_dwelling`
* `locality`
* `neighbourhood`
* `province`
* `scientific_station`
* `state`
* `town`
* `village`

## Points of Interest

![image](images/mapzen-vector-tile-docs-pois.png)

* Layer name: `pois`
* Geometry types: `point`

Over 200 points of interest (POI) kinds are supported. POIs are included starting at zoom 12 for major features like `airport`, `hospital`, `zoo`, and `motorway_junction`. Then progressively more features added at each additional zoom based on a combination of feature area (if available) and `kind` value. For instance, by zoom 15 most `police`, `library`, `university`, and `beach` features should be included, and by zoom 16 things like `car_sharing`, `picnic_site`, and `tree` are added. By zoom 16 all local features are added, like `amusement_ride`, `atm`, and `bus_stop`, but may be marked with a `min_zoom` property to suggest at which zoom levels they are suitable for display. For example, `bench` and `waste_basket` features may be marked `min_zoom: 18` to suggest that they are displayed at zoom 18 and higher.

The `pois` layer should be used in conjuction with `landuse` (parks, etc) label_position features and `buildings` label_position features, throttled by area.

Points of interest from OpenStreetMap, with per-zoom selections similar to the primary [OSM.org Mapnik stylesheet](https://trac.openstreetmap.org/browser/subversion/applications/rendering/mapnik).

Features from OpenStreetMap which are tagged `disused=*` for any other value than `disused=no` are not included in the data. Features which have certain parenthetical comments after their name are suppressed until zoom 17 and have their `kind` property set to that comment. Currently anything with a name ending in '(closed)' or '(historical)' will be suppressed in this manner. Railway stops, halts, stations and tram stops from OpenStreetMap tagged with a `historic` tag are also not included in the data.

To resolve inconsistency in data tagging in OpenStreetMap we normalize several operator values for United States National Parks as `United States National Park Service`, several United States Forest Service values as `United States Forest Service`, and several values for New South Wales National Parks in Australia as `National Parks & Wildlife Service NSW`.

#### POI properties (common):

* `name`
* `id`: osm_id
* `source`: `openstreetmap.org`
* `kind`: combination of the `aerialway`, `aeroway`, `amenity`, `attraction`, `barrier`, `craft`, `highway`, `historic`, `leisure`, `lock`, `man_made`, `natural`, `office`, `power`, `railway`, `rental`, `shop`, `tourism`, `waterway`, and `zoo` tags. Can also be one of `closed` or `historical` if the original feature was parenthetically commented as closed or historical.

#### POI properties (common optional):

* `aeroway`:
* `attraction`:
* `cuisine`:
* `exit_to`: only for highway exits
* `ref`: generally only for `gate` and `station_entrance` features
* `religion`:
* `sport`:
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

#### POI properties (only on `kind:bicycle_parking`):

* `access`: Whether the bicyle parking is for general public use (`yes`, `permissive`, `public`) or for customers only (`customers`) or private use only (`private`, `no`).
* `capacity`: Approximate number of total bicycle parking spots.
* `covered`: Is the parking area covered.
* `fee`: If present, indicates whether a fee must be paid to use the bicycle parking. A value of `true` means a fee must be paid, a value of `false` means no fee is required. If the property is not present, then it is unknown whether a fee is required or not.
* `operator`: Who runs the bike parking lot.
* `maxstay`: A duration indicating the maximum time a bike is allowed to be parked.
* `surveillance`: If present, then indicates whether there is surveillance. A value of `true` means the parking is covered by surveillance, a value of `false` means it is not. If the property is not present, then it is unknown whether surveillance is in place or not.

#### POI properties (only on `kind:peak` and `kind:volcano`):

* `elevation`: Elevation of the peak or volcano in meters, where available.
* `kind_tile_rank`: A rank of each peak or volcano, with 1 being the most important. Both peaks and volcanos are scored in the same scale. When the zoom is less than 16, only five of these features are included in each tile. At zoom 16, all the features are - although it's rare to have more than 5 peaks in a zoom 16 tile.

#### POI kind values:

* `accountant`
* `adit`
* `administrative`
* `advertising_agency`
* `aerodrome`
* `airport`
* `alcohol`
* `alpine_hut`
* `ambulatory_care`
* `amusement_ride`
* `animal`
* `aquarium`
* `archaeological_site`
* `architect`
* `are_home`
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
* `cafe`
* `camp_site`
* `car_repair`
* `car_sharing`
* `car`
* `caravan_site`
* `carousel`
* `carpenter`
* `cave_entrance`
* `cemetery`
* `chalet`
* `childcare`
* `childrens_centre`
* `cinema`
* `clinic`
* `closed`
* `clothes`
* `club`
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
* `enclosure`
* `estate_agent`
* `fashion`
* `fast_food`
* `farm`
* `ferry_terminal`
* `financial`
* `fire_station`
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
* `garden`
* `gardener`
* `gas` - Shop selling bottled gas for cooking. Some offer gas canister refills.
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
* `historical`
* `hospital`
* `hostel`
* `hot_spring`
* `hotel`
* `hunting`
* `hvac`
* `ice_cream`
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
* `metal_construction`
* `midwife`
* `military`
* `mineshaft`
* `mini_roundabout`
* `mobile_phone`
* `monument`
* `motel`
* `motorcycle`
* `motorway_junction`
* `museum`
* `music`
* `national_park`
* `nature_reserve`
* `newspaper`
* `ngo`
* `notary`
* `nursing_home`
* `observatory`
* `offshore_platform`
* `optician`
* `outdoor`
* `outreach`
* `painter`
* `park`
* `parking`
* `peak` A mountain peak. See above for properties available on peaks and volcanos.
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
* `place_of_worship`
* `plant`
* `playground`
* `plumber`
* `police`
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
* `restaurant`
* `rock`
* `roller_coaster`
* `saddle`
* `sawmill`
* `school`
* `scuba_diving`
* `service_area`
* `shelter`
* `shoemaker`
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
* `station`
* `stone`
* `stonemason`
* `substation`
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
* `toilets`
* `toll_booth`
* `townhall`
* `toys`
* `trade`
* `traffic_signals`
* `trail_riding_station`
* `trailhead`
* `tram_stop`
* `travel_agent`
* `tree`
* `university`
* `veterinary`
* `viewpoint`
* `village_green`
* `volcano` The peak of a volcano. See above for properties available on peaks and volcanos.
* `walking_junction` - Common in Europe for signed walking routes with named junctions. The walking network reference point's `ref` value is derived from one of `iwn_ref`, `nwn_ref`, `rwn_ref` or `lwn_ref`, in descending order and is suitable for naming or use in a shield.
* `waste_basket`
* `waste_disposal`
* `wastewater_plant`
* `water_park`
* `water_point`
* `water_slide`
* `water_tower`
* `water_well`
* `water_works`
* `waterfall`
* `watering_place`
* `wilderness_hut`
* `wildlife_park`
* `windmill`
* `wine`
* `winery`
* `winter_sports`
* `wood`
* `works`
* `workshop`
* `zoo`

## Roads (Transportation)

![image](images/mapzen-vector-tile-docs-roads.png)

* Layer name: `roads`
* Geometry types: `line`

More than just roads, this OpenStreetMap and Natural Earth based transportation layer includes highways, major roads, minor roads, paths, railways, ferries, and ski pistes matching the selection found in High Road. Sort them with `sort_key` to correctly represent layered overpasses, bridges and tunnels. Natural Earth roads at zooms < 8 and OpenStreetMap at zooms 8+. See zoom ranges section below for more information per kind.

Road names are **abbreviated** so directionals like `North` is replaced with `N`, `Northeast` is replaced with `NE`, and common street suffixes like `Avenue` to `Ave.` and `Street` to `St.`. Full details in the [StreetNames](https://github.com/nvkelso/map-label-style-manual/blob/master/tools/street_names/StreetNames/__init__.py) library.

Mapzen calculates the `landuse_kind` value by intercutting `roads` with the `landuse` layer to determine if a road segment is over a parks, hospitals, universities or other landuse features. Use this property to modify the visual appearance of roads over these features. For instance, light grey minor roads look great in general, but aren't legible over most landuse colors unless they are darkened. 

To improve performance, some road segments are merged at low and mid-zooms. To facilitate this, certain properties are dropped at those zooms. Examples include `is_bridge` and `is_tunnel`, `name`, `network`, and `ref`. The exact zoom varies per feature class (major roads keep this properties over a wider range, minor roads drop them starting at zoom 14). When roads are merged, the original OSM `id` values are dropped.

#### Road properties (common):

* `name`: From OpenStreetMap, but transformed to abbreviated names as detailed above.
* `id`: From OpenStreetMap or Natural Earth
* `source`: `openstreetmap` or `naturalearthdata.com`
* `kind`: one of High Road's values for `highway`, `major_road`, `minor_road`, `rail`, `path`, `ferry`, `piste`, `aerialway`, `aeroway`, `racetrack`, `portage_way` if `whitewater=portage_way`; or Natural Earth's `featurecla` value. You'll want to look at other tags like `highway` and `railway` for raw OpenStreetMap values.
* `kind_detail`: See kind detail list below.
* `landuse_kind`: See description above, values match values in the `landuse` layer.
* `ref`: Commonly-used reference for roads, for example "I 90" for Interstate 90. To use with shields, see the common optional properties `network` and `shield_text`. Related, see `symbol` for pistes.
* `sort_key`: a suggestion for which order to draw features. The value is an integer where smaller numbers suggest that features should be "behind" features with larger numbers. At zooms >= 15, the `sort_key` is adjusted to realistically model bridge, tunnel, and layer ordering.

#### Road properties (common optional):

* `aeroway`: See kind list below.
* `all_networks` and `all_shield_texts`: All the networks of which this road is a part, and all of the shield texts. See `network` and `shield_text` below. **Note** that these properties will not be present on MVT format tiles, as we cannot currently encode lists as values.
* `bicycle_network`: Present if the feature is part of a cycling network. If so, the value will be one of `icn` for International Cycling Network, `ncn` for National Cycling Network, `rcn` for Regional Cycling Network, `lcn` for Local Cycling Network.
* `cycleway`: `cycleway` tag from feature. If no `cycleway` tag is present but `cycleway:both` exists, we source from that tag instead.
* `cycleway_left`: `cycleway_left` tag from feature
* `cycleway_right`: `cycleway_right` tag from feature
* `ferry`: See kind list below.
* `is_bicycle_related`: Present and `true` when road features is a dedicated cycleway, part of an OSM bicycle network route relation, or includes cycleway infrastructure like bike lanes or designed for shared use.
* `is_bridge`: `true` if the road is part of a bridge. The property will not be present if the road is not part of a bridge.
* `is_bus_route`: If present and `true`, then buses or trolley-buses travel down this road. This property is determined based on whether the road is part of an OSM bus route relation, and is only present on roads at zoom 12 and higher.
* `is_link`: `true` if the road is part of a highway link or ramp. The property will not be present if the road is not part of a highway link or ramp.
* `is_tunnel`: `true` if the road is part of a tunnel. The property will not be present if the road is not part of a tunnel.
* `leisure`: See kind list below.
* `man_made`: See kind list below.
* `network`: eg: `US:I` for the United States Interstate network, useful for shields and road selections. This only contains _road_ network types. Please see `bicycle_network` and `walking_network` for bicycle and walking networks, respectively.
* `oneway_bicycle`: `oneway:bicycle` tag from feature
* `oneway`: `yes` or `no`
* `segregated`: Set to `true` when a path allows both pedestrian and bicycle traffic, but when pedestrian traffic is segregated from bicycle traffic.
* `service`: See value list below, provided for `railway` and `kind_detail=service` roads.
* `shield_text`: Contains text to display on a shield. For example, I 90 would have a `network` of `US:I` and a `shield_text` of `90`. The `ref`, `I 90`, is less useful for shield display without further processing.
* `walking_network`: Present if the feature is part of a hiking network. If so, the value will be one of `iwn` for International Walking Network, `nwn` for National Walking Network, `rwn` for Regional Walking Network, `lwn` for Local Walking Network.
* `kind_detail`: normalized values describing the kind value, see below.

#### Road properties (optional):

* `ascent`: ski pistes from OpenStreetMap
* `colour`: ski pistes from OpenStreetMap
* `descent`: ski pistes from OpenStreetMap
* `description`: OpenStreetMap features
* `distance`: ski pistes from OpenStreetMap
* `labelrank`: Natural Earth features
* `level`: Natural Earth features
* `motor_vehicle`: OpenStreetMap features
* `namealt`: Natural Earth features
* `namealtt`: Natural Earth features
* `operator`: OpenStreetMap features
* `piste_difficulty`: ski pistes from OpenStreetMap
* `piste_grooming`: ski pistes from OpenStreetMap
* `piste_name`: ski pistes from OpenStreetMap
* `roundtrip`: OpenStreetMap features 
* `route_name`: OpenStreetMap features
* `scalerank`: Natural Earth features
* `ski`: ski pistes from OpenStreetMap
* `snowshoe`: ski pistes from OpenStreetMap
* `sport`: OpenStreetMap features
* `state`: OpenStreetMap features
* `symbol`: ski pistes from OpenStreetMap

#### Road transportation kind values (lines):

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

**Roads** from **OpenStreetMap** are shown starting at zoom 8 with `motorway`, `trunk`, `primary`. `secondary` are added starting at zoom 10, with `motorway_link`, `tertiary` added at zoom 11. Zoom 12 sees addition of `trunk_link`, `residential`, `unclassified`, and `road`, and internationally and nationally significant paths (`path`, `footway`, `steps`). Zoom 13 adds `primary_link`, `secondary_link`, `track`, `pedestrian`, `living_street`, `cycleway` and `bridleway` and regionally significant and/or named or designated paths. Zoom 14 adds `tertiary_link`, all remaining `path`, `footway`, and `steps`, and `alley` service roads. By zoom 15 all remaining service roads are added, including `driveway`, `parking_aisle`, `drive_through`.

**Roads** from **Natural Earth**  are used at low zooms below 8. Road `kind_detail` values are limited to `motorway`, `trunk`, `primary`, `secondary`, `tertiary`.

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
* `sort_key`: a suggestion for which order to draw features. The value is an integer where smaller numbers suggest that features should be "behind" features with larger numbers.

#### Transit properties (common optional):

Depending on upstream OpenStreetMap tagging, the following properties may be present:

* `ref`
* `network`
* `operator`
* `railway`
* `route`

A smaller set is also available for non-`platform` features:

* `colour`: either a `#rrggbb` hex value, or a CSS colour name (like `red`)
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
* `route_name`

#### Transit kind values (line, polygon):

* `light_rail`
* `platform`
* `railway`
* `subway`
* `train`
* `tram`

## Water

![image](images/mapzen-vector-tile-docs-water.png)

* Layer name: `water`
* Geometry types: `point`, `line`, and `polygon`

Water `polygons` representing oceans, riverbanks and lakes. Derived from a combination of the `waterway`, `natural`, and `landuse` OpenStreetMap tags. Includes coastline-derived water polygons from [openstreetmapdata.com](http://openstreetmapdata.com) and inland water directly from OpenStreetMap at higher zoom levels 9+, and [Natural Earth](http://naturalearthdata.com) polygons at lower zoom levels (0-8). Water polygons are progressively added based on an area filter until all water is shown at zoom 16+.

Also includes water `line` geometries for river and stream centerlines and "label_position" `points` for labeling polygons de-duplicated across tile boundaries. OpenStreetMap sourced waterway lines kinds of `river`, `canal`, and `stream` are included starting at zoom 11 and `ditch`, `drain` (zoom 16+).

Mapzen calculates the composite exterior edge for overlapping water polygons and marks the resulting line `boundary=true`. Set to `true` when present on `line` geometry, or from Natural Earth line source.

#### Water properties (common):

* `name`: including localized name variants
* `kind`: detailed below, per geometry type
* `source`: one of `naturalearthdata.com`, `openstreetmapdata.com`, `openstreetmap.org`
* `boundary`: `true`, on lines only. See description above.
* `sort_key`: a suggestion for which order to draw features. The value is an integer where smaller numbers suggest that features should be "behind" features with larger numbers.

#### Water properties (common optional):

* `area`: in square meters (spherical Mercator, no real-world), `polygon` features only
* `id`: OpenStreetMap feature `osm_id`, when sourced from `openstreetmap.org`
* `is_tunnel`: for `line` features only (`true` values only)

#### Water kind values (point, polygon):

* `basin`
* `dock`
* `lake`
* `ocean`
* `playa`
* `riverbank`
* `swimming_pool`
* `water`

Additionally, a `reservoir: true` or `alkaline: true` value can be present on the appropriate `kind=lake` features. Intermittent water features that sometimes run dry or disappear seasonally are marked `intermittent: true`.

#### Water kind values (point only):

These are intended for label placement, and are included as points only.

* `bay`
* `fjord`
* `strait`
* `sea`

**Gotchas:**

* `lake` features with `alkaline: true` and `playa` features are sourced solely from Natural Earth. Zooming in, your feature may disappear (there is no equivalent in OpenStreetMap). Beware the desert around Great Salt Lake in Utah!
* Some of the minor kinds (like `bay`, `strait`, and `fjord`) are used for label_placement points only, as their area would duplicate water polygons already present from openstreetmapdata.com.

#### Water kind values (lines):

* `canal`
* `dam`
* `ditch`
* `drain`
* `river`
* `stream`
