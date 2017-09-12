from . import FixtureTest


class Subways(FixtureTest):
    def test_subway(self):
        self.load_fixtures(
            ['https://www.openstreetmap.org/way/101647480'])

        self.assert_has_feature(
            16, 10472, 25348, 'roads',
            {'kind': 'rail', 'kind_detail': 'subway', 'id': 101647480,
             'sort_rank': 382})
