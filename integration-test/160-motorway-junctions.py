from . import FixtureTest


class MotorwayJunctions(FixtureTest):

    def test_motorway_junctions(self):
        self.load_fixtures([
            'http://www.openstreetmap.org/node/733619113',
        ])

        self.assert_has_feature(
            16, 10483, 25332, 'pois', {
                'kind': 'motorway_junction'})

        self.assert_has_feature(
            14, 2620, 6333, 'pois', {
                'kind': 'motorway_junction'})
