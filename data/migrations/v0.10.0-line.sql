UPDATE planet_osm_line
SET mz_water_min_zoom = mz_calculate_min_zoom_water(planet_osm_line.*)
WHERE mz_calculate_min_zoom_water(planet_osm_line.*) IS NOT NULL;

CREATE INDEX new_planet_osm_line_water_geom_9_index ON planet_osm_line USING gist(way) WHERE mz_water_min_zoom <= 9;
CREATE INDEX new_planet_osm_line_water_geom_12_index ON planet_osm_line USING gist(way) WHERE mz_water_min_zoom <= 12;
CREATE INDEX new_planet_osm_line_water_geom_15_index ON planet_osm_line USING gist(way) WHERE mz_water_min_zoom <= 15;

BEGIN;
  DROP INDEX IF EXISTS planet_osm_line_water_geom_9_index;
  DROP INDEX IF EXISTS planet_osm_line_water_geom_12_index;
  DROP INDEX IF EXISTS planet_osm_line_water_geom_15_index;

  ALTER INDEX new_planet_osm_line_water_geom_9_index RENAME TO planet_osm_line_water_geom_9_index;
  ALTER INDEX new_planet_osm_line_water_geom_12_index RENAME TO planet_osm_line_water_geom_12_index;
  ALTER INDEX new_planet_osm_line_water_geom_15_index RENAME TO planet_osm_line_water_geom_15_index;
COMMIT;
