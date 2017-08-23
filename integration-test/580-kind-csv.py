from . import OsmFixtureTest


class KindCsv(OsmFixtureTest):
    def test_post_office(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/1223019595'])

        self.assert_has_feature(
            16, 10486, 25326, 'pois',
            {'kind': 'post_office'})

    def test_museum(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/317081601'])

        self.assert_has_feature(
            16, 10485, 25329, 'pois',
            {'kind': 'museum'})

    def test_gate(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/3910307149',
                            'https://www.openstreetmap.org/way/387798241'])

        self.assert_has_feature(
            16, 10487, 25329, 'pois',
            {'kind': 'gate'})

    def test_enclosure(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/382798029',
                            'https://www.openstreetmap.org/way/382798035'])

        self.assert_has_feature(
            16, 10466, 25340, 'pois',
            {'kind': 'enclosure'})

    def test_forest(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/422270533'])

        self.assert_has_feature(
            16, 10476, 25324, 'landuse',
            {'id': 422270533, 'kind': 'forest'})

    def test_substation(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/274459406',
                            'https://www.openstreetmap.org/way/274459420'])

        self.assert_has_feature(
            16, 10478, 25329, 'landuse',
            {'kind': 'substation'})
