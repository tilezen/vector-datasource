
CREATE TABLE "ne_110m_land" (
  gid serial,
  "featurecla" varchar(15),
  "scalerank" int2);
ALTER TABLE "ne_110m_land" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_110m_land','the_geom','3857','MULTIPOLYGON',2);
