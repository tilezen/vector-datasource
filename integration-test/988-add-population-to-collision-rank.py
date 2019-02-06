# -*- encoding: utf-8 -*-
from . import FixtureTest


class PopulationRankTest(FixtureTest):

    def _check_rank(self, population, rank):
        import dsl

        z, x, y = 16, 0, 0

        self.generate_fixtures(
            dsl.way(1, dsl.tile_centre_shape(z, x, y), {
                'place': 'city',
                'population': str(population),
                'name': 'Fooville',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'places', {
                'population': population,
                'population_rank': rank,
            })

    def test_18(self):
        self._check_rank(1000000000, 18)

    def test_17(self):
        self._check_rank(100000000, 17)

    def test_16(self):
        self._check_rank(50000000, 16)

    def test_15(self):
        self._check_rank(20000000, 15)

    def test_14(self):
        self._check_rank(10000000, 14)

    def test_13(self):
        self._check_rank(5000000, 13)

    def test_12(self):
        self._check_rank(1000000, 12)

    def test_11(self):
        self._check_rank(500000, 11)

    def test_10(self):
        self._check_rank(200000, 10)

    def test_9(self):
        self._check_rank(100000, 9)

    def test_8(self):
        self._check_rank(50000, 8)

    def test_7(self):
        self._check_rank(20000, 7)

    def test_6(self):
        self._check_rank(10000, 6)

    def test_5(self):
        self._check_rank(5000, 5)

    def test_4(self):
        self._check_rank(2000, 4)

    def test_3(self):
        self._check_rank(1000, 3)

    def test_2(self):
        self._check_rank(200, 2)

    def test_1(self):
        self._check_rank(100, 1)

    def test_0(self):
        import dsl

        z, x, y = 16, 0, 0

        self.generate_fixtures(
            dsl.way(1, dsl.tile_centre_shape(z, x, y), {
                'place': 'city',
                # missing population
                'name': 'Fooville',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'places', {
                'population': type(None),
                'population_rank': 0,
            })

    def _rank_for_pop(self, population):
        import dsl

        z, x, y = 16, 0, 0

        self.generate_fixtures(
            dsl.way(1, dsl.tile_centre_shape(z, x, y), {
                'place': 'city',
                'population': population,
                'name': 'Fooville',
                'source': 'openstreetmap.org',
            }),
        )

        with self.features_in_tile_layer(z, x, y, 'places') as features:
            self.assertEqual(len(features), 1)
            return features[0]['properties'].get('collision_rank')

    def test_collision_rank_decreasing(self):
        last = self._rank_for_pop(None)
        self.assertGreater(last, 0)

        for exp in xrange(30):
            population = 1 << exp
            rank = self._rank_for_pop(population)
            self.assertLessEqual(rank, last)
            last = rank
