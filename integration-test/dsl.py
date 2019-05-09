from collections import namedtuple
from shapely.geometry import Point
from tilequeue.tile import reproject_lnglat_to_mercator


Feature = namedtuple('Feature', 'fid shape properties')


# turns a dict mapping keys to values, either of which might be unicode,
# into a dict mapping only utf-8 encoded values (if they're strings at
# all - it'll leave other types alone).
def _tags_to_utf8(tags):
    new_tags = {}
    for k, v in tags.iteritems():
        if isinstance(k, unicode):
            k = k.encode('utf-8')
        if isinstance(v, unicode):
            v = v.encode('utf-8')
        new_tags[k] = v
    return new_tags


# simple utility wrapper to generate a Feature at a point. note that the
# position is expected to be in (lon, lat) coordinates.
def point(id, position, tags):
    x, y = reproject_lnglat_to_mercator(*position)
    return Feature(id, Point(x, y), _tags_to_utf8(tags))


# utility wrapper to generate a Feature from a lat/lon shape.
def way(id, shape, tags):
    from shapely.ops import transform
    merc_shape = transform(reproject_lnglat_to_mercator, shape)
    return Feature(id, merc_shape, _tags_to_utf8(tags))


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
    for k, v in _tags_to_utf8(tags).items():
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


def tile_centre_shape(z, x, y):
    """
    Returns a shape consisting of a single point at the (mercator) tile
    centre.
    """

    from shapely.geometry import Point

    lon, lat = tile_centre(z, x, y)
    return Point(lon, lat)


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


def box_area(z, x, y, area, include_boundary=False):
    """
    Returns a Shapely Polygon which is in the z/x/y tile and has the given
    area in Mercator square meters.

    If include_boundary is truthy, set up the shape such that the boundary
    is part of the tile. Try to keep the centroid within the tile. If that
    isn't possible, throw an exception.
    """

    from ModestMaps.Core import Coordinate
    from math import sqrt
    from shapely.geometry import box
    from shapely.ops import transform
    from tilequeue.tile import coord_to_mercator_bounds
    from tilequeue.tile import half_earth_circum
    from tilequeue.tile import reproject_mercator_to_lnglat

    bounds = coord_to_mercator_bounds(Coordinate(zoom=z, column=x, row=y))

    if include_boundary:
        # make the shape 90% of the tile's height, and whatever width is
        # necessary for that without wrapping around the world.
        size_y = 0.9 * (bounds[3] - bounds[1])
        size_x = area / size_y

    else:
        # otherwise, a square shape is easiest to reason about.
        size_y = size_x = sqrt(area)

    # make a shape with the given size
    centre_x = 0.5 * (bounds[0] + bounds[2])
    centre_y = 0.5 * (bounds[1] + bounds[3])

    def _check(coord):
        assert -half_earth_circum <= coord <= half_earth_circum
        return coord

    mercator_shape = box(
        _check(centre_x - 0.5 * size_x),
        _check(centre_y - 0.5 * size_y),
        _check(centre_x + 0.5 * size_x),
        _check(centre_y + 0.5 * size_y),
    )

    return transform(reproject_mercator_to_lnglat, mercator_shape)


def fit_in_tile(z, x, y, shape):
    """
    Fit shape into the tile. Shape should be a Shapely geometry or WKT string
    with coordinates between 0 and 1. This unit square is then remapped into
    the tile z/x/y.
    """

    from ModestMaps.Core import Coordinate
    from shapely.ops import transform
    from shapely.wkt import loads as wkt_loads
    from tilequeue.tile import coord_to_mercator_bounds
    from tilequeue.tile import reproject_mercator_to_lnglat

    bounds = coord_to_mercator_bounds(Coordinate(zoom=z, column=x, row=y))

    if isinstance(shape, (str, unicode)):
        shape = wkt_loads(shape)

    # check shape fits within unit square, so we can transform it to fit
    # within the tile.
    assert shape.bounds[0] >= 0
    assert shape.bounds[1] >= 0
    assert shape.bounds[2] <= 1
    assert shape.bounds[3] <= 1

    def _transform(x, y, *unused_coords):
        return (
            x * (bounds[2] - bounds[0]) + bounds[0],
            y * (bounds[3] - bounds[1]) + bounds[1],
        )

    merc_shape = transform(_transform, shape)
    return transform(reproject_mercator_to_lnglat, merc_shape)
