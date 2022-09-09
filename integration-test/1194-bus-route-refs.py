import unittest

import dsl

from . import FixtureTest
from . import SKIP_UNIT_TEST_REASON


@unittest.skip(SKIP_UNIT_TEST_REASON)
class BusRouteRefs(FixtureTest):
    def test_one_bus_route(self):
        # Sloat Blvd, part of:
        #   type=route, route=bus, network="", ref=23
        #   type=route, route=bicycle, network=lcn, ref=50
        #   type=route, route=road, network=US:CA, ref=35
        self.generate_fixtures(
            dsl.way(417097119, dsl.tile_diagonal(16, 10469, 25340), {
                'source': 'openstreetmap.org',
                'cycleway:right': 'lane',
                'hgv': 'designated',
                'hgv:state_network': 'yes',
                'highway': 'primary',
                'lanes': '2',
                'lcn_ref': '50',
                'maxspeed': '35 mph',
                'name': 'Sloat Boulevard',
                'name:etymology:wikidata': 'Q634931',
                'oneway': 'yes',
                'ref': 'CA 35',
                'sidewalk': 'right',
                'source:hgv:state_network': 'Caltrans http://www.dot.ca.gov/hq/traffops/trucks/truckmap/',
                'tiger:cfcc': 'A45',
                'tiger:county': 'San Francisco, CA',
                'tiger:name_base': 'Sloat',
                'tiger:name_type': 'Blvd'
            }),
            dsl.relation(3002741, {
                'source': 'openstreetmap.org',
                'fee': 'yes',
                'from': 'Palou Avenue & 3rd Street',
                'name': 'Muni 23 outbound: Bayview => SF Zoo',
                'operator': 'San Francisco Municipal Railway',
                'payment:cash': 'yes',
                'payment:clipper': 'yes',
                'payment:prepaid_ticket': 'yes',
                'public_transport:version': '2',
                'ref': '23',
                'route': 'bus',
                'to': 'Great Highway & Sloat Boulevard',
                'type': 'route'
            }, ways=[417097119]),
            dsl.relation(32312, {
                'source': 'openstreetmap.org',
                'cycle_network': 'US:CA:SF',
                'network': 'lcn',
                'ref': '50',
                'route': 'bicycle',
                'type': 'route'
            }, ways=[417097119]),
            dsl.relation(1976278, {
                'source': 'openstreetmap.org',
                'network': 'US:CA',
                'ref': '35',
                'route': 'road',
                'type': 'route'
            }, ways=[417097119]),
        )

        self.assert_has_feature(
            16, 10469, 25340, 'roads',
            {'id': 417097119,
             'network': 'US:CA',
             'shield_text': '35',
             'bicycle_network': 'lcn',
             'bicycle_shield_text': '50',
             'bus_network': type(None),
             'bus_shield_text': type(None),
             'is_bus_related': True})

    def test_inbound_and_outbound_routes(self):
        # Jackson St. SF, part of trolley-bus route 3
        # relation 2980505 is outbound
        # relation 2980504 is inbound
        self.generate_fixtures(
            dsl.way(225516711, dsl.tile_diagonal(16, 10477, 25327), {
                'source': 'openstreetmap.org',
                'highway': 'residential',
                'name': 'Jackson Street',
                'name:etymology:wikidata': 'Q11817',
                'sidewalk': 'both',
                'tiger:cfcc': 'A41',
                'tiger:county': 'San Francisco, CA',
                'tiger:name_base': 'Jackson',
                'tiger:name_type': 'St',
                'trolley_wire': 'yes'
            }),
            dsl.relation(2980505, {
                'source': 'openstreetmap.org',
                'name': '3-Jackson: Outbound to The Richmond',
                'ref': '3',
                'route': 'trolleybus',
                'type': 'route',
                'from': 'Sutter St & Sansome St',
                'to': 'Presidio Ave & California St'
            }, ways=[225516711]),
            dsl.relation(2980504, {
                'source': 'openstreetmap.org',
                'name': 'Muni 3 inbound: Pacific Heights => Downtown',
                'ref': '3',
                'route': 'trolleybus',
                'type': 'route',
                'to': 'Sutter St & Sansome St',
                'from': 'Presidio Ave & California St'
            }, ways=[225516711]),
        )

        self.assert_has_feature(
            16, 10477, 25327, 'roads',
            {'id': 225516711,
             'bus_network': type(None),
             'bus_shield_text': type(None),
             'is_bus_related': True,
             'all_bus_networks': [type(None)],
             'all_bus_shield_texts': [type(None)]})

    def test_full_lists_disappear_by_zoom_12(self):
        # make sure the all_* lists are gone by zoom 12 on major roads, but
        # the "most important", singular network & shield text remain at
        # earlier zooms
        #
        # note that it doesn't matter what the bus shield is - that's
        # data-dependent. for the purposes of the test, we only care that
        # there _is_ one.
        self.generate_fixtures(
            dsl.way(225516711, dsl.tile_diagonal(12, 654, 1583), {
                'source': 'openstreetmap.org',
                'highway': 'residential',
                'name': 'Jackson Street',
                'name:etymology:wikidata': 'Q11817',
                'sidewalk': 'both',
                'tiger:cfcc': 'A41',
                'tiger:county': 'San Francisco, CA',
                'tiger:name_base': 'Jackson',
                'tiger:name_type': 'St',
                'trolley_wire': 'yes'
            }),
            dsl.relation(2980505, {
                'source': 'openstreetmap.org',
                'name': '3-Jackson: Outbound to The Richmond',
                'ref': '3',
                'route': 'trolleybus',
                'type': 'route',
                'from': 'Sutter St & Sansome St',
                'to': 'Presidio Ave & California St'
            }, ways=[225516711]),
            dsl.relation(2980504, {
                'source': 'openstreetmap.org',
                'name': 'Muni 3 inbound: Pacific Heights => Downtown',
                'ref': '3',
                'route': 'trolleybus',
                'type': 'route',
                'to': 'Sutter St & Sansome St',
                'from': 'Presidio Ave & California St'
            }, ways=[225516711]),
        )
        self.assert_has_feature(
            10, 163, 395, 'roads',
            {'bus_network': type(None),
             'bus_shield_text': None})

        self.assert_no_matching_feature(
            12, 654, 1583, 'roads',
            {'all_bus_networks': None})

        self.assert_no_matching_feature(
            12, 654, 1583, 'roads',
            {'all_bus_shield_texts': None})
