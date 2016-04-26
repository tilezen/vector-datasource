UPDATE planet_osm_line
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(planet_osm_line.*)
  WHERE mz_calculate_min_zoom_water(planet_osm_line.*) IS NOT NULL;

-- drop indexes first, so that the update goes faster
DROP INDEX IF EXISTS planet_osm_line_roads_geom_index;
DROP INDEX IF EXISTS planet_osm_line_roads_geom_9_index;
DROP INDEX IF EXISTS planet_osm_line_roads_geom_12_index;
DROP INDEX IF EXISTS planet_osm_line_roads_geom_15_index;

UPDATE planet_osm_line
  SET mz_road_level = mz_calculate_min_zoom_roads(planet_osm_line.*)
  WHERE
    mz_calculate_min_zoom_roads(planet_osm_line.*) IS NOT NULL;

-- however, there are some things which might now be NULL which weren't before,
-- and so we need to update those too.
UPDATE planet_osm_line
  SET mz_road_level = NULL
  WHERE
    mz_calculate_min_zoom_roads(planet_osm_line.*) IS NULL AND
    mz_road_level IS NOT NULL;

UPDATE planet_osm_line
  SET mz_landuse_min_zoom = mz_calculate_min_zoom_landuse(planet_osm_line.*)
  WHERE
    mz_calculate_min_zoom_landuse(planet_osm_line.*) IS NOT NULL;

CREATE INDEX new_planet_osm_line_roads_geom_index ON planet_osm_line USING gist(way) WHERE mz_road_level IS NOT NULL;
CREATE INDEX new_planet_osm_line_roads_geom_9_index ON planet_osm_line USING gist(way) WHERE mz_road_level <= 9;
CREATE INDEX new_planet_osm_line_roads_geom_12_index ON planet_osm_line USING gist(way) WHERE mz_road_level <= 12;
CREATE INDEX new_planet_osm_line_roads_geom_15_index ON planet_osm_line USING gist(way) WHERE mz_road_level <= 15;

CREATE INDEX new_planet_osm_line_landuse_geom_index ON planet_osm_line USING gist(way) WHERE mz_landuse_min_zoom IS NOT NULL;
CREATE INDEX new_planet_osm_line_landuse_geom_9_index ON planet_osm_line USING gist(way) WHERE mz_landuse_min_zoom <= 9;
CREATE INDEX new_planet_osm_line_landuse_geom_12_index ON planet_osm_line USING gist(way) WHERE mz_landuse_min_zoom <= 12;
CREATE INDEX new_planet_osm_line_landuse_geom_15_index ON planet_osm_line USING gist(way) WHERE mz_landuse_min_zoom <= 15;

UPDATE planet_osm_line
SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(planet_osm_line.*)
WHERE
  waterway = 'dam';

CREATE INDEX new_planet_osm_line_water_geom_9_index ON planet_osm_line USING gist(way) WHERE mz_water_min_zoom <= 9;
CREATE INDEX new_planet_osm_line_water_geom_12_index ON planet_osm_line USING gist(way) WHERE mz_water_min_zoom <= 12;
CREATE INDEX new_planet_osm_line_water_geom_15_index ON planet_osm_line USING gist(way) WHERE mz_water_min_zoom <= 15;

CREATE INDEX new_planet_osm_line_boundary_geom_9_index ON planet_osm_line USING gist(way) WHERE mz_boundary_min_zoom <= 9;
CREATE INDEX new_planet_osm_line_boundary_geom_12_index ON planet_osm_line USING gist(way) WHERE mz_boundary_min_zoom <= 12;
CREATE INDEX new_planet_osm_line_boundary_geom_15_index ON planet_osm_line USING gist(way) WHERE mz_boundary_min_zoom <= 15;

CREATE INDEX new_planet_osm_line_natural_geom_index ON planet_osm_line USING gist(way) WHERE "natural" IN ('cliff','arete','ridge','valley');

BEGIN;
  DROP INDEX IF EXISTS planet_osm_line_roads_geom_index;
  DROP INDEX IF EXISTS planet_osm_line_roads_geom_9_index;
  DROP INDEX IF EXISTS planet_osm_line_roads_geom_12_index;
  DROP INDEX IF EXISTS planet_osm_line_roads_geom_15_index;

  ALTER INDEX new_planet_osm_line_roads_geom_index RENAME TO planet_osm_line_roads_geom_index;
  ALTER INDEX new_planet_osm_line_roads_geom_9_index RENAME TO planet_osm_line_roads_geom_9_index;
  ALTER INDEX new_planet_osm_line_roads_geom_12_index RENAME TO planet_osm_line_roads_geom_12_index;
  ALTER INDEX new_planet_osm_line_roads_geom_15_index RENAME TO planet_osm_line_roads_geom_15_index;

  DROP INDEX IF EXISTS planet_osm_line_landuse_geom_index;
  DROP INDEX IF EXISTS planet_osm_line_landuse_geom_9_index;
  DROP INDEX IF EXISTS planet_osm_line_landuse_geom_12_index;
  DROP INDEX IF EXISTS planet_osm_line_landuse_geom_15_index;

  ALTER INDEX new_planet_osm_line_landuse_geom_index RENAME TO planet_osm_line_landuse_geom_index;
  ALTER INDEX new_planet_osm_line_landuse_geom_9_index RENAME TO planet_osm_line_landuse_geom_9_index;
  ALTER INDEX new_planet_osm_line_landuse_geom_12_index RENAME TO planet_osm_line_landuse_geom_12_index;
  ALTER INDEX new_planet_osm_line_landuse_geom_15_index RENAME TO planet_osm_line_landuse_geom_15_index;

  DROP INDEX IF EXISTS planet_osm_line_water_geom_9_index;
  DROP INDEX IF EXISTS planet_osm_line_water_geom_12_index;
  DROP INDEX IF EXISTS planet_osm_line_water_geom_15_index;
  DROP INDEX IF EXISTS planet_osm_line_natural_geom_index;

  ALTER INDEX new_planet_osm_line_water_geom_9_index RENAME TO planet_osm_line_water_geom_9_index;
  ALTER INDEX new_planet_osm_line_water_geom_12_index RENAME TO planet_osm_line_water_geom_12_index;
  ALTER INDEX new_planet_osm_line_water_geom_15_index RENAME TO planet_osm_line_water_geom_15_index;
  ALTER INDEX new_planet_osm_line_natural_geom_index RENAME TO planet_osm_line_natural_geom_index;

  DROP INDEX IF EXISTS planet_osm_line_boundary_geom_9_index;
  DROP INDEX IF EXISTS planet_osm_line_boundary_geom_12_index;
  DROP INDEX IF EXISTS planet_osm_line_boundary_geom_15_index;

  ALTER INDEX new_planet_osm_line_boundary_geom_9_index RENAME TO planet_osm_line_boundary_geom_9_index;
  ALTER INDEX new_planet_osm_line_boundary_geom_12_index RENAME TO planet_osm_line_boundary_geom_12_index;
  ALTER INDEX new_planet_osm_line_boundary_geom_15_index RENAME TO planet_osm_line_boundary_geom_15_index;
COMMIT;
