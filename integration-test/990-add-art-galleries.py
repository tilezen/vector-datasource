# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class AddArtGalleries(FixtureTest):
    def test_node(self):
        self.generate_fixtures(dsl.way(2026996113, wkt_loads('POINT (-122.399331086621 37.78741651330239)'), {u'addr:housenumber': u'111', u'source': u'openstreetmap.org', u'tourism': u'gallery', u'name': u'111 Minna', u'addr:street': u'Minna Street'}))  # noqa

        self.assert_has_feature(
            16, 10485, 25328, 'pois',
            {'id': 2026996113, 'kind': 'gallery', 'min_zoom': 17})

    def test_way(self):
        self.generate_fixtures(dsl.way(83488820, wkt_loads('POLYGON ((-0.153426141983682 51.51770999191131, -0.152916078565359 51.51779490348889, -0.152684403053585 51.5173152823619, -0.1528928121995 51.51727419570179, -0.152879427301767 51.5172478107795, -0.152865413583335 51.51722019603508, -0.152941141561786 51.51720538245069, -0.152955424774804 51.51723361210728, -0.152969887650878 51.51726206534747, -0.153183417193913 51.51722030783569, -0.153426141983682 51.51770999191131))'), {u'building': u'yes', u'fhrs:rating_date': u'2012-07-12', u'name': u'The Wallace Collection', u'fhrs:hygiene': u'15', u'opening_hours': u'Mo-Su 10:00-17:00; Fr,Sa 10:00-23:00', u'way_area': u'5386.88', u'wikipedia': u'en:Wallace Collection', u'uri': u'http://www.wallacecollection.org/', u'fhrs:id': u'411876', u'source': u'openstreetmap.org', u'fhrs:rating': u'2', u'postal_code': u'W1U 3BN', u'fhrs:confidence_management': u'5', u'fhrs:structural': u'10', u'building:name': u'Hertford House', u'addr:street': u'Manchester Square', u'tourism': u'gallery', u'fhrs:local_authority_id': u'00593/2001/2/001', u'name:es': u'Colecci\xf3n Wallace.', u'addr:city': u'London'}))  # noqa

        self.assert_has_feature(
            15, 16370, 10894, 'pois',
            {'id': 83488820, 'kind': 'gallery'})
