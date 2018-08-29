# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class AerowayGates(FixtureTest):
    def test_aeroway_gate(self):
        # Gate A5, SFO
        self.generate_fixtures(dsl.way(656398641, wkt_loads('POINT (-122.389152904958 37.61262666020428)'), {u'source': u'openstreetmap.org', u'layer': u'1', u'aeroway': u'gate', u'ref': u'A5'}))  # noqa

        self.assert_has_feature(
            16, 10487, 25368, 'pois',
            {'kind': 'aeroway_gate'})
