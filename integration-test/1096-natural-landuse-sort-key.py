# -*- encoding: utf-8 -*-
from . import FixtureTest


class NaturalLanduseSortKeyTest(FixtureTest):

    def _check(self, tags, expected_kind, expected_sort_rank):
        import dsl

        z, x, y = (16, 0, 0)

        full_tags = {
            'source': 'openstreetmap.org'
        }
        full_tags.update(tags)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), full_tags),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 1,
                'kind': expected_kind,
                'sort_rank': expected_sort_rank,
            })

    def test_natural_wood(self):
        self._check({'natural': 'wood'}, 'natural_wood', 34)

    def test_natural_forest(self):
        self._check({'natural': 'forest'}, 'natural_forest', 33)

    def test_natural_park(self):
        self._check({'natural': 'park'}, 'natural_park', 32)

    def test_grass(self):
        self._check({'landuse': 'grass'}, 'grass', 35)

    def test_meadow(self):
        self._check({'landuse': 'meadow'}, 'meadow', 36)

    def test_scrub(self):
        self._check({'natural': 'scrub'}, 'scrub', 37)

    def test_wetland(self):
        self._check({'natural': 'wetland'}, 'wetland', 220)
