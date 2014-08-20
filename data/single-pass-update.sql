DO $$
BEGIN

-- add way_area columns to all tables that use it
PERFORM mz_add_area_column('ne_110m_ocean', 'way_area', 'the_geom');
PERFORM mz_add_area_column('ne_110m_lakes', 'way_area', 'the_geom');
PERFORM mz_add_area_column('ne_50m_ocean', 'way_area', 'the_geom');
PERFORM mz_add_area_column('ne_50m_lakes', 'way_area', 'the_geom');
PERFORM mz_add_area_column('ne_50m_playas', 'way_area', 'the_geom');
PERFORM mz_add_area_column('ne_10m_ocean', 'way_area', 'the_geom');
PERFORM mz_add_area_column('ne_10m_lakes', 'way_area', 'the_geom');
PERFORM mz_add_area_column('ne_10m_playas', 'way_area', 'the_geom');
PERFORM mz_add_area_column('water_polygons', 'way_area', 'the_geom');
PERFORM mz_add_area_column('ne_10m_urban_areas', 'way_area', 'the_geom');
PERFORM mz_add_area_column('ne_50m_urban_areas', 'way_area', 'the_geom');
PERFORM mz_add_area_column('ne_10m_parks_and_protected_lands', 'way_area', 'the_geom');

-- water_polygons also has a simplified geometry
PERFORM mz_add_simplified_geometry_column('water_polygons', 'mz_the_geom12', 'the_geom', 'Geometry', 38.22);

--------------------------------------------------------------------------------
-- planet_osm_point
--------------------------------------------------------------------------------

ALTER TABLE planet_osm_point
    ADD COLUMN mz_id TEXT,
    ADD COLUMN mz_poi_level SMALLINT;

UPDATE planet_osm_point SET
    mz_id = mz_normalize_id(osm_id, way),
    mz_poi_level = mz_calculate_poi_level(
        "aerialway",
        "aeroway",
        "amenity",
        "barrier",
        "highway",
        "historic",
        "leisure",
        "lock",
        "man_made",
        "natural",
        "power",
        "railway",
        "shop",
        "tourism",
        "waterway"
    );

--------------------------------------------------------------------------------
-- planet_osm_line
--------------------------------------------------------------------------------

ALTER TABLE planet_osm_line
    ADD COLUMN mz_id TEXT,
    ADD COLUMN mz_road_level SMALLINT,
    ADD COLUMN mz_road_sort_key FLOAT;

UPDATE planet_osm_line AS line SET
    mz_id = mz_normalize_id(road.osm_id, road.way),
    mz_road_level = road.mz_road_level,
    mz_road_sort_key = (CASE WHEN road.mz_road_level IS NULL
        THEN NULL
        ELSE mz_calculate_road_sort_key(road.layer, road.bridge, road.tunnel, road.highway, road.railway)
    END)

    FROM (
        SELECT osm_id, way, layer, bridge, tunnel, highway, railway, mz_calculate_road_level(highway, railway) AS mz_road_level
        FROM planet_osm_line
    ) road

    WHERE line.osm_id = road.osm_id;

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

--------------------------------------------------------------------------------
-- indexes
--------------------------------------------------------------------------------

-- way_area indexes
PERFORM mz_create_index_if_not_exists('ne_110m_ocean_wayarea_index', 'ne_110m_ocean', 'way_area');
PERFORM mz_create_index_if_not_exists('ne_110m_lakes_wayarea_index', 'ne_110m_lakes', 'way_area');
PERFORM mz_create_index_if_not_exists('ne_50m_ocean_wayarea_index', 'ne_50m_ocean', 'way_area');
PERFORM mz_create_index_if_not_exists('ne_50m_lakes_wayarea_index', 'ne_50m_lakes', 'way_area');
PERFORM mz_create_index_if_not_exists('ne_50m_playas_wayarea_index', 'ne_50m_playas', 'way_area');
PERFORM mz_create_index_if_not_exists('ne_50m_urban_areas_way_area_index', 'ne_50m_urban_areas', 'way_area');
PERFORM mz_create_index_if_not_exists('ne_10m_ocean_wayarea_index', 'ne_10m_ocean', 'way_area');
PERFORM mz_create_index_if_not_exists('ne_10m_lakes_wayarea_index', 'ne_10m_lakes', 'way_area');
PERFORM mz_create_index_if_not_exists('ne_10m_playas_wayarea_index', 'ne_10m_playas', 'way_area');
PERFORM mz_create_index_if_not_exists('ne_10m_urban_areas_way_area_index', 'ne_10m_urban_areas', 'way_area');
PERFORM mz_create_index_if_not_exists('ne_10m_parks_and_protected_lands_way_area_index', 'ne_10m_parks_and_protected_lands', 'way_area');
PERFORM mz_create_index_if_not_exists('water_polygons_wayarea_index', 'water_polygons', 'way_area');
PERFORM mz_create_index_if_not_exists('planet_osm_polygon_wayarea_index', 'planet_osm_polygon', 'way_area');

-- indexes for existing columns
PERFORM mz_create_index_if_not_exists('planet_osm_polygon_building_index', 'planet_osm_polygon', 'building');
PERFORM mz_create_partial_index_if_not_exists('planet_osm_polygon_admin_level_index', 'planet_osm_polygon', 'admin_level', 'boundary = ''administrative''');
PERFORM mz_create_partial_index_if_not_exists('planet_osm_point_place', 'planet_osm_point', 'place',
    'name is NOT NULL' );

-- indexes for new columns
PERFORM mz_create_index_if_not_exists('planet_osm_polygon_mz_is_landuse_index', 'planet_osm_polygon', 'mz_is_landuse');
PERFORM mz_create_index_if_not_exists('planet_osm_polygon_mz_is_water_index', 'planet_osm_polygon', 'mz_is_water');
PERFORM mz_create_index_if_not_exists('planet_osm_point_mz_poi_level_index', 'planet_osm_point', 'mz_poi_level');
PERFORM mz_create_index_if_not_exists('planet_osm_polygon_mz_road_level_index', 'planet_osm_line', 'mz_road_level');
PERFORM mz_create_index_if_not_exists('planet_osm_polygon_mz_is_building_or_part_index', 'planet_osm_polygon', 'mz_is_building_or_part');

END $$;
