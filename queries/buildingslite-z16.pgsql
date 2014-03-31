SELECT
    name,

    (CASE WHEN building != 'yes' THEN building ELSE NULL END) AS kind,
    building,

    -- strip commas from heights (TODO: may need to strip other characters and/or do unit conversions)
    -- multiply by 100 and force int becuase that's what OpenScienceMap expects
    (TO_NUMBER(REPLACE(height, ',', '.'), '999999D99S') * 100)::int AS height,

    way AS __geometry__

FROM
    planet_osm_polygon

WHERE
    building IS NOT NULL
    AND ST_Area(way) > 25 -- 4px
