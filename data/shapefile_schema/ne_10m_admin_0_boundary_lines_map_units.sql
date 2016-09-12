
CREATE TABLE "ne_10m_admin_0_boundary_lines_map_units" (
  gid serial,
  "fid_ne_10m" int4,
  "scalerank" numeric,
  "featurecla" varchar(32),
  "comment" varchar(100),
  "adm0_a3" varchar(3),
  "adm0_name" varchar(100),
  "mapcolor9" int2);
ALTER TABLE "ne_10m_admin_0_boundary_lines_map_units" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_10m_admin_0_boundary_lines_map_units','the_geom','3857','MULTILINESTRING',2);
