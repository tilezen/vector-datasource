from . import OsmFixtureTest


class RoadSortKeysRailways(OsmFixtureTest):
    def test_rail(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/8920472'])

        self.assert_has_feature(
            16, 10487, 25333, "roads",
            {"kind": "rail", "kind_detail": "rail", "id": 8920472,
             "sort_rank": 382})

    def test_tram(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/95623728'])

        self.assert_has_feature(
            16, 10486, 25326, "roads",
            {"kind": "rail", "kind_detail": "tram", "id": 95623728,
             "sort_rank": 382})

    def test_light_rail(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/160279679'])

        self.assert_has_feature(
            16, 10478, 25341, "roads",
            {"kind": "rail", "kind_detail": "light_rail", "id": 160279679,
             "sort_rank": 382})

    def test_narrow_gauge(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/105574666'])

        self.assert_has_feature(
            16, 19216, 24778, "roads",
            {"kind": "rail", "kind_detail": "narrow_gauge", "id": 105574666,
             "sort_rank": 382})

    def test_monorail(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/296530703'])

        self.assert_has_feature(
            16, 17714, 24454, "roads",
            {"kind": "rail", "kind_detail": "monorail", "id": 296530703,
             "sort_rank": 382})

    def test_spur(self):
        # spurs, sidings, etc...
        self.load_fixtures(['https://www.openstreetmap.org/way/135403703'])

        self.assert_has_feature(
            16, 13353, 25941, "roads",
            {"kind": "rail", "kind_detail": "rail", "service": "spur",
             "id": 135403703, "sort_rank": 361})

    def test_siding(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/148018328'])

        self.assert_has_feature(
            16, 10485, 25331, "roads",
            {"kind": "rail", "kind_detail": "rail", "service": "siding",
             "id": 148018328, "sort_rank": 361})

    def test_yard(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/119709585'])

        self.assert_has_feature(
            16, 10485, 25331, "roads",
            {"kind": "rail", "kind_detail": "rail", "service": "yard",
             "id": 119709585, "sort_rank": 359})

    def test_crossover(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/119695339'])

        self.assert_has_feature(
            16, 10485, 25347, "roads",
            {"kind": "rail", "kind_detail": "rail", "service": "crossover",
             "id": 119695339, "sort_rank": 357})
