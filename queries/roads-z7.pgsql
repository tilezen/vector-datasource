SELECT
    way AS __geometry__,
    highway,
    name,
    railway,
    osm_id,
    mz_id AS __id__,
    mz_road_sort_key AS sort_key,

    (CASE WHEN highway IN ('motorway') THEN 'highway'
    END) AS kind

FROM planet_osm_line

WHERE
    mz_road_level <= 7

ORDER BY sort_key ASC
