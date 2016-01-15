UPDATE planet_osm_point SET
  mz_poi_min_zoom = mz_calculate_poi_level("aerialway", "aeroway", "amenity", "barrier", "craft", "highway", "historic", "leisure", "lock", "man_made", "natural", "office", "power", "railway", "shop", "tourism", "waterway", "tags", 0::real)
  WHERE
    "leisure" IN ('sports_centre', 'fitness_centre', 'fitness_station') OR
    "amenity" IN ('gym', 'prison') OR
    "shop" = 'electronics' OR
    "aeroway" = 'gate' OR
    "tourism" IN ('zoo', 'attraction', 'artwork', 'theme_park',
                  'wilderness_hut', 'hanami', 'resort', 'trail_riding_station',
                  'aquarium', 'winery') OR
    "tags"->'zoo' IN ('enclosure', 'petting_zoo', 'aviary', 'wildlife_park') OR
    "tags"->'attraction' IN ('animal', 'water_slide', 'roller_coaster',
                             'summer_toboggan', 'carousel', 'amusement_ride',
                             'maze');
