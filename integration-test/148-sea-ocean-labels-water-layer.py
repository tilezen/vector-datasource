from . import OsmFixtureTest


# ocean and sea labels should be in the water layer rather than the places
# layer.
class SeaOceanLabelsWaterLayer(OsmFixtureTest):

    def test_gulf_of_california(self):
        # Gulf of California: http://www.openstreetmap.org/node/305639734
        self.load_fixtures([
            'http://www.openstreetmap.org/node/305639734',
        ])
        self.assert_has_feature(
            9, 97, 215, 'water',
            {'kind': 'sea', 'name': 'Gulf of California',
             'label_placement': True})
        self.assert_no_matching_feature(
            9, 97, 215, 'places',
            {'kind': 'sea', 'name': 'Gulf of California'})

    def test_greenland_sea(self):
        # Greenland Sea: http://www.openstreetmap.org/node/305639396
        self.load_fixtures([
            'http://www.openstreetmap.org/node/305639396',
        ])
        self.assert_has_feature(
            9, 241, 90, 'water',
            {'kind': 'sea', 'name': 'Greenland Sea',
             'label_placement': True})
        self.assert_no_matching_feature(
            9, 241, 90, 'places',
            {'kind': 'sea', 'name': 'Greenland Sea'})

# NOTE: No ocean points in the North America extract :-(
