from . import FixtureTest


class WindmillZoom(FixtureTest):
    def test_windmill_with_attraction(self):
        # update windmill zoom to 15 and if attraction zoom to 14
        # windmill with tourism = attraction
        self.load_fixtures(['http://www.openstreetmap.org/way/287921407'])

        self.assert_has_feature(
            14, 2616, 6333, 'pois',
            {'id': 287921407, 'kind': 'windmill'})

    def test_windmill_without_attraction(self):
        # windmill without tourism = attraction
        self.load_fixtures(['http://www.openstreetmap.org/node/2304462088'])

        self.assert_no_matching_feature(
            14, 2675, 6412, 'pois',
            {'id': 2304462088, 'kind': 'windmill'})

        self.assert_has_feature(
            15, 5350, 12824, 'pois',
            {'id': 2304462088, 'kind': 'windmill'})
