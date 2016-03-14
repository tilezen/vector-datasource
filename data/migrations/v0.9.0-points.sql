UPDATE planet_osm_point SET
  mz_poi_min_zoom = mz_calculate_poi_level("aerialway", "aeroway", "amenity",
    "barrier", "craft", "disused", "emergency", "highway", "historic",
    "leisure", "lock", "man_made", "natural", "office", "power", "railway",
    "shop", "tourism", "waterway", "tags", 0::real)
  WHERE
    "disused" <> 'no' OR
    "railway" = 'station';
