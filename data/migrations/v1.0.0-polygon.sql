UPDATE
  planet_osm_polygon
  SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(planet_osm_polygon.*)
  WHERE
    (barrier IN ('city_wall', 'retaining_wall', 'fence') OR
     historic = 'citywalls' OR
     man_made = 'snow_fence' OR
     waterway = 'dam' OR
     boundary = 'aboriginal_lands' OR
     tags->'boundary:type' = 'aboriginal_lands')
    AND COALESCE(mz_boundary_min_zoom, 999) <> COALESCE(mz_calculate_min_zoom_boundaries(planet_osm_polygon.*), 999);

UPDATE
  planet_osm_polygon
  SET mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_polygon.*)
  WHERE
    (barrier = 'toll_booth' OR
     highway IN ('services', 'rest_area') OR
     tourism = 'camp_site' OR
     man_made = 'windmill' OR
     man_made = 'lighthouse' OR
     leisure = 'garden')
    AND COALESCE(mz_poi_min_zoom, 999) <> COALESCE(mz_calculate_min_zoom_pois(planet_osm_polygon.*), 999);

UPDATE
  planet_osm_polygon
  SET mz_landuse_min_zoom = mz_calculate_min_zoom_landuse(planet_osm_polygon.*)
  WHERE
    (highway IN  ('services', 'rest_area') OR
     barrier IN ('city_wall', 'retaining_wall', 'fence') OR
     historic = 'citywalls' OR
     man_made = 'snow_fence' OR
     waterway = 'dam' OR
     tourism = 'camp_site' OR
     leisure = 'garden' OR
     "natural" IN ('forest', 'park'))
    AND COALESCE(mz_landuse_min_zoom, 999) <> COALESCE(mz_calculate_min_zoom_landuse(planet_osm_polygon.*), 999);

UPDATE
  planet_osm_polygon
  SET mz_building_min_zoom = mz_calculate_min_zoom_buildings(planet_osm_polygon.*)
  WHERE
    tags->'location' = 'underground'
    AND COALESCE(mz_building_min_zoom, 999) <> COALESCE(mz_calculate_min_zoom_buildings(planet_osm_polygon.*), 999);
