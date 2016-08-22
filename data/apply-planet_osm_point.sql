DO $$
BEGIN

--------------------------------------------------------------------------------
-- planet_osm_point
--------------------------------------------------------------------------------

UPDATE planet_osm_point SET
    mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_point.*)
    WHERE mz_calculate_min_zoom_pois(planet_osm_point.*) IS NOT NULL;

UPDATE planet_osm_point
  SET mz_earth_min_zoom = mz_calculate_min_zoom_earth(planet_osm_point.*)
  WHERE mz_calculate_min_zoom_earth(planet_osm_point.*) IS NOT NULL;

UPDATE planet_osm_point
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(planet_osm_point.*)
  WHERE mz_calculate_min_zoom_water(planet_osm_point.*) IS NOT NULL;

UPDATE planet_osm_point
  SET mz_places_min_zoom = mz_calculate_min_zoom_places(planet_osm_point.*)
  WHERE mz_calculate_min_zoom_places(planet_osm_point.*) IS NOT NULL;

UPDATE planet_osm_point
  SET mz_building_min_zoom = mz_calculate_min_zoom_buildings(planet_osm_point.*)
  WHERE mz_calculate_min_zoom_buildings(planet_osm_point.*) IS NOT NULL;

CREATE INDEX planet_osm_point_min_zoom_way_index ON planet_osm_point USING gist(way) WHERE mz_poi_min_zoom IS NOT NULL;
CREATE INDEX planet_osm_point_min_zoom_way_9_index ON planet_osm_point USING gist(way) WHERE mz_poi_min_zoom <= 9;
CREATE INDEX planet_osm_point_min_zoom_way_12_index ON planet_osm_point USING gist(way) WHERE mz_poi_min_zoom <= 12;
CREATE INDEX planet_osm_point_min_zoom_way_15_index ON planet_osm_point USING gist(way) WHERE mz_poi_min_zoom <= 15;

CREATE INDEX planet_osm_point_min_zoom_earth_index ON planet_osm_point USING gist(way) WHERE mz_earth_min_zoom IS NOT NULL;
CREATE INDEX planet_osm_point_min_zoom_earth_9_index ON planet_osm_point USING gist(way) WHERE mz_earth_min_zoom <= 9;
CREATE INDEX planet_osm_point_min_zoom_earth_12_index ON planet_osm_point USING gist(way) WHERE mz_earth_min_zoom <= 12;
CREATE INDEX planet_osm_point_min_zoom_earth_15_index ON planet_osm_point USING gist(way) WHERE mz_earth_min_zoom <= 15;

CREATE INDEX planet_osm_point_min_zoom_water_index ON planet_osm_point USING gist(way) WHERE mz_water_min_zoom IS NOT NULL;
CREATE INDEX planet_osm_point_min_zoom_water_9_index ON planet_osm_point USING gist(way) WHERE mz_water_min_zoom <= 9;
CREATE INDEX planet_osm_point_min_zoom_water_12_index ON planet_osm_point USING gist(way) WHERE mz_water_min_zoom <= 12;
CREATE INDEX planet_osm_point_min_zoom_water_15_index ON planet_osm_point USING gist(way) WHERE mz_water_min_zoom <= 15;

CREATE INDEX planet_osm_point_min_zoom_places_index ON planet_osm_point USING gist(way) WHERE mz_places_min_zoom IS NOT NULL;
CREATE INDEX planet_osm_point_min_zoom_places_9_index ON planet_osm_point USING gist(way) WHERE mz_places_min_zoom <= 9;
CREATE INDEX planet_osm_point_min_zoom_places_12_index ON planet_osm_point USING gist(way) WHERE mz_places_min_zoom <= 12;
CREATE INDEX planet_osm_point_min_zoom_places_15_index ON planet_osm_point USING gist(way) WHERE mz_places_min_zoom <= 15;

END $$;

ANALYZE planet_osm_point;
