from . import FixtureTest


class Raceway(FixtureTest):
    def test_raceway_1(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/28825404'])

        self.assert_has_feature(
            16, 10476, 25242, 'roads',
            {'id': 28825404, 'kind': 'minor_road', 'kind_detail': 'raceway',
             'sort_rank': 375})

    def test_raceway_2(self):
        # Thunderoad Speedway Go-carts
        self.load_fixtures(['https://www.openstreetmap.org/way/59440900'])

        self.assert_has_feature(
            16, 10516, 25247, 'roads',
            {'id': 59440900, 'kind': 'minor_road', 'kind_detail': 'raceway',
             'sort_rank': 375})
