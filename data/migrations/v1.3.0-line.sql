UPDATE planet_osm_line
  SET mz_road_level = mz_calculate_min_zoom_roads(planet_osm_line.*)
  WHERE
      (tags -> 'highway' IN ( 'secondary', 'motorway_link', 'tertiary', 'trunk_link',
                   'primary_link', 'secondary_link', 'tertiary_link',
                   'residential', 'unclassified', 'road', 'living_street', 'pedestrian',
                   'path', 'track', 'cycleway', 'bridleway', 'footway', 'steps',
                   'service' ) OR
       tags -> 'whitewater' = 'portage_way')
      AND mz_calculate_min_zoom_roads(planet_osm_line.*) IS NOT NULL
      AND mz_road_level IS NOT NULL
      AND mz_road_level <> mz_calculate_min_zoom_roads(planet_osm_line.*);
