# -*- encoding: utf-8 -*-
from . import FixtureTest


class PostOfficeTest(FixtureTest):

    def test_post_office(self):
        import dsl

        z, x, y = (14, 2627, 6327)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/28842845
            dsl.way(28842845, dsl.tile_box(z, x, y), {
                'addr:city': 'Berkeley',
                'addr:country': 'US',
                'addr:housenumber': '2000',
                'addr:postcode': '94704',
                'addr:state': 'CA',
                'addr:street': 'Allston Way',
                'amenity': 'post_office',
                'building': 'civic',
                'name': 'Berkeley Main Post Office',
                'opening_hours': 'Mo-Fr 06:00-20:00; Sa 06:00-18:00',
                'source': 'openstreetmap.org',
                'wheelchair': 'yes',
                'wikidata': 'Q16902347',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 28842845,
                'kind': 'post_office',
                'min_zoom': 14,
            })

    def test_bank_14_way(self):
        import dsl

        z, x, y = (14, 2741, 6393)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/61820736
            dsl.way(61820736, dsl.tile_box(z, x, y), {
                'amenity': 'bank',
                'name': 'Bank of America',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 61820736,
                'kind': 'bank',
                'min_zoom': 14,
            })

    def test_cinema_14_way(self):
        import dsl

        z, x, y = (14, 2727, 6378)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/182809243
            dsl.way(182809243, dsl.tile_box(z, x, y), {
                'amenity': 'cinema',
                'name': 'Madera Drive-In Cinema 2',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 182809243,
                'kind': 'cinema',
                'min_zoom': 14,
            })

    def test_courthouse_14_way(self):
        import dsl

        z, x, y = (14, 2655, 6395)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/36802788
            dsl.way(36802788, dsl.tile_box(z, x, y), {
                'ALAND': '27250',
                'amenity': 'courthouse',
                'AREAID': '110411442188',
                'AWATER': '0',
                'COUNTYFP': '053',
                'latitude': '+36.6740857',
                'longitude': '-121.6593174',
                'MTFCC': 'K2165',
                'name': 'Salinas Civic Center',
                'source': 'openstreetmap.org',
                'STATEFP': '06',
                'Tiger:MTFCC': 'K2165',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 36802788,
                'kind': 'courthouse',
                'min_zoom': 14,
            })

    def test_embassy_14_way(self):
        import dsl

        z, x, y = (14, 2808, 6541)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/427270582
            dsl.way(427270582, dsl.tile_box(z, x, y), {
                'amenity': 'embassy',
                'building': 'yes',
                'country': 'ID',
                'diplomatic': 'consulate_general',
                'ele': '94.9',
                'height': '30.1',
                'lacounty:ain': '5502031015',
                'lacounty:bld_id': '470938845107',
                'name': 'Consulat General of the Republic of Indonesia',
                'name:id': 'Konsulat Jenderal Republik Indonesian',
                'source': 'openstreetmap.org',
                'start_date': '1946',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 427270582,
                'kind': 'embassy',
                'min_zoom': 14,
            })

    def test_fire_station_14_way(self):
        import dsl

        z, x, y = (14, 2841, 6539)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/35261044
            dsl.way(35261044, dsl.tile_box(z, x, y), {
                'addr:city': 'Rancho Cucamonga',
                'addr:housenumber': '11297',
                'addr:postcode': '91730',
                'addr:state': 'CA',
                'addr:street': 'Jersey Boulevard',
                'amenity': 'fire_station',
                'name': 'RCFD Jersey Station',
                'ref': '#174',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 35261044,
                'kind': 'fire_station',
                'min_zoom': 14,
            })

    def test_police_14_way(self):
        import dsl

        z, x, y = (14, 2835, 6539)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/146579135
            dsl.way(146579135, dsl.tile_box(z, x, y), {
                'amenity': 'police',
                'name': 'Montclair Police',
                'source': 'openstreetmap.org',
                'source_ref': 'AM909_DSCY3410',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 146579135,
                'kind': 'police',
                'min_zoom': 14,
            })

    def test_post_office_14_way(self):
        import dsl

        z, x, y = (14, 2857, 6541)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/45274545
            dsl.way(45274545, dsl.tile_box(z, x, y), {
                'addr:city': 'San Bernardino',
                'addr:housenumber': '1900',
                'addr:postcode': '92403',
                'addr:state': 'CA',
                'addr:street': 'West Redlands Boulevard',
                'amenity': 'post_office',
                'building': 'yes',
                'name': 'USPS San Bernardino Processing & Distribution Center',
                'operator': 'United States Postal Service',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 45274545,
                'kind': 'post_office',
                'min_zoom': 14,
            })

    def test_theatre_15_way(self):
        import dsl

        z, x, y = (15, 5612, 13077)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/133701914
            dsl.way(133701914, dsl.box_area(z, x, y, 24691), {
                'amenity': 'theatre',
                'name': 'Hollywood Bowl',
                'source': 'openstreetmap.org',
                'wikipedia': 'en:Hollywood Bowl',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 133701914,
                'kind': 'theatre',
                'min_zoom': 15,
            })

    def test_library_14_way(self):
        import dsl

        z, x, y = (14, 2646, 6359)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/26297898
            dsl.way(26297898, dsl.tile_box(z, x, y), {
                'amenity': 'library',
                'created_by': 'Potlatch 0.10b',
                'name': 'Tully Community Branch Library',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 26297898,
                'kind': 'library',
                'min_zoom': 14,
            })

    def test_fuel_14_way(self):
        import dsl

        z, x, y = (14, 2660, 6284)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/199461228
            dsl.way(199461228, dsl.tile_box(z, x, y), {
                'addr:city': 'Sacramento',
                'addr:housenumber': '2701',
                'addr:postcode': '95833',
                'addr:street': 'Orchard Lane',
                'amenity': 'fuel',
                'landuse': 'commercial',
                'name': 'Arco',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 199461228,
                'kind': 'fuel',
                'min_zoom': 14,
            })
