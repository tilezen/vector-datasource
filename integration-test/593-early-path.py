import unittest

from . import FixtureTest
from . import SKIP_UNIT_TEST_REASON


class EarlyPath(FixtureTest):
    def test_pacific_crest_trail(self):
        # highway=path, with route national (Pacific Crest Trail)
        import dsl

        z, x, y = (14, 2616, 6328)

        self.generate_fixtures(
            dsl.way(236361475, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org',
                'highway': 'path',
                'foot': 'yes',
                'bicycle': 'no',
                'ref': 'PCT',
                'alt_name': 'Pacific Crest National Scenic Trail',
                'horse': 'yes',
                'motorcar': 'name',
                'name': 'Pacific Crest Trail',
                'network': 'nwn',
                'ref': 'PCT Section H'
            }),
            dsl.relation(1225378, {
                'source': 'openstreetmap.org',
                'type': 'route',
                'route': 'hiking',
                'network': 'nwn',
                'ref': 'PCT',
                'name': 'Pacific Crest Trail',
            }, ways=[236361475]),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'walking_network': 'nwn',
             'walking_shield_text': 'PCT'})

    @unittest.skip(SKIP_UNIT_TEST_REASON)
    def test_merced_pass_trail(self):
        # highway=path, with route regional (Merced Pass Trail)
        self.load_fixtures(
            ['https://www.openstreetmap.org/way/373491941',
             'https://www.openstreetmap.org/relation/5549623'],
            clip=self.tile_bbox(12, 687, 1584))

        self.assert_has_feature(
            12, 687, 1584, 'roads',
            {'kind_detail': 'path', 'name': None, 'walking_network': None})

        # highway=path, with route regional (Merced Pass Trail)
        self.load_fixtures(
            ['https://www.openstreetmap.org/way/39996451',
             'https://www.openstreetmap.org/relation/5549623'],
            clip=self.tile_bbox(12, 688, 1584))

        self.assert_has_feature(
            12, 688, 1584, 'roads',
            {'kind_detail': 'path', 'name': None, 'walking_network': None})

    @unittest.skip(SKIP_UNIT_TEST_REASON)
    def test_upper_yosemite_falls_trail(self):
        # highway=path, no route, but has name (Upper Yosemite Falls Trail)
        self.load_fixtures(['https://www.openstreetmap.org/way/162322353'])

        self.assert_has_feature(
            13, 1374, 3166, 'roads',
            {'kind_detail': 'path', 'name': None})
