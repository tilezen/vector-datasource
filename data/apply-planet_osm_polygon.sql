DO $$
BEGIN

--------------------------------------------------------------------------------
-- planet_osm_polygon
--------------------------------------------------------------------------------

-- indexes on existing columns
PERFORM mz_create_index_if_not_exists('planet_osm_polygon_wayarea_index', 'planet_osm_polygon', 'way_area');
PERFORM mz_create_partial_index_if_not_exists('planet_osm_polygon_building_index', 'planet_osm_polygon', 'building', 'building IS NOT NULL');
PERFORM mz_create_partial_index_if_not_exists('planet_osm_polygon_admin_level_index', 'planet_osm_polygon', 'admin_level', 'boundary = ''administrative''');

-- indexes on functions
CREATE INDEX planet_osm_polygon_is_building_or_part_index ON planet_osm_polygon(mz_calculate_is_building_or_part(building, "building:part")) WHERE mz_calculate_is_building_or_part(building, "building:part") = TRUE;
CREATE INDEX planet_osm_polygon_is_landuse_index ON planet_osm_polygon(mz_calculate_is_landuse("landuse", "leisure", "natural", "highway", "amenity", "aeroway")) WHERE mz_calculate_is_landuse("landuse", "leisure", "natural", "highway", "amenity", "aeroway") = TRUE;
CREATE INDEX planet_osm_polygon_is_water_index ON planet_osm_polygon(mz_calculate_is_water("waterway", "natural", "landuse")) WHERE mz_calculate_is_water("waterway", "natural", "landuse") = TRUE;

END $$;
