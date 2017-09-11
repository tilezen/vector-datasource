from . import OsmFixtureTest


class CliffAreteRidgeValley(OsmFixtureTest):
    def test_cliff(self):
        # cliff in Yosemite
        self.load_fixtures(['https://www.openstreetmap.org/way/291684864'])

        self.assert_has_feature(
            13, 1374, 3166, "earth",
            {"kind": "cliff", "id": 291684864,
             "sort_rank": 227})

    def test_arete(self):
        # arete in Yosemite
        self.load_fixtures(['https://www.openstreetmap.org/way/375271242'])

        self.assert_has_feature(
            13, 1379, 3164, "earth",
            {"kind": "arete", "id": 375271242,
             "sort_rank": 228})

    def test_ridge(self):
        # ridge with name in Santa Cruz Mountains, California
        self.load_fixtures(['https://www.openstreetmap.org/way/115675159'])

        self.assert_has_feature(
            13, 1317, 3182, "earth",
            {"kind": "ridge", "id": 115675159,
             "name": "Castle Rock Ridge", "label_placement": True})

    def test_valley(self):
        # valley with name in Yosemite
        # https://www.openstreetmap.org/way/407467016
        self.load_fixtures(['https://www.openstreetmap.org/way/407467016'])

        self.assert_has_feature(
            13, 1381, 3164, "earth",
            {"kind": "valley", "id": 407467016,
             "name": "Lyell Canyon", "label_placement": True})
