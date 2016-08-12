
CREATE TABLE "land_polygons" (
  gid serial,
  "fid" float8);
ALTER TABLE "land_polygons" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','land_polygons','the_geom','3857','MULTIPOLYGON',2);
