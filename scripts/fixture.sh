#!/bin/bash

set -e

basedir="$(dirname ${BASH_SOURCE[0]})/.."

########################################################################
#
# FUNCTIONS
#
########################################################################

# exits the current process with the arguments echoed to stderr
#
function die {
    echo -e "ERROR: $@" 1>&2
    exit 1
}

function info {
    if [[ -n $VERBOSE ]]; then
        echo -e "INFO: $@"
    fi
}

# fetches the OSM elements given by the URLs in the file named by the first
# argument and stores the output XML in the file given by the second argument.
#
function fetch_osm_element {
    local file=$1
    local output=$2

    python "${basedir}/scripts/download-osm-data.py" "${file}" > "${output}"
}

# create a database with the name given by the first argument
#
function create_database {
    local dbname=$1

    info "=== Creating database \"${dbname}\"..."
    createdb -E UTF-8 -T template0 "${dbname}" || \
        die "Failed to set up database \"${dbname}\"."
}

# load the data given by the third argument into the database named in the
# first argument. note that the data should be an osmChange file.
#
function load_data_into_database {
    local dbname=$1
    local input_osc=$2

    if [[ ! -e "${basedir}/osm2pgsql.style" ]]; then
        die "Could not find file '${basedir}/osm2pgsql.style'."
    fi

    info "Enabling database extensions..."
    for ext in postgis hstore; do
        psql -d "${dbname}" -c "CREATE EXTENSION ${ext}"
    done

    info "Loading OSM data into database..."
    OSM2PGSQL_ARGS="-E 3857 -s -C 1024"
    OSM2PGSQL_ARGS+=" -S ${basedir}/osm2pgsql.style"
    OSM2PGSQL_ARGS+=" -d ${dbname} --hstore-all"
    if [[ ! -z ${PGHOST+x} ]]; then
        OSM2PGSQL_ARGS+=" -H $PGHOST"
    fi
    if [[ ! -z ${PGUSER+x} ]]; then
        OSM2PGSQL_ARGS+=" -U $PGUSER"
    fi

    osm2pgsql $OSM2PGSQL_ARGS --create "${basedir}/scripts/empty.osm"
    osm2pgsql $OSM2PGSQL_ARGS --append "${input_osc}"

    info "Loading shapefile schema..."
    # mock these tables - the shapefiles are _huge_ and we don't want to
    # spend time downloading and importing them - we use smaller extracts
    # in test/fixtures/ to handle specific test cases.
    for sql in `ls ${basedir}/data/shapefile_schema/*.sql`; do
        echo " >> ${sql}"
        cat ${sql} | psql $dbuserargs $dbhostargs -d "${dbname}"
    done

    info "Applying updates and indexes..."
    pushd "${basedir}/data"
    # Add indexes and any required database updates
    ./perform-sql-updates.sh -d "${dbname}"
    popd
}

# dump the full contents of the planet_osm_ tables in the datbase given by the
# first argument each into a GeoJSON file named by the table name and stored in
# the directory given by the second argument.
#
function export_geojson {
    local dbname=$1
    local tmpdir=$2

    info "Calculating GeoJSON..."
    for tbl in point line polygon; do
        num_features=$(psql -t -c "select count(*) from planet_osm_${tbl}" "${dbname}")
        if [[ $num_features -ne 0 ]]; then
            # note the "|| true" on the end to swallow the non-zero exit status
            # from read.
            read -d '' query <<EOF || true
SELECT
  json_build_object(
    'type',     'FeatureCollection',
    'features', json_agg(feature)
  )
FROM (
  SELECT
    json_build_object(
      'type',       'Feature',
      'id',         osm_id,
      'geometry',   ST_AsGeoJSON(ST_Transform(way, 4326))::json,
      'properties', hstore_to_json(tags)
    ) AS feature
  FROM planet_osm_${tbl}
) features;
EOF
            psql -t -c "${query}" "${dbname}" > "${tmpdir}/planet_osm_${tbl}.geojson"
        fi
    done
}

# move all the "*.geojson" files in the first argument directory into the second
# argument directory, failing with an error if no such files exist.
#
function move_fixtures {
    local tmpdir=$1
    local fixtures=$2

    shopt -s nullglob
    geojsons=(${tmpdir}/*.geojson)
    if [[ -z "$geojsons" ]]; then
        die "Ooops. Didn't find any features in the planet_osm_ tables." 1>&2

    else
        mkdir -p "${fixtures}"
        mv "${geojsons}" "${fixtures}/"

        info "Done"
    fi
}

########################################################################
#
# MAIN
#
########################################################################

# name the temporary directory and database so that they can be removed by
# the cleanup process common to all commands.
dbname="vector_datasource_fixture_$$"
tmpdir=$(mktemp -d)

# check that all the programs this script needs are available in the path.
for prog in osm2pgsql createdb dropdb psql python; do
    which $prog >/dev/null 2>&1 || \
        die "Unable to find program $prog - please install it and make sure" \
            "it is present in your \$PATH."
done

function cleanup {
    info "Dropping database \"${dbname}\" and cleaning up..."
    dropdb --if-exists "${dbname}"
    rm -rf "${tmpdir}"
}

# set the env var $NOCLEANUP to anything and the code won't clean up.
# this is useful when developing to see what the intermediate state is.
if [[ -z $NOCLEANUP ]]; then
    trap cleanup EXIT
fi

# unless overridden by the environment, set PGOPTIONS to unset psql's default
# verbosity.
: ${PGOPTIONS:='--client-min-messages=warning'}
export PGOPTIONS

# main command parsing.
case $1 in
    add)

        testname=$2
        if [[ -z $testname ]]; then
            die "Missing test name.\n" \
                "Usage: $0 add <name of test> <URL to element>\n" \
                "  For example:" \
                "$0 add 1234-my-test " \
                "http://www.openstreetmap.org/node/3958246944"
        fi

        url=$3
        if [[ -z $url ]]; then
            die "Missing OSM element URL.\n" \
                "Usage: $0 add <name of test> <URL to element>\n" \
                "  For example:" \
                "$0 add 1234-my-test " \
                "http://www.openstreetmap.org/node/3958246944"
        fi

        fixtures="${basedir}/integration-test/geojson-fixtures/${testname}"
        mkdir -p "${fixtures}"
        # note the leading comment hash sign at the beginning.
        echo "# ${url}" >> "${fixtures}/urls.txt"
        ;;

    update)
        create_database $dbname

        testname=$2
        if [[ -z $testname ]]; then
            die "Missing test name.\n" \
                "Usage: $0 update <name of test> <URL to element>\n" \
                "  For example:" \
                "$0 update 1234-my-test"
        fi

        osc_file="${tmpdir}/data.osc"
        fixtures="${basedir}/integration-test/geojson-fixtures/${testname}"

        fetch_osm_element "${fixtures}/urls.txt" $osc_file
        load_data_into_database $dbname $osc_file
        export_geojson $dbname $tmpdir
        move_fixtures $tmpdir $fixtures
        ;;

    *)
        die "Unknown command \"$1\"\n" \
            "Current commands are: add, update.\n" \
            "Usage: $0 add <name of test> <URL to element>"
        ;;
esac
