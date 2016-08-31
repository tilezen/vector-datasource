-- update polygon table to add feature zoom levels
ALTER TABLE planet_osm_polygon ADD COLUMN mz_poi_min_zoom REAL;
ALTER TABLE planet_osm_polygon ADD COLUMN mz_landuse_min_zoom REAL;
ALTER TABLE planet_osm_polygon ADD COLUMN mz_transit_level REAL;
ALTER TABLE planet_osm_polygon ADD COLUMN mz_water_min_zoom REAL;
ALTER TABLE planet_osm_polygon ADD COLUMN mz_earth_min_zoom REAL;

-- same for line table
ALTER TABLE planet_osm_line ADD COLUMN mz_road_level REAL;
ALTER TABLE planet_osm_line ADD COLUMN mz_transit_level REAL;
ALTER TABLE planet_osm_line ADD COLUMN mz_water_min_zoom REAL;
ALTER TABLE planet_osm_line ADD COLUMN mz_earth_min_zoom REAL;
ALTER TABLE planet_osm_line ADD COLUMN mz_landuse_min_zoom REAL;

-- same for point
ALTER TABLE planet_osm_point ADD COLUMN mz_poi_min_zoom REAL;
ALTER TABLE planet_osm_point ADD COLUMN mz_water_min_zoom REAL;
ALTER TABLE planet_osm_point ADD COLUMN mz_places_min_zoom REAL;
ALTER TABLE planet_osm_point ADD COLUMN mz_earth_min_zoom REAL;

-- and pre-calculated areas for all the polygonal NE and static OSM
-- tables.
ALTER TABLE ne_10m_urban_areas ADD COLUMN way_area REAL;
ALTER TABLE ne_50m_urban_areas ADD COLUMN way_area REAL;

ALTER TABLE ne_110m_ocean ADD COLUMN way_area REAL;
ALTER TABLE ne_110m_lakes ADD COLUMN way_area REAL;
ALTER TABLE ne_50m_ocean ADD COLUMN way_area REAL;
ALTER TABLE ne_50m_lakes ADD COLUMN way_area REAL;
ALTER TABLE ne_50m_playas ADD COLUMN way_area REAL;
ALTER TABLE ne_10m_ocean ADD COLUMN way_area REAL;
ALTER TABLE ne_10m_lakes ADD COLUMN way_area REAL;
ALTER TABLE ne_10m_playas ADD COLUMN way_area REAL;
ALTER TABLE water_polygons ADD COLUMN way_area REAL;

ALTER TABLE ne_110m_ocean ADD COLUMN mz_water_min_zoom REAL;
ALTER TABLE ne_110m_lakes ADD COLUMN mz_water_min_zoom REAL;
ALTER TABLE ne_110m_coastline ADD COLUMN mz_water_min_zoom REAL;
ALTER TABLE ne_50m_ocean ADD COLUMN mz_water_min_zoom REAL;
ALTER TABLE ne_50m_lakes ADD COLUMN mz_water_min_zoom REAL;
ALTER TABLE ne_50m_coastline ADD COLUMN mz_water_min_zoom REAL;
ALTER TABLE ne_50m_playas ADD COLUMN mz_water_min_zoom REAL;
ALTER TABLE ne_10m_ocean ADD COLUMN mz_water_min_zoom REAL;
ALTER TABLE ne_10m_lakes ADD COLUMN mz_water_min_zoom REAL;
ALTER TABLE ne_10m_coastline ADD COLUMN mz_water_min_zoom REAL;
ALTER TABLE ne_10m_playas ADD COLUMN mz_water_min_zoom REAL;
ALTER TABLE water_polygons ADD COLUMN mz_water_min_zoom REAL;

ALTER TABLE ne_110m_land ADD COLUMN way_area REAL;
ALTER TABLE ne_50m_land ADD COLUMN way_area REAL;
ALTER TABLE ne_10m_land ADD COLUMN way_area REAL;
ALTER TABLE land_polygons ADD COLUMN way_area REAL;

ALTER TABLE ne_110m_land ADD COLUMN mz_earth_min_zoom REAL;
ALTER TABLE ne_50m_land ADD COLUMN mz_earth_min_zoom REAL;
ALTER TABLE ne_10m_land ADD COLUMN mz_earth_min_zoom REAL;
ALTER TABLE land_polygons ADD COLUMN mz_earth_min_zoom REAL;

ALTER TABLE ne_10m_populated_places ADD COLUMN mz_places_min_zoom REAL;

ALTER TABLE planet_osm_polygon ADD COLUMN mz_boundary_min_zoom REAL;
ALTER TABLE planet_osm_line ADD COLUMN mz_boundary_min_zoom REAL;

ALTER TABLE ne_110m_admin_0_boundary_lines_land ADD COLUMN mz_boundary_min_zoom REAL;
ALTER TABLE ne_50m_admin_0_boundary_lines_land ADD COLUMN mz_boundary_min_zoom REAL;
ALTER TABLE ne_50m_admin_1_states_provinces_lines ADD COLUMN mz_boundary_min_zoom REAL;
ALTER TABLE ne_10m_admin_0_boundary_lines_land ADD COLUMN mz_boundary_min_zoom REAL;
ALTER TABLE ne_10m_admin_1_states_provinces_lines ADD COLUMN mz_boundary_min_zoom REAL;

ALTER TABLE planet_osm_point ADD COLUMN mz_building_min_zoom REAL;
ALTER TABLE planet_osm_polygon ADD COLUMN mz_building_min_zoom REAL;

ALTER TABLE planet_osm_polygon ADD COLUMN mz_label_placement geometry(Geometry, 3857);
ALTER TABLE planet_osm_line ADD COLUMN mz_label_placement geometry(Geometry, 3857);

ALTER TABLE water_polygons ADD COLUMN mz_label_placement geometry(Geometry, 3857);
ALTER TABLE land_polygons ADD COLUMN mz_label_placement geometry(Geometry, 3857);
ALTER TABLE ne_110m_ocean ADD COLUMN mz_label_placement geometry(Geometry, 3857);
ALTER TABLE ne_50m_ocean ADD COLUMN mz_label_placement geometry(Geometry, 3857);
ALTER TABLE ne_10m_ocean ADD COLUMN mz_label_placement geometry(Geometry, 3857);
ALTER TABLE ne_110m_lakes ADD COLUMN mz_label_placement geometry(Geometry, 3857);
ALTER TABLE ne_50m_lakes ADD COLUMN mz_label_placement geometry(Geometry, 3857);
ALTER TABLE ne_10m_lakes ADD COLUMN mz_label_placement geometry(Geometry, 3857);
ALTER TABLE ne_50m_playas ADD COLUMN mz_label_placement geometry(Geometry, 3857);
ALTER TABLE ne_10m_playas ADD COLUMN mz_label_placement geometry(Geometry, 3857);
ALTER TABLE ne_110m_land ADD COLUMN mz_label_placement geometry(Geometry, 3857);
ALTER TABLE ne_50m_land ADD COLUMN mz_label_placement geometry(Geometry, 3857);
ALTER TABLE ne_10m_land ADD COLUMN mz_label_placement geometry(Geometry, 3857);
ALTER TABLE ne_50m_urban_areas ADD COLUMN mz_label_placement geometry(Geometry, 3857);
ALTER TABLE ne_10m_urban_areas ADD COLUMN mz_label_placement geometry(Geometry, 3857);
