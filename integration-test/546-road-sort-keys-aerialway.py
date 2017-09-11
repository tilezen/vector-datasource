from . import FixtureTest


class RoadSortKeysAerialway(FixtureTest):
    def test_gondola(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/32051122'])

        self.assert_has_feature(
            16, 19321, 23740, "roads",
            {"kind": "aerialway", "kind_detail": "gondola", "id": 32051122,
             "sort_rank": 442})

    def test_cable_car(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/384371038'])

        self.assert_has_feature(
            16, 14894, 29232, "roads",
            {"kind": "aerialway", "kind_detail": "cable_car", "id": 384371038,
             "sort_rank": 442})

    def test_chair_lift(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/113791306'])

        self.assert_has_feature(
            16, 10553, 25492, "roads",
            {"kind": "aerialway", "kind_detail": "chair_lift", "id": 113791306,
             "sort_rank": 441})

    def test_rope_tow(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/209129274'])

        self.assert_has_feature(
            16, 10719, 25012, "roads",
            {"kind": "aerialway", "kind_detail": "rope_tow", "id": 209129274,
             "sort_rank": 440})
