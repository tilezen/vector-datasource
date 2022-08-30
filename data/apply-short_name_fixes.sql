-- These fix the short_name labels for Maryland, Massachusetts, and Texas in Daylight 1.15.
-- Maryland and Massachusetts had extra semicolon separated names while Texas was missing the tag completely

-- Maryland
update planet_osm_point set tags = tags || hstore('short_name', 'MD') where osm_id = 10900677274;
update planet_osm_point set tags = tags || hstore('short_name:en', 'MD') where osm_id = 10900677274;

-- Massachusetts
update planet_osm_point set tags = tags || hstore('short_name', 'Mass.') where osm_id = 10900677286;
update planet_osm_point set tags = tags || hstore('short_name:en', 'Mass.') where osm_id = 10900677286;

-- Texas
update planet_osm_point set tags = tags || hstore('short_name', 'Tex.') where osm_id = 11004763647;