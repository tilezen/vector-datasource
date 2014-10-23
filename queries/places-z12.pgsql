SELECT
    name,
    place AS kind,
    way AS __geometry__,
    mz_id AS __id__

FROM planet_osm_point 

WHERE name IS NOT NULL 

AND place IN (
	'city',
	'county',
	'province',
	'town',
	'neighbourhood',
	'locality',
	'lake'
)

ORDER BY __id__ ASC
