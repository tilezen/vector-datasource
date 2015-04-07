SELECT
    name,
    place AS kind,
    way AS __geometry__,
    osm_id AS __id__,
    admin_level

FROM planet_osm_point

WHERE name IS NOT NULL

AND place IN (
    'state',
    'city',
    'district',
    'county',
    'province',
    'island'
)
