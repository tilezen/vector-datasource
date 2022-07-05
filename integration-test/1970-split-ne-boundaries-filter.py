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
                'min_zoom': 5,  # min_zoom is set to 5 in the source data
                'scalerank': 5,
                'source': 'naturalearthdata.com',
            }),
        )
        for zoom in range(1, 17):
            self.assert_has_feature(
                zoom, x, y, 'boundaries', {
                    'kind': 'disputed_claim',
                    'kind:cn': 'country',
                    'min_zoom': 1,  # we change the min_zoom override in boundaries.yaml to 1 so we assert here
                })
