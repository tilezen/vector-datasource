UPDATE planet_osm_line
  SET mz_road_level = mz_calculate_min_zoom_roads(planet_osm_line.*)
  WHERE
      (tags -> 'highway' IN ( 'trunk_link', 'primary_link', 'secondary_link', 'tertiary_link',
                   'residential', 'unclassified', 'road', 'living_street', 'pedestrian',
                   'path', 'track', 'cycleway', 'bridleway', 'footway', 'steps',
                   'service' ) OR
       tags -> 'whitewater' = 'portage_way')
      AND mz_calculate_min_zoom_roads(planet_osm_line.*) IS NOT NULL;

CREATE INDEX new_planet_osm_line_roads_geom_index ON planet_osm_line USING gist(way) WHERE mz_road_level IS NOT NULL;
CREATE INDEX new_planet_osm_line_roads_geom_9_index ON planet_osm_line USING gist(way) WHERE mz_road_level <= 9;
CREATE INDEX new_planet_osm_line_roads_geom_12_index ON planet_osm_line USING gist(way) WHERE mz_road_level <= 12;
CREATE INDEX new_planet_osm_line_roads_geom_15_index ON planet_osm_line USING gist(way) WHERE mz_road_level <= 15;

BEGIN;
DROP INDEX IF EXISTS planet_osm_line_roads_geom_index;
ALTER INDEX new_planet_osm_line_roads_geom_index RENAME TO planet_osm_line_roads_geom_index;
COMMIT;

BEGIN;
DROP INDEX IF EXISTS planet_osm_line_roads_geom_9_index;
ALTER INDEX new_planet_osm_line_roads_geom_9_index RENAME TO planet_osm_line_roads_geom_9_index;
COMMIT;

BEGIN;
DROP INDEX IF EXISTS planet_osm_line_roads_geom_12_index;
ALTER INDEX new_planet_osm_line_roads_geom_12_index RENAME TO planet_osm_line_roads_geom_12_index;
COMMIT;

BEGIN;
DROP INDEX IF EXISTS planet_osm_line_roads_geom_15_index;
ALTER INDEX new_planet_osm_line_roads_geom_15_index RENAME TO planet_osm_line_roads_geom_15_index;
COMMIT;