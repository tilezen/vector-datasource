SELECT name, 
	boundary, 
	admin_level, 
	way AS __geometry__ 
FROM planet_osm_polygon 
WHERE boundary='administrative' AND admin_level IN ('2','3') -- national, disputed