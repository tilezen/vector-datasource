# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class BicycleRamps(FixtureTest):

    def test_ramp_properties_on_path(self):
        # Add ramp properties to paths in roads layer
        # Steps with ramp:bicycle=yes in Copenhagen
        self.generate_fixtures(dsl.way(1059654327, wkt_loads('POINT (12.5654789653828 55.6710021120983)'), {u'source': u'openstreetmap.org', u'layer': u'-1'}),dsl.way(91275149, wkt_loads('LINESTRING (12.5654789653828 55.6710021120983, 12.5655751749497 55.6707845776341)'), {u'step_count': u'36', u'layer': u'-1', u'handrail': u'yes', u'wheelchair': u'no', u'source': u'openstreetmap.org', u'ramp:bicycle': u'yes', u'highway': u'steps'}))  # noqa

        self.assert_has_feature(
            15, 17527, 10257, 'roads',
            {'id': 91275149, 'kind': 'path', 'kind_detail': 'steps',
             'is_bicycle_related': True, 'ramp_bicycle': 'yes'})

    def test_ramp_properties_on_footway(self):
        # Footway with ramp=yes in San Francisco
        self.generate_fixtures(dsl.way(3527029688, wkt_loads('POINT (-122.482511129344 37.7237613643332)'), {u'source': u'openstreetmap.org', u'entrance': u'yes'}),dsl.way(346088008, wkt_loads('LINESTRING (-122.48252208879 37.72357186298978, -122.482525232894 37.72364241978959, -122.482500619055 37.7236557779677, -122.482318800041 37.72366068070269, -122.482317991558 37.72368512331858, -122.48251912435 37.72373500328299, -122.482511129344 37.7237613643332)'), {u'source': u'openstreetmap.org', u'ramp': u'yes', u'highway': u'footway'}))  # noqa

        self.assert_has_feature(
            16, 10470, 25342, 'roads',
            {'id': 346088008, 'kind': 'path', 'kind_detail': 'footway',
             'ramp': 'yes'})
