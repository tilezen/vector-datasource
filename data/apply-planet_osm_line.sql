DO $$
BEGIN

--------------------------------------------------------------------------------
-- planet_osm_line
--------------------------------------------------------------------------------

UPDATE planet_osm_line
  SET mz_road_level = mz_calculate_min_zoom_roads(planet_osm_line.*)
  WHERE mz_calculate_min_zoom_roads(planet_osm_line.*) IS NOT NULL;

UPDATE planet_osm_line
  SET mz_transit_level = mz_calculate_min_zoom_transit(planet_osm_line.*)
  WHERE mz_calculate_min_zoom_transit(planet_osm_line.*) IS NOT NULL;

UPDATE planet_osm_line
  SET mz_earth_min_zoom = mz_calculate_min_zoom_earth(planet_osm_line.*)
  WHERE mz_calculate_min_zoom_earth(planet_osm_line.*) IS NOT NULL;

UPDATE planet_osm_line
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(planet_osm_line.*)
  WHERE mz_calculate_min_zoom_water(planet_osm_line.*) IS NOT NULL;

UPDATE planet_osm_line
  SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(planet_osm_line.*)
  WHERE mz_calculate_min_zoom_boundaries(planet_osm_line.*) IS NOT NULL;

UPDATE planet_osm_line
  SET mz_landuse_min_zoom = mz_calculate_min_zoom_landuse(planet_osm_line.*)
  WHERE mz_calculate_min_zoom_landuse(planet_osm_line.*) IS NOT NULL;

UPDATE planet_osm_line
  SET mz_label_placement = ST_PointOnSurface(way);

-- only these 2 columns are relevant in lower zoom queries
CREATE
  INDEX planet_osm_line_geom_min_zoom_8_index
  ON planet_osm_line USING gist(way)
  WHERE
    mz_landuse_min_zoom < 8 OR
    mz_transit_level < 8;

-- ladder the higher zoom level indexes
CREATE INDEX
  planet_osm_line_geom_min_zoom_9_index
  ON planet_osm_line USING gist(way)
  WHERE
    mz_earth_min_zoom < 9 OR
    mz_landuse_min_zoom < 9 OR
    mz_road_level < 9 OR
    mz_transit_level < 9 OR
    mz_water_min_zoom < 9;

CREATE INDEX
  planet_osm_line_geom_min_zoom_12_index
  ON planet_osm_line USING gist(way)
  WHERE
    mz_earth_min_zoom < 12 OR
    mz_landuse_min_zoom < 12 OR
    mz_road_level < 12 OR
    mz_transit_level < 12 OR
    mz_water_min_zoom < 12;

CREATE INDEX
  planet_osm_line_geom_min_zoom_15_index
  ON planet_osm_line USING gist(way)
  WHERE
    mz_earth_min_zoom < 15 OR
    mz_landuse_min_zoom < 15 OR
    mz_road_level < 15 OR
    mz_transit_level < 15 OR
    mz_water_min_zoom < 15;

CREATE INDEX
  planet_osm_line_geom_min_zoom_index
  ON planet_osm_line USING gist(way)
  WHERE
    mz_earth_min_zoom IS NOT NULL OR
    mz_landuse_min_zoom IS NOT NULL OR
    mz_road_level IS NOT NULL OR
    mz_transit_level IS NOT NULL OR
    mz_water_min_zoom IS NOT NULL;

END $$;

ANALYZE planet_osm_line;
