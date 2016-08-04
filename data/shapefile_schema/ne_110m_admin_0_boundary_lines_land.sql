
CREATE TABLE "ne_110m_admin_0_boundary_lines_land" (
  gid serial,
  "scalerank" numeric(10,0),
  "featurecla" varchar(50),
  "name" varchar(50),
  "name_alt" varchar(50));
ALTER TABLE "ne_110m_admin_0_boundary_lines_land" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_110m_admin_0_boundary_lines_land','the_geom','3857','MULTILINESTRING',2);
