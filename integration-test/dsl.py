from collections import namedtuple
from shapely.geometry import Point
from tilequeue.tile import reproject_lnglat_to_mercator


Feature = namedtuple('Feature', 'fid shape properties')


# simple utility wrapper to generate a Feature at a point. note that the
# position is expected to be in (lon, lat) coordinates.
def point(id, position, tags):
    x, y = reproject_lnglat_to_mercator(*position)
    return Feature(id, Point(x, y), tags)


# the fixture code expects "raw" relations as if they come straight from
# osm2pgsql. the structure is a little cumbersome, so this utility function
# constructs it from a more readable function call.
def relation(id, tags, nodes=None, ways=None, relations=None):
    nodes = nodes or []
    ways = ways or []
    relations = relations or []
    way_off = len(nodes)
    rel_off = way_off + len(ways)
    return dict(
        id=id, tags=tags, way_off=way_off, rel_off=rel_off,
        parts=(nodes + ways + relations))
