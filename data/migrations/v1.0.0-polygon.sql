UPDATE
  planet_osm_polygon
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(planet_osm_polygon.*)
  WHERE
    tags -> 'place' = 'sea'
    AND COALESCE(mz_water_min_zoom, 999) <> COALESCE(mz_calculate_min_zoom_water(planet_osm_polygon.*), 999);
