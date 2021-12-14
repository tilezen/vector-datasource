from . import FixtureTest


class EarlyStep(FixtureTest):
    def test_steps_with_regional_route(self):
        self.load_fixtures([
            'https://www.openstreetmap.org/way/24655593',
            'https://www.openstreetmap.org/relation/2260059',
        ], clip=self.tile_bbox(12, 653, 1582))

        self.assert_has_feature(
            12, 653, 1582, 'roads',
            {'kind_detail': 'steps'})

    def test_steps_without_route(self):
        self.load_fixtures([
            'https://www.openstreetmap.org/way/38060491',
        ])

        self.assert_has_feature(
            13, 1309, 3166, 'roads',
            {'kind_detail': 'steps'})

    def test_min_zoom(self):
        # way 25292070   highway=steps, no route, but has name (Esmeralda,
        # Bernal, SF)
        self.load_fixtures(['https://www.openstreetmap.org/way/25292070'])

        self.assert_no_matching_feature(
            13, 1310, 3167, 'roads',
            {'kind': 'path', 'kind_detail': 'steps',
             'name': 'Esmeralda Ave.'})

        # we don't assert name feature because name has been dropped in
        # https://github.com/tilezen/vector-datasource/pull/2031
        self.assert_has_feature(
            14, 2620, 6334, 'roads',
            {'kind': 'path', 'kind_detail': 'steps'})
