# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class NeMinZoomRoads(FixtureTest):
    def setUp(self):
        super(NeMinZoomRoads, self).setUp()

        # note: uses existing fixture from 976-fractional-pois
        self.generate_fixtures(dsl.way(1, wkt_loads('LINESTRING (-74.34536905773159 40.52738074072361, -74.43219878225844 40.44228761068732, -74.505135750861 40.28252091755795, -74.60585823131211 40.19221800405002)'), {u'labelrank': 0, u'length_km': 41, u'scalerank': 3, u'prefix': u'', u'continent': u'North America', u'namealtt': u'', u'localalt': u'', u'question': 0, u'sov_a3': u'USA', u'label': u'', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'ne_1d4_original', u'toll': 1, u'expressway': 1, u'local': u'', u'edited': u'New in version 2.0.0', u'label2': u'', u'orig_fid': 0, u'namealt': u'', u'uident': 76105, u'featurecla': u'Road', u'rwdb_rd_id': 0, u'name': u'95', u'level': u'Interstate', u'type': u'Major Highway', u'routeraw': u'', u'ignore': 0, u'add': 0, u'localtype': u'', u'min_zoom': 3.0}))  # noqa

    def test_roads_present_at_zoom_5(self):
        # the road should be present at zoom 5
        self.assert_has_feature(
            5, 9, 12, 'roads',
            {'source': 'naturalearthdata.com', 'kind': 'highway',
             'shield_text': '95'})

    def test_roads_not_present_at_zoom_3(self):
        # but not at zoom 3 or 4
        self.assert_no_matching_feature(
            3, 2, 3, 'roads',
            {'source': 'naturalearthdata.com', 'kind': 'highway',
             'shield_text': '95'})

    def test_roads_not_present_at_zoom_4(self):
        self.assert_no_matching_feature(
            4, 4, 6, 'roads',
            {'source': 'naturalearthdata.com', 'kind': 'highway',
             'shield_text': '95'})
