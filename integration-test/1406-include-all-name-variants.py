# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class IncludeAllNameVariants(FixtureTest):

    def test_duplicate_names(self):
        self.generate_fixtures(dsl.way(206270454, wkt_loads('POINT (19.94780199025289 50.06866631266201)'), {u'name:en': u'Krakow Main Station', u'uic_ref': u'5100028', u'name': u'Krak\xf3w G\u0142\xf3wny', u'designation': u'A', u'platforms': u'5', u'wikipedia': u'pl:Krak\xf3w G\u0142\xf3wny', u'name:cs': u'Krakov hlavn\xed n\xe1dra\u017e\xed', u'name:de': u'Krakau Hauptbahnhof', u'source': u'openstreetmap.org', u'wikidata': u'Q2154725', u'name:pl': u'Krak\xf3w G\u0142\xf3wny', u'railway': u'station'}))  # noqa

        self.assert_has_feature(
            15, 18199, 11103, 'pois',
            {'id': 206270454, 'kind': 'station',
             'name': None, 'name:pl': None})
