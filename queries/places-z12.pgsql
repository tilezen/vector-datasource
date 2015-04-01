SELECT
    name,
    place AS kind,
    way AS __geometry__,
    osm_id::text AS __id__,
    osm_id,
    admin_level

FROM planet_osm_point

WHERE name IS NOT NULL

AND place IN (
    'city',
    'county',
    'province',
    'island',
    'town',
    'neighbourhood',
    'suburb',
    'locality',
    'lake',
    'village',
    'hamlet',
    'isolated_dwelling'
)
