UPDATE planet_osm_point
  SET mz_poi_min_zoom = mz_calculate_poi_level("aerialway", "aeroway", "amenity", "barrier", "craft", "highway", "historic", "leisure", "lock", "man_made", "natural", "office", "power", "railway", "tags"->'rental', "shop", "tourism", "waterway", 0::real)
WHERE railway = 'station'
   OR shop IN ('toys', 'ski', 'alcohol', 'wine', 'ice_cream')
   OR "natural" = 'beach'
   OR tags->'rental' = 'ski'
   OR amenity IN ('ski_rental', 'ski_school', 'ice_cream')
   OR man_made = 'snow_cannon'
   OR highway = 'motorway_junction'
   OR tourism = 'zoo';
