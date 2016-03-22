UPDATE planet_osm_line
  SET mz_road_level = mz_calculate_road_level(highway, railway, aeroway, route,
    service, aerialway, leisure, sport, man_made, way)
  WHERE
    railway IN ('subway', 'funicular');

UPDATE planet_osm_line
  SET mz_transit_level = mz_calculate_min_zoom_transit(planet_osm_line.*)
  WHERE
    route IN ('railway', 'subway', 'light_rail', 'tram', 'funicular', 'monorail', 'train')
    OR railway IN ('halt', 'stop', 'tram_stop', 'platform', 'station')
    OR public_transport IN ('platform', 'stop_area')
    OR highway IN ('platform', 'bus_stop')
    OR tags->'site' = 'stop_area';
