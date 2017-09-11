from . import OsmFixtureTest


class RemoveSea(OsmFixtureTest):
    def test_drop_sea_polygon_but_keep_label(self):
        # Drop sea polygon but keep the label
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/4594226',
        ], simplify=100)

        self.assert_no_matching_feature(
            12, 2315, 1580, 'water',
            {'id': -4594226, 'kind': 'sea', 'label_placement': None})

        self.assert_has_feature(
            9, 292, 197, 'water',
            {'id': -4594226, 'kind': 'sea', 'label_placement': True})

        self.assert_has_feature(
            12, 2338, 1579, 'water',
            {'id': -4594226, 'kind': 'sea', 'label_placement': True})
