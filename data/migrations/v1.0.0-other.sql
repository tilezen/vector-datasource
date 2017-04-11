UPDATE water_polygons SET mz_label_placement = ST_PointOnSurface(the_geom) WHERE mz_label_placement IS NULL;
UPDATE land_polygons SET mz_label_placement = ST_PointOnSurface(the_geom) WHERE mz_label_placement IS NULL;
UPDATE ne_110m_ocean SET mz_label_placement = ST_PointOnSurface(the_geom) WHERE mz_label_placement IS NULL;
UPDATE ne_50m_ocean SET mz_label_placement = ST_PointOnSurface(the_geom) WHERE mz_label_placement IS NULL;
UPDATE ne_10m_ocean SET mz_label_placement = ST_PointOnSurface(the_geom) WHERE mz_label_placement IS NULL;
UPDATE ne_110m_lakes SET mz_label_placement = ST_PointOnSurface(the_geom) WHERE mz_label_placement IS NULL;
UPDATE ne_50m_lakes SET mz_label_placement = ST_PointOnSurface(the_geom) WHERE mz_label_placement IS NULL;
UPDATE ne_10m_lakes SET mz_label_placement = ST_PointOnSurface(the_geom) WHERE mz_label_placement IS NULL;
UPDATE ne_50m_playas SET mz_label_placement = ST_PointOnSurface(the_geom) WHERE mz_label_placement IS NULL;
UPDATE ne_10m_playas SET mz_label_placement = ST_PointOnSurface(the_geom) WHERE mz_label_placement IS NULL;
UPDATE ne_110m_land SET mz_label_placement = ST_PointOnSurface(the_geom) WHERE mz_label_placement IS NULL;
UPDATE ne_50m_land SET mz_label_placement = ST_PointOnSurface(the_geom) WHERE mz_label_placement IS NULL;
UPDATE ne_10m_land SET mz_label_placement = ST_PointOnSurface(the_geom) WHERE mz_label_placement IS NULL;
UPDATE ne_50m_urban_areas SET mz_label_placement = ST_PointOnSurface(the_geom) WHERE mz_label_placement IS NULL;
UPDATE ne_10m_urban_areas SET mz_label_placement = ST_PointOnSurface(the_geom) WHERE mz_label_placement IS NULL;

UPDATE ne_110m_admin_0_boundary_lines_land
  SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(ne_110m_admin_0_boundary_lines_land.*);

UPDATE ne_50m_admin_0_boundary_lines_land
  SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(ne_50m_admin_0_boundary_lines_land.*);

UPDATE ne_50m_admin_1_states_provinces_lines
  SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(ne_50m_admin_1_states_provinces_lines.*);

UPDATE ne_10m_admin_0_boundary_lines_land
  SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(ne_10m_admin_0_boundary_lines_land.*);

UPDATE ne_10m_admin_0_boundary_lines_map_units
  SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(ne_10m_admin_0_boundary_lines_map_units.*);

UPDATE ne_10m_admin_1_states_provinces_lines
  SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(ne_10m_admin_1_states_provinces_lines.*);
