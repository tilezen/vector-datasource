SELECT name,
       COALESCE("aeroway", "natural", "railway") AS kind,
       way AS __geometry__,
       mz_id AS __id__

FROM planet_osm_point

WHERE
    mz_poi_level <= 12
