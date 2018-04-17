-- Add new shop types
UPDATE planet_osm_point
  SET mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_point.*)
  WHERE mz_poi_min_zoom <> mz_calculate_min_zoom_pois(planet_osm_point.*)
    AND (shop IN ('art', 'beauty', 'coffee', 'deli', 'furniture', 'hifi',
    'newsagent', 'perfumery', 'shoes', 'stationery', 'tobacco', 'travel_agency',
    'variety_store')
      OR tourism in ('alpine_hut')
      OR amenity IN ('bar', 'car_wash', 'charging_station', 'hunting_stand', 'marketplace', 'motorcycle_parking', 'nightclub'));

-- ladder the point indexes
SET client_min_messages TO WARNING;
CREATE INDEX IF NOT EXISTS
  planet_osm_point_geom_min_zoom_6_index
  ON planet_osm_point USING gist(way)
  WHERE
    mz_building_min_zoom < 6 OR
    mz_earth_min_zoom < 6 OR
    mz_places_min_zoom < 6 OR
    mz_poi_min_zoom < 6 OR
    mz_water_min_zoom < 6;

CREATE INDEX IF NOT EXISTS
  planet_osm_point_geom_min_zoom_9_index
  ON planet_osm_point USING gist(way)
  WHERE
    mz_building_min_zoom < 9 OR
    mz_earth_min_zoom < 9 OR
    mz_places_min_zoom < 9 OR
    mz_poi_min_zoom < 9 OR
    mz_water_min_zoom < 9;

CREATE INDEX IF NOT EXISTS
  planet_osm_point_geom_min_zoom_12_index
  ON planet_osm_point USING gist(way)
  WHERE
    mz_building_min_zoom < 12 OR
    mz_earth_min_zoom < 12 OR
    mz_places_min_zoom < 12 OR
    mz_poi_min_zoom < 12 OR
    mz_water_min_zoom < 12;

CREATE INDEX IF NOT EXISTS
  planet_osm_point_geom_min_zoom_15_index
  ON planet_osm_point USING gist(way)
  WHERE
    mz_building_min_zoom < 15 OR
    mz_earth_min_zoom < 15 OR
    mz_places_min_zoom < 15 OR
    mz_poi_min_zoom < 15 OR
    mz_water_min_zoom < 15;

CREATE INDEX IF NOT EXISTS
  planet_osm_point_geom_min_zoom_index
  ON planet_osm_point USING gist(way)
  WHERE
    mz_building_min_zoom IS NOT NULL OR
    mz_earth_min_zoom IS NOT NULL OR
    mz_places_min_zoom IS NOT NULL OR
    mz_poi_min_zoom IS NOT NULL OR
    mz_water_min_zoom IS NOT NULL;

-- remove all old indexes

DROP INDEX IF EXISTS planet_osm_point_min_zoom_pois_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_pois_6_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_pois_9_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_pois_12_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_pois_15_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_earth_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_earth_9_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_earth_12_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_earth_15_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_water_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_water_9_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_water_12_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_water_15_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_places_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_places_9_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_places_12_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_places_15_index;
RESET client_min_messages;
