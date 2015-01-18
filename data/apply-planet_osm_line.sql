DO $$
BEGIN

--------------------------------------------------------------------------------
-- planet_osm_line
--------------------------------------------------------------------------------

ALTER TABLE planet_osm_line
    ADD COLUMN mz_id TEXT,
    ADD COLUMN mz_road_level SMALLINT,
    ADD COLUMN mz_road_sort_key FLOAT;

UPDATE planet_osm_line AS line SET
    mz_id = mz_normalize_id(road.osm_id, road.way),
    mz_road_level = road.mz_road_level,
    mz_road_sort_key = (CASE WHEN road.mz_road_level IS NULL
        THEN NULL
        ELSE mz_calculate_road_sort_key(road.layer, road.bridge, road.tunnel, road.highway, road.railway)
    END)

    FROM (
        SELECT osm_id, way, layer, bridge, tunnel, highway, railway, mz_calculate_road_level(highway, railway) AS mz_road_level
        FROM planet_osm_line
    ) road

    WHERE line.osm_id = road.osm_id;

PERFORM mz_create_partial_index_if_not_exists('planet_osm_line_mz_road_level_index', 'planet_osm_line', 'mz_road_level', 'mz_road_level IS NOT NULL');
PERFORM mz_create_partial_index_if_not_exists('planet_osm_line_waterway', 'planet_osm_line', 'waterway', 'waterway IS NOT NULL');

END $$;
