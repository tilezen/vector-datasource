# -*- encoding: utf-8 -*-
from . import FixtureTest


class HideEarlyAtmBusStopTest(FixtureTest):

    def test_atm(self):
        import dsl

        z, x, y = (16, 10473, 25332)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3161882181
            dsl.point(3161882181, (-122.466755, 37.769587), {
                'amenity': 'atm',
                'name': 'Wells Fargo',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3161882181,
                'kind': 'atm',
                'min_zoom': 18,
            })

    def test_highway_bus_stop(self):
        import dsl

        z, x, y = (16, 10482, 25328)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/381940953
            dsl.point(381940953, (-122.416392, 37.787220), {
                'bulb': 'no',
                'highway': 'bus_stop',
                'operator': 'San Francisco Municipal Railway',
                'route_ref': '2;3;4;76',
                'shelter': 'no',
                'source': 'openstreetmap.org',
                'ticker': 'no',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 381940953,
                'kind': 'bus_stop',
                'min_zoom': 18,
            })

    def test_platform_bus_stop(self):
        import dsl

        z, x, y = (16, 10511, 25255)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/1866509704
            dsl.point(1866509704, (-122.259434, 38.100169), {
                'bus': 'yes',
                'covered': 'yes',
                'highway': 'platform',
                'local_ref': '85',
                'network': 'SolTrans',
                'operator': 'Soltrans',
                'public_transport': 'platform',
                'ref': 'Y',
                'source': 'openstreetmap.org',
                'wheelchair': 'yes',
                'wifi': 'free for guests',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1866509704,
                'kind': 'bus_stop',
                'min_zoom': 18,
            })

    def test_public_transport_bus_stop(self):
        import dsl

        z, x, y = (16, 10483, 25329)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/1847714412
            dsl.point(1847714412, (-122.412267, 37.781180), {
                'bus': 'yes',
                'highway': 'bus_stop',
                'operator': 'San Francisco Municipal Railway',
                'public_transport': 'platform',
                'route_ref': '5',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1847714412,
                'kind': 'bus_stop',
                'min_zoom': 18,
            })

    def test_street_lamp(self):
        import dsl

        z, x, y = (16, 10483, 25330)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5441990644
            dsl.point(5441990644, (-122.413513, 37.777848), {
                'highway': 'street_lamp',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5441990644,
                'kind': 'street_lamp',
                'min_zoom': 18,
            })

    def test_post_box(self):
        import dsl

        z, x, y = (16, 10483, 25328)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/669137638
            dsl.point(669137638, (-122.412930, 37.785763), {
                'amenity': 'post_box',
                'note': 'TODO: location',
                'operator': 'US Mail Service',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 669137638,
                'kind': 'post_box',
                'min_zoom': 18,
            })

    def test_telephone(self):
        import dsl

        z, x, y = (16, 10479, 25328)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/429649021
            dsl.point(429649021, (-122.436433, 37.785572), {
                'amenity': 'telephone',
                'capacity': '1',
                'outside': 'yes',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 429649021,
                'kind': 'telephone',
                'min_zoom': 18,
            })

    def test_amenity_bus_stop_unsupported(self):
        import dsl

        z, x, y = (16, 32768, 32768)

        self.generate_fixtures(
            dsl.point(1, (0, 0), {
                'amenity': 'bus_stop',
                'source': 'openstreetmap.org',
            }),
        )

        # should not produce any POI in the output
        self.assert_no_matching_feature(
            z, x, y, 'pois', {
                'kind': 'bus_stop',
            })
