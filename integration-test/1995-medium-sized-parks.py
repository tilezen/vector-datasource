# -*- encoding: utf-8 -*-
import unittest

import dsl

from . import FixtureTest
from . import SKIP_UNIT_TEST_MESSAGE


class MediumSizedParks(FixtureTest):
    @unittest.skip(SKIP_UNIT_TEST_MESSAGE)
    def test_alamo_square_min_zoom_12(self):

        z, x, y = (12, 654, 1583)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/745183964
            dsl.way(745183964, dsl.box_area(z, x, y, 173000), {
                'addr:city': 'San Francisco',
                'addr:postcode': '94117',
                'addr:state': 'CA',
                'ele': '79',
                'leisure': 'park',
                'localwiki': 'sf/Alamo Square',
                'name': 'Alamo Square',
                'operator': 'San Francisco Recreation and Parks Department',
                'source': 'openstreetmap.org',
                'tourism': 'attraction',
                'wikidata': 'Q1855438',
                'wikipedia': 'en:Alamo Square, San Francisco',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 745183964,
                'kind': 'park',
                'min_zoom': 12
            })

    def test_bryant_park_min_zoom_14(self):
        import dsl

        z, x, y = (14, 4824, 6157)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/22727025
            dsl.way(22727025, dsl.box_area(z, x, y, 40000), {
                'addr:city': 'New York',
                'addr:full': 'Between 40th and 42nd Streets at 6th Avenue',
                'addr:postcode': '10018',
                'addr:state': 'NY',
                'check_date:opening_hours': '2021-11-16',
                'ele': '20',
                'gnis:county_id': '061',
                'gnis:created': '01/17/2006',
                'gnis:feature_id': '2083160',
                'gnis:state_id': '36',
                'leisure': 'park',
                'name': 'Bryant Park',
                'name:ja': u'\u30d6\u30e9\u30a4\u30a2\u30f3\u30c8\u30d1\u30fc\u30af',
                'name:ko': u'\ube0c\ub77c\uc774\uc5b8\ud2b8 \uacf5\uc6d0',
                'name:tr': 'Bryant Park',
                'opening_hours': 'Mo-Su 07:00-23:00',
                'source': 'openstreetmap.org',
                'tourism': 'attraction',
                'website': 'http://www.bryantpark.org',
                'wheelchair': 'yes',
                'wikidata': 'Q995174',
                'wikipedia': 'en:Bryant Park',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 22727025,
                'kind': 'park',
                'min_zoom': 14
            })
