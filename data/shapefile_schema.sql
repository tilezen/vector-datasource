-- create tables matching the schema of the static asset shapefiles.
--
-- this is an edited version of the output of:
--
-- ```
-- mkdir shapefiles; cd shapefiles/
-- tar zxf ../shapefiles.tar.gz
-- for i in *.zip; do unzip $i; done
-- for i in `find . -name "*.shp"`; do
--   j=`echo $i | sed "s,.*/,,;s,-merc,,;s,\.shp\$,,"`
--   shp2pgsql -p -s 3857 -W Windows-1252 -g the_geom $i $j >> shape_tables.sql
-- done
-- ```

BEGIN;

CREATE TABLE "ne_10m_ocean" (
  gid serial,
  "featurecla" varchar(32),
  "scalerank" int2);
ALTER TABLE "ne_10m_ocean" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_10m_ocean','the_geom','3857','MULTIPOLYGON',2);

CREATE TABLE "buffered_land" (
  gid serial,
  "featurecla" varchar(32),
  "scalerank" numeric);
ALTER TABLE "buffered_land" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','buffered_land','the_geom','3857','MULTIPOLYGON',2);

CREATE TABLE "ne_50m_coastline" (
  gid serial,
  "scalerank" numeric(10,0),
  "featurecla" varchar(32));
ALTER TABLE "ne_50m_coastline" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_50m_coastline','the_geom','3857','MULTILINESTRING',2);

CREATE TABLE "ne_110m_coastline" (
  gid serial,
  "scalerank" numeric(10,0),
  "featurecla" varchar(12));
ALTER TABLE "ne_110m_coastline" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_110m_coastline','the_geom','3857','MULTILINESTRING',2);

CREATE TABLE "ne_110m_admin_0_boundary_lines_land" (
  gid serial,
  "scalerank" numeric(10,0),
  "featurecla" varchar(50),
  "name" varchar(50),
  "name_alt" varchar(50));
ALTER TABLE "ne_110m_admin_0_boundary_lines_land" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_110m_admin_0_boundary_lines_land','the_geom','3857','MULTILINESTRING',2);

CREATE TABLE "ne_110m_land" (
  gid serial,
  "featurecla" varchar(15),
  "scalerank" int2);
ALTER TABLE "ne_110m_land" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_110m_land','the_geom','3857','MULTIPOLYGON',2);

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

CREATE TABLE "water_polygons" (
  gid serial,
  "fid" float8);
ALTER TABLE "water_polygons" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','water_polygons','the_geom','3857','MULTIPOLYGON',2);

CREATE TABLE "land_polygons" (
  gid serial,
  "fid" float8);
ALTER TABLE "land_polygons" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','land_polygons','the_geom','3857','MULTIPOLYGON',2);

CREATE TABLE "ne_10m_roads" (
  gid serial,
  "scalerank" numeric(10,0),
  "featurecla" varchar(30),
  "type" varchar(50),
  "sov_a3" varchar(3),
  "note" varchar(50),
  "edited" varchar(50),
  "name" varchar(25),
  "namealt" varchar(25),
  "namealtt" varchar(30),
  "routeraw" varchar(50),
  "question" numeric(10,0),
  "length_km" int4,
  "toll" int2,
  "ne_part" varchar(50),
  "label" varchar(50),
  "label2" varchar(50),
  "local" varchar(30),
  "localtype" varchar(30),
  "localalt" varchar(30),
  "labelrank" int2,
  "ignore" int2,
  "add" int2,
  "rwdb_rd_id" int4,
  "orig_fid" int4,
  "prefix" varchar(5),
  "uident" int4,
  "continent" varchar(50),
  "expressway" int2,
  "level" varchar(50));
ALTER TABLE "ne_10m_roads" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_10m_roads','the_geom','3857','MULTILINESTRING',2);

CREATE TABLE "ne_10m_urban_areas" (
  gid serial,
  "scalerank" numeric(10,0),
  "featurecla" varchar(50),
  "area_sqkm" float8);
ALTER TABLE "ne_10m_urban_areas" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_10m_urban_areas','the_geom','3857','MULTIPOLYGON',2);

CREATE TABLE "ne_110m_lakes" (
  gid serial,
  "scalerank" numeric(10,0),
  "featurecla" varchar(32),
  "name" varchar(254),
  "name_alt" varchar(254),
  "admin" varchar(50));
ALTER TABLE "ne_110m_lakes" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_110m_lakes','the_geom','3857','MULTIPOLYGON',2);

CREATE TABLE "ne_10m_populated_places" (
  gid serial,
  "scalerank" int2,
  "natscale" int2,
  "labelrank" int2,
  "featurecla" varchar(50),
  "name" varchar(100),
  "namepar" varchar(254),
  "namealt" varchar(254),
  "diffascii" int2,
  "nameascii" varchar(100),
  "adm0cap" numeric,
  "capalt" numeric,
  "capin" varchar(15),
  "worldcity" numeric,
  "megacity" int2,
  "sov0name" varchar(100),
  "sov_a3" varchar(3),
  "adm0name" varchar(50),
  "adm0_a3" varchar(3),
  "adm1name" varchar(50),
  "iso_a2" varchar(5),
  "note" varchar(254),
  "latitude" numeric,
  "longitude" numeric,
  "changed" numeric,
  "namediff" int2,
  "diffnote" varchar(254),
  "pop_max" int4,
  "pop_min" int4,
  "pop_other" int4,
  "rank_max" int4,
  "rank_min" int4,
  "geonameid" numeric,
  "meganame" varchar(50),
  "ls_name" varchar(41),
  "ls_match" int2,
  "checkme" int2,
  "max_pop10" numeric,
  "max_pop20" numeric,
  "max_pop50" numeric,
  "max_pop300" numeric,
  "max_pop310" numeric,
  "max_natsca" numeric,
  "min_areakm" numeric,
  "max_areakm" numeric,
  "min_areami" numeric,
  "max_areami" numeric,
  "min_perkm" numeric,
  "max_perkm" numeric,
  "min_permi" numeric,
  "max_permi" numeric,
  "min_bbxmin" numeric,
  "max_bbxmin" numeric,
  "min_bbxmax" numeric,
  "max_bbxmax" numeric,
  "min_bbymin" numeric,
  "max_bbymin" numeric,
  "min_bbymax" numeric,
  "max_bbymax" numeric,
  "mean_bbxc" numeric,
  "mean_bbyc" numeric,
  "compare" int2,
  "gn_ascii" varchar(254),
  "feature_cl" varchar(254),
  "feature_co" varchar(254),
  "admin1_cod" numeric,
  "gn_pop" numeric,
  "elevation" numeric,
  "gtopo30" numeric,
  "timezone" varchar(254),
  "geonamesno" varchar(100),
  "un_fid" int4,
  "un_adm0" varchar(254),
  "un_lat" numeric,
  "un_long" numeric,
  "pop1950" numeric,
  "pop1955" numeric,
  "pop1960" numeric,
  "pop1965" numeric,
  "pop1970" numeric,
  "pop1975" numeric,
  "pop1980" numeric,
  "pop1985" numeric,
  "pop1990" numeric,
  "pop1995" numeric,
  "pop2000" numeric,
  "pop2005" numeric,
  "pop2010" numeric,
  "pop2015" numeric,
  "pop2020" numeric,
  "pop2025" numeric,
  "pop2050" numeric,
  "cityalt" varchar(50));
ALTER TABLE "ne_10m_populated_places" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_10m_populated_places','the_geom','3857','POINT',2);

CREATE TABLE "ne_50m_admin_1_states_provinces_lines" (
  gid serial,
  "objectid" int4,
  "scalerank" numeric,
  "featurecla" varchar(32));
ALTER TABLE "ne_50m_admin_1_states_provinces_lines" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_50m_admin_1_states_provinces_lines','the_geom','3857','MULTILINESTRING',2);

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

CREATE TABLE "ne_10m_coastline" (
  gid serial,
  "scalerank" numeric,
  "featurecla" varchar(80));
ALTER TABLE "ne_10m_coastline" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_10m_coastline','the_geom','3857','MULTILINESTRING',2);

CREATE TABLE "ne_50m_ocean" (
  gid serial,
  "scalerank" numeric(10,0),
  "featurecla" varchar(32));
ALTER TABLE "ne_50m_ocean" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_50m_ocean','the_geom','3857','MULTIPOLYGON',2);

CREATE TABLE "ne_50m_land" (
  gid serial,
  "scalerank" numeric(10,0),
  "featurecla" varchar(32));
ALTER TABLE "ne_50m_land" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_50m_land','the_geom','3857','MULTIPOLYGON',2);

CREATE TABLE "ne_110m_ocean" (
  gid serial,
  "scalerank" int2,
  "featurecla" varchar(30));
ALTER TABLE "ne_110m_ocean" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_110m_ocean','the_geom','3857','MULTIPOLYGON',2);

CREATE TABLE "ne_10m_land" (
  gid serial,
  "featurecla" varchar(32),
  "scalerank" int2);
ALTER TABLE "ne_10m_land" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_10m_land','the_geom','3857','MULTIPOLYGON',2);

CREATE TABLE "ne_50m_playas" (
  gid serial,
  "scalerank" numeric(10,0),
  "featurecla" varchar(32),
  "name" varchar(254),
  "name_alt" varchar(254),
  "note" varchar(100));
ALTER TABLE "ne_50m_playas" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_50m_playas','the_geom','3857','MULTIPOLYGON',2);

CREATE TABLE "ne_50m_urban_areas" (
  gid serial,
  "scalerank" numeric(10,0),
  "featurecla" varchar(50),
  "area_sqkm" float8);
ALTER TABLE "ne_50m_urban_areas" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_50m_urban_areas','the_geom','3857','MULTIPOLYGON',2);

CREATE TABLE "ne_50m_admin_0_boundary_lines_land" (
  gid serial,
  "scalerank" numeric(10,0),
  "featurecla" varchar(32),
  "name" varchar(254));
ALTER TABLE "ne_50m_admin_0_boundary_lines_land" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_50m_admin_0_boundary_lines_land','the_geom','3857','MULTILINESTRING',2);

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

CREATE TABLE "ne_10m_parks_and_protected_lands" (
  gid serial,
  "unit_code" varchar(10),
  "unit_name" varchar(254),
  "unit_type" varchar(254),
  "nps_region" varchar(128),
  "scalerank" numeric(10,0),
  "featurecla" varchar(30),
  "note" varchar(50),
  "name" varchar(100));
ALTER TABLE "ne_10m_parks_and_protected_lands" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('','ne_10m_parks_and_protected_lands','the_geom','3857','MULTIPOLYGON',2);

COMMIT;
