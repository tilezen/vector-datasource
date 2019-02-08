# -*- encoding: utf-8 -*-
from . import FixtureTest


class LowZoomPlacesTest(FixtureTest):

    def test_zoom_1(self):
        import dsl

        z, x, y = (3, 7, 3)

        self.generate_fixtures(
            dsl.way(607976629, dsl.tile_centre_shape(z, x, y), {
                "min_zoom": 1,
                "__ne_max_zoom": 10,
                "__ne_min_zoom": 3,
                "area": 0,
                "place": "country",
                "name": "Guam",
                "population": 185427,
                "source": "openstreetmap.org",
            }),
        )

        # should exist at zoom 3 (the min zoom from NE)
        self.assert_has_feature(
            z, x, y, 'places', {
                'id': 607976629,
                'kind': 'country',
                'name': 'Guam',
            })

        # should not exist at zoom 2 (one past the min zoom)
        self.assert_no_matching_feature(
            z-1, x//2, y//2, 'places', {
                'id': 607976629
            })

        # should not exist at zoom 1
        self.assert_no_matching_feature(
            z-2, x//4, y//4, 'places', {
                'id': 607976629,
            })

        # should not exist at zoom 0
        self.assert_no_matching_feature(
            0, 0, 0, 'water', {
                'kind': 'ocean',
                'label_placement': True,
            })

        # should not exist at zoom 0
        self.assert_no_matching_feature(
            0, 0, 0, 'earth', {
                'kind': 'continent',
                'label_placement': True,
            })
