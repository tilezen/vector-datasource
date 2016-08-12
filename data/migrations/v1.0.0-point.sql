UPDATE
  planet_osm_point
  SET mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_point.*)
  WHERE
    (tags -> 'man_made' IN ('wastewater_plant', 'water_works', 'works') OR
     tags -> 'leisure' IN ('golf_course', 'nature_reserve', 'park', 'pitch') OR
     tags -> 'landuse' IN ('cemetery', 'farm', 'forest', 'military', 'quarry', 'recreation_ground', 'village_green', 'winter_sports', 'wood') OR
     tags -> 'amenity' = 'grave_yard' OR
     tags -> 'boundary' IN ('national_park', 'protected_area') OR
     tags -> 'power' IN ('plant', 'substation') OR
     tags -> 'natural' IN ('wood', 'forest') OR
     tags -> 'public_transport' IN ('stop_position', 'tram_stop', 'stop') OR
     tags -> 'railway' IN ('halt', 'tram_stop', 'stop', 'station'))
    AND COALESCE(mz_poi_min_zoom, 999) <> COALESCE(mz_calculate_min_zoom_pois(planet_osm_point.*), 999);
