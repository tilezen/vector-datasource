from . import FixtureTest


class RoadSortKeysLayers(FixtureTest):
    def test_layer_5(self):
        # layer 5
        self.load_fixtures(['https://www.openstreetmap.org/way/48474682'])

        self.assert_has_feature(
            16, 10654, 25150, "roads",
            {"kind": "highway", "kind_detail": "motorway", "is_bridge": True,
             "id": 48474682, "sort_rank": 447})

    def test_layer_4(self):
        # layer 4
        self.load_fixtures(['https://www.openstreetmap.org/way/8918870'])

        self.assert_has_feature(
            16, 10483, 25340, "roads",
            {"kind": "highway", "kind_detail": "motorway", "is_bridge": True,
             "id": 8918870, "sort_rank": 446})

    def test_layer_3(self):
        # layer 3
        self.load_fixtures(['https://www.openstreetmap.org/way/29394019'])

        self.assert_has_feature(
            16, 10479, 25341, "roads",
            {"kind": "highway", "kind_detail": "motorway_link",
             "is_bridge": True, "id": 29394019, "sort_rank": 445})

    def test_layer_2(self):
        # layer 2
        self.load_fixtures(['https://www.openstreetmap.org/way/27651523'])

        self.assert_has_feature(
            16, 10480, 25365, "roads",
            {"kind": "highway", "kind_detail": "motorway", "is_bridge": True,
             "id": 27651523, "sort_rank": 444})

    def test_layer_1(self):
        # layer 1
        self.load_fixtures(['https://www.openstreetmap.org/way/28412298'])

        self.assert_has_feature(
            16, 10472, 25323, "roads",
            {"kind": "highway", "kind_detail": "motorway", "is_bridge": True,
             "id": 28412298, "sort_rank": 443})

    def test_layer_minus_1(self):
        # layer -1
        self.load_fixtures(['https://www.openstreetmap.org/way/43685501'])

        self.assert_has_feature(
            16, 10472, 25323, "roads",
            {"kind": "minor_road", "kind_detail": "service", "is_tunnel": True,
             "id": 43685501, "sort_rank": 304})

    def test_layer_minus_2(self):
        # layer -2
        self.load_fixtures(['https://www.openstreetmap.org/way/50691047'])

        self.assert_has_feature(
            16, 10491, 25323, "roads",
            {"kind": "highway", "kind_detail": "motorway", "is_tunnel": True,
             "id": 50691047, "sort_rank": 303})
