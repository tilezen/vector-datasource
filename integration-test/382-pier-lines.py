# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class PierLines(FixtureTest):
    def test_pier_in_roads_layer(self):
        self.generate_fixtures(dsl.way(23783924, wkt_loads('LINESTRING (-122.50095902185 37.8738182018396, -122.500377811861 37.87328382336269, -122.501296159576 37.87268746488599, -122.501370989239 37.87273405334987, -122.501576972934 37.87253089339431, -122.502331737436 37.87205167477718)'), {u'source': u'openstreetmap.org', u'man_made': u'pier', u'name': u'Liberty Dock'}))  # noqa

        self.assert_has_feature(
            16, 10467, 25308, 'roads',
            {'kind': 'path',
             'kind_detail': 'pier'})
