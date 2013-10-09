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
          WHEN highway IN ('residential', 'unclassified', 'road') THEN 6
          WHEN highway IN ('unclassified', 'service', 'minor') THEN 7
          ELSE 9 END) AS sort_key

FROM (

 -- SELECT
 --     way,
 --     highway,
 --     name
 -- FROM streets_skeletron
 -- WHERE zoomlevel=16
 -- 
 -- UNION
    
    SELECT
        way,
        highway,
        name
    FROM planet_osm_line

    WHERE highway IN ('motorway', 'motorway_link', 'trunk', 'trunk_link')
       OR highway IN ('primary', 'primary_link', 'secondary', 'secondary_link', 'tertiary', 'tertiary_link')
       OR highway IN ('residential', 'unclassified', 'road', 'unclassified', 'service', 'minor')
       OR highway IN ('footpath', 'track', 'footway', 'steps', 'pedestrian', 'path', 'cycleway')

) AS roads

WHERE name IS NOT NULL