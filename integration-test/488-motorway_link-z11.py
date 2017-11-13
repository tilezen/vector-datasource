from . import FixtureTest


class MotorwayLinkZ11(FixtureTest):
    def test_motorway_link_until_zoom_11(self):
        z, x, y = 11, 327, 791

        self.load_fixtures(['https://www.openstreetmap.org/way/8915478'])

        self.assert_has_feature(
            z, x, y, 'roads',
            {'kind': 'highway',
             'is_link': True,
             'kind_detail': 'motorway_link'})

        self.assert_no_matching_feature(
            z - 1, x / 2, y / 2, 'roads',
            {'kind': 'highway',
             'is_link': True,
             'kind_detail': 'motorway_link'})
