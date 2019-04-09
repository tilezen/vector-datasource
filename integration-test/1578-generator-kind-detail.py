# -*- encoding: utf-8 -*-
from . import FixtureTest


class GeneratorTest(FixtureTest):

    def test_nuclear_generator(self):
        import dsl

        z, x, y = (16, 32942, 21964)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2697712892
            dsl.point(2697712892, (0.9602262, 50.9137851), {
                'generator:output:electricity': u'600 MW',
                'generator:source': u'nuclear',
                'generator:type': u'AGR',
                'name': u'Dungeness B Reactor 2',
                'power': u'generator',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2697712892,
                'kind': u'generator',
                'kind_detail': u'nuclear',
            })

    def test_wind_generator(self):
        import dsl

        z, x, y = (16, 32817, 21990)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4640594887
            dsl.point(4640594887, (0.2736757, 50.8255855), {
                'description': u'Shepham wind farm (Mid)',
                'generator:method': u'wind_turbine',
                'generator:source': u'wind',
                'note': u'Approximate location',
                'power': u'generator',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4640594887,
                'kind': u'generator',
                'kind_detail': u'wind',
            })

    def test_solar_generator(self):
        import dsl

        z, x, y = (16, 32892, 21451)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3704770949
            dsl.point(3704770949, (0.6836448, 52.6564959), {
                'generator:source': u'solar',
                'operator': u'Ecotricity',
                'power': u'generator',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3704770949,
                'kind': u'generator',
                'kind_detail': u'solar',
            })
