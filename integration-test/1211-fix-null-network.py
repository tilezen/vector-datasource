from . import FixtureTest


class FixNullNetwork(FixtureTest):
    def test_routes_with_no_network(self):
        # ref="N 4", route=road, but no network=*
        # so we should get something that has no network, but a shield text of
        # 'N4' (see #1062 regarding why it's 'N4' rather than '4').
        self.load_fixtures(
            ['http://www.openstreetmap.org/relation/2307408'],
            clip=self.tile_bbox(11, 1038, 705))

        self.assert_has_feature(
            11, 1038, 705, 'roads',
            {'kind': 'major_road', 'shield_text': 'N4', 'network': type(None)})
