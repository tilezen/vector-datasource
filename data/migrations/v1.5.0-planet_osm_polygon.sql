-- Add new shop types
UPDATE planet_osm_polygon
  SET mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_polygon.*)
  WHERE mz_poi_min_zoom <> mz_calculate_min_zoom_pois(planet_osm_polygon.*)
    AND (shop IN ('art', 'beauty', 'coffee', 'deli', 'furniture', 'hifi',
    'newsagent', 'perfumery', 'shoes', 'stationery', 'tobacco', 'travel_agency',
    'variety_store')
      OR amenity IN ('bar', 'car_wash', 'charging_station', 'hunting_stand', 'marketplace', 'motorcycle_parking', 'nightclub'));

-- polygon low zoom
SET client_min_messages TO WARNING;
CREATE INDEX IF NOT EXISTS
  planet_osm_polygon_geom_min_zoom_7_index
  ON planet_osm_polygon USING gist(way)
  WHERE
    mz_landuse_min_zoom < 7 OR
    mz_poi_min_zoom < 7 OR
    mz_transit_level < 7;

-- polygon zoom 7 specific query
CREATE INDEX IF NOT EXISTS
  planet_osm_polygon_geom_min_zoom_8_index
  ON planet_osm_polygon USING gist(way)
  WHERE
    mz_earth_min_zoom < 8 OR
    mz_landuse_min_zoom < 8 OR
    mz_poi_min_zoom < 8 OR
    mz_transit_level < 8;

-- ladder the rest of the polygon queries
CREATE INDEX IF NOT EXISTS
  planet_osm_polygon_geom_min_zoom_9_index
  ON planet_osm_polygon USING gist(way)
  WHERE
    mz_boundary_min_zoom < 9 OR
    mz_building_min_zoom < 9 OR
    mz_earth_min_zoom < 9 OR
    mz_landuse_min_zoom < 9 OR
    mz_poi_min_zoom < 9 OR
    mz_transit_level < 9 OR
    mz_water_min_zoom < 9;

CREATE INDEX IF NOT EXISTS
  planet_osm_polygon_geom_min_zoom_12_index
  ON planet_osm_polygon USING gist(way)
  WHERE
    mz_boundary_min_zoom < 12 OR
    mz_building_min_zoom < 12 OR
    mz_earth_min_zoom < 12 OR
    mz_landuse_min_zoom < 12 OR
    mz_poi_min_zoom < 12 OR
    mz_transit_level < 12 OR
    mz_water_min_zoom < 12;

CREATE INDEX IF NOT EXISTS
  planet_osm_polygon_geom_min_zoom_15_index
  ON planet_osm_polygon USING gist(way)
  WHERE
    mz_boundary_min_zoom < 15 OR
    mz_building_min_zoom < 15 OR
    mz_earth_min_zoom < 15 OR
    mz_landuse_min_zoom < 15 OR
    mz_poi_min_zoom < 15 OR
    mz_transit_level < 15 OR
    mz_water_min_zoom < 15;

CREATE INDEX IF NOT EXISTS
  planet_osm_polygon_geom_min_zoom_index
  ON planet_osm_polygon USING gist(way)
  WHERE
    mz_boundary_min_zoom IS NOT NULL OR
    mz_building_min_zoom IS NOT NULL OR
    mz_earth_min_zoom IS NOT NULL OR
    mz_landuse_min_zoom IS NOT NULL OR
    mz_poi_min_zoom IS NOT NULL OR
    mz_transit_level IS NOT NULL OR
    mz_water_min_zoom IS NOT NULL;


-- remove all old indexes

DROP INDEX IF EXISTS planet_osm_polygon_landuse_geom_index;
DROP INDEX IF EXISTS planet_osm_polygon_landuse_geom_9_index;
DROP INDEX IF EXISTS planet_osm_polygon_landuse_geom_12_index;
DROP INDEX IF EXISTS planet_osm_polygon_landuse_geom_15_index;
DROP INDEX IF EXISTS planet_osm_polygon_transit_geom_index;
DROP INDEX IF EXISTS planet_osm_polygon_transit_geom_6_index;
DROP INDEX IF EXISTS planet_osm_polygon_transit_geom_9_index;
DROP INDEX IF EXISTS planet_osm_polygon_transit_geom_12_index;
DROP INDEX IF EXISTS planet_osm_polygon_transit_geom_15_index;
DROP INDEX IF EXISTS planet_osm_polygon_earth_geom_index;
DROP INDEX IF EXISTS planet_osm_polygon_earth_geom_9_index ;
DROP INDEX IF EXISTS planet_osm_polygon_earth_geom_12_index;
DROP INDEX IF EXISTS planet_osm_polygon_earth_geom_15_index;
DROP INDEX IF EXISTS planet_osm_polygon_water_geom_index;
DROP INDEX IF EXISTS planet_osm_polygon_water_geom_9_index;
DROP INDEX IF EXISTS planet_osm_polygon_water_geom_12_index;
DROP INDEX IF EXISTS planet_osm_polygon_water_geom_15_index;
DROP INDEX IF EXISTS planet_osm_polygon_boundary_geom_index;
DROP INDEX IF EXISTS planet_osm_polygon_boundary_geom_9_index;
DROP INDEX IF EXISTS planet_osm_polygon_boundary_geom_12_index;
DROP INDEX IF EXISTS planet_osm_polygon_boundary_geom_15_index;
DROP INDEX IF EXISTS planet_osm_polygon_building_geom_index;
DROP INDEX IF EXISTS planet_osm_polygon_building_geom_15_index;
DROP INDEX IF EXISTS planet_osm_polygon_pois_geom_index;
DROP INDEX IF EXISTS planet_osm_polygon_pois_geom_6_index;
DROP INDEX IF EXISTS planet_osm_polygon_pois_geom_9_index;
DROP INDEX IF EXISTS planet_osm_polygon_pois_geom_12_index;
DROP INDEX IF EXISTS planet_osm_polygon_pois_geom_15_index;
RESET client_min_messages;
