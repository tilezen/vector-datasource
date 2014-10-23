SELECT
    way AS __geometry__,
    highway,
    name,
    railway,

    (CASE WHEN highway IN ('motorway') THEN 'highway'
    END) AS kind,

    mz_id AS __id__,

    mz_road_sort_key AS sort_key

FROM planet_osm_line

WHERE
    mz_road_level <= 7

ORDER BY sort_key ASC
