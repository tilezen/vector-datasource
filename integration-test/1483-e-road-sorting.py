# -*- encoding: utf-8 -*-
from . import FixtureTest


class ERoadSortTest(FixtureTest):
    def test_eroad_a90_e90(self):
        # Sort A-road first, then e-road
        self.load_fixtures(
            ['https://www.openstreetmap.org/way/188060822',
             'https://www.openstreetmap.org/relation/2000662',
             'https://www.openstreetmap.org/relation/2870369',
             'https://www.openstreetmap.org/relation/2084465'])

        # We could test on GRA shield_text but there's an unrelated bug
        # We could test to ensure e-road network in all_networks
        self.assert_has_feature(
            16, 35043, 24378, 'roads',
            {'id': 188060822, 'kind': 'highway', 'network': 'IT:A-road'})
