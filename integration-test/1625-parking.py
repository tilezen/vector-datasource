# -*- encoding: utf-8 -*-
from . import FixtureTest


class ParkingTest(FixtureTest):

    def test_parking_node(self):
        import dsl

        z, x, y = (16, 10477, 25330)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/1706619902
            dsl.point(1706619902, (-122.445233, 37.776196), {
                'amenity': 'parking',
                'name': 'Fulton Market Garage',
                'parking': 'underground',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1706619902,
                'kind': 'parking_garage',
                'min_zoom': 18,
                'capacity': type(None),  # should _not_ set capacity
            })

    def test_parking_tiny(self):
        import dsl

        z, x, y = (16, 10466, 25340)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/257593333
            dsl.way(257593333, dsl.box_area(z, x, y, 678), {
                'amenity': 'parking',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 257593333,
                'kind': 'parking',
                'min_zoom': 17,
                'capacity': int,
            })

    def test_parking_small(self):
        import dsl

        z, x, y = (16, 10471, 25341)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/506510951
            dsl.way(506510951, dsl.box_area(z, x, y, 2207), {
                'amenity': 'parking',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 506510951,
                'kind': 'parking',
                'min_zoom': 17,
                'capacity': int,
            })

    def test_parking_medium(self):
        import dsl

        z, x, y = (16, 10471, 25341)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/162093420
            dsl.way(162093420, dsl.box_area(z, x, y, 6111), {
                'access': 'destination',
                'amenity': 'parking',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 162093420,
                'kind': 'parking',
                'min_zoom': 16,
                'capacity': int,
            })

    def test_parking_huge_1(self):
        import dsl

        z, x, y = (15, 5234, 12670)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/32928608
            dsl.way(32928608, dsl.box_area(z, x, y, 16489), {
                'amenity': 'parking',
                'source': 'openstreetmap.org',
                'tiger:cfcc': 'A41',
                'tiger:county': 'San Francisco, CA',
                'tiger:reviewed': 'no',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 32928608,
                'kind': 'parking',
                'min_zoom': 15,
                'capacity': int,
            })

    def test_parking_huge_2(self):
        import dsl

        z, x, y = (15, 5900, 12855)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/52175579
            dsl.way(52175579, dsl.box_area(z, x, y, 31611), {
                'amenity': 'parking',
                'source': 'openstreetmap.org',
                'building':	'yes',
                'fee': 'yes',
                'name': 'Aria and Vdara Self Parking',
                'parking': 'multi-storey',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 52175579,
                'kind': 'parking_garage',
                'min_zoom': 15,
                'capacity': int,
            })

    def test_parking_mega(self):
        import dsl

        z, x, y = (14, 2950, 6428)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/73540518
            dsl.way(73540518, dsl.box_area(z, x, y, 55615), {
                'amenity': 'parking',
                'source': 'openstreetmap.org',
                'building':	'yes',
                'fee': 'yes',
                'name': 'MGM Grand Self Parking',
                'parking': 'multi-storey',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 73540518,
                'kind': 'parking_garage',
                'min_zoom': 14,
                'capacity': int,
            })
