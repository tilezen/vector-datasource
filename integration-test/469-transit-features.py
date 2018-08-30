# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class TransitFeatures(FixtureTest):
    def test_bus_stop_way(self):
        # way 91806504
        self.generate_fixtures(dsl.way(91806504, wkt_loads('LINESTRING (-122.485366604137 37.83936229124878, -122.48536498717 37.83933050878218, -122.485321598542 37.83933185669962, -122.485323305341 37.83936371010859, -122.485366604137 37.83936229124878)'), {u'source': u'openstreetmap.org', u'highway': u'platform'}))  # noqa

        self.assert_has_feature(
            16, 10470, 25316, 'transit',
            {'kind': 'bus_stop'})

    def test_bus_stop_node(self):
        # node 1241518350
        self.generate_fixtures(dsl.way(1241518350, wkt_loads('POINT (-122.429272204536 37.76962539168078)'), {u'local_ref': u'22 Fillmore', u'name': u'Church & Doboce', u'bus': u'yes', u'wheelchair': u'yes', u'source': u'openstreetmap.org', u'public_transport': u'platform'}))  # noqa

        self.assert_has_feature(
            16, 10480, 25332, 'pois',
            {'kind': 'bus_stop'})

    def test_platform(self):
        # way 196670577
        self.generate_fixtures(dsl.way(196670577, wkt_loads('LINESTRING (-122.394100017059 37.79533960862489, -122.394350826686 37.79561410831099)'), {u'covered': u'yes', u'railway': u'platform', u'public_transport': u'platform', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_has_feature(
            16, 10486, 25326, 'transit',
            {'kind': 'platform'})
