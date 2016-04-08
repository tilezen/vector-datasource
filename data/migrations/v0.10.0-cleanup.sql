DROP INDEX IF EXISTS planet_osm_line_waterway_index;
DROP INDEX IF EXISTS planet_osm_point_water_index;
DROP INDEX IF EXISTS planet_osm_polygon_water_geom_index;

DROP FUNCTION IF EXISTS mz_calculate_is_water(text, text, text, text, text);

DROP INDEX IF EXISTS planet_osm_point_place_index;

DROP INDEX IF EXISTS planet_osm_polygon_admin_level_index;
DROP INDEX IF EXISTS planet_osm_polygon_admin_level_geom_index;

DROP INDEX IF EXISTS planet_osm_polygon_landuse_boundary_geom_4_index;
DROP INDEX IF EXISTS planet_osm_polygon_landuse_boundary_geom_6_index;
DROP INDEX IF EXISTS planet_osm_polygon_landuse_boundary_geom_8_index;

DROP FUNCTION IF EXISTS mz_building_filter(text, text, FLOAT, FLOAT, FLOAT);
