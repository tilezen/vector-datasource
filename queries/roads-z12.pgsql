SELECT
    way AS __geometry__,
    highway,
    name,
    railway,

    (CASE WHEN highway IN ('motorway', 'motorway_link') THEN 'highway'
          WHEN highway IN ('trunk', 'trunk_link', 'secondary', 'primary') THEN 'major_road'
          ELSE 'minor_road' END) AS kind,

    (CASE WHEN highway LIKE '%_link' THEN 'yes'
          ELSE 'no' END) AS is_link,
    (CASE WHEN tunnel IN ('yes', 'true') THEN 'yes'
          ELSE 'no' END) AS is_tunnel,
    (CASE WHEN bridge IN ('yes', 'true') THEN 'yes'
          ELSE 'no' END) AS is_bridge,

    mz_id AS __id__,

    mz_road_sort_key AS sort_key

FROM planet_osm_line

WHERE
    mz_road_level <= 12

ORDER BY sort_key ASC
