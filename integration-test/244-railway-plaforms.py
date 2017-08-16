import unittest
from . import OsmFixtureTest


class RailwayPlatforms(OsmFixtureTest):

    def test_hunterspoint_avenue_lirr(self):
        # Hunterspoint Avenue LIRR
        self.load_fixtures([
            'https://www.openstreetmap.org/way/326365794',
        ])
        self.assert_has_feature(
            16, 19306, 24633, 'transit',
            { 'kind': 'platform' })
