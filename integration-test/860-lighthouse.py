from . import FixtureTest


class Lighthouse(FixtureTest):
    def test_with_attraction(self):
        # update lighthouse zoom to 15 and if attraction zoom to 14
        # lighthouse with tourism = attraction
        self.load_fixtures(['https://www.openstreetmap.org/way/423023928'])

        self.assert_has_feature(
            14, 2615, 6330, 'pois',
            {'id': 423023928, 'kind': 'lighthouse'})

    def test_without_attraction(self):
        # lighthouse without tourism = attraction
        self.load_fixtures(['http://www.openstreetmap.org/node/1243877573'])

        self.assert_no_matching_feature(
            14, 2617, 6329, 'pois',
            {'id': 1243877573, 'kind': 'lighthouse'})

        self.assert_has_feature(
            15, 5235, 12659, 'pois',
            {'id': 1243877573, 'kind': 'lighthouse'})
