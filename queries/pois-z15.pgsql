SELECT
    name,
    COALESCE("aerialway", "aeroway", "amenity", "barrier", "highway",
             "lock", "man_made", "natural", "power", "railway", "tourism",
             "waterway") AS kind,
    way AS __geometry__,
    mz_id AS __id__,
    osm_id

FROM planet_osm_point

WHERE
    mz_poi_level <= 15

ORDER BY __id__ ASC
