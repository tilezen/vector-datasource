DO $$
BEGIN

--------------------------------------------------------------------------------
-- planet_osm_point
--------------------------------------------------------------------------------

UPDATE planet_osm_point SET
    mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_point.*),
    mz_earth_min_zoom = mz_calculate_min_zoom_earth(planet_osm_point.*),
    mz_water_min_zoom = mz_calculate_min_zoom_water(planet_osm_point.*),
    mz_places_min_zoom = mz_calculate_min_zoom_places(planet_osm_point.*),
    mz_building_min_zoom = mz_calculate_min_zoom_buildings(planet_osm_point.*)
  WHERE
    (mz_calculate_min_zoom_pois(planet_osm_point.*) IS NOT NULL OR
     mz_calculate_min_zoom_earth(planet_osm_point.*) IS NOT NULL OR
     mz_calculate_min_zoom_water(planet_osm_point.*) IS NOT NULL OR
     mz_calculate_min_zoom_places(planet_osm_point.*) IS NOT NULL OR
     mz_calculate_min_zoom_buildings(planet_osm_point.*) IS NOT NULL) AND
    -- NOTE: the following line isn't SQL syntax, it's replaced in the
    -- perform-sql-updates.sh script with a range over osm_id when we're
    -- sharding the query to make use of all CPUs, or TRUE if we're not.
    {{SHARDING}};

END $$;
