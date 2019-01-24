# -*- encoding: utf-8 -*-
from . import FixtureTest


class LowEmissionZoneTest(FixtureTest):

    def test_low_emission_zone_way(self):
        import dsl

        z, x, y = (13, 4212, 2702)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/373249337
            dsl.way(373249337, dsl.box_area(z, x, y, 8608219), {
                'boundary': 'low_emission_zone',
                'name': 'Milieuzone Utrecht',
                'source': 'openstreetmap.org',
                'website': 'http://www.utrecht.nl/verkeersbeleid/milieuzone/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 373249337,
                'min_zoom': lambda z: 12 <= z < 13,
                'kind': 'low_emission_zone',
            })


class HgvRoadPropertiesTest(FixtureTest):

    def test_access(self):
        import dsl

        z, x, y = (16, 0, 0)

        for value in ('no', 'designated', 'destination', 'delivery', 'local',
                      'agricultural'):
            self.generate_fixtures(
                dsl.way(1, dsl.tile_diagonal(z, x, y), {
                    'highway': 'unclassified',
                    'hgv': value,
                    'source': 'openstreetmap.org',
                }),
            )

            self.assert_has_feature(
                z, x, y, 'roads', {
                    'kind': 'minor_road',
                    'kind_detail': 'unclassified',
                    'hgv': value,
                })

    def test_access_whitelist(self):
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'highway': 'unclassified',
                'hgv': 'not_a_whitelisted_value',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'kind': 'minor_road',
                'kind_detail': 'unclassified',
                'hgv': type(None),
            })

    def _check_restriction(self, tags, restriction=None, shield_text=None):
        import dsl

        z, x, y = (16, 0, 0)

        all_tags = tags.copy()
        all_tags.update({
            'highway': 'unclassified',
            'source': 'openstreetmap.org',
        })
        self.generate_fixtures(
            dsl.way(1, dsl.tile_diagonal(z, x, y), all_tags))

        expect = {
            'kind': 'minor_road',
            'kind_detail': 'unclassified',
        }
        if restriction:
            expect['hgv_restriction'] = restriction
        if shield_text:
            expect['hgv_restriction_shield_text'] = shield_text

        self.assert_has_feature(z, x, y, 'roads', expect)

    def test_restriction_weight(self):
        self._check_restriction(
            {'maxweight': 1.5},
            restriction='weight', shield_text='1.5t',
        )

    def test_restriction_height(self):
        self._check_restriction(
            {'maxheight': 2.0},
            restriction='height', shield_text='2m',
        )

    def test_restriction_height_imperial(self):
        # this rounds _down_ to 1.9m, since 6'6" is 1.98m, so that it doesn't
        # mistakenly indicate that a vehicle which is 1.99m would be allowed
        # to pass.
        self._check_restriction(
            {'maxheight': "6'6\""},
            restriction='height', shield_text='1.9m',
        )

    def test_restriction_width(self):
        self._check_restriction(
            {'maxwidth': 3},
            restriction='width', shield_text='3m',
        )

    def test_restriction_width_imperial(self):
        self._check_restriction(
            {'maxwidth': "6'6\""},
            restriction='width', shield_text='1.9m',
        )

    def test_restriction_length(self):
        self._check_restriction(
            {'maxlength': 3},
            restriction='length', shield_text='3m',
        )

    def test_restriction_wpa(self):
        self._check_restriction(
            {'maxaxleload': 1.5},
            restriction='wpa', shield_text='1.5t',
        )

    def test_restriction_hazmat(self):
        self._check_restriction(
            {'hazmat': 'no'},
            restriction='hazmat')

    def test_restriction_multiple(self):
        self._check_restriction(
            {'maxheight': 1.5,
             'maxweight': 1.5},
            restriction='multiple')


class TollTest(FixtureTest):

    def test_toll(self):
        import dsl

        z, x, y = (16, 0, 0)

        values = {
            'yes': True,
            'some_random_value': True,
            'no': type(None),
        }

        for value, expect in values.items():
            self.generate_fixtures(
                dsl.way(1, dsl.tile_diagonal(z, x, y), {
                    'highway': 'unclassified',
                    'toll': value,
                    'source': 'openstreetmap.org',
                }),
            )

            self.assert_has_feature(
                z, x, y, 'roads', {
                    'kind': 'minor_road',
                    'toll': expect,
                })

    def test_hgv_toll(self):
        import dsl

        z, x, y = (16, 0, 0)

        values = {
            'yes': True,
            'some_random_value': True,
            'no': type(None),
        }

        for value, expect in values.items():
            self.generate_fixtures(
                dsl.way(1, dsl.tile_diagonal(z, x, y), {
                    'highway': 'unclassified',
                    'toll:hgv': value,
                    'source': 'openstreetmap.org',
                }),
            )

            self.assert_has_feature(
                z, x, y, 'roads', {
                    'kind': 'minor_road',
                    'toll_hgv': expect,
                })
