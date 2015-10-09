DO $$
BEGIN

--------------------------------------------------------------------------------
-- planet_osm_line
--------------------------------------------------------------------------------

CREATE INDEX planet_osm_line_waterway_index ON planet_osm_line(waterway) WHERE waterway IS NOT NULL;
CREATE INDEX planet_osm_line_admin_boundaries_index ON planet_osm_line(boundary) WHERE boundary='administrative';
CREATE INDEX planet_osm_line_road_level_index ON planet_osm_line(mz_calculate_road_level(highway, railway, aeroway, route, way)) WHERE mz_calculate_road_level(highway, railway, aeroway, route, way) IS NOT NULL;
CREATE INDEX planet_osm_line_transit_level_index ON planet_osm_line(mz_calculate_transit_level(route)) WHERE mz_calculate_transit_level(route) IS NOT NULL;

CREATE INDEX planet_osm_line_roads_geom_9_index ON planet_osm_line USING gist(way) WHERE (osm_id > 0 OR route = 'ferry') AND mz_calculate_road_level(highway, railway, aeroway, route, way) <= 9;
CREATE INDEX planet_osm_line_roads_geom_12_index ON planet_osm_line USING gist(way) WHERE (osm_id > 0 OR route = 'ferry') AND mz_calculate_road_level(highway, railway, aeroway, route, way) <= 12;
CREATE INDEX planet_osm_line_roads_geom_15_index ON planet_osm_line USING gist(way) WHERE (osm_id > 0 OR route = 'ferry') AND mz_calculate_road_level(highway, railway, aeroway, route, way) <= 15;

CREATE INDEX planet_osm_line_waterway_geom_index ON planet_osm_line USING gist(way) WHERE waterway IN ('canal', 'river', 'stream', 'dam', 'ditch', 'drain');

CREATE INDEX planet_osm_line_transit_geom_9_index ON planet_osm_line USING gist(way) WHERE mz_calculate_transit_level(route) <= 9;
CREATE INDEX planet_osm_line_transit_geom_12_index ON planet_osm_line USING gist(way) WHERE mz_calculate_transit_level(route) <= 12;
CREATE INDEX planet_osm_line_transit_geom_15_index ON planet_osm_line USING gist(way) WHERE mz_calculate_transit_level(route) <= 15;

END $$;

ANALYZE planet_osm_line;
