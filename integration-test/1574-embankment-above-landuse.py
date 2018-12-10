# -*- encoding: utf-8 -*-
from . import FixtureTest


class EmbankmentAboveLanduseTest(FixtureTest):

    def test_embankment_above_landuse(self):
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'man_made': 'embankment',
                'source': 'openstreetmap.org',
            }),
            dsl.way(2, dsl.tile_box(z, x, y), {
                'natural': 'wetland',
                'wetland': 'bog',
                'source': 'openstreetmap.org',
            }),
        )

        # set here for convenience, in case we change them later. the exact
        # values aren't as important as the wetland one being more than the
        # water one.
        wetland_rank = 220
        embankment_rank = 278

        self.assertTrue(embankment_rank > wetland_rank)
        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 1,
                'kind': 'embankment',
                'sort_rank': embankment_rank,
            })
        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 2,
                'kind': 'wetland',
                'sort_rank': wetland_rank,
            })
