SELECT
    osm_id AS __id__,
    way AS __geometry__,
    tags->'border_type' AS kind,
    name,
    %#tags AS tags
FROM
    planet_osm_line
WHERE
    boundary='administrative'
