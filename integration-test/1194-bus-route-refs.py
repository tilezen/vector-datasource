from . import FixtureTest


class BusRouteRefs(FixtureTest):
    def test_one_bus_route(self):
        # Sloat Blvd, part of:
        #   type=route, route=bus, network="", ref=23
        #   type=route, route=bicycle, network=lcn, ref=50
        #   type=route, route=road, network=US:CA, ref=35
        self.load_fixtures(['https://www.openstreetmap.org/way/417097119',
                            'https://www.openstreetmap.org/relation/3002741',
                            'https://www.openstreetmap.org/relation/32312',
                            'https://www.openstreetmap.org/relation/1976278'])

        self.assert_has_feature(
            16, 10469, 25340, 'roads',
            {'id': 417097119,
             'network': 'US:CA',
             'shield_text': '35',
             'bicycle_network': 'lcn',
             'bicycle_shield_text': '50',
             'bus_network': type(None),
             'bus_shield_text': '23'})

    def test_inbound_and_outbound_routes(self):
        # Jackson St. SF, part of trolley-bus route 3
        # relation 2980505 is outbound
        # relation 2980504 is inbound
        self.load_fixtures(['http://www.openstreetmap.org/way/225516711',
                            'http://www.openstreetmap.org/relation/2980505',
                            'http://www.openstreetmap.org/relation/2980504'])

        self.assert_has_feature(
            16, 10477, 25327, 'roads',
            {'id': 225516711,
             'bus_network': type(None),
             'bus_shield_text': '3',
             'all_bus_networks': [type(None)],
             'all_bus_shield_texts': ['3']})

    def test_full_lists_disappear_by_zoom_12(self):
        # make sure the all_* lists are gone by zoom 12 on major roads, but
        # the "most important", singular network & shield text remain at
        # earlier zooms
        #
        # note that it doesn't matter what the bus shield is - that's
        # data-dependent. for the purposes of the test, we only care that
        # there _is_ one.
        self.load_fixtures(['http://www.openstreetmap.org/way/225516711',
                            'http://www.openstreetmap.org/relation/2980505',
                            'http://www.openstreetmap.org/relation/2980504'])

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
