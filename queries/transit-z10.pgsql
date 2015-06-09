SELECT
    osm_id AS __id__,
    way AS __geometry__,
    name,
    ref,
    operator,
    route AS kind,
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

WHERE mz_calculate_transit_level(route) <= 10
