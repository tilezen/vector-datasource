SELECT
    name,
    way_area::bigint AS area,
    osm_id AS __id__,
    "building:part",
    building,
    amenity,
    shop,
    tourism,
    "building:levels",
    "building:min_levels",
    height,
    min_height,
    "addr:housenumber" AS addr_housenumber,
    "addr:street" AS addr_street,
    "roof:color" AS roof_color,
    "roof:material" AS roof_material,
    "roof:shape" AS roof_shape,
    "roof:height" AS roof_height,
    "roof:orientation" AS roof_orientation,
    way AS __geometry__

FROM
    planet_osm_polygon

WHERE
    mz_calculate_is_building_or_part(building, "building:part") = TRUE
