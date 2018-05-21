from collections import namedtuple
from shapely.geometry import Point
from tilequeue.tile import reproject_lnglat_to_mercator


Feature = namedtuple('Feature', 'fid shape properties')


# simple utility wrapper to generate a Feature at a point. note that the
# position is expected to be in (lon, lat) coordinates.
def point(id, position, tags):
    x, y = reproject_lnglat_to_mercator(*position)
    return Feature(id, Point(x, y), tags)


# utility wrapper to generate a Feature from a lat/lon shape.
def way(id, shape, tags):
    from shapely.ops import transform
    merc_shape = transform(reproject_lnglat_to_mercator, shape)
    return Feature(id, merc_shape, tags)


# the fixture code expects "raw" relations as if they come straight from
# osm2pgsql. the structure is a little cumbersome, so this utility function
# constructs it from a more readable function call.
def relation(id, tags, nodes=None, ways=None, relations=None):
    nodes = nodes or []
    ways = ways or []
    relations = relations or []
    way_off = len(nodes)
    rel_off = way_off + len(ways)
    tags_as_list = []
    for k, v in tags.items():
        tags_as_list.extend((k, v))
    return dict(
        id=id, tags=tags_as_list, way_off=way_off, rel_off=rel_off,
        parts=(nodes + ways + relations))


def tile_diagonal(z, x, y):
    """
    Returns a Shapely LineString which goes from the lower left of the tile
    to the upper right.
    """

    from tilequeue.tile import coord_to_bounds
    from shapely.geometry import LineString
    from ModestMaps.Core import Coordinate

    bounds = coord_to_bounds(Coordinate(zoom=z, column=x, row=y))
    shape = LineString([
        [bounds[0], bounds[1]],
        [bounds[2], bounds[3]],
    ])

    return shape


def tile_box(z, x, y):
    """
    Returns a Shapely Polygon which covers the tile.
    """

    from tilequeue.tile import coord_to_bounds
    from shapely.geometry import box
    from ModestMaps.Core import Coordinate

    bounds = coord_to_bounds(Coordinate(zoom=z, column=x, row=y))
    return box(*bounds)


def tile_centre(z, x, y):
    """
    Returns the (lon, lat) tuple of the centre of the tile. Note that the
    centre is calculated in mercator projection, so might not be the centre of
    the tile in lat/lon projection.
    """

    from tilequeue.tile import num2deg

    lat, lon = num2deg(x + 0.5, y + 0.5, z)
    return (lon, lat)


def is_in(iso_code, z, x, y, way_id=-1):
    """
    This pattern gets used a lot in road shield tests to set up a country
    polygon which is joined to the roads to apply country-specific processing
    logic. It's a little verbose, so this utility function can shorten it and
    make it a little more readable.
    """

    return way(way_id, tile_box(z, x, y), {
        'kind': 'admin_area', 'iso_code': iso_code,
        'source': 'openstreetmap.org',
    })
