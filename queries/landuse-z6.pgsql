SELECT name, area, kind, source, __geometry__, __id__

FROM
(
    --
    -- Urban Areas
    --
    SELECT
        '' AS name,
        way_area::bigint AS area,
        'urban area' AS kind,
        'naturalearthdata.com' AS source,
        the_geom AS __geometry__,
        gid AS __id__

    FROM ne_10m_urban_areas

    WHERE the_geom && !bbox!

    --
    -- Parks and Protected Lands
    --
    UNION

    SELECT
        name,
        way_area::bigint AS area,
        'park or protected land' AS kind,
        'naturalearthdata.com' AS source,
        the_geom AS __geometry__,
        gid AS __id__

    FROM ne_10m_parks_and_protected_lands

    WHERE the_geom && !bbox!

) AS land_usages
