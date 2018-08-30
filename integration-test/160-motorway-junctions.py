# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class MotorwayJunctions(FixtureTest):

    def test_motorway_junctions(self):
        self.generate_fixtures(dsl.way(733619113, wkt_loads('POINT (-122.409809844579 37.76916141081359)'), {u'source': u'openstreetmap.org', u'exit_to': u'I 80 East; Bay Bridge; Oakland', u'noref': u'yes', u'highway': u'motorway_junction'}))  # noqa

        self.assert_has_feature(
            16, 10483, 25332, 'pois', {
                'kind': 'motorway_junction'})

        self.assert_has_feature(
            14, 2620, 6333, 'pois', {
                'kind': 'motorway_junction'})
