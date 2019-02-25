DO $$
BEGIN

--------------------------------------------------------------------------------
-- planet_osm_polygon
--------------------------------------------------------------------------------

UPDATE planet_osm_polygon SET
   mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(planet_osm_polygon.*),
   mz_building_min_zoom = mz_calculate_min_zoom_buildings(planet_osm_polygon.*),
   mz_earth_min_zoom = mz_calculate_min_zoom_earth(planet_osm_polygon.*),
   mz_landuse_min_zoom = mz_calculate_min_zoom_landuse(planet_osm_polygon.*),
   mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_polygon.*),
   mz_transit_level = mz_calculate_min_zoom_transit(planet_osm_polygon.*),
   mz_water_min_zoom = mz_calculate_min_zoom_water(planet_osm_polygon.*),
   mz_label_placement = ST_PointOnSurface(way)
 WHERE
   -- NOTE: the following line isn't SQL syntax, it's replaced in the
   -- perform-sql-updates.sh script with a range over osm_id when we're
   -- sharding the query to make use of all CPUs, or TRUE if we're not.
   {{SHARDING}};


END $$;
