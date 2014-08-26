SELECT name,
       COALESCE("aeroway") AS kind,
       way AS __geometry__,
       osm_id AS __id__,
       "aeroway"

FROM planet_osm_point

WHERE
    mz_poi_level <= 9
