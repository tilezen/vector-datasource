# -*- encoding: utf-8 -*-
from . import FixtureTest


class SubstationTest(FixtureTest):

    def test_substation_14_way(self):
        import dsl

        z, x, y = (14, 4786, 5898)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/142431633
            dsl.way(142431633, dsl.box_area(z, x, y, 545185), {
                'barrier': 'fence',
                'name': 'Dennison Substation',
                'power': 'substation',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 142431633,
                'kind': 'substation',
                'min_zoom': 14,
            })

    def test_substation_15_way(self):
        import dsl

        z, x, y = (15, 9653, 12314)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/108298302
            dsl.way(108298302, dsl.box_area(z, x, y, 51769), {
                'frequency': '60',
                'location': 'outdoor',
                'name': 'Rainey Substation',
                'operator': 'Consolidated Edison',
                'power': 'substation',
                'source': 'openstreetmap.org',
                'substation': 'transmission',
                'voltage': '345000;138000',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 108298302,
                'kind': 'substation',
                'min_zoom': 15,
            })

    def test_substation_16_way(self):
        import dsl

        z, x, y = (16, 11223, 26160)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/394710539
            dsl.way(394710539, dsl.box_area(z, x, y, 39876), {
                'frequency': '60',
                'location': 'outdoor',
                'name': 'RECEIVING STATION H',
                'operator': 'LOS ANGELES DEPARTMENT OF WATER AND POWER',
                'power': 'substation',
                'ref': 'H',
                'source': 'openstreetmap.org',
                'substation': 'transmission',
                'voltage': '138000',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 394710539,
                'kind': 'substation',
                'min_zoom': 16,
            })

    def test_substation_17_way(self):
        import dsl

        z, x, y = (17, 20966, 50660)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/35115839
            dsl.way(35115839, dsl.box_area(z, x, y, 4869), {
                'building': 'yes',
                'height': '36 m',
                'name': 'Pacific Gas & Electric Mission Substation',
                'power': 'substation',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 35115839,
                'kind': 'substation',
                'min_zoom': 17,
            })
