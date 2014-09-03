SELECT
    name,

    (CASE WHEN COALESCE("building:part", building) != 'yes' THEN COALESCE("building:part", building) ELSE NULL END) AS kind,
    COALESCE("building:part", building) AS building,
    "building:part" AS building_part,

    (mz_height * 100)::int AS height,
    (mz_min_height * 100)::int AS min_height,

    way AS __geometry__

FROM
    planet_osm_polygon

WHERE
    mz_is_building_or_part = TRUE
