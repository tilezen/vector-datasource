from . import FixtureTest


class DontMergeZ16Roads(FixtureTest):
    def test_roads_not_merged(self):
        # if we're merging, then only one of these will be in tiles. if
        # both exist then it's more likely that no merging is happening.
        self.load_fixtures(['http://www.openstreetmap.org/way/89912879',
                            'http://www.openstreetmap.org/way/89911760'])

        self.assert_has_feature(
            16, 19829, 24234, "roads",
            {"kind": "major_road", "kind_detail": "trunk", "id": 89912879})

        self.assert_has_feature(
            16, 19829, 24234, "roads",
            {"kind": "major_road", "kind_detail": "trunk", "id": 89911760})
