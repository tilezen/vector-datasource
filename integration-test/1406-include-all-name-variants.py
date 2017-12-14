from . import FixtureTest


class IncludeAllNameVariants(FixtureTest):

    def test_duplicate_names(self):
        self.load_fixtures([
            'http://www.openstreetmap.org/node/206270454',
        ])

        self.assert_has_feature(
            15, 18199, 11103, 'pois',
            {'id': 206270454, 'kind': 'station',
             'name': None, 'name:pl': None})
