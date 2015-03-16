SELECT
    name,
    way_area::bigint AS area,
    mz_id AS __id__,
    osm_id,

    COALESCE((CASE WHEN COALESCE("building:part", building) != 'yes' THEN COALESCE("building:part", building) ELSE NULL END), amenity, shop, tourism) AS kind,

    COALESCE(mz_height,
             (CASE WHEN mz_safe_convert_to_float("building:levels") IS NULL
              THEN NULL
              ELSE GREATEST(mz_safe_convert_to_float("building:levels"), 1) * 3 + 2 END)) AS height,
    COALESCE(mz_min_height,
             (CASE WHEN mz_safe_convert_to_float("building:min_levels") IS NULL
              THEN NULL
              ELSE GREATEST(mz_safe_convert_to_float("building:min_levels"), 0) * 3 END)) AS min_height,

    "roof:color" AS roof_color,
    "roof:material" AS roof_material,
    "roof:shape" AS roof_shape,
    "roof:height" AS roof_height,
    "roof:orientation" AS roof_orientantion,

    way AS __geometry__

FROM
    planet_osm_polygon AS building_outer

WHERE
    mz_is_building_or_part = TRUE
    AND way_area::bigint > 100 -- 4px

ORDER BY
    way_area DESC,
    __id__ ASC
