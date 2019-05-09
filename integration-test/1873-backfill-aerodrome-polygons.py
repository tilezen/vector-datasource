# -*- encoding: utf-8 -*-
from . import FixtureTest


class AerodromeTest(FixtureTest):

    def test_sfo(self):
        # SFO should be "international": both the polygon _and_ the POI.
        import dsl

        z, x, y = (13, 1311, 3170)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/545819287
            dsl.way(545819287, dsl.box_area(z, x, y, 12545795), {
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
