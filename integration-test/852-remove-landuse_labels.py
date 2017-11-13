from . import FixtureTest


class RemoveLanduseLabels(FixtureTest):

    def test_landuse_labels_layer_no_longer_exists(self):
        # Label placement Cemetery in landuse - note that we test the
        # label exists in the landuse layer in test 742.
        self.load_fixtures(['http://www.openstreetmap.org/way/44580948'])

        with self.layers_in_tile(15, 5471, 12981) as layers:
            self.assertTrue('landuse_labels' not in layers)
