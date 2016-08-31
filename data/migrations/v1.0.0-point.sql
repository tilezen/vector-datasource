UPDATE
  planet_osm_point
  SET mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_point.*)
  WHERE
    (tags -> 'man_made' IN ('wastewater_plant', 'water_works', 'works') OR
     tags -> 'leisure' IN ('golf_course', 'nature_reserve', 'park', 'pitch') OR
     tags -> 'landuse' IN ('cemetery', 'farm', 'forest', 'military', 'quarry', 'recreation_ground', 'village_green', 'winter_sports', 'wood') OR
     tags -> 'amenity' = 'grave_yard' OR
     tags -> 'boundary' IN ('national_park', 'protected_area') OR
     tags -> 'power' IN ('plant', 'substation') OR
     tags -> 'natural' IN ('wood', 'forest') OR
     tags -> 'tourism' = 'gallery')
    AND COALESCE(mz_poi_min_zoom, 999) <> COALESCE(mz_calculate_min_zoom_pois(planet_osm_point.*), 999);

CREATE INDEX new_planet_osm_point_min_zoom_pois_index ON planet_osm_point USING gist(way) WHERE mz_poi_min_zoom IS NOT NULL;
CREATE INDEX new_planet_osm_point_min_zoom_pois_6_index ON planet_osm_point USING gist(way) WHERE mz_poi_min_zoom <= 6;
CREATE INDEX new_planet_osm_point_min_zoom_pois_9_index ON planet_osm_point USING gist(way) WHERE mz_poi_min_zoom <= 9;
CREATE INDEX new_planet_osm_point_min_zoom_pois_12_index ON planet_osm_point USING gist(way) WHERE mz_poi_min_zoom <= 12;
CREATE INDEX new_planet_osm_point_min_zoom_pois_15_index ON planet_osm_point USING gist(way) WHERE mz_poi_min_zoom <= 15;

BEGIN;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_pois_index;
ALTER INDEX new_planet_osm_point_min_zoom_pois_index RENAME TO planet_osm_point_min_zoom_pois_index;
COMMIT;

BEGIN;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_pois_6_index;
ALTER INDEX new_planet_osm_point_min_zoom_pois_6_index RENAME TO planet_osm_point_min_zoom_pois_6_index;
COMMIT;

BEGIN;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_pois_9_index;
ALTER INDEX new_planet_osm_point_min_zoom_pois_9_index RENAME TO planet_osm_point_min_zoom_pois_9_index;
COMMIT;

BEGIN;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_pois_12_index;
ALTER INDEX new_planet_osm_point_min_zoom_pois_12_index RENAME TO planet_osm_point_min_zoom_pois_12_index;
COMMIT;

BEGIN;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_pois_15_index;
ALTER INDEX new_planet_osm_point_min_zoom_pois_15_index RENAME TO planet_osm_point_min_zoom_pois_15_index;
COMMIT;

DROP INDEX IF EXISTS planet_osm_point_min_zoom_way_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_wa9_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_way_9_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_way_12_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_way_15_index;
