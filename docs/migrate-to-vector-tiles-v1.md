# Migrate to vector tiles 1.0 from earlier releases

If you are connecting to the Mapzen vector tile service using a URL that starts with `https://vector.mapzen.com`, you need to consider your migration path for Mapzen vector tiles 1.0 and take action.

The 1.0 release of the Mapzen vector tiles service has some [major changes and enhancements](https://mapzen.com/blog/v1-vector-tile-service/), and Mapzen recommends all existing users of the service migrate to it. This process is not automatic, and does require you to modify your project.

At a minimum, you need to update your code or stylesheets, such as [Tangram YAML files](https://mapzen.com/documentation/tangram/sources/), to point to the service's new URL. Any additional work to use the 1.0 release depends on how much customization and styling you are using.

## Update the service URL

You can determine which release of the service you are using by looking at the URL in your code. If you see `vector.mapzen.com`, you are using the deprecated tile service.

To use vector tiles 1.0, replace your URL with the following scheme, depending on which tile format you want:

- GeoJSON: `http://tile.mapzen.com/mapzen/vector/v1/all/{z}/{x}/{y}.json`
- TopoJSON: `http://tile.mapzen.com/mapzen/vector/v1/all/{z}/{x}/{y}.topojson`
- Mapbox Vector Tile: `http://tile.mapzen.com/mapzen/vector/v1/all/{z}/{x}/{y}.mvt`

You need to append your own [API key](https://mapzen.com/documentation/overview/).

Mapzen offers several different types of tiles in vector and raster formats and the service combines data from multiple sources. Because of data model changes in 1.0, it was not possible to redirect existing queries automatically to use the 1.0 URL.

## Choose whether to use some or all layers

A vector tiles request can be for one or more individual layers, such as `roads` or `landuse`, or for `all` layers in the service.

With the 1.0 release, you may find benefits to requesting `all` layers instead of custom ones. Specifically, the `all` layers option generally loads faster because these tiles are often served directly from Mapzen's global tile cache. Custom layers experience a small lag because they are extracted, on demand, from `all` tiles. However, custom layer tiles generally have a smaller file size than `all` layers.

You should run benchmark tests for both custom and `all` layers on your target devices and network connections. If you find that one method is clearly faster than the other or better suited to your bandwidth requirements, then choose it. If the results are about the same, then use `all` because it has a simpler service architecture.

If you choose `all`, you can use client-side cartography to limit the display of the layers. For example, if you are using Tangram to draw your map, you can use data [filters](https://mapzen.com/documentation/tangram/Filters-Overview/).

## If you continue using vector.mapzen.com

Although Mapzen announced that the deprecated service will be maintained until October 31, 2017, you should update sooner for the best experience.

During this transition period, only tiles that were previously archived on Mapzen's servers will be available. This means that you may encounter locations, such as rural areas or certain zoom levels, where no data is returned. This can result in a 404 HTTP status error code.

At the time of the 1.0 release, only the `all` and `buildings` layers were archived and cached from the deprecated service. If you attempted to query for other layers, you may have been unable to access them and received an error. This was happening because tiles for custom layers were generated only on demand, and no fresh tiles were being served from the previous URLs. However, shortly after the 1.0 release, Mapzen added special handing for custom layers served from the archive, which restores the ability to query for any layer on the previous URLs.

Even if tiles are loading and your `vector.mapzen.com` map appears to be working in your area of interest, keep in mind that the content of the tiles reflect the state of OpenStreetMap as of early October 2016. No further changes from OpenStreetMap will be imported into the archived tiles. For example, if you modify a building in OpenStreetMap, you will not see that change in the deprecated service.

If you update to 1.0, all these functions to work properly; tiles in previously uncached areas are generated on demand and the data is fresh. OpenStreetMap data in the 1.0 tiles are updated frequently, often within hours or a day of the edits being made in OpenStreetMap.

## Detailed migration reference

Below is a summary of the major, breaking changes listed for the vector tiles 1.0 release, and you can use it as you prepare your cartographic updates. You can see more in the [CHANGLELOG](https://github.com/tilezen/vector-datasource/blob/master/CHANGELOG.md).

* **Topic**:
    * **example** `pre-1.0` > `value at 1.0`


* new tile URL sources:
    * `https://vector.mapzen.com/osm/all/{z}/{x}/{y}.mvt` > `https://tile.mapzen.com/mapzen/vector/v1/all/{z}/{x}/{y}.mvt`


* every layer: `sort_key` property renamed to `sort_rank`
    * `feature.sort_key` > `feature.sort_rank`

* every layer: boolean values `yes` > `true` (for everything except `oneway`)
    * **water** layer:
        * `boundary: yes` > `boundary: true`
    * **roads** layer:
        * `is_tunnel: yes` > `is_tunnel: true`
    * **roads** layer:
        * `is_bridge: yes` > `is_bridge: true`
    * **roads** layer:
        * `is_link: yes` > `is_link: true`
    * **boundaries** layer:
        * `maritime_boundary: yes` > `maritime_boundary: true`
    * **building**, **earth**, **landuse**, and **water** layers:
        * `label_position: yes` > `label_position: true`

* **roads** layer: `highway` property renamed to `kind_detail`

      * `highway: [trunk, primary]` >  `kind_detail: [trunk, primary]`
      * `highway: secondary` > `kind_detail: secondary`
      * `highway: [tertiary, tertiary_link]` > `kind_detail: [tertiary, tertiary_link]`
      * `highway: service` > `kind_detail: service`
      * `highway: [steps, track]` > `kind_detail: [steps, track]`
      * `highway: pedestrian` > `kind_detail: pedestrian`
      * `highway: track` > `kind_detail: track`
      * `highway: steps` > `kind_detail: steps`

* **roads** layer

    * Natural Earth

  	  ```
  	  natural_earth_roads:
  		  * filter:
  		  *   * - $zoom: { min: 5, max: 8 }
  		  * major_road:
  		  *   * filter: { kind: major_road }
  		  * minor_road:
  		  *   * filter: { kind: minor_road }
  	  ```

    * for OSM roads in mid- and high zooms, optionally:

        ```
        osm_roads:
           filter:
               - $zoom: { min: 8 }
        ```

* **roads** layer: `man_made` > `kind_detail`
    * `man_made: [pier]` > `kind_detail: [pier]`

* **roads** layer: `aeroway` > `kind_detail`
    * `aeroway: taxiway` > `kind_detail: taxiway`

* **roads** layer: `aerialway` > `kind_detail`
    * `aerialway: [gondola, cable_car]` > `kind_detail: [gondola, cable_car]`

* **boundaries** layer: `admin_level` > `kind_detail`
    * `admin_level: 2` > `kind_detail: 2`

* **pois** layer: `sport` > `kind_detail`
    * `feature.sport` > `feature.kind_detail`
    * `sport: basketball` > `kind_detail: basketball`

* **places** layer: `type` > `kind`
    * `type: country` > `kind: country`

* **buildings** layer: you may see unexpected results with building areas at mid-zooms because of merging
    * use new `scale_rank` to filter instead of area at zoom 13 and 14
    * zoom 13

        ```
        - { $zoom: [13], area: { min: 50000 } }
        - { $zoom: [13], height: { min: 250 } }
        - { $zoom: [13], volume: { min: 200000 } }
        ```

        to

        ```
        - { $zoom: [13], scale_rank: [1,2] }
        ```
    * zoom 14

        ```
        - { $zoom: [14], area: { min: 5000 } }
        - { $zoom: [14], height: { min: 190 } }
        - { $zoom: [14], volume: { min: 150000 } }
        ```

        to

        ```
        - { $zoom: [14], scale_rank: [1,2,3] }
        ```
    * Where scale_rank is defined in this table:

  	  |area|height|volume|scale_rank|
      |----|------|------|----------|
  	  |>=100000|>=250|>=300000|1|
  	  |>=20000|>=150|>=150000|2|
  	  |>=5000|>=100|>=100000|3|
  	  |>=1000|  | >=50000|4|
  	  |<500|<100|<50000|5|

* **buildings** layer: `kind` properties are now `kind_detail`
    * `kind: [university, college, school, kindergarten]` > `kind_detail: [university, college, school, kindergarten]`
    * `kind` values in buildings are now `building` or `building_part` (in addition to address & etc)


* **places** layer: `scalerank` > `min_zoom`
     * you can generally remove the scalerank filters completely from low zooms, as well as source filters.
     * at mid zooms you can still mix and match Natural Earth and OpenStreetMap features to "backfill" low or no pop places.
     * `scalerank: [0]`  > `min_zoom: [2]`
     * `scalerank: [1]`  > `min_zoom: [3]`
     * `scalerank: [2]`  > `min_zoom: [4]`
     * `scalerank: [3]`  > `min_zoom: [5]`
     * `scalerank: [4]`  > `min_zoom: [5]`
     * `scalerank: [5]`  > `min_zoom: [6]`
     * `scalerank: [6]`  > `min_zoom: [6]`
     * `scalerank: [7]`  > `min_zoom: [7]`
     * `scalerank: [8]`  > `min_zoom: [9]`
     * `scalerank: [9]`  > `min_zoom: [9]`
     * `scalerank: [10]` > `min_zoom: [10]`


* **boundaries** layer: `scalerank` > `min_zoom`
     * `scalerank: [0]`  > `min_zoom: [7]`
     * `scalerank: [1]`  > `min_zoom: [2]`
     * `scalerank: [2]`  > `min_zoom: [2]`
     * `scalerank: [3]`  > `min_zoom: [3]`
     * `scalerank: [4]`  > `min_zoom: [5]`
     * `scalerank: [5]`  > `min_zoom: [5.5]`
     * `scalerank: [6]`  > `min_zoom: [6]`
     * `scalerank: [7]`  > `min_zoom: [6.7]`
     * `scalerank: [8]`  > `min_zoom: [6.8]`
     * `scalerank: [9]`  > `min_zoom: [7]`
     * `filter: { scalerank: [0,3,4,5,6,7,8,9,10], $zoom: { max: 8 } }` > `filter: { not: { min_zoom: [1,2] }, $zoom: { max: 8 } }`

* **landuse** layer (and points-of-interest that have areas from landuse polygons)
    * remove all the area filters
    * except:
        * `kind: [garden, allotments]`
        * `kind: [police, fire_station, substation, plant, wastewater_plant, water_works]`
        * `kind: [cafe, restaurant, nursing_home]`
        * `kind: [parking, pedestrian, common, pitch, place_of_worship, playground, school, nursing_home]`

* **place** layer: `kind values`
    * `kind: [city, town]` > `kind: locality`
    * `kind: [village]` > `kind_detail: [village]`
    * `kind: [hamlet]` > `kind_detail: [hamlet]`

* **place** layer: `capital` (and `yes`)
    * `capital: yes` > `country_capital: true`
    * `state_capital: yes` > `region_capital: true`

* **place** and **boundaries** layers: `region`
    * `kind: [state]` > `kind: [region]`

* **landuse** layer: `forest`
    * some values are now `natural_forest`
    * but many values are still forest

* **landuse** layer: `park`
    * some values are now `natural_park`
    * but many values are still park

* **landuse** layer: `wood`
    * some values are now `natural_wood`
    * but many values are still wood

* **earth** layer: `continent` labels
    * If you have not updated for several releases, continent labels moved to the earth layer (from places layer)

* **water** layer: `ocean` and `sea` labels
    * If you have not updated for several releases, ocean and sea labels moved to the water layer (from places layer)
