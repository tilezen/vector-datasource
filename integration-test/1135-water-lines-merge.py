from . import FixtureTest


class WaterLinesMergeTest(FixtureTest):

    def test_successful_merge(self):
        from ModestMaps.Core import Coordinate
        from shapely.geometry import LineString
        from tilequeue.tile import coord_to_bounds
        import dsl

        z, x, y = 9, 145, 201

        bounds = coord_to_bounds(Coordinate(zoom=z, column=x, row=y))
        mid_x = (bounds[2] - bounds[0]) / 2.0 + bounds[0]
        mid_y = (bounds[3] - bounds[1]) / 2.0 + bounds[1]
        ls1 = LineString([(mid_x-0.01, mid_y-0.01), (mid_x, mid_y)])
        ls2 = LineString([(mid_x, mid_y), (mid_x+0.01, mid_y+0.01)])
        props = dict(waterway=u'river', name=u'foo')
        self.generate_fixtures(
            dsl.way(1, ls1, props),
            dsl.way(2, ls2, props),
        )

        self.assert_n_matching_features(
            z, x, y, 'water', {
                'name': 'foo',
                'kind': 'river',
                'label_placement': type(None),
            }, 1)

        with self.features_in_tile_layer(z, x, y, 'water') as features:
            for f in features:
                if 'label_placement' in f['properties']:
                    continue
                assert f['geometry']['type'] == 'LineString'
                assert len(f['geometry']['coordinates']) == 2

    def test_unsuccessful_merge_same_props(self):
        from ModestMaps.Core import Coordinate
        from shapely.geometry import LineString
        from tilequeue.tile import coord_to_bounds
        import dsl

        z, x, y = 9, 145, 201

        bounds = coord_to_bounds(Coordinate(zoom=z, column=x, row=y))
        mid_x = (bounds[2] - bounds[0]) / 2.0 + bounds[0]
        mid_y = (bounds[3] - bounds[1]) / 2.0 + bounds[1]
        ls1 = LineString([
            (bounds[0]+0.1, bounds[1]+0.1),
            (mid_x-0.1, mid_y-0.1),
        ])
        ls2 = LineString([
            (mid_x+0.1, mid_y+0.1),
            (bounds[2]-0.1, bounds[2]-0.1),
        ])
        props = dict(waterway=u'river', name=u'foo')
        self.generate_fixtures(
            dsl.way(1, ls1, props),
            dsl.way(2, ls2, props),
        )

        self.assert_n_matching_features(
            z, x, y, 'water', {
                'name': 'foo',
                'kind': 'river',
                'label_placement': type(None),
            }, 1)

        with self.features_in_tile_layer(z, x, y, 'water') as features:
            for f in features:
                if 'label_placement' in f['properties']:
                    continue
                assert f['geometry']['type'] == 'MultiLineString'
                multi_coords = f['geometry']['coordinates']
                assert len(multi_coords) == 2
                assert len(multi_coords[0]) == 2
                assert len(multi_coords[1]) == 2

    def test_unsuccessful_merge_diff_props(self):
        from ModestMaps.Core import Coordinate
        from shapely.geometry import LineString
        from tilequeue.tile import coord_to_bounds
        import dsl

        z, x, y = 9, 145, 201

        bounds = coord_to_bounds(Coordinate(zoom=z, column=x, row=y))
        mid_x = (bounds[2] - bounds[0]) / 2.0 + bounds[0]
        mid_y = (bounds[3] - bounds[1]) / 2.0 + bounds[1]
        ls1 = LineString([
            (bounds[0]+0.1, bounds[1]+0.1),
            (mid_x-0.1, mid_y-0.1),
        ])
        ls2 = LineString([
            (mid_x+0.1, mid_y+0.1),
            (bounds[2]-0.1, bounds[2]-0.1),
        ])
        self.generate_fixtures(
            dsl.way(1, ls1, dict(waterway=u'river', name=u'foo')),
            dsl.way(2, ls2, dict(waterway=u'river', name=u'bar')),
        )

        self.assert_n_matching_features(
            z, x, y, 'water', {
                'kind': 'river',
                'label_placement': type(None),
            }, 2)

        with self.features_in_tile_layer(z, x, y, 'water') as features:
            for f in features:
                if 'label_placement' in f['properties']:
                    continue
                assert f['geometry']['type'] == 'LineString'
                assert len(f['geometry']['coordinates']) == 2
