#!/bin/bash

# subsequent sql depends on functions installed
echo "Creating functions..."
psql $@ -f functions.sql
echo "done."

# apply updates in parallel across tables
echo -e "\nApplying updates in parallel across tables..."
psql $@ -f apply-updates-non-planet-tables.sql &
psql $@ -f apply-planet_osm_polygon.sql &
psql $@ -f apply-planet_osm_line.sql &
psql $@ -f apply-planet_osm_point.sql &
psql $@ -f wof-schema.sql &
wait
echo "done."

echo -e '\nApplying triggers...'
psql $@ -f triggers.sql
echo 'done.'

echo -e "\nAll updates complete. Exiting."
