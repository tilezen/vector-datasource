
CREATE TABLE "water_polygons" (
  gid serial,
  "fid" float8);
ALTER TABLE "water_polygons" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','water_polygons','the_geom','3857','MULTIPOLYGON',2);
