#!/bin/bash

migration_dir=${0%/*}

# first, run any "pre-function" migrations. these might be necessary if the
# migration alters tables to add columns referenced in the functions, in
# which case the function creation would fail.
for sql in ${migration_dir}/*.sql; do
    # break the loop if the file doesn't exist - this is generally the case
    # if the glob matches nothing and we end up looking for a file which is
    # called literally '*.sql'.
    [ -f $sql ] || break

    if [[ $sql = *prefunction*.sql ]]; then
        psql -f "$sql" $*
    else
        echo "SKIPPING $sql - this will be run after the functions."
    fi
done

# next run functions and triggers, bailing if either of these fail, as they
# are required by later steps.
psql --set ON_ERROR_STOP=1 -f "${migration_dir}/../functions.sql" $*
if [ $? -ne 0 ]; then echo "Installing new functions failed.">&2; exit 1; fi
python ${migration_dir}/create-sql-functions.py | psql --set ON_ERROR_STOP=1 $*
if [ $? -ne 0 ]; then echo "Installing generated functions failed.">&2; exit 1; fi
psql --set ON_ERROR_STOP=1 -f "${migration_dir}/../triggers.sql" $*
if [ $? -ne 0 ]; then echo "Installing new triggers failed.">&2; exit 1; fi

# then disable triggers
for table in planet_osm_point planet_osm_line planet_osm_polygon; do
    psql -c "ALTER TABLE ${table} DISABLE TRIGGER USER" $*
done

# run updates in parallel. note that we don't bail here, as we want to
# re-enable the triggers regardless of whether we failed or not.
for sql in ${migration_dir}/*.sql; do
    # break the loop if the file doesn't exist - this is generally the case
    # if the glob matches nothing and we end up looking for a file which is
    # called literally '*.sql'.
    [ -f $sql ] || break

    if [[ $sql = *cleanup*.sql ]]; then
        echo "SKIPPING $sql - run this after the code migration."
    elif [[ $sql = *prefunction*.sql ]]; then
        echo "SKIPPING $sql - this was already run before the functions."
    else
        psql -f "$sql" $* &
    fi
done

wait

# re-enable triggers
for table in planet_osm_point planet_osm_line planet_osm_polygon; do
    psql -c "ALTER TABLE ${table} ENABLE TRIGGER USER" $*
done

# re-generate the functions to avoid issues when a migration updates
# the schema
python ${migration_dir}/create-sql-functions.py | psql --set ON_ERROR_STOP=1 $*
if [ $? -ne 0 ]; then echo "Installing generated functions second time failed.">&2; exit 1; fi

for python in ${migration_dir}/*.py; do
    # break the loop if the file doesn't exist - this is generally the case
    # if the glob matches nothing and we end up looking for a file which is
    # called literally '*.py'.
    [ -f $python ] || break

    if [ $python != "${migration_dir}/create-sql-functions.py" ]; then
        echo "executing python: $python"
        python $python
    fi
done
