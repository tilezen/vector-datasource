
CREATE TABLE "ne_50m_admin_1_states_provinces_lines" (
  gid serial,
  "objectid" int4,
  "scalerank" numeric,
  "featurecla" varchar(32));
ALTER TABLE "ne_50m_admin_1_states_provinces_lines" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_50m_admin_1_states_provinces_lines','the_geom','3857','MULTILINESTRING',2);
