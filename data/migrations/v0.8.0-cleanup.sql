-- old version of the transit routes function - the new version
-- takes a node ID and/or a way ID.
DROP FUNCTION IF EXISTS mz_calculate_transit_routes(BIGINT);

-- old version of the mz_calculate_poi_level function - new one takes the
-- "emergency" key as well.
DROP FUNCTION IF EXISTS mz_calculate_poi_level(
  text, text, text, text, text, text, text, text, text, text, text, text, text,
  text, text, text, text, hstore, real);
