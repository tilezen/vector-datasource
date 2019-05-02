# -*- encoding: utf-8 -*-
from . import FixtureTest


class AerodromeTest(FixtureTest):

    def test_sfo(self):
        # SFO should be international because the "aerodrome" tag is
        # international. that should override the "aerodrome:type=public" tag.
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

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 545819287,
                'kind': 'aerodrome',
                'kind_detail': 'international',
            })

    def test_bes(self):
        # BES should be international, too. it doesn't have aerodrome:type,
        # but should still get the kind_detail from falling back to the
        # "aerodrome" tag.
        import dsl

        z, x, y = (13, 3995, 2832)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/5369273
            dsl.way(5369273, dsl.box_area(z, x, y, 4789953), {
                'aerodrome': 'international',
                'aeroway': 'aerodrome',
                'iata': 'BES',
                'icao': 'LFRB',
                'name': u'A\xe9roport de Brest-Bretagne',
                'name:br': 'Aerborzh Brest-Breizh',
                'ref': 'LFRB',
                'source': 'openstreetmap.org',
                'wikidata': 'Q1191525',
                'wikipedia': u'fr:A\xe9roport Brest Bretagne',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5369273,
                'kind': 'aerodrome',
                'kind_detail': 'international',
            })

    def test_mex(self):
        # although MEX doesn't have an "aerodrome:type" of international, and
        # no "aerodrome" tag, there's still an "international_flights" tag we
        # can use to determine this.
        import dsl

        z, x, y = (13, 1841, 3645)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/99909133
            dsl.way(99909133, dsl.box_area(z, x, y, 8005638), {
                'aerodrome:type': 'public',
                'aeroway': 'aerodrome',
                'barrier': 'fence',
                'ele': '2238',
                'fence_type': 'wire',
                'iata': 'MEX',
                'icao': 'MMMX',
                'international_flights': 'yes',
                'is_in': 'Mexico City,D.F.,Mexico',
                'name': u'Aeropuerto Internacional de la Ciudad de M\xe9xico',
                'name:en': 'Mexico City International Airport',
                'operator': u'Grupo Aeroportuario de la Ciudad de M\xe9xico',
                'passengers': '33000000',
                'source': 'openstreetmap.org',
                'wikidata': 'Q860559',
                'wikipedia': 'en:Mexico City International Airport',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 99909133,
                'kind': 'aerodrome',
                'kind_detail': 'international',
            })

    def test_tpe(self):
        # TPE doesn't have "aerodrome" or "aerodrome:type" tags, so we look at
        # the join to Wikidata for the passenger numbers.
        import dsl

        z, x, y = (13, 6854, 3506)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/321502590
            dsl.way(321502590, dsl.box_area(z, x, y, 13507964), {
                'aeroway': 'aerodrome',
                'barrier': 'wall',
                'ele': '33',
                'iata': 'TPE',
                'icao': 'RCTP',
                'IFR': 'yes',
                'name': u'\u81fa\u7063\u6843\u5712\u570b\u969b\u6a5f\u5834',
                'name:af': 'Taiwan Taoyuan Internasionale Lughawe',
                'name:de': 'Flughafen Taiwan Taoyuan',
                'name:en': 'Taiwan Taoyuan International Airport',
                'name:es': u'Aeropuerto Internacional de Taiw\xe1n Taoyuan',
                'name:fr': u'A\xe9roport international Taiwan-Taoyuan',
                'source': 'openstreetmap.org',
                'variation': '4 W 2014 0.04 W',
                'website': 'https://www.taoyuan-airport.com/',
                'wikidata': 'Q44856',
                'wikipedia:en': 'Taiwan_Taoyuan_International_Airport',
                'passenger_count': '46535180',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 321502590,
                'kind': 'aerodrome',
                'kind_detail': 'international',
            })

    def test_aci(self):
        # ACI is a regional airport, carrying around 100,000 passengers a year.
        # however, it has no tags on it to indicate it's more important than a
        # flying club airfield. so we use the passenger count to backfill that.
        import dsl

        z, x, y = (15, 16182, 11154)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/384693131
            dsl.way(384693131, dsl.box_area(z, x, y, 601403), {
                'aeroway': 'aerodrome',
                'alt_name': 'The Blaye',
                'ele': '88',
                'iata': 'ACI',
                'icao': 'EGJA',
                'is_in': 'Alderney,Channel Islands,UK',
                'name': 'Alderney Airport',
                'operator': 'States of Guernsey',
                'ref': 'ACI',
                'source': 'openstreetmap.org',
                'start_date': '1935',
                'type': 'civil',
                'wikidata': 'Q2559952',
                'wikipedia': 'en:Alderney Airport',
                'passenger_count': '105458',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 384693131,
                'kind': 'aerodrome',
                'kind_detail': 'regional',
            })
