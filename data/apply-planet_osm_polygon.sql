DO $$
BEGIN

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


-- polygon low zoom
CREATE INDEX
  planet_osm_polygon_landuse_poi_transit_geom_7_index
  ON planet_osm_polygon USING gist(way)
  WHERE
    mz_landuse_min_zoom < 7 OR
    mz_poi_min_zoom < 7 OR
    mz_transit_level < 7;

-- polygon zoom 7 specific query
CREATE INDEX
  planet_osm_polygon_geom_min_zoom_8_index
  ON planet_osm_polygon USING gist(way)
  WHERE
    mz_earth_min_zoom < 8 OR
    mz_landuse_min_zoom < 8 OR
    mz_poi_min_zoom < 8 OR
    mz_transit_level < 8;

-- ladder the rest of the polygon queries
CREATE INDEX
  planet_osm_polygon_geom_min_zoom_9_index
  ON planet_osm_polygon USING gist(way)
  WHERE
    mz_building_min_zoom < 9 OR
    mz_earth_min_zoom < 9 OR
    mz_landuse_min_zoom < 9 OR
    mz_poi_min_zoom < 9 OR
    mz_transit_level < 9 OR
    mz_water_min_zoom < 9;

CREATE INDEX
  planet_osm_polygon_geom_min_zoom_12_index
  ON planet_osm_polygon USING gist(way)
  WHERE
    mz_building_min_zoom < 12 OR
    mz_earth_min_zoom < 12 OR
    mz_landuse_min_zoom < 12 OR
    mz_poi_min_zoom < 12 OR
    mz_transit_level < 12 OR
    mz_water_min_zoom < 12;

CREATE INDEX
  planet_osm_polygon_geom_min_zoom_15_index
  ON planet_osm_polygon USING gist(way)
  WHERE
    mz_building_min_zoom < 15 OR
    mz_earth_min_zoom < 15 OR
    mz_landuse_min_zoom < 15 OR
    mz_poi_min_zoom < 15 OR
    mz_transit_level < 15 OR
    mz_water_min_zoom < 15;

CREATE INDEX
  planet_osm_polygon_geom_min_zoom_index
  ON planet_osm_polygon USING gist(way)
  WHERE
    mz_building_min_zoom IS NOT NULL OR
    mz_earth_min_zoom IS NOT NULL OR
    mz_landuse_min_zoom IS NOT NULL OR
    mz_poi_min_zoom IS NOT NULL OR
    mz_transit_level IS NOT NULL OR
    mz_water_min_zoom IS NOT NULL;


END $$;

ANALYZE planet_osm_polygon;
