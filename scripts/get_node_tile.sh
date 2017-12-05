#!/usr/bin/env bash

# This script downloads an OSM node by ID and returns the z16 tile its in.
# Requirements: osmium-tool, curl, and python.

set -e

OPL=$(curl -s "https://api.openstreetmap.org/api/0.6/node/$1" | osmium cat -F osm -f opl -)

X=$( echo $OPL | cut -d' ' -f9 | tail -c +2)
Y=$( echo $OPL | cut -d' ' -f10 | tail -c +2)

xtile=$(python -c "print( int( (2.0**16) * ($X+180)/360 ) )")
ytile=$(python -c "import math;
lat_rad=math.radians($Y)
print(int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * 2.0**16))")

echo "16/$xtile/$ytile"
