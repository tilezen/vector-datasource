SELECT name, area, kind, source, __geometry__, __id__

FROM
(
    --
    -- Ocean
    --
    SELECT
        '' AS name,
        way_area::bigint AS area,
        'ocean' AS kind,
        'openstreetmapdata.com' AS source,
        the_geom AS __geometry__,
        gid::varchar AS __id__,
        NULL AS osm_id

    FROM water_polygons

    WHERE the_geom && !bbox!

    --
    -- Other water areas
    --
    UNION

    SELECT
        name,
        way_area::bigint AS area,
        COALESCE("waterway", "natural", "landuse") AS kind,
        'openstreetmap.org' AS source,
        way AS __geometry__,
        mz_id AS __id__,
        osm_id

    FROM planet_osm_polygon

    WHERE
        mz_is_water = TRUE
        AND way_area::bigint > 100 -- 4px
        AND way && !bbox!

    --
    -- Water line geometries
    --
    UNION

    SELECT
        name,
        NULL AS area,
        waterway AS kind,
        'openstreetmap.org' AS source,
        way AS __geometry__,
        mz_id AS __id__,
        osm_id

    FROM planet_osm_line

    WHERE
        waterway IN ('canal', 'dam', 'river', 'stream')
        AND way && !bbox!

) AS water_areas

ORDER BY
    area DESC,
    __id__ ASC
