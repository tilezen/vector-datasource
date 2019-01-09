# -*- encoding: utf-8 -*-
from . import FixtureTest


class ParkTest(FixtureTest):

    def test_henry_coe_state_park(self):
        import dsl

        z, x, y = (11, 333, 795)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/318202
            dsl.way(318202, dsl.box_area(z, x, y, 560913461), {
                'attribution': 'CASIL CSP_Opbdys072008',
                'boundary': 'national_park',
                'csp:globalid': '{4BE5C08F-9239-4491-9400-5B776F304A18}',
                'csp:unitcode': '432',
                'leisure': 'nature_reserve',
                'name': 'Henry W. Coe State Park',
                'park:type': 'state_park',
                'protect_class': '5',
                'short_name': 'Coe Park',
                'source': 'openstreetmap.org',
                'type': 'multipolygon',
                'wikidata': 'Q5729631',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 318202,
                'kind': 'park',
            })

    def test_lake_district_national_park(self):
        import dsl

        z, x, y = (9, 251, 163)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/287917
            dsl.way(287917, dsl.box_area(z, x, y, 6990909071), {
                'area': 'yes',
                'boundary': 'national_park',
                'designation': 'national_park',
                'name': 'Lake District National Park',
                'name:cy': 'Parc Cenedlaethol Ardal y Llynnoedd',
                'name:en': 'Lake District National Park',
                'ref:gss': 'E26000003',
                'source': 'openstreetmap.org',
                'source:ref:gss': 'ONS_OpenData',
                'type': 'boundary',
                'wikidata': 'Q211778',
            }),
        )

        # this is a national park, and should be tagged as such.
        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 287917,
                'kind': 'national_park',
            })

    def test_north_pennines_aonb(self):
        import dsl

        z, x, y = (9, 252, 162)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/6576894
            dsl.way(6576894, dsl.box_area(z, x, y, 5946792285), {
                'boundary': 'national_park',
                'designation': 'area_of_outstanding_natural_beauty',
                'name': 'North Pennines AONB',
                'note': 'not a true national park',
                'source': 'openstreetmap.org',
                'type': 'boundary',
                'wikidata': 'Q1332452',
            }),
        )

        # this is a large AONB - but not technically a national park, as the
        # helpful note in the OSM data points out.
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 6576894,
                'kind': 'park',
            })
