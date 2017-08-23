from . import OsmFixtureTest


class EarlyPath(OsmFixtureTest):
    def test_pacific_crest_trail(self):
        # highway=path, with route national (Pacific Crest Trail)
        self.load_fixtures(
            ['https://www.openstreetmap.org/way/236361475',
             'https://www.openstreetmap.org/relation/1225378'],
            clip=self.tile_bbox(11, 345, 790))

        self.assert_has_feature(
            11, 345, 790, 'roads',
            {'walking_network': 'nwn',
             'walking_shield_text': 'PCT'})

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

    def test_upper_yosemite_falls_trail(self):
        # highway=path, no route, but has name (Upper Yosemite Falls Trail)
        self.load_fixtures(['https://www.openstreetmap.org/way/162322353'])

        self.assert_has_feature(
            13, 1374, 3166, 'roads',
            {'kind_detail': 'path', 'name': None})
