
CREATE TABLE "buffered_land" (
  gid serial,
  "featurecla" varchar(32),
  "scalerank" numeric);
ALTER TABLE "buffered_land" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','buffered_land','the_geom','3857','MULTIPOLYGON',2);
