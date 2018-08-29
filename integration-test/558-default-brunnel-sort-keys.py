# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class DefaultBrunnelSortKeys(FixtureTest):
    def test_footway(self):
        self.generate_fixtures(dsl.way(70656344, wkt_loads('LINESTRING (-122.454680782852 37.79794337491749, -122.454564091697 37.79787239207469)'), {u'bridge': u'yes', u'highway': u'footway', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_has_feature(
            16, 10475, 25325, "roads",
            {"kind": "path", "kind_detail": "footway", "id": 70656344,
             "sort_rank": 404})

    def test_path(self):
        self.generate_fixtures(dsl.way(275618623, wkt_loads('LINESTRING (-122.436378058096 37.70074431240968, -122.436308438662 37.7007187960834)'), {u'bridge': u'yes', u'highway': u'path', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_has_feature(
            16, 10479, 25348, "roads",
            {"kind": "path", "kind_detail": "path", "id": 275618623,
             "sort_rank": 404})

    def test_cycleway(self):
        self.generate_fixtures(dsl.way(8915047, wkt_loads('LINESTRING (-122.488438662746 37.7125587071943, -122.48700126846 37.71289136066618)'), {u'bridge': u'yes', u'name': u'Lake Merced Bike Path', u'tiger:cfcc': u'A41', u'source': u'openstreetmap.org', u'tiger:county': u'San Francisco, CA', u'highway': u'cycleway'}))  # noqa

        self.assert_has_feature(
            16, 10469, 25345, "roads",
            {"kind": "path", "kind_detail": "cycleway", "id": 8915047,
             "sort_rank": 404})

    def test_steps(self):
        self.generate_fixtures(dsl.way(1257335719, wkt_loads('POINT (-117.92093753265 33.81130848987728)'), {u'source': u'openstreetmap.org', u'barrier': u'gate'}),dsl.way(109938341, wkt_loads('LINESTRING (-117.920943461531 33.81131625230589, -117.92093753265 33.81130848987728, -117.920926124046 33.8113000556992, -117.920905911952 33.81129169615908, -117.92087114715 33.81128169456529, -117.920854618149 33.8112802764288)'), {u'bridge': u'yes', u'name': u'Privet Enterance', u'highway': u'steps', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_has_feature(
            16, 11301, 26220, "roads",
            {"kind": "path", "kind_detail": "steps", "id": 109938341,
             "sort_rank": 404})

    def test_track(self):
        self.generate_fixtures(dsl.way(66418490, wkt_loads('LINESTRING (-117.496740928232 33.79722225378411, -117.496584082384 33.79705891717991)'), {u'bridge': u'yes', u'tiger:source': u'tiger_import_dch_v0.6_20070809', u'tiger:name_base': u'Lee Lake Water District', u'name': u'Lee Lake Water District Road', u'tiger:cfcc': u'A41', u'source': u'openstreetmap.org', u'access': u'private', u'tiger:separated': u'no', u'tiger:county': u'Riverside, CA', u'tiger:tlid': u'194814276:194868384', u'tiger:name_type': u'Rd', u'highway': u'track'}))  # noqa

        self.assert_has_feature(
            16, 11378, 26224, "roads",
            {"kind": "path", "kind_detail": "track", "id": 66418490,
             "sort_rank": 404})

    def test_footway_tunnel(self):
        self.generate_fixtures(dsl.way(97639585, wkt_loads('LINESTRING (-122.493036509865 37.7689956722224, -122.493134785557 37.76920266787728)'), {u'tunnel': u'yes', u'source': u'openstreetmap.org', u'layer': u'-1', u'surface': u'paved', u'highway': u'footway'}))  # noqa

        self.assert_has_feature(
            16, 10468, 25332, "roads",
            {"kind": "path", "kind_detail": "footway", "id": 97639585,
             "sort_rank": 304})

    def test_path_tunnel(self):
        self.generate_fixtures(dsl.way(356449810, wkt_loads('LINESTRING (-122.467281810669 37.7723095213776, -122.467322234857 37.77283497451699)'), {u'horse': u'no', u'tunnel': u'yes', u'layer': u'-1', u'surface': u'asphalt', u'source': u'openstreetmap.org', u'highway': u'path'}))  # noqa

        self.assert_has_feature(
            16, 10473, 25331, "roads",
            {"kind": "path", "kind_detail": "path", "id": 356449810,
             "sort_rank": 304})

    def test_track_tunnel(self):
        self.generate_fixtures(dsl.way(338682183, wkt_loads('LINESTRING (-122.481349967007 37.7241805108767, -122.480495489509 37.72519628659159, -122.48086873951 37.72539558901948, -122.480891826213 37.72542429420911)'), {u'FIXME': u'Tag how this passes under the parking garage (e.g. building passage)', u'bicycle': u'yes', u'tunnel': u'yes', u'source': u'openstreetmap.org', u'motor_vehicle': u'no', u'foot': u'yes', u'highway': u'track'}))  # noqa

        self.assert_has_feature(
            16, 10470, 25342, "roads",
            {"kind": "path", "kind_detail": "track", "id": 338682183,
             "sort_rank": 304})

    def test_steps_tunnel(self):
        self.generate_fixtures(dsl.way(99231479, wkt_loads('LINESTRING (-122.391070628426 37.78772178224, -122.391294219101 37.7875416737194)'), {u'tunnel': u'yes', u'source': u'openstreetmap.org', u'highway': u'steps'}))  # noqa

        self.assert_has_feature(
            16, 10487, 25328, "roads",
            {"kind": "path", "kind_detail": "steps", "id": 99231479,
             "sort_rank": 304})
