
CREATE TABLE "ne_50m_ocean" (
  gid serial,
  "scalerank" numeric(10,0),
  "featurecla" varchar(32));
ALTER TABLE "ne_50m_ocean" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_50m_ocean','the_geom','3857','MULTIPOLYGON',2);
