SELECT
    name,

    (CASE WHEN COALESCE("building:part", building) != 'yes' THEN COALESCE("building:part", building) ELSE NULL END) AS kind,
    COALESCE("building:part", building) AS building,
    "building:part" AS building_part,

    -- strip commas from heights (TODO: may need to strip other characters and/or do unit conversions)
    -- multiply by 100 and force int becuase that's what OpenScienceMap expects
    (TO_NUMBER(REPLACE(height, ',', '.'), '999999D99S') * 100)::int AS height,
    (TO_NUMBER(REPLACE(min_height, ',', '.'), '999999D99S') * 100)::int AS min_height,

    way AS __geometry__

FROM
    planet_osm_polygon AS building_outer

WHERE
    (building IS NOT NULL OR "building:part" IS NOT NULL)
