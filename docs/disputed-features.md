## Disputed borders

We use [Daylight Distribution](https://daylightmap.org/) over straight OpenStreetMap data for our data source. Daylight has quality control checks applied to it that limits the possibility of major vandalism getting onto the map. Additionally, Daylight provides optional 'sidecars' containing data such as ML based roads and buildings and other open source data sets. One potential drawback when considering Daylight is that the data will always be a month or so behind live OSM.

Daylight does not currently include the disputed borders that we need to render on the map. Instead, we download and patch them onto the pbf ourselves. This approach offers some advantages, as we can iterate on the borders as necessary without relying on Daylight to update, however, the mismatch between Daylight and live OSM can require some additional local edits to render properly.

We have a two-step process to patching in these disputes. First, we download and assemble a `.osm` file that contains all the dispute relations we are interested in. Then we convert and apply this file to the Daylight pbf using a script that assembles all the sidecar files into a final pbf.


### Building a dispute patch
1. When Daylight has a new release, it is best to start with a fresh disputed relation package. Using the overpass query in `disputed_relation_overpass_query.txt` run an overpass query to get the data.
2. Click export and select download as raw osm data
3. Open the file in JOSM and compare this file with the previous version. Features may have been altered or deleted since the last build and updates may be necessary. If there are fixes necessary, make and upload them.
4. Some edits may need to be made locally on the patch without committing to OSM itself, such as when daylight borders are out of alignment with live OSM. These edits can be done in JOSM and the file then just saved without uploading. The reverter plugin is handy for realigning borders that have been moved.
   *  Note: This will only work for modifying or deleting existing features. If features are created, they must be uploaded to OSM for osmium to work correctly.
5. If you need to update features within the patch it is safest to select the relation or way then run update selection. This will limit the chances of unintentional changes being introduced to the .osm file once it’s been initially downloaded.
6. The dispute patch may be used to bring in other features or updates as needed, such as missing labels. Just download the feature into the layer and save.
7. Save the new patch file as something like `filtered_disputes.1.10.osm` using the desired Daylight version and upload to the [`scripts`](https://github.com/tilezen/vector-datasource/tree/master/scripts) folder for tracking.

### Patching Daylight
1. Run osmium cat to convert the .osm file to a pbf. The script expects the name to be `filtered_disputes.pbf`. [filtered_disputes_example.osm](https://github.com/tilezen/vector-datasource/tree/master/scripts/filtered_disputes_example.osm) can be used to try out the process.
   * `osmium cat filtered_disputes.1.10.osm -o filtered_disputes.pbf --overwrite`
2. Scp the file to the server
   * `scp -i tilezen.pem filtered_disputes.pbf  ubuntu@1.2.3.4:/mnt/username/`
3. ssh onto the server and navigate to /mnt/username/
4. Run [`parallel_create_planet_file.sh`](https://github.com/tilezen/vector-datasource/tree/master/scripts/parallel_create_planet_file.sh) with a daylight version to build a fresh pbf. This will take some time.
   *  example usage: `sh parallel_create_planet_file.sh 1.10`
5. Once the `parallel_create_planet_file.sh` has been run on a Daylight version at least once, you can use the [`patch_disputes_into_pbf.sh`](https://github.com/tilezen/vector-datasource/tree/master/scripts/scripts/patch_disputes_into_pbf.sh) script to repatch the disputes if changes need to be made. This script just cuts out some of the early steps to save time.
   * example usage: `sh patch_disputes_into_pbf.sh 1.10`
6. If you want to test out disputes in a build, run [`create_disputed_areas_pbf.sh`](https://github.com/tilezen/vector-datasource/tree/master/scripts/create_disputed_areas_pbf.sh) to create a smaller pbf with just the data within disputed areas.
   * example usage: `sh create_disputed_areas-pbf.sh 1.10`


## Disputed capitals

Some cities are considered different administrative levels depending on a country's viewpoint. One country may consider a city to be a regional or country capital while a disputant does not. Natural Earth has this information in the `ne_10m_populated_places` table for affected countries in the `FCLASS_XX` columns. Using Wikidata ID tags, the NE `FCLASS_XX` data is joined to the OSM feature to create output kinds of `regional_capital:xx` or `country_capital:xx` with a true or false value to allow for different rendering options.

This should all happen automatically in Tilezen, however, Wikidata ID tag changes in OSM could cause breakages in the join. In this instance, a locally applied patch to Daylight like described in the disputed border section may be needed or an update to NE if the OSM change is valid.
