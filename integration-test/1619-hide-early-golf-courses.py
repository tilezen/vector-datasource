# -*- encoding: utf-8 -*-
from . import FixtureTest


class GolfCourseTest(FixtureTest):

    def test_golf_course_13_way(self):
        import dsl

        z, x, y = (13, 1308, 3167)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/16753068
            dsl.way(16753068, dsl.box_area(z, x, y, 1120479), {
                'addr:city': 'San Francisco',
                'addr:housenumber': '99',
                'addr:postcode': '94132',
                'addr:state': 'CA',
                'addr:street': 'Harding Road',
                'golf:course': '27_hole',
                'golf:par': '72 + 30',
                'leisure': 'golf_course',
                'name': 'TPC Harding Park',
                'phone': '415-664-4690',
                'source': 'openstreetmap.org',
                'website': 'http://www.tpc.com/tpc-harding-park-golf',
                'wikidata': 'Q3512308',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 16753068,
                'kind': 'golf_course',
                'min_zoom': 13,
            })

    def test_golf_course_12_way(self):
        import dsl

        z, x, y = (12, 1170, 1564)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/45755011
            dsl.way(45755011, dsl.box_area(z, x, y, 2696812), {
                'leisure': 'golf_course',
                'name': 'Woodmont Country Club',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 45755011,
                'kind': 'golf_course',
                'min_zoom': 12,
            })
