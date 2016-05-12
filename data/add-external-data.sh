# this function exists to try and avoid downloading the file if it already
# exists. wget's default behaviour is to download it again with a ".1"
# added to the end.
function download {
	 file="$(basename $1)"
	 curl $1 -z "${file}" -o "${file}" -L -C -
}

# water polygons
#
download http://data.openstreetmapdata.com/water-polygons-split-3857.zip
unzip water-polygons-split-3857.zip
shp2pgsql -dID -s 900913 -W Windows-1252 -g the_geom water-polygons-split-3857/water_polygons.shp water_polygons | psql "$@" 
rm -rf ./water-polygons-split-3857

# land polygons
#
download http://data.openstreetmapdata.com/land-polygons-split-3857.zip
unzip land-polygons-split-3857.zip
shp2pgsql -dID -s 900913 -W Windows-1252 -g the_geom land-polygons-split-3857/land_polygons.shp land_polygons | psql "$@"
rm -rf ./land-polygons-split-3857

# simplified land polygons
#
download http://data.openstreetmapdata.com/simplified-land-polygons-complete-3857.zip
unzip simplified-land-polygons-complete-3857.zip
shp2pgsql -dID -s 900913 -W Windows-1252 -g the_geom simplified-land-polygons-complete-3857/simplified_land_polygons.shp simplified_land_polygons | psql "$@"
rm -rf ./simplified-land-polygons-complete-3857
