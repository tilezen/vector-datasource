# API keys and rate limits

## Obtain an API key

To use the Mapzen Vector Tile service, you must first obtain a free developer API key. Sign in at https://mapzen.com/developers to create and manage your API keys.

1. Go to https://mapzen.com/developers.
2. Sign in with your GitHub account. If you have not done this before, you need to agree to the terms first.
3. Create a new key for Mapzen Vector Tiles, and optionally, give it a name so you can remember the purpose of the project.
4. Copy the key into your code.

## Rate limits
Mapzen Vector Tiles is a free, shared service. Mapzen Vector Tiles does not currently enforce rate limits. 

We pre-generate popular map areas and those tiles are highly available and served directly via Fastly's edge cache. But map areas with low traffic are generated on-demand. If an individual user abuses the service (especially by "vacuming" or "scraping" tiles not pre-generated), the overall system performance with be degraded for the on-demand portion of the service.

If you have questions, contact [tiles@mapzen.com](mailto:tiles@mapzen.com). You can also set up your own instance of [Vector Tiles](https://github.com/mapzen/vector-tiles), which has access to the same data used in the Mapzen Vector Tiles service.

## Security
Mapzen Vector Tiles works over HTTPS, in addition to HTTP. You are strongly encouraged to use HTTPS for all requests, especially for queries involving potentially sensitive information.