# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class ZoosZ13(FixtureTest):
    def test_zoo_appears_at_z13(self):
        # Zoo Montana, Billings, MT
        self.generate_fixtures(dsl.way(2274329294, wkt_loads('POINT (-108.620965329915 45.7322965681428)'), {u'addr:housenumber': u'2100', u'name': u'Zoo Montana', u'addr:city': u'Billings, MT 59106', u'source': u'openstreetmap.org', u'tourism': u'zoo', u'addr:street': u'S. Shiloh Road'}))  # noqa

        self.assert_has_feature(
            13, 1624, 2923, 'pois',
            {'kind': 'zoo'})
