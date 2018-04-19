from . import FixtureTest


class EarlyUnclassifiedRoads(FixtureTest):

    def test_early_unclassified_road1_utah(self):
        self.load_fixtures([
            'https://www.openstreetmap.org/way/315437880',
        ])

        self.assert_has_feature(
            11, 388, 790, 'roads',
            {'kind': 'minor_road',
             'kind_detail': 'unclassified'})

    def test_early_unclassified_road2_utah(self):
        self.load_fixtures([
            'https://www.openstreetmap.org/way/10203268',
        ])

        self.assert_has_feature(
            11, 389, 787, 'roads',
            {'kind': 'minor_road',
             'kind_detail': 'unclassified'})

    def test_early_unclassified_road3_california(self):
        self.load_fixtures([
            'https://www.openstreetmap.org/way/7712776',
        ])

        self.assert_has_feature(
            11, 323, 785, 'roads',
            {'kind': 'minor_road',
             'kind_detail': 'unclassified'})
