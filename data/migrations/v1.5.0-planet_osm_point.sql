-- ladder the point indexes
CREATE INDEX IF NOT EXISTS planet_osm_point_building_earth_places_pois_water_geom_6_index
  ON planet_osm_point USING gist(way)
  WHERE
    mz_building_min_zoom < 6 OR
    mz_earth_min_zoom < 6 OR
    mz_places_min_zoom < 6 OR
    mz_poi_min_zoom < 6 OR
    mz_water_min_zoom < 6;

CREATE INDEX IF NOT EXISTS planet_osm_point_building_earth_places_pois_water_geom_9_index
  ON planet_osm_point USING gist(way)
  WHERE
    mz_building_min_zoom < 9 OR
    mz_earth_min_zoom < 9 OR
    mz_places_min_zoom < 9 OR
    mz_poi_min_zoom < 9 OR
    mz_water_min_zoom < 9;

CREATE INDEX IF NOT EXISTS planet_osm_point_building_earth_places_pois_water_geom_12_index
  ON planet_osm_point USING gist(way)
  WHERE
    mz_building_min_zoom < 12 OR
    mz_earth_min_zoom < 12 OR
    mz_places_min_zoom < 12 OR
    mz_poi_min_zoom < 12 OR
    mz_water_min_zoom < 12;

CREATE INDEX IF NOT EXISTS planet_osm_point_building_earth_places_pois_water_geom_15_index
  ON planet_osm_point USING gist(way)
  WHERE
    mz_building_min_zoom < 15 OR
    mz_earth_min_zoom < 15 OR
    mz_places_min_zoom < 15 OR
    mz_poi_min_zoom < 15 OR
    mz_water_min_zoom < 15;

CREATE INDEX IF NOT EXISTS planet_osm_point_building_earth_places_pois_water_geom_index
  ON planet_osm_point USING gist(way)
  WHERE
    mz_building_min_zoom IS NOT NULL OR
    mz_earth_min_zoom IS NOT NULL OR
    mz_places_min_zoom IS NOT NULL OR
    mz_poi_min_zoom IS NOT NULL OR
    mz_water_min_zoom IS NOT NULL;

-- remove all old indexes

DROP INDEX IF EXISTS planet_osm_point_min_zoom_pois_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_pois_6_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_pois_9_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_pois_12_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_pois_15_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_earth_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_earth_9_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_earth_12_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_earth_15_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_water_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_water_9_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_water_12_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_water_15_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_places_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_places_9_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_places_12_index;
DROP INDEX IF EXISTS planet_osm_point_min_zoom_places_15_index;
