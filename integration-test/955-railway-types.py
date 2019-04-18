# -*- encoding: utf-8 -*-
from . import FixtureTest


class RailwayTest(FixtureTest):

    def test_razed_rail(self):
        import dsl

        z, x, y = (16, 34905, 23736)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/521306179
            dsl.way(521306179, dsl.tile_diagonal(z, x, y), {
                'historic': 'railway',
                'name': 'Ferrovia Massalombarda-Imola-Fontanelice',
                'railway': 'razed',
                'source': 'openstreetmap.org',
            }),
        )

        # should _not_ include razed rails
        self.assert_no_matching_feature(
            z, x, y, 'roads', {
                'id': 521306179,
            })

    def test_abandoned_rail(self):
        import dsl

        z, x, y = (16, 34900, 23738)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/521306174
            dsl.way(521306174, dsl.tile_diagonal(z, x, y), {
                'railway': 'abandoned',
                'service': 'yard',
                'source': 'openstreetmap.org',
            }),
        )

        # should _not_ include abandoned rails
        self.assert_no_matching_feature(
            z, x, y, 'roads', {
                'id': 521306174,
            })

    def test_disused_rail(self):
        import dsl

        z, x, y = (16, 10503, 25309)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/610527680
            dsl.way(610527680, dsl.tile_diagonal(z, x, y), {
                'disused:railway': 'rail',
                'railway': 'disused',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 610527680,
                'kind': u'rail',
                'kind_detail': u'disused',
            })

    def test_rail_rail(self):
        import dsl

        z, x, y = (16, 10504, 25313)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/77517466
            dsl.way(77517466, dsl.tile_diagonal(z, x, y), {
                'electrified': 'no',
                'gauge': '1435',
                'maxspeed': '79 mph',
                'maxspeed:freight': '70 mph',
                'name': 'Martinez Subdivision MT1',
                'owner': 'Union Pacific Railroad',
                'passenger_lines': '2',
                'railway': 'rail',
                'railway:track_ref': '1',
                'source': 'openstreetmap.org',
                'usage': 'main',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 77517466,
                'kind': u'rail',
                'kind_detail': u'rail',
            })

    def _check(self, osm_tag, expected_kind_detail):
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'railway': osm_tag,
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 1,
                'kind': 'rail',
                'kind_detail': expected_kind_detail,
            })

    def test_subway(self):
        self._check('subway', 'subway')

    def test_preserved(self):
        self._check('preserved', 'preserved')

    def test_narrow_gauge(self):
        self._check('narrow_gauge', 'narrow_gauge')

    def test_disused(self):
        self._check('disused', 'disused')

    def test_funicular(self):
        self._check('funicular', 'funicular')

    def test_monorail(self):
        self._check('monorail', 'monorail')

    def test_miniature(self):
        self._check('miniature', 'miniature')

    def test_light_rail(self):
        self._check('light_rail', 'light_rail')

    def test_tram(self):
        self._check('tram', 'tram')
