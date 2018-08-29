# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class CyclewayEqualsNo(FixtureTest):
    def test_centre(self):
        # Way: Grant Avenue (184956229)
        self.generate_fixtures(dsl.way(65328690, wkt_loads('POINT (-122.405056678748 37.78776849537549)'), {u'source': u'openstreetmap.org', u'turn_restrictions': u'no', u'highway': u'traffic_signals'}),dsl.way(184956229, wkt_loads('LINESTRING (-122.405056678748 37.78776849537549, -122.405140671227 37.7881806771727)'), {u'bicycle': u'yes', u'lanes': u'2', u'name': u'Grant Avenue', u'tiger:cfcc': u'A41', u'surface': u'paved', u'cycleway': u'no', u'source': u'openstreetmap.org', u'tiger:county': u'San Francisco, CA', u'tiger:name_type': u'Ave', u'oneway': u'no', u'turn:lanes:backward': u'right', u'lanes:backward': u'1', u'sidewalk': u'both', u'lanes:forward': u'1', u'highway': u'secondary'}))  # noqa

        self.assert_no_matching_feature(
            16, 10484, 25327, 'roads',
            {'cycleway': 'no'})

    def test_left(self):
        # Way: Wedge Parkway (263563960)
        self.generate_fixtures(dsl.way(263563960, wkt_loads('LINESTRING (-119.761154538137 39.40182560413608, -119.760988619304 39.40192486611568, -119.760863663648 39.40200462266687)'), {u'name_1': u'County Road 52', u'bicycle': u'yes', u'name': u'Wedge Parkway', u'source': u'openstreetmap.org', u'surface': u'asphalt', u'access': u'yes', u'cycleway:right': u'lane', u'maxspeed': u'35 mph', u'motor_vehicle': u'yes', u'foot': u'yes', u'lanes': u'1', u'sidewalk': u'separate', u'highway': u'tertiary', u'cycleway:left': u'no'}))  # noqa

        self.assert_no_matching_feature(
            16, 10966, 24952, 'roads',
            {'cycleway_left': 'no'})

        self.assert_has_feature(
            16, 10966, 24952, 'roads',
            {'cycleway_right': 'lane'})

    def test_right(self):
        # Way: Wedge Parkway (263563950)
        self.generate_fixtures(dsl.way(263563950, wkt_loads('LINESTRING (-119.765746007218 39.39833065944239, -119.765556642356 39.39856737271308)'), {u'name_1': u'County Road 52', u'bicycle': u'yes', u'name': u'Wedge Parkway', u'source': u'openstreetmap.org', u'surface': u'asphalt', u'access': u'yes', u'cycleway:right': u'no', u'maxspeed': u'35 mph', u'motor_vehicle': u'yes', u'foot': u'yes', u'lanes': u'1', u'sidewalk': u'separate', u'highway': u'tertiary', u'cycleway:left': u'lane'}))  # noqa

        self.assert_no_matching_feature(
            16, 10965, 24952, 'roads',
            {'cycleway_right': 'no'})

        self.assert_has_feature(
            16, 10965, 24952, 'roads',
            {'cycleway_left': 'lane'})
