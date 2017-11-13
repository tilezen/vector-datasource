from . import FixtureTest


class GatesLineGeometry(FixtureTest):
    def test_linear_gate(self):
        # Add barrier:gates with line geometries in landuse
        # Line barrier:ghate feature
        self.load_fixtures(['http://www.openstreetmap.org/way/391260223'])

        self.assert_has_feature(
            16, 10482, 25335, 'landuse',
            {'id': 391260223, 'kind': 'gate'})
