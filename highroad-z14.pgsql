SELECT
    way AS __geometry__,
    highway,
    railway,

    (CASE WHEN highway IN ('motorway', 'motorway_link') THEN 'highway'
          WHEN highway IN ('trunk', 'trunk_link', 'primary', 'primary_link', 'secondary', 'secondary_link', 'tertiary', 'tertiary_link') THEN 'major_road'
          WHEN highway IN ('residential', 'unclassified', 'road', 'minor') THEN 'minor_road'
          WHEN railway IN ('rail') THEN 'rail'
          ELSE 'unknown' END) AS kind,

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

    (
        --
        -- Highways are separated from other roads and drawn on top.
        --
        (CASE WHEN highway IN ('motorway', 'motorway_link', 'trunk', 'trunk_link') THEN 10000
              ELSE 0
              END)
        
        +

        --
        -- Explicit physical layers are drawn in order.
        --
        (CASE WHEN layer ~ E'^-?[[:digit:]]+(\.[[:digit:]]+)?$' THEN 1000 * CAST (layer AS FLOAT)
              ELSE 0
              END)
        
        +
        
        --
        -- Bridges and tunnels have an implicit physical layering.
        --
        (CASE WHEN bridge IN ('yes', 'true') THEN 100
              WHEN tunnel IN ('yes', 'true') THEN -100
              ELSE 0
              END)
        
        +
        
        --
        -- Large roads are drawn on top of smaller roads.
        --
        (CASE WHEN highway IN ('motorway') THEN 0
              WHEN highway IN ('trunk') THEN -1
              WHEN highway IN ('primary') THEN -2
              WHEN highway IN ('secondary') THEN -3
              WHEN highway IN ('tertiary') THEN -4
              WHEN highway LIKE '%_link' THEN -5
              WHEN highway IN ('residential', 'unclassified', 'road', 'minor') THEN -6
              WHEN railway IN ('rail') THEN -7
              ELSE -9 END)
        
    ) AS sort_key


FROM planet_osm_line

WHERE highway IN ('motorway', 'motorway_link')
   OR highway IN ('trunk', 'trunk_link', 'primary', 'primary_link', 'secondary', 'secondary_link', 'tertiary', 'tertiary_link')
   OR highway IN ('residential', 'unclassified', 'road', 'minor')
   OR railway IN ('rail')
