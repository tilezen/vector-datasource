# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class NormalizeUnderscore(FixtureTest):
    def test_drive_through(self):
        self.generate_fixtures(dsl.way(219071307, wkt_loads('LINESTRING (-122.439743506477 37.74433156222058, -122.439601931988 37.74445487765141)'), {u'source': u'openstreetmap.org', u'service': u'drive-through', u'highway': u'service', u'oneway': u'yes'}))  # noqa

        self.assert_has_feature(
            16, 10478, 25338, 'roads',
            {'id': 219071307, 'kind': 'minor_road',
             'service': 'drive_through'})

    def test_ski_lift_t_bar(self):
        self.generate_fixtures(dsl.way(258020271, wkt_loads('LINESTRING (-119.148929585307 37.22200869601988, -119.15274482015 37.21744005458098)'), {u'source': u'openstreetmap.org', u'name': u'Firebowl', u'aerialway': u't-bar'}))  # noqa

        self.assert_has_feature(
            16, 11077, 25458, 'roads',
            {'id': 258020271, 'kind': 'aerialway', 'kind_detail': 't_bar'})

    def test_ski_lift_j_bar(self):
        self.generate_fixtures(dsl.way(256717307, wkt_loads('LINESTRING (-76.92694539811389 40.108910216706, -76.9271689887881 40.10789646600079)'), {u'source': u'openstreetmap.org', u'name': u'J-Bar', u'aerialway': u'j-bar'}))  # noqa

        self.assert_has_feature(
            16, 18763, 24784, 'roads',
            {'id': 256717307, 'kind': 'aerialway', 'kind_detail': 'j_bar'})

    def test_aerialway_no_detail(self):
        self.generate_fixtures(dsl.way(232074914, wkt_loads('LINESTRING (-106.9157086076 39.2062991907858, -106.916424834376 39.20577900674078)'), {u'source': u'openstreetmap.org', u'fixme': u'Please confirm that this actually is an aerialway.', u'aerialway': u'yes'}))  # noqa

        self.assert_has_feature(
            16, 13304, 24998, 'roads',
            {'id': 232074914, 'kind': 'aerialway', 'kind_detail': type(None)})
