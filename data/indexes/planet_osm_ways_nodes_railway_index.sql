-- This index is used to improve performance of mz_calculate_transit_routes_and_score
CREATE INDEX
  planet_osm_ways_nodes_railway
  ON planet_osm_ways USING gin(nodes)
  WHERE
    hstore(tags)->'railway' IN ('subway', 'light_rail', 'tram', 'rail');
