from . import FixtureTest


class WaterBoundarySortKey(FixtureTest):
    def test_water_boundary_sort_key(self):
        # from https://github.com/mapzen/vector-datasource/issues/552
        self.load_fixtures([
            'file://integration-test/fixtures/'
            'water_polygons/552-water-boundary-sort-key.shp',
        ])

        self.assert_has_feature(
            16, 10487, 25327, "water",
            {"kind": "ocean", "boundary": True, "sort_rank": 205})
