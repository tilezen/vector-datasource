
CREATE TABLE "ne_10m_lakes" (
  gid serial,
  "featurecla" varchar(32),
  "scalerank" numeric(10,0),
  "name" varchar(254),
  "name_abb" varchar(25),
  "name_alt" varchar(254),
  "note" varchar(100),
  "delta" varchar(100),
  "dam_name" varchar(254),
  "year" int4,
  "admin" varchar(50));
ALTER TABLE "ne_10m_lakes" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_10m_lakes','the_geom','3857','MULTIPOLYGON',2);
