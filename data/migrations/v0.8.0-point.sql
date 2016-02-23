UPDATE planet_osm_point SET
  mz_poi_min_zoom = mz_calculate_poi_level("aerialway", "aeroway", "amenity",
    "barrier", "craft", "emergency", "highway", "historic", "leisure", "lock",
    "man_made", "natural", "office", "power", "railway", "shop", "tourism",
    "waterway", "tags", 0::real)
  WHERE
    "emergency" = 'phone' OR
    "amenity" IN ('social_facility', 'clinic', 'doctors', 'dentist',
      'kindergarten', 'childcare', 'toilets') OR
    "tags"->'healthcare' = 'midwife';
