from . import FixtureTest


class BayWater(FixtureTest):
    def test_san_pablo_bay(self):
        # San Pablo Bay
        self.load_fixtures(['https://www.openstreetmap.org/way/43950409'])

        self.assert_has_feature(
            14, 2623, 6318, 'water',
            {'kind': 'bay', 'label_placement': True})

    def test_sansum_narrows(self):
        # Sansum Narrows
        self.load_fixtures(['https://www.openstreetmap.org/relation/1019862'])

        self.assert_has_feature(
            11, 321, 705, 'water',
            {'kind': 'strait', 'label_placement': True})

    def test_horsens_fjord(self):
        # Horsens Fjord
        self.load_fixtures(['https://www.openstreetmap.org/relation/1451065'])

        self.assert_has_feature(
            10, 540, 319, 'water',
            {'kind': 'fjord', 'label_placement': True})
