
CREATE TABLE "ne_110m_ocean" (
  gid serial,
  "scalerank" int2,
  "featurecla" varchar(30));
ALTER TABLE "ne_110m_ocean" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_110m_ocean','the_geom','3857','MULTIPOLYGON',2);
