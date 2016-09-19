# API keys and rate limits

## Obtain an API key

To use the Mapzen Vector Tile service, you should first obtain a free developer API key. Sign in at https://mapzen.com/developers to create and manage your API keys.

1. Go to https://mapzen.com/developers.
2. Sign in with your GitHub account. If you have not done this before, you need to agree to the terms first.
3. Create a new key and optionally, give it a name so you can remember the purpose of the project.
4. Copy the key into your code.

## Rate limits

Because Mapzen Vector Tiles is a shared service, there are limitations on the numbers of requests to prevent individual users from degrading system performance.

* [Rate limits](https://mapzen.com/documentation/overview/#mapzen-vector-tiles) are detailed in Mapzen's developer overview.

If an individual user abuses the service (especially by "vacuuming" or "scraping" tiles not pre-generated), the overall system performance will be degraded for the on-demand portion of the service for all users. Cached tiles will continue to be highly available for all users.

We pre-generate popular map areas and those tiles are highly available and served directly via Fastly's edge cache. But map areas with low traffic are generated on-demand.

If you experience slow tile loading in a map area, it's likely because you are a first requester using on-demand tile generation. Subsequent loads of the same map area should be much faster because the tile is now available in the cache, and when the source OSM data changes in that map area we will update the tiles automatically for you.

If you have questions, contact [tiles@mapzen.com](mailto:tiles@mapzen.com). You can also set up your own instance of [Tilezen](https://github.com/mapzen/vector-datasource), which has access to the same data used in the Mapzen Vector Tiles service.

## Caching

You are free to cache Mapzen’s vector tiles for offline use. But you must give credit to the source data by including [attribution](attribution.md). A shoutout to Mapzen would also be nice!

Tiles include features from several open data sources, including OpenStreetMap, Natural Earth, and Who’s On First and each source has its own attribution and sharing requirement.
