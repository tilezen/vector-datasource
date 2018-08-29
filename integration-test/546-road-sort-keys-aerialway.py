# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class RoadSortKeysAerialway(FixtureTest):
    def test_gondola(self):
        self.generate_fixtures(dsl.way(32051122, wkt_loads('LINESTRING (-73.8612524312483 44.35322360623517, -73.89189926564978 44.35616478273359)'), {u'source': u'openstreetmap.org', u'aerialway:capacity': u'1800', u'name': u'Cloudsplitter Gondola', u'aerialway': u'gondola', u'aerialway:occupancy': u'8'}))  # noqa

        self.assert_has_feature(
            16, 19321, 23740, "roads",
            {"kind": "aerialway", "kind_detail": "gondola", "id": 32051122,
             "sort_rank": 442})

    def test_cable_car(self):
        self.generate_fixtures(dsl.way(384371038, wkt_loads('LINESTRING (-98.18087867736098 19.05732433042759, -98.18652638555228 19.06035322854389)'), {u'aerialway:occupancy': u'40', u'aerialway:heating': u'yes', u'name': u'Telef\xe9rico de Puebla', u'aerialway': u'cable_car', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_has_feature(
            16, 14894, 29232, "roads",
            {"kind": "aerialway", "kind_detail": "cable_car", "id": 384371038,
             "sort_rank": 442})

    def test_chair_lift(self):
        self.generate_fixtures(dsl.way(113791306, wkt_loads('LINESTRING (-122.029130596965 37.06861081628058, -122.028981566459 37.06925956980519)'), {u'source': u'openstreetmap.org', u'name': u'Zip Line', u'aerialway': u'chair_lift'}))  # noqa

        self.assert_has_feature(
            16, 10553, 25492, "roads",
            {"kind": "aerialway", "kind_detail": "chair_lift", "id": 113791306,
             "sort_rank": 441})

    def test_rope_tow(self):
        self.generate_fixtures(dsl.way(209129274, wkt_loads('LINESTRING (-121.11701826806 39.14406599692289, -121.11745970019 39.14463700862707)'), {u'source': u'openstreetmap.org', u'name': u'Zip Line', u'aerialway': u'rope_tow'}))  # noqa

        self.assert_has_feature(
            16, 10719, 25012, "roads",
            {"kind": "aerialway", "kind_detail": "rope_tow", "id": 209129274,
             "sort_rank": 440})
