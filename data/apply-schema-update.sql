-- update polygon table to add feature zoom levels
ALTER TABLE planet_osm_polygon ADD COLUMN mz_poi_min_zoom REAL;
ALTER TABLE planet_osm_polygon ADD COLUMN mz_landuse_min_zoom REAL;
ALTER TABLE planet_osm_polygon ADD COLUMN mz_transit_level REAL;
ALTER TABLE planet_osm_polygon ADD COLUMN mz_water_min_zoom SMALLINT;

-- same for line table
ALTER TABLE planet_osm_line ADD COLUMN mz_road_level SMALLINT;
ALTER TABLE planet_osm_line ADD COLUMN mz_transit_level SMALLINT;
ALTER TABLE planet_osm_line ADD COLUMN mz_water_min_zoom SMALLINT;

-- same for point
ALTER TABLE planet_osm_point ADD COLUMN mz_poi_min_zoom REAL;
ALTER TABLE planet_osm_point ADD COLUMN mz_water_min_zoom SMALLINT;
ALTER TABLE planet_osm_point ADD COLUMN mz_places_min_zoom SMALLINT;

-- and pre-calculated areas for all the polygonal NE and static OSM
-- tables.
ALTER TABLE ne_110m_ocean ADD COLUMN way_area REAL;
ALTER TABLE ne_110m_lakes ADD COLUMN way_area REAL;
ALTER TABLE ne_50m_ocean ADD COLUMN way_area REAL;
ALTER TABLE ne_50m_lakes ADD COLUMN way_area REAL;
ALTER TABLE ne_50m_playas ADD COLUMN way_area REAL;
ALTER TABLE ne_10m_ocean ADD COLUMN way_area REAL;
ALTER TABLE ne_10m_lakes ADD COLUMN way_area REAL;
ALTER TABLE ne_10m_playas ADD COLUMN way_area REAL;
ALTER TABLE ne_10m_urban_areas ADD COLUMN way_area REAL;
ALTER TABLE ne_50m_urban_areas ADD COLUMN way_area REAL;
ALTER TABLE ne_10m_parks_and_protected_lands ADD COLUMN way_area REAL;
ALTER TABLE water_polygons ADD COLUMN way_area REAL;

ALTER TABLE ne_110m_ocean ADD COLUMN mz_water_min_zoom SMALLINT;
ALTER TABLE ne_110m_lakes ADD COLUMN mz_water_min_zoom SMALLINT;
ALTER TABLE ne_50m_ocean ADD COLUMN mz_water_min_zoom SMALLINT;
ALTER TABLE ne_50m_lakes ADD COLUMN mz_water_min_zoom SMALLINT;
ALTER TABLE ne_50m_playas ADD COLUMN mz_water_min_zoom SMALLINT;
ALTER TABLE ne_10m_ocean ADD COLUMN mz_water_min_zoom SMALLINT;
ALTER TABLE ne_10m_lakes ADD COLUMN mz_water_min_zoom SMALLINT;
ALTER TABLE ne_10m_playas ADD COLUMN mz_water_min_zoom SMALLINT;
ALTER TABLE water_polygons ADD COLUMN mz_water_min_zoom SMALLINT;

ALTER TABLE ne_10m_populated_places ADD COLUMN mz_places_min_zoom SMALLINT;

ALTER TABLE planet_osm_polygon ADD COLUMN mz_boundary_min_zoom SMALLINT;
ALTER TABLE planet_osm_line ADD COLUMN mz_boundary_min_zoom SMALLINT;

ALTER TABLE ne_110m_admin_0_boundary_lines_land ADD COLUMN mz_boundary_min_zoom SMALLINT;
ALTER TABLE ne_50m_admin_0_boundary_lines_land ADD COLUMN mz_boundary_min_zoom SMALLINT;
ALTER TABLE ne_50m_admin_1_states_provinces_lines ADD COLUMN mz_boundary_min_zoom SMALLINT;
ALTER TABLE ne_10m_admin_0_boundary_lines_land ADD COLUMN mz_boundary_min_zoom SMALLINT;
ALTER TABLE ne_10m_admin_1_states_provinces_lines ADD COLUMN mz_boundary_min_zoom SMALLINT;

ALTER TABLE planet_osm_point ADD COLUMN mz_building_min_zoom SMALLINT;
ALTER TABLE planet_osm_polygon ADD COLUMN mz_building_min_zoom SMALLINT;
