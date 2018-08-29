# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class Subways(FixtureTest):
    def test_subway(self):
        self.generate_fixtures(dsl.way(101647480, wkt_loads('LINESTRING (-122.470410283477 37.6963250949029, -122.470486730108 37.69652141854918, -122.4706878629 37.6970339046909, -122.470759009471 37.69722070181008, -122.470824676318 37.6974158858161, -122.470882258328 37.69761441002629, -122.47092528763 37.69781698520299, -122.470956099844 37.69802816035058, -122.470974874633 37.69825205794847, -122.470987990037 37.69851305772319, -122.470991044309 37.69875507875209, -122.471008291962 37.69974149285229)'), {u'source': u'openstreetmap.org', u'railway': u'subway', u'name': u'Bay Area Rapid Transit'}))  # noqa

        self.assert_has_feature(
            16, 10472, 25348, 'roads',
            {'kind': 'rail', 'kind_detail': 'subway', 'id': 101647480,
             'sort_rank': 382})
