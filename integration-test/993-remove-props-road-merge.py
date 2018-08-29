# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class RemovePropsRoadMerge(FixtureTest):
    # NOTE: fixtures load up a single element, so this doesn't actually test
    # merging itself, only that we drop the properties (which can lead to
    # more merges).

    def test_drop_oneway_but_not_bridge(self):
        # Way: I 81 (302933871)
        #
        # testing that it dropped oneway, but hasn't dropped is_bridge.
        self.generate_fixtures(dsl.way(302933871, wkt_loads('LINESTRING (-81.2011780289799 36.92756280303799, -81.2006921302427 36.92767030393928)'), {u'bridge': u'yes', u'horse': u'no', u'maxspeed': u'70 mph', u'lanes': u'2', u'tiger:cfcc': u'A15', u'source': u'openstreetmap.org', u'hgv': u'designated', u'tiger:reviewed': u'no', u'layer': u'1', u'tiger:name_base_1': u'United States Highway 52', u'tiger:name_base': u'I-81', u'oneway': u'yes', u'foot': u'no', u'bicycle': u'no', u'sidewalk': u'none', u'ref': u'I 81', u'tiger:county': u'Wythe, VA', u'highway': u'motorway'}))  # noqa

        self.assert_has_feature(
            14, 4496, 6381, 'roads',
            {'kind': 'highway', 'oneway': type(None), 'is_bridge': True})

    def test_drop_crossing(self):
        self.generate_fixtures(dsl.way(4324682054, wkt_loads('POINT (-71.5924171338517 42.24481519215379)'), {u'crossing': u'uncontrolled', u'source': u'openstreetmap.org'}),dsl.way(434308106, wkt_loads('LINESTRING (-71.5923849741645 42.24490051209801, -71.5924171338517 42.24481519215379, -71.5924668106869 42.24471191696178)'), {u'crossing': u'zebra', u'source': u'openstreetmap.org', u'surface': u'concrete', u'highway': u'pedestrian'}))  # noqa

        self.assert_has_feature(
            14, 4933, 6066, 'roads',
            {'kind': 'path', 'crossing': type(None)})

    def test_drop_sidewalk(self):
        # Way: The Embarcadero (397140734)
        self.generate_fixtures(dsl.way(65373362, wkt_loads('POINT (-122.394582771693 37.79601559864509)'), {u'source': u'openstreetmap.org', u'highway': u'crossing'}),dsl.way(397140734, wkt_loads('LINESTRING (-122.394459971993 37.79588101160508, -122.394582771693 37.79601559864509)'), {u'tiger:name_base': u'The Embarcadero', u'maxspeed': u'30 mph', u'lanes': u'4', u'name': u'The Embarcadero', u'lcn_ref': u'4', u'source': u'openstreetmap.org', u'turn:lanes': u'left||', u'surface': u'asphalt', u'lit': u'yes', u'cycleway:right': u'lane', u'tiger:county': u'San Francisco, CA', u'oneway': u'yes', u'sidewalk': u'separate', u'tiger:cfcc': u'A45', u'highway': u'primary'}))  # noqa

        self.assert_has_feature(
            14, 2621, 6331, 'roads',
            {'name': 'The Embarcadero', 'kind': 'major_road'})

        self.assert_no_matching_feature(
            14, 2621, 6331, 'roads',
            {'name': 'The Embarcadero', 'kind': 'major_road',
             'sidewalk': None})

    def test_drop_sidewalk_left_and_right(self):
        # Way: Carrie Furnace Boulevard (438362919)
        self.generate_fixtures(dsl.way(438362919, wkt_loads('LINESTRING (-79.8826816097629 40.41101322070767, -79.8831899663821 40.41135651420059, -79.88400851126899 40.41189241516631, -79.88584332023679 40.41295517589352, -79.8870018774588 40.41360549127349, -79.8875516464127 40.4139608092326, -79.8877082227667 40.4140138844779, -79.88778934063679 40.41404137962718)'), {u'maxspeed': u'25 mph', u'lanes': u'2', u'name': u'Carrie Furnace Boulevard', u'sidewalk:left': u'sidepath', u'lit': u'yes', u'source': u'openstreetmap.org', u'sidewalk:right': u'no', u'lanes:backward': u'1', u'lanes:forward': u'1', u'highway': u'tertiary'}))  # noqa

        self.assert_has_feature(
            14, 4556, 6178, 'roads',
            {'name': 'Carrie Furnace Blvd.', 'kind': 'major_road'})

        self.assert_no_matching_feature(
            14, 4556, 6178, 'roads',
            {'name': 'Carrie Furnace Blvd.', 'kind': 'major_road',
             'sidewalk_left': None, 'sidewalk_right': None})
