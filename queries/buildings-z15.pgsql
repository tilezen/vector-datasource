SELECT
    name,

    (CASE WHEN COALESCE("building:part", building) != 'yes' THEN COALESCE("building:part", building) ELSE NULL END) AS kind,
    
    -- strip commas from heights (TODO: may need to strip other characters and/or do unit conversions)
    TO_NUMBER(REPLACE(height, ',', '.'), '999999D99S')::float AS height,
    TO_NUMBER(REPLACE(min_height, ',', '.'), '999999D99S')::float AS min_height,

    way AS __geometry__

FROM
    planet_osm_polygon AS building_outer

WHERE
    (building IS NOT NULL OR "building:part" IS NOT NULL)
    AND way_area > 100 -- 4px
