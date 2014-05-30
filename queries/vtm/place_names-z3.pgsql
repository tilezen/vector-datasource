SELECT 
	name, 
	place, 
	way AS __geometry__ 

FROM planet_osm_point 

WHERE name IS NOT NULL 

AND place IN (
	'ocean', 
	'country',
	'state',
	'island',
	'gulf',
	'sea',
	'bay',
	'archipelago'
)