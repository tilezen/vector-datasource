from . import OsmFixtureTest


class WinterSportsPois(OsmFixtureTest):

    def test_ski_shop(self):
        # ski shop in Big Bear Lake, CA
        self.load_fixtures(['https://www.openstreetmap.org/node/2720341705'])

        self.assert_has_feature(
            16, 11488, 26126, 'pois',
            {'kind': 'ski',
             'name': None})

    def test_ski_jumps(self):
        # Ski-jumping "racetracks" in Lake Placid, NY
        self.load_fixtures(['https://www.openstreetmap.org/way/135968166',
                            'https://www.openstreetmap.org/way/135968170',
                            'https://www.openstreetmap.org/way/135968168'])

        self.assert_has_feature(
            16, 19302, 23765, 'roads',
            {'kind': 'racetrack',
             'leisure': 'track',
             'kind_detail': 'ski_jumping'})
