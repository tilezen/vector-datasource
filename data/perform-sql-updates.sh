#!/bin/bash
if [ -z "$1" ]
then
    echo 'Missing database name'
    exit 1
fi

dbname="$1"

shift

psql -d $dbname $@ -f functions.sql
psql -d $dbname $@ -f single-pass-update.sql
psql -d $dbname $@ -f triggers.sql
