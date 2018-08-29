# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class DisusedRailwayStations(FixtureTest):

    def test_old_south_ferry(self):
        # Old South Ferry (1) (disused=yes)
        self.generate_fixtures(dsl.way(2086974744, wkt_loads('POINT (-74.01325716895789 40.701283821753)'), {u'name': u'Old South Ferry (1)', u'wheelchair': u'no', u'source': u'openstreetmap.org', u'railway': u'station', u'disused': u'yes', u'network': u'New York City Subway'}))  # noqa

        self.assert_no_matching_feature(
            16, 19294, 24643, 'pois',
            {'kind': 'station', 'id': 2086974744})

    def test_valle_az(self):
        # Valle, AZ (disused=station)
        self.generate_fixtures(dsl.way(366220389, wkt_loads('POINT (-112.200039193448 35.65261688375637)'), {u'name': u'Valle', u'gnis:reviewed': u'no', u'addr:state': u'AZ', u'ele': u'1794', u'source': u'openstreetmap.org', u'gnis:feature_id': u'21103', u'disused': u'station', u'gnis:county_name': u'Coconino'}))  # noqa

        self.assert_no_matching_feature(
            16, 12342, 25813, 'pois',
            {'id': 366220389})
