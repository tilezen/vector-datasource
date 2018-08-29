# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class AddKindDetailForPois(FixtureTest):
    def test_seafood_restaurant(self):
        self.generate_fixtures(dsl.way(1426311638, wkt_loads('POINT (-73.98758834870338 40.75562796002149)'), {u'cuisine': u'seafood', u'amenity': u'restaurant', u'name': u'Red Lobster', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_has_feature(
            16, 19298, 24629, 'pois',
            {'id': 1426311638, 'kind': 'restaurant',
             'kind_detail': 'seafood'})

    def test_japanese_restaurant(self):
        self.generate_fixtures(dsl.way(280288213, wkt_loads('POLYGON ((-73.87594850997039 40.73503422247008, -73.8759177875877 40.73506036078218, -73.8759362928825 40.73507288538649, -73.87585643265369 40.7351412941888, -73.87578681321918 40.73509419082197, -73.875790675975 40.73509085546669, -73.87586667344799 40.73502591810828, -73.8758842804276 40.7350377620337, -73.8759150028103 40.7350114875756, -73.87594850997039 40.73503422247008))'), {u'building': u'yes', u'cuisine': u'japanese', u'amenity': u'restaurant', u'name': u'Sushi Island', u'addr:postcode': u'11373', u'way_area': u'165.042', u'height': u'8.8', u'source': u'openstreetmap.org', u'addr:housenumber': u'87-18A', u'nycdoitt:bin': u'4437595', u'addr:street': u'Queens Boulevard'}))  # noqa

        self.assert_has_feature(
            16, 19319, 24634, 'pois',
            {'id': 280288213, 'kind': 'restaurant',
             'kind_detail': 'japanese'})

    def test_baseball_pitch(self):
        self.generate_fixtures(dsl.way(4305351592, wkt_loads('POINT (-73.7833481941897 40.84455331362909)'), {u'source': u'openstreetmap.org', u'sport': u'baseball', u'name': u'Anthony Ambrosini Field', u'leisure': u'pitch', u'surface': u'grass'}))  # noqa

        self.assert_has_feature(
            16, 19336, 24608, 'pois',
            {'id': 4305351592, 'kind': 'pitch', 'kind_detail': 'baseball'})

    def test_basketball_pitch(self):
        self.generate_fixtures(dsl.way(326894220, wkt_loads('POLYGON ((-73.8630419651258 40.73616871106279, -73.86291260772489 40.73639789351569, -73.86275962463201 40.73634827255258, -73.8628889820329 40.73611908992869, -73.8630419651258 40.73616871106279))'), {u'source': u'openstreetmap.org', u'way_area': u'678.376', u'sport': u'basketball', u'leisure': u'pitch'}))  # noqa

        self.assert_has_feature(
            16, 19321, 24634, 'pois',
            {'id': 326894220, 'kind': 'pitch', 'kind_detail': 'basketball'})
