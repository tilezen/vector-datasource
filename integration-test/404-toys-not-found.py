import unittest

import dsl

from . import FixtureTest
from . import SKIP_UNIT_TEST_MESSAGE


class ToysNotFound(FixtureTest):

    def test_01(self):
        # https://www.openstreetmap.org/way/215472849
        z, x, y = (16, 10473, 25339)

        self.generate_fixtures(
            dsl.point(215472849, dsl.tile_centre(z, x, y),
                      {'phone': '+1 415 759 TOYS', 'height': '7', 'building': 'retail',
                       'name': 'Ambassador Toys', 'opening_hours': 'Mo-Su 10:00-19:00',
                       'shop': 'toys', 'addr:city': 'San Francisco', 'addr:country': 'US',
                       'addr:housenumber': '186', 'addr:postcode': '94127', 'addr:state': 'CA',
                       'addr:street': 'West Portal Avenue'}))

        self.assert_has_feature(
            z, x, y, 'pois',
            {'kind': 'toys'})

    def test_02(self):
        self._run_test(16, 10479, 25336,
                       'https://www.openstreetmap.org/node/1713279804')

    def test_03(self):
        self._run_test(16, 10480, 25337,
                       'https://www.openstreetmap.org/node/3188857553')

    def test_04(self):
        # https://www.openstreetmap.org/node/3396659022
        z, x, y = (16, 10484, 25328)

        self.generate_fixtures(
            dsl.point(3396659022, dsl.tile_centre(z, x, y),
                      {'name': 'Disney Store', 'shop': 'toys'}))

        self.assert_has_feature(
            z, x, y, 'pois',
            {'kind': 'toys'})

    def test_05(self):
        # https://www.openstreetmap.org/node/1467717312
        z, x, y = (16, 10506, 25318)

        self.generate_fixtures(
            dsl.point(2286100659, dsl.tile_centre(z, x, y),
                      {'name': 'Michaels Arts and Crafts', 'shop': 'toys'}))

        self.assert_has_feature(
            z, x, y, 'pois',
            {'kind': 'toys'})

    def test_06(self):
        # https://www.openstreetmap.org/node/2286100659
        z, x, y = (16, 10509, 25308)

        self.generate_fixtures(
            dsl.point(2286100659, dsl.tile_centre(z, x, y),
                      {'wheelchair': 'yes', 'name': 'Eudemonia', 'shop': 'toys',
                       'website': 'http://www.eudemonia.com/', 'addr:city': 'Berkeley',
                       'addr:housenumber': '2154', 'addr:street': 'University Avenue'}))

        self.assert_has_feature(
            z, x, y, 'pois',
            {'kind': 'toys'})

    def test_07(self):
        self._run_test(16, 10514, 25322,
                       'https://www.openstreetmap.org/node/3711137981')

    def test_08(self):
        self._run_test(16, 19298, 24633,
                       'https://www.openstreetmap.org/node/3810578539')

    def test_09(self):
        self._run_test(16, 19300, 24630,
                       'https://www.openstreetmap.org/node/1429062988')

    @unittest.skip(SKIP_UNIT_TEST_MESSAGE)
    def test_10(self):
        self._run_test(16, 19300, 24629,
                       'https://www.openstreetmap.org/node/1058296287')

    def _run_test(self, z, x, y, url):
        self.load_fixtures([url])

        self.assert_has_feature(
            z, x, y, 'pois',
            {'kind': 'toys'})
