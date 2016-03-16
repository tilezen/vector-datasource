UPDATE planet_osm_point SET
  mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_point.*)
  WHERE
    "disused" <> 'no' OR
    "railway" = 'station';
