-- old version of the POI level calculation without the 'disused' parameter.
DROP FUNCTION IF EXISTS mz_calculate_poi_level(
  text, text, text, text, text, text, text, text, text, text, text, text, text,
  text, text, text, text, text, hstore, real);

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
