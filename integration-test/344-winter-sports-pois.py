# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class WinterSportsPois(FixtureTest):

    def test_ski_shop(self):
        # ski shop in Big Bear Lake, CA
        self.generate_fixtures(dsl.way(2720341705, wkt_loads('POINT (-116.889174638465 34.243057498121)'), {u'shop': u'ski', u'source': u'openstreetmap.org', u'name': u'Blauer Board Shop'}))  # noqa

        self.assert_has_feature(
            16, 11488, 26126, 'pois',
            {'kind': 'ski',
             'name': None})

    def test_ski_jumps(self):
        # Ski-jumping "racetracks" in Lake Placid, NY
        self.generate_fixtures(dsl.way(135968170, wkt_loads('LINESTRING (-73.9669287141361 44.2548200600309, -73.9664931210549 44.2550734995694, -73.96614807815421 44.25524097881737, -73.96592592478449 44.2553499076305)'), {u'source': u'openstreetmap.org', u'sport': u'ski_jumping', u'leisure': u'track'}),dsl.way(135968168, wkt_loads('LINESTRING (-73.9663000731003 44.2547990847879, -73.9658996041467 44.25506088874239, -73.96556920378509 44.25525146636098)'), {u'source': u'openstreetmap.org', u'sport': u'ski_jumping', u'leisure': u'track'}),dsl.way(135968166, wkt_loads('LINESTRING (-73.9657291937372 44.25613620939738, -73.96503847911529 44.25633250975307)'), {u'source': u'openstreetmap.org', u'sport': u'ski_jumping', u'leisure': u'track'}))  # noqa

        self.assert_has_feature(
            16, 19302, 23765, 'roads',
            {'kind': 'racetrack',
             'leisure': 'track',
             'kind_detail': 'ski_jumping'})
