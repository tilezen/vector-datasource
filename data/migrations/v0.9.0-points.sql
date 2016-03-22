UPDATE planet_osm_point SET
  mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_point.*)
  WHERE
    "disused" <> 'no'
    OR "railway" IN ('station', 'halt', 'tram_stop', 'platform', 'stop')
    OR "highway" IN ('platform', 'bus_stop')
    OR public_transport IN ('platform', 'stop_area')
    OR tags->'site' = 'stop_area'
    OR "aerialway" = 'station';
