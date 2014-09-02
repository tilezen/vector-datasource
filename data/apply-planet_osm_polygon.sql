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

    -- tolerances are calculated as follows
    -- [6378137 * 2 * pi / (2 ** (zoom + 8)) for zoom in range(22)]
    -- zoom level  0: 156543.033928
    -- zoom level  1: 78271.516964
    -- zoom level  2: 39135.758482
    -- zoom level  3: 19567.879241
    -- zoom level  4: 9783.9396205
    -- zoom level  5: 4891.96981025
    -- zoom level  6: 2445.98490513
    -- zoom level  7: 1222.99245256
    -- zoom level  8: 611.496226281
    -- zoom level  9: 305.748113141
    -- zoom level 10: 152.87405657
    -- zoom level 11: 76.4370282852
    -- zoom level 12: 38.2185141426
    -- zoom level 13: 19.1092570713
    -- zoom level 14: 9.55462853565
    -- zoom level 15: 4.77731426782
    -- zoom level 16: 2.38865713391
    -- zoom level 17: 1.19432856696
    -- zoom level 18: 0.597164283478
    -- zoom level 19: 0.298582141739
    -- zoom level 20: 0.149291070869
    -- zoom level 21: 0.0746455354347
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
