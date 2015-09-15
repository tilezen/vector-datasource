#!/bin/sh
#
# After unpacking the contents of each zip archive, pipe this script to psql.
#

import_shapefile(){
	shp2pgsql -dID -s 900913 -W Windows-1252 -g the_geom "$@"
}

import_shapefile ne_10m_lakes-merc.shp ne_10m_lakes
import_shapefile ne_10m_ocean-merc.shp ne_10m_ocean
import_shapefile ne_10m_playas-merc.shp ne_10m_playas
import_shapefile ne_110m_lakes-merc.shp ne_110m_lakes
import_shapefile ne_110m_ocean-merc.shp ne_110m_ocean
import_shapefile ne_50m_lakes-merc.shp ne_50m_lakes
import_shapefile ne_50m_ocean-merc.shp ne_50m_ocean
import_shapefile ne_50m_playas-merc.shp ne_50m_playas
import_shapefile ne_50m_urban_areas-merc.shp ne_50m_urban_areas
import_shapefile ne_10m_urban_areas-merc.shp ne_10m_urban_areas
import_shapefile ne_10m_parks_and_protected_lands-merc.shp ne_10m_parks_and_protected_lands
import_shapefile ne_10m_land-tiled-merc.shp ne_10m_land
import_shapefile ne_50m_land-merc.shp ne_50m_land
import_shapefile ne_110m_land-merc.shp ne_110m_land
import_shapefile ne_10m_populated_places-merc.shp ne_10m_populated_places
import_shapefile -W UTF-8 ne_110m_admin_0_boundary_lines_land-merc.shp ne_110m_admin_0_boundary_lines_land
import_shapefile -W UTF-8 ne_50m_admin_0_boundary_lines_land-merc.shp ne_50m_admin_0_boundary_lines_land
import_shapefile -W UTF-8 ne_50m_admin_1_states_provinces_lines-merc.shp ne_50m_admin_1_states_provinces_lines
import_shapefile -W UTF-8 ne_10m_admin_0_boundary_lines_land-merc.shp ne_10m_admin_0_boundary_lines_land
import_shapefile -W UTF-8 ne_10m_admin_1_states_provinces_lines-merc.shp ne_10m_admin_1_states_provinces_lines
import_shapefile ne_10m_roads-merc.shp ne_10m_roads
import_shapefile ne_10m_coastline-merc.shp ne_10m_coastline
import_shapefile ne_50m_coastline-merc.shp ne_50m_coastline
import_shapefile ne_110m_coastline-merc.shp ne_110m_coastline
