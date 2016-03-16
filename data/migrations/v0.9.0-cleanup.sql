-- drop no longer used functions, supplanted by generated functions
DROP FUNCTION IF EXISTS mz_calculate_poi_level(
  text, text, text, text, text, text, text, text, text, text, text, text, text,
  text, text, text, text, text, hstore, real);
DROP FUNCTION IF EXISTS mz_calculate_landuse_min_zoom(text, text, text, text, text, text, text, text, text, text, real);
DROP FUNCTION IF EXISTS mz_calculate_landuse_kind(text, text, text, text, text, text, text, text, text, text);
DROP FUNCTION IF EXISTS mz_calculate_is_landuse(text, text, text, text, text, text, text, text, text, text);
DROP FUNCTION IF EXISTS mz_calculate_is_landuse(text, text, text, text, text, text, text, text, text, text, hstore);
DROP FUNCTION IF EXISTS mz_calculate_landuse_kind(text, text, text, text, text, text, text, text, text, text, hstore);

ALTER TABLE planet_osm_polygon DROP COLUMN IF EXISTS mz_is_landuse;

BEGIN;

DROP INDEX planet_osm_polygon_landuse_geom_9_index;
ALTER INDEX new_planet_osm_polygon_landuse_geom_9_index RENAME TO planet_osm_polygon_landuse_geom_9_index;;
DROP INDEX planet_osm_polygon_landuse_geom_12_index;
ALTER INDEX new_planet_osm_polygon_landuse_geom_12_index RENAME TO planet_osm_polygon_landuse_geom_12_index;
DROP INDEX planet_osm_polygon_landuse_geom_15_index;
ALTER INDEX new_planet_osm_polygon_landuse_geom_15_index RENAME TO planet_osm_polygon_landuse_geom_15_index;

DROP INDEX planet_osm_polygon_landuse_boundary_geom_4_index;
ALTER INDEX new_planet_osm_polygon_landuse_boundary_geom_4_index RENAME TO planet_osm_polygon_landuse_boundary_geom_4_index;
DROP INDEX planet_osm_polygon_landuse_boundary_geom_6_index;
ALTER INDEX new_planet_osm_polygon_landuse_boundary_geom_6_index RENAME TO planet_osm_polygon_landuse_boundary_geom_6_index;
DROP INDEX planet_osm_polygon_landuse_boundary_geom_8_index;
ALTER INDEX new_planet_osm_polygon_landuse_boundary_geom_8_index RENAME TO planet_osm_polygon_landuse_boundary_geom_8_index;

COMMIT;

ANALYZE planet_osm_polygon;
