#!/bin/bash

set -e

dbname="vector_datasource_$$"
basedir="$(dirname ${BASH_SOURCE[0]})"

function die {
   echo "$@" 1>&2;
   exit 1
}

for prog in createdb cat dropdb python osm2pgsql xargs zip; do
   which "${prog}" >/dev/null || die "Unable to find '${prog}' program in PATH."
done

echo "=== Creating database \"${dbname}\"..."
createdb -E UTF-8 -T template0 "${dbname}"
cat >empty.osm <<EOF
<?xml version='1.0' encoding='utf-8'?>
<osm version="0.6">
</osm>
EOF

function cleanup {
   echo "=== Dropping database \"${dbname}\" and cleaning up..."
   dropdb --if-exists "${dbname}"
   rm -f empty.osm data.osc
}

# set the env var $NOCLEANUP to anything and the code won't clean up. this is
# useful when developing to see what the intermediate state is.
if [[ -z $NOCLEANUP ]]; then
    trap cleanup EXIT
fi

echo "=== Enabling database extensions..."
for ext in postgis hstore; do
   psql -d "${dbname}" -c "CREATE EXTENSION ${ext}"
done

echo "=== Dumping test data..."
if [[ -f data.osc ]]; then
    rm -f data.osc
fi
python "${basedir}/test.py" -dumpdata

echo "=== Loading test data..."
osm2pgsql -E 900913 -s -C 1024 -S "${basedir}/osm2pgsql.style" \
  -d "${dbname}" -k --create empty.osm
osm2pgsql -E 900913 -s -C 1024 -S "${basedir}/osm2pgsql.style" \
  -d "${dbname}" -k --append data.osc

echo "=== Loading external data..."
pushd "${basedir}/data"
# Load external data
#./add-external-data.sh -d "${dbname}"
psql "${dbname}" <<EOF
CREATE TABLE water_polygons (
    gid integer NOT NULL,
    fid double precision,
    the_geom geometry(MultiPolygon,900913)
);
CREATE TABLE land_polygons (
    gid integer NOT NULL,
    fid double precision,
    the_geom geometry(MultiPolygon,900913)
);
CREATE TABLE simplified_land_polygons (
    gid integer NOT NULL,
    fid double precision,
    the_geom geometry(MultiPolygon,900913)
);
EOF
# Unzip all zip
ls *.zip | xargs -n1 unzip -o
# Load data from zips
./shp2pgsql.sh | psql -d "${dbname}"
# Add indexes and any required database updates
./perform-sql-updates.sh -d "${dbname}"
popd

echo "=== Loading Who's on First data..."
# Finally, neighbourhood data is required to be loaded from Who's on First.
#wget https://s3.amazonaws.com/mapzen-tiles-prod-us-east/data/wof/wof_neighbourhoods.pgdump
#pg_restore --clean --if-exists -d "${dbname}" -O wof_neighbourhoods.pgdump

# TODO: make config for tileserver and serve

# TODO: run tests
#VECTOR_DATASOURCE_CONFIG_URL=
