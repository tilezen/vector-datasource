# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class RestAreaServices(FixtureTest):
    def test_rest_area_node(self):
        self.generate_fixtures(dsl.way(159773030, wkt_loads('POINT (-76.73912905210828 40.99079246918038)'), {u'source': u'openstreetmap.org', u'highway': u'rest_area', u'name': u'Foo Rest Area'}))  # noqa

        self.assert_has_feature(
            16, 18798, 24573, 'pois',
            {'kind': 'rest_area', 'id': 159773030, 'min_zoom': 13})

    def test_rest_area_way(self):
        # Way: Crystal Springs Rest Area (97057565)
        self.generate_fixtures(dsl.way(97057565, wkt_loads('POLYGON ((-122.365488944754 37.54048597695269, -122.363673359734 37.53894968362569, -122.363521634282 37.53881541316188, -122.363421831454 37.53868392047339, -122.363355445955 37.53852749658311, -122.363020823511 37.53696630264469, -122.36330406232 37.5367516065384, -122.365488944754 37.54048597695269))'), {u'drinking_water': u'yes', u'toilets': u'yes', u'handicapped_accessible': u'yes', u'vending': u'yes', u'name': u'Crystal Springs Rest Area', u'sanitation': u'no', u'area': u'yes', u'route': u'280', u'way_area': u'35229.6', u'pet_area': u'yes', u'phone': u'yes', u'picnic_tables': u'yes', u'source': u'openstreetmap.org', u'addr:county': u'San Mateo', u'attribution': u'Caltrans', u'caltrans:district': u'4', u'highway': u'rest_area', u'description': u'Near San Francisco Reservoir'}))  # noqa

        self.assert_has_feature(
            16, 10492, 25385, 'landuse',
            {'kind': 'rest_area', 'id': 97057565, 'sort_rank': 44})

    def test_service_area_node(self):
        # NOTE: this has been remapped as an area now. the test data here
        # is superseded by the 1698-too-many-service-areas test.
        # node: Tiffin River
        self.generate_fixtures(dsl.way(200412620, wkt_loads('POINT (-84.41292493378698 41.6045519557572)'), {u'source': u'openstreetmap.org', u'name': u'Tiffin River', u'highway': u'services'}))  # noqa

        self.assert_has_feature(
            16, 17401, 24424, 'pois',
            {'kind': 'service_area', 'id': 200412620, 'min_zoom': 17})

    def test_service_area_way(self):
        # Way: Nicole Driveway (274732386)
        self.generate_fixtures(dsl.way(274732386, wkt_loads('POLYGON ((-120.123766060274 38.09757738412661, -120.123761209371 38.0977196908478, -120.123658621766 38.0979925683359, -120.123633379106 38.0982482663423, -120.123585319239 38.098378271151, -120.123533216952 38.09837445372108, -120.123577234401 38.09825915310519, -120.123617928083 38.09797468287368, -120.123713957987 38.09768759586379, -120.123702639215 38.09747749355018, -120.123762826339 38.09746978790201, -120.123766060274 38.09757738412661))'), {u'source': u'openstreetmap.org', u'way_area': u'744.019', u'name': u'Nicole Driveway', u'highway': u'services', u'area': u'yes'}))  # noqa

        self.assert_has_feature(
            16, 10900, 25256, 'landuse',
            {'kind': 'service_area', 'id': 274732386, 'sort_rank': 45})
