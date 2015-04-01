SELECT
    'base' AS land,
    the_geom AS __geometry__,
    gid::varchar AS __id__
FROM
    ne_110m_land
