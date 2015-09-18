DO $$
BEGIN

--------------------------------------------------------------------------------
-- planet_osm_point
--------------------------------------------------------------------------------

CREATE INDEX planet_osm_point_place_index ON planet_osm_point(place) WHERE name IS NOT NULL AND place IN ('borough', 'city', 'continent', 'country', 'county', 'district', 'farm', 'hamlet', 'island', 'isolated_dwelling', 'lake', 'locality', 'neighbourhood', 'ocean', 'province', 'quarter', 'sea', 'state', 'suburb', 'town', 'village');
-- NOTE: removed index on mz_poi_min_zoom, possibly will replace with
-- a partial index at some point in the future, depends on how the
-- query performs.

ALTER TABLE planet_osm_point ADD COLUMN mz_poi_min_zoom SMALLINT;
-- the coalesce here is just an optimisation, as the poi level
-- will always be NULL if all of the arguments are NULL.
UPDATE planet_osm_point SET
    mz_poi_min_zoom = mz_calculate_poi_level("aerialway", "aeroway", "amenity", "barrier", "craft", "highway", "historic", "leisure", "lock", "man_made", "natural", "office", "power", "railway", "shop", "tourism", "waterway", 0::real)
    WHERE coalesce("aerialway", "aeroway", "amenity", "barrier", "craft", "highway", "historic", "leisure", "lock", "man_made", "natural", "office", "power", "railway", "shop", "tourism", "waterway") IS NOT NULL;


END $$;
