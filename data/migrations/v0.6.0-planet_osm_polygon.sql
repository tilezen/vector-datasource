DO $$
BEGIN

IF NOT EXISTS (
  SELECT 1
  FROM   pg_class c
  JOIN   pg_namespace n ON n.oid = c.relnamespace
  WHERE  c.relname = 'planet_osm_polygon_railway_platform_index'
  AND    n.nspname = 'public'
  ) THEN

  CREATE INDEX planet_osm_polygon_railway_platform_index ON planet_osm_polygon USING gist(way) WHERE railway='platform';
END IF;

END$$;

UPDATE planet_osm_polygon
  SET mz_is_landuse = TRUE,
      mz_landuse_min_zoom = mz_calculate_landuse_min_zoom("landuse", "leisure", "natural", "highway", "amenity", "aeroway", "tourism", "man_made", "power", "boundary", way_area)
WHERE landuse IN ('rural', 'military', 'winter_sports')
   OR "natural" = 'beach';

UPDATE planet_osm_polygon
  SET mz_poi_min_zoom = mz_calculate_poi_level("aerialway", "aeroway", "amenity", "barrier", "craft", "highway", "historic", "leisure", "lock", "man_made", "natural", "office", "power", "railway", "tags"->'rental', "shop", "tourism", "waterway", way_area)
WHERE railway = 'station'
   OR shop IN ('toys', 'ski', 'alcohol', 'wine', 'ice_cream')
   OR "natural" = 'beach'
   OR tags->'rental' = 'ski'
   OR amenity IN ('ski_rental', 'ski_school', 'ice_cream')
   OR man_made = 'snow_cannon'
   OR highway = 'motorway_junction'
   OR tourism = 'zoo';
