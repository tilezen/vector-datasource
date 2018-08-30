# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class IceCreamShops(FixtureTest):
    def test_amenity_ice_cream(self):
        # New York, NY (amenity=ice_cream)
        self.generate_fixtures(dsl.way(2782000317, wkt_loads('POINT (-73.9865498064034 40.75743609254629)'), {u'source': u'openstreetmap.org', u'amenity': u'ice_cream', u'name': u'Ben and Jerry'}))  # noqa

        self.assert_has_feature(
            16, 19299, 24629, 'pois',
            {'kind': 'ice_cream'})

    def test_shop_ice_cream(self):
        # Oakland, CA (shop=ice_cream)
        self.generate_fixtures(dsl.way(661742947, wkt_loads('POINT (-122.252297895189 37.84753397443631)'), {u'shop': u'ice_cream', u'cuisine': u'ice_cream', u'amenity': u'ice_cream', u'name': u"Dreyer's Ice Cream", u'wheelchair': u'yes', u'outdoor_seating': u'yes', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_has_feature(
            16, 10512, 25314, 'pois',
            {'kind': 'ice_cream'})
