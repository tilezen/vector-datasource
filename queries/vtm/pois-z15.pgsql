SELECT name,
       COALESCE("aerialway", "aeroway", "amenity", "barrier", "highway",
                "lock", "man_made", "natural", "power", "railway", "tourism",
                "waterway") AS kind,
       way AS __geometry__,
       mz_id AS __id__,
       "aerialway", "aeroway", "amenity", "barrier", "highway",
       "lock", "man_made", "natural", "power", "railway", "tourism",
       "waterway"

FROM planet_osm_point

WHERE
    mz_poi_level <= 15
