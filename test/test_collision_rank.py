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

    def test_transform_adds_layer(self):
        """
        Tests that the "$layer" pseudo-property is being injected by the
        add_collision_rank post-processor. We use the $-prefix so that it
        doesn't clash with the "layer" property, which represents something
        close to z-order for features.
        """

        from ModestMaps.Core import Coordinate
        from shapely.geometry import Point
        from tilequeue.process import Context
        from tilequeue.tile import coord_to_bounds
        from tilequeue.tile import num2deg
        from vectordatasource.collision import CollisionRanker
        from vectordatasource.transform import add_collision_rank

        z, x, y = (16, 0, 0)

        ranker = CollisionRanker([
            {"$layer": "foo"},
        ])

        shape = Point(*num2deg(x + 0.5, y + 0.5, z))
        feature_layers = [
            dict(
                layer_datum=dict(name='foo'),
                features=[
                    (shape, {}, 1),
                ],
            ),
        ]
        nominal_zoom = z
        padded_bounds = coord_to_bounds(Coordinate(zoom=z, column=x, row=y))
        params = {}
        resources = {'ranker': ranker}

        ctx = Context(
            feature_layers,
            nominal_zoom,
            padded_bounds,
            params,
            resources,
            log=None,
        )

        # NOTE: modifies layers in-place, doesn't return anything
        add_collision_rank(ctx)

        # we should have assigned the collision rank because of the
        # $layer match
        _, props, _ = feature_layers[0]['features'][0]
        self.assertEqual(props.get('collision_rank'), 1)

    def test_reserved_count(self):
        """
        Test that we can reserve a specific number of collision rank indices
        without needing to specify the exact start/end.
        """
        from vectordatasource.collision import CollisionRanker

        ranker = CollisionRanker([
            # should be 1
            {'kind': 'foo'},
            # should skip 2-10 (count 9) as reserved
            {'_reserved': {'count': 9}},
            # should be 11
            {'kind': 'bar'},
        ])

        shape = None
        props = {'kind': 'bar'}
        fid = 1
        rank = ranker((shape, props, fid))

        self.assertEqual(rank, 11)
