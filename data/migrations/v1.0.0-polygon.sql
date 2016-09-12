UPDATE
  planet_osm_polygon
  SET mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_polygon.*)
  WHERE
    (tags -> 'man_made' IN ('wastewater_plant', 'water_works', 'works') OR
     tags -> 'leisure' IN ('golf_course', 'nature_reserve', 'park', 'pitch') OR
     tags -> 'amenity' = 'grave_yard' OR
     tags -> 'landuse' IN ('cemetery', 'farm', 'forest', 'military', 'quarry', 'recreation_ground', 'village_green', 'winter_sports', 'wood') OR
     tags -> 'boundary' IN ('national_park', 'protected_area') OR
     tags -> 'power' IN ('plant', 'substation') OR
     tags -> 'natural' IN ('wood', 'forest') OR
     tags -> 'tourism' = 'gallery')
    AND COALESCE(mz_poi_min_zoom, 999) <> COALESCE(mz_calculate_min_zoom_pois(planet_osm_polygon.*), 999);

UPDATE
  planet_osm_polygon
  SET mz_landuse_min_zoom = mz_calculate_min_zoom_landuse(planet_osm_polygon.*)
  WHERE
    (tags -> 'man_made' IN ('wastewater_plant', 'water_works', 'works') OR
     tags -> 'leisure' IN ('golf_course', 'nature_reserve', 'park', 'pitch') OR
     tags -> 'natural' IN ('forest', 'park', 'wood') OR
     tags -> 'amenity' = 'grave_yard' OR
     tags -> 'landuse' IN ('cemetery', 'farm', 'forest', 'military', 'quarry', 'recreation_ground', 'village_green', 'winter_sports', 'wood') OR
     tags -> 'boundary' IN ('national_park', 'protected_area') OR
     tags -> 'power' IN ('plant', 'substation') OR
     tags -> 'natural' IN ('wood', 'forest'))
    AND COALESCE(mz_landuse_min_zoom, 999) <> COALESCE(mz_calculate_min_zoom_landuse(planet_osm_polygon.*), 999);

UPDATE planet_osm_polygon
  SET mz_building_min_zoom = mz_calculate_min_zoom_buildings(planet_osm_polygon.*)
  WHERE mz_calculate_min_zoom_buildings(planet_osm_polygon.*) IS NOT NULL;
    (tags -> 'building' IS NOT NULL AND (way_area >= 1600 OR volume >= 300000 ))
    AND COALESCE(mz_building_min_zoom, 999) <> COALESCE(mz_building_min_zoom(planet_osm_polygon.*), 999);

UPDATE planet_osm_polygon
  SET mz_label_placement = ST_PointOnSurface(way)
  WHERE mz_label_placement IS NULL;

CREATE INDEX new_planet_osm_polygon_pois_geom_index ON planet_osm_polygon USING gist(way) WHERE mz_poi_min_zoom IS NOT NULL;
CREATE INDEX new_planet_osm_polygon_pois_geom_6_index ON planet_osm_polygon USING gist(way) WHERE mz_poi_min_zoom <= 6;
CREATE INDEX new_planet_osm_polygon_pois_geom_9_index ON planet_osm_polygon USING gist(way) WHERE mz_poi_min_zoom <= 9;
CREATE INDEX new_planet_osm_polygon_pois_geom_12_index ON planet_osm_polygon USING gist(way) WHERE mz_poi_min_zoom <= 12;
CREATE INDEX new_planet_osm_polygon_pois_geom_15_index ON planet_osm_polygon USING gist(way) WHERE mz_poi_min_zoom <= 15;

BEGIN;
DROP INDEX IF EXISTS planet_osm_polygon_pois_geom_index;
ALTER INDEX new_planet_osm_polygon_pois_geom_index RENAME TO planet_osm_polygon_pois_geom_index;
COMMIT;

BEGIN;
DROP INDEX IF EXISTS planet_osm_polygon_pois_geom_6_index;
ALTER INDEX new_planet_osm_polygon_pois_geom_6_index RENAME TO planet_osm_polygon_pois_geom_6_index;
COMMIT;

BEGIN;
DROP INDEX IF EXISTS planet_osm_polygon_pois_geom_9_index;
ALTER INDEX new_planet_osm_polygon_pois_geom_9_index RENAME TO planet_osm_polygon_pois_geom_9_index;
COMMIT;

BEGIN;
DROP INDEX IF EXISTS planet_osm_polygon_pois_geom_12_index;
ALTER INDEX new_planet_osm_polygon_pois_geom_12_index RENAME TO planet_osm_polygon_pois_geom_12_index;
COMMIT;

BEGIN;
DROP INDEX IF EXISTS planet_osm_polygon_pois_geom_15_index;
ALTER INDEX new_planet_osm_polygon_pois_geom_15_index RENAME TO planet_osm_polygon_pois_geom_15_index;
COMMIT;
