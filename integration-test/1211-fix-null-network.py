from . import FixtureTest


class FixNullNetwork(FixtureTest):
    def test_routes_with_no_network(self):
        import dsl
        # ref="N 4", route=road, but no network=*
        # so we should get something that has no network, but a shield text of
        # 'N4' (see #1062 regarding why it's 'N4' rather than '4').

        self.generate_fixtures(
            dsl.way(69415104, dsl.tile_diagonal(11, 1038, 705), {
                'source': 'openstreetmap.org',
                'highway': 'primary',
                'lanes': '3',
                'maxspeed': '50',
                'name': 'Avenue Roger Salengro',
                'old_ref': 'N 4',
                'ref': 'D 4',
                'source:maxspeed': 'FR:urban',
                'surface': 'asphalt'
            }),
            dsl.relation(2307408, {
                'source': 'openstreetmap.org',
                'ref': 'N 4',
                'route': 'road',
                'type': 'route'
            }, ways=[69415104]),
        )

        self.assert_has_feature(
            11, 1038, 705, 'roads',
            {'kind': 'major_road', 'shield_text': 'N4', 'network': type(None)})
