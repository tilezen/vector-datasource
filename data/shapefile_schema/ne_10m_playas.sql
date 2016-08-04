
CREATE TABLE "ne_10m_playas" (
  gid serial,
  "scalerank" numeric(10,0),
  "featurecla" varchar(30),
  "name" varchar(100),
  "name_abb" varchar(254),
  "name_alt" varchar(254),
  "note" varchar(100));
ALTER TABLE "ne_10m_playas" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_10m_playas','the_geom','3857','MULTIPOLYGON',2);
