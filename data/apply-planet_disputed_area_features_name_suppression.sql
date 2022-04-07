-- Script to delete names from certain disputed locations after osm2pgsql import.
-- The "bbox" query creates polygon geometries to define which areas to select for name removal
-- The "suppress" query selects features from the planet table that are fully within a "bbox" polygon
-- The "update" query then deletes any key value pair within the selection with "name" somewhere in the key's string.

with bbox as
    (select *
    from (values
        (st_transform(st_geomfromtext('POLYGON ((-78.89 15.59,-78.89 16.12,-78.30 16.12,-78.30 15.59,-78.89 15.59))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((-80.15 15.50,-80.15 16.05,-79.54 16.05,-79.54 15.50,-80.15 15.50))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((39.28 -21.82,39.28 -21.14,40.09 -21.14,40.09 -21.82,39.28 -21.82))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((-63.73 15.55,-63.737 15.79,-63.500 15.79,-63.500 15.55,-63.73 15.55))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((131.52 36.97,131.52 37.49,132.21 37.49,132.21 36.97,131.52 36.97))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((40.05 -22.65,40.05 -22.07,40.68 -22.07,40.69 -22.65,40.05 -22.65))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((47.01 -11.86,47.01 -11.2,47.66 -11.2,47.66 -11.86,47.01 -11.86))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((-3.90 35.21,-3.90 35.21,-3.89 35.21,-3.89 35.21,-3.90 35.21))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((-3.90 35.21,-3.90 35.2,-3.90 35.2,-3.90 35.21,-3.90 35.21))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((-3.89 35.21,-3.89 35.21,-3.88 35.21,-3.88 35.21,-3.89 35.21))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((-2.44 35.17,-2.44 35.18,-2.41 35.18,-2.41 35.17,-2.44 35.17))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((-5.42 35.9,-5.42 35.9,-5.414 35.9,-5.41 35.9,-5.42 35.9))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((54.99 25.83,54.99 25.91,55.08 25.91,55.08 25.83,54.99 25.83))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((166.33 19.01,166.33 19.55,166.96 19.55,166.96 19.01,166.33 19.01))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((54.26 -16.14,54.26 -15.6,54.78 -15.6,54.785 -16.14,54.26 -16.14))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((-171.33 -11.30,-171.33 -10.80,-170.81 -10.80,-170.81 -11.30,-171.33 -11.30))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((110.58 7.31,110.58 10.23,116.2 10.23,116.2 7.31,110.58 7.31))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((113.20 9.39,113.20 11.95,116.28 11.95,116.28 9.39,113.20 9.39))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((117.4 14.8,117.4 15.49,118.11 15.49,118.11 14.8,117.4 14.8))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((-88.37 16.05,-88.37 16.22,-88.20 16.22,-88.20 16.05,-88.37 16.05))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((123.3 25.66,123.3 25.99,123.81 25.99,123.81 25.66,123.3 25.66))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((110.81 15.35,110.81 17.41,113.28 17.41,113.28 15.35,110.81 15.35))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((-75.262 18.16,-75.262 18.64,-74.7 18.64,-74.7 18.16,-75.262 18.16))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((9.37 0.80,9.37 0.81,9.38 0.81,9.38 0.80,9.37 0.80))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((171.08 -22.78,171.08 -22.05,172.36 -22.05,172.36 -22.78,171.08 -22.78))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((42.43 -17.31,42.43 -16.79,43.03 -16.79,43.03 -17.31,42.43 -17.31))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((-66.50 80.81,-66.50 80.8,-66.39 80.8,-66.39 80.81,-66.50 80.81))', 4326), 3857)),
        (st_transform(st_geomfromtext('POLYGON ((149.31 45.25, 148.51 46.28, 145.16 43.85, 146.08 43.21, 149.31 45.25))', 4326), 3857))
   ) as b (geom)),

 suppress_point as
     (select *
      from planet_osm_point l,
           bbox
      where st_within(l.way, bbox.geom)),

 update_point as
     (update planet_osm_point p
         set tags = delete(p.tags, (select array_agg(key) from (select distinct skeys(tags) as key from suppress_point) a where key like '%name%'))
         from suppress_point s
         where s.osm_id = p.osm_id),

 suppress_line as
     (select *
      from planet_osm_line l,
           bbox
      where st_within(l.way, bbox.geom)),

 update_line as
     (update planet_osm_line p
         set tags = delete(p.tags, (select array_agg(key) from (select distinct skeys(tags) as key from suppress_line) a where key like '%name%'))
         from suppress_line s
         where s.osm_id = p.osm_id),

 suppress_polygon as
     (select *
      from planet_osm_polygon l,
           bbox
      where st_within(l.way, bbox.geom)),

 update_polygon as
     (update planet_osm_polygon p
         set tags = delete(p.tags, (select array_agg(key) from (select distinct skeys(tags) as key from suppress_polygon) a where key like '%name%'))
         from suppress_polygon s
         where s.osm_id = p.osm_id),

 suppress_roads as
     (select *
      from planet_osm_roads l,
           bbox
      where st_within(l.way, bbox.geom))

update planet_osm_roads p
set tags = delete(p.tags, (select array_agg(key) from (select distinct skeys(tags) as key from suppress_roads) a where key like '%name%'))
from suppress_roads s
where s.osm_id = p.osm_id
