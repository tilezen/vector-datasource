UPDATE planet_osm_polygon SET
  mz_is_landuse = TRUE,
  mz_landuse_min_zoom = mz_calculate_landuse_min_zoom("landuse", "leisure", "natural", "highway", "amenity", "aeroway", "tourism", "man_made", "power", "boundary", way_area)
  WHERE amenity='prison';

UPDATE planet_osm_polygon SET
  mz_poi_min_zoom = mz_calculate_poi_level("aerialway", "aeroway", "amenity", "barrier", "craft", "highway", "historic", "leisure", "lock", "man_made", "natural", "office", "power", "railway", "tags"->'rental', "shop", "tourism", "waterway", way_area)
  WHERE
    "leisure" IN ('sports_centre', 'fitness_centre', 'fitness_station') OR
    "amenity" IN ('gym', 'prison') OR
    "shop" = 'electronics' OR
    "aeroway" = 'gate';

CREATE INDEX CONCURRENTLY new_planet_osm_polygon_water_geom_index ON planet_osm_polygon USING gist(way) WHERE mz_calculate_is_water("amenity", "landuse", "leisure", "natural", "waterway") = TRUE;

BEGIN;

DROP INDEX planet_osm_polygon_water_geom_index;
ALTER INDEX new_planet_osm_polygon_water_geom_index RENAME TO planet_osm_polygon_water_geom_index;

COMMIT;
