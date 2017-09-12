from . import FixtureTest


class BicycleRamps(FixtureTest):

    def test_ramp_properties_on_path(self):
        # Add ramp properties to paths in roads layer
        # Steps with ramp:bicycle=yes in Copenhagen
        self.load_fixtures([
            'https://www.openstreetmap.org/way/91275149',
        ])

        self.assert_has_feature(
            15, 17527, 10257, 'roads',
            {'id': 91275149, 'kind': 'path', 'kind_detail': 'steps',
             'is_bicycle_related': True, 'ramp_bicycle': 'yes'})

    def test_ramp_properties_on_footway(self):
        # Footway with ramp=yes in San Francisco
        self.load_fixtures([
            'https://www.openstreetmap.org/way/346088008',
        ])

        self.assert_has_feature(
            16, 10470, 25342, 'roads',
            {'id': 346088008, 'kind': 'path', 'kind_detail': 'footway',
             'ramp': 'yes'})
