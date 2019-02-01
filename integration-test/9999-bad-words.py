# -*- encoding: utf-8 -*-
from . import FixtureTest


class BadWordsTest(FixtureTest):

    def test_global_drop(self):
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_centre_shape(z, x, y), {
                'place': 'town',
                'name': 'Darn it',
            })
        )

        # feature should have been dropped
        self.assert_no_matching_feature(
            z, x, y, 'places', {
                'id': 1,
            })

    def test_global_exception_location(self):
        import dsl

        z, x, y = (16, 28661, 16430)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5303386436
            dsl.point(5303386436, (-22.557100, 66.411820), {
                'ele': '667',
                'name': 'Darn',
                'natural': 'peak',
                'source': 'openstreetmap.org',
            }),
        )

        # despite the offensive name, not hidden in the tile.
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5303386436,
                'kind': 'peak',
            })

    def test_global_exception_whitelist(self):
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_centre_shape(z, x, y), {
                'amenity': 'place_of_worship',
                'name': 'Darnton Abbey',
            })
        )

        # feature should be present, because whitelist
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1,
                'name': 'Darnton Abbey',  # name survives intact
            })
