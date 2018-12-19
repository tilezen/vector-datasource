# -*- encoding: utf-8 -*-
from . import FixtureTest


class HideEarlyNursingHomeTest(FixtureTest):

    def test_nursing_home_area(self):
        import dsl

        z, x, y = (15, 5237, 12667)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/267296981
            dsl.way(267296981, dsl.tile_box(z, x, y), {
                'addr:city': u'San Francisco',
                'addr:country': u'US',
                'addr:housenumber': u'1575',
                'addr:postcode': u'94122',
                'addr:state': u'CA',
                'addr:street': u'7th Avenue',
                'amenity': u'nursing_home',
                'building': u'yes',
                'height': u'5',
                'name': (u'Kindred Transitional Care and Rehabilitation - '
                         u'Lawton'),
                'phone': u'+1 (415) 566-1200',
                'source': u'openstreetmap.org',
                'website': u'http://www.lawtonhealthcare.com',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 267296981,
                'kind': u'nursing_home',
                'min_zoom': 15,
            })
