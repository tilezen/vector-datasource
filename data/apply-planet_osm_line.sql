DO $$
BEGIN

--------------------------------------------------------------------------------
-- planet_osm_line
--------------------------------------------------------------------------------

-- indexes on existing columns
PERFORM mz_create_partial_index_if_not_exists('planet_osm_line_waterway', 'planet_osm_line', 'waterway', 'waterway IS NOT NULL');

-- indexes on functions
CREATE INDEX planet_osm_line_road_level_index ON planet_osm_line(mz_calculate_road_level(highway, railway, aeroway)) WHERE mz_calculate_road_level(highway, railway, aeroway) IS NOT NULL;
CREATE INDEX planet_osm_line_admin_boundaries_index ON planet_osm_line(boundary) WHERE boundary='administrative';
CREATE INDEX planet_osm_line_road_level_index ON planet_osm_line(mz_calculate_road_level(highway, railway, aeroway, tags->'network')) WHERE mz_calculate_road_level(highway, railway, aeroway, tags->'network') IS NOT NULL;

END $$;
