SELECT
    name,
    way_area::bigint AS area,
    mz_id AS __id__,

    COALESCE((CASE WHEN building != 'yes' THEN building ELSE NULL END), amenity, shop, tourism) AS kind,

    COALESCE(mz_height, GREATEST(mz_safe_convert_to_float("building:levels"), 1) * 3 + 2) AS height,
    COALESCE(mz_min_height, GREATEST(mz_safe_convert_to_float("building:min_levels"), 0) * 3) AS min_height,

    mz_way14 AS __geometry__

FROM
    planet_osm_polygon

WHERE
    building IS NOT NULL
    AND way_area::bigint > 100

ORDER BY
    way_area DESC,
    __id__ ASC
