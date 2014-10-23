SELECT
    name,
    mz_id AS __id__,

    (CASE WHEN building != 'yes' THEN building ELSE NULL END) AS kind,

    mz_height AS height,
    mz_min_height AS min_height,

    mz_way14 AS __geometry__

FROM
    planet_osm_polygon

WHERE
    building IS NOT NULL
    AND way_area::bigint > 1600 -- 4px

ORDER BY
    way_area DESC,
    __id__ ASC
