
CREATE TABLE "ne_50m_lakes" (
  gid serial,
  "scalerank" numeric(10,0),
  "featurecla" varchar(32),
  "name" varchar(254),
  "name_alt" varchar(254),
  "note" varchar(100),
  "admin" varchar(50));
ALTER TABLE "ne_50m_lakes" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_50m_lakes','the_geom','3857','MULTIPOLYGON',2);
