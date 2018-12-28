# -*- encoding: utf-8 -*-
from . import FixtureTest


class BikeShopTest(FixtureTest):

    def test_bicycle_shop_node(self):
        import dsl

        z, x, y = (16, 10479, 25331)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2484293076
            dsl.point(2484293076, (-122.432202, 37.771036), {
                'addr:city': 'San Francisco',
                'addr:housenumber': '520',
                'addr:street': 'Waller Street',
                'name': 'Wiggle Bicycles',
                'opening_hours': 'Tu-Fr 10:00-18:30; Sa-Su 10:00-17:00',
                'service:bicycle:diy': 'no',
                'service:bicycle:pump': 'yes',
                'service:bicycle:repair': 'yes',
                'shop': 'bicycle',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2484293076,
                'kind': 'bicycle',
                'min_zoom': 17,
            })

    def test_bicycle_shop_large_way(self):
        import dsl

        z, x, y = (15, 5242, 12665)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/260354461
            dsl.way(260354461, dsl.box_area(z, x, y, 723), {
                'addr:city': 'San Francisco',
                'addr:housenumber': '1090',
                'addr:postcode': '94103',
                'addr:state': 'CA',
                'addr:street': 'Folsom Street',
                'building': 'yes',
                'height': '7',
                'name': 'SF Bike Connection',
                'shop': 'bicycle',
                'source': 'openstreetmap.org',
                'website': 'http://bikeconnection.net/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 260354461,
                'kind': 'bicycle',
                # should be in z15 tile, so min_zoom between 15 and 16
                'min_zoom': lambda z: 15 <= z < 16,
            })

    def test_bicycle_shop_small_way(self):
        import dsl

        z, x, y = (16, 10476, 25332)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/264534357
            dsl.way(264534357, dsl.box_area(z, x, y, 362), {
                'addr:city': 'San Francisco',
                'addr:housenumber': '858',
                'addr:postcode': '94117',
                'addr:street': 'Stanyan Street',
                'building': 'yes',
                'height': '5',
                'name': 'American Cyclery Too',
                'operator': 'American Cyclery',
                'service:bicycle:pump': 'yes',
                'service:bicycle:repair': 'yes',
                'service:bicycle:retail': 'yes',
                'service:bicycle:second_hand': 'yes',
                'shop': 'bicycle',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 264534357,
                'kind': 'bicycle',
                # min_zoom between 16 and 17, less than the node at z17
                'min_zoom': lambda z: 16 <= z < 17,
            })


class TheatreTest(FixtureTest):

    def test_theatre_node(self):
        import dsl

        z, x, y = (16, 10483, 25329)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/358805392
            dsl.point(358805392, (-122.411371, 37.782168), {
                'amenity': 'theatre',
                'ele': '14',
                'gnis:county_id': '075',
                'gnis:created': '01/01/1995',
                'gnis:feature_id': '1657186',
                'gnis:state_id': '06',
                'name': 'Market Street Theatre',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 358805392,
                'kind': 'theatre',
                'min_zoom': 17,
            })

    def test_theatre_medium_way(self):
        import dsl

        z, x, y = (16, 10483, 25330)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/35115840
            dsl.way(35115840, dsl.box_area(z, x, y, 4782), {
                'amenity': 'theatre',
                'building': 'yes',
                'height': '46 m',
                'name': 'Orpheum Theatre',
                'source': 'openstreetmap.org',
                'wikidata': 'Q7103971',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 35115840,
                'kind': 'theatre',
                'min_zoom': lambda z: 16 <= z < 17,
            })

    def test_theatre_large_way(self):
        import dsl

        z, x, y = (15, 9650, 12314)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/266170808
            dsl.way(266170808, dsl.box_area(z, x, y, 7492), {
                'amenity': 'theatre',
                'building': 'yes',
                'building:colour': '#CAC3A9',
                'building:part': 'yes',
                'height': '30',
                'name': 'Radio City Music Hall',
                'nycdoitt:bin': '1083862',
                'opening_hours': '09:30-17:00',
                'roof:colour': '#956C66',
                'roof:material': 'concrete',
                'roof:shape': 'flat',
                'source': 'openstreetmap.org',
                'tourism': 'yes',
                'website': 'http://www.radiocity.com/',
                'wikidata': 'Q753437',
                'wikipedia': 'en:Radio City Music Hall',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 266170808,
                'kind': 'theatre',
                'min_zoom': lambda z: 15 <= z < 16,
            })


class WaterTowerTest(FixtureTest):

    def test_water_tower_no_height(self):
        import dsl

        z, x, y = (16, 10477, 25334)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/247759532
            dsl.way(247759532, dsl.box_area(z, x, y, 448), {
                'man_made': 'water_tower',
                'name': 'Ashbury tank',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 247759532,
                'kind': 'water_tower',
                'min_zoom': 17,
            })

    def test_water_tower_tall(self):
        import dsl

        z, x, y = (15, 5240, 12671)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/424957085
            dsl.way(424957085, dsl.box_area(z, x, y, 146), {
                'building': 'yes',
                'height': '23',
                'man_made': 'water_tower',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 424957085,
                'kind': 'water_tower',
                'min_zoom': 15,
            })

    def test_water_tower_short(self):
        import dsl

        z, x, y = (16, 11310, 26168)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/470968538
            dsl.way(470968538, dsl.box_area(z, x, y, 198), {
                'ele': '300.5',
                'height': '10.9',
                'lacounty:ain': '8277036900',
                'lacounty:bld_id': '600581840682',
                'man_made': 'water_tower',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 470968538,
                'kind': 'water_tower',
                'min_zoom': 16,
            })
