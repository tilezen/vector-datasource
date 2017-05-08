# count the unique parameters - there should only be one, indicating that the
# roads have been merged.
#
# beware: overpass wants (south,west,north,east) coords for bbox, in defiance
# of x, y coordinate ordering.
#
# RAW QUERY: way(36.563,-122.377,37.732,-120.844)[highway=motorway];>;
# RAW QUERY: way(36.563,-122.377,37.732,-120.844)[highway=primary];>;
# RAW QUERY: way(36.563,-122.377,37.732,-120.844)[highway=trunk];>;
#

def _freeze(thing):
    if isinstance(thing, dict):
        return frozenset([(_freeze(k), _freeze(v)) for k, v in thing.items()])

    elif isinstance(thing, list):
        return tuple([_freeze(i) for i in thing])

    return thing

with test.features_in_tile_layer(8, 41, 99, 'roads') as roads:
    features = set()

    for road in roads:
        props = frozenset(_freeze(road['properties']))
        if props in features:
            test.fail('Duplicate properties %r in roads layer, but properties '
                 'should be unique.' % road['properties'])
        features.add(props)
