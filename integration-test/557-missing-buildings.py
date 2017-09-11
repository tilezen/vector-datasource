from . import OsmFixtureTest


class MissingBuildings(OsmFixtureTest):
    def test_best_tile(self):
        # Best Tile
        self.load_fixtures(['https://www.openstreetmap.org/way/103383621'])

        self.assert_has_feature(
            16, 10484, 25339, 'buildings',
            {'id': 103383621})

    def test_miraloma_school(self):
        # Miraloma School
        self.load_fixtures(['https://www.openstreetmap.org/way/338881092'])

        self.assert_has_feature(
            16, 10476, 25339, 'buildings',
            {'id': 338881092})

    def test_small_building(self):
        # Tiny individual building (way_area = 5.4 sq.m.)
        self.load_fixtures(['https://www.openstreetmap.org/way/278410540'])

        self.assert_has_feature(
            16, 10474, 25343, 'buildings',
            {'id': 278410540, 'min_zoom': 17})
