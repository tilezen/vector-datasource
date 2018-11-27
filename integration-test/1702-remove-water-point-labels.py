# -*- encoding: utf-8 -*-
from . import FixtureTest


class RemoveWaterPointLabelsTest(FixtureTest):

    def test_water_labels(self):
        import dsl
        from tilequeue.tile import coord_to_bounds
        from shapely.geometry import LineString
        from ModestMaps.Core import Coordinate

        z, x, y = (16, 2**15, 2**15)

        bounds = coord_to_bounds(Coordinate(zoom=z, column=x, row=y))
        dx = bounds[2] - bounds[0]
        dy = bounds[3] - bounds[1]
        shape = LineString([
            [bounds[0] + 0.01 * dx, bounds[1] + 0.01 * dy],
            [bounds[2] - 0.01 * dx, bounds[3] - 0.01 * dy],
        ])

        self.generate_fixtures(
            dsl.way(1, shape, {
                'waterway': 'river',
                'name': 'Foo',
                'source': u'openstreetmap.org',
            }),
        )

        with self.features_in_tile_layer(z, x, y, 'water') as features:
            self.assertTrue(len(features) == 1)

            # when "download fixtures" phase is run, this won't be true. but
            # the preceding assertion will have been short-circuited to true,
            # so we guard the rest of the assertions here.
            if len(features) == 1:
                self.assertTrue(
                    features[0]['geometry']['type'] == 'LineString')
