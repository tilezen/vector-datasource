import unittest


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
