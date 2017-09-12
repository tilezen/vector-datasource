from . import FixtureTest


class DefaultBrunnelSortKeys(FixtureTest):
    def test_footway(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/70656344'])

        self.assert_has_feature(
            16, 10475, 25325, "roads",
            {"kind": "path", "kind_detail": "footway", "id": 70656344,
             "sort_rank": 404})

    def test_path(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/275618623'])

        self.assert_has_feature(
            16, 10479, 25348, "roads",
            {"kind": "path", "kind_detail": "path", "id": 275618623,
             "sort_rank": 404})

    def test_cycleway(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/8915047'])

        self.assert_has_feature(
            16, 10469, 25345, "roads",
            {"kind": "path", "kind_detail": "cycleway", "id": 8915047,
             "sort_rank": 404})

    def test_steps(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/109938341'])

        self.assert_has_feature(
            16, 11301, 26220, "roads",
            {"kind": "path", "kind_detail": "steps", "id": 109938341,
             "sort_rank": 404})

    def test_track(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/66418490'])

        self.assert_has_feature(
            16, 11378, 26224, "roads",
            {"kind": "path", "kind_detail": "track", "id": 66418490,
             "sort_rank": 404})

    def test_footway_tunnel(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/97639585'])

        self.assert_has_feature(
            16, 10468, 25332, "roads",
            {"kind": "path", "kind_detail": "footway", "id": 97639585,
             "sort_rank": 304})

    def test_path_tunnel(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/356449810'])

        self.assert_has_feature(
            16, 10473, 25331, "roads",
            {"kind": "path", "kind_detail": "path", "id": 356449810,
             "sort_rank": 304})

    def test_track_tunnel(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/338682183'])

        self.assert_has_feature(
            16, 10470, 25342, "roads",
            {"kind": "path", "kind_detail": "track", "id": 338682183,
             "sort_rank": 304})

    def test_steps_tunnel(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/99231479'])

        self.assert_has_feature(
            16, 10487, 25328, "roads",
            {"kind": "path", "kind_detail": "steps", "id": 99231479,
             "sort_rank": 304})
