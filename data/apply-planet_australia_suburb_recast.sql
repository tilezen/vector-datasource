-- Suburbs in Australia are treated more like cities, so this recasts them to place=town.

with bounds as
         (select *
          from (values
                    (st_transform(st_geomfromtext('Polygon ((116.16 -14.31, 104.29 -22.95, 113.34 -38.30, 155.33 -47.28, 156.30 -21.83, 144.91 -9.41, 127.14 -9.73, 116.16 -14.31))', 4326), 3857))
               ) as b (geom)),

     suburb as
         (select *
          from planet_osm_point l where tags->'place'='suburb'),

     selection as
         (select * from suburb,
                        bounds
          where st_within(way, geom)),

-- These cities are already present in OSM as place=city so we don't want to show any locality point that could cause duplicates
     trim_major_cities as
        (select * from selection
            where tags->'name' not in (
                'Adelaide'
                'Brisbane',
                'Melbourne,',
                'Perth',
                'Sydney')
        )

update planet_osm_point p
set tags = p.tags || hstore('place', 'town')
from trim_major_cities s
where s.osm_id = p.osm_id