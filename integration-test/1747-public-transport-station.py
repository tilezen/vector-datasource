# -*- encoding: utf-8 -*-
from . import FixtureTest


class PublicTransportStationTest(FixtureTest):

    def test_station_node(self):
        import dsl

        z, x, y = (16, 10522, 25402)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2160213344
            dsl.point(2160213344, (-122.197968, 37.464501), {
                'name': 'Atherton',
                'network': 'Caltrain',
                'note': 'Weekend local service only',
                'opening_hours': 'Sa,Su',
                'public_transport': 'station',
                'railway': 'halt',
                'source': 'openstreetmap.org',
                'wikidata': 'Q4813588',
                'wikipedia': 'en:Atherton (Caltrain station)',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2160213344,
                'kind': 'station',
            })
