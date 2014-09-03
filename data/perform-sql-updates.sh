#!/bin/bash
if [ -z "$1" ]
then
    echo 'Missing database name'
    exit 1
fi

# first arg is required to be the database name
dbname="$1"

# subsequent args are used to supplement the psql query connection string
shift

# subsequent sql depends on functions installed
psql -d $dbname $@ -f functions.sql

# apply updates in parallel across tables
psql -d $dbname $@ -f apply-updates-non-planet-tables.sql &
psql -d $dbname $@ -f apply-planet_osm_polygon.sql &
psql -d $dbname $@ -f apply-planet_osm_line.sql &
psql -d $dbname $@ -f apply-planet_osm_point.sql &

wait

# triggers should get added last
psql -d $dbname $@ -f triggers.sql
