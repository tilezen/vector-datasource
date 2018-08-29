# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class EarlierPiers(FixtureTest):

    def test_very_large_pier(self):
        # a very, very large pier which alters the coastline visually, so
        # should be kept until z11.
        self.generate_fixtures(dsl.way(377915546, wkt_loads('POLYGON ((121.369997686123 25.16007715057551, 121.389781463288 25.16886019888699, 121.393176645904 25.16588309891378, 121.393223358299 25.16575162904959, 121.393218956554 25.1655327562094, 121.380700483913 25.16002364948639, 121.380536810868 25.16032132014178, 121.371928345332 25.15653415695679, 121.369997686123 25.16007715057551))'), {u'name': u'\u7b2c\u4e00\u8ca8\u6ac3\u5132\u904b\u4e2d\u5fc3', u'area': u'yes', u'way_area': u'1.31001e+06', u'man_made': u'pier', u'source': u'openstreetmap.org', u'operator': u'\u53f0\u5317\u6e2f\u8ca8\u6ac3\u78bc\u982d\u516c\u53f8'}))  # noqa

        self.assert_has_feature(
            11, 1714, 876, 'landuse',
            {'id': 377915546, 'kind': 'pier', 'min_zoom': 11})

    def test_cruise_terminal(self):
        # zoom 11 for Cruise Terminal with area 53,276
        self.generate_fixtures(dsl.way(275609726, wkt_loads('POLYGON ((-117.176719701526 32.7179229716355, -117.176661221201 32.71797111545498, -117.173474717225 32.7179511626036, -117.173464925588 32.7168440746718, -117.17667819936 32.71684596416999, -117.176703711514 32.7168737019992, -117.176719701526 32.7179229716355))'), {u'source': u'openstreetmap.org', u'way_area': u'53276.3', u'man_made': u'pier', u'name': u'Cruise Terminal'}))  # noqa

        self.assert_has_feature(
            11, 357, 826, 'landuse',
            {'id': 275609726, 'kind': 'pier', 'min_zoom': 11.22})

    def test_broadway_pier(self):
        # zoom 12 for Broadway Pier with area 17,856
        self.generate_fixtures(dsl.way(275609725, wkt_loads('POLYGON ((-117.176717725232 32.71556026475498, -117.176717725232 32.71586825686789, -117.176676223066 32.7158965240661, -117.173469596828 32.71589319851391, -117.173405187622 32.7158976577771, -117.173402492676 32.71553320674671, -117.17348028678 32.71552640445288, -117.173583593037 32.7155264800339, -117.176681523126 32.7155310148966, -117.176717725232 32.71556026475498))'), {u'source': u'openstreetmap.org', u'way_area': u'17855.9', u'man_made': u'pier', u'name': u'Broadway Pier'}))  # noqa

        self.assert_has_feature(
            12, 714, 1653, 'landuse',
            {'id': 275609725, 'kind': 'pier', 'min_zoom': 12})

    def test_smaller_unnamed_pier(self):
        # zoom 12 for unnamed pier with area 4,734
        self.generate_fixtures(dsl.way(275609722, wkt_loads('POLYGON ((-117.175814469214 32.71132656919218, -117.175718529142 32.71141069481718, -117.17566966079 32.71143488186461, -117.175632380706 32.7114030607791, -117.175599322703 32.7113747921568, -117.175648909707 32.71133820922049, -117.175576505495 32.7112800846483, -117.175587195447 32.71127222384509, -117.174076408802 32.7098766179425, -117.174094464939 32.7098630124915, -117.173743762653 32.70953239939531, -117.173824341534 32.70947366895718, -117.175814469214 32.71132656919218))'), {u'source': u'openstreetmap.org', u'way_area': u'4734.17', u'man_made': u'pier', u'area': u'yes'}))  # noqa

        self.assert_has_feature(
            12, 714, 1653, 'landuse',
            {'id': 275609722, 'kind': 'pier', 'min_zoom': 12.96})
