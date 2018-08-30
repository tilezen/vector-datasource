# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class NormalizeOperatorValues(FixtureTest):
    def test_us_national_park_service(self):
        # Standardize operator values
        # US National Park Service in POIS
        self.generate_fixtures(dsl.way(4285104560, wkt_loads('POINT (-93.15995443474161 36.06406411633689)'), {u'operator': u'US National Park Service', u'capacity': u'31', u'tourism': u'camp_site', u'name': u'Ozark Campground', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_has_feature(
            16, 15808, 25720, 'pois',
            {'id': 4285104560,
             'operator': 'United States National Park Service'})

        self.assert_no_matching_feature(
            16, 15808, 25720, 'pois',
            {'id': 4285104560, 'operator': 'US National Park Service'})

    def test_national_park_service(self):
        # National Park Service in landuse
        self.generate_fixtures(dsl.way(368766687, wkt_loads('POLYGON ((-107.691008327217 38.5435818599483, -107.691004105135 38.54385727991479, -107.690910410851 38.54430869938989, -107.690689065965 38.5452222794257, -107.690455683654 38.54550261120179, -107.689922264039 38.54559057473178, -107.68940573275 38.5454993090544, -107.688838985638 38.54515391765138, -107.68833071885 38.54479461328009, -107.688422347009 38.54431628742849, -107.688349224145 38.54383606137318, -107.687916146346 38.54338667648649, -107.688157703326 38.5432047015075, -107.688166506816 38.54291199484179, -107.688087005913 38.5422459878861, -107.688923696769 38.5421561231987, -107.690414540814 38.54232067596549, -107.690772878781 38.54257811386849, -107.690901966688 38.54293658618219, -107.690962513138 38.54322830909829, -107.691008327217 38.5435818599483))'), {u'name': u'South Rim Campground', u'wheelchair': u'limited', u'way_area': u'129067', u'source': u'openstreetmap.org', u'operator': u'National Park Service', u'tourism': u'camp_site'}))  # noqa

        self.assert_has_feature(
            16, 13163, 25153, 'landuse',
            {'id': 368766687,
             'operator': 'United States National Park Service'})

        self.assert_no_matching_feature(
            16, 13163, 25153, 'landuse',
            {'id': 368766687, 'operator': 'National Park Service'})

    def test_us_national_forest_service(self):
        # US National Forest Service in POIS
        self.generate_fixtures(dsl.way(796692690, wkt_loads('POINT (-122.08805873213 46.165678293632)'), {u'operator': u'US National Forest Service', u'toilets': u'outhouse', u'amenity': u'toilets', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_has_feature(
            16, 10542, 23271, 'pois',
            {'id': 796692690, 'operator': 'United States Forest Service'})

        self.assert_no_matching_feature(
            16, 10542, 23271, 'pois',
            {'id': 796692690, 'operator': 'US National Forest Service'})

    def test_us_forest_service(self):
        # US Forest Service in landuse
        self.generate_fixtures(dsl.way(432302983, wkt_loads('POLYGON ((-118.192735038948 37.33343659588739, -118.192166315542 37.33508296600598, -118.189130099713 37.3358507121247, -118.187252530938 37.33467348391568, -118.186898504884 37.3336668755964, -118.187005763729 37.3328308940269, -118.187724595619 37.3324981844882, -118.188679504766 37.33261761152519, -118.189355397186 37.33237875726129, -118.190320996285 37.3324896845901, -118.192735038948 37.33343659588739))'), {u'operator': u'US Forest Service', u'source': u'openstreetmap.org', u'way_area': u'225657', u'tourism': u'camp_site', u'name': u'Grandview campground'}))  # noqa

        self.assert_has_feature(
            16, 11252, 25432, 'landuse',
            {'id': 432302983, 'operator': 'United States Forest Service'})

        self.assert_no_matching_feature(
            16, 11252, 25432, 'landuse',
            {'id': 432302983, 'operator': 'US Forest Service'})

    def test_nsw_parks_and_wildlife_service(self):
        # NSW Parks and Wildlife Service in POIs
        self.generate_fixtures(dsl.way(2514034066, wkt_loads('POINT (148.493255333852 -35.87963414153472)'), {u'website': u'http://www.nationalparks.nsw.gov.au/kosciuszko-national-park/wolgal-hut/accommodation', u'amenity': u'shelter', u'name': u'Wolgal Lodge', u'source': u'openstreetmap.org', u'wheelchair': u'no', u'shelter_type': u'basic_hut', u'internet_access:fee': u'no', u'operator': u'NSW Parks and Wildlife Service', u'smoking': u'no', u'tourism': u'wilderness_hut', u'internet_access': u'no'}))  # noqa

        self.assert_has_feature(
            16, 59800, 39773, 'pois',
            {'id': 2514034066,
             'operator': 'National Parks & Wildife Service NSW'})

        self.assert_no_matching_feature(
            16, 59800, 39773, 'pois',
            {'id': 2514034066, 'operator': 'NSW Parks and Wildlife Service'})

    def test_department_of_national_parks_nsw(self):
        # Department of National Parks NSW in landuse
        self.generate_fixtures(dsl.way(429280600, wkt_loads('POLYGON ((150.297311106735 -34.6696140263849, 150.297940107097 -34.66947062214052, 150.298033981044 -34.66962614296092, 150.29738485842 -34.66977390594021, 150.297311106735 -34.6696140263849))'), {u'amenity': u'parking', u'fee': u'yes', u'way_area': u'1702.33', u'surface': u'unpaved', u'access': u'yes', u'source': u'openstreetmap.org', u'parking': u'surface', u'operator': u'NSW National Parks and Wildlife Service', u'smoothness': u'intermediate'}))  # noqa

        self.assert_has_feature(
            16, 60128, 39504, 'landuse',
            {'id': 429280600,
             'operator': 'National Parks & Wildife Service NSW'})

        self.assert_no_matching_feature(
            16, 60128, 39504, 'landuse',
            {'id': 429280600, 'operator': 'Department of National Parks NSW'})
