# -*- encoding: utf-8 -*-
from . import FixtureTest


class HideEarlyTramStopTest(FixtureTest):

    def test_tram_stop(self):
        import dsl

        z, x, y = (16, 10482, 25324)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2081705827
            dsl.point(2081705827, (-122.4196615, 37.8020638), {
                'name': u'Hyde Street & Lombard Street',
                'railway': u'tram_stop',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2081705827,
                'kind': u'tram_stop',
                'min_zoom': 16,
            })

    def test_stop(self):
        import dsl

        z, x, y = (16, 10578, 25372)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/53051770
            dsl.point(53051770, (-121.8890223, 37.5941573), {
                'name': u'Sunol',
                'railway': u'stop',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 53051770,
                'kind': u'stop',
                'min_zoom': 16,
            })

    def test_halt(self):
        import dsl

        z, x, y = (16, 10715, 25124)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4560580421
            dsl.point(4560580421, (-121.138147, 38.6654377), {
                'name': u'Oak Avenue Whistlestop',
                'railway': u'halt',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4560580421,
                'kind': u'halt',
                'min_zoom': 16,
            })
