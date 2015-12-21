UPDATE planet_osm_point SET
  mz_poi_min_zoom = mz_calculate_poi_level("aerialway", "aeroway", "amenity", "barrier", "craft", "highway", "historic", "leisure", "lock", "man_made", "natural", "office", "power", "railway", "tags"->'rental', "shop", "tourism", "waterway", 0::real)
  WHERE shop='electronics';
