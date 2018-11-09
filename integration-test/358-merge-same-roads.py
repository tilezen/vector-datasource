from . import FixtureTest


def _freeze(thing):
    if isinstance(thing, dict):
        return frozenset([(_freeze(k), _freeze(v)) for k, v in thing.items()])

    elif isinstance(thing, list):
        return tuple([_freeze(i) for i in thing])

    return thing


def _query_highway(highway):
    # beware: overpass wants (south,west,north,east) coords for bbox,
    # in defiance of conventional x, y coordinate ordering.
    bbox = "36.563,-122.377,37.732,-120.844"
    overpass = "http://overpass-api.de/api/interpreter?data="
    return overpass + 'way(' + bbox + ')[highway=' + highway + ']%3B>%3B'


class MergeSameRoads(FixtureTest):

    def test_roads_merged(self):
        from collections import defaultdict
        from shapely.geometry import asShape

        # count the unique parameters - there should only be one, indicating
        # that the roads have been merged.
        self.load_fixtures(
            [_query_highway(t) for t in ('motorway', 'primary', 'trunk')],
            clip=self.tile_bbox(8, 41, 99))

        with self.features_in_tile_layer(8, 41, 99, 'roads') as roads:
            features = defaultdict(list)

            for road in roads:
                props = frozenset(_freeze(road['properties']))
                geom = asShape(road['geometry'])

                for f in features[props]:
                    if f.disjoint(geom):
                        self.assertTrue(
                            False,
                            'Duplicate properties %r in roads layer for '
                            'disjoint geometries (%r & %r), but '
                            'properties should be unique or geometries '
                            'intersecting.' % (road['properties'], f.wkt,
                                               geom.wkt))

                features[props].append(geom)
