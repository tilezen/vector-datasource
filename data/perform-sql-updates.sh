#!/bin/bash

set -e

# apply schema updates first, some functions now depend on it.
echo "Creating custom schema..."
psql $@ -f schema.sql
echo "done."

# subsequent sql depends on functions installed
echo "Creating functions..."
psql $@ -f functions.sql
echo "done."

# update the schema of the tables
echo "Updating table schemas..."
psql $@ -f apply-schema-update.sql
echo "done."

# dynamic functions generated from csv
echo "Generating functions from csv..."
(cd ../vectordatasource/meta && python sql.py) | psql $@
echo "done."

# apply updates in parallel across tables
echo -e "\nApplying updates in parallel across tables..."
psql $@ -f apply-updates-non-planet-tables.sql &
psql $@ -f apply-planet_osm_polygon.sql &
psql $@ -f apply-planet_osm_line.sql &
psql $@ -f apply-planet_osm_point.sql &
wait
echo "done."

echo -e '\nApplying triggers...'
psql $@ -f triggers.sql
echo 'done.'

echo -e "\nAll updates complete. Exiting."
