UPDATE
  planet_osm_polygon
  SET mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_polygon.*)
  WHERE
    (tags -> 'man_made' IN ('wastewater_plant', 'water_works', 'works') OR
     tags -> 'leisure' IN ('golf_course', 'nature_reserve', 'park', 'pitch') OR
     tags -> 'amenity' = 'grave_yard' OR
     tags -> 'landuse' IN ('cemetery', 'farm', 'forest', 'military', 'quarry', 'recreation_ground', 'village_green', 'winter_sports') OR
     tags -> 'boundary' IN ('national_park', 'protected_area') OR
     tags -> 'power' IN ('plant', 'substation') OR
     tags -> 'natural' IN ('wood'))
    AND COALESCE(mz_poi_min_zoom, 999) <> COALESCE(mz_calculate_min_zoom_pois(planet_osm_polygon.*), 999);

UPDATE
  planet_osm_polygon
  SET mz_landuse_min_zoom = mz_calculate_min_zoom_landuse(planet_osm_polygon.*)
  WHERE
    (tags -> 'man_made' IN ('wastewater_plant', 'water_works', 'works') OR
     tags -> 'leisure' IN ('golf_course', 'nature_reserve', 'park', 'pitch') OR
     tags -> 'natural' IN ('forest', 'park', 'wood') OR
     tags -> 'amenity' = 'grave_yard' OR
     tags -> 'landuse' IN ('cemetery', 'farm', 'forest', 'military', 'quarry', 'recreation_ground', 'village_green', 'winter_sports') OR
     tags -> 'boundary' IN ('national_park', 'protected_area') OR
     tags -> 'power' IN ('plant', 'substation'))
    AND COALESCE(mz_landuse_min_zoom, 999) <> COALESCE(mz_calculate_min_zoom_landuse(planet_osm_polygon.*), 999);
