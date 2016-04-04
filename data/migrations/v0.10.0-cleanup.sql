DROP INDEX IF EXISTS planet_osm_line_waterway_index;
DROP INDEX IF EXISTS planet_osm_point_water_index;
DROP INDEX IF EXISTS planet_osm_polygon_water_geom_index;

DROP FUNCTION IF EXISTS mz_calculate_is_water(text, text, text, text, text);
