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

        # dealing with the --download-only mode of the tests. because it
        # yields [] into the features_in_tile_layer call, we end up with
        # no landuse_kinds entries. we don't want that to be OK in the
        # regular test mode, so we can assert the landuse kinds is truthy
        # (which will short-circuit in --download-only mode) and then use
        # an if to guard the actual tests. this is super-ugly and should
        # go away when we don't need --download-only any more: when we've
        # converted all the tests to generative.
        self.assertTrue(landuse_kinds)
        if landuse_kinds:
            aerodrome_rank = landuse_kinds['aerodrome']
            self.assertTrue(aerodrome_rank < landuse_kinds['runway'])
            self.assertTrue(aerodrome_rank < landuse_kinds['taxiway'])
            self.assertTrue(aerodrome_rank < landuse_kinds['apron'])

        roads_kinds = {}
        with self.features_in_tile_layer(z, x, y, 'roads') as features:
            for feature in features:
                kind_detail = feature['properties']['kind_detail']
                sort_rank = feature['properties']['sort_rank']
                assert kind_detail not in roads_kinds
                roads_kinds[kind_detail] = sort_rank

        self.assertTrue(roads_kinds)
        if roads_kinds:
            aerodrome_rank = landuse_kinds['aerodrome']
            self.assertTrue(aerodrome_rank < roads_kinds['runway'])
            self.assertTrue(aerodrome_rank < roads_kinds['taxiway'])

            # however, we also want the roads to be _under_ the landuse
            # polygons for the same type, due to the styling adding a
            # casing which looks weird.
            self.assertLess(roads_kinds['runway'], landuse_kinds['runway'])
            self.assertLess(roads_kinds['taxiway'], landuse_kinds['taxiway'])


class AerowayAreaTest(FixtureTest):

    def _check(self, tags, kind):
        import dsl

        z, x, y = 16, 0, 0
        tags['source'] = 'openstreetmap.org'
        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), tags),
        )
        self.assert_has_feature(
            z, x, y, 'landuse', {
                'kind': kind,
            })

    def test_taxiway(self):
        self._check({'area:aeroway': 'taxiway'}, 'taxiway')

    def test_runway(self):
        self._check({'area:aeroway': 'runway'}, 'runway')

    def test_apron(self):
        self._check({'area:aeroway': 'apron'}, 'apron')
