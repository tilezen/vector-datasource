# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class GatesLineGeometry(FixtureTest):
    def test_linear_gate(self):
        # Add barrier:gates with line geometries in landuse
        # Line barrier:ghate feature
        self.generate_fixtures(dsl.way(391260223, wkt_loads('LINESTRING (-122.419974102356 37.75523615662039, -122.419995033102 37.7552581740033, -122.420020814751 37.75527081623959)'), {u'source': u'openstreetmap.org', u'barrier': u'gate'}))  # noqa

        self.assert_has_feature(
            16, 10482, 25335, 'landuse',
            {'id': 391260223, 'kind': 'gate'})
