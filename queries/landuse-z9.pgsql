SELECT
    name,
    way_area::bigint AS area,
    COALESCE("landuse", "leisure", "natural", "highway", "aeroway", "amenity") AS kind,
    'openstreetmap.org' AS source,
    way AS __geometry__,
    osm_id AS __id__

FROM planet_osm_polygon

WHERE
    mz_calculate_is_landuse("landuse", "leisure", "natural", "highway", "amenity", "aeroway") = TRUE
    AND way_area::bigint > 409600 -- 4px
