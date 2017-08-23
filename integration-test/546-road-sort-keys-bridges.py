from . import OsmFixtureTest


class RoadSortKeysBridges(OsmFixtureTest):
    def test_motorway_bridge(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/28412298'])

        self.assert_has_feature(
            16, 10472, 25323, "roads",
            {"kind": "highway", "kind_detail": "motorway", "id": 28412298,
             "name": "Presidio Pkwy.", "is_bridge": True, "sort_rank": 443})

    def test_trunk_bridge(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/59801274'])

        self.assert_has_feature(
            16, 10471, 25331, "roads",
            {"kind": "major_road", "kind_detail": "trunk", "id": 59801274,
             "name": "Crossover Dr.", "is_bridge": True, "sort_rank": 443})

    def test_primary_bridge(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/399640204'])

        self.assert_has_feature(
            16, 11265, 26221, "roads",
            {"kind": "major_road", "kind_detail": "primary", "id": 399640204,
             "name": "North Los Coyotes Diagonal", "is_bridge": True, "sort_rank": 430})

    def test_secondary_bridge(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/27613581'])

        self.assert_has_feature(
            16, 10486, 25339, "roads",
            {"kind": "major_road", "kind_detail": "secondary", "id": 27613581,
             "name": "Oakdale Ave.", "is_bridge": True, "sort_rank": 429})

    def test_teriary_bridge(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/242940297'])

        self.assert_has_feature(
            16, 10486, 25327, "roads",
            {"kind": "major_road", "kind_detail": "tertiary", "id": 242940297,
             "name": "Beale St.", "is_bridge": True, "sort_rank": 427})

    def test_residential_bridge(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/162038104'])

        self.assert_has_feature(
            16, 10738, 24989, "roads",
            {"kind": "minor_road", "kind_detail": "residential", "id": 162038104,
             "name": "Woodwardia Pl.", "sort_rank": 410})

    def test_service_bridge(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/232303398'])

        self.assert_has_feature(
            16, 10482, 25363, "roads",
            {"id": 232303398, "kind": "minor_road", "kind_detail": "service",
             "is_bridge": True, "sort_rank": 408})
