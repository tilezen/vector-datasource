# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class SubwayStationsZ12(FixtureTest):
    def test_subway_stations_appear_at_z12(self):
        # 23rd St Station, New York, NY
        self.generate_fixtures(dsl.way(597928317, wkt_loads('POINT (-73.9927627345714 40.7428445602345)'), {u'source': u'openstreetmap.org', u'wheelchair': u'no', u'railway': u'station', u'name': u'23rd Street (F,M,PATH)', u'network': u'New York City Subway'}))  # noqa

        self.assert_has_feature(
            12, 1206, 1539, 'pois',
            {'kind': 'station'})
