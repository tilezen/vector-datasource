UPDATE planet_osm_polygon
SET mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_polygon.*)
WHERE
  amenity = 'boat_rental' OR
  shop = 'boat_rental' OR
  tags->'rental' = 'boat' OR
  (shop = 'boat' AND tags->'rental' = 'yes');

UPDATE planet_osm_polygon
SET mz_water_min_zoom = mz_calculate_min_zoom_water(planet_osm_polygon.*)
WHERE mz_calculate_min_zoom_water(planet_osm_polygon.*) IS NOT NULL;
