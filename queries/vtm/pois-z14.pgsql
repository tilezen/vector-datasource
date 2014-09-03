SELECT name,
       COALESCE("aerialway", "aeroway", "natural", "railway", "tourism") AS kind,
       way AS __geometry__,
       mz_id AS __id__,
       "aerialway", "aeroway", "natural", "railway", "tourism"

FROM planet_osm_point

WHERE
    mz_poi_level <= 14
