**Tilezen** loves contributions from community members like you! Contributions come in many different shapes and sizes. In this file we provide guidance around two of the most common types of contributions: opening issues and opening pull requests.

# Community Values

We ask that you are respectful when contributing to Tilezen or engaging with our community. As a community, we appreciate the fact that contributors might be approaching the project from a different perspective and background. We hope that beginners as well as advanced users will be able to use and contribute back to Tilezen. We want to encourage contributions and feedback from all over the world, which means that English might not be a contributor's native language, and sometimes we may encounter cultural differences. Constructive disagreements can be essential to moving a project forward, but disrespectful language or behavior will not be tolerated.

Above all, be patient, be respectful, and be kind!

# Submitting Issues

Most issues for Tilezen are housed in the [Tilezen/vector-datasource](https://github.com/Tilezen/vector-datasource) repo. Before opening an issue, be sure to search the repository to see if someone else has asked your question before. If not, go ahead and [open a new issue](https://github.com/Tilezen/vector-datasource/issues/new).

## Submitting technical bugs

When submitting bug reports, please be sure to give us as much context as possible so that we can reproduce the error you encountered. Be sure to include:

- System conditions (operating system, browser, etc), if you're running from source
- Steps to reproduce
- Expected outcome
- Actual outcome
- Screenshots, if applicable
- Code that exposes the bug, if you have it (such as a failing test or a basic script)

## Submitting issues around vector tile quality

It's important to get feedback about the quality of local tile results. Your local knowledge will make it easier for us to understand the problem. When submitting issues be sure to include details like:

- Where in the world you were looking:
  - A placename and zoom, or
  - Zoom, latitude, and longitude, or
  - Tile URL, e.g.: http://vector.mapzen.com/osm/all/10/518/352.topojson, with the feature ID and/or tile layer, if available
- Your expected result!
- Your actual result :(


# Pull Requests Welcome!

## Project standards overview

Tilezen has several miscellaneous standards:

- we follow [PEP8](https://www.python.org/dev/peps/pep-0008/) coding style for Python and use [Flake8](http://flake8.pycqa.org/en/latest/) to enforce those conventions
- we *love* tests, [check them out](https://github.com/tilezen/vector-datasource/tree/master/integration-test)
- we use [CircleCI](https://circleci.com/gh/mapzen/vector-datasource) for continuous integration testing
- we use [semver](http://semver.org/) for package versioning

All unit tests in a project will be automatically invoked when you commit to an existing project; make sure they pass!

## Active contributors

We'll gladly invite active contributors to become members of the [Tilezen organization](https://github.com/Tilezen). New members will gain direct write permissions, *and with great power comes great responsibility*.

## Project overview (what to change, where)

Generally speaking there are three aspects of developing vector tiles.

- Configuring project setup, see [wiki page](https://github.com/tilezen/vector-datasource/wiki/Mapzen-Vector-Tile-Service)
- Updating database properties (can be done ahead of time or at runtime)
- Changing how features are selected from the database (requires tileserver restart)

<div class='alert-message' style="color: #8a6d3b; background-color: #fcf8e3; padding: 15px; margin-bottom: 20px; border: 1px solid #faebcc; border-radius: 4px;">
:warning: <b>Yellow call-outs</b> like this are meant to draw your attention to an important idea or distinction you should keep in mind.
</div>

Map database in Postgres stores data from OpenStreetMap and other projects like Natural Earth and Who's On First.

When data is loaded, database [triggers](https://www.postgresql.org/docs/current/static/triggers.html) calculate if a feature is included in which layer(s), at what "minimum zoom", and other Mapzen specific "mz" properties.

When modifying the logic below, we'll need to update our Postgres functions, migrate the data, and cut new tiles.

<div class='alert-message' style="color: #8a6d3b; background-color: #fcf8e3; padding: 15px; margin-bottom: 20px; border: 1px solid #faebcc; border-radius: 4px;">
:warning: <b>COMMON TERMS</b>
<ul>
<li><b>Vector tiles</b> (or just "tiles") allow bite sized access to large geographic databases with "raw" vector geometries and properties instead of rendered raster images.</li>
<li><b>Map features</b> (or just "feature") are individual map features, commonly with a name, geometry, and additonal properties like unique ID and source. Example include individual roads, landuse polygons, or business icons.</li>
</ul>
</div>

### Changing tile content in the vector-datasource repo

Tile **layers** are configured in a root `queries.yaml` file. This file  specifies which `jinja` template to use per layer, and also specifies post-processing via Python transforms. Individual database **features** are "filtered" into tiles per layer based on `yaml` files.

Typical tile content changes occur at the **yaml** level, but there are 4 levels total:

- **yaml** files determine which **features** are included in a tile layer by specifying a series of source data _filters_ and _property_ value rules, the most import of which are a feature's `kind` and `min_zoom`.
- **jinja templates** These filter & property rules get folded into **sql** functions, which are generated via **layer** templates. Some sql functions are run in the database _before_ a tile is requested (for properties like `min_zoom`) and others are run _as_ a tile is requested (like `kind`).
- **Python** post-processing occurs per feature and across layers once a set of features has been returned for a given tile, which is useful for more involved logic.
- **layers** are specified in the root `queries.yaml`. This file  specifies which **jinja** template to use per layer, and also specifies per layer post-processing **Python** transforms.


The **yaml** configuration files establish which features are included per layer, and the **jinja** templates are better suited for rules that apply to all features in a layer.

To recap, with examples:

- **yaml** files are located in the `yaml/` directory. Example: [pois.yaml](yaml/pois.yaml)
- **jinja** files are located in the `queries/` directory. Example: [pois.jinja](queries/pois.jinja).
- **Python** files are located in the `vectordatasource/` directory. Example: [transform.py](vectordatasource/transform.py).
- **layers** are specified in [queries.yaml](queries.yaml).

<div class='alert-message' style="color: #8a6d3b; background-color: #fcf8e3; padding: 15px; margin-bottom: 20px; border: 1px solid #faebcc; border-radius: 4px;">:warning: <b>NOTE:</b> Generally perform maintenance on pre-existing jinja filters or optionally migrate them to the newer YAML format.</div>


### Serving tiles in the tileserver repo

Listens for API requests on localhost, which are in the format of `layer/z/x/y.ext`.

When tileserver hears a request it asks Postgres for "the stuff" inside that tile's bounding box, configured via the `queries.yaml` layers file, **jinja2** templates, **Python** transforms, and per feature **sql** functions generated from the **yaml** filter files.

<div class='alert-message' style="color: #8a6d3b; background-color: #fcf8e3; padding: 15px; margin-bottom: 20px; border: 1px solid #faebcc; border-radius: 4px;">:warning: <b>NOTE:</b> You must restart tileserver when vector-datasource <b>layers</b> are updated in <a href="queries.yaml">queries.yaml</a>.</div>

**Other considerations**

- **yaml** updates don't require restart (but do require a **database migration**, see below).
- **jinja** updates don't require restarting tileserver; they are re-read on request during development.
- **Python** updates don't require restarting tileserver; they are re-read on request during development.

**DATA MIGRATION:** Changes to layer **yaml** files will require at a minimum reloading the **sql** functions. This is sufficient if only the `kind` or any output properties have changed. But for `min_zoom` changes the affected features will need to be recalculated, probably via a data migration. This topic is covered in [further detail](CONTRIBUTING.md#4-edit-database-or-query-logic) below.

## Let's do this!

We'll cover the following topics in the next sections:

- [Choose an issue to work on](CONTRIBUTING.md#1-choose-an-issue-to-work-on)
- [Do your work in a local branch](CONTRIBUTING.md#2-create-a-new-branch)
- [Create a new test](CONTRIBUTING.md#3-create-a-new-test)
- [Edit database &/or query logic](CONTRIBUTING.md#4-edit-database-or-query-logic)
- [Verify the new logic by running the test](CONTRIBUTING.md#5-verify-the-new-logic-by-running-the-test)
- [Perform any modifications, as necessary](CONTRIBUTING.md#6-perform-any-modifications-as-necessary)
- [Update data migrations](CONTRIBUTING.md#7-update-data-migrations)
- [Update documentation](CONTRIBUTING.md#8-update-documentation)
- [Push your local branch to the server](CONTRIBUTING.md#9-push-your-local-branch-to-the-server)
- [Submit a Pull Request (PR)](CONTRIBUTING.md#10-submit-a-pull-request-pr)

### 1. Choose an issue to work on

We have a backlog of issues, but they are also grouped into milestones and tracked with [Waffle board](https://waffle.io/tilezen/vector-datasource).

When picking an issue from the Ready column for the active milestone, self assign it to let other people know you'll be working on it and move it to the In Progress column.

If you propose to work on an issue in the Backlog but what to confirm some details add a comment to the issue or ask about it in Slack.

### 2. Create a new branch

Ensure you're on the master branch to establish a clean history:

```bash
git checkout master
```

Ensure your `master` branch is up-to-date with the server:

```bash
git pull
```

You will need a descriptive name for your new branch, and one way to do that is concatenate your user name, any relevant issue number(s) and a brief description, for example `olga/875-camp-ground-zoom`. Then create a new branch using `git checkout -b <branchname>`, like so:

```bash
git checkout -b olga/875-camp-ground-zoom
```

Congratulations, now you have a local branch!

We're going to push our work to the server eventually (so other people can see your work, and so you have a backup), so let's make sure that works now:

```bash
git push
```

NOTE: Your first push for a branch might require additional details:

```bash
git push --set-upstream origin olga/875-camp-ground-zoom
```

### 3. Create a new test

Create a new test for the issue in `integration-test` dir. Sometimes it's helpful to look thru the existing tests to find one that is a close match to the pattern and start there.

- Create new test file
- You'll need a specific OpenStreetMap feature ID to test against
- You'll need the coordinates (z/x/y) of a map tile containing that feature
- Ensure that test data is loaded into your local database
- Ensure tileserver is running!
- Run the test

<div class='alert-message' style="color: #8a6d3b; background-color: #fcf8e3; padding: 15px; margin-bottom: 20px; border: 1px solid #faebcc; border-radius: 4px;">:warning: <b>Remember</b> to note the openstreetmap.org URL for your test feature. You'll store that in your test file as a comment for other humans to read later when the test might fail, and for the continuous integration computer to download that feature and verify your work.</div>


#### Example test


```python
# http://www.openstreetmap.org/way/431725967
assert_has_feature(
   16, 10959, 25337, 'landuse',
   { 'kind': 'camp_site'})
```

#### Missing a database feature?

Sometimes you'll find a feature in OverPass that is more recent than your local database, or is in a region outside your loaded Metro Extract.

To load that feature, specify the URL and the database to import into:


```bash
./test-data-update-osm.sh http://www.openstreetmap.org/way/431725967 osm
```

**Ensure tileserver is running locally:**

Launch tileserver from within the tileserver directory in a new terminal window. As tileserver is usually installed alongside vector-datasource `cd ../tileserver` will usually get you there.


```bash
python tileserver/__init__.py config.yaml
```

**Example test run:**

Back in the `vector-datasource` directory in your first terminal window, run your new test to make sure it **fails** using the existing config:


```bash
python integration-test.py local integration-test/875-camp-grounds-zoom.py
```

Once it fails, we'll update our logic in step 4 below so it passes.

<div class='alert-message' style="color: #8a6d3b; background-color: #fcf8e3; padding: 15px; margin-bottom: 20px; border: 1px solid #faebcc; border-radius: 4px;">:warning: <b>So what's happening here?</b> The <code>integration-test.py</code> script is asking tileserver for that specific tile to test with on your `local` machine. But before that runs, we're setting up a temporary database to load the specified OpenStreetMap feature into. Once the tile is received, we run the python based test, in this example that's <code>160-motorway-junctions.py</code> in the <code>integration-test</code> directory.</div>

Now the gory details...

#### Find example feature in the raw data to test against

There are two options to identify test features:

1. **Query local database** using psql on the command line or PGAdmin app.
2. **Query remote OpenStreetMap database** using [Overpass Turbo](http://overpass-turbo.eu/).

Confused about which tags to use? Read up on the OSM wiki ([example](https://taginfo.openstreetmap.org/tags/highway=services)) and confirm actual usage in TagInfo.

##### Overpass Turbo example

To find an example feature in OpenStreetMap search [overpass-turbo](http://overpass-turbo.eu/) for specific tags. Here's a sample query (assuming you've zoomed the map to an interesting area like the greater San Francisco metropolitan area):


```
/*
This has been generated by the overpass-turbo wizard.
The original search was:
“highway=rest_area”
*/
[out:json][timeout:25];
// gather results
(
  // query part for: “highway=rest_area”
  node["highway"="rest_area"]({{bbox}});
  way["highway"="rest_area"]({{bbox}});
  relation["highway"="rest_area"]({{bbox}});
);
// print results
out body;
>;
out skel qt;
```

<div class='alert-message' style="color: #8a6d3b; background-color: #fcf8e3; padding: 15px; margin-bottom: 20px; border: 1px solid #faebcc; border-radius: 4px;">:warning: <b>NOTE:</b> Update the above example for your tag (e.g.: `"highway"="rest_area"`)!</div>

##### Determine which tile the feature should appear in for your test

Once you find a result you like, click on it's map marker to pull up the info window. Following the link from Overpass take you to a page like:

- http://www.openstreetmap.org/node/1114457089

On that new web page, zoom the map out to the desired **min zoom** of the feature (it's usually specified in the Issue description in Github), then right click on the map near the marker (but not on the marker!). Then you'll use your web browsers debug tools to "Inspect element" and look for the `leaflet-map-pane` and follow that down till you find the named raster tile file which encodes the tile coordinate.

##### Alternative method if feature is already in Mapzen tiles

Use one of the Mapzen house styles, like Bubble Wrap, to determine the tile:

- http://tangrams.github.io/bubble-wrap/#7/37.606/-121.943

Click on a feature to "view more", then click "view tile data".

<img width="375" alt="screen shot 2016-07-18 at 18 07 06" src="https://cloud.githubusercontent.com/assets/853051/16935233/8fe8f6a8-4d12-11e6-9ce0-90ac40b185fa.png">

<img width="372" alt="screen shot 2016-07-18 at 18 07 14" src="https://cloud.githubusercontent.com/assets/853051/16935232/8fe83c0e-4d12-11e6-86f7-b16eebc22f84.png">

If you're modifying a feature, it can be helpful to search in the JSON response for the thing you want to change to confirm it's the right tile. If you're adding a new feature, you could search for something you know should be in the tile already to confirm you got the right one.

<div class='alert-message' style="color: #8a6d3b; background-color: #fcf8e3; padding: 15px; margin-bottom: 20px; border: 1px solid #faebcc; border-radius: 4px;"><b>TIP:</b> It's helpful to install a browser extension to view the JSON formatted. <a href="https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc">jsonview</a> for Chrome is pretty good.</div>

**Specific map tile to test with:**

- http://vector.mapzen.com/osm/all/7/20/49.topojson

But the tests require this to be formatted like:

- `7, 20, 49`

#### Common test types

The python file `integration-test.py` contains several useful tests:

- `assert_has_feature`
- `assert_no_matching_feature`
- `assert_at_least_n_features`
- `assert_feature_geom_type`


### 4. Edit database &/or query logic

Edit the YAML file corresponding to the layer. In this case we're modifying the `landuse.yaml` to add a new filter that looks for OpenStreetMap feature tagged `tourism=camp_site` and assigns them a `min_zoom` based on the feature area of at least 16 but up to zoom 13 depending on the feature's area and assigning a Tilezen kind of **camp_site**.


```yaml
- filter: {tourism: camp_site}
  min_zoom: GREATEST(LEAST(zoom, 16), 13)
  output: {kind: camp_site}
```

#### Update the database properties

Once you make your edits to the YAML file you need to update the database. To recreate SQL functions in Postgres run:


```bash
cd data/migrations && python create-sql-functions.py | psql osm
```

Because some properties (like `min_zoom`) in the database are pre-computed, we need to update records to recalculate that using the updated functions. We call this "data migration", see some examples below.

1. Prototype migration in PGAdmin (this step)
2. Update data migration SQL files for the release (see step 7 below)

<div class='alert-message' style="color: #8a6d3b; background-color: #fcf8e3; padding: 15px; margin-bottom: 20px; border: 1px solid #faebcc; border-radius: 4px;">:warning: <b>Advanced topic:</b> If you modify any other raw functions in the data directory, you'll also need to run <code>psql -f data/functions.sql osm</code>.</div>

#### Update the query configuration

Continuing our `camp_site` example from the previous section in Postgres run:

```sql
SET
  mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_polygon.*),
  mz_landuse_min_zoom = mz_calculate_min_zoom_landuse(planet_osm_polygon.*)
WHERE
  tourism = 'camp_site';
```

##### Debugging filters

Sometimes you need to debug why a feature appears one of multiple possible representations:

```sql
SELECT
  osm_id, name, mz_landuse_min_zoom, mz_pois_min_zoom
FROM planet_osm_polygon
WHERE
  osm_id IN (237314510, 417405356)
```

If you have a continent or planet sized database sometimes it's helpful to preview the changes in a smaller area of interest. For example: roads using a smaller viewport in latitude & longitude coordinates to Web Mercator meters:

```sql
UPDATE planet_osm_line
  SET mz_road_level = mz_calculate_road_level(highway, railway, aeroway, route, service, aerialway, leisure, sport, man_made, way, name, bicycle, foot, horse, tags->'snowmobile', tags->'ski', osm_id)
  WHERE
    highway IN ('pedestrian', 'living_street', 'track', 'path', 'cycleway', 'footway', 'steps') AND
    way && ST_Transform(ST_SetSrid(ST_MakeBox2D(ST_MakePoint(-124.03564453125, 36.59788913307022), ST_MakePoint(-117.333984375, 39.06184913429154)), 4326), 3857);
```

### 5. Verify the new logic by running the test

Run the test, hopefully it passes now! You'll need to run the test from the project's root directory, you may need to `cd ../../` to get back there after step 4 above.

```bash
python integration-test.py local integration-test/875-camp-grounds-zoom.py
```

**Example output:**

```python
python integration-test.py local integration-test/875-camp-grounds-zoom.py
config_url=None
[   1/1] PASS: 'integration-test/875-camp-grounds-zoom.py'
PASSED ALL TESTS.
```

If the test failed like so:

```python
python integration-test.py local integration-test/875-camp-grounds-zoom.py
config_url=None
[   1/1] FAIL: 'integration-test/875-camp-grounds-zoom.py'
FAILED 1 TESTS. For more information, see 'test.log'
```

You can investigate why the test failed by printing out the full debug:

```bash
cat test.log
```

<div class='alert-message' style="color: #8a6d3b; background-color: #fcf8e3; padding: 15px; margin-bottom: 20px; border: 1px solid #faebcc; border-radius: 4px;">:warning: <b>NOTE:</b> It's best practice to run your own test AND to also confirm that all other tests are still passing before submitting a pull request. It's possible that you might need to run an overall database migration to achieve this locally, or you can rely on CircleCI to run all the tests for you in your branch by pushing it to the server.</div>

#### Some tests require tileserver restart

A minority of issues will require updating the `queries.yaml` file. In those cases you'll also need to restart tileserver to reload this file.

First, switch to the Terminal session where tileserver is running and kill it with a `contrl-c` keyboard press.

Then relaunch tileserver from within the tileserver directory:

```bash
python tileserver/__init__.py config.yaml
```

Then run your test starting at the top of step 5 above.

### 6. Perform any modifications, as necessary

Rinse and repeat, rewrite your code. Don't be afraid to ask for help!

### 7. Update data migrations

Once you've finished testing your new database logic in step 4 above you need to record that that same SQL in modified form in `data/migrations/` to ensure someone with an earlier database configuration can catch up with you. (Migrations are reset for each Tilezen release.)

Continuing the `camp_site` example, edit the following in the `data/migrations/v1.0.0-polygon.sql` file:

<div class='alert-message' style="color: #8a6d3b; background-color: #fcf8e3; padding: 15px; margin-bottom: 20px; border: 1px solid #faebcc; border-radius: 4px;">:warning: <b>NOTE:</b> The exact file name for the migration will change, matching the <i>upcoming</i> release version.</div>

```sql
UPDATE
   planet_osm_polygon
    SET mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_polygon.*)
    WHERE
     (barrier = 'toll_booth' OR
      highway IN ('services', 'rest_area') OR
      tourism = 'camp_site')
      AND COALESCE(mz_poi_min_zoom, 999) <> COALESCE(mz_calculate_min_zoom_pois(planet_osm_polygon.*), 999);

UPDATE
   planet_osm_polygon
   SET mz_landuse_min_zoom = mz_calculate_min_zoom_landuse(planet_osm_polygon.*)
   WHERE
     (highway IN  ('services', 'rest_area') OR
      barrier IN ('city_wall', 'retaining_wall', 'fence') OR
      historic = 'citywalls' OR
      man_made = 'snow_fence' OR
      waterway = 'dam' OR
      tourism = 'camp_site' OR
      "natural" IN ('forest', 'park'))
      AND COALESCE(mz_landuse_min_zoom, 999) <> COALESCE(mz_calculate_min_zoom_landuse(planet_osm_polygon.*), 999);
```

<div class='alert-message' style="color: #8a6d3b; background-color: #fcf8e3; padding: 15px; margin-bottom: 20px; border: 1px solid #faebcc; border-radius: 4px;">:warning: <b>NOTE:</b> Occasionally two PRs will land at the same time and you'll need to clean up the SQL to address a merge conflict. To prevent this, use more new lines in your SQL.</div>


#### Migration details

OpenStreetMap related migrations are recorded in the following files:

* `v1.0.0-point.sql`
* `v1.0.0-line.sql`
* `v1.0.0-polygon.sql`

Migrations for other data sources like Natural Earth and Who's On First go in:

* `v1.0.0-other-tables.sql`

<div class='alert-message' style="color: #8a6d3b; background-color: #fcf8e3; padding: 15px; margin-bottom: 20px; border: 1px solid #faebcc; border-radius: 4px;">:warning: <b>NOTE:</b> The exact file names for the migration will change, matching the <i>upcoming</i> release version.</div>

#### Example database SQL

Here's an example out of the `v1.0.0-point.sql` file:

Updating a simple **point** feature:

```sql
UPDATE planet_osm_point
  SET mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_point.*)
  WHERE shop IN ('outdoor');
```

A more complicated **point** example:

```sql
UPDATE
  planet_osm_point
  SET mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_point.*)
  WHERE
    (barrier = 'toll_booth' OR
     highway IN ('services', 'rest_area'))
    AND COALESCE(mz_poi_min_zoom, 999) <> COALESCE(mz_calculate_min_zoom_pois(planet_osm_point.*), 999);
```

Updating a simple **line** feature:

```sql
UPDATE planet_osm_line
  SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(planet_osm_line.*)
  WHERE
    waterway = 'dam';
```

Updating a simple **polygon** feature:

```sql
UPDATE planet_osm_polygon
  SET mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_polygon.*)
  WHERE shop IN ('outdoor');
```

<div class='alert-message' style="color: #8a6d3b; background-color: #fcf8e3; padding: 15px; margin-bottom: 20px; border: 1px solid #faebcc; border-radius: 4px;">:warning: <b>NOTE:</b> Some features can have a POI "label" and a landuse polygon, so calculate both!</div>

When we calculate both the POIs and the landuse min zoom:

```sql
UPDATE planet_osm_polygon
  SET mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_polygon.*),
      mz_poi_min_zoom = mz_calculate_min_zoom_landuse(planet_osm_polygon.*)
  WHERE shop IN ('outdoor');
```

### 8. Update documentation

Everything good? time to update the docs! Generally this is in the [docs/layer.md](docs/layer.md) file in the various layer sections to specify new properties and new kind values.

Since `camp_site` was already in the `pois` layer, we only need to document it's addition to the alphabetical list of `landuse` kinds:

```
  * `bridge`
  * `camp_site`
  * `caravan_site`
```

<div class='alert-message' style="color: #8a6d3b; background-color: #fcf8e3; padding: 15px; margin-bottom: 20px; border: 1px solid #faebcc; border-radius: 4px;">:warning: <b>NOTE:</b> Project documentation is <a href="https://mapzen.com/documentation/vector-tiles/layers/">publicly accessible</a> and documents the API promises the service makes.</div>

### 9. Push your local branch to the server

First let's commit our changes. Let's confirm which files changed:


```bash
git status
```

You can also do a `git diff` on each file to determine if you meant to change or insert logic. Once you've confirmed the changes...

For each, commit using a specific commit message. The first should use the "Connects to #issuenum" format to link up the PR to the original issue in Waffle.io.


```bash
git commit -m 'Connects to #875 to add camp_site polygons' filename
```

_NOTE: Subsequent commit messages can be more generic._

Make sure you have a clean merge by pulling down the latest master by checking out master:


```bash
git checkout master
```

Fetch latest changes from the server:


```bash
git pull origin master
```

Go back to your branch:


```bash
git checkout olga/875-camp-ground-zoom
```

Rebase (compare) it with master:


```bash
git rebase master
```

And resolve any funk, as necessary.

Then push to the server so other people can see your work. (If this is a large change over multiple days, please push the server once a day so your work is backed up.)


```bash
git push
```

NOTE: Your first push for a branch might require additional details:


```bash
git push --set-upstream origin olga/875-camp-ground-zoom
```

### 10. Submit a Pull Request (PR)

Back on Github.com load the project page and notice there's a button suggested you create a PR for your active branch. Press that green button. Need help? [Github docs](https://help.github.com/articles/creating-a-pull-request/) have you covered.

In the PR form, give it a good title that ties in with the original Issue title. In the comment section summarize the work you did to resolve the issue and indicate you added tests, data migrations, and updated the documentation.

A Tilezen team member will review the PR for you, either merging it right away or following up with questions.

If the review leads to code modifications those should be done in same branch and the PR will automatically update with subsequent commits to the branch.

<div class='alert-message' style="color: #8a6d3b; background-color: #fcf8e3; padding: 15px; margin-bottom: 20px; border: 1px solid #faebcc; border-radius: 4px;">:clap: Good luck, and <b>thank you</b> for contributing!</div>
