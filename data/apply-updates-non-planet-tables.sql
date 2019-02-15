-- correct the invalid data in the ne tables from reprojection
UPDATE ne_10m_lakes SET the_geom=ST_MakeValid(the_geom) WHERE NOT ST_IsValid(the_geom);
UPDATE ne_110m_land SET the_geom=ST_MakeValid(the_geom) WHERE NOT ST_IsValid(the_geom);
UPDATE ne_10m_ocean SET the_geom=ST_MakeValid(the_geom) WHERE NOT ST_IsValid(the_geom);

UPDATE ne_10m_admin_0_boundary_lines_land
  SET
    the_geom = (CASE WHEN GeometryType(ST_MakeValid(the_geom)) = 'MULTILINESTRING'
                          THEN ST_MakeValid(the_geom)
                     ELSE the_geom END)
  WHERE NOT ST_IsValid(the_geom);
DELETE FROM ne_10m_admin_0_boundary_lines_land WHERE NOT ST_IsValid(the_geom);

UPDATE ne_10m_admin_0_boundary_lines_map_units
  SET
    the_geom = (CASE WHEN GeometryType(ST_MakeValid(the_geom)) = 'MULTILINESTRING'
                          THEN ST_MakeValid(the_geom)
                     ELSE the_geom END)
  WHERE NOT ST_IsValid(the_geom);
DELETE FROM ne_10m_admin_0_boundary_lines_map_units WHERE NOT ST_IsValid(the_geom);

UPDATE ne_10m_admin_0_boundary_lines_disputed_areas
  SET
    the_geom = (CASE WHEN GeometryType(ST_MakeValid(the_geom)) = 'MULTILINESTRING'
                          THEN ST_MakeValid(the_geom)
                     ELSE the_geom END)
  WHERE NOT ST_IsValid(the_geom);
DELETE FROM ne_10m_admin_0_boundary_lines_disputed_areas WHERE NOT ST_IsValid(the_geom);

UPDATE ne_10m_admin_1_states_provinces_lines
  SET
    the_geom = (CASE WHEN GeometryType(ST_MakeValid(the_geom)) = 'MULTILINESTRING'
                          THEN ST_MakeValid(the_geom)
                     ELSE the_geom END)
  WHERE NOT ST_IsValid(the_geom);
DELETE FROM ne_10m_admin_1_states_provinces_lines WHERE NOT ST_IsValid(the_geom);

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

UPDATE ne_110m_ocean
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_110m_ocean.*)
  WHERE mz_calculate_min_zoom_water(ne_110m_ocean.*) IS NOT NULL;

UPDATE ne_50m_ocean
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_50m_ocean.*)
  WHERE mz_calculate_min_zoom_water(ne_50m_ocean.*) IS NOT NULL;

UPDATE ne_10m_ocean
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_10m_ocean.*)
  WHERE mz_calculate_min_zoom_water(ne_10m_ocean.*) IS NOT NULL;

UPDATE ne_110m_lakes
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_110m_lakes.*)
  WHERE mz_calculate_min_zoom_water(ne_110m_lakes.*) IS NOT NULL;

UPDATE ne_50m_lakes
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_50m_lakes.*)
  WHERE mz_calculate_min_zoom_water(ne_50m_lakes.*) IS NOT NULL;

UPDATE ne_10m_lakes
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_10m_lakes.*)
  WHERE mz_calculate_min_zoom_water(ne_10m_lakes.*) IS NOT NULL;

UPDATE ne_110m_coastline
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_110m_coastline.*)
  WHERE mz_calculate_min_zoom_water(ne_110m_coastline.*) IS NOT NULL;

UPDATE ne_50m_coastline
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_50m_coastline.*)
  WHERE mz_calculate_min_zoom_water(ne_50m_coastline.*) IS NOT NULL;

UPDATE ne_10m_coastline
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_10m_coastline.*)
  WHERE mz_calculate_min_zoom_water(ne_10m_coastline.*) IS NOT NULL;

UPDATE ne_50m_playas
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_50m_playas.*)
  WHERE mz_calculate_min_zoom_water(ne_50m_playas.*) IS NOT NULL;

UPDATE ne_10m_playas
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_10m_playas.*)
  WHERE mz_calculate_min_zoom_water(ne_10m_playas.*) IS NOT NULL;

UPDATE water_polygons
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(water_polygons.*)
  WHERE mz_calculate_min_zoom_water(water_polygons.*) IS NOT NULL;

UPDATE ne_110m_admin_0_boundary_lines_land
  SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(ne_110m_admin_0_boundary_lines_land.*)
  WHERE mz_calculate_min_zoom_boundaries(ne_110m_admin_0_boundary_lines_land.*) IS NOT NULL;

UPDATE ne_50m_admin_0_boundary_lines_land
  SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(ne_50m_admin_0_boundary_lines_land.*)
  WHERE mz_calculate_min_zoom_boundaries(ne_50m_admin_0_boundary_lines_land.*) IS NOT NULL;

UPDATE ne_50m_admin_1_states_provinces_lines
  SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(ne_50m_admin_1_states_provinces_lines.*)
  WHERE mz_calculate_min_zoom_boundaries(ne_50m_admin_1_states_provinces_lines.*) IS NOT NULL;

UPDATE ne_10m_admin_0_boundary_lines_land
  SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(ne_10m_admin_0_boundary_lines_land.*)
  WHERE mz_calculate_min_zoom_boundaries(ne_10m_admin_0_boundary_lines_land.*) IS NOT NULL;

UPDATE ne_10m_admin_0_boundary_lines_map_units
  SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(ne_10m_admin_0_boundary_lines_map_units.*)
  WHERE mz_calculate_min_zoom_boundaries(ne_10m_admin_0_boundary_lines_map_units.*) IS NOT NULL;

UPDATE ne_10m_admin_0_boundary_lines_disputed_areas
  SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(ne_10m_admin_0_boundary_lines_disputed_areas.*)
  WHERE mz_calculate_min_zoom_boundaries(ne_10m_admin_0_boundary_lines_disputed_areas.*) IS NOT NULL;

UPDATE ne_10m_admin_1_states_provinces_lines
  SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(ne_10m_admin_1_states_provinces_lines.*)
  WHERE mz_calculate_min_zoom_boundaries(ne_10m_admin_1_states_provinces_lines.*) IS NOT NULL;

UPDATE ne_10m_populated_places
  SET mz_places_min_zoom = mz_calculate_min_zoom_places(ne_10m_populated_places.*)
  WHERE mz_calculate_min_zoom_places(ne_10m_populated_places.*) IS NOT NULL;

UPDATE ne_50m_urban_areas
  SET mz_landuse_min_zoom = mz_calculate_min_zoom_landuse(ne_50m_urban_areas.*)
  WHERE mz_calculate_min_zoom_landuse(ne_50m_urban_areas.*) IS NOT NULL;

UPDATE ne_10m_urban_areas
  SET mz_landuse_min_zoom = mz_calculate_min_zoom_landuse(ne_10m_urban_areas.*)
  WHERE mz_calculate_min_zoom_landuse(ne_10m_urban_areas.*) IS NOT NULL;

UPDATE water_polygons SET mz_label_placement = ST_PointOnSurface(the_geom);
UPDATE land_polygons SET mz_label_placement = ST_PointOnSurface(the_geom);
UPDATE ne_110m_ocean SET mz_label_placement = ST_PointOnSurface(the_geom);
UPDATE ne_50m_ocean SET mz_label_placement = ST_PointOnSurface(the_geom);
UPDATE ne_10m_ocean SET mz_label_placement = ST_PointOnSurface(the_geom);
UPDATE ne_110m_lakes SET mz_label_placement = ST_PointOnSurface(the_geom);
UPDATE ne_50m_lakes SET mz_label_placement = ST_PointOnSurface(the_geom);
UPDATE ne_10m_lakes SET mz_label_placement = ST_PointOnSurface(the_geom);
UPDATE ne_50m_playas SET mz_label_placement = ST_PointOnSurface(the_geom);
UPDATE ne_10m_playas SET mz_label_placement = ST_PointOnSurface(the_geom);
UPDATE ne_110m_land SET mz_label_placement = ST_PointOnSurface(the_geom);
UPDATE ne_50m_land SET mz_label_placement = ST_PointOnSurface(the_geom);
UPDATE ne_10m_land SET mz_label_placement = ST_PointOnSurface(the_geom);
UPDATE ne_50m_urban_areas SET mz_label_placement = ST_PointOnSurface(the_geom);
UPDATE ne_10m_urban_areas SET mz_label_placement = ST_PointOnSurface(the_geom);

UPDATE ne_10m_urban_areas SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
UPDATE ne_50m_urban_areas SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
UPDATE ne_110m_ocean SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
UPDATE ne_110m_lakes SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
UPDATE ne_50m_ocean SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
UPDATE ne_50m_lakes SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
UPDATE ne_50m_playas SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
UPDATE ne_10m_ocean SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
UPDATE ne_10m_lakes SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
UPDATE ne_10m_playas SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
UPDATE water_polygons SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
UPDATE ne_110m_land SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
UPDATE ne_50m_land SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
UPDATE ne_10m_land SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
UPDATE land_polygons SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
