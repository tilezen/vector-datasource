# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class MissingNameShort(FixtureTest):
    def test_missouri(self):
        self.generate_fixtures(dsl.way(473849775, wkt_loads('POINT (-92.56178739745549 38.76048147258739)'), {u'name:short': u'MO', u'population:date': u'2014-01-01', u'ISO3166-2': u'US-MO', u'name:ru': u'\u041c\u0438\u0441\u0441\u0443\u0440\u0438', u'name:pl': u'Missouri', u'name:abbreviation': u'Mo.', u'is_in': u'USA', u'name:hu': u'Missouri', u'is_in:country': u'USA', u'wikipedia': u'en:Missouri', u'source': u'openstreetmap.org', u'name:fy': u'Missoury', u'name:zh': u'\u5bc6\u82cf\u91cc\u5dde', u'name:nl': u'Missouri', u'is_in:country_code': u'US', u'source:population': u'wikipedia', u'name:tok': u'ma Misuwi', u'name:uk': u'\u041c\u0456\u0441\u0441\u0443\u0440\u0456', u'name:be': u'\u041c\u0456\u0441\u0443\u0440\u044b', u'state_code': u'MO', u'population': u'6063589', u'name:eo': u'Misurio', u'name:en': u'Missouri', u'name': u'Missouri', u'ref': u'MO', u'place': u'state', u'is_in:continent': u'North America', u'name:es': u'Misuri'}))  # noqa

        self.assert_has_feature(
            16, 15917, 25102, 'places',
            {'id': 473849775, 'name:short': 'MO'})
