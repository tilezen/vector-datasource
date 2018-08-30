# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class RoadsAccess(FixtureTest):

    def test_restricted_access(self):
        # Add surface properties to roads layer (at max zooms)
        # restricted access road in military base, Kraków, Poland
        self.generate_fixtures(dsl.way(43322699, wkt_loads('LINESTRING (19.91692410916029 50.08136991321498, 19.9166161666809 50.08011381643398, 19.9154504229367 50.08025026507099, 19.9149552715521 50.07862029240179, 19.9145364769667 50.07867229097101, 19.9143010285307 50.07870376679587, 19.91417310843419 50.0787363955596, 19.9140622563282 50.0787813609573, 19.9139710773268 50.07883399347819, 19.9139009189031 50.078897463725, 19.9138471098176 50.07897361638069, 19.91382447227249 50.07903207110028, 19.9138019245588 50.07914869208819, 19.9137963550041 50.0792332608624, 19.9137690462194 50.0793369107312, 19.9137153269654 50.07942851212509, 19.9136439109004 50.07951417569938, 19.913532160479 50.07960698734)'), {u'access': u'private', u'source': u'openstreetmap.org', u'highway': u'service'}))  # noqa

        self.assert_has_feature(
            16, 36393, 22203, 'roads',
            {'id': 43322699, 'kind': 'minor_road', 'kind_detail': 'service',
             'access': 'private'})

        self.assert_has_feature(
            14, 9098, 5550, 'roads',
            {'id': 43322699, 'kind': 'minor_road', 'kind_detail': 'service',
             'access': 'private'})

    def test_no_access(self):
        # motorway bridge in Honk-Kong
        # ID may get dropped due to a merge with the other carriageway
        self.generate_fixtures(dsl.way(276506948, wkt_loads('LINESTRING (113.946219477016 22.48987718363269, 113.946440911733 22.4892435633672, 113.946573772564 22.48891820313059, 113.946835272143 22.48832508273119, 113.947111863419 22.487783171317, 113.947547905658 22.48686318696448)'), {u'bridge': u'yes', u'layer': u'2', u'goods': u'permit', u'lanes': u'2', u'name': u'\u6df1\u6e2f\u897f\u90e8\u901a\u9053 Hong Kong\u2013Shenzhen Western Corridor', u'hgv': u'permit', u'name:zh': u'\u6df1\u6e2f\u897f\u90e8\u901a\u9053', u'alt_name:en': u'Shenzhen Bay Bridge', u'access': u'no', u'source': u'openstreetmap.org', u'name:en': u'Hong Kong\u2013Shenzhen Western Corridor', u'alt_name:zh': u'\u6df1\u5733\u7063\u516c\u8def\u5927\u6a4b', u'alt_name': u'\u6df1\u5733\u7063\u516c\u8def\u5927\u6a4b Shenzhen Bay Bridge', u'oneway': u'yes', u'ref': u'10', u'start_date': u'2007-07-01', u'highway': u'motorway'}))  # noqa

        self.assert_has_feature(
            12, 3344, 1785, 'roads',
            {'kind': 'highway', 'kind_detail': 'motorway',
             'alt_name:en': 'Shenzhen Bay Bridge', 'access': 'no'})

    def test_access_yes(self):
        # cycleway in Gdańsk, Poland
        self.generate_fixtures(dsl.way(1988099751, wkt_loads('POINT (18.6106772968205 54.32720157959729)'), {u'source': u'openstreetmap.org', u'bicycle': u'yes', u'highway': u'crossing'}),dsl.way(1988099752, wkt_loads('POINT (18.6106279793114 54.3272640757605)'), {u'source': u'openstreetmap.org', u'bicycle': u'yes', u'highway': u'crossing'}),dsl.way(151351130, wkt_loads('LINESTRING (18.6107030784692 54.3271706719878, 18.6106772968205 54.32720157959729, 18.6106279793114 54.3272640757605, 18.6105730024161 54.32730430794268)'), {u'bicycle': u'yes', u'segregated': u'yes', u'surface': u'paving_stones', u'access': u'yes', u'source': u'openstreetmap.org', u'foot': u'yes', u'highway': u'cycleway'}))  # noqa

        self.assert_has_feature(
            16, 36155, 20940, 'roads',
            {'id': 151351130, 'kind': 'path', 'access': 'yes'})
