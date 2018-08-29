# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class MotorwayLinkZ11(FixtureTest):
    def test_motorway_link_until_zoom_11(self):
        z, x, y = 11, 327, 791

        self.generate_fixtures(dsl.way(8915478, wkt_loads('LINESTRING (-122.406862472132 37.734545870453, -122.407111934286 37.73462970195289, -122.40739894602 37.7347028768287, -122.407687215394 37.73474848676319, -122.407939282663 37.73477285467619, -122.408226294396 37.73478031423981, -122.408474409078 37.73476965772019, -122.40874668844 37.73474209284889, -122.409002798128 37.7346954172573, -122.409246870391 37.73464128205939, -122.409486181582 37.73457052260729)'), {u'bridge': u'yes', u'layer': u'3', u'bicycle': u'no', u'tiger:cfcc': u'A63', u'destination': u'Daly City', u'source': u'openstreetmap.org', u'tiger:county': u'San Francisco, CA', u'oneway': u'yes', u'lanes': u'2', u'destination:ref': u'I 280 South', u'highway': u'motorway_link'}))  # noqa

        self.assert_has_feature(
            z, x, y, 'roads',
            {'kind': 'highway',
             'is_link': True,
             'kind_detail': 'motorway_link'})

        self.assert_no_matching_feature(
            z - 1, x / 2, y / 2, 'roads',
            {'kind': 'highway',
             'is_link': True,
             'kind_detail': 'motorway_link'})
