SELECT
    gid AS __id__,
    the_geom AS __geometry__,
    'naturalearthdata.com' AS source,
    name,
    namealt,
    namealtt,
    featurecla AS kind,
    scalerank::float,
    labelrank,
    level,
    type

FROM ne_10m_roads

WHERE scalerank <= 7
