-- This index is used to improve performance of mz_calculate_transit_routes_and_score
CREATE INDEX
  planet_osm_rels_parts_interesting_transit_relation
  ON planet_osm_rels USING gin(parts)
  WHERE
    mz_is_interesting_transit_relation(hstore(tags));
