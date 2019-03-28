# -*- encoding: utf-8 -*-
from . import FixtureTest


class MilitaryAirfieldTest(FixtureTest):

    def test_combo(self):
        # tagged both military=airfield and aeroway=aerodrome, prefer
        # (military) airfield as per
        # https://github.com/tilezen/vector-datasource/issues/1580
        import dsl

        z, x, y = (16, 32459, 21686)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/412044660
            dsl.point(412044660, (-1.69678, 51.8666626), {
                'aeroway': u'aerodrome',
                'closest_town': u'Bourton-on-the-Water',
                'ele': u'223',
                'icao': u'EGVL',
                'military': u'airfield',
                'name': u'RAF Little Rissington',
                'operator': u'Royal Air Force',
                'source': u'openstreetmap.org',
                'wikidata': u'Q7275442',
                'wikipedia': u'en:RAF Little Rissington',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 412044660,
                'kind': u'airfield',
            })

    def test_solo(self):
        # test military=airfield by itself
        import dsl

        z, x, y = (16, 32450, 21880)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4226596407
            dsl.point(4226596407, (-1.7449519, 51.2060171), {
                'military': u'airfield',
                'name': u'Bulford Field',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4226596407,
                'kind': u'airfield',
            })

    def test_combo_poly(self):
        # combo tagging with polygon
        import dsl

        z, x, y = (16, 32692, 21778)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/166164837
            dsl.way(166164837, dsl.box_area(z, x, y, 4991683), {
                'aerodrome': 'military',
                'aeroway': 'aerodrome',
                'iata': 'NHT',
                'icao': 'EGWU',
                'landuse': 'military',
                'military': 'airfield',
                'name': 'RAF Northolt',
                'operator': 'Royal Air Force',
                'ref': 'NHT',
                'source': 'openstreetmap.org',
                'wikidata': 'Q106119',
                'wikipedia': 'en:RAF Northolt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 166164837,
                'kind': 'airfield',
            })

        # check landuse too
        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 166164837,
                'kind': 'airfield',
            })

    def test_solo_way(self):
        import dsl

        z, x, y = (16, 32744, 21517)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/164058691
            dsl.way(164058691, dsl.box_area(z, x, y, 1793476), {
                'closed:aeroway': 'aerodrome',
                'military': 'airfield',
                'name': 'RAF Upwood',
                'source': 'openstreetmap.org',
                'wikidata': 'Q7275648',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 164058691,
                'kind': 'airfield',
            })
