SELECT name, area, kind, source, __geometry__, __id__, tags

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
        gid AS __id__,
        NULL AS tags

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
        osm_id AS __id__,
        %#tags AS tags

    FROM planet_osm_polygon

    WHERE
        mz_calculate_is_water("waterway", "natural", "landuse") = TRUE
        AND way_area::bigint > 1600 -- 4px
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
        osm_id AS __id__,
        %#tags AS tags

    FROM planet_osm_line

    WHERE
        waterway IN ('canal', 'dam', 'river', 'stream')
        AND way && !bbox!

) AS water_areas
