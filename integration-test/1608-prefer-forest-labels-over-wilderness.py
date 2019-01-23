# -*- encoding: utf-8 -*-
from . import FixtureTest


class ForestTest(FixtureTest):

    def test_lake_roosevelt_national_rec_area(self):
        import dsl

        z, x, y = (9, 87, 177)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/5908558
            dsl.way(5908558, dsl.box_area(z, x, y, 914801107), {
                'boundary': 'national_park',
                'boundary:type': 'protected_area',
                'leisure': 'nature_reserve',
                'name': 'Lake Roosevelt National Recreation Area',
                'operator': 'National Park Service',
                'ownership': 'national',
                'protect_class': '5',
                'protection_title': 'National Recreation Area',
                'source': 'openstreetmap.org',
                'type': 'boundary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5908558,
                'kind': 'nature_reserve',
                'min_zoom': 9,
            })

    def test_waterton_lakes_national_park(self):
        import dsl

        z, x, y = (8, 46, 87)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/6395476
            dsl.way(6395476, dsl.box_area(z, x, y, 1194507152), {
                'boundary': 'national_park',
                'leisure': 'nature_reserve',
                'name': 'Waterton Lakes National Park',
                'operator': 'Parks Canada',
                'protect_class': '2',
                'protection_title': 'National Park',
                'source': 'openstreetmap.org',
                'type': 'multipolygon',
                'wikidata': 'Q902778',
                'wikipedia': 'en:Waterton Lakes National Park',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 6395476,
                'kind': 'national_park',
                'min_zoom': 6,
            })

    def test_glacier_national_park(self):
        import dsl

        z, x, y = (6, 11, 22)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/1242641
            dsl.way(1242641, dsl.box_area(z, x, y, 9350484254), {
                'boundary': 'national_park',
                'boundary:type': 'protected_area',
                'leisure': 'nature_reserve',
                'name': 'Glacier National Park',
                'operator': 'United States National Park Service',
                'ownership': 'national',
                'protect_id': '2',
                'protected': 'perpetuity',
                'protection_title': 'National Park',
                'source': 'openstreetmap.org',
                'type': 'multipolygon',
                'wikidata': 'Q373567',
                'wikipedia': 'en:Glacier National Park (U.S.)',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1242641,
                'kind': 'national_park',
                'min_zoom': 6,
            })

    def test_charles_m_russell_wildlife_refuge(self):
        import dsl

        z, x, y = (9, 103, 178)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/6059779
            dsl.way(6059779, dsl.box_area(z, x, y, 8589619557), {
                'boundary': 'protected_area',
                'leisure': 'nature_reserve',
                'name': 'Charles M. Russell National Wildlife Refuge',
                'operator': 'US Fish and Wildlife Service',
                'ownership': 'national',
                'protect_class': '4',
                'protection_title': 'National Wildlife Refuge',
                'source': 'openstreetmap.org',
                'type': 'boundary',
                'wikidata': 'Q5080495',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 6059779,
                'kind': 'nature_reserve',
                'min_zoom': 9,
            })

    def test_absaroka_beartooth_wilderness(self):
        import dsl

        z, x, y = (9, 99, 183)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/6003517
            dsl.way(6003517, dsl.box_area(z, x, y, 7675407331), {
                'boundary': 'protected_area',
                'leisure': 'nature_reserve',
                'name': 'Absaroka-Beartooth Wilderness Area',
                'operator': 'US Forest Service',
                'ownership': 'national',
                'protect_class': '1b',
                'protection_title': 'Wilderness Area',
                'source': 'openstreetmap.org',
                'type': 'boundary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 6003517,
                'kind': 'nature_reserve',
                'min_zoom': 9,
            })

    def test_desert_national_wildlife_refuge(self):
        import dsl

        z, x, y = (9, 91, 199)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/5982772
            dsl.way(5982772, dsl.box_area(z, x, y, 10301141266), {
                'boundary': 'protected_area',
                'leisure': 'nature_reserve',
                'name': 'Desert National Wildlife Refuge',
                'operator': 'US Fish and Wildlife Service',
                'ownership': 'national',
                'protect_class': '4',
                'protection_title': 'National Wildlife Refuge',
                'source': 'openstreetmap.org',
                'type': 'boundary',
                'wikidata': 'Q5263981',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5982772,
                'kind': 'nature_reserve',
                'min_zoom': 9,
            })

    def test_white_sands_national_monument(self):
        import dsl

        z, x, y = (9, 104, 206)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/1504622
            dsl.way(1504622, dsl.box_area(z, x, y, 856339892), {
                'boundary': 'national_park',
                'boundary:type': 'protected_area',
                'gnis:feature_id': '914261',
                'leisure': 'nature_reserve',
                'name': 'White Sands National Monument',
                'operator': 'National Park Service',
                'ownership': 'national',
                'protect_class': '3',
                'protection_title': 'National Monument',
                'source': 'openstreetmap.org',
                'type': 'boundary',
                'website': 'http://www.nps.gov/whsa',
                'wikidata': 'Q1200164',
                'wikipedia': 'en:White Sands National Monument',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1504622,
                'kind': 'national_park',
                'min_zoom': 6,
            })

    def test_stanislaus_national_forest(self):
        import dsl

        z, x, y = (8, 42, 98)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/972008
            dsl.way(972008, dsl.box_area(z, x, y, 5882440714), {
                'attribution': 'USDA-Forest Service, Pacific Southwest Region',
                'boundary': 'national_park',
                'boundary:type': 'protected_area',
                'name': 'Stanislaus National Forest',
                'name:de': 'Nationalforst Stanislaus',
                'operator': 'United States Forest Service',
                'ownership': 'national',
                'protect_class': '6',
                'protected': 'perpetuity',
                'protection_title': 'National Forest',
                'source': 'openstreetmap.org',
                'type': 'multipolygon',
                'website': 'http://www.fs.usda.gov/stanislaus',
                'wikidata': 'Q2898163',
                'wikipedia': 'en:Stanislaus National Forest',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 972008,
                'kind': 'forest',
                'min_zoom': 7,
            })

    def test_emigrant_wilderness(self):
        import dsl

        z, x, y = (10, 171, 394)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/5366680
            dsl.way(5366680, dsl.box_area(z, x, y, 739870504), {
                'boundary': 'protected_area',
                'leisure': 'nature_reserve',
                'name': 'Emigrant Wilderness',
                'operator': 'US Forest Service',
                'ownership': 'national',
                'protect_class': '1b',
                'protection_title': 'Wilderness Area',
                'source': 'openstreetmap.org',
                'type': 'boundary',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5366680,
                'kind': 'nature_reserve',
                'min_zoom': 9,
            })

    def test_hoover_wilderness(self):
        import dsl

        z, x, y = (10, 172, 394)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/5372299
            dsl.way(5372299, dsl.box_area(z, x, y, 840685203), {
                'boundary': 'protected_area',
                'leisure': 'nature_reserve',
                'name': 'Hoover Wilderness',
                'operator': 'US Forest Service',
                'ownership': 'national',
                'protect_class': '1b',
                'protection_title': 'Wilderness Area',
                'source': 'openstreetmap.org',
                'type': 'boundary',
                'wikidata': 'Q6317507',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5372299,
                'kind': 'nature_reserve',
                'min_zoom': 9,
            })

    def test_algonquin_provincial_park(self):
        # provincial park, although a large one, isn't a national park. so
        # should appear with other parks around zoom 8.
        import dsl

        z, x, y = (8, 72, 91)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/910784
            dsl.way(910784, dsl.box_area(z, x, y, 15694581677), {
                'boundary': 'national_park',
                'date:protected': '1893',
                'governance_type': 'sub-national ministry or agency',
                'heritage': '2',
                'heritage:operator': 'hsamboc',
                'hsamboc:criteria': 'National Historic Site of Canada',
                'hsamboc:inscription_date': '1992-06-07',
                'is_in': 'Ontario',
                'is_in:zone': 'ALGONQUIN',
                'iucn_level': 'II',
                'leisure': 'nature_reserve',
                'name': 'Algonquin Provincial Park',
                'name:short': 'ALGONQUIN',
                'operator': 'Ontario Parks',
                'operator:url': 'www.ontarioparks.com/english/',
                'protect_class': '2',
                'protection_title': 'Provincial Park',
                'ref:hsamboc': '3249',
                'short_name': 'Algonquin Park',
                'site_ownership': 'national',
                'site_status': 'designated',
                'source': 'openstreetmap.org',
                'source:type': 'Provincial Park',
                'type': 'multipolygon',
                'WDPA_ID:ref': '4167',
                'website': 'http://www.ontarioparks.com/park/algonquin',
                'wikidata': 'Q1543478',
                'wikipedia': 'en:Algonquin Provincial Park',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 910784,
                'kind': 'park',
                'min_zoom': 8,
            })


class BlmTest(FixtureTest):

    def test_blm_public_lands(self):
        import dsl

        z, x, y = (9, 107, 183)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/2517672
            dsl.way(2517672, dsl.box_area(z, x, y, 1172619201), {
                'boundary': 'protected_area',
                'name': 'BLM',
                'operator': 'US Bureau of Land Management',
                'ownership': 'national',
                'protect_class': '27',
                'protection_title': 'Public Access Land',
                'source': 'openstreetmap.org',
                'type': 'multipolygon',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2517672,
                'kind': 'protected_area',
                'min_zoom': 9,
            })

    def test_okanogan_wenatchee_national_forest(self):
        import dsl

        z, x, y = (8, 42, 89)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/1447414
            dsl.way(1447414, dsl.box_area(z, x, y, 38300253290), {
                'boundary': 'national_park',
                'boundary:type': 'protected_area',
                'name': 'Okanogan-Wenatchee National Forest',
                'operator': 'United States Forest Service',
                'ownership': 'national',
                'protect_class': '6',
                'protected': 'perpetuity',
                'protection_title': 'National Forest',
                'source': 'openstreetmap.org',
                'type': 'multipolygon',
                'website': 'http://www.fs.usda.gov/okawen/',
                'wikidata': 'Q3079103',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1447414,
                'kind': 'forest',
                'min_zoom': 7,
            })

    def test_arapahoe_national_forest(self):
        import dsl

        z, x, y = (8, 52, 97)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/396026
            dsl.way(396026, dsl.box_area(z, x, y, 3218601885), {
                'attribution': 'US Forest Service',
                'boundary': 'national_park',
                'boundary:type': 'protected_area',
                'name': 'Arapaho National Forest',
                'operator': 'United States Forest Service',
                'ownership': 'national',
                'protect_class': '6',
                'protected': 'perpetuity',
                'protection_title': 'National Forest',
                'source': 'openstreetmap.org',
                'type': 'multipolygon',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 396026,
                'kind': 'forest',
                'min_zoom': 7,
            })


class ScientificProtectedAreasTest(FixtureTest):

    def test_cumberland_island_national_seashore(self):
        import dsl

        z, x, y = (9, 140, 209)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/4269033
            dsl.way(4269033, dsl.box_area(z, x, y, 202731274), {
                'boundary': 'protected_area',
                'name': 'Cumberland Island National Seashore',
                'protect_class': '1',
                'protection_title': 'National Seashore',
                'source': 'openstreetmap.org',
                'type': 'multipolygon',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4269033,
                'kind': 'protected_area',
                'min_zoom': 9,
            })

    def test_buck_island_reef(self):
        # NOTE: this is also tagged as a national monument... so should it be
        # treated as a "strict nature reserve" and held back a few zooms or
        # promoted as a national monument??? for the moment, i've taken the
        # view that it should be held back.
        import dsl

        z, x, y = (9, 164, 230)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/8973739
            dsl.way(8973739, dsl.box_area(z, x, y, 88094771), {
                'boundary': 'protected_area',
                'leisure': 'nature_reserve',
                'name': 'Buck Island Reef National Monument',
                'operator': 'National Park Service',
                'protect_class': '1a',
                'protected_area': 'nature_reserve_strict',
                'protection_title': 'National Monument',
                'seamark:name': 'Buck Island Reef NM',
                'seamark:type': 'protected_area',
                'source': 'openstreetmap.org',
                'type': 'boundary',
                'website': 'https://www.nps.gov/buis',
                'wikidata': 'Q999352',
                'wikipedia': 'en:Buck Island Reef National Monument',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 8973739,
                'kind': 'nature_reserve',
                'min_zoom': 9,
            })

    def test_little_lake_creek_wilderness(self):
        import dsl

        z, x, y = (10, 239, 420)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/209936201
            dsl.way(209936201, dsl.box_area(z, x, y, 21727129), {
                'boundary': 'protected_area',
                'landuse': 'conservation',
                'name': 'Little Lake Creek Wilderness',
                'protect_class': '1b',
                'source': 'openstreetmap.org',
                'wikidata': 'Q27973601',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 209936201,
                'kind': 'protected_area',
                'min_zoom': 10,
            })
