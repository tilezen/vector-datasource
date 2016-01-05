UPDATE planet_osm_polygon SET
  mz_poi_min_zoom = mz_calculate_poi_level("aerialway", "aeroway", "amenity", "barrier", "craft", "highway", "historic", "leisure", "lock", "man_made", "natural", "office", "power", "railway", "tags"->'rental', "shop", "tourism", "waterway", way_area)
  WHERE
    "leisure" IN ('sports_centre', 'fitness_centre', 'fitness_station') OR
    "amenity" = 'gym';
