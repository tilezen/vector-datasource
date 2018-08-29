# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class Funicular(FixtureTest):
    def test_funicular(self):
        self.generate_fixtures(dsl.way(393550019, wkt_loads('LINESTRING (-122.424982928717 37.71021708581208, -122.425064316082 37.7100604539297)'), {u'source': u'openstreetmap.org', u'railway': u'funicular'}))  # noqa

        self.assert_has_feature(
            16, 10481, 25345, 'roads',
            {'kind': 'rail', 'kind_detail': 'funicular'})
