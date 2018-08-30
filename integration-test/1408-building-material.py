# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class BuildingMaterial(FixtureTest):

    def test_building_material(self):
        self.generate_fixtures(dsl.way(135174116, wkt_loads('POLYGON ((-122.405489487052 37.79049399242389, -122.405257182719 37.79052182048538, -122.405229334945 37.7903863005666, -122.405323298724 37.79037409027359, -122.405312159615 37.790320705713, -122.405218285667 37.79033291601488, -122.405188641263 37.79018965781179, -122.405420316775 37.79015977090678, -122.405489487052 37.79049399242389))'), {u'website': u'http://www.hoteltriton.com/?utm_source=tripadvisor.com&utm_medium=media&utm_content=homepagelink&utm_campaign=paid-businesslisting', u'building': u'yes', u'name': u'Hotel Triton', u'building:colour': u'white', u'building:levels': u'8', u'addr:postcode': u'94108', u'way_area': u'1162.21', u'addr:state': u'CA', u'height': u'26.54', u'phone': u'415) 394-0555', u'building:material': u'brick', u'source': u'openstreetmap.org', u'addr:housenumber': u'342', u'operator': u'Kimpton Hotel', u'smoking': u'no', u'addr:street': u'Grant Avenue', u'tourism': u'hotel', u'addr:city': u'San Francisco'}))  # noqa

        self.assert_has_feature(
            16, 10484, 25327, 'buildings',
            {'id': 135174116, 'kind': 'building',
             'building_material': 'brick'})

    def test_building_part_material(self):
        self.generate_fixtures(dsl.way(451331532, wkt_loads('POLYGON ((-122.405961461902 37.80237427287228, -122.405957060157 37.80240167058777, -122.4059466397 37.80240379994348, -122.40595427538 37.8024273648092, -122.405921666535 37.80243396580938, -122.405929122552 37.8024566079453, -122.405898040843 37.80246285405057, -122.405830667197 37.80247669485009, -122.405804705885 37.80248201823378, -122.4057973397 37.80245937610569, -122.405761227425 37.80246675786609, -122.405753412082 37.802443193013, -122.405738859375 37.8024461741093, -122.405718826944 37.80242090576539, -122.405707957329 37.80238378399748, -122.405706160698 37.80234630731798, -122.405720803237 37.8023433971962, -122.405712269242 37.8023174900098, -122.405748471348 37.80231010823448, -122.405745596739 37.80229797089068, -122.405772366535 37.8022842010364, -122.405819258593 37.80227256053891, -122.405864893009 37.80227355423999, -122.405872888015 37.80228469788678, -122.405905407028 37.80227809687329, -122.405913941023 37.8023038621163, -122.405924361481 37.80230180373629, -122.405944214249 37.80232352319099, -122.405957599146 37.8023510628825, -122.405961461902 37.80237427287228))'), {u'building:colour': u'gray', u'source': u'openstreetmap.org', u'building:part': u'yes', u'way_area': u'636.801', u'height': u'5', u'building:material': u'concrete'}))  # noqa

        self.assert_has_feature(
            16, 10484, 25324, 'buildings',
            {'id': 451331532, 'kind': 'building_part',
             'building_material': 'concrete'})
