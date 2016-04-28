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

DROP FUNCTION IF EXISTS mz_calculate_highway_level(highway_val text, service_val text);
DROP FUNCTION IF EXISTS mz_calculate_highway_level(highway_val text, service_val text, name_val text, bicycle_val text, foot_val text, horse_val text, snowmobile_val text, ski_val text, osm_id bigint);

DROP FUNCTION IF EXISTS mz_calculate_railway_level(text, text);
DROP FUNCTION IF EXISTS mz_calculate_highway_level(text, text, text, text, text, text, text, text, BIGINT);
DROP FUNCTION IF EXISTS mz_calculate_aeroway_level(text);
DROP FUNCTION IF EXISTS mz_calculate_aerialway_level(text);
DROP FUNCTION IF EXISTS mz_calculate_leisure_level(text, text);
DROP FUNCTION IF EXISTS mz_calculate_man_made_level(text);
DROP FUNCTION IF EXISTS mz_calculate_road_level(text, text, text, text, text, text, text, text, text, geometry, text, text, text, text, text, text, BIGINT, text);

-- function was re-implemented in YAML
DROP FUNCTION IF EXISTS mz_is_path_named_or_designated(text, text, text, text, text, text, text);
