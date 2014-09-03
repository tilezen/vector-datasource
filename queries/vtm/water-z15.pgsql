SELECT name, area, kind, waterway, "natural", landuse, source, __geometry__, __id__

FROM
(
    --
    -- Ocean
    --
    SELECT '' AS name,
           way_area::bigint AS area,
           'ocean' AS kind,
           'ocean' AS waterway,
           'water' AS natural,
           NULL AS landuse,
           'openstreetmapdata.com' AS source,
           the_geom AS __geometry__,
           gid::varchar AS __id__

    FROM water_polygons

    WHERE the_geom && !bbox!

    --
    -- Other water areas
    --
    UNION

    SELECT name,
           way_area::bigint AS area,
           COALESCE("waterway", "natural", "landuse") AS kind,
           "waterway",
           "natural",
           "landuse",
           'openstreetmap.org' AS source,
           way AS __geometry__,
           mz_id AS __id__

    FROM planet_osm_polygon

    WHERE
        mz_is_water = TRUE
        AND way_area::bigint > 100 -- 4px
        AND way && !bbox!

) AS water_areas
