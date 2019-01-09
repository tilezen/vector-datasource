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
