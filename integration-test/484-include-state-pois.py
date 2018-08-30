# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class IncludeStatePois(FixtureTest):
    def test_proposed_stations(self):
        # Antioch Station
        self.generate_fixtures(dsl.way(3353451464, wkt_loads('POINT (-121.785229642994 37.99688077243528)'), {u'name': u'Antioch Station (in construction)', u'source': u'openstreetmap.org', u'state': u'proposed', u'train': u'yes', u'public_transport': u'station', u'operator': u'BART', u'railway': u'station'}))  # noqa

        self.assert_has_feature(
            16, 10597, 25279, 'pois',
            {'id': 3353451464, 'state': 'proposed'})

        # Pittsburg Center
        self.generate_fixtures(dsl.way(3354463416, wkt_loads('POINT (-121.88916373322 38.01684868163071)'), {u'toilets': u'yes', u'name': u'BART - Pittsburg Center Station (In Construction)', u'wheelchair': u'yes', u'source': u'openstreetmap.org', u'state': u'proposed', u'train': u'yes', u'public_transport': u'station', u'operator': u'BART', u'railway': u'station', u'toilets:wheelchair': u'yes'}))  # noqa

        self.assert_has_feature(
            16, 10578, 25275, 'pois',
            {'id': 3354463416, 'state': 'proposed'})
