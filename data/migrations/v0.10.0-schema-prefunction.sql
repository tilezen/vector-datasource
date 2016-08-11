CREATE OR REPLACE function tmp_add_col(_tbl regclass, _col text)
RETURNS integer AS $$
BEGIN
 IF NOT EXISTS (
   SELECT 1 FROM pg_attribute
   WHERE attrelid = _tbl
   AND attname = _col
   AND NOT attisdropped) THEN

   EXECUTE format('ALTER TABLE %s ADD COLUMN %s SMALLINT', _tbl, _col);
 END IF;
 RETURN 1;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE function tmp_add_col_label_placement(_tbl regclass)
RETURNS integer AS $$
BEGIN
 IF NOT EXISTS (
   SELECT 1 FROM pg_attribute
   WHERE attrelid = _tbl
   AND attname = 'mz_label_placement'
   AND NOT attisdropped) THEN

   EXECUTE format('ALTER TABLE %s ADD COLUMN mz_label_placement geometry(Geometry, 900913)', _tbl);
 END IF;
 RETURN 1;
END;
$$ LANGUAGE plpgsql;

DO $$
BEGIN
  PERFORM tmp_add_col('public.planet_osm_polygon', 'mz_earth_min_zoom');
  PERFORM tmp_add_col('public.planet_osm_line',    'mz_earth_min_zoom');
  PERFORM tmp_add_col('public.planet_osm_point',   'mz_earth_min_zoom');

  PERFORM tmp_add_col('public.ne_10m_land',  'mz_earth_min_zoom');
  PERFORM tmp_add_col('public.ne_50m_land',  'mz_earth_min_zoom');
  PERFORM tmp_add_col('public.ne_110m_land', 'mz_earth_min_zoom');

  PERFORM tmp_add_col('public.land_polygons',      'mz_earth_min_zoom');

  PERFORM tmp_add_col('public.planet_osm_polygon', 'mz_water_min_zoom');
  PERFORM tmp_add_col('public.planet_osm_line', 'mz_water_min_zoom');
  PERFORM tmp_add_col('public.planet_osm_point', 'mz_water_min_zoom');

  PERFORM tmp_add_col('public.ne_10m_coastline', 'mz_water_min_zoom');
  PERFORM tmp_add_col('public.ne_50m_coastline', 'mz_water_min_zoom');
  PERFORM tmp_add_col('public.ne_110m_coastline', 'mz_water_min_zoom');
  PERFORM tmp_add_col('public.ne_10m_ocean', 'mz_water_min_zoom');
  PERFORM tmp_add_col('public.ne_50m_ocean', 'mz_water_min_zoom');
  PERFORM tmp_add_col('public.ne_110m_ocean', 'mz_water_min_zoom');
  PERFORM tmp_add_col('public.ne_10m_lakes', 'mz_water_min_zoom');
  PERFORM tmp_add_col('public.ne_50m_lakes', 'mz_water_min_zoom');
  PERFORM tmp_add_col('public.ne_110m_lakes', 'mz_water_min_zoom');
  PERFORM tmp_add_col('public.ne_10m_playas', 'mz_water_min_zoom');
  PERFORM tmp_add_col('public.ne_50m_playas', 'mz_water_min_zoom');

  PERFORM tmp_add_col('public.water_polygons', 'mz_water_min_zoom');

  PERFORM tmp_add_col('public.planet_osm_point', 'mz_places_min_zoom');
  PERFORM tmp_add_col('public.ne_10m_populated_places', 'mz_places_min_zoom');

  PERFORM tmp_add_col('public.planet_osm_line', 'mz_boundary_min_zoom');
  PERFORM tmp_add_col('public.planet_osm_polygon', 'mz_boundary_min_zoom');

  PERFORM tmp_add_col('public.ne_110m_admin_0_boundary_lines_land', 'mz_boundary_min_zoom');
  PERFORM tmp_add_col('public.ne_50m_admin_0_boundary_lines_land', 'mz_boundary_min_zoom');
  PERFORM tmp_add_col('public.ne_50m_admin_1_states_provinces_lines', 'mz_boundary_min_zoom');
  PERFORM tmp_add_col('public.ne_10m_admin_0_boundary_lines_land', 'mz_boundary_min_zoom');
  PERFORM tmp_add_col('public.ne_10m_admin_1_states_provinces_lines', 'mz_boundary_min_zoom');

  PERFORM tmp_add_col('public.planet_osm_point', 'mz_building_min_zoom');
  PERFORM tmp_add_col('public.planet_osm_polygon', 'mz_building_min_zoom');
  PERFORM tmp_add_col('public.planet_osm_line', 'mz_landuse_min_zoom');

  PERFORM tmp_add_col('public.planet_osm_point', 'mz_earth_min_zoom');
  PERFORM tmp_add_col('public.planet_osm_polygon', 'mz_earth_min_zoom');
  PERFORM tmp_add_col('public.planet_osm_line', 'mz_earth_min_zoom');

END$$;

DO $$
BEGIN

  PERFORM tmp_add_col_label_placement('public.planet_osm_polygon');
  PERFORM tmp_add_col_label_placement('public.planet_osm_line');

  PERFORM tmp_add_col_label_placement('public.water_polygons');
  PERFORM tmp_add_col_label_placement('public.land_polygons');
  PERFORM tmp_add_col_label_placement('public.ne_110m_ocean');
  PERFORM tmp_add_col_label_placement('public.ne_50m_ocean');
  PERFORM tmp_add_col_label_placement('public.ne_10m_ocean');
  PERFORM tmp_add_col_label_placement('public.ne_110m_coastline');
  PERFORM tmp_add_col_label_placement('public.ne_50m_coastline');
  PERFORM tmp_add_col_label_placement('public.ne_10m_coastline');
  PERFORM tmp_add_col_label_placement('public.ne_110m_lakes');
  PERFORM tmp_add_col_label_placement('public.ne_50m_lakes');
  PERFORM tmp_add_col_label_placement('public.ne_10m_lakes');
  PERFORM tmp_add_col_label_placement('public.ne_50m_playas');
  PERFORM tmp_add_col_label_placement('public.ne_10m_playas');
  PERFORM tmp_add_col_label_placement('public.ne_110m_land');
  PERFORM tmp_add_col_label_placement('public.ne_50m_land');
  PERFORM tmp_add_col_label_placement('public.ne_10m_land');
  PERFORM tmp_add_col_label_placement('public.ne_50m_urban_areas');
  PERFORM tmp_add_col_label_placement('public.ne_10m_urban_areas');

END$$;

DROP FUNCTION tmp_add_col(regclass, text);
DROP FUNCTION tmp_add_col_label_placement(regclass);

DO $$
BEGIN
 IF NOT EXISTS (
   SELECT 1 FROM pg_class WHERE relname='mz_pending_path_major_route'
   ) THEN

   CREATE TABLE mz_pending_path_major_route (
     osm_id BIGINT NOT NULL
   );
 END IF;
END $$;
