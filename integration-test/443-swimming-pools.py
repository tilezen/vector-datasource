# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class SwimmingPools(FixtureTest):

    def test_amenity_swimming_pool(self):
        # Bayonne Municipal Pool, amenity=swimming_pool
        self.generate_fixtures(dsl.way(361100118, wkt_loads('POLYGON ((-74.1298780761098 40.6627944152586, -74.12941041317291 40.6634303170169, -74.12865852328009 40.6631120943273, -74.12912609638551 40.66247618953508, -74.1298780761098 40.6627944152586))'), {u'amenity': u'swimming_pool', u'name': u'Bayonne Municipal Pool', u'way_area': u'10242.3', u'source': u'openstreetmap.org', u'covered': u'no', u'sport': u'swimming'}))  # noqa

        self.assert_has_feature(
            16, 19273, 24652, 'water',
            {'kind': 'swimming_pool'})

    def test_leisure_swimming_pool(self):
        # McCarren Park Swimming Pool, leisure=swimming_pool
        self.generate_fixtures(dsl.way(118987681, wkt_loads('POLYGON ((-73.94979927897241 40.72060267284089, -73.94921357740721 40.72065768412269, -73.94906625370058 40.71975591548219, -73.94965186543429 40.7197009034551, -73.94979927897241 40.72060267284089))'), {u'source': u'openstreetmap.org', u'way_area': u'8767.63', u'name': u'McCarren Park Swimming Pool', u'leisure': u'swimming_pool'}))  # noqa

        self.assert_has_feature(
            16, 19305, 24638, 'water',
            {'kind': 'swimming_pool'})
