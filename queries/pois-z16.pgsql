SELECT name,
       COALESCE("aerialway", "aeroway", "amenity", "barrier", "highway", "historic",
                "lock", "man_made", "natural", "power", "railway", "shop", "tourism",
                "waterway") AS kind,
       way AS __geometry__,
       mz_id AS __id__

FROM planet_osm_point

WHERE
    mz_poi_level <= 16
