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

DO $$
BEGIN
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
END$$;

DROP FUNCTION tmp_add_col(regclass, text);
