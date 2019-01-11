# -*- encoding: utf-8 -*-
from . import FixtureTest


class CommonTest(FixtureTest):

    def test_blithedale_summit_landuse(self):
        import dsl

        z, x, y = (13, 1307, 3162)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/297452972
            dsl.way(297452972, dsl.box_area(z, x, y, 4142889), {
                'boundary': 'national_park',
                'boundary:type': 'protected_area',
                'leisure': 'common',
                'name': 'Blithedale Summit Open Space Preserve',
                'operator': 'Marin County Parks',
                'protect_class': '5',
                'protection_title': 'Open Space Preserve',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 297452972,
                'kind': 'common',
            })

    def test_blithedale_summit_poi(self):
        import dsl

        z, x, y = (13, 1307, 3162)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/297452972
            dsl.way(297452972, dsl.box_area(z, x, y, 4142889), {
                'boundary': 'national_park',
                'boundary:type': 'protected_area',
                'leisure': 'common',
                'name': 'Blithedale Summit Open Space Preserve',
                'operator': 'Marin County Parks',
                'protect_class': '5',
                'protection_title': 'Open Space Preserve',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 297452972,
                'kind': 'common',
            })
