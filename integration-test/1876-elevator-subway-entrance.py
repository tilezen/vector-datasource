# -*- encoding: utf-8 -*-
from . import FixtureTest


class BusStopTest(FixtureTest):

    def test_elevator(self):
        import dsl

        z, x, y = (16, 10482, 25333)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3570271795
            dsl.point(3570271795, (-122.4195493, 37.7653381), {
                'bicycle': u'yes',
                'highway': u'elevator',
                'railway': u'subway_entrance',
                'source': u'openstreetmap.org',
                'wheelchair': u'yes',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3570271795,
                'kind': u'elevator',
            })
