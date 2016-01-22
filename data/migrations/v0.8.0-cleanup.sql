-- old version of the transit routes function - the new version
-- takes a node ID and/or a way ID.
DROP FUNCTION IF EXISTS mz_calculate_transit_routes(BIGINT);
