# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class MissingBuildingPart(FixtureTest):
    def test_building_part_exists(self):
        self.generate_fixtures(dsl.way(287494678, wkt_loads('POLYGON ((-73.99059348282329 40.7454950572076, -73.9905764148329 40.7455184690973, -73.9904632271071 40.7454704202684, -73.99047939678222 40.74544830146149, -73.9905005071914 40.74544687224599, -73.9905184734971 40.74544809728789, -73.9905329363732 40.74545081960298, -73.99053679912889 40.7454523168762, -73.99055054335278 40.74545742121659, -73.99056797066929 40.74546558816039, -73.9905814453985 40.74547702188008, -73.99058764377401 40.7454860055155, -73.99059348282329 40.7454950572076))'), {u'building:colour': u'#F0E8D1', u'source': u'openstreetmap.org', u'building:part': u'yes', u'roof:material': u'concrete', u'way_area': u'81.1201', u'height': u'111', u'roof:shape': u'flat', u'building:material': u'glass'}))  # noqa

        self.assert_has_feature(
            16, 19298, 24632, 'buildings',
            {'kind': 'building_part',
             'id': 287494678,
             'min_zoom': 15})
