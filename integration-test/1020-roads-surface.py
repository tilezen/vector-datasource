from . import FixtureTest


class RoadsSurface(FixtureTest):

    def test_road_surface(self):
        # Add surface properties to roads layer (at max zooms)
        # Prince St with cobblestones in Alexandria, VA
        # https://www.openstreetmap.org/way/190536019
        self.load_fixtures([
            'https://www.openstreetmap.org/way/190536019',
        ])

        self.assert_has_feature(
            15, 9371, 12546, 'roads',
            {'id': 190536019, 'kind': 'minor_road',
             'surface': 'cobblestone'})
