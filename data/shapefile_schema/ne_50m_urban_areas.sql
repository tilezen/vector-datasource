
CREATE TABLE "ne_50m_urban_areas" (
  gid serial,
  "scalerank" numeric(10,0),
  "featurecla" varchar(50),
  "area_sqkm" float8);
ALTER TABLE "ne_50m_urban_areas" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_50m_urban_areas','the_geom','3857','MULTIPOLYGON',2);
