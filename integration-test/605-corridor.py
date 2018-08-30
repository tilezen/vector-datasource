# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class Corridor(FixtureTest):
    def test_corridor(self):
        # Way: The Nave (205644309)
        self.generate_fixtures(dsl.way(2156202856, wkt_loads('POINT (-122.400024406358 37.76714596457248)'), {u'source': u'openstreetmap.org', u'entrance': u'main_entrance'}),dsl.way(205644309, wkt_loads('LINESTRING (-122.399059525911 37.76790309481861, -122.400024406358 37.76714596457248, -122.400131395708 37.7670594714286)'), {u'source': u'openstreetmap.org', u'name': u'The Nave', u'highway': u'corridor'}))  # noqa

        self.assert_has_feature(
            16, 10485, 25332, 'roads',
            {'id': 205644309, 'kind': 'path', 'kind_detail': 'corridor'})
