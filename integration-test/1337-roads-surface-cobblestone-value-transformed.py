from . import FixtureTest


class RoadsSurfaceCobblestoneValueTransformed(FixtureTest):
    def test_transform(self):
        # transform cobblestone:flattened to cobblestone_flattened
        # Illicha Avenue in Donetsk, Ukraine
        self.load_fixtures(['http://www.openstreetmap.org/way/239860289'])

        self.assert_has_feature(
            16, 39650, 22780, 'roads',
            {'id': 239860289, 'name:en': 'Illicha Avenue',
             'kind': 'major_road', 'surface': 'cobblestone_flattened'})
