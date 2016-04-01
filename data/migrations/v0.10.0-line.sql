UPDATE planet_osm_line
SET mz_water_min_zoom = mz_calculate_min_zoom_water(planet_osm_line.*)
WHERE mz_calculate_min_zoom_water(planet_osm_line.*) IS NOT NULL;
