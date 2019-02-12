--DO $$
--BEGIN

\timing on

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
    mz_calculate_min_zoom_pois(planet_osm_point.*) IS NOT NULL OR
    mz_calculate_min_zoom_earth(planet_osm_point.*) IS NOT NULL OR
    mz_calculate_min_zoom_water(planet_osm_point.*) IS NOT NULL OR
    mz_calculate_min_zoom_places(planet_osm_point.*) IS NOT NULL OR
    mz_calculate_min_zoom_buildings(planet_osm_point.*) IS NOT NULL;

--END $$;

ANALYZE planet_osm_point;
