#!/bin/bash

set -e

PSQLOPTS="--set ON_ERROR_STOP=on -X"

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
psql $PSQLOPTS  $@ -f apply-planet_osm_polygon.sql &
psql $PSQLOPTS  $@ -f apply-planet_osm_line.sql &
psql $PSQLOPTS  $@ -f apply-planet_osm_point.sql &
wait
echo "done."

echo -e '\nApplying triggers...'
psql $PSQLOPTS  $@ -f triggers.sql
echo 'done.'

echo -e "\nAll updates complete. Exiting."
