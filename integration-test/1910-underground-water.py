# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class UndergroundWaterTest(FixtureTest):
    def test_water_level_1(self):
        # tunnels at level = 0
        self.generate_fixtures(dsl.way(3685132833, wkt_loads('POINT (-122.455329276656 37.80300739883197)'), {u'source': u'openstreetmap.org', u'ref': u'437', u'highway': u'motorway_junction'}),dsl.way(167952621, wkt_loads('LINESTRING (-122.455329276656 37.80300739883197, -122.454934107763 37.80304260388298, -122.45454783219 37.80306545876599, -122.454197309567 37.803080789988)'), {u'lanes': u'3', u'name': u'Presidio Parkway', u'tunnel': u'yes', u'destination:street': u'Marina Boulevard', u'source': u'openstreetmap.org', u'alt_name': u'Doyle Drive', u'oneway': u'yes', u'ref': u'US 101', u'highway': u'motorway'}))  # noqa

        self.assert_has_feature(
            16, 33199, 22546, "water",
            {"kind": "riverbank", "id": 236735251,
             "name": "Voûte Richard Lenoir", "is_tunnel": True, "sort_rank": 9})

    def test_water_level_2(self):
        self.generate_fixtures(dsl.way(259492789, wkt_loads('LINESTRING (-74.16702601822249 40.73275266220829, -74.16711180733211 40.73254919807029)'), {u'tunnel': u'yes', u'tiger:name_base': u'McCarter', u'hgv:state_network': u'yes', u'name': u'McCarter Highway', u'tiger:cfcc': u'A35', u'tiger:name_base_1': u'State Route 21', u'hgv': u'designated', u'tiger:zip_left': u'07104', u'tiger:zip_right': u'07104', u'lanes': u'4', u'source': u'openstreetmap.org', u'tiger:county': u'Essex, NJ', u'tiger:name_type': u'Hwy', u'NHS': u'yes', u'ref': u'NJ 21', u'NJDOT_SRI': u'00000021', u'HFCS': u'Urban Principal Arterial', u'source:hgv:state_network': u'NJDOT http://www.state.nj.us/transportation/about/rules/pdf/chapter32truckaccess.pdf', u'highway': u'trunk'}))  # noqa

        self.assert_has_feature(
            16, 33199, 22547, "water",
            {"kind": "riverbank", "id": 259492789,
             "name": "McCarter Hwy.", "is_tunnel": True, "sort_rank": 8})

    def test_pedestrian(self):
        self.generate_fixtures(dsl.way(259492789, wkt_loads('LINESTRING (-74.16702601822249 40.73275266220829, -74.16711180733211 40.73254919807029)'), {u'tunnel': u'yes', u'tiger:name_base': u'McCarter', u'hgv:state_network': u'yes', u'name': u'McCarter Highway', u'tiger:cfcc': u'A35', u'tiger:name_base_1': u'State Route 21', u'hgv': u'designated', u'tiger:zip_left': u'07104', u'tiger:zip_right': u'07104', u'lanes': u'4', u'source': u'openstreetmap.org', u'tiger:county': u'Essex, NJ', u'tiger:name_type': u'Hwy', u'NHS': u'yes', u'ref': u'NJ 21', u'NJDOT_SRI': u'00000021', u'HFCS': u'Urban Principal Arterial', u'source:hgv:state_network': u'NJDOT http://www.state.nj.us/transportation/about/rules/pdf/chapter32truckaccess.pdf', u'highway': u'trunk'}))  # noqa

        self.assert_has_feature(
            16, 33199, 22546, "landuse",
            {"kind": "pedestrian", "id": -1602299,
             "name": "Esplanade Roger Joseph Boscovich", "sort_rank": 110})

    def test_garden(self):
        self.generate_fixtures(dsl.way(259492789, wkt_loads('LINESTRING (-74.16702601822249 40.73275266220829, -74.16711180733211 40.73254919807029)'), {u'tunnel': u'yes', u'tiger:name_base': u'McCarter', u'hgv:state_network': u'yes', u'name': u'McCarter Highway', u'tiger:cfcc': u'A35', u'tiger:name_base_1': u'State Route 21', u'hgv': u'designated', u'tiger:zip_left': u'07104', u'tiger:zip_right': u'07104', u'lanes': u'4', u'source': u'openstreetmap.org', u'tiger:county': u'Essex, NJ', u'tiger:name_type': u'Hwy', u'NHS': u'yes', u'ref': u'NJ 21', u'NJDOT_SRI': u'00000021', u'HFCS': u'Urban Principal Arterial', u'source:hgv:state_network': u'NJDOT http://www.state.nj.us/transportation/about/rules/pdf/chapter32truckaccess.pdf', u'highway': u'trunk'}))  # noqa

        self.assert_has_feature(
            16, 33199, 22546, "landuse",
            {"kind": "garden", "id": -1602306,
             "sort_rank": 112})
