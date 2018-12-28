# -*- encoding: utf-8 -*-
from . import FixtureTest


class HideEarlyUniversityTest(FixtureTest):

    def test_large_university(self):
        import dsl

        z, x, y = (10, 165, 399)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/309918
            dsl.way(309918, dsl.box_area(z, x, y, 14614122), {
                'amenity': 'university',
                'name': 'California State University Monterey Bay',
                'source': 'openstreetmap.org',
                'type': 'multipolygon',
                'website': 'https://csumb.edu/',
                'wikidata': 'Q624686',
                'wikipedia': 'en:California State University, Monterey Bay',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 309918,
                'kind': 'university',
                'min_zoom': 10,
            })

    def test_medium_university(self):
        import dsl

        z, x, y = (11, 328, 794)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/29268613
            dsl.way(29268613, dsl.box_area(z, x, y, 7165443), {
                'amenity': 'university',
                'ele': '22',
                'gnis:county_id': '085',
                'gnis:created': '01/19/1981',
                'gnis:edited': '01/04/2008',
                'gnis:feature_id': '235365',
                'gnis:state_id': '06',
                'name': 'Stanford University',
                'official_name': 'Leland Stanford Junior University',
                'official_name:en': 'Leland Stanford Junior University',
                'source': 'openstreetmap.org',
                'wikidata': 'Q41506',
                'wikipedia': 'en:Stanford University',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 29268613,
                'kind': 'university',
                'min_zoom': 11,
            })

    def test_college_1(self):
        import dsl

        z, x, y = (12, 658, 1585)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/124842735
            dsl.way(124842735, dsl.box_area(z, x, y, 600142), {
                'addr:street': '25555 Hesperian Blvd',
                'amenity': 'college',
                'ele': '13',
                'gnis:county_id': '001',
                'gnis:created': '01/19/1981',
                'gnis:edited': '01/04/2008',
                'gnis:feature_id': '220866',
                'gnis:state_id': '06',
                'name': 'Chabot College',
                'source': 'openstreetmap.org',
                'wikidata': 'Q5066011',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 124842735,
                'kind': 'college',
                'min_zoom': 12,
            })

    def test_college_2(self):
        import dsl

        z, x, y = (12, 658, 1582)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/31486857
            dsl.way(31486857, dsl.box_area(z, x, y, 859573), {
                'amenity': 'college',
                'name': "St. Mary's College of California",
                'source': 'openstreetmap.org',
                'wikipedia': "en:Saint Mary's College of California",
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 31486857,
                'kind': 'college',
                'min_zoom': 12,
            })
