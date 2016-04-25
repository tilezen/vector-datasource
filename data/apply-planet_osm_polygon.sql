DO $$
BEGIN

--------------------------------------------------------------------------------
-- planet_osm_polygon
--------------------------------------------------------------------------------

-- indexes on existing columns
CREATE INDEX planet_osm_polygon_wayarea_index ON planet_osm_polygon(way_area);
CREATE INDEX planet_osm_polygon_building_index ON planet_osm_polygon(building) WHERE building IS NOT NULL;
CREATE INDEX planet_osm_polygon_is_building_or_part_index ON planet_osm_polygon(mz_calculate_is_building_or_part(building, "building:part")) WHERE mz_calculate_is_building_or_part(building, "building:part") = TRUE;


UPDATE planet_osm_polygon SET
    mz_landuse_min_zoom = mz_calculate_min_zoom_landuse(planet_osm_polygon.*)
    WHERE mz_calculate_min_zoom_landuse(planet_osm_polygon.*) IS NOT NULL;


UPDATE planet_osm_polygon SET
    mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_polygon.*)
    WHERE mz_calculate_min_zoom_pois(planet_osm_polygon.*) IS NOT NULL;


UPDATE planet_osm_polygon SET
  mz_transit_level = mz_calculate_min_zoom_transit(planet_osm_polygon.*)
  WHERE mz_calculate_min_zoom_transit(planet_osm_polygon.*) IS NOT NULL;


UPDATE ne_110m_land
  SET mz_earth_min_zoom = mz_calculate_min_zoom_earth(ne_110m_land.*)
  WHERE mz_calculate_min_zoom_earth(ne_110m_land.*) IS NOT NULL;
  
UPDATE ne_50m_land
  SET mz_earth_min_zoom = mz_calculate_min_zoom_earth(ne_50m_land.*)
  WHERE mz_calculate_min_zoom_earth(ne_50m_land.*) IS NOT NULL;
  
UPDATE ne_10m_land
  SET mz_earth_min_zoom = mz_calculate_min_zoom_earth(ne_10m_land.*)
  WHERE mz_calculate_min_zoom_earth(ne_10m_land.*) IS NOT NULL;

UPDATE land_polygons
  SET mz_earth_min_zoom = mz_calculate_min_zoom_earth(land_polygons.*)
  WHERE mz_calculate_min_zoom_earth(land_polygons.*) IS NOT NULL;

UPDATE planet_osm_polygon
  SET mz_earth_min_zoom = mz_calculate_min_zoom_earth(planet_osm_polygon.*)
  WHERE mz_calculate_min_zoom_earth(planet_osm_polygon.*) IS NOT NULL;


UPDATE ne_110m_ocean
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_110m_ocean.*)
  WHERE mz_calculate_min_zoom_water(ne_110m_ocean.*) IS NOT NULL;
  
UPDATE ne_50m_ocean
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_50m_ocean.*)
  WHERE mz_calculate_min_zoom_water(ne_50m_ocean.*) IS NOT NULL;
  
UPDATE ne_10m_ocean
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_10m_ocean.*)
  WHERE mz_calculate_min_zoom_water(ne_10m_ocean.*) IS NOT NULL;

UPDATE ne_110m_lakes
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_110m_lakes.*)
  WHERE mz_calculate_min_zoom_water(ne_110m_lakes.*) IS NOT NULL;
  
UPDATE ne_50m_lakes
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_50m_lakes.*)
  WHERE mz_calculate_min_zoom_water(ne_50m_lakes.*) IS NOT NULL;
  
UPDATE ne_10m_lakes
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_10m_lakes.*)
  WHERE mz_calculate_min_zoom_water(ne_10m_lakes.*) IS NOT NULL;

UPDATE ne_50m_playas
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_50m_playas.*)
  WHERE mz_calculate_min_zoom_water(ne_50m_playas.*) IS NOT NULL;
  
UPDATE ne_10m_playas
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(ne_10m_playas.*)
  WHERE mz_calculate_min_zoom_water(ne_10m_playas.*) IS NOT NULL;

UPDATE water_polygons
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(water_polygons.*)
  WHERE mz_calculate_min_zoom_water(water_polygons.*) IS NOT NULL;

UPDATE planet_osm_polygon
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(planet_osm_polygon.*)
  WHERE mz_calculate_min_zoom_water(planet_osm_polygon.*) IS NOT NULL;


UPDATE planet_osm_polygon
  SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(planet_osm_polygon.*)
  WHERE mz_calculate_min_zoom_boundaries(planet_osm_polygon.*) IS NOT NULL;


UPDATE planet_osm_polygon
  SET mz_building_min_zoom = mz_calculate_min_zoom_buildings(planet_osm_polygon.*)
  WHERE mz_calculate_min_zoom_buildings(planet_osm_polygon.*) IS NOT NULL;


CREATE INDEX planet_osm_polygon_landuse_geom_9_index ON planet_osm_polygon USING gist(way) WHERE mz_landuse_min_zoom <= 9;
CREATE INDEX planet_osm_polygon_landuse_geom_12_index ON planet_osm_polygon USING gist(way) WHERE mz_landuse_min_zoom <= 12;
CREATE INDEX planet_osm_polygon_landuse_geom_15_index ON planet_osm_polygon USING gist(way) WHERE mz_landuse_min_zoom <= 15;

CREATE INDEX planet_osm_polygon_railway_platform_index ON planet_osm_polygon USING gist(way) WHERE railway='platform';

CREATE INDEX planet_osm_polygon_transit_geom_index ON planet_osm_polygon USING gist(way) WHERE mz_transit_level IS NOT NULL;
CREATE INDEX planet_osm_polygon_transit_geom_6_index ON planet_osm_polygon USING gist(way) WHERE mz_transit_level <= 6;
CREATE INDEX planet_osm_polygon_transit_geom_9_index ON planet_osm_polygon USING gist(way) WHERE mz_transit_level <= 9;
CREATE INDEX planet_osm_polygon_transit_geom_12_index ON planet_osm_polygon USING gist(way) WHERE mz_transit_level <= 12;
CREATE INDEX planet_osm_polygon_transit_geom_15_index ON planet_osm_polygon USING gist(way) WHERE mz_transit_level <= 15;

CREATE INDEX planet_osm_polygon_earth_geom_9_index  ON planet_osm_polygon USING gist(way) WHERE mz_earth_min_zoom <= 9;
CREATE INDEX planet_osm_polygon_earth_geom_12_index ON planet_osm_polygon USING gist(way) WHERE mz_earth_min_zoom <= 12;
CREATE INDEX planet_osm_polygon_earth_geom_15_index ON planet_osm_polygon USING gist(way) WHERE mz_earth_min_zoom <= 15;

CREATE INDEX planet_osm_polygon_water_geom_9_index ON planet_osm_polygon USING gist(way) WHERE mz_water_min_zoom <= 9;
CREATE INDEX planet_osm_polygon_water_geom_12_index ON planet_osm_polygon USING gist(way) WHERE mz_water_min_zoom <= 12;
CREATE INDEX planet_osm_polygon_water_geom_15_index ON planet_osm_polygon USING gist(way) WHERE mz_water_min_zoom <= 15;

CREATE INDEX planet_osm_polygon_boundary_geom_9_index ON planet_osm_polygon USING gist(way) WHERE mz_boundary_min_zoom <= 9;
CREATE INDEX planet_osm_polygon_boundary_geom_12_index ON planet_osm_polygon USING gist(way) WHERE mz_boundary_min_zoom <= 12;
CREATE INDEX planet_osm_polygon_boundary_geom_15_index ON planet_osm_polygon USING gist(way) WHERE mz_boundary_min_zoom <= 15;

CREATE INDEX planet_osm_polygon_building_geom_15_index ON planet_osm_polygon USING gist(way) WHERE mz_building_min_zoom <= 15;

END $$;

ANALYZE planet_osm_polygon;
