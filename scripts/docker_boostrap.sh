set -e
export

export PGPASSWORD=$POSTGRES_ENV_POSTGRES_PASSWORD
psql -h "$POSTGRES_PORT_5432_TCP_ADDR" \
     -p "$POSTGRES_PORT_5432_TCP_PORT" \
     -U "$POSTGRES_ENV_POSTGRES_USER" \
     -d "$POSTGRES_ENV_POSTGRES_DB" \
     -c "create extension if not exists postgis; create extension if not exists hstore;"

/usr/bin/wget https://s3.amazonaws.com/metro-extracts.mapzen.com/new-york_new-york.osm.pbf
osm2pgsql --slim \
          --cache 1024 \
          --style osm2pgsql.style \
          --hstore-all \
          new-york_new-york.osm.pbf \
          -H "$POSTGRES_PORT_5432_TCP_ADDR" \
          -P "$POSTGRES_PORT_5432_TCP_PORT" \
          -U "$POSTGRES_ENV_POSTGRES_USER" \
          -d "$POSTGRES_ENV_POSTGRES_DB"

cd data
/usr/bin/python2.7 bootstrap.py
/usr/bin/make -f Makefile-import-data
./import-shapefiles.sh | \
    psql -h "$POSTGRES_PORT_5432_TCP_ADDR" \
         -p "$POSTGRES_PORT_5432_TCP_PORT" \
         -U "$POSTGRES_ENV_POSTGRES_USER" \
         -d "$POSTGRES_ENV_POSTGRES_DB"
./perform-sql-updates.sh \
    -h "$POSTGRES_PORT_5432_TCP_ADDR" \
    -p "$POSTGRES_PORT_5432_TCP_PORT" \
    -U "$POSTGRES_ENV_POSTGRES_USER" \
    -d "$POSTGRES_ENV_POSTGRES_DB"
cd ..
