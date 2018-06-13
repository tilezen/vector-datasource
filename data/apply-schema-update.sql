CREATE OR REPLACE function tmp_add_column(tbl_name text, cln_name text, typ_name text)
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
PERFORM tmp_add_column('planet_osm_polygon', 'mz_poi_min_zoom', 'REAL');
PERFORM tmp_add_column('planet_osm_polygon', 'mz_landuse_min_zoom', 'REAL');
PERFORM tmp_add_column('planet_osm_polygon', 'mz_transit_level', 'REAL');
PERFORM tmp_add_column('planet_osm_polygon', 'mz_water_min_zoom', 'REAL');
PERFORM tmp_add_column('planet_osm_polygon', 'mz_earth_min_zoom', 'REAL');

-- same for line table
PERFORM tmp_add_column('planet_osm_line', 'mz_road_level', 'REAL');
PERFORM tmp_add_column('planet_osm_line', 'mz_transit_level', 'REAL');
PERFORM tmp_add_column('planet_osm_line', 'mz_water_min_zoom', 'REAL');
PERFORM tmp_add_column('planet_osm_line', 'mz_earth_min_zoom', 'REAL');
PERFORM tmp_add_column('planet_osm_line', 'mz_landuse_min_zoom', 'REAL');

-- same for point
PERFORM tmp_add_column('planet_osm_point', 'mz_poi_min_zoom', 'REAL');
PERFORM tmp_add_column('planet_osm_point', 'mz_water_min_zoom', 'REAL');
PERFORM tmp_add_column('planet_osm_point', 'mz_places_min_zoom', 'REAL');
PERFORM tmp_add_column('planet_osm_point', 'mz_earth_min_zoom', 'REAL');

-- and pre-calculated areas for all the polygonal NE and static OSM
-- tables.
PERFORM tmp_add_column('ne_10m_urban_areas', 'way_area', 'REAL');
PERFORM tmp_add_column('ne_50m_urban_areas', 'way_area', 'REAL');

PERFORM tmp_add_column('ne_110m_ocean', 'way_area', 'REAL');
PERFORM tmp_add_column('ne_110m_lakes', 'way_area', 'REAL');
PERFORM tmp_add_column('ne_50m_ocean', 'way_area', 'REAL');
PERFORM tmp_add_column('ne_50m_lakes', 'way_area', 'REAL');
PERFORM tmp_add_column('ne_50m_playas', 'way_area', 'REAL');
PERFORM tmp_add_column('ne_10m_ocean', 'way_area', 'REAL');
PERFORM tmp_add_column('ne_10m_lakes', 'way_area', 'REAL');
PERFORM tmp_add_column('ne_10m_playas', 'way_area', 'REAL');
PERFORM tmp_add_column('water_polygons', 'way_area', 'REAL');

PERFORM tmp_add_column('ne_110m_ocean', 'mz_water_min_zoom', 'REAL');
PERFORM tmp_add_column('ne_110m_lakes', 'mz_water_min_zoom', 'REAL');
PERFORM tmp_add_column('ne_110m_coastline', 'mz_water_min_zoom', 'REAL');
PERFORM tmp_add_column('ne_50m_ocean', 'mz_water_min_zoom', 'REAL');
PERFORM tmp_add_column('ne_50m_lakes', 'mz_water_min_zoom', 'REAL');
PERFORM tmp_add_column('ne_50m_coastline', 'mz_water_min_zoom', 'REAL');
PERFORM tmp_add_column('ne_50m_playas', 'mz_water_min_zoom', 'REAL');
PERFORM tmp_add_column('ne_10m_ocean', 'mz_water_min_zoom', 'REAL');
PERFORM tmp_add_column('ne_10m_lakes', 'mz_water_min_zoom', 'REAL');
PERFORM tmp_add_column('ne_10m_coastline', 'mz_water_min_zoom', 'REAL');
PERFORM tmp_add_column('ne_10m_playas', 'mz_water_min_zoom', 'REAL');
PERFORM tmp_add_column('water_polygons', 'mz_water_min_zoom', 'REAL');

PERFORM tmp_add_column('ne_110m_land', 'way_area', 'REAL');
PERFORM tmp_add_column('ne_50m_land', 'way_area', 'REAL');
PERFORM tmp_add_column('ne_10m_land', 'way_area', 'REAL');
PERFORM tmp_add_column('land_polygons', 'way_area', 'REAL');

PERFORM tmp_add_column('ne_110m_land', 'mz_earth_min_zoom', 'REAL');
PERFORM tmp_add_column('ne_50m_land', 'mz_earth_min_zoom', 'REAL');
PERFORM tmp_add_column('ne_10m_land', 'mz_earth_min_zoom', 'REAL');
PERFORM tmp_add_column('land_polygons', 'mz_earth_min_zoom', 'REAL');

PERFORM tmp_add_column('ne_10m_populated_places', 'mz_places_min_zoom', 'REAL');

PERFORM tmp_add_column('planet_osm_polygon', 'mz_boundary_min_zoom', 'REAL');
PERFORM tmp_add_column('planet_osm_line', 'mz_boundary_min_zoom', 'REAL');

PERFORM tmp_add_column('ne_110m_admin_0_boundary_lines_land', 'mz_boundary_min_zoom', 'REAL');
PERFORM tmp_add_column('ne_50m_admin_0_boundary_lines_land', 'mz_boundary_min_zoom', 'REAL');
PERFORM tmp_add_column('ne_50m_admin_1_states_provinces_lines', 'mz_boundary_min_zoom', 'REAL');
PERFORM tmp_add_column('ne_10m_admin_0_boundary_lines_land', 'mz_boundary_min_zoom', 'REAL');
PERFORM tmp_add_column('ne_10m_admin_0_boundary_lines_map_units', 'mz_boundary_min_zoom', 'REAL');
PERFORM tmp_add_column('ne_10m_admin_1_states_provinces_lines', 'mz_boundary_min_zoom', 'REAL');

PERFORM tmp_add_column('planet_osm_point', 'mz_building_min_zoom', 'REAL');
PERFORM tmp_add_column('planet_osm_polygon', 'mz_building_min_zoom', 'REAL');

PERFORM tmp_add_column('ne_50m_urban_areas', 'mz_landuse_min_zoom', 'REAL');
PERFORM tmp_add_column('ne_10m_urban_areas', 'mz_landuse_min_zoom', 'REAL');

PERFORM tmp_add_column('planet_osm_polygon', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM tmp_add_column('planet_osm_line', 'mz_label_placement', 'geometry(Geometry, 3857)');

PERFORM tmp_add_column('water_polygons', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM tmp_add_column('land_polygons', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM tmp_add_column('ne_110m_ocean', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM tmp_add_column('ne_50m_ocean', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM tmp_add_column('ne_10m_ocean', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM tmp_add_column('ne_110m_lakes', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM tmp_add_column('ne_50m_lakes', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM tmp_add_column('ne_10m_lakes', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM tmp_add_column('ne_50m_playas', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM tmp_add_column('ne_10m_playas', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM tmp_add_column('ne_110m_land', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM tmp_add_column('ne_50m_land', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM tmp_add_column('ne_10m_land', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM tmp_add_column('ne_50m_urban_areas', 'mz_label_placement', 'geometry(Geometry, 3857)');
PERFORM tmp_add_column('ne_10m_urban_areas', 'mz_label_placement', 'geometry(Geometry, 3857)');

END$$;

DROP FUNCTION tmp_add_column(text, text, text);
