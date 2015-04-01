SELECT
    name,
    COALESCE("aerialway", "aeroway", "amenity", "barrier", "highway",
             "lock", "man_made", "natural", "power", "railway", "tourism",
             "waterway") AS kind,
    way AS __geometry__,
    osm_id::text AS __id__,
    osm_id

FROM planet_osm_point

WHERE
    mz_calculate_poi_level(
        "aerialway",
        "aeroway",
        "amenity",
        "barrier",
        "highway",
        "historic",
        "leisure",
        "lock",
        "man_made",
        "natural",
        "power",
        "railway",
        "shop",
        "tourism",
        "waterway"
    ) <= 15
