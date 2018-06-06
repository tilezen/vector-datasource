# -*- encoding: utf-8 -*-
from . import FixtureTest


# see https://en.wikipedia.org/wiki/Numbered_routes_in_South_Africa
#
# there also appear to be H-numbered roads in Kruger National Park, and
# S-numbered roads mostly in Kruger, but some scattered over the rest of
# the country too.
#
class SouthAfricanShieldTest(FixtureTest):
    def test_304_zaregional(self):
        import dsl

        z, x, y = (16, 36189, 39316)

        self.generate_fixtures(
            dsl.is_in('ZA', z, x, y),
            # https://www.openstreetmap.org/way/4020644
            dsl.way(4020644, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'maxspeed': u'80',
                'ref': u'R304',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'direction': u'south',
                'name': u'R304 (southbound)',
                'network': u'za:regional',
                'ref': u'R304',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[4020644]),
            dsl.relation(2, {
                'direction': u'north',
                'name': u'R304 (northbound)',
                'network': u'za:regional',
                'ref': u'R304',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[4020644]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4020644,
                'network': u'ZA:regional',
                'shield_text': u'304',
            })

    def test_101_zaregional(self):
        import dsl

        z, x, y = (16, 36189, 39319)

        self.generate_fixtures(
            dsl.is_in('ZA', z, x, y),
            # https://www.openstreetmap.org/way/56160610
            dsl.way(56160610, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'maxspeed': u'80',
                'ref': u'R304;R101',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'direction': u'south',
                'name': u'R101 (southbound)',
                'network': u'za:regional',
                'ref': u'R101',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[56160610]),
            dsl.relation(2, {
                'direction': u'north',
                'name': u'R101 (northbound)',
                'network': u'za:regional',
                'ref': u'R101',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[56160610]),
            dsl.relation(3, {
                'direction': u'south',
                'name': u'R304 (southbound)',
                'network': u'za:regional',
                'ref': u'R304',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[56160610]),
            dsl.relation(4, {
                'direction': u'north',
                'name': u'R304 (northbound)',
                'network': u'za:regional',
                'ref': u'R304',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[56160610]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 56160610,
                'network': u'ZA:regional',
                'shield_text': u'101',
                'all_networks': ['ZA:regional', 'ZA:regional'],
                'all_shield_texts': ['101', '304'],
            })

    def test_3_zanational(self):
        import dsl

        z, x, y = (16, 38204, 38297)

        self.generate_fixtures(
            dsl.is_in('ZA', z, x, y),
            # https://www.openstreetmap.org/way/4075691
            dsl.way(4075691, dsl.tile_diagonal(z, x, y), {
                'highway': u'motorway',
                'maxspeed': u'120',
                'oneway': u'yes',
                'ref': u'N3',
                'source': u'openstreetmap.org',
            }),
            # TODO: figure out what this SADC network is... wasn't able to find
            # any signage for it. is it a multinational network?
            dsl.relation(1, {
                'direction': u'south',
                'name': u'SADC 36 (southbound)',
                'network': u'sadc',
                'ref': u'SADC 36',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[4075691]),
            dsl.relation(2, {
                'direction': u'south',
                'name': u'N3 (southbound)',
                'network': u'za:national',
                'ref': u'N3',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[4075691]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4075691,
                'network': u'ZA:national',
                'shield_text': u'3',
            })

    def test_12_zametropolitan(self):
        import dsl

        z, x, y = (16, 37420, 39344)

        self.generate_fixtures(
            dsl.is_in('ZA', z, x, y),
            # https://www.openstreetmap.org/way/4018652
            dsl.way(4018652, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'lanes': u'2',
                'name': u'Disa Avenue',
                'ref': u'M12',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 4018652,
                'network': u'ZA:metropolitan',
                'shield_text': u'12',
            })

    def test_p_roads(self):
        # some roads seem to get a P-number, which i couldn't find a sign for,
        # so we'll just drop them for now.
        import dsl

        z, x, y = (16, 36765, 39395)

        self.generate_fixtures(
            dsl.is_in('ZA', z, x, y),
            # https://www.openstreetmap.org/way/5199653
            dsl.way(5199653, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'lanes': u'2',
                'maxspeed': u'100',
                'oneway': u'no',
                'ref': u'P1532',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 5199653,
                'network': type(None),
                'shield_text': type(None),
            })

    def test_334_zaregional_metropolitan(self):
        import dsl

        z, x, y = (16, 37398, 39302)

        self.generate_fixtures(
            dsl.is_in('ZA', z, x, y),
            # https://www.openstreetmap.org/way/5052303
            dsl.way(5052303, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'ref': u'R334/M20',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'direction': u'east',
                'name': u'R334 (eastbound)',
                'network': u'za:regional',
                'ref': u'R334',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[5052303]),
            dsl.relation(2, {
                'direction': u'west',
                'name': u'R334 (westbound)',
                'network': u'za:regional',
                'ref': u'R334',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[5052303]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 5052303,
                'network': u'ZA:regional',
                'shield_text': u'334',
                'all_networks': ['ZA:regional', 'ZA:metropolitan'],
                'all_shield_texts': ['334', '20'],
            })

    def test_48_zametropolitan(self):
        import dsl

        z, x, y = (16, 36162, 39319)

        self.generate_fixtures(
            dsl.is_in('ZA', z, x, y),
            # https://www.openstreetmap.org/way/6045026
            dsl.way(6045026, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'maxspeed': u'60',
                'name': u'Vissershokpad',
                'ref': u'M48',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'direction': u'west',
                'name': u'M48 (westbound)',
                'network': u'za:capetown',
                'ref': u'M48',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[6045026]),
            dsl.relation(2, {
                'direction': u'east',
                'name': u'M48 (eastbound)',
                'network': u'za:capetown',
                'ref': u'M48',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[6045026]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 6045026,
                'network': u'ZA:metropolitan',
                'shield_text': u'48',
            })

    def test_33_zaprovincial(self):
        import dsl

        z, x, y = (16, 38339, 38300)

        self.generate_fixtures(
            dsl.is_in('ZA', z, x, y),
            # https://www.openstreetmap.org/way/362712293
            dsl.way(362712293, dsl.tile_diagonal(z, x, y), {
                'bridge': u'yes',
                'highway': u'primary',
                'layer': u'1',
                'name': u'R33 (northbound)',
                'ref': u'R74,R33',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'direction': u'south',
                'name': u'R33 (southbound)',
                'network': u'za:regional',
                'ref': u'R33',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[362712293]),
            dsl.relation(2, {
                'direction': u'north',
                'name': u'R33 (northbound)',
                'network': u'za:regional',
                'ref': u'R33',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[362712293]),
            dsl.relation(3, {
                'direction': u'east',
                'name': u'R74 (eastbound)',
                'network': u'za:regional',
                'ref': u'R74',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[362712293]),
            dsl.relation(4, {
                'direction': u'west',
                'name': u'R74 (westbound)',
                'network': u'za:regional',
                'ref': u'R74',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[362712293]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 362712293,
                'network': u'ZA:provincial',
                'shield_text': u'33',
                'all_networks': ['ZA:provincial', 'ZA:provincial'],
                'all_shield_texts': ['33', '74'],
            })

    def test_33_zaprovincial_norel(self):
        # check that we can parse the same information from just the ref, and
        # don't need the relations in this case.
        import dsl

        z, x, y = (16, 38339, 38300)

        self.generate_fixtures(
            dsl.is_in('ZA', z, x, y),
            # https://www.openstreetmap.org/way/362712293
            dsl.way(362712293, dsl.tile_diagonal(z, x, y), {
                'bridge': u'yes',
                'highway': u'primary',
                'layer': u'1',
                'name': u'R33 (northbound)',
                'ref': u'R74,R33',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 362712293,
                'network': u'ZA:provincial',
                'shield_text': u'33',
                'all_networks': ['ZA:provincial', 'ZA:provincial'],
                'all_shield_texts': ['33', '74'],
            })

    def test_h11_zakruger(self):
        import dsl

        z, x, y = (16, 38446, 37501)

        self.generate_fixtures(
            dsl.is_in('ZA', z, x, y),
            # https://www.openstreetmap.org/way/22375922
            dsl.way(22375922, dsl.tile_diagonal(z, x, y), {
                'alt_name': u'H1-1',
                'highway': u'secondary',
                'maxspeed': u'50',
                'name': u'Napi Road',
                'oneway': u'no',
                'ref': u'H1-1',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'name': u'Napi Road',
                'ref': u'H1-1',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[22375922]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 22375922,
                'network': u'ZA:kruger',
                'shield_text': u'H1-1',
            })

    def test_s110_zasroad(self):
        import dsl

        z, x, y = (16, 38505, 37562)

        self.generate_fixtures(
            dsl.is_in('ZA', z, x, y),
            # https://www.openstreetmap.org/way/22375193
            dsl.way(22375193, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'maxspeed': u'50',
                'name': u'Matjulu Loop',
                'oneway': u'no',
                'ref': u'S110',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 22375193,
                'network': u'ZA:S-road',
                'shield_text': u'S110',
            })
