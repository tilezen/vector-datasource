#!/bin/bash

set -e

PSQLOPTS="--set ON_ERROR_STOP=on -X -q"

# apply schema updates first, some functions now depend on it.
echo "Creating custom schema..."
psql $PSQLOPTS $@ -f schema.sql
echo "done."

# subsequent sql depends on functions installed
echo "Creating functions..."
psql $PSQLOPTS  $@ -f functions.sql
echo "done."

# update the schema of the tables
echo "Updating table schemas..."
psql $PSQLOPTS  $@ -f apply-schema-update.sql
echo "done."

# dynamic functions generated from YAML
echo "Generating functions from YAML..."

# store SQL in a temporary file, so make a temporary directory for it.
tmpdir=$(mktemp -d "${TMPDIR:-/tmp/}$(basename 0).XXXXXXXXXXXX")
sqlfile="${tmpdir}/generated-fuctions.sql"
trap "{ rm -rf $tmpdir; }" EXIT

# the reason for doing it this way is that the failure of `python sql.py`
# will now be picked up by `set -e` and fail the script, whereas piping it
# into psql  would have given the illusion of success.
pushd ../vectordatasource/meta
python sql.py > $sqlfile
popd
psql $PSQLOPTS  -f $sqlfile $@
echo "done."

# apply updates in parallel across tables
echo -e "\nApplying updates in parallel across tables..."
psql $PSQLOPTS  $@ -f apply-updates-non-planet-tables.sql &

# use postgres' own estimate of the percentile breakdown of the osm_id column to
# guide the distribution of jobs, so hopefully they end up mostly evenly sized.
#
# NOTE: currently hard-coded to 4-way parallelism. should be enough to keep a
# 4-core system busy, or more cores for a short while since points, lines and
# polygons are run concurrently. figuring out how many cores a remote postgres
# server has seems non-trivial, and the complexity of writing variable-level
# parallel code in shell script makes me call 4-way fixed "good enough" for
# now.
for tbl in polygon line point; do
    sql_script="apply-planet_osm_${tbl}.sql"
    for pct in 25 50 75; do
        breaks[$pct]=`psql -t -c "select (histogram_bounds::text::bigint[])[$pct] from pg_stats where tablename='planet_osm_${tbl}' and attname='osm_id'" $PSQLOPTS $@`
    done

    # try to paralellise across 4 processors.
    if [ -n "${breaks[25]}" ] && [ -n "${breaks[50]}" ] && [ -n "${breaks[75]}" ]; then
        sed "s/{{SHARDING}}/osm_id < ${breaks[25]}/" "${sql_script}" | psql $PSQLOPTS $@ &
        sed "s/{{SHARDING}}/osm_id >= ${breaks[25]} AND osm_id < ${breaks[50]}/" "${sql_script}" | psql $PSQLOPTS $@ &
        sed "s/{{SHARDING}}/osm_id >= ${breaks[50]} AND osm_id < ${breaks[75]}/" "${sql_script}" | psql $PSQLOPTS $@ &
        sed "s/{{SHARDING}}/osm_id >= ${breaks[75]}/" "${sql_script}" | psql $PSQLOPTS $@ &

    else
        # if no breaks, just use the serial version
        echo "Serial build for planet_osm_${tbl} - this might be slower."
        sed "s/{{SHARDING}}/TRUE/" "${sql_script}" | psql $PSQLOPTS $@ &
    fi
done
wait
# note: moved the analyze step out of the script and explicitly here to ensure
# that it's done only once, after all the updates.
echo -e "\nAnalyzing..."
for tbl in polygon line point; do
    psql $PSQLOPTS -c "ANALYZE planet_osm_${tbl}" $@ &
done
wait
echo -e "\nBuilding database indexes..."
for sql in indexes/*.sql; do
    psql $PSQLOPTS  $@ -f $sql &
done
wait
echo "done."

echo -e '\nApplying triggers...'
psql $PSQLOPTS  $@ -f triggers.sql
echo 'done.'

echo -e "\nAll updates complete. Exiting."
