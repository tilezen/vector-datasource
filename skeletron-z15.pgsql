SELECT
    way AS __geometry__,
    highway,
    name,

    --
    -- Large roads are drawn before smaller roads.
    --
    (CASE WHEN highway IN ('motorway') THEN 0
          WHEN highway IN ('trunk') THEN 1
          WHEN highway IN ('primary') THEN 2
          WHEN highway IN ('secondary') THEN 3
          WHEN highway IN ('tertiary') THEN 4
          WHEN highway LIKE '%_link' THEN 5
          ELSE 9 END) AS sort_key

FROM streets_skeletron

WHERE zoomlevel = 15