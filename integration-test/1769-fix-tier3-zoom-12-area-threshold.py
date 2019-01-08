# -*- encoding: utf-8 -*-
from . import FixtureTest


class LanduseTest(FixtureTest):

    def test_tier1_national_park(self):
        import dsl

        z, x, y = (12, 655, 1582)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/82207054
            dsl.way(82207054, dsl.box_area(z, x, y, 421901), {
                'admin_level': '1',
                'boundary': 'national_park',
                'leisure': 'park',
                'name': 'Fort Mason',
                'operator': 'U.S. National Park Service',
                'source': 'openstreetmap.org',
                'website': 'http://www.nps.gov/goga/index.htm',
                'wikidata': 'Q948933',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 82207054,
                'kind': 'national_park',
                'min_zoom': 12,
                'tier': 1,
            })

    def test_tier3_university(self):
        import dsl

        z, x, y = (12, 657, 1581)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/109193723
            dsl.way(109193723, dsl.box_area(z, x, y, 289389), {
                'amenity': 'university',
                'name': 'University of California, Berkeley - '
                'Clark Kerr Campus',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 109193723,
                'kind': 'university',
                'min_zoom': 12,
                'tier': 3,
            })

    def test_tier4_hospital(self):
        import dsl

        z, x, y = (12, 703, 1638)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/571388052
            dsl.way(571388052, dsl.box_area(z, x, y, 264897), {
                'addr:city': 'Long Beach',
                'addr:housenumber': '2801',
                'addr:postcode': '90806',
                'addr:street': 'Atlantic Avenue',
                'amenity': 'hospital',
                'emergency': 'yes',
                'healthcare': 'hospital',
                'name': 'Long Beach Memorial Hospital',
                'opening_hours': '24/7',
                'operator': 'MemorialCare',
                'phone': '+1 562 933 2000',
                'source': 'openstreetmap.org',
                'wikidata': 'Q6672309',
                'wikipedia': 'en:Long Beach Memorial Medical Center',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 571388052,
                'kind': 'hospital',
                'min_zoom': 12,
                'tier': 4,
            })
