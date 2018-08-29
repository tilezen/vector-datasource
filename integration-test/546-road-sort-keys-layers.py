# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class RoadSortKeysLayers(FixtureTest):
    def test_layer_5(self):
        # layer 5
        self.generate_fixtures(dsl.way(48474682, wkt_loads('LINESTRING (-121.474073979658 38.55419551547709, -121.474107396987 38.55438195862888)'), {u'bridge': u'yes', u'layer': u'5', u'maxspeed': u'65 mph', u'lanes': u'4', u'tiger:cfcc': u'A35', u'tiger:name_base_1': u'State Highway 99', u'hgv': u'designated', u'hgv:national_network': u'yes', u'hov': u'lane', u'note:lanes': u'left lane is hov', u'tiger:name_base': u'South Sacramento', u'tiger:name_type': u'Fwy', u'source': u'openstreetmap.org', u'oneway': u'yes', u'bicycle': u'no', u'source:hgv:national_network': u'Title%2023:%20Highways%20Part%20658%20http://ecfr.gpoaccess.gov/cgi/t/text/text-idx?c=ecfr&rgn=div5&view=text&node=23:1.0.1.7.33&idno=23', u'ref': u'CA 51', u'tiger:county': u'Sacramento, CA', u'highway': u'motorway'}))  # noqa

        self.assert_has_feature(
            16, 10654, 25150, "roads",
            {"kind": "highway", "kind_detail": "motorway", "is_bridge": True,
             "id": 48474682, "sort_rank": 447})

    def test_layer_4(self):
        # layer 4
        self.generate_fixtures(dsl.way(8918870, wkt_loads('LINESTRING (-122.411178697409 37.73354279788042, -122.409649944459 37.73416535950228, -122.409213363231 37.7343443902903, -122.408764115757 37.7345183054984, -122.408334990546 37.73467950350251, -122.407874963289 37.73483437829259, -122.405695740241 37.735536496959)'), {u'bridge': u'yes', u'horse': u'no', u'tiger:name_base': u'I-280', u'lanes': u'2', u'name': u'Southern Embarcadero Freeway', u'tiger:cfcc': u'A15', u'hgv': u'designated', u'layer': u'4', u'source': u'openstreetmap.org', u'tiger:county': u'San Francisco, CA', u'oneway': u'yes', u'foot': u'no', u'bicycle': u'no', u'sidewalk': u'none', u'ref': u'I 280', u'highway': u'motorway'}))  # noqa

        self.assert_has_feature(
            16, 10483, 25340, "roads",
            {"kind": "highway", "kind_detail": "motorway", "is_bridge": True,
             "id": 8918870, "sort_rank": 446})

    def test_layer_3(self):
        # layer 3
        self.generate_fixtures(dsl.way(29394019, wkt_loads('LINESTRING (-122.436406265196 37.7315028648389, -122.436238729396 37.73149227889409, -122.43610730587 37.7314701123472, -122.435987919768 37.7314350863476, -122.435876618505 37.73138727192388, -122.435581611765 37.73124098659328, -122.435460878191 37.7311963691548, -122.435321369827 37.73116141407269, -122.435172518985 37.7311381106754, -122.434986118563 37.7311305796979, -122.434805108034 37.73115075703219, -122.434669642089 37.73118045464789, -122.434060674158 37.731390469026)'), {u'bridge': u'yes', u'layer': u'3', u'lanes': u'1', u'tiger:cfcc': u'A63', u'source': u'openstreetmap.org', u'tiger:county': u'San Francisco, CA', u'oneway': u'yes', u'highway': u'motorway_link'}))  # noqa

        self.assert_has_feature(
            16, 10479, 25341, "roads",
            {"kind": "highway", "kind_detail": "motorway_link",
             "is_bridge": True, "id": 29394019, "sort_rank": 445})

    def test_layer_2(self):
        # layer 2
        self.generate_fixtures(dsl.way(27651523, wkt_loads('LINESTRING (-122.431455290339 37.6276109841108, -122.431086172589 37.6272982960442, -122.430708610675 37.62696518753708)'), {u'bridge': u'yes', u'horse': u'no', u'maxspeed': u'65 mph', u'lanes': u'4', u'name': u'Junipero Serra Freeway', u'hgv': u'designated', u'layer': u'2', u'maxspeed:trailer': u'55 mph', u'source': u'openstreetmap.org', u'maxspeed:hgv': u'55 mph', u'oneway': u'yes', u'foot': u'no', u'bicycle': u'no', u'sidewalk': u'none', u'ref': u'I 280', u'highway': u'motorway'}))  # noqa

        self.assert_has_feature(
            16, 10480, 25365, "roads",
            {"kind": "highway", "kind_detail": "motorway", "is_bridge": True,
             "id": 27651523, "sort_rank": 444})

    def test_layer_1(self):
        # layer 1
        self.generate_fixtures(dsl.way(295487932, wkt_loads('POINT (-122.474508577467 37.80641851996678)'), {u'source': u'openstreetmap.org', u'ref': u'439', u'highway': u'motorway_junction'}),dsl.way(28412298, wkt_loads('LINESTRING (-122.474314182039 37.80619487846148, -122.474508577467 37.80641851996678)'), {u'bridge': u'yes', u'layer': u'1', u'maxspeed': u'35 mph', u'lanes': u'5', u'name': u'Presidio Parkway', u'note:lanes': u'center lanes are reversible, so number may be different', u'hgv': u'designated', u'source:hgv:state_network': u'Caltrans http://www.dot.ca.gov/hq/traffops/trucks/truckmap/', u'oneway': u'yes', u'lit': u'yes', u'source': u'openstreetmap.org', u'tiger:county': u'San Francisco, CA', u'alt_name': u'Doyle Drive', u'NHS': u'STRAHNET', u'toll': u'no', u'bicycle': u'no', u'hgv:state_network': u'yes', u'ref': u'US 101;CA 1', u'highway': u'motorway'}))  # noqa

        self.assert_has_feature(
            16, 10472, 25323, "roads",
            {"kind": "highway", "kind_detail": "motorway", "is_bridge": True,
             "id": 28412298, "sort_rank": 443})

    def test_layer_minus_1(self):
        # layer -1
        self.generate_fixtures(dsl.way(43685501, wkt_loads('LINESTRING (-122.475136230356 37.80740917768379, -122.47562608168 37.80707638119829, -122.47567836363 37.80703528722239, -122.475723818383 37.80699390932719, -122.475870962426 37.80684507646618)'), {u'layer': u'-1', u'maxspeed': u'15 mph', u'tiger:cfcc': u'A41', u'lcn_ref': u'95', u'tunnel': u'yes', u'maxheight': u'3.61', u'source': u'openstreetmap.org', u'tiger:county': u'San Francisco, CA', u'highway': u'service'}))  # noqa

        self.assert_has_feature(
            16, 10472, 25323, "roads",
            {"kind": "minor_road", "kind_detail": "service", "is_tunnel": True,
             "id": 43685501, "sort_rank": 304})

    def test_layer_minus_2(self):
        # layer -2
        self.generate_fixtures(dsl.way(50691047, wkt_loads('LINESTRING (-122.36675233537 37.80855546520939, -122.365044188857 37.81017851999598)'), {u'tiger:name_base': u'I-80', u'layer': u'-2', u'maxspeed': u'50 mph', u'lanes': u'5', u'name': u'San Francisco \u2013 Oakland Bay Bridge', u'tiger:cfcc': u'A11', u'tiger:name_base_1': u'Bay', u'tunnel': u'yes', u'tiger:name_type_1': u'Brg', u'maxheight': u'14\'0"', u'source': u'openstreetmap.org', u'hgv': u'designated', u'oneway': u'yes', u'bicycle': u'no', u'ref': u'I 80', u'tiger:county': u'San Francisco, CA', u'highway': u'motorway'}))  # noqa

        self.assert_has_feature(
            16, 10491, 25323, "roads",
            {"kind": "highway", "kind_detail": "motorway", "is_tunnel": True,
             "id": 50691047, "sort_rank": 303})
