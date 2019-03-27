# -*- encoding: utf-8 -*-
from . import FixtureTest


class AerodromeTest(FixtureTest):

    def _check(self, aerodrome_type, kind_detail):
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'aeroway': 'aerodrome',
                'aerodrome:type': aerodrome_type,
                'name': 'Fake Aerodrome',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'kind': 'aerodrome',
                'kind_detail': kind_detail,
            })
        self.assert_has_feature(
            z, x, y, 'landuse', {
                'kind': 'aerodrome',
                'kind_detail': kind_detail,
            })

    def test_public(self):
        self._check('public', 'public')

    def test_private(self):
        self._check('private', 'private')

    def test_military_public(self):
        self._check('military/public', 'military_public')

    def test_airfield(self):
        self._check('airfield', 'airfield')

    def test_international(self):
        self._check('international', 'international')

    def test_regional(self):
        self._check('regional', 'regional')

    def test_gliding(self):
        self._check('gliding', 'gliding')

    def test_unknown(self):
        self._check('unknown', type(None))

    def test_military(self):
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'aeroway': 'aerodrome',
                'aerodrome:type': 'military',
                'name': 'Fake Aerodrome',
                'source': 'openstreetmap.org',
            }),
        )

        # note: kind=airfield means a _military_ airfield
        self.assert_has_feature(
            z, x, y, 'pois', {
                'kind': 'airfield',
            })
