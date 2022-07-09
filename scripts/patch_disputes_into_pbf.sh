# This patches in the dispute file to a daylight build more quickly than regenerating the entire pbf.
# It requires the parallel-create.sh script to have been run on the Daylight version already as it just runs the last part of the script.

echo "Determining starting id for dispute renumber"
osmium fileinfo -e -t node -g data.maxid.nodes merged-renumbered-oscs-v$1.osm.pbf > max-id-disputes-v$1.txt

export MAX_DISPUTE_ID=`cat max-id-disputes-v$1.txt`
export START_DISPUTE_ID=$((MAX_DISPUTE_ID + 1))
echo "Renumber disputes starting ID is $START_DISPUTE_ID"
osmium renumber --progress -v --start-id=$START_DISPUTE_ID --output v$1_renumbered_filtered_disputes.pbf filtered_disputes.pbf --overwrite

osmium apply-changes -v --output planet-v$1-plus-buildings-admin-filtered-disputes-renumbered.osm.pbf planet-v$1.osm.pbf merged-renumbered-oscs-v$1.osm.pbf v$1_renumbered_filtered_disputes.pbf  --overwrite
md5sum planet-v$1-plus-buildings-admin-filtered-disputes-renumbered.osm.pbf > planet-v$1-plus-buildings-admin-filtered-disputes-renumbered.osm.pbf.md5
aws s3 cp --acl public-read planet-v$1-plus-buildings-admin-filtered-disputes-renumbered.osm.pbf.md5 s3://nextzen-tile-assets-us-east-1/planet-v$1-plus-buildings-admin-filtered-disputes-renumbered.osm.pbf.md5
aws s3 cp --acl public-read planet-v$1-plus-buildings-admin-filtered-disputes-renumbered.osm.pbf s3://nextzen-tile-assets-us-east-1/planet-v$1-plus-buildings-admin-filtered-disputes-renumbered.osm.pbf &
