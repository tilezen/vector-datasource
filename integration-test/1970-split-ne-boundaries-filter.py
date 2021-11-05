# -*- encoding: utf-8 -*-
from . import FixtureTest


class NaturalEarth(FixtureTest):
    def test_claim_boundary(self):
        import dsl

        z, x, y = 1, 0, 0

        self.generate_fixtures(
            dsl.way(1, dsl.tile_diagonal_dexter(z, x, y), {
                'featurecla': 'Claim boundary',
                'fclass_cn': 'International boundary (verify)',
                'min_zoom': 5,
                'scalerank': 5,
                'source': 'naturalearthdata.com',
            }),
        )
        for zoom in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
            self.assert_has_feature(
                zoom, x, y, 'boundaries', {
                    'kind': 'disputed_claim',
                    'kind:cn': 'country',
                    'min_zoom': 1,  # we change the min_zoom in boundaries.yaml to 1 so we assert here  # noqa
                })
