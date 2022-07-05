(
	echo "Getting daylight $1 planet file"
	wget -c --quiet https://daylight-map-distribution.s3.amazonaws.com/release/v$1/planet-v$1.osm.pbf
	echo "Determining starting id for renumber"
	osmium fileinfo -e -t node -g data.maxid.nodes planet-v$1.osm.pbf > max-id-planet-v$1.txt
) &\
(
	(
		echo "Getting daylight $1 buildings file"
		wget -c --quiet https://daylight-map-distribution.s3.amazonaws.com/release/v$1/ms-ml-buildings-v$1.osc.bz2
	) &\
	(
		echo "Getting daylight $1 admin file"
		wget -c --quiet https://daylight-map-distribution.s3.amazonaws.com/release/v$1/admin-v$1.osc.bz2
	) &\
	wait
	echo "Sorting and merging $1 admin and buildings files"
	osmium sort --progress -v  --output merged-sorted-oscs-v$1.osm.pbf admin-v$1.osc.bz2 ms-ml-buildings-v$1.osc.bz2 --overwrite
) &\
wait

export MAX_ID=`cat max-id-planet-v$1.txt`
export START_ID=$((MAX_ID + 1))
echo "Renumber starting ID is $START_ID"

echo "Renumbering merged $1 file"
osmium renumber --progress -v --start-id=$START_ID --output merged-renumbered-oscs-v$1.osm.pbf  merged-sorted-oscs-v$1.osm.pbf --overwrite

echo "Determining starting id for dispute renumber"
osmium fileinfo -e -t node -g data.maxid.nodes merged-renumbered-oscs-v$1.osm.pbf > max-id-disputes-v$1.txt

export MAX_DISPUTE_ID=`cat max-id-disputes-v$1.txt`
export START_DISPUTE_ID=$((MAX_DISPUTE_ID + 1))
echo "Renumber disputes starting ID is $START_DISPUTE_ID"
osmium renumber --progress -v --start-id=$START_DISPUTE_ID --output v$1_renumbered_filtered_disputes.pbf filtered_disputes.pbf --overwrite

echo "Concatenating planet file with merged renumbered file"
osmium apply-changes -v --output planet-v$1-plus-buildings-admin-filtered-disputes-renumbered.osm.pbf planet-v$1.osm.pbf merged-renumbered-oscs-v$1.osm.pbf v$1_renumbered_filtered_disputes.pbf  --overwrite
md5sum planet-v$1-plus-buildings-admin-filtered-disputes-renumbered.osm.pbf > planet-v$1-plus-buildings-admin-filtered-disputes-renumbered.osm.pbf.md5
aws s3 cp --acl public-read planet-v$1-plus-buildings-admin-filtered-disputes-renumbered.osm.pbf.md5 s3://nextzen-tile-assets-us-east-1/planet-v$1-plus-buildings-admin-filtered-disputes-renumbered.osm.pbf.md5
aws s3 cp --acl public-read planet-v$1-plus-buildings-admin-filtered-disputes-renumbered.osm.pbf s3://nextzen-tile-assets-us-east-1/planet-v$1-plus-buildings-admin-filtered-disputes-renumbered.osm.pbf &
