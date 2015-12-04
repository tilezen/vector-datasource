DO $$
BEGIN

--------------------------------------------------------------------------------
-- planet_osm_line
--------------------------------------------------------------------------------

ALTER TABLE planet_osm_line ADD COLUMN mz_road_level SMALLINT;
ALTER TABLE planet_osm_line ADD COLUMN mz_transit_level SMALLINT;

UPDATE planet_osm_line
  SET mz_road_level = mz_calculate_road_level(highway, railway, aeroway, route, service, aerialway, tags->'piste:type', way)
  WHERE mz_calculate_road_level(highway, railway, aeroway, route, service, aerialway, tags->'piste:type', way) IS NOT NULL;

UPDATE planet_osm_line
  SET mz_transit_level = mz_calculate_transit_level(route)
  WHERE mz_calculate_transit_level(route) IS NOT NULL;

CREATE INDEX planet_osm_line_waterway_index ON planet_osm_line(waterway) WHERE waterway IS NOT NULL;
CREATE INDEX planet_osm_line_road_level_index ON planet_osm_line(mz_road_level) WHERE mz_road_level IS NOT NULL;
CREATE INDEX planet_osm_line_transit_level_index ON planet_osm_line(mz_transit_level) WHERE mz_transit_level IS NOT NULL;

CREATE INDEX planet_osm_line_roads_geom_index ON planet_osm_line USING gist(way) WHERE (osm_id > 0 OR route = 'ferry') AND mz_road_level IS NOT NULL;
CREATE INDEX planet_osm_line_roads_geom_9_index ON planet_osm_line USING gist(way) WHERE (osm_id > 0 OR route = 'ferry') AND mz_road_level <= 9;
CREATE INDEX planet_osm_line_roads_geom_12_index ON planet_osm_line USING gist(way) WHERE (osm_id > 0 OR route = 'ferry') AND mz_road_level <= 12;
CREATE INDEX planet_osm_line_roads_geom_15_index ON planet_osm_line USING gist(way) WHERE (osm_id > 0 OR route = 'ferry') AND mz_road_level <= 15;

CREATE INDEX planet_osm_line_transit_geom_index ON planet_osm_line USING gist(way) WHERE mz_transit_level IS NOT NULL;
CREATE INDEX planet_osm_line_transit_geom_6_index ON planet_osm_line USING gist(way) WHERE mz_transit_level <= 6;
CREATE INDEX planet_osm_line_transit_geom_9_index ON planet_osm_line USING gist(way) WHERE mz_transit_level <= 9;
CREATE INDEX planet_osm_line_transit_geom_12_index ON planet_osm_line USING gist(way) WHERE mz_transit_level <= 12;
CREATE INDEX planet_osm_line_transit_geom_15_index ON planet_osm_line USING gist(way) WHERE mz_transit_level <= 15;

CREATE INDEX planet_osm_line_waterway_geom_index ON planet_osm_line USING gist(way) WHERE waterway IN ('canal', 'river', 'stream', 'dam', 'ditch', 'drain');

END $$;

ANALYZE planet_osm_line;
