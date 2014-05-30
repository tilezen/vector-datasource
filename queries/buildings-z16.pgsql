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

    -- building "shells" that enclose building parts should not be rendered
    AND NOT (
        building_outer.building IS NOT NULL
        AND building_outer."building:part" IS NULL
        AND EXISTS (
            SELECT
                building_part_inner.osm_id
            FROM
                planet_osm_polygon AS building_part_inner
            WHERE
                building_part_inner.osm_id != building_outer.osm_id
                AND building_part_inner."building:part" IS NOT NULL
                AND ST_Intersects(building_outer.way, building_part_inner.way)
            LIMIT 1
        )
    )

    AND ST_Area(way) > 25 -- 4px
