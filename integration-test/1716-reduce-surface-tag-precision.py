# -*- encoding: utf-8 -*-
from . import FixtureTest


class ResidentialTest(FixtureTest):

    def test_z16(self):
        self._check(zoom=16, expect_surface='fine_gravel')

    def test_z15(self):
        self._check(zoom=15, expect_surface='fine_gravel')

    def test_z14(self):
        self._check(zoom=14, expect_surface='unpaved')

    def test_z13(self):
        self._check(zoom=13, expect_surface='unpaved')

    def test_z12(self):
        self._check(zoom=12, expect_surface='unpaved')

    def setUp(self):
        FixtureTest.setUp(self)

        import dsl

        z, x, y = (16, 0, 0)

        full_tags = {
            'source': 'openstreetmap.org',
            'highway': 'residential',
            'surface': 'fine_gravel',
        }

        self.generate_fixtures(
            dsl.way(1, dsl.tile_diagonal(z, x, y), full_tags),
        )

    def _check(self, zoom=16, expect_surface=None):
        self.assert_has_feature(
            zoom, 0, 0, 'roads', {
                'id': 1,
                'surface': expect_surface,
            })


class HighwayTest(FixtureTest):

    def test_z16(self):
        self._check(zoom=16, expect_surface='asphalt')

    def test_z15(self):
        self._check(zoom=15, expect_surface='asphalt')

    def test_z14(self):
        self._check(zoom=14, expect_surface='asphalt')

    def test_z13(self):
        self._check(zoom=13, expect_surface='asphalt')

    def test_z12(self):
        self._check(zoom=12, expect_surface='asphalt')

    def test_z11(self):
        self._check(zoom=11, expect_surface='asphalt')

    def test_z10(self):
        self._check(zoom=10, expect_surface='paved')

    def test_z09(self):
        self._check(zoom=9, expect_surface='paved')

    def test_z08(self):
        self._check(zoom=8, expect_surface='paved')

    def setUp(self):
        FixtureTest.setUp(self)

        import dsl

        z, x, y = (16, 0, 0)

        full_tags = {
            'source': 'openstreetmap.org',
            'highway': 'motorway',
            'surface': 'asphalt',
        }

        self.generate_fixtures(
            dsl.way(1, dsl.tile_diagonal(z, x, y), full_tags),
        )

    def _check(self, zoom=16, expect_surface=None):
        self.assert_has_feature(
            zoom, 0, 0, 'roads', {
                'id': 1,
                'surface': expect_surface,
            })
