# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class Whitewater(FixtureTest):
    def test_put_in_egress(self):
        self.generate_fixtures(dsl.way(3134398100, wkt_loads('POINT (-72.3809157999388 43.56597652094081)'), {u'source': u'openstreetmap.org', u'whitewater': u'put_in;egress'}))  # noqa

        self.assert_has_feature(
            16, 19591, 23939, 'pois',
            {'kind': 'put_in_egress'})

    def test_portage_way(self):
        self.generate_fixtures(dsl.way(308154534, wkt_loads('LINESTRING (-72.3802859910931 43.56679697783709, -72.38030332857809 43.56671216634889, -72.3803565986745 43.56654195720779, -72.38046574398149 43.56631498924139, -72.38063732220078 43.56617947196938)'), {u'whitewater': u'portage_way', u'lanes': u'1', u'tiger:cfcc': u'A74', u'snowplowing': u'no', u'tiger:reviewed': u'yes', u'surface': u'compacted', u'access': u'permissive', u'source': u'openstreetmap.org', u'tiger:county': u'Windsor, VT', u'highway': u'service'}))  # noqa

        self.assert_has_feature(
            13, 2448, 2992, 'roads',
            {'kind': 'portage_way'})
