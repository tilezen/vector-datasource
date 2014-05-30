SELECT
    way AS __geometry__,
    highway,
    railway,

    (CASE WHEN highway IN ('motorway') THEN 'highway'
    END) AS kind,

    --
    -- Negative osm_id is synthetic, with possibly multiple geometry rows.
    --
    (CASE WHEN osm_id < 0 THEN Substr(MD5(ST_AsBinary(way)), 1, 10)
          ELSE osm_id::varchar END) AS __id__,

    --
    -- Ascending sort means motorway paints in front.
    --
    (CASE WHEN highway IN ('motorway') THEN 0
          ELSE -9 END) AS sort_key

FROM planet_osm_line

WHERE highway IN ('motorway')

