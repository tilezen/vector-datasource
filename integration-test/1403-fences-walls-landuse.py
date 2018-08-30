# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class FencesWalls(FixtureTest):

    def test_long_wall(self):
        self.generate_fixtures(dsl.way(1736599953, wkt_loads('POINT (-122.511352978845 37.77135482027317)'), {u'source': u'openstreetmap.org', u'barrier': u'entrance'}),dsl.way(1736599954, wkt_loads('POINT (-122.511508207726 37.77263487672119)'), {u'source': u'openstreetmap.org', u'barrier': u'entrance'}),dsl.way(1736599956, wkt_loads('POINT (-122.511856574393 37.77544840934478)'), {u'source': u'openstreetmap.org', u'barrier': u'entrance'}),dsl.way(2992158522, wkt_loads('POINT (-122.511303212178 37.77093388157529)'), {u'source': u'openstreetmap.org', u'barrier': u'entrance'}),dsl.way(2992158524, wkt_loads('POINT (-122.511412986306 37.77181857435369)'), {u'source': u'openstreetmap.org', u'barrier': u'entrance'}),dsl.way(2992158525, wkt_loads('POINT (-122.511462842804 37.77222828882918)'), {u'source': u'openstreetmap.org', u'barrier': u'entrance'}),dsl.way(2992158527, wkt_loads('POINT (-122.511567586366 37.77310025592669)'), {u'source': u'openstreetmap.org', u'barrier': u'entrance'}),dsl.way(2992158528, wkt_loads('POINT (-122.511615376739 37.77345621152629)'), {u'source': u'openstreetmap.org', u'barrier': u'entrance'}),dsl.way(2992158529, wkt_loads('POINT (-122.51165831621 37.77381287547209)'), {u'source': u'openstreetmap.org', u'barrier': u'entrance'}),dsl.way(2992158530, wkt_loads('POINT (-122.511707993045 37.77422328895248)'), {u'source': u'openstreetmap.org', u'barrier': u'entrance'}),dsl.way(2992158531, wkt_loads('POINT (-122.511759017353 37.77462887180089)'), {u'source': u'openstreetmap.org', u'barrier': u'entrance'}),dsl.way(2992158532, wkt_loads('POINT (-122.511809323009 37.7750368665881)'), {u'source': u'openstreetmap.org', u'barrier': u'entrance'}),dsl.way(2992169634, wkt_loads('POINT (-122.51190750887 37.77586016282258)'), {u'source': u'openstreetmap.org', u'barrier': u'entrance'}),dsl.way(2992169636, wkt_loads('POINT (-122.511947394068 37.77615880514149)'), {u'source': u'openstreetmap.org', u'barrier': u'entrance'}),dsl.way(295483721, wkt_loads('LINESTRING (-122.511969492624 37.77635640827611, -122.511947394068 37.77615880514149, -122.51190750887 37.77586016282258, -122.511856574393 37.77544840934478, -122.511809323009 37.7750368665881, -122.511759017353 37.77462887180089, -122.511707993045 37.77422328895248, -122.51165831621 37.77381287547209, -122.511615376739 37.77345621152629, -122.511567586366 37.77310025592669, -122.511508207726 37.77263487672119, -122.511462842804 37.77222828882918, -122.511412986306 37.77181857435369, -122.511352978845 37.77135482027317, -122.511303212178 37.77093388157529, -122.511268986366 37.77058877822358, -122.511294229025 37.77048375571108, -122.511324681913 37.77042069952647, -122.511345971986 37.7703822835138, -122.511365106101 37.77032966561547, -122.511376604537 37.7702744203325, -122.511384689374 37.77016371661427)'), {u'source': u'openstreetmap.org', u'barrier': u'wall'}))  # noqa

        self.assert_has_feature(
            16, 10465, 25331, 'landuse',
            {'id': 295483721, 'kind': 'wall', 'min_zoom': 16})

    def test_wall_kind_detail_from_wall_col(self):
        self.generate_fixtures(dsl.way(526327448, wkt_loads('LINESTRING (-121.898961478361 37.1606955709096, -121.899014478963 37.16068669365728, -121.899056789612 37.16065970393998, -121.899079067832 37.16062040059451, -121.899076822043 37.16057730291339, -121.899050321742 37.1605395745246, -121.899005316147 37.16051559157309, -121.898951596893 37.16051036543639, -121.898900572585 37.16052511316369, -121.898863472163 37.16055646997238, -121.898848290635 37.16059792107618, -121.898858082272 37.16064030283759, -121.898890960611 37.16067466641039)'), {u'wall': u'dry_stone', u'source': u'openstreetmap.org', u'barrier': u'wall', u'height': u'0.5'}))  # noqa

        self.assert_has_feature(
            16, 10576, 25471, 'landuse',
            {'id': 526327448, 'kind': 'wall', 'kind_detail': 'dry_stone',
             'min_zoom': 16})

    def test_fence_kind_detail_from_fence_type_col(self):
        self.generate_fixtures(dsl.way(231049157, wkt_loads('LINESTRING (-122.007559801205 37.7572282060895, -122.008053066127 37.7569186209177, -122.009316546574 37.75615150603488, -122.01100313352 37.75508906612929, -122.011098085446 37.75420488347088, -122.011953191765 37.75436788524539)'), {u'source': u'openstreetmap.org', u'fence_type': u'barbed_wire', u'barrier': u'fence'}))  # noqa

        self.assert_has_feature(
            16, 10556, 25335, 'landuse',
            {'id': 231049157, 'kind': 'fence', 'kind_detail': 'barbed_wire',
             'min_zoom': 16})
