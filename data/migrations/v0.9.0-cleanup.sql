-- drop no longer used functions, supplanted by generated functions
DROP FUNCTION IF EXISTS mz_calculate_poi_level(
  text, text, text, text, text, text, text, text, text, text, text, text, text,
  text, text, text, text, text, hstore, real);
DROP FUNCTION IF EXISTS mz_calculate_landuse_min_zoom(text, text, text, text, text, text, text, text, text, text, real);
DROP FUNCTION IF EXISTS mz_calculate_landuse_kind(text, text, text, text, text, text, text, text, text, text);
DROP FUNCTION IF EXISTS mz_calculate_is_landuse(text, text, text, text, text, text, text, text, text, text);
DROP FUNCTION IF EXISTS mz_calculate_is_landuse(text, text, text, text, text, text, text, text, text, text, hstore);
DROP FUNCTION IF EXISTS mz_calculate_landuse_kind(text, text, text, text, text, text, text, text, text, text, hstore);

DROP FUNCTION IF EXISTS mz_calculate_transit_level(text);

ALTER TABLE planet_osm_polygon DROP COLUMN IF EXISTS mz_is_landuse;

-- new queries don't use this function, so once the tilequeue/tileserver
-- instances are updated, it should be safe to drop. the new function is
-- called "mz_calculate_transit_routes_and_score".
DROP FUNCTION IF EXISTS mz_calculate_transit_routes(bigint,bigint);

BEGIN;

DO $$
BEGIN
IF EXISTS (SELECT 1 FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace
           WHERE c.relname = 'new_planet_osm_polygon_landuse_geom_9_index'
           AND n.nspname = 'public') THEN
  DROP INDEX IF EXISTS planet_osm_polygon_landuse_geom_9_index;
  ALTER INDEX new_planet_osm_polygon_landuse_geom_9_index RENAME TO planet_osm_polygon_landuse_geom_9_index;
END IF;
END$$;

DO $$
BEGIN
IF EXISTS (SELECT 1 FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace
           WHERE c.relname = 'new_planet_osm_polygon_landuse_geom_12_index'
           AND n.nspname = 'public') THEN
  DROP INDEX IF EXISTS planet_osm_polygon_landuse_geom_12_index;
  ALTER INDEX new_planet_osm_polygon_landuse_geom_12_index RENAME TO planet_osm_polygon_landuse_geom_12_index;
END IF;
END$$;

DO $$
BEGIN
IF EXISTS (SELECT 1 FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace
           WHERE c.relname = 'new_planet_osm_polygon_landuse_geom_15_index'
           AND n.nspname = 'public') THEN
  DROP INDEX IF EXISTS planet_osm_polygon_landuse_geom_15_index;
  ALTER INDEX new_planet_osm_polygon_landuse_geom_15_index RENAME TO planet_osm_polygon_landuse_geom_15_index;
END IF;
END$$;

DO $$
BEGIN
IF EXISTS (SELECT 1 FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace
           WHERE c.relname = 'new_planet_osm_polygon_landuse_boundary_geom_4_index'
           AND n.nspname = 'public') THEN
  DROP INDEX IF EXISTS planet_osm_polygon_landuse_boundary_geom_4_index;
  ALTER INDEX new_planet_osm_polygon_landuse_boundary_geom_4_index RENAME TO planet_osm_polygon_landuse_boundary_geom_4_index;
END IF;
END$$;

DO $$
BEGIN
IF EXISTS (SELECT 1 FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace
           WHERE c.relname = 'new_planet_osm_polygon_landuse_boundary_geom_6_index'
           AND n.nspname = 'public') THEN
  DROP INDEX IF EXISTS planet_osm_polygon_landuse_boundary_geom_6_index;
  ALTER INDEX new_planet_osm_polygon_landuse_boundary_geom_6_index RENAME TO planet_osm_polygon_landuse_boundary_geom_6_index;
END IF;
END$$;

DO $$
BEGIN
IF EXISTS (SELECT 1 FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace
           WHERE c.relname = 'new_planet_osm_polygon_landuse_boundary_geom_8_index'
           AND n.nspname = 'public') THEN
  DROP INDEX IF EXISTS planet_osm_polygon_landuse_boundary_geom_8_index;
  ALTER INDEX new_planet_osm_polygon_landuse_boundary_geom_8_index RENAME TO planet_osm_polygon_landuse_boundary_geom_8_index;
END IF;
END$$;

COMMIT;

ANALYZE planet_osm_polygon;
