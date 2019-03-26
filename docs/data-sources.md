# Data sources in Mapzen Vector Tiles

Mapzen Vector Tiles are powered by several major open data sets and we owe a tremendous debt of gratitude to the individuals and communities which produced them.

**Attribution is required** for many data providers. See the [Attribution](https://github.com/tilezen/vector-datasource/blob/master/docs/attribution.md) document for more information.

## What is sourced at what zooms?

Generally speaking, **Natural Earth** is used at low-zooms, and **OpenStreetMap** is relied on in mid- and high-zooms. Data from **osmdata.openstreetmap.de** is used at the same zooms as the raw OSM data, and is derived from the OSM data. **Who's On First** neighbourhood labels generally come in at high-zooms.

When possible, we annotate individual map features in each tile with a `source` property.


## OpenStreetMap

`source:openstreetmap`

[OpenStreetMap](https://www.openstreetmap.org/) is a community-driven, editable map of the world. It prioritizes local knowledge and individual contributions over bulk imports, which often means it has excellent coverage even in remote areas where no large-scale mapping efforts have been attempted. OpenStreetMap contains information on landmarks, buildings, roads, and natural features.

With its coverage of roads, POIs, landuse, as well as rich metadata, OpenStreetMap is arguably the most valuable dataset used by Mapzen Vector Tiles for general usage.

All OpenStreetMap data is licensed under the [ODbL](http://opendatacommons.org/licenses/odbl/), a [share-alike](https://en.wikipedia.org/wiki/Share-alike) license which also requires attribution.

## osmdata.openstreetmap.de

`source:osmdata.openstreetmap.de`

We include coastline-derived water polygons from [osmdata.openstreetmap.de](https://osmdata.openstreetmap.de) at mid- and high-zooms. This service, now run by [FOSSGIS e.V.](https://www.fossgis.de/), replaces `openstreetmapdata.com` - it's the same service, but a different hosting arrangement. The service was created by Jochen Topf and Christoph Hormann for the OpenStreetMap community and the general public and it rocks!

As they say, "The coastline in OpenStreetMap is often broken. The update process will try to repair it, but this does not always work. If the OSM data can't be repaired automatically, the data here will not be updated."


## Natural Earth

`source:naturalearthdata.com`

Natural Earth is a public domain map dataset available at 1:10m, 1:50m, and 1:110 million scales suitable for zooms 0 to 8. Featuring tightly integrated vector and raster data, with Natural Earth you can make a variety of visually pleasing, well-crafted maps with cartography or GIS software.

Natural Earth was built through a collaboration of many [volunteers](http://www.naturalearthdata.com/about/contributors/) and is supported by [NACIS](http://www.nacis.org/) (North American Cartographic Information Society), and is free for use in any type of project (see our [Terms of Use](http://www.naturalearthdata.com/about/terms-of-use/) page for more information).

More details can be found at: http://www.naturalearthdata.com/about/terms-of-use/


## Who's On First

`source:whosonfirst`

[Who's On First](http://www.whosonfirst.org/) is an open place gazetteer initiated by Mapzen and is used to source neighbourhood labels.
