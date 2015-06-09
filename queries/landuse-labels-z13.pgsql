SELECT
    name,
    way_area::bigint AS area,
    COALESCE("landuse", "leisure", "natural", "highway", "aeroway", "amenity") AS kind,
    'openstreetmap.org' AS source,
    mz_centroid AS __geometry__,
    osm_id AS __id__,
    %#tags AS tags

FROM planet_osm_polygon

WHERE
    mz_is_landuse = TRUE
    AND way_area::bigint > 1600 -- 4px
    AND name IS NOT NULL
