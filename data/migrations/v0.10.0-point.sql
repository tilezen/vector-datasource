UPDATE planet_osm_point
SET mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_point.*)
WHERE
  amenity = 'boat_rental' OR
  shop = 'boat_rental' OR
  tags->'rental' = 'boat' OR
  (shop = 'boat' AND tags->'rental' = 'yes') OR
  man_made IN ('beacon', 'cross', 'mineshaft', 'adit', 'water_well') OR
  "natural" IN ('saddle', 'dune', 'geyser', 'sinkhole', 'hot_spring', 'rock', 'stone') OR
  highway = 'trailhead' OR
  tags->'whitewater' IN ('put_in;egress', 'put_in', 'egress', 'hazard', 'rapid');

UPDATE planet_osm_point
SET mz_water_min_zoom = mz_calculate_min_zoom_water(planet_osm_point.*)
WHERE mz_calculate_min_zoom_water(planet_osm_point.*) IS NOT NULL;

UPDATE planet_osm_point
  SET mz_places_min_zoom = mz_calculate_min_zoom_places(planet_osm_point.*)
  WHERE mz_calculate_min_zoom_places(planet_osm_point.*) IS NOT NULL;

UPDATE planet_osm_point
  SET mz_building_min_zoom = mz_calculate_min_zoom_buildings(planet_osm_point.*)
  WHERE mz_calculate_min_zoom_buildings(planet_osm_point.*) IS NOT NULL;

CREATE INDEX new_planet_osm_point_min_zoom_water_9_index ON planet_osm_point USING gist(way) WHERE mz_water_min_zoom <= 9;
CREATE INDEX new_planet_osm_point_min_zoom_water_12_index ON planet_osm_point USING gist(way) WHERE mz_water_min_zoom <= 12;
CREATE INDEX new_planet_osm_point_min_zoom_water_15_index ON planet_osm_point USING gist(way) WHERE mz_water_min_zoom <= 15;

CREATE INDEX new_planet_osm_point_min_zoom_places_9_index ON planet_osm_point USING gist(way) WHERE mz_places_min_zoom <= 9;
CREATE INDEX new_planet_osm_point_min_zoom_places_12_index ON planet_osm_point USING gist(way) WHERE mz_places_min_zoom <= 12;
CREATE INDEX new_planet_osm_point_min_zoom_places_15_index ON planet_osm_point USING gist(way) WHERE mz_places_min_zoom <= 15;

BEGIN;
  DROP INDEX IF EXISTS planet_osm_point_min_zoom_water_9_index;
  DROP INDEX IF EXISTS planet_osm_point_min_zoom_water_12_index;
  DROP INDEX IF EXISTS planet_osm_point_min_zoom_water_15_index;

  ALTER INDEX new_planet_osm_point_min_zoom_water_9_index RENAME TO planet_osm_point_min_zoom_water_9_index;
  ALTER INDEX new_planet_osm_point_min_zoom_water_12_index RENAME TO planet_osm_point_min_zoom_water_12_index;
  ALTER INDEX new_planet_osm_point_min_zoom_water_15_index RENAME TO planet_osm_point_min_zoom_water_15_index;

  DROP INDEX IF EXISTS planet_osm_point_min_zoom_places_9_index;
  DROP INDEX IF EXISTS planet_osm_point_min_zoom_places_12_index;
  DROP INDEX IF EXISTS planet_osm_point_min_zoom_places_15_index;

  ALTER INDEX new_planet_osm_point_min_zoom_places_9_index RENAME TO planet_osm_point_min_zoom_places_9_index;
  ALTER INDEX new_planet_osm_point_min_zoom_places_12_index RENAME TO planet_osm_point_min_zoom_places_12_index;
  ALTER INDEX new_planet_osm_point_min_zoom_places_15_index RENAME TO planet_osm_point_min_zoom_places_15_index;
COMMIT;
