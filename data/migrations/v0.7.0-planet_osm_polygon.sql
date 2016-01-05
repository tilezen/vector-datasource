UPDATE planet_osm_polygon SET
  mz_poi_min_zoom = mz_calculate_poi_level("aerialway", "aeroway", "amenity", "barrier", "craft", "highway", "historic", "leisure", "lock", "man_made", "natural", "office", "power", "railway", "tags"->'rental', "shop", "tourism", "waterway", way_area),
  mz_is_landuse = TRUE,
  mz_landuse_min_zoom = mz_calculate_landuse_min_zoom("landuse", "leisure", "natural", "highway", "amenity", "aeroway", "tourism", "man_made", "power", "boundary", way_area)
  WHERE amenity='prison';
