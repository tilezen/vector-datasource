from . import OsmFixtureTest


class RoadSortKeysRoads(OsmFixtureTest):
    def test_motorway(self):
        # regular roads
        self.load_fixtures(['https://www.openstreetmap.org/way/26765956'])

        self.assert_has_feature(
            16, 10472, 25323, "roads",
            {"kind": "highway", "kind_detail": "motorway", "id": 26765956,
             "name": "Presidio Pkwy.", "sort_rank": 383})

    def test_trunk(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/89802409'])

        self.assert_has_feature(
            16, 10471, 25337, "roads",
            {"kind": "major_road", "kind_detail": "trunk", "id": 89802409,
             "name": "19th Ave.", "sort_rank": 381})

    def test_primary(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/160842753'])

        self.assert_has_feature(
            16, 10488, 25336, "roads",
            {"kind": "major_road", "kind_detail": "primary", "id": 160842753,
             "name": "3rd St.", "sort_rank": 380})

    def test_secondary(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/25337673'])

        self.assert_has_feature(
            16, 10482, 25332, "roads",
            {"kind": "major_road", "kind_detail": "secondary", "id": 25337673,
             "name": "Mission St.", "sort_rank": 379})

    def test_tertiary(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/255330035'])

        self.assert_has_feature(
            16, 10485, 25324, "roads",
            {"kind": "major_road", "kind_detail": "tertiary", "id": 255330035,
             "name": "Battery St.", "sort_rank": 377})

    def test_motorway_link(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/8923765'])

        self.assert_has_feature(
            16, 10472, 25347, "roads",
            {"kind": "highway", "kind_detail": "motorway_link", "id": 8923765,
             "is_link": True, "sort_rank": 374})

    def test_residential(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/8919312'])

        self.assert_has_feature(
            16, 10485, 25344, "roads",
            {"kind": "minor_road", "kind_detail": "residential", "id": 8919312,
             "name": "Racine Ln.", "sort_rank": 360})

    def test_service(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/59161514'])

        self.assert_has_feature(
            16, 10477, 25323, "roads",
            {"kind": "minor_road", "kind_detail": "service", "id": 59161514,
             "name": "Yacht Rd.", "sort_rank": 358})

    def test_parking_aisle(self):
        # service roads
        self.load_fixtures(['https://www.openstreetmap.org/way/147002738'])

        self.assert_has_feature(
            16, 10471, 25341, "roads",
            {"kind": "minor_road", "kind_detail": "service",
             "service": "parking_aisle", "id": 147002738, "sort_rank": 356})

    def test_driveway(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/242769687'])

        self.assert_has_feature(
            16, 10487, 25329, "roads",
            {"kind": "minor_road", "kind_detail": "service",
             "service": "driveway", "id": 242769687, "sort_rank": 356})
