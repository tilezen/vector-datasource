SELECT name, area, kind, source, __geometry__, __id__

FROM
(
    --
    -- Ocean
    --
    SELECT '' AS name,
           way_area::bigint AS area,
           'ocean' AS kind,
           'openstreetmapdata.com' AS source,
           mz_the_geom12 AS __geometry__,
           gid::varchar AS __id__

    FROM water_polygons

    WHERE mz_the_geom12 && !bbox!

    --
    -- Other water areas
    --
    UNION

    SELECT name,
           way_area::bigint AS area,
           COALESCE("waterway", "natural", "landuse") AS kind,
           'openstreetmap.org' AS source,
           mz_way12 AS __geometry__,
           mz_id AS __id__

    FROM planet_osm_polygon

    WHERE
        mz_is_water = TRUE
        AND way_area::bigint > 25600 -- 4px
        AND mz_way12 && !bbox!

) AS water_areas

ORDER BY
    area DESC,
    __id__ ASC
