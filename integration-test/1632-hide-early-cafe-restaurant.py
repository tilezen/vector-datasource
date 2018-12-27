# -*- encoding: utf-8 -*-
from . import FixtureTest


class CafeRestaurantTest(FixtureTest):

    def test_restaurant(self):
        import dsl

        z, x, y = (15, 5081, 12309)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/409101877
            dsl.way(409101877, dsl.tile_box(z, x, y), {
                'amenity': 'restaurant',
                'building': 'yes',
                'cuisine': 'seafood',
                'name': "Jack's Seafood",
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 409101877,
                'kind': 'restaurant',
                'min_zoom': 15,
            })

    def test_cafe(self):
        import dsl

        z, x, y = (15, 5241, 12664)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/256045050
            dsl.way(256045050, dsl.tile_box(z, x, y), {
                'addr:city': 'San Francisco',
                'addr:housenumber': '614',
                'addr:street': 'Polk Street',
                'amenity': 'cafe',
                'building': 'yes',
                'height': '21',
                'name': "Emile's Coffee & Tea",
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 256045050,
                'kind': 'cafe',
                'min_zoom': 15,
            })
