SELECT
    name,
    COALESCE("aeroway") AS kind,
    way AS __geometry__,
    osm_id AS __id__

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
    ) <= 9
