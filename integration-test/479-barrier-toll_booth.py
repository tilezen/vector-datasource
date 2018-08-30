# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class BarrierTollBooth(FixtureTest):
    def test_01(self):
        self.generate_fixtures(dsl.way(52529616, wkt_loads('POLYGON ((-122.314001285593 37.82514188814168, -122.313857824642 37.8251641685313, -122.31367142422 37.82441528830999, -122.313814885171 37.82439300769418, -122.314001285593 37.82514188814168))'), {u'building': u'yes', u'source': u'openstreetmap.org', u'way_area': u'1750.63', u'barrier': u'toll_booth'}))  # noqa

        self.assert_has_feature(
            16, 10501, 25319, 'pois',
            {'id': 52529616, 'kind': 'toll_booth'})

    def test_02(self):
        # Node: Main Gate (392430963)
        self.generate_fixtures(dsl.way(392430963, wkt_loads('POINT (-122.46950532066 37.7701796937487)'), {u'source': u'openstreetmap.org', u'name': u'Main Gate', u'barrier': u'toll_booth'}))  # noqa

        self.assert_has_feature(
            16, 10473, 25332, 'pois',
            {'id': 392430963, 'kind': 'toll_booth'})
