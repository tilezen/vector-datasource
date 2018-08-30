# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class RoadsSurfaceCobblestoneValueTransformed(FixtureTest):
    def test_transform(self):
        # transform cobblestone:flattened to cobblestone_flattened
        # Illicha Avenue in Donetsk, Ukraine
        self.generate_fixtures(dsl.way(2671385252, wkt_loads('POINT (37.8059417987771 48.00198857929431)'), {u'crossing': u'uncontrolled', u'source': u'openstreetmap.org', u'highway': u'crossing'}),dsl.way(239860289, wkt_loads('LINESTRING (37.8058308568395 48.00198845908089, 37.8059417987771 48.00198857929431, 37.8070071108725 48.00198930057479)'), {u'name:en': u'Illicha Avenue', u'name': u'\u0406\u043b\u043b\u0456\u0447\u0430 \u043f\u0440\u043e\u0441\u043f\u0435\u043a\u0442', u'surface': u'cobblestone:flattened', u'source': u'openstreetmap.org', u'name:uk': u'\u0406\u043b\u043b\u0456\u0447\u0430 \u043f\u0440\u043e\u0441\u043f\u0435\u043a\u0442', u'oneway': u'yes', u'name:ru': u'\u0418\u043b\u044c\u0438\u0447\u0430 \u043f\u0440\u043e\u0441\u043f\u0435\u043a\u0442', u'highway': u'secondary'}))  # noqa

        self.assert_has_feature(
            16, 39650, 22780, 'roads',
            {'id': 239860289, 'name:en': 'Illicha Avenue',
             'kind': 'major_road', 'surface': 'cobblestone_flattened'})
