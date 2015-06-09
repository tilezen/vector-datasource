SELECT
    osm_id AS __id__,
    way AS __geometry__,
    'openstreetmap' AS source,
    name,
    aeroway,
    bridge,
    highway,
    layer,
    railway,
    tunnel,
    oneway,
    ref,
    operator,
    route,
    tags->'type' AS type,
    tags->'colour' AS colour,
    tags->'network' AS network,
    tags->'state' AS state,
    tags->'symbol' AS symbol,
    tags->'description' AS description,
    tags->'distance' AS distance,
    tags->'ascent' AS ascent,
    tags->'descent' AS descent,
    tags->'roundtrip' AS roundtrip,
    tags->'route_name' AS route_name,
    %#tags AS tags

FROM planet_osm_line

WHERE
    mz_calculate_road_level(highway, railway, aeroway, tags->'network') <= 14
