# -*- encoding: utf-8 -*-
from . import FixtureTest


class BikeShopTest(FixtureTest):

    def test_bicycle_shop_node(self):
        import dsl

        z, x, y = (16, 10479, 25331)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2484293076
            dsl.point(2484293076, (-122.432202, 37.771036), {
                'addr:city': 'San Francisco',
                'addr:housenumber': '520',
                'addr:street': 'Waller Street',
                'name': 'Wiggle Bicycles',
                'opening_hours': 'Tu-Fr 10:00-18:30; Sa-Su 10:00-17:00',
                'service:bicycle:diy': 'no',
                'service:bicycle:pump': 'yes',
                'service:bicycle:repair': 'yes',
                'shop': 'bicycle',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2484293076,
                'kind': 'bicycle',
                'min_zoom': 17,
            })

    def test_bicycle_shop_large_way(self):
        import dsl

        z, x, y = (15, 5242, 12665)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/260354461
            dsl.way(260354461, dsl.box_area(z, x, y, 723), {
                'addr:city': 'San Francisco',
                'addr:housenumber': '1090',
                'addr:postcode': '94103',
                'addr:state': 'CA',
                'addr:street': 'Folsom Street',
                'building': 'yes',
                'height': '7',
                'name': 'SF Bike Connection',
                'shop': 'bicycle',
                'source': 'openstreetmap.org',
                'website': 'http://bikeconnection.net/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 260354461,
                'kind': 'bicycle',
                # should be in z15 tile, so min_zoom between 15 and 16
                'min_zoom': lambda z: 15 <= z < 16,
            })

    def test_bicycle_shop_small_way(self):
        import dsl

        z, x, y = (16, 10476, 25332)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/264534357
            dsl.way(264534357, dsl.box_area(z, x, y, 362), {
                'addr:city': 'San Francisco',
                'addr:housenumber': '858',
                'addr:postcode': '94117',
                'addr:street': 'Stanyan Street',
                'building': 'yes',
                'height': '5',
                'name': 'American Cyclery Too',
                'operator': 'American Cyclery',
                'service:bicycle:pump': 'yes',
                'service:bicycle:repair': 'yes',
                'service:bicycle:retail': 'yes',
                'service:bicycle:second_hand': 'yes',
                'shop': 'bicycle',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 264534357,
                'kind': 'bicycle',
                # min_zoom between 16 and 17, less than the node at z17
                'min_zoom': lambda z: 16 <= z < 17,
            })
