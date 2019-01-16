from unittest import TestCase


class CollisionRankTest(TestCase):

    def test_simple_assignment(self):
        # ranker should assign us a rank.
        from vectordatasource.collision import CollisionRanker

        ranker = CollisionRanker([
            {'kind': 'foo'},
        ])

        shape = None
        props = {'kind': 'foo'}
        fid = 1
        rank = ranker((shape, props, fid))

        self.assertEqual(rank, 1)

    def test_contiguous_ranks(self):
        # ranker should assign ranks contiguously in order
        from vectordatasource.collision import CollisionRanker

        ranker = CollisionRanker([
            {'kind': 'foo'},
            {'kind': 'bar'},
        ])

        shape = None
        props = {'kind': 'bar'}
        fid = 1
        rank = ranker((shape, props, fid))

        # bar is the second in the list, so we should get 2 in response.
        self.assertEqual(rank, 2)

    def test_complex_filter(self):
        from vectordatasource.collision import CollisionRanker

        ranker = CollisionRanker([
            {'kind': 'foo', 'population': {'min': 1000}},
            {'kind': 'foo'},
        ])

        # check that filter expressions can be used to modify the behaviour.
        for population, expected_rank in [(999, 2), (1000, 1)]:
            shape = None
            props = {'kind': 'foo', 'population': population}
            fid = 1
            rank = ranker((shape, props, fid))

            self.assertEqual(rank, expected_rank)

    def test_reserved_blocks(self):
        # test that if we overflow the reserved block by having too many items
        # in the preceding section, then the code fails with an error.
        from vectordatasource.collision import CollisionRanker

        with self.assertRaises(AssertionError):
            CollisionRanker([
                {'foo': 'bar'},
                {'baz': 'bat'},
                {'_reserved': {'from': 2, 'to': 10}},
            ])

    def test_skips_reserved_blocks(self):
        # test that we skip reserved blocks in the numbering
        from vectordatasource.collision import CollisionRanker

        ranker = CollisionRanker([
            # should be 1
            {'kind': 'foo'},
            # should skip 2-9 as unused
            # should skip 10-20 as reserved
            {'_reserved': {'from': 10, 'to': 20}},
            # should be 21
            {'kind': 'bar'},
        ])

        shape = None
        props = {'kind': 'bar'}
        fid = 1
        rank = ranker((shape, props, fid))

        self.assertEqual(rank, 21)
