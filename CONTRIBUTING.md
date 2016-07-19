<html lang="en-us">
  <head>
    <style>
		.alert-message {
			color: #8a6d3b;
			background-color: #fcf8e3;
			padding: 15px;
			margin-bottom: 20px;
			border: 1px solid #faebcc;
			border-radius: 4px;
		}
    </style>
  </head>

  <body>

**Tilezen** loves contributions from community members like you! Contributions come in many different shapes and sizes. In this file we provide guidance around two of the most common types of contributions: opening issues and opening pull requests.

# Community Values

We ask that you are respectful when contributing to Tilezen or engaging with our community. As a community, we appreciate the fact that contributors might be approaching the project from a different perspective and background. We hope that beginners as well as advanced users will be able to use and contribute back to Tilezen. We want to encourage contributions and feedback from all over the world, which means that English might not be a contributor's native language, and sometimes we may encounter cultural differences. Contructive disagreements can be essential to moving a project forward, but disrespectful language or behavior will not be tolerated.

Above all, be patient, be respectful, and be kind!

# Submitting Issues

Most issues for Tilezen are housed in the [Tilezen/vector-datasource](https://github.com/Tilezen/vector-datasource) repo. Before opening an issue, be sure to search the repository to see if someone else has asked your question before. If not, go ahead and [open a new issue](https://github.com/Tilezen/vector-datasource/issues/new).

## Submitting technical bugs

When submitting bug reports, please be sure to give us as much context as possible so that we can reproduce the error you encountered. Be sure to include:

- System conditons (operating system, browser, etc), if you're running from source
- Steps to reproduce
- Expected outcome
- Actual outcome
- Screenshots, if applicable
- Code that exposes the bug, if you have it (such as a failing test or a basic script)

## Submitting issues around vector tile quality

It's important to get feedback about the quality of local tile results. Your local knowledge will make it easier for us to understand the problem. When submitting issues be sure to include:

- Where in the world you were looking (a placename &/or zoom, latitude, longitude)
- Your tile query
- Your expected result
- Your actual result


# Pull Requests Welcome!

## Project standards overview

Tilezen has several miscellaneous standards:

- we write idomatic Python code and use Flake to QA that code.
- we *love* tests, [check them out](https://github.com/tilezen/vector-datasource/tree/master/integration-test)
- we use [CircleCI](https://circleci.com/gh/mapzen/vector-datasource) for continuous integration
- we use [semver](http://semver.org/) for package versioning

All  unit tests in a project will be automatically invoked when you commit to an existing project; make sure they exit successfully!

## Active contributors

We'll gladly invite active contributors to become members of the [Tilezen organization](https://github.com/Tilezen). New members will gain direct write permissions, *and with great power comes great responsibility*.

## Project overview (what to change, where)

Generally speaking there are three aspects of developing vector tiles.

- Configuring project setup, see [wiki page](https://github.com/tilezen/vector-datasource/wiki/Mapzen-Vector-Tile-Service)
- Updating database properties (can be done ahead of time or at runtime)
- Changing how features are selected from the database (requires TileServer restart)

<div class='alert-message'>
Yellow call-outs like this are meant to draw your attention to an important idea or distinction you should keep in mind.
</div>

Map database in Postgres stores data from OpenStreetMap and other projects like Natural Earth and Who's On First.

When data is loaded, database "triggers" calculate if a feature is included in which layer(s), at what "minimum zoom", and other Mapzen specific "mz" properties.

When modifying the logic below, we'll need to update our Postgres functions, migrate the data, and cut new tiles.

### Changing tile content in the vector-datasource repo

Most content changes (eg: adding a new kind of feature) only require a database modification. Content changes are configured using YAML files which specify which database features are "filtered" and outputed in tiles. The location for these content filters is in the `yaml/` directory, for example: [pois.yaml](yaml/pois.yaml).

Some preexisting feature filters are configured using an older raw SQL format in `jinja` files in the `queries/` directory. This older syntax is still helpful to select multiple feature properties across many kinds of features at once. For example, [pois.jinja](queries/pois.jinja).

<div class='alert-message'>Generally perform maintenance on pre-existing jinja filters or optionally migrate them to the newer YAML format.</div>

Additionally, the root `queries.yaml` specifies which `jinja` file to use per layer, and also specifies post-processing via Python transforms.

### Serving tiles in the TileServer repo

Listens for API requests on localhost, which are in the format of 0/0/0.ext

When TileServer hears a request it asks Postgres for "the stuff" inside that tile's bounding box, configured via the `queries.yaml` file and `.jinja2` files.

_**NOTE:** A change to one of the query files (jinja) requires TileServer to be restarted so they can be reloaded. But content filter changes (YAML) generally doesn't require restarting TileServer._


## Let's do this!

We'll cover the following topics in the next sections:

- [Choose an issue to work on](CONTRIBUTING.md#1-choose-an-issue-to-work-on)
- [Do you work in a local branch](CONTRIBUTING.md#2-create-a-new-branch)
- [Create a new test](CONTRIBUTING.md#3-create-a-new-test)
- [Edit database &/or query logic](CONTRIBUTING.md#4-edit-database-&/or-query-logic)
- [Verify the new logic by running the test](CONTRIBUTING.md#5-verify-the-new-logic-by-running-the-test)
- [Perform any modifications, if necessary](CONTRIBUTING.md#6-perform-any-modifications,-as-necessary)
- [Update data migrations](CONTRIBUTING.md#7-update-data-migrations)
- [Update documentation](CONTRIBUTING.md#8-update-documentation)
- [Push your local branch to the server](CONTRIBUTING.md#9-push-your-local-branch-to-the-server)
- [Submit a Pull Request (PR)](CONTRIBUTING.md#10-submit-a-Pull-Request-PR)

### 1. Choose an issue to work on

We have a backlog of issues, but they are also grouped into milestones and tracked with [Waffle board](https://waffle.io/tilezen/vector-datasource).

When picking an issue from the Ready column for the active milestone, self assign it to let other people know you'll be working on it.

If you propose to work on an issue in the Backlog but what to confirm some details add a comment to the issue or ask about it in Slack.

### 2. Create a new branch

Make sure your `master` branch is up-to-date with a `git pull`. Then...

Checkout a new branch, name it something descriptive like the `yourname/#issue-issue title`.

    git checkout -b olga/713-urban-areas

### 3. Create a new test

Create a new test for the issue in `integration-test` dir. Sometimes it's helpful to look thru the existing tests to find one that is a close match to the pattern and start there.

- Create new test file
- You'll need a specific OpenStreetMap feature ID to test against
- You'll need a specific map tile (0/0/0) to test with

Much of our data comes from OpenStreetMap. Are you confused about feature tagging there? Read up on it in the OSM Wiki and search TagInfo to see how common it actually is.

- https://taginfo.openstreetmap.org/tags/highway=services

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

NOTE: Update the above example for your tag (eg: `"highway"="rest_area"`)!

Once you find a result you like, click on it to pull up the info window, and follow the view on OSM.org link like so:

**Specific OSM feature to test for:**

- http://www.openstreetmap.org/node/1114457089

Zoom out to the "min_zoom" of the feature, then right click on the map near the icon, but not on the icon. Then Inspect element, and look for the `leaflet-map-pane` and follow that down till you find the raster tile.

Alternatively... Use one of the Mapzen house styles to determine the tile.

- http://tangrams.github.io/bubble-wrap/#7/37.606/-121.943

Click on a feature to "view more", then click "view tile data". It's helpful to install a browser extension to view the JSON formatted. [jsonview](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc) for Chrome is pretty good.

If you're modifying a feature it can be helpful to search in the JSON response for the thing you want to change to confirm it's the right tile. If you're adding a new feature, you could search for something you know should be in the tile already to confirm you got the right one.

**Specific map tile to test with:**

- http://vector.mapzen.com/osm/all/7/20/49.topojson

The tests require this to be formatted like:

- `7, 20, 49`

And run the test to make sure it **fails** using the existing config:

    python integration-test.py local integration-test/160-motorway-junctions.py

Once it fails, we'll update our logic in the next section so it passes.

**So what's happening here?** The `integration-test.py` script is asking TileServer for that specific tile to test with on your `local` machine. But before that runs, we're setting up a temporary database to load the specified OpenStreetMap feature into. Once the tile is received, we run the python based test, in this example that's `160-motorway-junctions.py` in the `integration-test` directory.

##### Missing a database feature?

Sometimes you'll find a feature in OverPass that is more recent than your local database, or is in a region outside your loaded Metro Extract.

    ./test-data-update-osm.sh https://www.openstreetmap.org/node/418185265 osm

### 4. Edit database &/or query logic

Tk tk tk intro

#### Update the database properties

Once you make your edits to the YAML files you need to update the database. To recreate SQL functions in Postgres run:

    cd data/migrations && python create-sql-functions.py | psql osm

Because some properties in the database are pre-computed, we need to update records to use the new functions. We call this "data migration", see some examples below.

1. Prototype it in PGAdmin
2. Record it in the migration SQL files, see later step

<div class='alert-message'>Advanced topic: if you modify any other raw functions in the data directory, you'll also need to run `psql -f data/functions.sql osm`.</div>

#### Update the query configuration

Tk tk tk body

Sometimes you'll want to investigate features in the database:

```sql
SELECT name, height, tags from planet_osm_point
  WHERE waterway = 'waterfall' AND height IS NOT NULL LIMIT 100;
```

Sometimes you need to debug why a feature appears one of multiple possible representations:

```sql
SELECT
  osm_id, name, place, mz_earth_min_zoom, mz_places_min_zoom from planet_osm_point where osm_id
IN (3178316462, 358955020, 358796350, 358761955, 358768646, 358795646)
ORDER BY
  osm_id;
```

If you have a continent or planet sized database sometimes it's helpful to preview the changes in a smaller area of interest. For example: roads using a smaller viewport in latitude & longitude to Web Mercator meters:

```sql
UPDATE planet_osm_line
  SET mz_road_level = mz_calculate_road_level(highway, railway, aeroway, route, service, aerialway, leisure, sport, man_made, way, name, bicycle, foot, horse, tags->'snowmobile', tags->'ski', osm_id)
  WHERE
    highway IN ('pedestrian', 'living_street', 'track', 'path', 'cycleway', 'footway', 'steps') AND
    way && ST_Transform(ST_SetSrid(ST_MakeBox2D(ST_MakePoint(-124.03564453125, 36.59788913307022), ST_MakePoint(-117.333984375, 39.06184913429154)), 4326), 900913);
```

### 5. Verify the new logic by running the test

This step is not necessary if only database properties were changed.

Run the test, hopefully it passes now!

    python integration-test.py local integration-test/160-motorway-junctions.py

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

<div class='alert-message'>NOTE: It's best practice to run your own test, and confirm that all other tests are still passing before submitting a PR. It's possible that you might need to run an overall database migration to achive this locally, or you can rely on CircleCI to run all the tests for you in your branch by pushing it to the server.</div>

#### Some tests require tileserver restart

A minority of issues will require updating the `queries.yaml` file. In those cases you'll also need to restart TileServer to reload this file.

Kill tileserver with a `contrl-c` keyboard press in terminal.

Then relaunch tileserver from within the tileserver directory:

```bash
python tileserver/__init__.py config.yaml
```

Then run your test like in the previous step.

### 6. Perform any modifications, as necessary

Rinse and repeat, rewrite your code.

### 7. Update data migrations

Once you've finished testing your new database logic in the steps above you need to record that that same SQL in modified form in `data/migrations/` to ensure someone with an earlier database can catch up with you. (They are reset for each release.)

OpenStreetMap related migrations:

* `v1.0.0-point.sql`
* `v1.0.0-line.sql`
* `v1.0.0-polygon.sql`

Migrations for other data sources like Natural Earth and Who's On First:

* `v1.0.0-other-tables.sql`

<div class='alert-message'>NOTE: Occasionally two PRs will land at the same time and you'll need to clean up the SQL to address a merge conflict. To prevent this, use more new lines in your SQL.</div>

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

<div class='alert-message'>Some features can have a POI "label" and a landuse polygon, so calculate both!</div>

When we calculate both the POIs and the landuse min zoom...

```sql
UPDATE planet_osm_polygon
  SET mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_polygon.*),
      mz_poi_min_zoom = mz_calculate_min_zoom_landuse(planet_osm_polygon.*)
  WHERE shop IN ('outdoor');
```

### 8. Update documentation

Everything good? time to update the docs!

Project documentation is [publicly accessable](https://mapzen.com/documentation/vector-tiles/layers/), they document the API promises the service makes.

Tk tk tk

### 9. Push your local branch to the server

First let's commit our changes. Let's confirm which files changed:

    git status

You can also do a `git diff` on each file to determine if you meant to change or insert logic. Once you've confirmed the changes...

For each, commit using a specific commit message. The first should use the "Connects to #issuenum" format to link up the PR to the original issue in Waffle.io.

    git commit -m 'Connects to #713 for urban area kind rename' filename

NOTE: Subsequent commit messages can be more generic.

Make sure you have a clean merge by pulling down the lastest master by checking out master:

    git checkout master

Fetch latest changes from the server:

    git pull origin master

Go back to your branch:

    git checkout olga/713-urban-areas

Rebase (compare) it with master:

    git rebase master

And resolve any funk, as necessary.

Then push to the server so other people can see your work. (If this is a large change over multiple days, please push the server once a day so your work is backed up.)

    git push

NOTE: Your first push for a branch might require additional details:

    git push --set-upstream origin olga/713-urban-areas

### 10. Submit a Pull Request (PR)

Back on Github.com load the project page and notice there's a button suggested you create a PR for your active branch. Press that green button.

In the PR form, give it a good title that ties in with the original issue title. In the comment section summarize the work you did to resolve the issue and indicate you added tests and updated the documentation.

A Tilezen team member will review the PR for you, either merging it right away or following up with questions.

If the review leads to code modifications those should be done in same branch and the PR will automatically update with subsequent commits to the branch.

_Good luck, and **thank you** for contributing!_

  </body>
</html>