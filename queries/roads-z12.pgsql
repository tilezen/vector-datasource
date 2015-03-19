SELECT
    way AS __geometry__,
    highway,
    name,
    railway,
    aeroway,
    osm_id,
    mz_id AS __id__,
    mz_road_sort_key AS sort_key,

    (CASE WHEN highway IN ('motorway', 'motorway_link') THEN 'highway'
          WHEN highway IN ('trunk', 'trunk_link', 'secondary', 'primary') THEN 'major_road'
          ELSE 'minor_road' END) AS kind,

    (CASE WHEN highway LIKE '%_link' THEN 'yes'
          ELSE 'no' END) AS is_link,
    (CASE WHEN tunnel IN ('yes', 'true') THEN 'yes'
          ELSE 'no' END) AS is_tunnel,
    (CASE WHEN bridge IN ('yes', 'true') THEN 'yes'
          ELSE 'no' END) AS is_bridge

FROM planet_osm_line

WHERE
    mz_road_level <= 12

ORDER BY sort_key ASC
