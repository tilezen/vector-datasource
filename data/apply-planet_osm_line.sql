DO $$
BEGIN

--------------------------------------------------------------------------------
-- planet_osm_line
--------------------------------------------------------------------------------

CREATE INDEX planet_osm_line_waterway_index ON planet_osm_line(waterway) WHERE waterway IS NOT NULL;
CREATE INDEX planet_osm_line_admin_boundaries_index ON planet_osm_line(boundary) WHERE boundary='administrative';
CREATE INDEX planet_osm_line_road_level_index ON planet_osm_line(mz_calculate_road_level(highway, railway, aeroway)) WHERE mz_calculate_road_level(highway, railway, aeroway) IS NOT NULL;
CREATE INDEX planet_osm_line_transit_level_index ON planet_osm_line(mz_calculate_transit_level(route)) WHERE mz_calculate_transit_level(route) IS NOT NULL;

END $$;
