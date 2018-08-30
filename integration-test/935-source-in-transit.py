# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class SourceInTransit(FixtureTest):
    def test_source_in_transit(self):
        # Add source info in transit
        # Way: 189011731
        self.generate_fixtures(dsl.way(189011731, wkt_loads('LINESTRING (-122.389305888051 37.76950410648259, -122.389265104537 37.76907278971079)'), {u'tram': u'yes', u'source': u'openstreetmap.org', u'railway': u'platform', u'public_transport': u'platform'}))  # noqa

        self.assert_has_feature(
            16, 10487, 25332, 'transit',
            {'id': 189011731, 'kind': 'platform',
             'source': 'openstreetmap.org'})
