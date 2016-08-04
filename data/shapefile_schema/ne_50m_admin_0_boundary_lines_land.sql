
CREATE TABLE "ne_50m_admin_0_boundary_lines_land" (
  gid serial,
  "scalerank" numeric(10,0),
  "featurecla" varchar(32),
  "name" varchar(254));
ALTER TABLE "ne_50m_admin_0_boundary_lines_land" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_50m_admin_0_boundary_lines_land','the_geom','3857','MULTILINESTRING',2);
