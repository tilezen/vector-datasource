import unittest
from collections import OrderedDict


class BuildingsClassTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(BuildingsClassTest, self).__init__(*args, **kwargs)

        from vectordatasource.transform import CSVMatcher
        import os.path
        buildings_path = os.path.join(
            os.path.dirname(__file__), '..', 'spreadsheets', 'scalerank',
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
        from ModestMaps.Core import Coordinate
        from vectordatasource.transform import drop_features_mz_min_pixels
        params = dict(property='mz_min_pixels', source_layers=('layer-name',))
        ctx = Context(
            feature_layers=feature_layers,
            tile_coord=Coordinate(column=1, row=1, zoom=zoom),
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
            os.path.dirname(__file__), '..', 'spreadsheets', 'sort_key',
            'landuse.csv')
        with open(landuse_path) as fh:
            self.matcher = CSVMatcher(fh)

    def test_geometry_type(self):
        import shapely.geometry

        shape = shapely.geometry.LineString([(0, 0), (1, 1)])
        props = dict(kind='dam')
        zoom = 16
        sort_key_result = self.matcher(shape, props, zoom)
        self.assertIsNotNone(sort_key_result)
        _, sort_key = sort_key_result
        self.assertEquals(int(sort_key), 265)

        shape = shapely.geometry.Polygon([(0, 0), (1, 1), (0, 1), (0, 0)])
        sort_key_result = self.matcher(shape, props, zoom)
        self.assertIsNotNone(sort_key_result)
        _, sort_key = sort_key_result
        self.assertEquals(int(sort_key), 223)


class BuildingsUnifyTest(unittest.TestCase):

    def _call_fut(self, building_shapes, building_part_shapes):
        from tilequeue.tile import deserialize_coord
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
            tile_coord=deserialize_coord('0/0/0'),
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
