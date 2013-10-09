SELECT
    way AS __geometry__,
    highway,
    railway,

    (CASE WHEN highway IN ('motorway') THEN 'highway'
          WHEN highway IN ('trunk', 'primary') THEN 'major_road'
          ELSE 'minor_road' END) AS kind,

    'no'::VARCHAR AS is_link,
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
          WHEN highway IN ('trunk', 'primary') THEN -1
          WHEN highway IN ('secondary', 'tertiary') THEN -2
          ELSE -9 END) AS sort_key

FROM planet_osm_line

WHERE highway IN ('motorway')
   OR highway IN ('trunk', 'primary')
   OR highway IN ('secondary', 'tertiary')
