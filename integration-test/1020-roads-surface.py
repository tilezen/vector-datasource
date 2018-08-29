# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class RoadsSurface(FixtureTest):

    def test_road_surface(self):
        # Add surface properties to roads layer (at max zooms)
        # Prince St with cobblestones in Alexandria, VA
        # https://www.openstreetmap.org/way/190536019
        self.generate_fixtures(dsl.way(190536019, wkt_loads('LINESTRING (-77.0417094875735 38.8032479690508, -77.04050987734308 38.80310697696918)'), {u'tiger:name_base': u'Prince', u'name': u'Prince Street', u'tiger:cfcc': u'A41', u'tiger:zip_left': u'22314', u'tiger:zip_right': u'22314', u'tiger:reviewed': u'no', u'surface': u'cobblestone', u'source': u'openstreetmap.org', u'tiger:county': u'Alexandria, VA', u'tiger:name_type': u'St', u'oneway': u'yes', u'highway': u'residential'}))  # noqa

        self.assert_has_feature(
            15, 9371, 12546, 'roads',
            {'id': 190536019, 'kind': 'minor_road',
             'surface': 'cobblestone'})
