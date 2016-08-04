
CREATE TABLE "ne_110m_coastline" (
  gid serial,
  "scalerank" numeric(10,0),
  "featurecla" varchar(12));
ALTER TABLE "ne_110m_coastline" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_110m_coastline','the_geom','3857','MULTILINESTRING',2);
