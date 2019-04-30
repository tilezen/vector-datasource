# -*- encoding: utf-8 -*-
from . import FixtureTest


class BusStopTest(FixtureTest):

    def test_bus_stop(self):
        import dsl

        z, x, y = (16, 10478, 25331)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/6374841147
            dsl.point(6374841147, (-122.4374762, 37.7749819), {
                'highway': u'bus_stop',
                'name': u'Hayes Street & Divisadero Street',
                'network': u'Muni',
                'operator': u'San Francisco Municipal Railway',
                'public_transport': u'platform',
                'source': u'openstreetmap.org',
                'trolleybus': u'yes',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 6374841147,
                'kind': u'bus_stop',
            })
