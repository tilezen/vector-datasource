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

-- additional updates
PERFORM mz_create_index_if_not_exists('ne_10m_populated_places_scalerank_index', 'ne_10m_populated_places', 'scalerank');

PERFORM AddGeometryColumn('ne_50m_urban_areas', 'mz_centroid', 900913, 'Geometry', 2);
UPDATE ne_50m_urban_areas SET mz_centroid=ST_Centroid(the_geom);
CREATE INDEX ne_50m_urban_areas_centroid_index ON ne_50m_urban_areas USING gist(mz_centroid);

PERFORM AddGeometryColumn('ne_10m_parks_and_protected_lands', 'mz_centroid', 900913, 'Geometry', 2);
UPDATE ne_10m_parks_and_protected_lands SET mz_centroid=ST_Centroid(the_geom);
CREATE INDEX ne_10m_parks_and_protected_lands_centroid_index ON ne_10m_parks_and_protected_lands USING gist(mz_centroid);

PERFORM AddGeometryColumn('ne_10m_urban_areas', 'mz_centroid', 900913, 'Geometry', 2);
UPDATE ne_10m_urban_areas SET mz_centroid=ST_Centroid(the_geom);
CREATE INDEX ne_10m_urban_areas_centroid_index ON ne_10m_urban_areas USING gist(mz_centroid);

END $$;
