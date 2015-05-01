SELECT name, kind, source, __geometry__, __id__, admin_level, scalerank, labelrank, population

FROM
(

    -- Natural Earth
    SELECT
        name,
        featurecla AS kind,
        'naturalearthdata.com' AS source,
        the_geom AS __geometry__,
        gid AS __id__,

        NULL as admin_level,

        scalerank,
        labelrank,
        pop_max AS population

    FROM ne_10m_populated_places

    WHERE
        scalerank <= 6
        AND the_geom && !bbox!

    UNION

    -- OSM
    SELECT
        name,
        place AS kind,
        'openstreetmap' AS source,
        way AS __geometry__,
        osm_id AS __id__,

        admin_level,

        NULL AS scalerank,
        NULL AS labelrank,
        NULL AS population

    FROM planet_osm_point

    WHERE
        name IS NOT NULL
        AND place IN (
            'continent',
            'ocean',
            'country',
            'sea',
            'state',
            'province'
        )
        AND way && !bbox!

) AS places
