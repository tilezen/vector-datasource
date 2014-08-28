DO $$
BEGIN

--------------------------------------------------------------------------------
-- planet_osm_polygon
--------------------------------------------------------------------------------

ALTER TABLE planet_osm_polygon
    ADD COLUMN mz_id TEXT,
    ADD COLUMN mz_height FLOAT,
    ADD COLUMN mz_min_height FLOAT,
    ADD COLUMN mz_is_landuse BOOLEAN,
    ADD COLUMN mz_is_water BOOLEAN,
    ADD COLUMN mz_is_building_or_part BOOLEAN;
PERFORM AddGeometryColumn('planet_osm_polygon', 'mz_way14', 900913, 'Geometry', 2);
PERFORM AddGeometryColumn('planet_osm_polygon', 'mz_way12', 900913, 'Geometry', 2);
PERFORM AddGeometryColumn('planet_osm_polygon', 'mz_way11', 900913, 'Geometry', 2);

UPDATE planet_osm_polygon AS t SET
    mz_id = mz_normalize_id(t.osm_id, t.way),
    mz_height = (CASE WHEN t.height IS NOT NULL THEN mz_safe_convert_to_float(t.height) ELSE NULL END),
    mz_min_height = (CASE WHEN t.min_height IS NOT NULL THEN mz_safe_convert_to_float(t.min_height) ELSE NULL END),
    mz_is_building_or_part = (CASE WHEN mz_calculate_is_building_or_part(t.building, "building:part") = TRUE THEN TRUE ELSE NULL END),
    mz_is_landuse = p.mz_is_landuse,
    mz_is_water = p.mz_is_water,
    mz_way14 = (CASE WHEN t.way IS NOT NULL AND t.building IS NOT NULL THEN ST_SimplifyPreserveTopology(t.way, 9.55) ELSE NULL END),
    mz_way12 = (CASE WHEN t.way IS NOT NULL AND p.mz_is_water = TRUE THEN ST_SimplifyPreserveTopology(t.way, 38.22) ELSE NULL END),
    mz_way11 = (CASE WHEN t.way IS NOT NULL AND p.mz_is_landuse = TRUE THEN ST_SimplifyPreserveTopology(t.way, 76.44) ELSE NULL END)

    FROM (
        SELECT osm_id,
               (CASE WHEN mz_calculate_is_landuse("landuse", "leisure", "natural", "highway", "amenity") = TRUE THEN TRUE ELSE NULL END) AS mz_is_landuse,
               (CASE WHEN mz_calculate_is_water("waterway", "natural", "landuse") = TRUE THEN TRUE ELSE NULL END) AS mz_is_water
            FROM planet_osm_polygon
    ) p

    WHERE t.osm_id = p.osm_id;

-- INDEXES
PERFORM mz_create_index_if_not_exists('planet_osm_polygon_wayarea_index', 'planet_osm_polygon', 'way_area');
PERFORM mz_create_partial_index_if_not_exists('planet_osm_polygon_building_index', 'planet_osm_polygon', 'building', 'building IS NOT NULL');
PERFORM mz_create_partial_index_if_not_exists('planet_osm_polygon_admin_level_index', 'planet_osm_polygon', 'admin_level', 'boundary = ''administrative''');
PERFORM mz_create_partial_index_if_not_exists('planet_osm_polygon_mz_is_landuse_index', 'planet_osm_polygon', 'mz_is_landuse', 'mz_is_landuse = TRUE');
PERFORM mz_create_partial_index_if_not_exists('planet_osm_polygon_mz_is_water_index', 'planet_osm_polygon', 'mz_is_water', 'mz_is_water = TRUE');
PERFORM mz_create_partial_index_if_not_exists('planet_osm_polygon_mz_is_building_or_part_index', 'planet_osm_polygon', 'mz_is_building_or_part', 'mz_is_building_or_part = TRUE');

END $$;
