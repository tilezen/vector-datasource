from . import OsmFixtureTest


class NormalizePoiKind(OsmFixtureTest):
    def test_aeroway_gate(self):
        # Node: Gate G102 (1096088604)
        self.load_fixtures(['http://www.openstreetmap.org/node/1096088604'])

        self.assert_has_feature(
            16, 10487, 25366, 'pois',
            {'id': 1096088604, 'kind': 'aeroway_gate'})

    def test_gate_not_aeroway(self):
        # TODO: not sure what this is testing? the node seems to have been
        # updated recently to remove the aeroway=gate tag.
        # Node: Gate 1 (2618197593)
        self.load_fixtures(['http://www.openstreetmap.org/node/2618197593',
                            'http://www.openstreetmap.org/way/320595943'])

        self.assert_has_feature(
            16, 10309, 22665, 'pois',
            {'id': 2618197593, 'kind': 'gate', 'aeroway': type(None)})

    def test_ski_rental(self):
        # Node: Lone Star Sports
        self.load_fixtures(['http://www.openstreetmap.org/node/2122898936'])

        self.assert_has_feature(
            16, 13462, 24933, 'pois',
            {'id': 2122898936, 'kind': 'ski_rental'})

    def test_wood(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/52497271'])

        self.assert_has_feature(
            16, 10566, 25429, 'landuse',
            {'id': 52497271, 'kind': 'wood'})

        self.load_fixtures(['http://www.openstreetmap.org/way/207859675'])

        self.assert_has_feature(
            16, 11306, 26199, 'landuse',
            {'id': 207859675, 'kind': 'wood'})

    def test_natural_wood(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/417405367'])

        self.assert_has_feature(
            16, 10480, 25323, 'landuse',
            {'id': 417405367, 'kind': 'natural_wood'})

    def test_forest(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/422270533'])

        self.assert_has_feature(
            16, 10476, 25324, 'landuse',
            {'id': 422270533, 'kind': 'forest'})

    def test_natural_forest(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/95360670'])

        self.assert_has_feature(
            16, 17780, 27428, 'landuse',
            {'id': 95360670, 'kind': 'natural_forest'})

    def test_park(self):
        # Way: Stables & Equestrian Area (393312618)
        self.load_fixtures(['http://www.openstreetmap.org/way/393312618'])

        self.assert_has_feature(
            16, 10294, 25113, 'landuse',
            {'id': 393312618, 'kind': 'park'})

    def test_natural_park(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/469494860'])

        self.assert_has_feature(
            16, 17612, 24209, 'landuse',
            {'id': 469494860, 'kind': 'natural_park'})
