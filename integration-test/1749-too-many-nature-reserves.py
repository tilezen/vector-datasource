# -*- encoding: utf-8 -*-
from . import FixtureTest


class NatureReserveTest(FixtureTest):

    def test_nature_reserve_15_way(self):
        import dsl

        z, x, y = (16, 19788, 24194)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/105703183
            dsl.way(105703183, dsl.box_area(z, x, y, 7057), {
                'access': 'yes',
                'landuse': 'conservation',
                'leisure': 'nature_reserve',
                'massgis:ARTICLE97': '0',
                'massgis:ASSESS_ACR': '1.25000000',
                'massgis:ASSESS_BLK': '35',
                'massgis:ASSESS_MAP': '76',
                'massgis:ATT_DATE': '1997/12/15',
                'massgis:BASE_MAP': '31-12',
                'massgis:CAL_DATE_R': '1/1/1991',
                'massgis:DCAM_ID': '0',
                'massgis:DEED_ACRES': '0.00000000',
                'massgis:EOEAINVOLV': '0',
                'massgis:FEE_OWNER': 'Sudbury Valley Trustees',
                'massgis:FEESYM': 'L',
                'massgis:FY_FUNDING': '0',
                'massgis:LEV_PROT': 'P',
                'massgis:OS_DEED_BO': '5749',
                'massgis:OS_DEED_PA': '191',
                'massgis:OS_ID': '31-6392',
                'massgis:OWNER_ABRV': 'SVT',
                'massgis:OWNER_TYPE': 'L',
                'massgis:POLY_ID': '6392',
                'massgis:PRIM_PURP': 'C',
                'massgis:PUB_ACCESS': 'Y',
                'massgis:SITE_NAME': 'JUG ISLAND',
                'massgis:SOURCE_MAP': 'USGSB1',
                'massgis:TOWN_ID': '31',
                'name': 'Jug Island',
                'owner': 'Sudbury Valley Trustees',
                'ownership': 'land_trust',
                'place': 'islet',
                'protected': 'perpetuity',
                'source': 'openstreetmap.org',
                'start_date': '1991',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 105703183,
                'kind': 'nature_reserve',
                'min_zoom': 15,
            })

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 105703183,
                'kind': 'nature_reserve',
                'min_zoom': 16,
                'name': 'Jug Island',
            })
