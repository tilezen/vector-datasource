# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class CrosswalkSidewalk(FixtureTest):
    def test_crossing_traffic_signals(self):
        self.generate_fixtures(dsl.way(444491374, wkt_loads('LINESTRING (-122.458564020163 37.7673278980966, -122.458563481173 37.76727818952789, -122.458562313364 37.76720618305619, -122.458560965891 37.76712288554148)'), {u'bicycle': u'dismount', u'footway': u'crossing', u'surface': u'asphalt', u'source': u'openstreetmap.org', u'crossing': u'traffic_signals', u'kerb': u'yes', u'highway': u'footway'}))  # noqa

        self.assert_has_feature(
            16, 10475, 25332, 'roads',
            {'id': 444491374, 'kind': 'path', 'crossing': 'traffic_signals'})

    def test_major_road_sidewalk_separate(self):
        # Way: The Embarcadero (397140734)
        self.generate_fixtures(dsl.way(65373362, wkt_loads('POINT (-122.394582771693 37.79601559864509)'), {u'source': u'openstreetmap.org', u'highway': u'crossing'}),dsl.way(397140734, wkt_loads('LINESTRING (-122.394459971993 37.79588101160508, -122.394582771693 37.79601559864509)'), {u'tiger:name_base': u'The Embarcadero', u'maxspeed': u'30 mph', u'lanes': u'4', u'name': u'The Embarcadero', u'lcn_ref': u'4', u'source': u'openstreetmap.org', u'turn:lanes': u'left||', u'surface': u'asphalt', u'lit': u'yes', u'cycleway:right': u'lane', u'tiger:county': u'San Francisco, CA', u'oneway': u'yes', u'sidewalk': u'separate', u'tiger:cfcc': u'A45', u'highway': u'primary'}))  # noqa

        self.assert_has_feature(
            16, 10486, 25326, 'roads',
            {'id': 397140734, 'kind': 'major_road', 'sidewalk': 'separate'})

    def test_major_road_no_sidewalk_right(self):
        # Way: Carrie Furnace Boulevard (438362919)
        self.generate_fixtures(dsl.way(438362919, wkt_loads('LINESTRING (-79.8826816097629 40.41101322070767, -79.8831899663821 40.41135651420059, -79.88400851126899 40.41189241516631, -79.88584332023679 40.41295517589352, -79.8870018774588 40.41360549127349, -79.8875516464127 40.4139608092326, -79.8877082227667 40.4140138844779, -79.88778934063679 40.41404137962718)'), {u'maxspeed': u'25 mph', u'lanes': u'2', u'name': u'Carrie Furnace Boulevard', u'sidewalk:left': u'sidepath', u'lit': u'yes', u'source': u'openstreetmap.org', u'sidewalk:right': u'no', u'lanes:backward': u'1', u'lanes:forward': u'1', u'highway': u'tertiary'}))  # noqa

        self.assert_has_feature(
            16, 18225, 24712, 'roads',
            {'id': 438362919, 'kind': 'major_road',
             'sidewalk_left': 'sidepath', 'sidewalk_right': 'no'})
