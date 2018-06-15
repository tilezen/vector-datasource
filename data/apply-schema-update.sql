-- this function creates a new column named `cln_name` on table `tbl_name` with
-- type `typ_name` - UNLESS that column already exists (the type is not checked)
-- in which case it does nothing.
--
-- the function is idempotent, so can be run multiple times to make the same
-- change without erroring, unlike the `ALTER TABLE ... ADD COLUMN ...`
-- statement. this is useful when the import process errors out part way through
-- and rather than starting from scratch, this section can just be re-run.
--
-- NOTE: this function should be deleted at the end of the file, when it's no
-- longer needed. it won't error if not (see `CREATE OR REPLACE`), but it's not
-- a function that needs to be left lying around in the database.
--
CREATE OR REPLACE function add_column_if_not_exists(tbl_name text, cln_name text, typ_name text)
RETURNS VOID AS $$
BEGIN
  IF NOT EXISTS (
      SELECT column_name FROM information_schema.columns
      WHERE table_name=tbl_name and column_name=cln_name
      ) THEN
            EXECUTE format('ALTER TABLE %s ADD COLUMN %s %s', tbl_name, cln_name, typ_name);
  END IF;
END;
$$ LANGUAGE plpgsql;

DO $$
BEGIN

-- update polygon table to add feature zoom levels
PERFORM add_column_if_not_exists('planet_osm_polygon', 'mz_poi_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('planet_osm_polygon', 'mz_landuse_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('planet_osm_polygon', 'mz_transit_level', 'REAL');
PERFORM add_column_if_not_exists('planet_osm_polygon', 'mz_water_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('planet_osm_polygon', 'mz_earth_min_zoom', 'REAL');

-- same for line table
PERFORM add_column_if_not_exists('planet_osm_line', 'mz_road_level', 'REAL');
PERFORM add_column_if_not_exists('planet_osm_line', 'mz_transit_level', 'REAL');
PERFORM add_column_if_not_exists('planet_osm_line', 'mz_water_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('planet_osm_line', 'mz_earth_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('planet_osm_line', 'mz_landuse_min_zoom', 'REAL');

-- same for point
PERFORM add_column_if_not_exists('planet_osm_point', 'mz_poi_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('planet_osm_point', 'mz_water_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('planet_osm_point', 'mz_places_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('planet_osm_point', 'mz_earth_min_zoom', 'REAL');

-- and pre-calculated areas for all the polygonal NE and static OSM
-- tables.
PERFORM add_column_if_not_exists('ne_10m_urban_areas', 'way_area', 'REAL');
PERFORM add_column_if_not_exists('ne_50m_urban_areas', 'way_area', 'REAL');

PERFORM add_column_if_not_exists('ne_110m_ocean', 'way_area', 'REAL');
PERFORM add_column_if_not_exists('ne_110m_lakes', 'way_area', 'REAL');
PERFORM add_column_if_not_exists('ne_50m_ocean', 'way_area', 'REAL');
PERFORM add_column_if_not_exists('ne_50m_lakes', 'way_area', 'REAL');
PERFORM add_column_if_not_exists('ne_50m_playas', 'way_area', 'REAL');
PERFORM add_column_if_not_exists('ne_10m_ocean', 'way_area', 'REAL');
PERFORM add_column_if_not_exists('ne_10m_lakes', 'way_area', 'REAL');
PERFORM add_column_if_not_exists('ne_10m_playas', 'way_area', 'REAL');
PERFORM add_column_if_not_exists('water_polygons', 'way_area', 'REAL');

PERFORM add_column_if_not_exists('ne_110m_ocean', 'mz_water_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('ne_110m_lakes', 'mz_water_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('ne_110m_coastline', 'mz_water_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('ne_50m_ocean', 'mz_water_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('ne_50m_lakes', 'mz_water_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('ne_50m_coastline', 'mz_water_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('ne_50m_playas', 'mz_water_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('ne_10m_ocean', 'mz_water_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('ne_10m_lakes', 'mz_water_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('ne_10m_coastline', 'mz_water_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('ne_10m_playas', 'mz_water_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('water_polygons', 'mz_water_min_zoom', 'REAL');

PERFORM add_column_if_not_exists('ne_110m_land', 'way_area', 'REAL');
PERFORM add_column_if_not_exists('ne_50m_land', 'way_area', 'REAL');
PERFORM add_column_if_not_exists('ne_10m_land', 'way_area', 'REAL');
PERFORM add_column_if_not_exists('land_polygons', 'way_area', 'REAL');

PERFORM add_column_if_not_exists('ne_110m_land', 'mz_earth_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('ne_50m_land', 'mz_earth_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('ne_10m_land', 'mz_earth_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('land_polygons', 'mz_earth_min_zoom', 'REAL');

PERFORM add_column_if_not_exists('ne_10m_populated_places', 'mz_places_min_zoom', 'REAL');

PERFORM add_column_if_not_exists('planet_osm_polygon', 'mz_boundary_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('planet_osm_line', 'mz_boundary_min_zoom', 'REAL');

PERFORM add_column_if_not_exists('ne_110m_admin_0_boundary_lines_land', 'mz_boundary_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('ne_50m_admin_0_boundary_lines_land', 'mz_boundary_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('ne_50m_admin_1_states_provinces_lines', 'mz_boundary_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('ne_10m_admin_0_boundary_lines_land', 'mz_boundary_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('ne_10m_admin_0_boundary_lines_map_units', 'mz_boundary_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('ne_10m_admin_1_states_provinces_lines', 'mz_boundary_min_zoom', 'REAL');

PERFORM add_column_if_not_exists('planet_osm_point', 'mz_building_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('planet_osm_polygon', 'mz_building_min_zoom', 'REAL');

PERFORM add_column_if_not_exists('ne_50m_urban_areas', 'mz_landuse_min_zoom', 'REAL');
PERFORM add_column_if_not_exists('ne_10m_urban_areas', 'mz_landuse_min_zoom', 'REAL');

PERFORM add_column_if_not_exists('planet_osm_polygon', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM add_column_if_not_exists('planet_osm_line', 'mz_label_placement', 'geometry(Geometry, 3857)');

PERFORM add_column_if_not_exists('water_polygons', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM add_column_if_not_exists('land_polygons', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM add_column_if_not_exists('ne_110m_ocean', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM add_column_if_not_exists('ne_50m_ocean', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM add_column_if_not_exists('ne_10m_ocean', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM add_column_if_not_exists('ne_110m_lakes', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM add_column_if_not_exists('ne_50m_lakes', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM add_column_if_not_exists('ne_10m_lakes', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM add_column_if_not_exists('ne_50m_playas', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM add_column_if_not_exists('ne_10m_playas', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM add_column_if_not_exists('ne_110m_land', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM add_column_if_not_exists('ne_50m_land', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM add_column_if_not_exists('ne_10m_land', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM add_column_if_not_exists('ne_50m_urban_areas', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM add_column_if_not_exists('ne_10m_urban_areas', 'mz_label_placement', 'geometry(Geometry, 3857)');

-- NOTE: the absence of:
--
--  * ne_10m_admin_0_countries
--  * ne_10m_admin_0_map_units
--  * ne_10m_admin_1_states_provinces
--
-- although we do import the _boundaries_ variants of some of these, we only use
-- the polygon variants above to join on the wikidata ID, we don't draw or label
-- them directly.

END$$;

DROP FUNCTION add_column_if_not_exists(text, text, text);
