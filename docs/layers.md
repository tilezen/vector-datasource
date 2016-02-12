# Layers in the vector tile service

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


## Points of interest
Points of interest from OpenStreetMap, with per-zoom selections similar to the primary [OSM.org Mapnik stylesheet](https://trac.openstreetmap.org/browser/subversion/applications/rendering/mapnik).

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
