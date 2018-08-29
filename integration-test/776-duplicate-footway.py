# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


# we used to duplicate footway features between the roads and landuse layers.
# this test exists to make sure we don't backslide.
# see https://github.com/tilezen/vector-datasource/issues/776 for more info.
class DuplicateFootway(FixtureTest):

    def test_pedestrian(self):
        self.generate_fixtures(dsl.way(128534087, wkt_loads('LINESTRING (-122.420156819685 37.77915886514469, -122.420667601755 37.77909389933378)'), {u'source': u'openstreetmap.org', u'highway': u'pedestrian'}))  # noqa

        self.assert_has_feature(
            16, 10482, 25330, 'roads',
            {'id': 128534087})

        self.assert_no_matching_feature(
            16, 10482, 25330, 'landuse',
            {'id': 128534087})

    def test_footway(self):
        self.generate_fixtures(dsl.way(367756094, wkt_loads('LINESTRING (-122.511661460313 37.7742249220812, -122.511574772888 37.7742313125844, -122.511478563322 37.7742386971651)'), {u'source': u'openstreetmap.org', u'highway': u'footway'}))  # noqa

        self.assert_has_feature(
            16, 10465, 25331, 'roads',
            {'id': 367756094})

        self.assert_no_matching_feature(
            16, 10465, 25331, 'landuse',
            {'id': 367756094})
