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
        'naturalearthdata.com' AS source,
        the_geom AS __geometry__,
        gid AS __id__

    FROM ne_10m_ocean

    WHERE the_geom && !bbox!

    --
    -- Lakes
    --
    UNION

    SELECT
        name,
        way_area::bigint AS area,
        'lake' AS kind,
        'naturalearthdata.com' AS source,
        the_geom AS __geometry__,
        gid AS __id__

    FROM ne_10m_lakes

    WHERE the_geom && !bbox!

    --
    -- Playas
    --
    UNION

    SELECT
        name,
        way_area::bigint AS area,
        'playa' AS kind,
        'naturalearthdata.com' AS source,
        the_geom AS __geometry__,
        gid AS __id__

    FROM ne_10m_playas

    WHERE the_geom && !bbox!

) AS water_areas
