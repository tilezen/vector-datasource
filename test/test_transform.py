# -*- coding: utf-8 -*-
import unittest
from collections import OrderedDict


class BuildingsClassTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(BuildingsClassTest, self).__init__(*args, **kwargs)

        from vectordatasource.transform import CSVMatcher
        import os.path
        buildings_path = os.path.join(
            os.path.dirname(__file__), '..', 'spreadsheets', 'scale_rank',
            'buildings.csv')
        with open(buildings_path) as fh:
            self.matcher = CSVMatcher(fh)

    def _call_fut(self, props):
        z = -1
        shape = None
        match_result = self.matcher(shape, props, z)
        if match_result is None:
            return None
        k, v = match_result
        return float(v)

    def test_area_most_important(self):
        props = dict(area=1000000)
        result = self._call_fut(props)
        self.assertEquals(result, 1.0)

    def test_height_importance(self):
        props = dict(height=20000)
        result = self._call_fut(props)
        self.assertEquals(result, 1.0)

    def test_volume_importance(self):
        props = dict(volume=1000000)
        result = self._call_fut(props)
        self.assertEquals(result, 1.0)

    def test_area_not_important(self):
        props = dict(area=1)
        result = self._call_fut(props)
        self.assertEquals(result, 5)

    def test_address_not_important(self):
        props = {}
        result = self._call_fut(props)
        self.assertIsNone(result)


class L10nOsmTransformTest(unittest.TestCase):

    def _call_fut(self, x):
        from vectordatasource.transform import _convert_osm_l10n_name
        result = _convert_osm_l10n_name(x)
        if result:
            result = result.code
        return result

    def test_osm_convert_2_3(self):
        eng = self._call_fut('en')
        self.assertEquals(eng, 'en')

    def test_osm_convert_3(self):
        eng = self._call_fut('eng')
        self.assertEquals(eng, 'en')

    def test_osm_convert_not_found(self):
        invalid = self._call_fut('foo')
        self.assertIsNone(invalid)

    def test_osm_convert_country(self):
        eng_gb = self._call_fut('en_GB')
        self.assertEquals(eng_gb, 'en_GB')

    def test_osm_convert_country_invalid(self):
        no_country = self._call_fut('en_foo')
        self.assertEquals(no_country, 'en')

    def test_osm_convert_lookup(self):
        zh_min_nan = self._call_fut('zh-min-nan')
        self.assertEquals(zh_min_nan, 'zh-min-nan')
        zh_min_nan = self._call_fut('zh-yue')
        self.assertEquals(zh_min_nan, 'zh-yue')


class L10nWofTransformTest(unittest.TestCase):

    def _call_fut(self, x):
        from vectordatasource.transform import _convert_wof_l10n_name
        result = _convert_wof_l10n_name(x)
        if result:
            result = result.code
        return result

    def test_osm_convert_valid(self):
        eng = self._call_fut('eng_x')
        self.assertEquals(eng, 'en')

    def test_osm_convert_invalid(self):
        invalid = self._call_fut('zzz_x')
        self.assertIsNone(invalid)


class TagsNameI18nTest(unittest.TestCase):

    def _call_fut(self, source, name_key, name_val):
        from vectordatasource.transform import tags_name_i18n
        shape = fid = zoom = None
        name = 'name:%s' % name_key
        tags = {
            name: name_val,
        }
        props = dict(
            source=source,
            tags=tags,
            name='unused',
        )
        result = tags_name_i18n(shape, props, fid, zoom)
        return result

    def test_osm_source(self):
        shape, props, fid = self._call_fut('openstreetmap.org', 'en', 'foo')
        self.assertTrue('name:en' in props)
        self.assertEquals('foo', props['name:en'])

    def test_wof_source(self):
        shape, props, fid = self._call_fut('whosonfirst.mapzen.com',
                                           'eng_x', 'foo')
        self.assertTrue('name:en' in props)
        self.assertEquals('foo', props['name:en'])

    def test_short_name(self):
        shape, props, fid = self._call_fut(
            'openstreetmap.org', 'short', 'foo')
        self.assertTrue('name:short' in props)
        self.assertEquals('foo', props['name:short'])


class TagsPriorityI18nTest(unittest.TestCase):

    def _call_fut(self, source, kvs):
        from vectordatasource.transform import tags_name_i18n
        shape = fid = zoom = None

        # need to control the order of tags so that we can force the situation
        # where one key overwrites another.
        tags = OrderedDict()
        for k, v in kvs.items():
            tags['name:%s' % k] = v

        props = dict(
            source=source,
            tags=tags,
            name='unused',
        )
        result = tags_name_i18n(shape, props, fid, zoom)
        return result

    def test_wof_no_two_letter_code(self):
        # given variants which have no 2-letter code (arq), then we should
        # just be left with the ones which do (ara).
        shape, props, fid = self._call_fut('whosonfirst.mapzen.com',
                                           {'ara': 'foo', 'arq': 'bar'})
        self.assertTrue('name:ar' in props)
        self.assertFalse('name:ara' in props)
        self.assertFalse('name:arq' in props)
        self.assertEquals('foo', props['name:ar'])

    def test_osm_invalid_country_code(self):
        # given variants with an invalid or unrecognised country code, then
        # we should keep any original which had no country code, as it is
        # more specific.
        langs = OrderedDict([
            ('en',    'foo'),  # The One True Flavour of English.
            ('en_GB', 'bar'),  # Also the correct flavour ;-)
            ('en_AA', 'baz'),  # User-defined country code.
            ('en_CT', 'bat'),  # Currently unassigned/deleted code.
        ])
        shape, props, fid = self._call_fut('openstreetmap.org', langs)

        self.assertEquals('foo', props.get('name:en'))
        self.assertEquals('bar', props.get('name:en_GB'))
        self.assertFalse('name:en_AA' in props)
        self.assertFalse('name:en_CT' in props)

    def test_osm_invalid_country_code_reverse(self):
        # same as the previous test, just checking that when the order of
        # the keys is different (we wouldn't normally have control over it
        # as it's in a dict), the result is the same.
        langs = OrderedDict([
            ('en_GB', 'bar'),
            ('en_AA', 'baz'),
            ('en_CT', 'bat'),
            ('en',    'foo'),
        ])
        shape, props, fid = self._call_fut('openstreetmap.org', langs)

        self.assertEquals('foo', props.get('name:en'))
        self.assertEquals('bar', props.get('name:en_GB'))
        self.assertFalse('name:en_AA' in props)
        self.assertFalse('name:en_CT' in props)


class DropFeaturesMinPixelsTest(unittest.TestCase):

    def _make_feature_layers(self, pixel_threshold, shape):
        props = dict(mz_min_pixels=pixel_threshold)
        fid = None
        feature = shape, props, fid
        features = [feature]
        feature_layers = [dict(name='layer-name', features=features)]
        return feature_layers

    def _call_fut(self, feature_layers, zoom):
        from tilequeue.process import Context
        from vectordatasource.transform import drop_features_mz_min_pixels
        params = dict(property='mz_min_pixels', source_layers=('layer-name',))
        ctx = Context(
            feature_layers=feature_layers,
            nominal_zoom=zoom,
            params=params,
            unpadded_bounds=None,
            resources=None,
        )
        result = drop_features_mz_min_pixels(ctx)
        return result

    def test_feature_drops(self):
        import shapely.geometry
        exterior_ring = [
            (0, 0),
            (0, 1),
            (1, 1),
            (0, 0),
        ]
        polygon = shapely.geometry.Polygon(exterior_ring)
        feature_layers = self._make_feature_layers(1, polygon)
        zoom = 1
        self._call_fut(feature_layers, zoom)
        features = feature_layers[0]['features']
        self.assertEquals(0, len(features))

    def test_feature_remains(self):
        import shapely.geometry
        exterior_ring = [
            (0, 0),
            (0, 1),
            (1, 1),
            (0, 0),
        ]
        polygon = shapely.geometry.Polygon(exterior_ring)
        feature_layers = self._make_feature_layers(1, polygon)
        zoom = 20
        self._call_fut(feature_layers, zoom)
        features = feature_layers[0]['features']
        self.assertEquals(1, len(features))


class SortKeyTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(SortKeyTest, self).__init__(*args, **kwargs)

        from vectordatasource.transform import CSVMatcher
        import os.path
        landuse_path = os.path.join(
            os.path.dirname(__file__), '..', 'spreadsheets', 'sort_rank',
            'landuse.csv')
        with open(landuse_path) as fh:
            self.matcher = CSVMatcher(fh)

    def test_geometry_type(self):
        import shapely.geometry

        shape = shapely.geometry.LineString([(0, 0), (1, 1)])
        props = dict(kind='dam')
        zoom = 16
        sort_rank_result = self.matcher(shape, props, zoom)
        self.assertIsNotNone(sort_rank_result)
        _, sort_rank = sort_rank_result
        self.assertEquals(int(sort_rank), 265)

        shape = shapely.geometry.Polygon([(0, 0), (1, 1), (0, 1), (0, 0)])
        sort_rank_result = self.matcher(shape, props, zoom)
        self.assertIsNotNone(sort_rank_result)
        _, sort_rank = sort_rank_result
        self.assertEquals(int(sort_rank), 223)


class BuildingsUnifyTest(unittest.TestCase):

    def _call_fut(self, building_shapes, building_part_shapes):
        from tilequeue.process import Context

        building_features = []
        building_id = 1
        for building_shape in building_shapes:
            building_props = dict(
                id=building_id,
                kind='building',
            )
            building_feature = building_shape, building_props, building_id
            building_features.append(building_feature)
            building_id += 1

        part_features = []
        building_part_id = building_id
        for part_shape in building_part_shapes:
            part_props = dict(
                id=building_part_id,
                kind='building_part',
            )
            part_feature = part_shape, part_props, building_part_id
            part_features.append(part_feature)
            building_part_id += 1

        building_features = building_features + part_features
        building_feature_layer = dict(
            features=building_features,
            layer_datum=dict(name='buildings'),
        )
        feature_layers = [building_feature_layer]

        ctx = Context(
            feature_layers=feature_layers,
            nominal_zoom=0,
            unpadded_bounds=None,
            params=dict(source_layer='buildings'),
            resources=None)
        from vectordatasource.transform import buildings_unify
        buildings_unify(ctx)
        return building_feature_layer['features']

    def test_no_overlap(self):
        import shapely.geometry
        building_shape = shapely.geometry.Polygon(
            [(1, 1), (2, 2), (1, 2), (1, 1)])
        part_shape = shapely.geometry.Polygon(
            [(10, 10), (20, 20), (10, 20), (10, 10)])
        result = self._call_fut([building_shape], [part_shape])
        building, part = result
        part_props = part[1]
        assert 'root_id' not in part_props

    def test_overlap(self):
        import shapely.geometry
        building_shape = shapely.geometry.Polygon(
            [(1, 1), (20, 20), (10, 20), (1, 1)])
        part_shape = shapely.geometry.Polygon(
            [(10, 10), (20, 20), (10, 20), (10, 10)])
        result = self._call_fut([building_shape], [part_shape])
        building, part = result
        part_props = part[1]
        root_id = part_props.get('root_id')
        self.assertEquals(root_id, 1)

    def test_best_overlap(self):
        import shapely.geometry
        building1_shape = shapely.geometry.Polygon(
            [(2, 1), (2, 2), (0, 2), (2, 1)])
        building2_shape = shapely.geometry.Polygon(
            [(1, 1), (20, 20), (10, 20), (1, 1)])
        building3_shape = shapely.geometry.Polygon(
            [(19, 1), (30, 30), (19, 30), (19, 1)])
        part_shape = shapely.geometry.Polygon(
            [(10, 10), (20, 20), (10, 20), (10, 10)])

        building_shapes = [building1_shape, building2_shape, building3_shape]
        part_shapes = [part_shape]
        result = self._call_fut(building_shapes, part_shapes)
        for feature in result:
            props = feature[1]
            if props['kind'] == 'building_part':
                root_id = props.get('root_id')
                self.assertEquals(root_id, 2)
            else:
                assert 'root_id' not in props


class DropMergedIdTest(unittest.TestCase):

    def _assert_no_id_in_props(self, features, merge_fn):
        from tilequeue.process import Context
        layer_name = 'layername'
        feature_layer = dict(
            features=features,
            layer_datum=dict(name=layer_name),
        )
        feature_layers = [feature_layer]
        ctx = Context(
            feature_layers=feature_layers,
            nominal_zoom=0,
            unpadded_bounds=None,
            params=dict(source_layer=layer_name),
            resources=None)
        merged_feature_layer = merge_fn(ctx)
        merged_features = merged_feature_layer['features']
        self.assertEquals(1, len(merged_features))
        merged_feature = merged_features[0]
        props = merged_feature[1]
        self.assertTrue('id' not in props)

    def test_merge_buildings(self):
        import shapely.geometry
        from vectordatasource.transform import merge_polygon_features

        buildings = []
        for i in (0, 1):
            id = i + 1
            points = [
                (1, 1),
                (10 + i, 10 + i),
                (1, 10 + i),
                (1, 1),
            ]
            shape = shapely.geometry.Polygon(points)
            props = dict(
                id=id,
                kind='building',
            )
            building = shape, props, id
            buildings.append(building)

        self._assert_no_id_in_props(buildings, merge_polygon_features)

    def test_merge_lines(self):
        import shapely.geometry
        from vectordatasource.transform import merge_line_features

        roads = []
        for i in (0, 1):
            id = i + 1
            points = [
                (1, 1),
                (10 + i, 10 + i),
            ]
            shape = shapely.geometry.LineString(points)
            props = dict(
                id=id,
                kind='road',
            )
            road = shape, props, id
            roads.append(road)

        self._assert_no_id_in_props(roads, merge_line_features)

    def test_merge_polygons(self):
        import shapely.geometry
        from vectordatasource.transform import merge_polygon_features

        landuses = []
        for i in (0, 1):
            id = i + 1
            points = [
                (1, 1),
                (10 + i, 10 + i),
                (1, 10 + i),
                (1, 1),
            ]
            shape = shapely.geometry.Polygon(points)
            props = dict(
                id=id,
                kind='landuse',
            )
            landuse = shape, props, id
            landuses.append(landuse)

        self._assert_no_id_in_props(landuses, merge_polygon_features)

    def test_no_merge_preserve_props(self):
        import shapely.geometry
        from tilequeue.process import Context
        from vectordatasource.transform import merge_polygon_features

        buildings = []
        for i in (0, 100):
            id = i + 1
            points = [
                (1 + i, 1 + i),
                (10 + i, 10 + i),
                (1 + i, 10 + i),
                (1 + i, 1 + i),
            ]
            shape = shapely.geometry.Polygon(points)
            props = dict(
                id=id,
                kind='building',
                unique_value='value-%d' % id,
            )
            building = shape, props, id
            buildings.append(building)

        layer_name = 'buildings'
        feature_layer = dict(
            features=buildings,
            layer_datum=dict(name=layer_name),
        )
        feature_layers = [feature_layer]
        ctx = Context(
            feature_layers=feature_layers,
            nominal_zoom=0,
            unpadded_bounds=None,
            params=dict(source_layer=layer_name),
            resources=None)
        merged_feature_layer = merge_polygon_features(ctx)
        merged_features = merged_feature_layer['features']
        self.assertEquals(2, len(merged_features))
        for f in merged_features:
            props = f[1]
            self.assertTrue('id' in props)

    def test_no_merge_preserve_del_props_fn(self):
        import shapely.geometry
        from vectordatasource.transform import _merge_features_by_property
        from vectordatasource.transform import _POLYGON_DIMENSION

        buildings = []
        for i in (0, 100):
            id = i + 1
            points = [
                (1 + i, 1 + i),
                (10 + i, 10 + i),
                (1 + i, 10 + i),
                (1 + i, 1 + i),
            ]
            shape = shapely.geometry.Polygon(points)
            props = dict(
                id=id,
                kind='building',
                unique_value='value-%d' % id,
            )
            building = shape, props, id
            buildings.append(building)

        def _drop_all_props((shape, props, fid)):
            return None

        merged_features = _merge_features_by_property(
            buildings, _POLYGON_DIMENSION, update_props_pre_fn=_drop_all_props)

        self.assertEquals(2, len(merged_features))
        for f in merged_features:
            props = f[1]
            self.assertTrue('id' in props)
            self.assertTrue('unique_value' in props)


class ShieldTextTransform(unittest.TestCase):

    def _assert_shield_text(self, network, ref, expected_shield_text):
        from vectordatasource.transform import extract_network_information
        shape, properties, fid = extract_network_information(
            None, dict(mz_networks=['road', network, ref]), None, 0)
        self.assertTrue('all_networks' in properties)
        self.assertTrue('all_shield_texts' in properties)
        self.assertEquals([expected_shield_text],
                          properties['all_shield_texts'])

    def test_a_road(self):
        # based on http://www.openstreetmap.org/relation/2592
        # simple pattern, should be just the number.
        self._assert_shield_text("BAB", "A 66", "66")

        # based on http://www.openstreetmap.org/relation/446270
        # simple pattern, should be just the number
        self._assert_shield_text("FR:A-road", "A 66", "66")

    def test_sr70var1(self):
        # based on http://www.openstreetmap.org/relation/449595
        # see https://github.com/tilezen/vector-datasource/issues/192
        self._assert_shield_text("IT:Toscana", "SR70var1", "70var1")

    def test_cth_j(self):
        # based on http://www.openstreetmap.org/relation/4010101
        # see https://github.com/tilezen/vector-datasource/issues/192
        self._assert_shield_text("US:WI:CTH", "CTH J", "J")

    def test_purple_belt(self):
        # based on http://www.openstreetmap.org/relation/544634
        # see https://github.com/tilezen/vector-datasource/issues/192
        self._assert_shield_text("US:PA:Belt", "Purple Belt", "Purple Belt")

    def test_t_02_16(self):
        # based on http://www.openstreetmap.org/relation/1296750
        # see https://github.com/tilezen/vector-datasource/issues/192
        self._assert_shield_text("ua:territorial", u"Т-02-16", u"Т0216")

    def test_fi_pi_li(self):
        # based on http://www.openstreetmap.org/relation/1587534
        # see https://github.com/tilezen/vector-datasource/issues/192
        self._assert_shield_text("IT:B-road", "FI-PI-LI", "FI-PI-LI")

    def test_cr_315a(self):
        # based on http://www.openstreetmap.org/relation/2564219
        # see https://github.com/tilezen/vector-datasource/issues/192
        self._assert_shield_text("US:TX:Guadalupe", "CR 315A", "315A")

    def test_eo1a(self):
        # based on http://www.openstreetmap.org/relation/5641878
        # see https://github.com/tilezen/vector-datasource/issues/192
        self._assert_shield_text("GR:national", u"ΕΟ1α", u"ΕΟ1α")

    def test_i5_truck(self):
        # based on http://www.openstreetmap.org/relation/146933
        # see https://github.com/tilezen/vector-datasource/issues/192
        # note: original example was SD 37 Truck, but that wasn't in the 'ref',
        # so changed to this example.
        self._assert_shield_text("US:I", "5 Truck", "5")

    def test_cth_pv(self):
        # based on http://www.openstreetmap.org/relation/5179634
        # see https://github.com/tilezen/vector-datasource/issues/192
        self._assert_shield_text("US:WI:Washington", "CTH PV", "PV")

    def test_null(self):
        # see https://github.com/tilezen/vector-datasource/issues/192
        self._assert_shield_text("something", None, None)


class RankBoundsTest(unittest.TestCase):

    def _call_fut(self, shape, bounds):
        from tilequeue.process import Context
        from vectordatasource.transform import rank_features
        props = dict(foo='bar')
        feature = shape, props, 1
        feature_layer = dict(
            features=[feature],
            layer_datum=dict(name='layer-name'),
        )
        params = dict(
            source_layer='layer-name',
            rank_key='rank',
            items_matching=dict(foo='bar'),
        )
        ctx = Context(
            feature_layers=[feature_layer],
            nominal_zoom=0,
            unpadded_bounds=bounds,
            params=params,
            resources=None,
        )
        rank_features(ctx)
        rank = props.get('rank')
        return rank

    def test_rank_within_bounds(self):
        from shapely.geometry import Point
        shape = Point(1, 1)
        bounds = (0, 0, 2, 2)
        rank = self._call_fut(shape, bounds)
        self.assertEquals(rank, 1)

    def test_rank_outside_bounds(self):
        from shapely.geometry import Point
        shape = Point(10, 10)
        bounds = (0, 0, 2, 2)
        rank = self._call_fut(shape, bounds)
        self.assertIsNone(rank)
