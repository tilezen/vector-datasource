
CREATE TABLE "ne_10m_land" (
  gid serial,
  "featurecla" varchar(32),
  "scalerank" int2);
ALTER TABLE "ne_10m_land" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_10m_land','the_geom','3857','MULTIPOLYGON',2);
