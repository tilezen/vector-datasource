SELECT __id__, __geometry__, name, type, scalerank, kind, labelrank
FROM
(
    SELECT
        gid AS __id__,
        the_geom AS __geometry__,
        name,
        'country' AS type,
        scalerank::float,
        featurecla AS kind,
        labelrank
    FROM
        ne_10m_admin_0_boundary_lines_land
    WHERE the_geom && !bbox!

    UNION

    SELECT
        gid AS __id__,
        the_geom AS __geometry__,
        name,
        'state' AS type,
        scalerank::float,
        featurecla AS kind,
        NULL AS labelrank
    FROM
        ne_10m_admin_1_states_provinces_lines
    WHERE the_geom && !bbox!

) AS boundaries
