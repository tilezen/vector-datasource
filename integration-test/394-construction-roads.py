# -*- encoding: utf-8 -*-
from . import FixtureTest


class ConstructionTest(FixtureTest):

    def test_residential(self):
        import dsl

        z, x, y = (16, 10492, 25319)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/215879087
            dsl.way(215879087, dsl.tile_diagonal(z, x, y), {
                'construction': u'residential',
                'highway': u'construction',
                'name': u'4th Street',
                'source': u'openstreetmap.org',
                'tiger:cfcc': u'A41',
                'tiger:county': u'San Francisco, CA',
                'tiger:name_base': u'4th',
                'tiger:name_type': u'St',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 215879087,
                'kind': u'construction',
                'kind_detail': u'residential',
                'min_zoom': 12,
            })

    def test_motorway_link(self):
        import dsl

        z, x, y = (16, 10492, 25322)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/236455470
            dsl.way(236455470, dsl.tile_diagonal(z, x, y), {
                'construction': u'motorway_link',
                'destination': u'Yerba Buena island',
                'highway': u'construction',
                'oneway': u'yes',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 236455470,
                'kind': u'construction',
                'kind_detail': u'motorway_link',
                'min_zoom': 12,
            })

    def test_tertiary(self):
        import dsl

        z, x, y = (16, 10492, 25322)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/11416105
            dsl.way(11416105, dsl.tile_diagonal(z, x, y), {
                'construction': u'tertiary',
                'highway': u'construction',
                'oneway': u'yes',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 11416105,
                'kind': u'construction',
                'kind_detail': u'tertiary',
                'min_zoom': 12,
            })

    def test_cycleway(self):
        import dsl

        z, x, y = (16, 10492, 25322)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/662177827
            dsl.way(662177827, dsl.tile_diagonal(z, x, y), {
                'construction': u'cycleway',
                'foot': u'yes',
                'highway': u'construction',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 662177827,
                'kind': u'construction',
                'kind_detail': u'cycleway',
                'min_zoom': 13,
            })
