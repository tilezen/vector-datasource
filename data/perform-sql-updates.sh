#!/bin/bash

# subsequent sql depends on functions installed
psql $@ -f functions.sql

# apply updates in parallel across tables
psql $@ -f apply-updates-non-planet-tables.sql &
psql $@ -f apply-planet_osm_polygon.sql &
psql $@ -f apply-planet_osm_line.sql &
psql $@ -f apply-planet_osm_point.sql &

wait

# triggers should get added last
psql $@ -f triggers.sql
