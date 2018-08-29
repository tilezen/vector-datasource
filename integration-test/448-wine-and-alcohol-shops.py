# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class WineAndAlcoholShops(FixtureTest):

    def test_shop_wine(self):
        # Wine, New York, NY (shop=wine)
        self.generate_fixtures(dsl.way(2549960970, wkt_loads('POINT (-73.99107794425609 40.7455829198091)'), {u'shop': u'wine', u'addr:housenumber': u'795A', u'name': u'Wine & Liquior', u'addr:postcode': u'10001', u'source': u'openstreetmap.org', u'addr:street': u'Avenue Of The Americas'}))  # noqa

        self.assert_has_feature(
            16, 19298, 24632, 'pois',
            {'kind': 'wine'})

    def test_shop_alcohol(self):
        # Noe Valley Wine Merchants, San Francisco, CA
        self.generate_fixtures(dsl.way(1713269631, wkt_loads('POINT (-122.427979978 37.7515696737989)'), {u'shop': u'alcohol', u'addr:housenumber': u'3821', u'name': u'Noe Valley Wine Merchants', u'addr:city': u'San Francisco', u'source': u'openstreetmap.org', u'addr:street': u'24th Street'}))  # noqa

        self.assert_has_feature(
            16, 10480, 25336, 'pois',
            {'kind': 'alcohol'})
