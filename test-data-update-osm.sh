#!/bin/bash

set -e

function die {
    echo -e "ERROR: $@" 1>&2
    exit 1
}

for prog in awk curl xsltproc osm2pgsql; do
    which $prog >/dev/null 2>&1 || \
        die "Unable to find program $prog - please install it and make sure" \
            "it is present in your \$PATH."
done

url=$1
if [[ -z $url ]]; then
    die "Usage: test-data-update-osm.sh <URL to element> [database name]\n  For example:" \
        "test-data-update-osm.sh http://www.openstreetmap.org/node/3958246944"
fi

db=$2
if [[ -z $db ]]; then
    db=$MZ_DATABASE
fi
if [[ -z $db ]]; then
    die "Usage: test-data-update-osm.sh <URL to element> [database name]\n  Unable to" \
        "figure out database name. Please either provide it as the second" \
        "parameter or as the environment variable \$MZ_DATABASE."
fi

if [[ ! -e test-data-osm-template.xsl ]]; then
    die "Could not find file 'test-data-osm-template.xsl', make sure you are running from" \
        "the vector-datasource root dir."
fi

if [[ ! -e osm2pgsql.style ]]; then
    die "Could not find file 'osm2pgsql.style', make sure you are running" \
        "from the vector-datasource root dir."
fi

typ=`echo $url | awk -F / '{print $4;}'`
if [[ $typ != 'node' && $typ != 'way' && $typ != 'relation' ]]; then
    die "Could not understand URL as an OSM element type. URLs should look" \
        "like this: http://www.openstreetmap.org/node/3958246944"
fi

id=`echo $url | awk -F / '{print $5;}'`
echo $id
if [[ ! $id =~ ^[0-9]+$ ]]; then
    die "Could not understand URL as an OSM element ID. URLs should look" \
        "like this: http://www.openstreetmap.org/node/3958246944"
fi

api_url="https://www.openstreetmap.org/api/0.6/$typ/$id"
if [[ $typ == 'way' || $typ == 'relation' ]]; then
    api_url="$api_url/full"
fi

curl -o update.osm $api_url
xsltproc test-data-osm-template.xsl update.osm > update.osc
osm2pgsql -s -C 1024 -S osm2pgsql.style --hstore-all -d $db -a -H localhost update.osc
rm -f update.osc update.osm

echo "Done!"
