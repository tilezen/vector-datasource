UPDATE planet_osm_line
  SET mz_road_level = mz_calculate_min_zoom_roads(planet_osm_line.*)
  WHERE
    highway IN ('raceway', 'corridor') AND
    COALESCE(mz_road_level, 999) <> COALESCE(mz_calculate_min_zoom_roads(planet_osm_line.*), 999);

UPDATE
  planet_osm_line
  SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(planet_osm_line.*)
  WHERE
    (barrier IN ('city_wall', 'retaining_wall', 'fence') OR
     historic = 'citywalls' OR
     man_made = 'snow_fence' OR
     waterway = 'dam' OR
     boundary = 'aboriginal_lands' OR
     tags->'boundary:type' = 'aboriginal_lands')
    AND COALESCE(mz_boundary_min_zoom, 999) <> COALESCE(mz_calculate_min_zoom_boundaries(planet_osm_line.*), 999);

UPDATE
  planet_osm_line
  SET mz_landuse_min_zoom = mz_calculate_min_zoom_landuse(planet_osm_line.*)
  WHERE
     (barrier IN ('city_wall', 'retaining_wall', 'fence') OR
     historic = 'citywalls' OR
     man_made = 'snow_fence' OR
     waterway = 'dam')
    AND COALESCE(mz_landuse_min_zoom, 999) <> COALESCE(mz_calculate_min_zoom_landuse(planet_osm_line.*), 999);
