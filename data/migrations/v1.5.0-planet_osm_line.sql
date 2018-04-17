-- Add new barrier types
UPDATE planet_osm_line
  SET mz_landuse_min_zoom = mz_calculate_min_zoom_landuse(planet_osm_line.*)
  WHERE mz_landuse_min_zoom <> mz_calculate_min_zoom_landuse(planet_osm_line.*)
    AND (barrier IN ('wall')
         OR power IN ('line','minor_line'));
SET client_min_messages TO WARNING;
CREATE INDEX IF NOT EXISTS
  planet_osm_line_geom_min_zoom_8_index
  ON planet_osm_line USING gist(way)
  WHERE
    mz_landuse_min_zoom < 8 OR
    mz_transit_level < 8;

-- ladder the higher zoom level indexes
CREATE INDEX IF NOT EXISTS
  planet_osm_line_geom_min_zoom_9_index
  ON planet_osm_line USING gist(way)
  WHERE
    mz_earth_min_zoom < 9 OR
    mz_landuse_min_zoom < 9 OR
    mz_road_level < 9 OR
    mz_transit_level < 9 OR
    mz_water_min_zoom < 9;

CREATE INDEX IF NOT EXISTS
  planet_osm_line_geom_min_zoom_12_index
  ON planet_osm_line USING gist(way)
  WHERE
    mz_earth_min_zoom < 12 OR
    mz_landuse_min_zoom < 12 OR
    mz_road_level < 12 OR
    mz_transit_level < 12 OR
    mz_water_min_zoom < 12;

CREATE INDEX IF NOT EXISTS
  planet_osm_line_geom_min_zoom_15_index
  ON planet_osm_line USING gist(way)
  WHERE
    mz_earth_min_zoom < 15 OR
    mz_landuse_min_zoom < 15 OR
    mz_road_level < 15 OR
    mz_transit_level < 15 OR
    mz_water_min_zoom < 15;

CREATE INDEX IF NOT EXISTS
  planet_osm_line_geom_min_zoom_index
  ON planet_osm_line USING gist(way)
  WHERE
    mz_earth_min_zoom IS NOT NULL OR
    mz_landuse_min_zoom IS NOT NULL OR
    mz_road_level IS NOT NULL OR
    mz_transit_level IS NOT NULL OR
    mz_water_min_zoom IS NOT NULL;

-- remove all old indexes

DROP INDEX IF EXISTS planet_osm_line_roads_geom_index;
DROP INDEX IF EXISTS planet_osm_line_roads_geom_9_index;
DROP INDEX IF EXISTS planet_osm_line_roads_geom_12_index;
DROP INDEX IF EXISTS planet_osm_line_roads_geom_15_index;
DROP INDEX IF EXISTS planet_osm_line_transit_geom_index;
DROP INDEX IF EXISTS planet_osm_line_transit_geom_6_index;
DROP INDEX IF EXISTS planet_osm_line_transit_geom_9_index;
DROP INDEX IF EXISTS planet_osm_line_transit_geom_12_index;
DROP INDEX IF EXISTS planet_osm_line_transit_geom_15_index;
DROP INDEX IF EXISTS planet_osm_line_earth_geom_index;
DROP INDEX IF EXISTS planet_osm_line_earth_geom_9_index;
DROP INDEX IF EXISTS planet_osm_line_earth_geom_12_index;
DROP INDEX IF EXISTS planet_osm_line_earth_geom_15_index;
DROP INDEX IF EXISTS planet_osm_line_water_geom_index;
DROP INDEX IF EXISTS planet_osm_line_water_geom_9_index;
DROP INDEX IF EXISTS planet_osm_line_water_geom_12_index;
DROP INDEX IF EXISTS planet_osm_line_water_geom_15_index;
DROP INDEX IF EXISTS planet_osm_line_boundary_geom_index;
DROP INDEX IF EXISTS planet_osm_line_boundary_geom_9_index;
DROP INDEX IF EXISTS planet_osm_line_boundary_geom_12_index;
DROP INDEX IF EXISTS planet_osm_line_boundary_geom_15_index;
RESET client_min_messages;
