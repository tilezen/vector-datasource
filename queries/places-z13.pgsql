SELECT 
	name, 
	place, 
	way AS __geometry__ 

FROM planet_osm_point 

WHERE name IS NOT NULL 

AND place IN (
	'city',
	'hamlet',
	'district',
	'county',
	'region',
	'province',
	'village',
	'district',
	'isolated_dwelling',
	'town',
	'suburb',
	'quarter',
	'neighbourhood',
	'locality',
	'borough',
	'allotments',
	'cape',
	'island',
	'islet',
	'gulf',
	'sea',
	'bay',
	'ocean',
	'lake',
	'reservoir',
	'pond',
	'glacier'
)