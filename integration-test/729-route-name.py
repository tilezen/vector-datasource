# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class RouteName(FixtureTest):
    def test_route_name(self):
        # Relation: M-Ocean View: Inbound to Downtown (91022)
        self.generate_fixtures(dsl.way(1723738813, wkt_loads('POINT (-122.396932315318 37.7928790038277)'), {u'name': u'Embarcadero', u'wikipedia': u'en:Embarcadero Station', u'source': u'openstreetmap.org', u'operator': u'San Francisco Municipal Railway', u'railway': u'station', u'network': u'Muni'}),dsl.way(160333986, wkt_loads('LINESTRING (-122.395818224703 37.79375015943719, -122.396932315318 37.7928790038277)'), {u'layer': u'-1', u'name': u'Muni Metro', u'tunnel': u'yes', u'electrified': u'contact_line', u'source': u'openstreetmap.org', u'frequency': u'0', u'gauge': u'1435', u'voltage': u'600', u'railway': u'light_rail'}),dsl.way(340366203, wkt_loads('LINESTRING (-122.396932315318 37.7928790038277, -122.3975068986359 37.79242240798857)'), {u'layer': u'-1', u'name': u'Muni Metro', u'level': u'-2', u'tunnel': u'yes', u'electrified': u'contact_line', u'source': u'openstreetmap.org', u'frequency': u'0', u'gauge': u'1435', u'voltage': u'600', u'railway': u'light_rail'}),dsl.way(-91022, wkt_loads('LINESTRING (-122.3975068986359 37.79242240798857, -122.396932315318 37.7928790038277, -122.395818224703 37.79375015943719)'), {u'from': u'Balboa Park Station', u'name': u'M-Ocean View: Inbound to Downtown', u'to': u'Embarcadero Station', u'route': u'light_rail', u'route_name': u'M-Ocean View: Inbound to Downtown', u'route_pref_color': u'0', u'source': u'openstreetmap.org', u'operator': u'San Francisco Municipal Railway', u'ref': u'M', u'colour': u'#008752'}))  # noqa

        self.assert_has_feature(
            16, 10486, 25326, 'transit',
            {'id': -91022, 'kind': 'light_rail', 'osm_relation': True,
             'name': 'M-Ocean View: Inbound to Downtown',
             'route_name': type(None)})
