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


CREATE INDEX planet_osm_polygon_landuse_geom_9_index ON planet_osm_polygon USING gist(way) WHERE mz_landuse_min_zoom <= 9;
CREATE INDEX planet_osm_polygon_landuse_geom_12_index ON planet_osm_polygon USING gist(way) WHERE mz_landuse_min_zoom <= 12;
CREATE INDEX planet_osm_polygon_landuse_geom_15_index ON planet_osm_polygon USING gist(way) WHERE mz_landuse_min_zoom <= 15;

CREATE INDEX planet_osm_polygon_railway_platform_index ON planet_osm_polygon USING gist(way) WHERE tags ? 'railway' and tags->'railway'='platform';

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
