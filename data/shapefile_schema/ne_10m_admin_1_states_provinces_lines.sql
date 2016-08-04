
CREATE TABLE "ne_10m_admin_1_states_provinces_lines" (
  gid serial,
  "objectid" int4,
  "fid_ne_10m" int4,
  "scalerank" numeric,
  "featurecla" varchar(32),
  "name" varchar(100),
  "adm0_a3" varchar(3),
  "adm0_name" varchar(100),
  "shape_leng" numeric,
  "mapcolor13" int2,
  "mapcolor9" int2,
  "sov_a3" varchar(3),
  "name_l" varchar(100),
  "name_r" varchar(100),
  "name_alt_l" varchar(200),
  "name_alt_r" varchar(200),
  "name_loc_l" varchar(200),
  "name_loc_r" varchar(200),
  "name_len_l" int2,
  "name_len_r" int2,
  "note" varchar(100),
  "type" varchar(50));
ALTER TABLE "ne_10m_admin_1_states_provinces_lines" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_10m_admin_1_states_provinces_lines','the_geom','3857','MULTILINESTRING',2);
