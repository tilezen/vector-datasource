SELECT 
	name, 
	place, 
	way AS __geometry__ 

FROM planet_osm_point 

WHERE name IS NOT NULL 

AND place IN (
	'country',
	'state',
	'island',
	'islet',
	'gulf',
	'sea',
	'bay',
	'ocean'
)