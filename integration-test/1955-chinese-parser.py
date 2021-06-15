# -*- encoding: utf-8 -*-
import dsl
from shapely.wkt import loads as wkt_loads
from . import FixtureTest


class ChineseNameTest(FixtureTest):
    def test_san_francisco_osm(self):
        # San Francisco (osm city)
        self.generate_fixtures(dsl.way(26819236, wkt_loads(
            'POINT (-122.419236226182 37.77928077351228)'),
                                       {u'name:pt': u'S\xe3o Francisco',
                                        u'name:ko':
                                            u'\uc0cc\ud504\ub780\uc2dc\uc2a4\ucf54',
                                        u'name:kn':
                                            u'\u0cb8\u0cbe\u0ca8\u0ccd '
                                            u'\u0cab\u0ccd\u0cb0\u0cbe\u0ca8\u0ccd\u0cb8\u0cbf\u0cb8\u0ccd\u0c95\u0cca',
                                        u'rank': u'10',
                                        u'wikidata': u'Q62',
                                        u'name:ru':
                                            u'\u0421\u0430\u043d-\u0424\u0440\u0430\u043d\u0446\u0438\u0441\u043a\u043e',
                                        u'name:ta':
                                            u'\u0bb8\u0bbe\u0ba9\u0bcd '
                                            u'\u0baa\u0bcd\xb2\u0bb0\u0bbe\u0ba9\u0bcd\u0bb8\u0bbf\u0bb8\u0bcd\u0b95\u0bca',
                                        u'name:fa': u'\u0633\u0627\u0646 '
                                                    u'\u0641\u0631\u0627\u0646\u0633\u06cc\u0633\u06a9\u0648',
                                        u'is_in:country': u'United States',
                                        u'wikipedia': u'en:San Francisco',
                                        u'name:de': u'San Francisco',
                                        u'source': u'openstreetmap.org',
                                        u'name:zh': u'旧金山/三藩市/舊金山',
                                        u'name:zh-Hans': u'旧金山',
                                        u'name:zh-Hant': u'舊金山',
                                        u'name:zh-Hant-hk': u'三藩市',
                                        u'name:zh-Hant-tw': u'舊金山',
                                        u'name:ja':
                                            u'\u30b5\u30f3\u30d5\u30e9\u30f3\u30b7\u30b9\u30b3',
                                        u'short_name': u'SF',
                                        u'name:hi': u'\u0938\u0948\u0928 '
                                                    u'\u092b\u094d\u0930\u093e\u0902\u0938\u093f\u0938\u094d\u0915\u094b',
                                        u'is_in:country_code': u'US',
                                        u'census:population': u'2010',
                                        u'population': u'864816',
                                        u'fixme': u'When zooming out, '
                                                  u'Oakland (a nearby city) '
                                                  u'label covers over the '
                                                  u'San Francisco label',
                                        u'name': u'San Francisco',
                                        u'place': u'city',
                                        u'is_in:continent': u'North America',
                                        u'name:eu': u'San Francisco'}))  # noqa

        self.assert_has_feature(
            16, 10482, 25330, 'places',
            {'id': 26819236, 'kind': 'locality', 'kind_detail': 'city',
             'source': "openstreetmap.org",
             'name': 'San Francisco',
             'name:zh': '旧金山',
             'name:zht': '舊金山'})
