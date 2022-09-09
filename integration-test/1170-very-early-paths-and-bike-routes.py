# -*- encoding: utf-8 -*-
import unittest

from . import FixtureTest
from . import SKIP_UNIT_TEST_MESSAGE


class VeryEarlyPathsAndBikeRoutes(FixtureTest):

    @unittest.skip(SKIP_UNIT_TEST_MESSAGE)
    def test_path_with_international_route(self):
        # highway=path, with route inter-national
        # GR5-Grand Traverse de Jura between France and Switzerland
        #         self.load_fixtures([
        #             'https://www.openstreetmap.org/way/285975282',
        #             'https://www.openstreetmap.org/relation/6009161',
        #         ], clip=self.tile_bbox(9, 265, 179))
        import dsl
        from shapely.wkt import loads as wkt_loads
        self.generate_fixtures(
            dsl.way(285975282, dsl.tile_diagonal(15, 17003, 11507), {
                'highway': 'footway',
                'name': 'GR5-Grand Traverse de Jura',
                'source': 'openstreetmap.org'
            }),
            dsl.relation(6009161, {
                'name': 'European long distance path E2 - Jura',
                'name:fr': 'Chemin de randonnée Européen E2 - Jura',
                'name:nl': 'Europese wandelroute E2, Jura',
                'network': 'iwn',
                'operator': 'European Ramblers Association',
                'ref': 'E2',
                'route': 'foot',
                'type': 'route',
                'source': 'openstreetmap.org'
            }, ways=[285975282]),
        )

        self.assert_has_feature(
            9, 265, 179, 'roads',
            {'kind': 'path', 'walking_network': 'iwn'})

    @unittest.skip(SKIP_UNIT_TEST_MESSAGE)
    def test_path_with_national_route(self):
        # highway=path, with route national (Pacific Crest Trail) at zoom 9
        #         self.load_fixtures([
        #             'https://www.openstreetmap.org/way/236361475',
        #             'https://www.openstreetmap.org/relation/1225378',
        #         ], clip=self.tile_bbox(9, 86, 197))

        import dsl
        self.generate_fixtures(
            dsl.way(236361475, dsl.tile_diagonal(9, 86, 197), {
                'ref': 'PCT Section H',
                'source': 'GPS',
                'motorcar': 'no',
                'motorcycle': 'no',
                'foot': 'designated',
                'name': 'Pacific Crest Trail',
                'alt_name': 'Pacific Crest National Scenic Trail',
                'bicycle': 'no',
                'highway': 'path',
                'horse': 'yes',
                'network': 'nwn',
                'source': 'openstreetmap.org'
            }),
            dsl.relation(1225378, {
                'name': 'Pacific Crest Trail',
                'network': 'nwn',
                'ref': 'PCT',
                'route': 'hiking',
                'type': 'route',
                'wikidata': 'Q2003736',
                'wikipedia': 'en:Pacific Crest Trail',
                'source': 'openstreetmap.org'
            }, ways=[236361475]),
        )

        self.assert_has_feature(
            9, 86, 197, 'roads',
            {'kind': 'path', 'walking_network': 'nwn'})

    def test_path_with_regional_route(self):
        # highway=path, with route regional (Merced Pass Trail) at zoom 11
        self.load_fixtures([
            'https://www.openstreetmap.org/way/373491941',
            'https://www.openstreetmap.org/relation/5549623',
        ], clip=self.tile_bbox(11, 343, 792))

        self.assert_has_feature(
            11, 343, 792, 'roads',
            {'kind': 'path', 'walking_network': 'rwn'})

    @unittest.skip(SKIP_UNIT_TEST_MESSAGE)
    def test_unclassified_with_local_route(self):
        # highway=unclassified, with route local (Grant Avenue) at zoom 12
        # part of The Barbary Coast Trail in San Francisco
        self.load_fixtures([
            'https://www.openstreetmap.org/way/91181758',
            'https://www.openstreetmap.org/relation/6322028',
        ], clip=self.tile_bbox(12, 655, 1582))

        self.assert_has_feature(
            12, 655, 1582, 'roads',
            {'kind': 'minor_road', 'walking_network': 'lwn'})

    @unittest.skip(SKIP_UNIT_TEST_MESSAGE)
    def test_secondary_with_international_route(self):
        # Strøby Bygade secondary road part of international cycle network
        # https://www.openstreetmap.org/relation/28441
        # https://www.openstreetmap.org/relation/2689634
        # https://www.openstreetmap.org/relation/2749837
        # https://www.openstreetmap.org/relation/36778
        # https://www.openstreetmap.org/relation/721738
        self.load_fixtures([
            'https://www.openstreetmap.org/way/378138944',
            'https://www.openstreetmap.org/relation/1737354',
            'https://www.openstreetmap.org/relation/28441',
            'https://www.openstreetmap.org/relation/2689634',
            'https://www.openstreetmap.org/relation/2749837',
            'https://www.openstreetmap.org/relation/36778',
            'https://www.openstreetmap.org/relation/721738',
        ], clip=self.tile_bbox(8, 136, 80))

        self.assert_has_feature(
            8, 136, 80, 'roads',
            {'kind': 'major_road', 'kind_detail': 'secondary',
             'is_bicycle_related': True, 'bicycle_network': 'icn'})

    @unittest.skip(SKIP_UNIT_TEST_MESSAGE)
    def test_teriary_with_national_route(self):
        # Sundbylillevej tertiary road part of national cycle network
        self.load_fixtures([
            'https://www.openstreetmap.org/way/28273516',
            'https://www.openstreetmap.org/relation/26863',
        ], clip=self.tile_bbox(8, 136, 79))

        self.assert_has_feature(
            8, 136, 79, 'roads',
            {'kind': 'major_road', 'kind_detail': 'tertiary',
             'is_bicycle_related': True, 'bicycle_network': 'ncn'})

    @unittest.skip(SKIP_UNIT_TEST_MESSAGE)
    def test_cycleway_with_international_route(self):
        # Way: North Sea Cycle Route - part Netherlands (1977662)
        # A really long highway=cycleway
        #         self.load_fixtures([
        #             'https://www.openstreetmap.org/way/35568189',
        #             'https://www.openstreetmap.org/relation/1977662',
        #             'https://www.openstreetmap.org/relation/1975739',
        #             'https://www.openstreetmap.org/relation/5294',
        #             'https://www.openstreetmap.org/relation/537418',
        #         ], clip=self.tile_bbox(8, 131, 83))
        import dsl
        from shapely.wkt import loads as wkt_loads
        self.generate_fixtures(
            dsl.way(35568189, dsl.tile_diagonal(13, 4211, 2670), {
                'source': 'openstreetmap.org',
                'bicycle': 'designated',
                'foot': 'designated',
                'highway': 'cycleway',
                'surface': 'asphalt'
            }),
            dsl.relation(1977662, {
                'source': 'openstreetmap.org',
                'type': 'route',
                'route': 'bicycle',
                'alt_name': 'North Sea Cycle Route - part Netherlands',
                'icn_ref': 'EV12',
                'network': 'icn',
                'ref': 'EV12',
                'name': 'EuroVelo 12 - part Netherlands',
                'name:de': 'EuroVelo 12 - Abschnitt Niederlande',
                'name:en': 'North Sea Cycle Route - part Netherlands',
                'name:pl': 'Szlak Rowerowy Morza Północnego - część Holandia',
                'wikidata': 'Q456594',
            }, ways=[35568189]),
            dsl.relation(1975739, {
                'source': 'openstreetmap.org',
                'type': 'route',
                'route': 'hiking',
                'network': 'iwn',
                'operator': 'European Ramblers Association',
                'operator:nl': 'Wandelnet',
                'ref': 'E9',
                'name': 'Europese wandelroute E9, Nederland',
                'name:de': 'Europäischer Fernwanderweg E9, Niederlande',
                'name:en': 'European walking route E9 - part Netherlands',
                'name:pl': 'Europejski długodystansowy szlak pieszy E9 - część Holandia',
                'wikidata': 'Q1377728',
            }, ways=[35568189]),
            dsl.relation(5294, {
                'source': 'openstreetmap.org',
                'type': 'route',
                'route': 'bicycle',
                'network': 'ncn',
                'ref': 'LF10',
                'name': 'Waddenzeeroute',
            }, ways=[35568189]),
            dsl.relation(537418, {
                'source': 'openstreetmap.org',
                'type': 'route',
                'route': 'bicycle',
                'network': 'ncn',
                'ref': 'LF21',
                'name': 'Zuiderzeeroute',
            }, ways=[35568189]),
        )

        self.assert_has_feature(
            8, 131, 83, 'roads',
            {'kind': 'path', 'is_bicycle_related': True,
             'bicycle_network': 'icn'})

    @unittest.skip(SKIP_UNIT_TEST_MESSAGE)
    def test_ferry_with_international_route(self):
        # Ferry between Denmark and Germany, icn
        self.load_fixtures([
            'https://www.openstreetmap.org/way/128631318',
            'https://www.openstreetmap.org/relation/721738',
        ], clip=self.tile_bbox(8, 136, 81))

        self.assert_has_feature(
            8, 136, 81, 'roads',
            {'kind': 'ferry', 'is_bicycle_related': True,
             'bicycle_network': 'icn'})

    @unittest.skip(SKIP_UNIT_TEST_MESSAGE)
    def test_minor_road_with_national_route(self):
        # Søndervangsvej minor road in Denmark as national cycle route
        self.load_fixtures([
            'https://www.openstreetmap.org/way/149701891',
            'https://www.openstreetmap.org/relation/349521',
        ], clip=self.tile_bbox(8, 136, 79))

        self.assert_has_feature(
            8, 136, 79, 'roads',
            {'kind': 'minor_road', 'is_bicycle_related': True,
             'bicycle_network': 'ncn'})

    def test_bay_trail_rcn(self):
        # Part of Bay Trail in South (San Francisco) Bay
        # way is marked rcn=yes, and part of a proper bike relation
        self.load_fixtures([
            'http://www.openstreetmap.org/way/44422697',
            'http://www.openstreetmap.org/relation/325779',
        ], clip=self.tile_bbox(13, 1313, 3172))

        # keeps bicycle_network at zoom 13
        self.assert_has_feature(
            13, 1313, 3172, 'roads',
            {'kind': 'path', 'is_bicycle_related': True,
             'bicycle_network': 'rcn'})

        # keeps is_bicycle_related at zoom 10
        self.assert_has_feature(
            10, 164, 396, 'roads',
            {'kind': 'path', 'is_bicycle_related': True,
             'bicycle_network': type(None)})

    @unittest.skip(SKIP_UNIT_TEST_MESSAGE)
    def test_residential_with_regional_route(self):
        # Hyltebjerg Allé residential road with rcn in Copenhagen
        self.load_fixtures([
            'https://www.openstreetmap.org/way/2860759',
            'https://www.openstreetmap.org/relation/2087590',
        ], clip=self.tile_bbox(10, 547, 320))

        # keep bicycle_network until 13
        self.assert_has_feature(
            13, 4379, 2563, 'roads',
            {'kind': 'minor_road', 'is_bicycle_related': True,
             'bicycle_network': 'rcn'})

        # keep the is_bicycle_related at lower zooms
        self.assert_has_feature(
            10, 547, 320, 'roads',
            {'kind': 'minor_road', 'is_bicycle_related': True,
             'bicycle_network': type(None)})

    def test_living_street_with_local_route(self):
        # lcn in Seattle - LCN only visible at zoom 16
        self.load_fixtures([
            'https://www.openstreetmap.org/way/6477775',
            'https://www.openstreetmap.org/relation/3541926',
        ], clip=self.tile_bbox(16, 10492, 22900))

        self.assert_has_feature(
            16, 10492, 22900, 'roads',
            {'kind': 'minor_road', 'bicycle_network': 'lcn'})

    def test_kirkham_street_lcn(self):
        # Kirkham Street lcn in San Francisco at zoom 16
        self.load_fixtures([
            'https://www.openstreetmap.org/way/89802424',
            'https://www.openstreetmap.org/relation/32313',
        ], clip=self.tile_bbox(16, 10471, 25334))

        self.assert_has_feature(
            16, 10471, 25334, 'roads',
            {'kind': 'minor_road', 'bicycle_network': 'lcn'})

    def test_asiatisk_plads_service_road_lcn(self):
        # Asiatisk Plads service road with lcn in Copenhagen
        self.load_fixtures([
            'https://www.openstreetmap.org/way/164049387',
            'https://www.openstreetmap.org/relation/6199242',
        ], clip=self.tile_bbox(16, 35059, 20513))

        self.assert_has_feature(
            16, 35059, 20513, 'roads',
            {'kind': 'minor_road', 'bicycle_network': 'lcn'})
