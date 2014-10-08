SELECT
    name,
    COALESCE("historic", "amenity", "landuse", "tourism", "railway") AS kind,
    TRUE AS haunted,
    way AS __geometry__,
    mz_id AS __id__

FROM planet_osm_point 

WHERE name IS NOT NULL 

AND (
	landuse = 'cemetery'
	OR amenity IN (
		'grave_yard',
		'crematorium'
	)
	OR historic IN (
		'tomb',
		'castle',
		'archaeological_site',
		'ruins'
	)
	OR tourism = 'museum'
	OR railway = 'abandoned'
)