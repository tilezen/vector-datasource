DO $$
BEGIN

--------------------------------------------------------------------------------
-- planet_osm_line
--------------------------------------------------------------------------------

UPDATE planet_osm_line SET
    mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(planet_osm_line.*),
    mz_earth_min_zoom = mz_calculate_min_zoom_earth(planet_osm_line.*),
    mz_landuse_min_zoom = mz_calculate_min_zoom_landuse(planet_osm_line.*),
    mz_road_level = mz_calculate_min_zoom_roads(planet_osm_line.*),
    mz_transit_level = mz_calculate_min_zoom_transit(planet_osm_line.*),
    mz_water_min_zoom = mz_calculate_min_zoom_water(planet_osm_line.*),
    mz_label_placement = ST_PointOnSurface(way)
  WHERE
    -- NOTE: the following line isn't SQL syntax, it's replaced in the
    -- perform-sql-updates.sh script with a range over osm_id when we're
    -- sharding the query to make use of all CPUs, or TRUE if we're not.
    {{SHARDING}};

END $$;
