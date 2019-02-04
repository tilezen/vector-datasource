# -*- encoding: utf-8 -*-
from . import FixtureTest


class AerodromeSortTest(FixtureTest):

    def test_sort_order(self):
        import dsl

        z, x, y = (16, 0, 0)

        poly = dsl.tile_box(z, x, y)
        line = dsl.tile_diagonal(z, x, y)

        def _src(props):
            p = {'source': 'openstreetmap.org'}
            p.update(props)
            return p

        self.generate_fixtures(
            dsl.way(1, poly, _src({'aeroway': 'aerodrome'})),
            dsl.way(2, poly, _src({'aeroway': 'runway'})),
            dsl.way(3, poly, _src({'aeroway': 'taxiway'})),
            dsl.way(4, poly, _src({'aeroway': 'apron'})),
            dsl.way(5, line, _src({'aeroway': 'runway'})),
            dsl.way(6, line, _src({'aeroway': 'taxiway'})),
        )

        landuse_kinds = {}
        with self.features_in_tile_layer(z, x, y, 'landuse') as features:
            for feature in features:
                kind = feature['properties']['kind']
                sort_rank = feature['properties']['sort_rank']
                assert kind not in landuse_kinds
                landuse_kinds[kind] = sort_rank

        self.assertTrue(landuse_kinds['aerodrome'] < landuse_kinds['runway'])
        self.assertTrue(landuse_kinds['aerodrome'] < landuse_kinds['taxiway'])
        self.assertTrue(landuse_kinds['aerodrome'] < landuse_kinds['apron'])

        roads_kinds = {}
        with self.features_in_tile_layer(z, x, y, 'roads') as features:
            for feature in features:
                kind_detail = feature['properties']['kind_detail']
                sort_rank = feature['properties']['sort_rank']
                assert kind_detail not in roads_kinds
                roads_kinds[kind_detail] = sort_rank

        self.assertTrue(landuse_kinds['aerodrome'] < roads_kinds['runway'])
        self.assertTrue(landuse_kinds['aerodrome'] < roads_kinds['taxiway'])
