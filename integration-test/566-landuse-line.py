# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class LanduseLine(FixtureTest):
    def test_tree_row(self):
        self.generate_fixtures(dsl.way(207142223, wkt_loads('LINESTRING (-122.569093990362 37.86354818155019, -122.568864560639 37.86273196194777)'), {u'source': u'openstreetmap.org', u'natural': u'tree_row'}))  # noqa

        self.assert_has_feature(
            16, 10454, 25310, 'landuse',
            {'kind': 'tree_row', 'sort_rank': 264})

    def test_hedge(self):
        self.generate_fixtures(dsl.way(205644321, wkt_loads('LINESTRING (-122.401041389091 37.76760278587829, -122.401059175733 37.76777740406509)'), {u'source': u'openstreetmap.org', u'barrier': u'hedge'}))  # noqa

        self.assert_has_feature(
            16, 10485, 25332, 'landuse',
            {'kind': 'hedge', 'sort_rank': 263})
