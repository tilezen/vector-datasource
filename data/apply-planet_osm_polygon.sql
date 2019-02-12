--DO $$
--BEGIN

\timing on

--------------------------------------------------------------------------------
-- planet_osm_polygon
--------------------------------------------------------------------------------

UPDATE planet_osm_polygon SET
    mz_landuse_min_zoom = mz_calculate_min_zoom_landuse(planet_osm_polygon.*)
    WHERE mz_calculate_min_zoom_landuse(planet_osm_polygon.*) IS NOT NULL;


UPDATE planet_osm_polygon SET
    mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_polygon.*)
    WHERE mz_calculate_min_zoom_pois(planet_osm_polygon.*) IS NOT NULL;


UPDATE planet_osm_polygon SET
  mz_transit_level = mz_calculate_min_zoom_transit(planet_osm_polygon.*)
  WHERE mz_calculate_min_zoom_transit(planet_osm_polygon.*) IS NOT NULL;


UPDATE planet_osm_polygon
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(planet_osm_polygon.*)
  WHERE mz_calculate_min_zoom_water(planet_osm_polygon.*) IS NOT NULL;


UPDATE planet_osm_polygon
  SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(planet_osm_polygon.*)
  WHERE mz_calculate_min_zoom_boundaries(planet_osm_polygon.*) IS NOT NULL;


UPDATE planet_osm_polygon
  SET mz_building_min_zoom = mz_calculate_min_zoom_buildings(planet_osm_polygon.*)
  WHERE mz_calculate_min_zoom_buildings(planet_osm_polygon.*) IS NOT NULL;


UPDATE planet_osm_polygon
  SET mz_earth_min_zoom = mz_calculate_min_zoom_earth(planet_osm_polygon.*)
  WHERE mz_calculate_min_zoom_earth(planet_osm_polygon.*) IS NOT NULL;


UPDATE planet_osm_polygon
  SET mz_label_placement = ST_PointOnSurface(way);


--END $$;

ANALYZE planet_osm_polygon;
