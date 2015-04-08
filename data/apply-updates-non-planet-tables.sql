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

END $$;
