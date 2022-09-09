import unittest

from . import FixtureTest
from . import SKIP_UNIT_TEST_MESSAGE


@unittest.skip(SKIP_UNIT_TEST_MESSAGE)
class MissingRoad(FixtureTest):
    def test_route_611(self):
        # Relation: route 611 (975266)
        self.load_fixtures(
            ['https://www.openstreetmap.org/relation/975266'],
            clip=self.tile_bbox(12, 1192, 1539))

        self.assert_has_feature(
            12, 1192, 1539, 'roads',
            {'kind': 'major_road',
             'shield_text': '611',
             'ref': 'PA 611',
             'all_shield_texts': ['611'],
             })
