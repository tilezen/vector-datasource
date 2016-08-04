
CREATE TABLE "ne_10m_admin_0_boundary_lines_land" (
  gid serial,
  "fid_ne_10m" int4,
  "scalerank" numeric,
  "featurecla" varchar(32),
  "note_" varchar(32),
  "name" varchar(100),
  "comment" varchar(100),
  "adm0_usa" int2,
  "adm0_left" varchar(100),
  "adm0_right" varchar(100),
  "adm0_a3_l" varchar(3),
  "adm0_a3_r" varchar(3),
  "sov_a3_l" varchar(3),
  "sov_a3_r" varchar(3),
  "type" varchar(50),
  "labelrank" int2);
ALTER TABLE "ne_10m_admin_0_boundary_lines_land" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_10m_admin_0_boundary_lines_land','the_geom','3857','MULTILINESTRING',2);
