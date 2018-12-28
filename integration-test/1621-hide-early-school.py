# -*- encoding: utf-8 -*-
from . import FixtureTest


class HideEarlySchoolTest(FixtureTest):

    def test_school_13(self):
        import dsl

        z, x, y = (13, 1308, 3166)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/39335805
            dsl.way(39335805, dsl.box_area(z, x, y, 103299), {
                'amenity': 'school',
                'ele': '80',
                'gnis:county_id': '075',
                'gnis:created': '01/19/1981',
                'gnis:edited': '02/15/2007',
                'gnis:feature_id': '237277',
                'gnis:state_id': '06',
                'name': 'George Washington High School',
                'operator': 'San Francisco Unified School District',
                'source': 'openstreetmap.org',
                'wikidata': 'Q5545977',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 39335805,
                'kind': 'school',
                'min_zoom': 13,
            })

    def test_school_14(self):
        import dsl

        z, x, y = (14, 2544, 6146)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/295324170
            dsl.way(295324170, dsl.box_area(z, x, y, 90009), {
                'amenity': 'school',
                'ele': '44',
                'gnis:county_id': '023',
                'gnis:created': '04/26/1996',
                'gnis:feature_id': '1682005',
                'gnis:state_id': '06',
                'name': 'McKinleyville Middle School',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 295324170,
                'kind': 'school',
                'min_zoom': 14,
            })

    def test_school_15(self):
        import dsl

        z, x, y = (15, 5233, 12667)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/162470880
            dsl.way(162470880, dsl.box_area(z, x, y, 13299), {
                'addr:city': 'San Francisco',
                'addr:country': 'US',
                'addr:housenumber': '1530',
                'addr:postcode': '94122',
                'addr:state': 'CA',
                'addr:street': '43rd Avenue',
                'amenity': 'school',
                'ele': '28',
                'fax': '(415) 759-2810',
                'gnis:feature_id': '223801',
                'grades': 'K-5',
                'name': 'Francis Scott Key Elementary School',
                'operator': 'San Francisco Unified School District',
                'phone': '(415) 759-2811',
                'source': 'openstreetmap.org',
                'url': 'http://www.francisscottkeyschool.org/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 162470880,
                'kind': 'school',
                'min_zoom': 15,
            })

    def test_school_16(self):
        import dsl

        z, x, y = (16, 10484, 25330)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/353732824
            dsl.way(353732824, dsl.box_area(z, x, y, 9069), {
                'amenity': 'school',
                'ele': '5',
                'gnis:county_id': '075',
                'gnis:created': '06/14/2000',
                'gnis:feature_id': '219093',
                'gnis:state_id': '06',
                'name': 'Bessie Carmichael Elementary School',
                'phone': '+1 (415) 355-6916',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 353732824,
                'kind': 'school',
                'min_zoom': 16,
            })

    def test_school_17_node(self):
        import dsl

        z, x, y = (16, 10477, 25332)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/358803287
            dsl.point(358803287, (-122.445249, 37.769930), {
                'amenity': 'school',
                'ele': '83',
                'gnis:county_id': '075',
                'gnis:created': '11/01/1994',
                'gnis:feature_id': '1655405',
                'gnis:state_id': '06',
                'name': "Haight Ashbury Children's Center",
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 358803287,
                'kind': 'school',
                'min_zoom': 17,
            })

    def test_kindergarten(self):
        import dsl

        z, x, y = (16, 10480, 25329)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/256908810
            dsl.way(256908810, dsl.box_area(z, x, y, 1405), {
                'amenity': 'kindergarten',
                'building': 'yes',
                'name': 'Golden Gate Kindergarten',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 256908810,
                'kind': 'kindergarten',
                'min_zoom': 17,
            })
