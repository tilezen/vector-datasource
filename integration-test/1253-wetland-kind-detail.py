# -*- encoding: utf-8 -*-
from . import FixtureTest


class WetlandTest(FixtureTest):

    def test_landuse_saltmarsh(self):
        import dsl

        z, x, y = (16, 19323, 24662)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/50977043
            dsl.way(50977043, dsl.box_area(z, x, y, 122442), {
                'boundary': 'national_park',
                'landuse': 'meadow',
                'natural': 'wetland',
                'place': 'island',
                'source': 'openstreetmap.org',
                'wetland': 'saltmarsh',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 50977043,
                'kind': 'wetland',
                'kind_detail': 'saltmarsh',
            })

    def test_yellow_bar_hassock(self):
        import dsl

        z, x, y = (16, 19325, 24665)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/50976996
            dsl.way(50976996, dsl.box_area(z, x, y, 930605), {
                'boundary': 'national_park',
                'ele': '0',
                'gnis:county_id': '047',
                'gnis:created': '01/23/1980',
                'gnis:feature_id': '971817',
                'gnis:state_id': '36',
                'name': 'Yellow Bar Hassock',
                'natural': 'wetland',
                'place': 'island',
                'source': 'openstreetmap.org',
                'wetland': 'saltmarsh',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 50976996,
                'kind': 'wetland',
                'kind_detail': 'saltmarsh',
            })

    def test_ruffle_bar(self):
        # sounds like candy...
        import dsl

        z, x, y = (16, 19322, 24667)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/110163359
            dsl.way(110163359, dsl.box_area(z, x, y, 900561), {
                'boundary': 'national_park',
                'ele': '4',
                'gnis:county_id': '047',
                'gnis:created': '01/23/1980',
                'gnis:feature_id': '963071',
                'gnis:state_id': '36',
                'name': 'Ruffle Bar',
                'natural': 'wetland',
                'place': 'island',
                'source': 'openstreetmap.org',
                'wetland': 'saltmarsh',
                'wikidata': 'Q15273739',
                'wikipedia': 'en:Ruffle Bar',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 110163359,
                'kind': 'wetland',
                'kind_detail': 'saltmarsh',
            })

    def test_big_egg_marsh(self):
        import dsl

        z, x, y = (16, 19327, 24668)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/50977027
            dsl.way(50977027, dsl.box_area(z, x, y, 254547), {
                'addr:state': 'NY',
                'boundary': 'national_park',
                'ele': '0',
                'gnis:county_name': 'Queens',
                'gnis:created': '01/23/1980',
                'gnis:feature_id': '943878',
                'gnis:feature_type': 'Swamp',
                'name': 'Big Egg Marsh',
                'natural': 'wetland',
                'place': 'island',
                'source': 'openstreetmap.org',
                'wetland': 'saltmarsh',
                'wikidata': 'Q34642571',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 50977027,
                'kind': 'wetland',
                'kind_detail': 'saltmarsh',
            })
