#!/bin/sh
#
# After unpacking the contents of each zip archive, pipe this script to psql.
#
shp2pgsql -dID -s 900913 -W Windows-1252 -g the_geom ne_10m_lakes-merc.shp ne_10m_lakes
shp2pgsql -dID -s 900913 -W Windows-1252 -g the_geom ne_10m_ocean-merc.shp ne_10m_ocean
shp2pgsql -dID -s 900913 -W Windows-1252 -g the_geom ne_10m_playas-merc.shp ne_10m_playas
shp2pgsql -dID -s 900913 -W Windows-1252 -g the_geom ne_110m_lakes-merc.shp ne_110m_lakes
shp2pgsql -dID -s 900913 -W Windows-1252 -g the_geom ne_110m_ocean-merc.shp ne_110m_ocean
shp2pgsql -dID -s 900913 -W Windows-1252 -g the_geom ne_110m_ocean.shp ne_110m_ocean.shp
shp2pgsql -dID -s 900913 -W Windows-1252 -g the_geom ne_50m_lakes-merc.shp ne_50m_lakes
shp2pgsql -dID -s 900913 -W Windows-1252 -g the_geom ne_50m_ocean-merc.shp ne_50m_ocean
shp2pgsql -dID -s 900913 -W Windows-1252 -g the_geom ne_50m_playas-merc.shp ne_50m_playas
shp2pgsql -dID -s 900913 -W Windows-1252 -g the_geom ne_50m_urban_areas-merc.shp ne_50m_urban_areas
shp2pgsql -dID -s 900913 -W Windows-1252 -g the_geom ne_10m_urban_areas-merc.shp ne_10m_urban_areas
shp2pgsql -dID -s 900913 -W Windows-1252 -g the_geom ne_10m_parks_and_protected_lands-merc.shp ne_10m_parks_and_protected_lands
