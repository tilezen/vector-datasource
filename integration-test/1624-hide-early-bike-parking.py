# -*- encoding: utf-8 -*-
from . import FixtureTest


class HideEarlyBikeParkingTest(FixtureTest):

    def test_bicycle_parking(self):
        import dsl

        z, x, y = (16, 10478, 25330)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3134706408
            dsl.point(3134706408, (-122.438528, 37.775930), {
                'amenity': 'bicycle_parking',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3134706408,
                'kind': 'bicycle_parking',
                'min_zoom': 19,
            })

    def test_car_sharing_with_name(self):
        import dsl

        z, x, y = (16, 10484, 25327)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/1409407263
            dsl.point(1409407263, (-122.404247, 37.792022), {
                'amenity': 'car_sharing',
                'name': 'California & Kearny (St. Marys Square)',
                'operator': 'City CarShare',
                'ref': '5',
                'source': 'openstreetmap.org',
                'source:pkey': '5',
                'website': 'http://www.citycarshare.org/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1409407263,
                'kind': 'car_sharing',
                'min_zoom': 17,
            })

    def test_car_sharing_no_name(self):
        import dsl

        z, x, y = (16, 10484, 25327)

        self.generate_fixtures(
            dsl.point(1409407264, (-122.404247, 37.792022), {
                'amenity': 'car_sharing',
                'operator': 'City CarShare',
                'website': 'http://www.citycarshare.org/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1409407264,
                'kind': 'car_sharing',
                'min_zoom': 19,
            })
