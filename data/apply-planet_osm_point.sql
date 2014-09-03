DO $$
BEGIN

--------------------------------------------------------------------------------
-- planet_osm_point
--------------------------------------------------------------------------------

ALTER TABLE planet_osm_point
    ADD COLUMN mz_id TEXT,
    ADD COLUMN mz_poi_level SMALLINT;

UPDATE planet_osm_point SET
    mz_id = mz_normalize_id(osm_id, way),
    mz_poi_level = mz_calculate_poi_level(
        "aerialway",
        "aeroway",
        "amenity",
        "barrier",
        "highway",
        "historic",
        "leisure",
        "lock",
        "man_made",
        "natural",
        "power",
        "railway",
        "shop",
        "tourism",
        "waterway"
    );

PERFORM mz_create_partial_index_if_not_exists('planet_osm_point_place', 'planet_osm_point', 'place',
    'name IS NOT NULL' );
PERFORM mz_create_partial_index_if_not_exists('planet_osm_point_mz_poi_level_index', 'planet_osm_point', 'mz_poi_level', 'mz_poi_level IS NOT NULL');

END $$;
