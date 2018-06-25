# -*- encoding: utf-8 -*-
from . import FixtureTest


class ArgentinaShieldTest(FixtureTest):
    def test_ruta_nacional_shield_text(self):
        import dsl

        # Argentina roads are generally prefixed with 2 characters and then
        # a third [A-Z] character can prefix the number part of the ref,
        # and should be included in the generated shield_text

        # we could just use a coordinate like 16/0/0, but we might later
        # start adding processing based on what country a road is in, so it
        # probably makes sense to use a tile actually in Argentina.
        z, x, y = 16, 22114, 39520

        self.generate_fixtures(
            dsl.is_in('AR', z, x, y),
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'highway': 'motorway',
                'ref': 'RNA002',
                'source': 'openstreetmap.org',
            }),
            dsl.relation(
                1, {
                    'network': 'AR:national',
                    'route': 'road',
                    'ref': 'RNA002',
                    'type': 'route',
                },
                ways=[1],
            ),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 1, 'kind': 'highway', 'network': 'AR:national',
             'ref': 'RNA002', 'shield_text': 'A002'})

    def test_ruta_provincial_shield_text(self):
        import dsl

        # Argentina provincial routes often aren't in relations with proper
        # network value (expected to be AR:provincial), but they do have a
        # RP prefix in he ref.

        # we could just use a coordinate like 16/0/0, but we might later
        # start adding processing based on what country a road is in, so it
        # probably makes sense to use a tile actually in Argentina.
        z, x, y = 16, 22114, 39520

        self.generate_fixtures(
            dsl.is_in('AR', z, x, y),
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'highway': 'primary',
                'ref': 'RP21',
                'source': 'openstreetmap.org',
            }),
            dsl.relation(
                1, {
                    'network': 'AR:provincial',
                    'route': 'road',
                    'ref': 'RP21',
                    'type': 'route',
                },
                ways=[1],
            ),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 1, 'kind': 'major_road', 'network': 'AR:provincial',
             'ref': 'RP21', 'shield_text': '21'})

    # same as the test above, but using the country backfill rather than
    # the relation.
    def test_ruta_provincial_backfill(self):
        import dsl

        z, x, y = 16, 22114, 39520

        self.generate_fixtures(
            dsl.is_in('AR', z, x, y),
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'highway': 'primary',
                'ref': 'RP21',
                'source': 'openstreetmap.org',
            }),
        )

        # note that the logic for backfilling currently pops the 'ref' off,
        # so that's slightly different from when it's present on both the
        # road _and_ the relation.
        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 1, 'kind': 'major_road', 'network': 'AR:provincial',
             'shield_text': '21'})
