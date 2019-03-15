from . import FixtureTest


def _freeze(thing):
    if isinstance(thing, dict):
        return frozenset([(_freeze(k), _freeze(v)) for k, v in thing.items()])

    elif isinstance(thing, list):
        return tuple([_freeze(i) for i in thing])

    return thing


class MergeSameRoads(FixtureTest):

    def test_roads_merged(self):
        from collections import defaultdict
        from shapely.geometry import asShape
        from tilequeue.tile import coord_to_bounds
        from shapely.geometry import LineString
        from ModestMaps.Core import Coordinate
        import dsl

        z, x, y = 8, 41, 99

        bounds = coord_to_bounds(Coordinate(zoom=z, column=x, row=y))

        def _line(frac):
            return LineString([
                [bounds[0] + frac * (bounds[2] - bounds[0]), bounds[1]],
                [bounds[0] + frac * (bounds[2] - bounds[0]), bounds[3]],
            ])

        # count the unique parameters - there should only be one, indicating
        # that the roads have been merged.
        self.generate_fixtures(
            dsl.way(1, _line(0.1), {
                'highway': 'motorway',
                'source': 'openstreetmap.org',
            }),
            dsl.way(2, _line(0.2), {
                'highway': 'motorway',
                'source': 'openstreetmap.org',
            }),
            dsl.way(3, _line(0.3), {
                'highway': 'primary',
                'source': 'openstreetmap.org',
            }),
            dsl.way(4, _line(0.4), {
                'highway': 'primary',
                'source': 'openstreetmap.org',
            }),
            dsl.way(5, _line(0.5), {
                'highway': 'trunk',
                'source': 'openstreetmap.org',
            }),
            dsl.way(6, _line(0.6), {
                'highway': 'trunk',
                'source': 'openstreetmap.org',
            }),
        )

        with self.features_in_tile_layer(z, x, y, 'roads') as roads:
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
