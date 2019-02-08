# -*- encoding: utf-8 -*-
from . import FixtureTest


class WaterLayerTooBigTest(FixtureTest):

    def test_drop_label(self):
        from shapely.ops import transform
        from tilequeue.tile import reproject_mercator_to_lnglat
        import math
        import dsl

        thresholds = {
            8:    200000000,
            9:    100000000,
            10:    10000000,
            11:     4000000,
            12:      750000,
            13:      100000,
            14:       50000,
            15:       10000,
        }

        for zoom in range(8, 16):
            area = thresholds.get(zoom)
            radius = math.sqrt(area / math.pi)

            coord = 2 ** (zoom - 1)

            # larger feature should retain name
            shape = dsl.tile_centre_shape(
                zoom, coord, coord).buffer(radius * 1.1)
            shape_lnglat = transform(
                    reproject_mercator_to_lnglat, shape)

            self.generate_fixtures(
                dsl.way(1, shape_lnglat, {
                    'natural': 'water',
                    'name': 'Foo',
                }),
            )

            self.assert_has_feature(
                zoom, coord, coord, 'water', {
                    'kind': 'water',
                    'name': 'Foo',
                })

            # smaller shape should drop it
            shape = dsl.tile_centre_shape(
                zoom, coord, coord).buffer(radius / 1.1)
            shape_lnglat = transform(
                    reproject_mercator_to_lnglat, shape)

            self.generate_fixtures(
                dsl.way(1, shape_lnglat, {
                    'natural': 'water',
                    'name': 'Foo',
                }),
            )

            self.assert_has_feature(
                zoom, coord, coord, 'water', {
                    'kind': 'water',
                    'name': type(None),
                })
