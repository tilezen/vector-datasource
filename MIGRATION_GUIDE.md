This is a cheat sheet summarizing the v1.0 Mapzen Vector Tiles [CHANGLELOG](https://github.com/tilezen/vector-datasource/blob/master/CHANGELOG.md)'s **major breaking changes** that we used to update Mapzen house styles.

* **Topic**
  * **example** Tangram scene file YAML `old` > `new`

===

* new tile url sources:
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
  * for OSM roads in mid and high zooms, optionally:

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

* **buildings** layer: building area are funky at mid-zooms now because of merging
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

	```
	  area,height,volume,landuse_kind,scale_rank
	  >=100000,*,*,*,1
	  *,>=250,*,*,1
	  *,*,>=300000,*,1
	  >=20000,*,*,*,2
	  >=5000,*,*,+,2
	  *,>=150,*,*,2
	  *,*,>=150000,*,2
	  >=5000,*,*,*,3
	  >=3000,*,*,+,3
	  *,>=100,*,*,3
	  *,*,>=100000,*,3
	  >=1000,*,*,*,4
	  >=500,*,*,+,4
	  *,*,>=50000,*,4
	  +,*,*,*,5
	```

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
   * `scalerank: [0]`  > `min_zoom: [7]` (yeah, right! this was to fix bad data, see Hungry)
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

* **landuse** layer (and pois that have areas from landuse polygons:
  * remove all the area filters
  * except:
      * `kind: [garden, allotments]`
      * `kind: [police, fire_station, substation, plant, wastewater_plant, water_works]`
      * `kind: [cafe, restaurant, nursing_home]`
      * `kind: [parking, pedestrian, common, pitch, place_of_worship, playground, school, nursing_home]`

* **place** layer: kind values
  * `kind: [city, town]` > `kind: locality`
  * `kind: [village]` > `kind_detail: [village]`
  * `kind: [hamlet]` > `kind_detail: [hamlet]`

* **place** layer: `capital` (and `yes`)
  * `capital: yes` > `country_capital: true`
  * `state_capital: yes` > `region_capital: true

* **place** and **boundaries** layers: region
  * `kind: [state]` > `kind: [region]`

* **landuse** layer: `forest`
  * some values are now `natural_forest`
  * but many values are still forest

* **landuse** layer: `park`
  * some values are now `natural_park`
  * but many values are still park

* **landuse** layer: `wood`
  * some values are now `natural_wood`
  * but many values are still work

* **earth** layer: `continent` labels
  * If you haven't updated for several versions, continent labels moved to the earth layer (from places layer)
  
* **water** layer: `ocean` and `sea` labels
  * If you haven't updated for several versions, ocean and sea labels moved to the water layer (from places layer)