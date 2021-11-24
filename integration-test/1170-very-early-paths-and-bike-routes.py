# -*- encoding: utf-8 -*-
from . import FixtureTest


class VeryEarlyPathsAndBikeRoutes(FixtureTest):

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
            dsl.way(285975282, wkt_loads('LineString (6.81894570000000044 47.14029759999999669, 6.81851650000000031 47.1398889999999966, 6.81791570000000036 47.1393051000000014, 6.81695009999999968 47.13809369999999888, 6.81658529999999985 47.13749519999999649, 6.8161132999999996 47.13699890000000181, 6.81561970000000006 47.13641510000000068, 6.81482580000000038 47.13607929999999868, 6.81381730000000019 47.13587499999999864, 6.8127658999999996 47.13588959999999872, 6.81134970000000006 47.13583119999999838, 6.81029820000000008 47.13587499999999864, 6.80961160000000021 47.13584579999999846, 6.80901080000000025 47.1359187999999989, 6.80849689999999974 47.13581949999999665, 6.80768039999999974 47.1355829999999969, 6.80735850000000031 47.13532029999999651, 6.80708070000000021 47.13485610000000037, 6.8068660999999997 47.13430139999999824, 6.80675879999999989 47.13235989999999731, 6.80665150000000008 47.13177600000000211, 6.80645840000000035 47.13138190000000094, 6.80617840000000029 47.13121840000000162, 6.80469889999999999 47.13091469999999816, 6.80328260000000018 47.13079799999999864, 6.80210250000000016 47.13056439999999725, 6.80059940000000029 47.13007970000000313, 6.79980540000000033 47.12968560000000195, 6.7990984000000001 47.12946949999999902, 6.7982604999999996 47.12921839999999918, 6.79748909999999995 47.12930889999999806, 6.79701700000000031 47.12927969999999789, 6.79637329999999995 47.12910449999999685, 6.7960718 47.12891179999999736, 6.79574989999999968 47.12878039999999658, 6.79524569999999972 47.12887529999999714, 6.79487229999999975 47.128579000000002, 6.79409979999999969 47.12815559999999948, 6.79306989999999988 47.12755700000000303)'), {
                "highway": "footway",
                "name": "GR5-Grand Traverse de Jura",
                "source": "openstreetmap.org"
            }),
            dsl.relation(6009161, {
                "name": "European long distance path E2 - Jura",
                "name:fr": "Chemin de randonnée Européen E2 - Jura",
                "name:nl": "Europese wandelroute E2, Jura",
                "network": "iwn",
                "operator": "European Ramblers Association",
                "ref": "E2",
                "route": "foot",
                "type": "route",
                "source": "openstreetmap.org"
            }, ways=[285975282]),
        )


        self.assert_has_feature(
            9, 265, 179, 'roads',
            {'kind': 'path', 'walking_network': 'iwn'})

    def test_path_with_national_route(self):
        # highway=path, with route national (Pacific Crest Trail) at zoom 9
#         self.load_fixtures([
#             'https://www.openstreetmap.org/way/236361475',
#             'https://www.openstreetmap.org/relation/1225378',
#         ], clip=self.tile_bbox(9, 86, 197))

        import dsl
        self.generate_fixtures(
            dsl.way(236361475, dsl.tile_diagonal(9, 86, 197), {
                "ref": "PCT Section H",
                "source": "GPS",
                "motorcar": "no",
                "motorcycle": "no",
                "foot": "designated",
                "name": "Pacific Crest Trail",
                "alt_name": "Pacific Crest National Scenic Trail",
                "bicycle": "no",
                "highway": "path",
                "horse": "yes",
                "network": "nwn",
                "source": "openstreetmap.org"
            }),
            dsl.relation(1225378, {
                "name": "Pacific Crest Trail",
                "network": "nwn",
                "ref": "PCT",
                "route": "hiking",
                "type": "route",
                "wikidata": "Q2003736",
                "wikipedia": "en:Pacific Crest Trail",
                "source": "openstreetmap.org"
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
             dsl.way(35568189, wkt_loads('LineString (5.20611110000000021 53.0203684000000024, 5.20225570000000026 53.01814749999999776, 5.20133840000000003 53.01767960000000102, 5.20109159999999981 53.01755539999999911, 5.2000295000000003 53.01723590000000286, 5.19848179999999971 53.01643560000000122, 5.19116390000000028 53.01260760000000261, 5.17956600000000034 53.00652889999999928, 5.15636820000000018 52.99436250000000115, 5.14245929999999962 52.98704740000000157, 5.13548730000000031 52.98336119999999738, 5.12635620000000003 52.97859449999999981, 5.12550750000000033 52.97814499999999782, 5.12357559999999967 52.97711340000000035, 5.11780650000000037 52.9740553000000034, 5.11234319999999975 52.97123249999999928, 5.11137360000000029 52.97082439999999792, 5.11007820000000024 52.97023440000000249, 5.10912040000000012 52.96974740000000281, 5.10839659999999984 52.96936840000000046, 5.1071093000000003 52.96868380000000087, 5.10643549999999991 52.96833000000000169, 5.10612449999999995 52.96815589999999929, 5.10582579999999986 52.96797099999999858, 5.1038036 52.96672759999999869, 5.10248640000000009 52.9660340000000005, 5.09509550000000022 52.9621532999999971, 5.08968869999999995 52.95931259999999696, 5.07287130000000008 52.95045970000000324, 5.06300279999999958 52.94526559999999904, 5.06257420000000025 52.94504040000000344, 5.06130849999999999 52.94437419999999861, 5.05951370000000011 52.94342830000000077, 5.05829210000000007 52.94278479999999831, 5.05619499999999977 52.94168160000000256, 5.05398130000000023 52.94051449999999903, 5.05171740000000025 52.93933280000000252, 5.05093960000000042 52.93901509999999888, 5.05027440000000016 52.93871359999999981, 5.04894219999999994 52.9380398999999997)'), {
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
