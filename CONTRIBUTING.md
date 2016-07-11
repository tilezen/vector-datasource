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

- we use [CircleCI](https://circleci.com/gh/mapzen/vector-datasource) for continuous integration
- we *love* tests, [check them out](https://github.com/tilezen/vector-datasource/tree/master/integration-test)
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

### vector-datasource

Map database in Postgres stores data from OpenStreetMap and other projects like Natural Earth and Who's On First.

When data is loaded, database "triggers" calculate if a feature is included in which layer(s), at what "minimum zoom", and other Mapzen specific "mz" properties.

Most **content filter changes** (eg: adding a new kind of feature) only requires a database modification and doesn't require restarting TileServer. These are done in the `yaml/` filter files, for example: pois.yaml.

**Query selections from the database** are detailed in queries.yaml and also specifies how it is post-processed via Python transforms. This primary file refers to layer specific `jinja` SQL "templates" in `queries/` (eg: landuse.jinja2) for Postgres SQL code.

### TileServer

Listens for API requests on localhost, which are in the format of 0/0/0.ext

When TileServer hears a request it asks Postgres for "the stuff" inside that tile's bounding box, configured via the `queries.yaml` file and `.jinja2` files.

NOTE: A change to one of the query files requires TileServer to be restarted so they can be reloaded.


## Let's do this!

We'll cover the following topics in the next sections:

- Choose an issue to work on
- Do you work in a local branch
- Create a new test
- Edit database &/or query logic
- Verify the new logic by running the test
- Perform any modifications, if necessary
- Update documentation
- Push your local branch to the server
- Submit a Pull Request (PR)

### Choose an issue to work on

We have a backlog of issues, but they are also grouped into milestones and tracked with [Waffle board](https://waffle.io/tilezen/vector-datasource).

When picking an issue from the Ready column for the active milestone, self assign it to let other people know you'll be working on it.

If you propose to work on an issue in the Backlog but what to confirm some details add a comment to the issue or ask about it in Slack.

### Create a new branch

Make sure your `master` branch is up-to-date with a `git pull`. Then...

Checkout a new branch, name it something descriptive like the `yourname/#issue-issue title`.

    git checkout -b olga/713-urban-areas

### Create a new test

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

### Edit database &/or query logic

Tk tk tk intro

#### Update the database properties

If you modify the functions:

    psql -f data/functions.sql osm

For example:

    cd data/migrations && python create-sql-functions.py | psql osm

##### Update the data migration SQL files

Files in the `data/migrations/` should be updated to ensure someone with an earlier database can catch up with you. They are reset fresh for each release.

* `create-sql-functions.py`
* `run_migrations.sh`
* `sql.jinja2`
* `update-wof-l10n.py`
* `v1.0.0-cleanup.sql`
* `v1.0.0-line.sql`
* `v1.0.0-other-tables.sql`
* `v1.0.0-point.sql`
* `v1.0.0-polygon.sql`
* `v1.0.0-schema-prefunction.sql`

Here's an example out of the `v1.0.0-point.sql` file:

```
UPDATE
  planet_osm_point
  SET mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_point.*)
  WHERE
    (barrier = 'toll_booth' OR
     highway IN ('services', 'rest_area'))
    AND COALESCE(mz_poi_min_zoom, 999) <> COALESCE(mz_calculate_min_zoom_pois(planet_osm_point.*), 999);
```

NOTE: Occasionally two PRs will land at the same time and you'll need to clean up the SQL to address a merge conflict. To prevent this, use more new lines in your SQL.

##### Missing a database feature?

Sometimes you'll find a feature in OverPass that is more recent than your local database, or is in a region outside your loaded Metro Extract.

    ./test-data-update-osm.sh https://www.openstreetmap.org/node/418185265 osm

To do this by hand, you'd download the feature from the OSM API:

    https://www.openstreetmap.org/api/0.6/node/3984333433

Then modify the XML file by hand

`<osm`
to
`<osmChange`

mod:
`</osm`
to
`</osmChange`

insert:
`<modify>`

insert:
`</modify>`


For example, all together now:

```
<?xml version="1.0" encoding="UTF-8"?>
<osmChange version="0.6" generator="CGImap 0.4.0 (21232 thorn-02.openstreetmap.org)" copyright="OpenStreetMap and contributors" attribution="http://www.openstreetmap.org/copyright" license="http://opendatacommons.org/licenses/odbl/1-0/">
 <modify>
 <node id="3984333433" visible="true" version="1" changeset="36959786" timestamp="2016-02-02T15:48:08Z" user="zaphod_beeblebrox" uid="567719" lat="37.6348416" lon="-112.1656853">
  <tag k="amenity" v="water_point"/>
 </node>
 </modify>
</osmChange>
```

Then run:

    osm2pgsql -s -C 1024 -S /Users/nvkelso/git-repos/vector-datasource/osm2pgsql.style -k path/to/xml -a -d osm -H localhost

Making sure to add `-a` so the data is appended to existing table!

Alternatively, if your feature exists locally but is missing a neccesary attribute just update the feature in place:

```
UPDATE planet_osm_polygon
SET 'name' = "Fort Monroe"
WHERE
  osm_id = 51064272;
```

#### Example database SQL

If you only want to update the database in a certain region (area of interest), here for roads converting a viewport in latitude & longitude to Web Mercator meters:

```
UPDATE planet_osm_line
  SET mz_road_level = mz_calculate_road_level(highway, railway, aeroway, route, service, aerialway, leisure, sport, man_made, way, name, bicycle, foot, horse, tags->'snowmobile', tags->'ski', osm_id)
  WHERE
    highway IN ('pedestrian', 'living_street', 'track', 'path', 'cycleway', 'footway', 'steps') AND
    way && ST_Transform(ST_SetSrid(ST_MakeBox2D(ST_MakePoint(-124.03564453125, 36.59788913307022), ST_MakePoint(-117.333984375, 39.06184913429154)), 4326), 900913);
```

Updating a simple **line** feature:

```
UPDATE planet_osm_line
  SET mz_boundary_min_zoom = mz_calculate_min_zoom_boundaries(planet_osm_line.*)
  WHERE
    waterway = 'dam';
```

Updating a simple **point** feature:

```
UPDATE planet_osm_point
  SET mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_point.*)
  WHERE shop IN ('outdoor');
```

Updating a simple **polygon** feature:

```
UPDATE planet_osm_polygon
  SET mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_polygon.*)
  WHERE shop IN ('outdoor');
```

Some features can have a POI "label" and a landuse polygon, so calculate both:

Same as above:

```
UPDATE planet_osm_polygon
  SET mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_polygon.*)
  WHERE shop IN ('outdoor');
```

Also adding:

```
UPDATE planet_osm_polygon
  SET mz_poi_min_zoom = mz_calculate_min_zoom_landuse(planet_osm_polygon.*)
  WHERE shop IN ('outdoor');
```

Sometimes you'll want to investigate features in the database:

```
SELECT name, height, tags from planet_osm_point
  WHERE waterway = 'waterfall' AND height IS NOT NULL LIMIT 100;
```

Sometimes you need to debug why a feature appears one of multiple possible representations:

```
SELECT
  osm_id, name, place, mz_earth_min_zoom, mz_places_min_zoom from planet_osm_point where osm_id
IN (3178316462, 358955020, 358796350, 358761955, 358768646, 358795646)
ORDER BY
  osm_id;
```

#### Update the query configuration

Tk tk tk body

### Verify the new logic by running the test

This step is not necessary if only database properties were changed.

Run the test, hopefully it passes now!

    python integration-test.py local integration-test/160-motorway-junctions.py

**Example output:**

```
tk tk tk
```

If the test failed you can investigate why:

    cat test.log

Will print out the full debug.

NOTE: It's best practice to run your own test, and confirm that all other tests are still passing before submitting a PR. It's possible that you might need to run an overall database migration to achive this locally, or you can rely on CircleCI to run all the tests for you in your branch by pushing it to the server.

#### Some tests require TileServer restart

A minority of issues will require updating the `queries.yaml` file. In those cases you'll also need to restart TileServer to reload this file.

    tk tk tk

Then run your test like in the previous step.

### Perform any modifications, as necessary

Rinse and repeat, rewrite your code.

### Update documentation

Everything good? time to update the docs!

Project documentation is publicly accessable here, they document the API promises the service makes.

- https://mapzen.com/documentation/vector-tiles/layers/

Tk tk tk

### Push your local branch to the server

First let's commit our changes. Let's confirm which files changed:

    git status

You can also do a `git diff` on each file to determine if you meant to change or insert logic. Once you've confirmed the changes...

For each, commit using a specific commit message. The first should use the "Connects to #issuenum" format to link up the PR to the original issue in Waffle.io.

    git commit -m 'Connects to #713 for urban area kind rename' filename

NOTE: Subsequent commit messages can be more generic.

Then push to the server so other people can see your work. (If this is a large change over multiple days, please push the server once a day so your work is backed up.)

    git push

NOTE: Your first push for a branch might require additional details:

    git push --set-upstream origin olga/713-urban-areas

### Submit a Pull Request (PR)

Back on Github.com load the project page and notice there's a button suggested you create a PR for your active branch. Press that green button.

In the PR form, give it a good title that ties in with the original issue title. In the comment section summarize the work you did to resolve the issue and indicate you added tests and updated the documentation.

A Tilezen team member will review the PR for you, either merging it right away or following up with questions.

If the review leads to code modifications those should be done in same branch and the PR will automatically update with subsequent commits to the branch.

_Good luck, and **thank you** for contributing!_

  </body>
</html>