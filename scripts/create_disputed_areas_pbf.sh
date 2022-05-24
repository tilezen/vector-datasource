# This creates a pbf with just the disputed areas as well as a kashmir specific pbf for testing.
# Run with the daylight version number as the input.

osmium extract -s smart planet-v$1-plus-buildings-admin-filtered-disputes-renumbered.osm.pbf -p collected_disputes.geojson  -o $1_disputed_areas.pbf --overwrite -S types=any
md5sum $1_disputed_areas.pbf > $1_disputed_areas.pbf.md5
aws s3 cp --acl public-read $1_disputed_areas.pbf.md5 s3://nextzen-tile-assets-us-east-1/$1_disputed_areas.pbf.md5
aws s3 cp --acl public-read $1_disputed_areas.pbf s3://nextzen-tile-assets-us-east-1/$1_disputed_areas.pbf
