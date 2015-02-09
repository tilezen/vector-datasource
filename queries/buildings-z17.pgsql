SELECT
    name,
    way_area::bigint AS area,
    mz_id AS __id__,

    COALESCE((CASE WHEN COALESCE("building:part", building) != 'yes' THEN COALESCE("building:part", building) ELSE NULL END), amenity, shop, tourism) AS kind,

    COALESCE(mz_height, GREATEST(mz_safe_convert_to_float("building:levels"), 1) * 3 + 2) AS height,
    COALESCE(mz_min_height, GREATEST(mz_safe_convert_to_float("building:min_levels"), 0) * 3) AS min_height,

    way AS __geometry__

FROM
    planet_osm_polygon AS building_outer

WHERE
    mz_is_building_or_part = TRUE

ORDER BY
    way_area DESC,
    __id__ ASC
