# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class RoadSortKeysAeroway(FixtureTest):
    def test_runway(self):
        self.generate_fixtures(dsl.way(214484985, wkt_loads('LINESTRING (-75.86166034196658 41.136580722233, -75.86071738041289 41.13658227832178, -75.85680737330719 41.13660839354539)'), {u'source': u'openstreetmap.org', u'aeroway': u'runway', u'surface': u'grass'}))  # noqa

        self.assert_has_feature(
            16, 18957, 24538, "roads",
            {"kind": "aeroway", "kind_detail": "runway", "id": 214484985,
             "sort_rank": 76})

    def test_taxiway(self):
        self.generate_fixtures(dsl.way(115434129, wkt_loads('LINESTRING (-75.7299211479091 41.3342970935806, -75.7294168337086 41.33452865486557, -75.7286980018182 41.33485896384377, -75.7286202077146 41.33488715840641, -75.72854780350271 41.33489929960178, -75.72848608924269 41.33489929960178, -75.72842976487441 41.33489120547178)'), {u'source': u'openstreetmap.org', u'aeroway': u'taxiway'}))  # noqa

        self.assert_has_feature(
            16, 18981, 24490, "roads",
            {"kind": "aeroway", "kind_detail": "taxiway", "id": 115434129,
             "sort_rank": 75})
