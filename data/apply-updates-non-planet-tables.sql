-- correct the invalid data in the ne tables from reprojection
UPDATE ne_10m_lakes SET the_geom=ST_MakeValid(the_geom) WHERE NOT ST_IsValid(the_geom);
UPDATE ne_110m_land SET the_geom=ST_MakeValid(the_geom) WHERE NOT ST_IsValid(the_geom);

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
CREATE INDEX ne_10m_urban_areas_way_area_index ON ne_10m_urban_areas(way_area);

UPDATE ne_50m_urban_areas SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX ne_50m_urban_areas_way_area_index ON ne_50m_urban_areas(way_area);

UPDATE ne_110m_ocean SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX ne_110m_ocean_wayarea_index ON ne_110m_ocean(way_area);

UPDATE ne_110m_lakes SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX ne_110m_lakes_wayarea_index ON ne_110m_lakes(way_area);

UPDATE ne_50m_ocean SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX ne_50m_ocean_wayarea_index ON ne_50m_ocean(way_area);

UPDATE ne_50m_lakes SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX ne_50m_lakes_wayarea_index ON ne_50m_lakes(way_area);

UPDATE ne_50m_playas SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX ne_50m_playas_wayarea_index ON ne_50m_playas(way_area);

UPDATE ne_10m_ocean SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX ne_10m_ocean_wayarea_index ON ne_10m_ocean(way_area);

UPDATE ne_10m_lakes SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX ne_10m_lakes_wayarea_index ON ne_10m_lakes(way_area);

UPDATE ne_10m_playas SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX ne_10m_playas_wayarea_index ON ne_10m_playas(way_area);

UPDATE water_polygons SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX water_polygons_wayarea_index ON water_polygons(way_area);

UPDATE ne_110m_land SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX ne_110m_land_wayarea_index ON ne_110m_land(way_area);

UPDATE ne_50m_land SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX ne_50m_land_wayarea_index ON ne_50m_land(way_area);

UPDATE ne_10m_land SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX ne_10m_land_way_area_index ON ne_10m_land(way_area);

UPDATE land_polygons SET way_area=ST_Area(the_geom) WHERE the_geom IS NOT NULL;
CREATE INDEX land_polygons_wayarea_index ON land_polygons(way_area);

-- we look up min_label, max_label by wikidata ID.
CREATE INDEX ne_10m_admin_0_countries_wikidata_index ON ne_10m_admin_0_countries(wikidataid);
CREATE INDEX ne_10m_admin_0_map_units_wikidata_index ON ne_10m_admin_0_map_units(wikidataid);
CREATE INDEX ne_10m_admin_1_states_provinces_wikidata_index ON ne_10m_admin_1_states_provinces(wikidataid);
