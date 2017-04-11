CREATE OR REPLACE function tmp_add_mz_label_placement(tbl_name text)
RETURNS VOID AS $$
BEGIN
 IF NOT EXISTS (
    SELECT column_name FROM information_schema.columns WHERE table_name=tbl_name and column_name='mz_label_placement') THEN
   EXECUTE format('ALTER TABLE %s ADD COLUMN mz_label_placement geometry(Geometry, 3857)', tbl_name);
 END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE function tmp_drop_mz_label_placement(tbl_name text)
RETURNS VOID AS $$
BEGIN
 IF EXISTS (
    SELECT 1 FROM information_schema.columns WHERE table_name=tbl_name and column_name='mz_label_placement') THEN
   EXECUTE format('ALTER TABLE %s DROP COLUMN mz_label_placement', tbl_name);
 END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE function tmp_make_real(tbl_name text, col_name text)
RETURNS VOID AS $$
BEGIN
 IF NOT EXISTS (
    SELECT data_type FROM information_schema.columns
    WHERE table_name = tbl_name AND
          column_name = col_name AND
          data_type = 'real'
    ) THEN
   EXECUTE format('ALTER TABLE %s ALTER COLUMN %s SET DATA TYPE REAL', tbl_name, col_name);
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

DO $$
BEGIN

PERFORM tmp_make_real('planet_osm_line', 'mz_road_level');
PERFORM tmp_make_real('planet_osm_line', 'mz_transit_level');
PERFORM tmp_make_real('planet_osm_line', 'mz_water_min_zoom');
PERFORM tmp_make_real('planet_osm_line', 'mz_earth_min_zoom');
PERFORM tmp_make_real('planet_osm_line', 'mz_landuse_min_zoom');
PERFORM tmp_make_real('planet_osm_line', 'mz_boundary_min_zoom');

PERFORM tmp_make_real('planet_osm_point', 'mz_water_min_zoom');
PERFORM tmp_make_real('planet_osm_point', 'mz_places_min_zoom');
PERFORM tmp_make_real('planet_osm_point', 'mz_earth_min_zoom');
PERFORM tmp_make_real('planet_osm_point', 'mz_building_min_zoom');

PERFORM tmp_make_real('planet_osm_polygon', 'mz_water_min_zoom');
PERFORM tmp_make_real('planet_osm_polygon', 'mz_earth_min_zoom');
PERFORM tmp_make_real('planet_osm_polygon', 'mz_boundary_min_zoom');
PERFORM tmp_make_real('planet_osm_polygon', 'mz_building_min_zoom');

PERFORM tmp_make_real('ne_10m_admin_0_boundary_lines_land', 'mz_boundary_min_zoom');
PERFORM tmp_make_real('ne_10m_admin_0_boundary_lines_map_units', 'mz_boundary_min_zoom');
PERFORM tmp_make_real('ne_10m_admin_1_states_provinces_lines', 'mz_boundary_min_zoom');
PERFORM tmp_make_real('ne_10m_coastline', 'mz_water_min_zoom');
PERFORM tmp_make_real('ne_10m_lakes', 'mz_water_min_zoom');
PERFORM tmp_make_real('ne_10m_land', 'mz_earth_min_zoom');
PERFORM tmp_make_real('ne_10m_ocean', 'mz_water_min_zoom');
PERFORM tmp_make_real('ne_10m_playas', 'mz_water_min_zoom');
PERFORM tmp_make_real('ne_10m_populated_places', 'mz_places_min_zoom');
PERFORM tmp_make_real('ne_110m_admin_0_boundary_lines_land', 'mz_boundary_min_zoom');
PERFORM tmp_make_real('ne_110m_coastline', 'mz_water_min_zoom');
PERFORM tmp_make_real('ne_110m_lakes', 'mz_water_min_zoom');
PERFORM tmp_make_real('ne_110m_land', 'mz_earth_min_zoom');
PERFORM tmp_make_real('ne_110m_ocean', 'mz_water_min_zoom');
PERFORM tmp_make_real('ne_50m_admin_0_boundary_lines_land', 'mz_boundary_min_zoom');
PERFORM tmp_make_real('ne_50m_admin_1_states_provinces_lines', 'mz_boundary_min_zoom');
PERFORM tmp_make_real('ne_50m_coastline', 'mz_water_min_zoom');
PERFORM tmp_make_real('ne_50m_lakes', 'mz_water_min_zoom');
PERFORM tmp_make_real('ne_50m_land', 'mz_earth_min_zoom');
PERFORM tmp_make_real('ne_50m_ocean', 'mz_water_min_zoom');
PERFORM tmp_make_real('ne_50m_playas', 'mz_water_min_zoom');

PERFORM tmp_make_real('wof_neighbourhood', 'min_zoom');
PERFORM tmp_make_real('wof_neighbourhood', 'max_zoom');

END$$;

DO $$
BEGIN

PERFORM tmp_drop_mz_label_placement('ne_110m_coastline');
PERFORM tmp_drop_mz_label_placement('ne_50m_coastline');
PERFORM tmp_drop_mz_label_placement('ne_10m_coastline');

END$$;

DROP FUNCTION tmp_add_mz_label_placement(text);
DROP FUNCTION tmp_make_real(text, text);
DROP FUNCTION tmp_drop_mz_label_placement(text);
