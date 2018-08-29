# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class RemoveLanduseLabels(FixtureTest):

    def test_landuse_labels_layer_no_longer_exists(self):
        # Label placement Cemetery in landuse - note that we test the
        # label exists in the landuse layer in test 742.
        self.generate_fixtures(dsl.way(44580948, wkt_loads('POLYGON ((-119.88781887966 34.97776097546719, -119.887378884834 34.97773698001399, -119.887378884834 34.97728496619119, -119.887808908361 34.9772929892559, -119.88781887966 34.97776097546719))'), {u'tiger:AWATER': u'0', u'Tiger:MTFCC': u'K2582', u'tiger:ALAND': u'2026', u'way_area': u'3025.11', u'tiger:reviewed': u'no', u'longitude': u'-119.8875977', u'tiger:COUNTYFP': u'083', u'source': u'openstreetmap.org', u'tiger:STATEFP': u'06', u'latitude': u'+34.9775199', u'tiger:AREAID': u'110809877813', u'landuse': u'cemetery'}))  # noqa

        with self.layers_in_tile(15, 5471, 12981) as layers:
            self.assertTrue('landuse_labels' not in layers)
