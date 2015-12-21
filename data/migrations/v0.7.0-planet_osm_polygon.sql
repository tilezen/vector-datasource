CREATE INDEX CONCURRENTLY new_planet_osm_polygon_water_geom_index ON planet_osm_polygon USING gist(way) WHERE mz_calculate_is_water("waterway", "natural", "landuse", "amenity", "leisure") = TRUE;

BEGIN;

DROP INDEX planet_osm_polygon_water_geom_index;
ALTER INDEX new_planet_osm_polygon_water_geom_index RENAME TO planet_osm_polygon_water_geom_index;

COMMIT;
