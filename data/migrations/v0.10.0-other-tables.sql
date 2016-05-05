UPDATE ne_110m_land
  SET mz_earth_min_zoom = mz_calculate_min_zoom_earth(ne_110m_land.*)
  WHERE mz_calculate_min_zoom_earth(ne_110m_land.*) IS NOT NULL;

UPDATE ne_50m_land
  SET mz_earth_min_zoom = mz_calculate_min_zoom_earth(ne_50m_land.*)
  WHERE mz_calculate_min_zoom_earth(ne_50m_land.*) IS NOT NULL;

UPDATE ne_10m_land
  SET mz_earth_min_zoom = mz_calculate_min_zoom_earth(ne_10m_land.*)
  WHERE mz_calculate_min_zoom_earth(ne_10m_land.*) IS NOT NULL;

UPDATE land_polygons
  SET mz_earth_min_zoom = mz_calculate_min_zoom_earth(land_polygons.*)
  WHERE mz_calculate_min_zoom_earth(land_polygons.*) IS NOT NULL;

UPDATE ne_10m_ocean SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_10m_ocean.*);
UPDATE ne_50m_ocean SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_50m_ocean.*);
UPDATE ne_110m_ocean SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_110m_ocean.*);

UPDATE ne_10m_coastline SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_10m_coastline.*);
UPDATE ne_50m_coastline SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_50m_coastline.*);
UPDATE ne_110m_coastline SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_110m_coastline.*);

UPDATE ne_10m_lakes SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_10m_lakes.*);
UPDATE ne_50m_lakes SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_50m_lakes.*);
UPDATE ne_110m_lakes SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_110m_lakes.*);

UPDATE ne_10m_playas SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_10m_playas.*);
UPDATE ne_50m_playas SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_50m_playas.*);

UPDATE water_polygons SET mz_water_min_zoom = mz_calculate_min_zoom_water(water_polygons.*);

UPDATE ne_110m_admin_0_boundary_lines_land SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(ne_110m_admin_0_boundary_lines_land.*);
UPDATE ne_50m_admin_0_boundary_lines_land SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(ne_50m_admin_0_boundary_lines_land.*);
UPDATE ne_50m_admin_1_states_provinces_lines SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(ne_50m_admin_1_states_provinces_lines.*);
UPDATE ne_10m_admin_0_boundary_lines_land SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(ne_10m_admin_0_boundary_lines_land.*);
UPDATE ne_10m_admin_1_states_provinces_lines SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(ne_10m_admin_1_states_provinces_lines.*);

UPDATE ne_10m_populated_places SET mz_places_min_zoom = mz_calculate_min_zoom_places(ne_10m_populated_places.*);
