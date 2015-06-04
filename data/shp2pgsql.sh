#!/bin/sh
#
# After unpacking the contents of each zip archive, pipe this script to psql.
#

import_shapefile(){
	shp2pgsql -dID -s 900913 -W Windows-1252 -g the_geom "$1" "$2"
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
