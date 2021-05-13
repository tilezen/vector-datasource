# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class UndergroundWaterTest(FixtureTest):
    def test_water_level_1(self):
        z, x, y = (16, 33199, 22547)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/236735251
            dsl.way(236735251, dsl.tile_diagonal(z, x, y), {
                'layer': '-1',
                'name': u'Vo\xfbte Richard Lenoir',
                'source': 'openstreetmap.org',
                'tunnel': 'yes',
                'waterway': 'riverbank',
            }),
        )

        # tunnels at level = 0
        self.assert_has_feature(
            16, 33199, 22547, "water",
            {"kind": "riverbank", "id": 236735251,
             "name": "Voûte Richard Lenoir", "is_tunnel": True, "sort_rank": 9})

    # def test_water_level_2(self):
    #     self.generate_fixtures(dsl.way(259492789, wkt_loads('LINESTRING (-74.16702601822249 40.73275266220829, -74.16711180733211 40.73254919807029)'), {u'tunnel': u'yes', u'tiger:name_base': u'McCarter', u'hgv:state_network': u'yes', u'name': u'McCarter Highway', u'tiger:cfcc': u'A35', u'tiger:name_base_1': u'State Route 21', u'hgv': u'designated', u'tiger:zip_left': u'07104', u'tiger:zip_right': u'07104', u'lanes': u'4', u'source': u'openstreetmap.org', u'tiger:county': u'Essex, NJ', u'tiger:name_type': u'Hwy', u'NHS': u'yes', u'ref': u'NJ 21', u'NJDOT_SRI': u'00000021', u'HFCS': u'Urban Principal Arterial', u'source:hgv:state_network': u'NJDOT http://www.state.nj.us/transportation/about/rules/pdf/chapter32truckaccess.pdf', u'highway': u'trunk'}))  # noqa
    #
    #     self.assert_has_feature(
    #         16, 33199, 22547, "water",
    #         {"kind": "riverbank", "id": 259492789,
    #          "name": "McCarter Hwy.", "is_tunnel": True, "sort_rank": 8})
    #
    # def test_pedestrian(self):
    #     self.generate_fixtures(dsl.way(259492789, wkt_loads('LINESTRING (-74.16702601822249 40.73275266220829, -74.16711180733211 40.73254919807029)'), {u'tunnel': u'yes', u'tiger:name_base': u'McCarter', u'hgv:state_network': u'yes', u'name': u'McCarter Highway', u'tiger:cfcc': u'A35', u'tiger:name_base_1': u'State Route 21', u'hgv': u'designated', u'tiger:zip_left': u'07104', u'tiger:zip_right': u'07104', u'lanes': u'4', u'source': u'openstreetmap.org', u'tiger:county': u'Essex, NJ', u'tiger:name_type': u'Hwy', u'NHS': u'yes', u'ref': u'NJ 21', u'NJDOT_SRI': u'00000021', u'HFCS': u'Urban Principal Arterial', u'source:hgv:state_network': u'NJDOT http://www.state.nj.us/transportation/about/rules/pdf/chapter32truckaccess.pdf', u'highway': u'trunk'}))  # noqa
    #
    #     self.assert_has_feature(
    #         16, 33199, 22546, "landuse",
    #         {"kind": "pedestrian", "id": -1602299,
    #          "name": "Esplanade Roger Joseph Boscovich", "sort_rank": 110})
    #
    # def test_garden(self):
    #     self.generate_fixtures(dsl.way(259492789, wkt_loads('LINESTRING (-74.16702601822249 40.73275266220829, -74.16711180733211 40.73254919807029)'), {u'tunnel': u'yes', u'tiger:name_base': u'McCarter', u'hgv:state_network': u'yes', u'name': u'McCarter Highway', u'tiger:cfcc': u'A35', u'tiger:name_base_1': u'State Route 21', u'hgv': u'designated', u'tiger:zip_left': u'07104', u'tiger:zip_right': u'07104', u'lanes': u'4', u'source': u'openstreetmap.org', u'tiger:county': u'Essex, NJ', u'tiger:name_type': u'Hwy', u'NHS': u'yes', u'ref': u'NJ 21', u'NJDOT_SRI': u'00000021', u'HFCS': u'Urban Principal Arterial', u'source:hgv:state_network': u'NJDOT http://www.state.nj.us/transportation/about/rules/pdf/chapter32truckaccess.pdf', u'highway': u'trunk'}))  # noqa
    #
    #     self.assert_has_feature(
    #         16, 33199, 22546, "landuse",
    #         {"kind": "garden", "id": -1602306,
    #          "sort_rank": 112})
