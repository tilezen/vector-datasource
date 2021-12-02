from . import FixtureTest


# Set gate min zoom based on highway type
class GateMinZoom(FixtureTest):

    def test_gate_on_secondary(self):
        # Gate on secondary road
        self.load_fixtures([
            'https://www.openstreetmap.org/node/5074813186',
            'https://www.openstreetmap.org/way/520725578',
        ])

        self.assert_has_feature(
            15, 5528, 12649, 'pois',
            {'id': 5074813186, 'kind': 'gate', 'min_zoom': 15})

    def test_gate_on_minor_road(self):
        # Gate on minor road
        self.load_fixtures([
            'http://www.openstreetmap.org/node/2591034891',
            'http://www.openstreetmap.org/way/784680412',
        ])

        self.assert_has_feature(
            16, 19244, 24628, 'pois',
            {'id': 2591034891, 'kind': 'gate', 'min_zoom': 16})

        self.assert_no_matching_feature(
            15, 9622, 12314, 'pois',
            {'id': 2591034891, 'kind': 'gate'})

    def test_gate_on_unclassified_road(self):
        # Gate on unclassified road
        self.load_fixtures([
            'http://www.openstreetmap.org/node/276321344',
            'http://www.openstreetmap.org/way/70807512',
        ])

        self.assert_has_feature(
            16, 10549, 25415, 'pois',
            {'id': 276321344, 'kind': 'gate', 'min_zoom': 16})

        self.assert_no_matching_feature(
            15, 5274, 12707, 'pois',
            {'id': 276321344, 'kind': 'gate'})

    def test_footway(self):
        # Gate on footway
        self.load_fixtures([
            'http://www.openstreetmap.org/node/302482019',
            'http://www.openstreetmap.org/way/27553445',
        ])

        self.assert_has_feature(
            16, 10466, 25328, 'pois',
            {'id': 302482019, 'kind': 'gate', 'min_zoom': 16})

        self.assert_no_matching_feature(
            15, 5233, 12664, 'pois',
            {'id': 302482019, 'kind': 'gate'})

    def test_gate_on_fence(self):
        # Gate on a fence
        self.load_fixtures([
            'http://www.openstreetmap.org/node/4320045170',
            'http://www.openstreetmap.org/way/427290222',
        ])

        self.assert_has_feature(
            16, 10479, 25344, 'pois',
            {'id': 4320045170, 'kind': 'gate', 'min_zoom': 17})
