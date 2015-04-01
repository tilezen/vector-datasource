#!/bin/bash

# subsequent sql depends on functions installed
echo -e "Creating functions... \c"
psql $@ -f functions.sql
echo "done."

# apply updates in parallel across tables
echo -e "\nApplying updates in parallel across tables... \c"
psql $@ -f apply-updates-non-planet-tables.sql &
psql $@ -f apply-planet_osm_polygon.sql &
psql $@ -f apply-planet_osm_line.sql &
psql $@ -f apply-planet_osm_point.sql &
wait
echo "done."

echo "\nAll updates complete. Exiting."
