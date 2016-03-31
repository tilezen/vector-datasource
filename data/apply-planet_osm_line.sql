DO $$
BEGIN

--------------------------------------------------------------------------------
-- planet_osm_line
--------------------------------------------------------------------------------

UPDATE planet_osm_line
  SET mz_road_level = mz_calculate_road_level(highway, railway, aeroway, route, service, aerialway, leisure, sport, man_made, way)
  WHERE mz_calculate_road_level(highway, railway, aeroway, route, service, aerialway, leisure, sport, man_made, way) IS NOT NULL;

UPDATE planet_osm_line
  SET mz_transit_level = mz_calculate_min_zoom_transit(planet_osm_line.*)
  WHERE mz_calculate_min_zoom_transit(planet_osm_line.*) IS NOT NULL;

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

CREATE INDEX planet_osm_line_piste_geom_index ON planet_osm_line USING gist(way) WHERE tags ? 'piste:type';

CREATE INDEX planet_osm_line_railway_platform_index ON planet_osm_line USING gist(way) WHERE railway='platform';

END $$;

ANALYZE planet_osm_line;
