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

-- ladder the point indexes
CREATE INDEX
  planet_osm_point_geom_min_zoom_6_index
  ON planet_osm_point USING gist(way)
  WHERE
    mz_building_min_zoom < 6 OR
    mz_earth_min_zoom < 6 OR
    mz_places_min_zoom < 6 OR
    mz_poi_min_zoom < 6 OR
    mz_water_min_zoom < 6;

CREATE INDEX
  planet_osm_point_geom_min_zoom_9_index
  ON planet_osm_point USING gist(way)
  WHERE
    mz_building_min_zoom < 9 OR
    mz_earth_min_zoom < 9 OR
    mz_places_min_zoom < 9 OR
    mz_poi_min_zoom < 9 OR
    mz_water_min_zoom < 9;

CREATE INDEX
  planet_osm_point_geom_min_zoom_12_index
  ON planet_osm_point USING gist(way)
  WHERE
    mz_building_min_zoom < 12 OR
    mz_earth_min_zoom < 12 OR
    mz_places_min_zoom < 12 OR
    mz_poi_min_zoom < 12 OR
    mz_water_min_zoom < 12;

CREATE INDEX
  planet_osm_point_geom_min_zoom_15_index
  ON planet_osm_point USING gist(way)
  WHERE
    mz_building_min_zoom < 15 OR
    mz_earth_min_zoom < 15 OR
    mz_places_min_zoom < 15 OR
    mz_poi_min_zoom < 15 OR
    mz_water_min_zoom < 15;

CREATE INDEX
  planet_osm_point_geom_min_zoom_index
  ON planet_osm_point USING gist(way)
  WHERE
    mz_building_min_zoom IS NOT NULL OR
    mz_earth_min_zoom IS NOT NULL OR
    mz_places_min_zoom IS NOT NULL OR
    mz_poi_min_zoom IS NOT NULL OR
    mz_water_min_zoom IS NOT NULL;

END $$;

ANALYZE planet_osm_point;
