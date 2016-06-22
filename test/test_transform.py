import unittest


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
        match_result = self.matcher(props, z)
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
        return result

    def test_osm_convert_2_3(self):
        eng = self._call_fut('en')
        self.assertEquals(eng, 'eng')

    def test_osm_convert_3(self):
        eng = self._call_fut('eng')
        self.assertEquals(eng, 'eng')

    def test_osm_convert_not_found(self):
        invalid = self._call_fut('foo')
        self.assertIsNone(invalid)

    def test_osm_convert_country(self):
        eng_gb = self._call_fut('en_GB')
        self.assertEquals(eng_gb, 'eng_GB')

    def test_osm_convert_country_invalid(self):
        not_found = self._call_fut('en_foo')
        self.assertIsNone(not_found)

    def test_osm_convert_lookup(self):
        zh_min_nan = self._call_fut('zh-min-nan')
        self.assertEquals(zh_min_nan, 'nan')
        zh_min_nan = self._call_fut('zh-yue')
        self.assertEquals(zh_min_nan, 'yue')


class L10nWofTransformTest(unittest.TestCase):

    def _call_fut(self, x):
        from vectordatasource.transform import _convert_wof_l10n_name
        result = _convert_wof_l10n_name(x)
        return result

    def test_osm_convert_valid(self):
        eng = self._call_fut('eng_x')
        self.assertEquals(eng, 'eng')

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
        self.assertTrue('name:eng' in props)
        self.assertEquals('foo', props['name:eng'])

    def test_wof_source(self):
        shape, props, fid = self._call_fut('whosonfirst.mapzen.com',
                                           'eng_x', 'foo')
        self.assertTrue('name:eng' in props)
        self.assertEquals('foo', props['name:eng'])


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
