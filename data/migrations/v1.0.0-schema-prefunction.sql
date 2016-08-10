CREATE OR REPLACE function tmp_add_mz_label_placement(tbl_name text)
RETURNS VOID AS $$
BEGIN
 IF NOT EXISTS (
    SELECT column_name FROM information_schema.columns WHERE table_name=tbl_name and column_name='mz_label_placement') THEN
   EXECUTE format('ALTER TABLE %s ADD COLUMN mz_label_placement geometry(Geometry, 3857)', tbl_name, _col);
 END IF;
END;
$$ LANGUAGE plpgsql;

DO $$
BEGIN

PERFORM tmp_add_mz_label_placement('planet_osm_polygon');
PERFORM tmp_add_mz_label_placement('planet_osm_line');

PERFORM tmp_add_mz_label_placement('water_polygons');
PERFORM tmp_add_mz_label_placement('land_polygons');
PERFORM tmp_add_mz_label_placement('ne_110m_ocean');
PERFORM tmp_add_mz_label_placement('ne_50m_ocean');
PERFORM tmp_add_mz_label_placement('ne_10m_ocean');
PERFORM tmp_add_mz_label_placement('ne_110m_coastline');
PERFORM tmp_add_mz_label_placement('ne_50m_coastline');
PERFORM tmp_add_mz_label_placement('ne_10m_coastline');
PERFORM tmp_add_mz_label_placement('ne_110m_lakes');
PERFORM tmp_add_mz_label_placement('ne_50m_lakes');
PERFORM tmp_add_mz_label_placement('ne_10m_lakes');
PERFORM tmp_add_mz_label_placement('ne_50m_playas');
PERFORM tmp_add_mz_label_placement('ne_10m_playas');
PERFORM tmp_add_mz_label_placement('ne_110m_land');
PERFORM tmp_add_mz_label_placement('ne_50m_land');
PERFORM tmp_add_mz_label_placement('ne_10m_land');
PERFORM tmp_add_mz_label_placement('ne_50m_urban_areas');
PERFORM tmp_add_mz_label_placement('ne_10m_urban_areas');

END$$;

DROP FUNCTION tmp_add_mz_label_placement(text);
