# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class NaturalManMade(FixtureTest):
    def test_mineshaft(self):
        self.generate_fixtures(dsl.way(4305375025, wkt_loads('POINT (-65.8005543126559 -28.3582812901338)'), {u'source': u'openstreetmap.org', u'man_made': u'mineshaft', u'name': u'Mina de Mica'}))  # noqa

        self.assert_has_feature(
            15, 10394, 19077, 'pois',
            {'kind': 'mineshaft'})

    def test_adit(self):
        self.generate_fixtures(dsl.way(369156437, wkt_loads('POINT (-114.455269505867 37.91662969370819)'), {u'name': u'California Pioche Mine', u'gnis:feature_type': u'Mine', u'man_made': u'adit', u'addr:state': u'NV', u'ele': u'1931', u'source': u'openstreetmap.org', u'gnis:created': u'04/01/1991', u'gnis:feature_id': u'853313', u'gnis:county_name': u'Lincoln'}))  # noqa

        self.assert_has_feature(
            16, 11932, 25298, 'pois',
            {'kind': 'adit'})

    def test_water_well(self):
        self.generate_fixtures(dsl.way(2794798164, wkt_loads('POINT (-122.047650893683 37.33775329446557)'), {u'operator': u'City of Sunnyvale', u'source': u'openstreetmap.org', u'man_made': u'water_well', u'name': u'Westmore Well'}))  # noqa

        self.assert_has_feature(
            16, 10549, 25431, 'pois',
            {'kind': 'water_well', 'min_zoom': 17})

    def test_saddle(self):
        self.generate_fixtures(dsl.way(966585438, wkt_loads('POINT (-119.249509096767 37.76157817043759)'), {u'source': u'openstreetmap.org', u'mountain_pass': u'yes', u'natural': u'saddle', u'name': u'Donohue Pass'}))  # noqa

        self.assert_has_feature(
            14, 2764, 6333, 'pois',
            {'kind': 'saddle'})

    def test_geyser(self):
        self.generate_fixtures(dsl.way(358832354, wkt_loads('POINT (-122.602134116344 38.5969426835878)'), {u'gnis:state_id': u'06', u'natural': u'geyser', u'name': u'Old Faithful Geyser of California', u'geyser:type': u'artificial,volcanic', u'gnis:county_id': u'055', u'ele': u'124', u'source': u'openstreetmap.org', u'gnis:created': u'07/20/1998', u'gnis:feature_id': u'1800305', u'tourism': u'attraction'}))  # noqa

        self.assert_has_feature(
            15, 5224, 12570, 'pois',
            {'kind': 'geyser'})

    def test_hot_spring(self):
        self.generate_fixtures(dsl.way(4020311689, wkt_loads('POINT (-120.642340566756 35.58781338516199)'), {u'tourism': u'attraction', u'natural': u'hot_spring', u'name': u'Franklin Hot Springs', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_has_feature(
            16, 10805, 25827, 'pois',
            {'kind': 'hot_spring'})

    def test_rock(self):
        self.generate_fixtures(dsl.way(1804644217, wkt_loads('POINT (-29.3124196557784 -20.5210076219402)'), {u'seamark:type': u'rock', u'seamark:rock:water_level': u'submerged', u'natural': u'rock', u'name': u'Pedra do Meio', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_has_feature(
            16, 27431, 36586, 'pois',
            {'kind': 'rock', 'min_zoom': 17})
