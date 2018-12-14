# -*- encoding: utf-8 -*-
import dsl
from . import FixtureTest


# test turning circles and loops
class TurningCirclesAndLoops(FixtureTest):

    def turning_circle(self):
        self.generate_fixtures(
            dsl.point(106186562, (-0.3544854, 51.5785667),
                      {u'source': u'openstreetmap.org',
                       u'highway': u'turning_circle'}))

        self.assert_has_feature(
            16, 32703, 21771, 'pois',
            {'id': 106186562, 'kind': 'turning_circle', 'min_zoom': 17})

    def turning_loop(self):
        self.generate_fixtures(
            dsl.point(4260010359, (8.43452, 49.4596352),
                      {u'source': u'openstreetmap.org',
                       u'highway': u'turning_loop'}))

        self.assert_has_feature(
            16, 34303, 22378, 'pois',
            {'id': 4260010359, 'kind': 'turning_loop', 'min_zoom': 17})
