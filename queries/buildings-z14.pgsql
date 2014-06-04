SELECT
    name,

    (CASE WHEN building != 'yes' THEN building ELSE NULL END) AS kind,

    -- strip commas from heights (TODO: may need to strip other characters and/or do unit conversions)
    TO_NUMBER(REPLACE(height, ',', '.'), '999999D99S')::float AS height,
    TO_NUMBER(REPLACE(min_height, ',', '.'), '999999D99S')::float AS min_height,

    way AS __geometry__

FROM
    planet_osm_polygon

WHERE
    building IS NOT NULL

    AND ST_Area(way) > 100
