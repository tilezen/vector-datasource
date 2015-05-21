SELECT
    'base' AS land,
    st_union(the_geom) AS __geometry__,
    max(gid) AS __id__
FROM
    ne_10m_land
WHERE
    the_geom && !bbox!
