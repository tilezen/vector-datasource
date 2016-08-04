
CREATE TABLE "ne_10m_coastline" (
  gid serial,
  "scalerank" numeric,
  "featurecla" varchar(80));
ALTER TABLE "ne_10m_coastline" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_10m_coastline','the_geom','3857','MULTILINESTRING',2);
