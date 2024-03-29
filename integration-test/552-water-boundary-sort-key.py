# -*- encoding: utf-8 -*-
import dsl
from shapely.wkt import loads as wkt_loads

from . import FixtureTest


class WaterBoundarySortKey(FixtureTest):
    def test_water_boundary_sort_key(self):
        # from https://github.com/mapzen/vector-datasource/issues/552
        self.generate_fixtures(dsl.way(1, wkt_loads(
            'POLYGON ((-122.3876870340772 37.78978681046502, -122.3879109580894 37.78970763238332, -122.3881711928106 37.78970763238332, -122.3882821 37.7897408, -122.3883666 37.7898383, -122.3884229 37.78992629999998, -122.3882311 37.789991, -122.3882378 37.79000370000001, -122.3884042 37.79032100000001, -122.3884323 37.79037459999996, -122.38862 37.79031209999999, -122.3886311 37.79033260000002, -122.3889325 37.79088969999999, -122.3888065 37.7909819, -122.3917249 37.7934276, -122.3916442 37.79348940000001, -122.3916078957368 37.7935126370961, -122.3876870340772 37.7935126370961, -122.3876870340772 37.78978681046502))'), {u'source': u'osmdata.openstreetmap.de', u'fid': 3610}))

        self.assert_has_feature(
            16, 10487, 25327, 'water',
            {'kind': 'ocean', 'boundary': True, 'sort_rank': 205})
