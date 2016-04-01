CREATE OR REPLACE function tmp_add_water_col(_tbl regclass)
RETURNS integer AS $$
BEGIN
 IF NOT EXISTS (
   SELECT 1 FROM pg_attribute
   WHERE attrelid = _tbl
   AND attname = 'mz_water_min_zoom'
   AND NOT attisdropped) THEN

   EXECUTE format('ALTER TABLE %s ADD COLUMN mz_water_min_zoom SMALLINT', _tbl);
 END IF;
 RETURN 1;
END;
$$ LANGUAGE plpgsql;

DO $$
BEGIN
  PERFORM tmp_add_water_col('public.planet_osm_polygon');
  PERFORM tmp_add_water_col('public.planet_osm_line');
  PERFORM tmp_add_water_col('public.planet_osm_point');

  PERFORM tmp_add_water_col('public.ne_10m_coastline');
  PERFORM tmp_add_water_col('public.ne_50m_coastline');
  PERFORM tmp_add_water_col('public.ne_110m_coastline');
  PERFORM tmp_add_water_col('public.ne_10m_ocean');
  PERFORM tmp_add_water_col('public.ne_50m_ocean');
  PERFORM tmp_add_water_col('public.ne_110m_ocean');
  PERFORM tmp_add_water_col('public.ne_10m_lakes');
  PERFORM tmp_add_water_col('public.ne_50m_lakes');
  PERFORM tmp_add_water_col('public.ne_110m_lakes');
  PERFORM tmp_add_water_col('public.ne_10m_playas');
  PERFORM tmp_add_water_col('public.ne_50m_playas');

  PERFORM tmp_add_water_col('public.water_polygons');
END$$;

DROP FUNCTION tmp_add_water_col(regclass);
