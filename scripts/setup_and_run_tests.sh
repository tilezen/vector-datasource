#!/bin/bash -x

set -e

dbname="vector_datasource_$$"
basedir="$(dirname ${BASH_SOURCE[0]})/.."
server_pid=0

# parse arguments
while [[ $# -gt 1 ]]; do
    key=$1
    case $key in
        -j|--num-jobs)
            NUM_JOBS=$2
            shift
            ;;
        *)
            # ignore unknown option
            ;;
    esac
    shift
done

function die {
   echo "$@" 1>&2;
   exit 1
}

for prog in createdb cat dropdb python osm2pgsql shp2pgsql xargs zip; do
   which "${prog}" >/dev/null || die "Unable to find '${prog}' program in PATH."
done

shp2pgsql | grep RELEASE: | awk '{split($2,v,"."); if (v[1] < 2) { exit 1; }}'
if [ $? -ne 0 ]; then
    die 'Your version of shp2pgsql is too old, we need at least version 2 or later.'
fi

echo "=== Creating database \"${dbname}\"..."
if [ -z "$PGHOST" ]; then
    dbhostargs=""
else
    dbhostargs="-h $PGHOST"
fi
if [ -z "$PGUSER" ]; then
    dbuserargs=""
else
    dbuserargs="-U $PGUSER"
fi
createdb -E UTF-8 -T template0 $dbhostargs $dbuserargs "${dbname}"
cat >empty.osm <<EOF
<?xml version='1.0' encoding='utf-8'?>
<osm version="0.6">
</osm>
EOF

function cleanup {
   if [[ $server_pid -ne 0 ]]; then
      echo "=== Killing test server ==="
      kill -HUP "${server_pid}"
   fi
   echo "=== Dropping database \"${dbname}\" and cleaning up..."
   dropdb --if-exists $dbuserargs $dbhostargs "${dbname}"
   rm -f empty.osm data.osc test_server.port
}

# set the env var $NOCLEANUP to anything and the code won't clean up. this is
# useful when developing to see what the intermediate state is.
if [[ -z $NOCLEANUP ]]; then
    trap cleanup EXIT
fi

echo "=== Enabling database extensions..."
for ext in postgis hstore; do
   psql $dbhostargs $dbuserargs -d "${dbname}" -c "CREATE EXTENSION ${ext}"
done

echo "=== Dumping test data..."
if [[ -f data.osc ]]; then
    rm -f data.osc
fi
python "${basedir}/integration-test.py" -dumpdata

echo "=== Loading test data..."

OSM2PGSQL_ARGS="-E 3857 -s -C 1024"
OSM2PGSQL_ARGS+=" -S ${basedir}/osm2pgsql.style"
OSM2PGSQL_ARGS+=" -d ${dbname} --hstore-all"
if [[ ! -z ${NUM_JOBS+x} ]]; then
    OSM2PGSQL_ARGS+=" --number-processes=$NUM_JOBS"
fi
if [[ ! -z ${PGHOST+x} ]]; then
    OSM2PGSQL_ARGS+=" -H $PGHOST"
fi
if [[ ! -z ${PGUSER+x} ]]; then
    OSM2PGSQL_ARGS+=" -U $PGUSER"
fi

osm2pgsql $OSM2PGSQL_ARGS --create empty.osm
osm2pgsql $OSM2PGSQL_ARGS --append data.osc

echo "=== Loading shapefile schema..."
# mock these tables - the shapefiles are _huge_ and we don't want to
# spend time downloading and importing them - we use smaller extracts
# in test/fixtures/ to handle specific test cases.
for sql in `ls ${basedir}/data/shapefile_schema/*.sql`; do
    echo " >> ${sql}"
    cat ${sql} | psql $dbuserargs $dbhostargs -d "${dbname}"
done

echo "=== Loading fixture data..."
# load up shapefile fixtures into the appropriate tables
# allow globs to expand to empty strings to make enumerating files in
# possibly empty directories easier.
shopt -s nullglob
for tbl in `ls ${basedir}/integration-test/fixtures/`; do
    if [[ -d "${basedir}/integration-test/fixtures/${tbl}" ]]; then
        for shp in "${basedir}/integration-test/fixtures/${tbl}"/*.shp; do
            shp2pgsql -a -D -s 3857 -g the_geom \
                      "${shp}" "${tbl}" \
                | psql $dbuserargs $dbhostargs -d "${dbname}"
        done
    fi
done
shopt -u nullglob

echo "=== Loading bundled data..."
pushd "${basedir}/data"
# NOTE: not loading bundled data! All data should come from fixtures.
# Add indexes and any required database updates
./perform-sql-updates.sh $dbuserargs $dbhostargs -d "${dbname}"
popd

# load up pgcopy fixtures into the appropriate tables - note that these
# go into the database _after_ the "apply updates" SQL, so should include
# any columns (e.g: way_area) that those add.
shopt -s nullglob
for tbl in `ls ${basedir}/integration-test/fixtures/`; do
    if [[ -d "${basedir}/integration-test/fixtures/${tbl}" ]]; then
        for pgcopy in "${basedir}/integration-test/fixtures/${tbl}"/*.pgcopy; do
            psql $dbuserargs $dbhostargs -c "copy ${tbl} from stdin" "${dbname}" < "${pgcopy}"
        done
    fi
done
shopt -u nullglob

echo "=== Starting test tile server..."
# make config for tileserver and serve
test_server_port="${basedir}/test_server.port"
rm -f "${test_server_port}"
python scripts/test_server.py "${dbname}" "${PGUSER}" "${test_server_port}" &
server_pid=$!

echo "=== Waiting for tile server to start..."
# wait for file to exist, which means server has started up
counter=0
limit=10
while [[ ! -f "${test_server_port}" ]]; do
    sleep 1
    # note: don't use postfix ++ as let returns 1 when the arg evaluates to
    # zero (as (counter=0)++ would), which makes `set -e` terminate the
    # program.
    let counter=counter+1
    if [[ $counter -gt $limit ]]; then
        echo "Test server didn't start up within ${limit}s."
        exit 1
    fi
done

# no longer an error to fail - all setup is done. if the test suite fails
# then we only want to print out, not kill the whole process.
set +e

# run tests
port=`cat "${test_server_port}"`
export VECTOR_DATASOURCE_CONFIG_URL="http://localhost:${port}/%(layer)s/%(z)d/%(x)d/%(y)d.json"
python "${basedir}/integration-test.py"
success=$?

if [[ $success -eq 0 ]]; then
    echo "SUCCESS"

else
    cat test.log
fi

kill -HUP "${server_pid}"
wait

exit $success
