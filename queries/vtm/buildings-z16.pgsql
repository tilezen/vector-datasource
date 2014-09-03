SELECT
    name,

    (CASE WHEN building != 'yes' THEN building ELSE NULL END) AS kind,
    building,

    (mz_height * 100)::int AS height,
    (mz_min_height * 100)::int AS min_height,

    way AS __geometry__

FROM
    planet_osm_polygon

WHERE
    building IS NOT NULL
    AND way_area::bigint > 25 -- 4px
