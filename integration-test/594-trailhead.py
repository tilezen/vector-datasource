# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class Trailhead(FixtureTest):
    def test_trailhead(self):
        self.generate_fixtures(dsl.way(3447700493, wkt_loads('POINT (-122.490783175806 37.78737221370528)'), {u'source': u'openstreetmap.org', u'outerspatial:id': u'19673', u'name': u'China Beach Entrance', u'highway': u'trailhead'}))  # noqa

        self.assert_has_feature(
            15, 5234, 12664, 'pois',
            {'kind': 'trailhead'})
