# -*- encoding: utf-8 -*-
from . import FixtureTest


class ModifyPoniZoomsTest(FixtureTest):

    def test_sports_pitch_with_name(self):
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'leisure': 'pitch',
                'name': 'Foo pitch',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1,
                'min_zoom': 16,
                'kind': 'pitch',
            })

    def test_sports_pitch_no_name(self):
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'leisure': 'pitch',
                'sport': 'basketball',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1,
                'min_zoom': 17,
                'kind': 'pitch',
            })

    def test_sports_pitch_no_name_volleyball(self):
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'leisure': 'pitch',
                'sport': 'volleyball',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1,
                'min_zoom': 17,
                'kind': 'pitch',
            })

    def test_drinking_water(self):
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_centre_shape(z, x, y), {
                'amenity': 'drinking_water',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'kind': 'drinking_water',
                'min_zoom': 18,
            })

    def _check_downgrade_poi(self, tags, kind, min_zoom):
        import dsl

        z, x, y = (16, 0, 0)

        full_tags = tags.copy()
        full_tags['source'] = 'openstreetmap.org'

        # test without a name
        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), full_tags),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'kind': kind,
                'min_zoom': min_zoom,
            })

        # and with a name
        full_tags['name'] = 'Some kind of name'
        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), full_tags),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'kind': kind,
                'name': full_tags['name'],
                'min_zoom': lambda z: z < min_zoom,
            })

    def test_information(self):
        self._check_downgrade_poi(
            {'tourism': 'information'},
            'information', 18)

    def test_playground(self):
        self._check_downgrade_poi(
            {'leisure': 'playground'},
            'playground', 18)

    def test_bicycle_parking(self):
        self._check_downgrade_poi(
            {'amenity': 'bicycle_parking'},
            'bicycle_parking', 19)

    def test_toilets(self):
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_centre_shape(z, x, y), {
                'amenity': 'toilets',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'kind': 'toilets',
                'min_zoom': 18,
            })

    def test_traffic_signals(self):
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_centre_shape(z, x, y), {
                'highway': 'traffic_signals',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'kind': 'traffic_signals',
                'min_zoom': 18,
            })
