CREATE OR REPLACE function tmp_add_ne_landuse(tbl_name text)
RETURNS VOID AS $$
BEGIN
  IF NOT EXISTS (
    SELECT column_name FROM information_schema.columns WHERE table_name=tbl_name and column_name='mz_landuse_min_zoom') THEN
      EXECUTE format('ALTER TABLE %s ADD COLUMN mz_landuse_min_zoom REAL', tbl_name);
  END IF;
END;
$$ LANGUAGE plpgsql;

DO $$
BEGIN

PERFORM tmp_add_ne_landuse('ne_50m_urban_areas');
PERFORM tmp_add_ne_landuse('ne_10m_urban_areas');

END$$;

DROP FUNCTION tmp_add_ne_landuse(text);
