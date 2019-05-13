# -*- encoding: utf-8 -*-
from . import FixtureTest


class AerodromeTest(FixtureTest):

    def test_sfo(self):
        # SFO should be "international": both the polygon _and_ the POI.
        import dsl

        z, x, y = (13, 1311, 3170)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/545819287
            dsl.way(545819287, dsl.tile_box(z, x, y), {
                'aerodrome': 'international',
                'aerodrome:type': 'public',
                'aeroway': 'aerodrome',
                'city_served': 'San Francisco, California',
                'ele': '4',
                'iata': 'SFO',
                'icao': 'KSFO',
                'name': 'San Francisco International Airport',
                'source': 'openstreetmap.org',
                'wikidata': 'Q8688',
                'wikipedia': 'en:San Francisco International Airport',
            }),
            # https://www.openstreetmap.org/way/22567191
            dsl.way(22567191, dsl.tile_diagonal(z, x, y), {
                'aeroway': 'runway',
                'length': '3618',
                'ref': '10L/28R',
                'surface': 'asphalt',
                'width': '61',
                'source': 'openstreetmap.org',
            }),
        )

        # POI
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 545819287,
                'kind': 'aerodrome',
                'kind_detail': 'international',
            })

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 545819287,
                'kind': 'aerodrome',
                'kind_detail': 'international',
            })

        # runway inside polygon
        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 22567191,
                'kind': 'aeroway',
                'kind_detail': 'runway',
                'aerodrome_kind_detail': 'international',
            })
