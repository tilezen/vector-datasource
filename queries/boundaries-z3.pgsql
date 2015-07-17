SELECT __id__, __geometry__, scalerank, kind, type
FROM
(
    SELECT
        gid AS __id__,
        the_geom AS __geometry__,
        scalerank::float,
        featurecla AS kind,
        'country' AS type
    FROM
        ne_50m_admin_0_boundary_lines_land
    WHERE the_geom && !bbox!

    UNION

    SELECT
        gid AS __id__,
        the_geom AS __geometry__,
        scalerank::float,
        featurecla AS kind,
        'state' AS type
    FROM
        ne_50m_admin_1_states_provinces_lines
    WHERE the_geom && !bbox!
) AS boundaries
