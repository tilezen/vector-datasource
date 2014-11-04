SELECT
    name,
    mz_id AS __id__,

    COALESCE((CASE WHEN COALESCE("building:part", building) != 'yes' THEN COALESCE("building:part", building) ELSE NULL END), amenity, shop) AS kind,

    mz_height AS height,
    mz_min_height AS min_height,

    way AS __geometry__

FROM
    planet_osm_polygon AS building_outer

WHERE
    mz_is_building_or_part = TRUE
    AND way_area::bigint > 100 -- 4px

ORDER BY
    way_area DESC,
    __id__ ASC
