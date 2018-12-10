# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class TestCranes(FixtureTest):

    def test_crane_landuse_line(self):
        self.generate_fixtures(dsl.way(1842715060, wkt_loads('POINT (0.6785997623748069 51.43672148243049)'), {u'source': u'openstreetmap.org', u'man_made': u'crane'}),dsl.way(173458931, wkt_loads('LINESTRING (0.6867062493302298 51.43649709368218, 0.6785997623748069 51.43672148243049)'), {u'source': u'openstreetmap.org', u'man_made': u'crane', u'crane:type': u'portal_crane'}))  # noqa

        self.assert_has_feature(
            16, 32891, 21813, 'landuse',
            {'id': 173458931, 'kind': 'crane', 'min_zoom': 16,
             'sort_rank': 272})

    def test_crane_pois(self):
        self.generate_fixtures(dsl.way(1842715058, wkt_loads('POINT (0.6785790112917439 51.43642978244269)'), {u'source': u'openstreetmap.org', u'man_made': u'crane'}))  # noqa

        self.assert_has_feature(
            16, 32891, 21813, 'pois',
            {'id': 1842715058, 'kind': 'crane', 'min_zoom': 16})
