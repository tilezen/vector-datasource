UPDATE
  planet_osm_polygon
  SET mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_polygon.*)
  WHERE
     man_made IN ('wastewater_plant', 'water_works', 'works') OR
     leisure IN ('golf_course', 'nature_reserve', 'park', 'pitch') OR
     amenity = 'grave_yard' OR
     landuse IN ('cemetery', 'farm', 'forest', 'military', 'quarry', 'recreation_ground', 'village_green', 'winter_sports') OR
     boundary IN ('national_park', 'protected_area') OR
     power IN ('plant', 'substation') OR
     "natural" IN ('wood'))
    AND COALESCE(mz_poi_min_zoom, 999) <> COALESCE(mz_calculate_min_zoom_pois(planet_osm_polygon.*), 999);

UPDATE
  planet_osm_polygon
  SET mz_landuse_min_zoom = mz_calculate_min_zoom_landuse(planet_osm_polygon.*)
  WHERE
    (man_made IN ('wastewater_plant', 'water_works', 'works') OR
     leisure IN ('golf_course', 'nature_reserve', 'park', 'pitch') OR
     "natural" IN ('forest', 'park', 'wood') OR
     amenity = 'grave_yard' OR
     landuse IN ('cemetery', 'farm', 'forest', 'military', 'quarry', 'recreation_ground', 'village_green', 'winter_sports') OR
     boundary IN ('national_park', 'protected_area') OR
     power IN ('plant', 'substation'))
    AND COALESCE(mz_landuse_min_zoom, 999) <> COALESCE(mz_calculate_min_zoom_landuse(planet_osm_polygon.*), 999);
