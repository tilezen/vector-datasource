
CREATE TABLE "ne_50m_coastline" (
  gid serial,
  "scalerank" numeric(10,0),
  "featurecla" varchar(32));
ALTER TABLE "ne_50m_coastline" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_50m_coastline','the_geom','3857','MULTILINESTRING',2);
