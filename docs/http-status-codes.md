# HTTP status codes

The following is a list of HTTP status error code conditions that may occur for a particular request.

In general, the service follows the [HTTP specification](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes). That is to say that `5xx` returns are generally ephemeral server problems that should be resolved shortly or are the result of a bug. `4xx` returns are used to mark requests that cannot be carried out, generally due to bad input in the request or problems with the underlying data. `3xx` returns are used to mark requests that are content redirects . A `2xx` return is expected when there is a successful `tile` response for a given tile coordinate, list of layers, and file format.

The following status codes are returned from the vector tile service:

- `200 OK`: The request has succeeded.
- `304 Not Modified`: Tile hasn't changed since the last time it was requested and there is no need to retransmit the resource since the client still has a previously-downloaded copy.
- `400 Bad Request`: An input parameter was invalid. An error message is included in the response body with more details.
- `403 Forbidden`: The URL is invalid or the path is no longer valid.
- `404 Not Found`: The URL is invalid or the path is no longer valid.
- `429 Too Many Requests`: Rate limiting, refer to Mapzen's [rate limits](https://mapzen.com/documentation/overview/rate-limits/) documentation.
- `500 Internal Server Error`: Generic fatal error.
- `502 Bad Gateway`: Connection was lost to the tileserver cluster.

In the `200 OK` case above, the `tile` response body will be valid GeoJSON, TopoJSON, or MVT document. In the other cases a text file will be returned with a message and the response header will specify the HTML status code.
