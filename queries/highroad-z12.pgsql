SELECT
    way AS __geometry__,
    highway,
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
    
    --
    -- Negative osm_id is synthetic, with possibly multiple geometry rows.
    --
    (CASE WHEN osm_id < 0 THEN Substr(MD5(ST_AsBinary(way)), 1, 10)
          ELSE osm_id::varchar END) AS __id__,

    --
    -- Ascending sort means motorway paints in front.
    --
    (CASE WHEN highway IN ('motorway') THEN 0
          WHEN highway IN ('trunk', 'secondary', 'primary') THEN -1
          WHEN highway IN ('tertiary', 'residential', 'unclassified', 'road') THEN -2
          WHEN highway LIKE '%_link' THEN -3
          ELSE -9 END) AS sort_key

FROM planet_osm_line

WHERE highway IN ('motorway', 'motorway_link')
   OR highway IN ('trunk', 'trunk_link', 'secondary', 'primary')
   OR highway IN ('tertiary', 'residential', 'unclassified', 'road', 'unclassified')
