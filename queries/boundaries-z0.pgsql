SELECT
    gid AS __id__,
    the_geom AS __geometry__,
    scalerank::float,
    featurecla AS kind,
    'country' AS type
FROM
    ne_110m_admin_0_boundary_lines_land
