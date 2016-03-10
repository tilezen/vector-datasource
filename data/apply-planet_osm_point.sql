DO $$
BEGIN

--------------------------------------------------------------------------------
-- planet_osm_point
--------------------------------------------------------------------------------

ALTER TABLE planet_osm_point ADD COLUMN mz_poi_min_zoom REAL;
-- the coalesce here is just an optimisation, as the poi level
-- will always be NULL if all of the arguments are NULL.
UPDATE planet_osm_point SET
    mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_point.*)
    WHERE mz_calculate_min_zoom_pois(planet_osm_point.*) IS NOT NULL;

CREATE INDEX planet_osm_point_place_index ON planet_osm_point(place) WHERE name IS NOT NULL AND place IN ('borough', 'city', 'continent', 'country', 'county', 'district', 'farm', 'hamlet', 'island', 'isolated_dwelling', 'lake', 'locality', 'neighbourhood', 'ocean', 'province', 'quarter', 'sea', 'state', 'suburb', 'town', 'village');

CREATE INDEX planet_osm_point_min_zoom_way_9_index ON planet_osm_point USING gist(way) WHERE mz_poi_min_zoom <= 9;
CREATE INDEX planet_osm_point_min_zoom_way_12_index ON planet_osm_point USING gist(way) WHERE mz_poi_min_zoom <= 12;
CREATE INDEX planet_osm_point_min_zoom_way_15_index ON planet_osm_point USING gist(way) WHERE mz_poi_min_zoom <= 15;

END $$;

ANALYZE planet_osm_point;
