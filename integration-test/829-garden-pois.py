# -*- encoding: utf-8 -*-
import unittest

import dsl
from shapely.wkt import loads as wkt_loads

from . import FixtureTest
from . import SKIP_UNIT_TEST_REASON


class GardenPois(FixtureTest):
    @unittest.skip(SKIP_UNIT_TEST_REASON)
    def test_garden_with_area(self):
        # update gardens in pois
        # garden with area in pois
        self.generate_fixtures(dsl.way(4867441963, wkt_loads('POINT (-122.470329974091 37.76904559266841)'), {u'name': u'Friend Gate', u'barrier': u'gate', u'access': u'yes', u'source': u'openstreetmap.org', u'alt_name': u'North Gate'}), dsl.way(120480164, wkt_loads('POLYGON ((-122.477009127891 37.76560789118319, -122.476976878373 37.76595571629439, -122.476343925424 37.76603198479138, -122.47561431375 37.76618466357608, -122.474777533063 37.76643058227678, -122.473704585287 37.76673586687239, -122.473028692868 37.76693100974988, -122.4728678046 37.76702432024518, -122.472685446598 37.76716847549728, -122.472502998763 37.7673381238552, -122.472417119822 37.767499179366, -122.4723634904 37.7677027706408, -122.472342020664 37.76793178352569, -122.47227770129 37.76816931707089, -122.472202602132 37.76837276447829, -122.472127502975 37.76853388874688, -122.471955834924 37.7687036049834, -122.471794946656 37.7688052925168, -122.471580339135 37.76889860064709, -122.471322792143 37.7689579655759, -122.470925826619 37.7690257807173, -122.470441724512 37.76906398440309, -122.470399413862 37.76905127351358, -122.470352072647 37.76904601873179, -122.470329974091 37.76904559266841, -122.470315062057 37.76904537963672, -122.470269697135 37.76905148654529, -122.470232417051 37.76906398440309, -122.470035326678 37.76907669529049, -122.469734930047 37.76906817402539, -122.469380903993 37.76899190865968, -122.469016098156 37.76889860064709, -122.468662072103 37.7687628990579, -122.46836158564 37.76861029660709, -122.468029119154 37.76840670783071, -122.467632063798 37.76817769641669, -122.467325828118 37.76801870171858, -122.467095589911 37.76788086816419, -122.466968208803 37.76778549940821, -122.466831485217 37.7675919920607, -122.466736173965 37.76739429448978, -122.466689281908 37.76721775806578, -122.466672483412 37.76702432024518, -122.466602774146 37.76679317416819, -122.466594060487 37.76668090295589, -122.466573309404 37.76608815641809, -122.477009127891 37.76560789118319))'), {
                               u'website': u'http://www.sfbotanicalgarden.org/', u'addr:housenumber': u'1199', u'name': u'San Francisco Botanical Garden', u'source': u'openstreetmap.org', u'addr:postcode': u'94122', u'way_area': u'298849', u'wikipedia': u'en:San Francisco Botanical Garden', u'leisure': u'garden', u'phone': u'+1-415-661-1316', u'wikidata': u'Q589884', u'addr:state': u'CA', u'old_name': u'Strybing Arboretum', u'operator': u'San Francisco Recreation & Parks Department;San Francisco Botanical Garden Society', u'addr:street': u'9th Avenue', u'tourism': u'attraction', u'addr:city': u'San Francisco'}))

        self.assert_has_feature(
            13, 1309, 3166, 'pois',
            {'id': 120480164, 'kind': 'garden'})

        # garden with area in landuse
        self.assert_has_feature(
            13, 1309, 3166, 'landuse',
            {'id': 120480164, 'kind': 'garden'})

    def test_garden_point(self):
        # garden without area in pois
        self.generate_fixtures(dsl.way(2969748431, wkt_loads('POINT (-122.469937859469 37.7687579993099)'),
                               {u'source': u'openstreetmap.org', u'name': u'Ancient Plant Garden', u'leisure': u'garden'}))

        self.assert_has_feature(
            16, 10473, 25332, 'pois',
            {'id': 2969748431, 'kind': 'garden'})
