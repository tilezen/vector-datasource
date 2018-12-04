# -*- encoding: utf-8 -*-
from . import FixtureTest


class TooManyServiceAreasTest(FixtureTest):

    def test_large_service_area(self):
        import dsl

        z, x, y = (11, 602, 769)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/193904383
            dsl.way(193904383, dsl.tile_box(z, x, y), {
                'area': u'yes',
                'highway': u'services',
                'name': u'Alexander Hamilton Service Area',
                'source': u'openstreetmap.org',
                'toilets': u'yes',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 193904383,
                'kind': 'service_area',
                'min_zoom': 11,
            })

    def test_tiny_service_area(self):
        # this really looks more like mistagging than a service area, not even
        # a small one.
        import dsl
        from shapely.wkt import loads as wkt_loads

        z, x, y = (16, 19285, 24783)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/427844785
            dsl.way(
                427844785,
                wkt_loads(
                    'POLYGON(('
                    '-74.0621163 40.1128853002825,'
                    '-74.0620970 40.1128760002825,'
                    '-74.0620736 40.1129032002825,'
                    '-74.0620939 40.1129133002825,'
                    '-74.0621163 40.1128853002825'
                    '))'
                ), {
                    'area': u'yes',
                    'highway': u'services',
                    'name': u'Franklin Submersibles',
                    'source': u'openstreetmap.org',
                }
            ),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 427844785,
                'kind': u'service_area',
                'min_zoom': 17,
            })

    def test_not_really_a_service_node(self):
        # another case of mistagging?
        import dsl

        z, x, y = (16, 19317, 24642)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5346072553
            dsl.point(5346072553, (-73.884929, 40.701724), {
                'addr:street': u'Myrtle Avenue',
                'highway': u'services',
                'name': u'GPS Roofing',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5346072553,
                'kind': u'service_area',
                'min_zoom': 17,
            })

    def test_service_area(self):
        import dsl

        z, x, y = (13, 2380, 3110)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4938688427
            dsl.point(4938688427, (-75.396299, 39.695616), {
                'highway': u'services',
                'name': u'John Fenwick Service Area',
                'name:en': u'John Fenwick Service Area',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4938688427,
                'kind': u'service_area',
                'min_zoom': 13,
            })

    def test_services(self):
        import dsl

        z, x, y = (13, 2380, 3110)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3621020976
            dsl.point(3621020976, (-75.396490, 39.698151), {
                'highway': u'services',
                'name': u'Clara Barton Services',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3621020976,
                'kind': u'service_area',
                'min_zoom': 13,
            })

    def test_travel_plaza(self):
        import dsl

        z, x, y = (13, 2410, 3053)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/450420567
            dsl.point(450420567, (-74.087849, 41.593617), {
                'addr:city': u'Modena',
                'addr:postcode': u'12548',
                'addr:state': u'NY',
                'alt_name': u'Modena Service Area',
                'highway': u'services',
                'internet_access': u'wlan',
                'name': u'Modena Travel Plaza',
                'operator': u'New York State Thruway Authority',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 450420567,
                'kind': u'service_area',
                'min_zoom': 13,
            })
