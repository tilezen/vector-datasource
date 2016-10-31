# API keys and rate limits

## Obtain an API key

To use the Mapzen Vector Tile service, you should [first obtain a free developer API key](https://mapzen.com/documentation/overview/).

## Rate limits

Mapzen Vector Tiles is a free, shared service and rate limits are enforced.

If an individual user abuses the service (especially by "vacuuming" or "scraping" tiles not pre-generated), the overall system performance will be degraded for the on-demand portion of the service for all users. Cached tiles will continue to be highly available for all users.

We pre-generate popular map areas and those tiles are highly available and served directly via Fastly's edge cache. But map areas with low traffic and custom layer requests are generated on-demand and must include an API key with the request.

If you experience slow tile loading in a map area, it's likely because you are a first requester using on-demand tile generation. Subsequent `all` and `buildings` layer loads of the same map area should be much faster because the tile is now available in the cache, and when the source OSM data changes in that map area we will update the tiles automatically for you. Other custom layers (or combinations of layers) are not cached.

If you have questions, contact [tiles@mapzen.com](mailto:tiles@mapzen.com). You can also set up your own instance of [Vector Tiles](https://github.com/mapzen/vector-datasource), which has access to the same data used in the Mapzen Vector Tiles service.

## Caching

You are free to cache Mapzen’s vector tiles for offline use. But you must give credit to the source data by including [attribution](attribution.md). A shoutout to Mapzen would also be nice!

Tiles include features from several open data sources, including OpenStreetMap, Natural Earth, and Who’s On First and each source has its own attribution and sharing requirement.
