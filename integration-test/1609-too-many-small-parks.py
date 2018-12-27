# -*- encoding: utf-8 -*-
from . import FixtureTest


class ParkTest(FixtureTest):

    def test_adirondack(self):
        import dsl

        z, x, y = (8, 75, 93)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/1695394
            dsl.way(1695394, dsl.box_area(z, x, y, 45506933692), {
                'boundary': 'national_park',
                'name': 'Adirondack Park',
                'source': 'openstreetmap.org',
                'type': 'multipolygon',
                'wikidata': 'Q357550',
                'wikipedia': 'en:Adirondack Park',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1695394,
                'kind': 'park',
                'min_zoom': 8,
            })

    def test_humboldt_redwoods(self):
        import dsl

        z, x, y = (9, 79, 193)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/181771
            dsl.way(181771, dsl.box_area(z, x, y, 371054814), {
                'attribution': 'CASIL CSP_Opbdys072008',
                'boundary': 'national_park',
                'boundary_1': 'protected_area',
                'csp:globalid': '{77E28E1D-AF1A-413A-85DF-A110183E3544}',
                'csp:unitcode': '119',
                'ele': '461',
                'gnis:county_id': '023',
                'gnis:created': '01/19/1981',
                'gnis:feature_id': '234054',
                'gnis:state_id': '06',
                'name': 'Humboldt Redwoods State Park',
                'park:type': 'state_park',
                'source': 'openstreetmap.org',
                'type': 'multipolygon',
                'wikidata': 'Q2894242',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 181771,
                'kind': 'park',
                'min_zoom': 9,
            })

    def test_san_bruno(self):
        import dsl

        z, x, y = (10, 163, 396)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/38414287
            dsl.way(38414287, dsl.box_area(z, x, y, 15396848), {
                'boundary': 'protected_area',
                'dog': 'no',
                'ele': '378',
                'gnis:county_id': '081',
                'gnis:created': '04/06/1998',
                'gnis:feature_id': '1785780',
                'gnis:state_id': '06',
                'leisure': 'park',
                'name': 'San Bruno Mountain State Park',
                'operator': 'County of San Mateo Parks Department',
                'protect_class': '5',
                'protection_title': 'State Park',
                'source': 'openstreetmap.org',
                'website': 'http://www.parks.ca.gov/?page_id=518',
                'wikidata': 'Q7413484',
                'wikipedia': 'en:San Bruno Mountain State Park',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 38414287,
                'kind': 'park',
                'min_zoom': 10,
            })

    def test_john_mclaren(self):
        import dsl

        z, x, y = (12, 655, 1584)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/28716696
            dsl.way(28716696, dsl.box_area(z, x, y, 2311826), {
                'dog': 'yes',
                'ele': '115',
                'gnis:feature_id': '226271',
                'leisure': 'park',
                'name': 'John McLaren Park',
                'source': 'openstreetmap.org',
                'wikidata': 'Q14683311',
                'wikipedia': 'en:John McLaren Park',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 28716696,
                'kind': 'park',
                'min_zoom': 12,
            })

    def test_mount_sutro_open_space(self):
        import dsl

        z, x, y = (13, 1309, 3166)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/3307684
            dsl.way(3307684, dsl.box_area(z, x, y, 675691), {
                'landuse': 'forest',
                'leisure': 'park',
                'name': 'Mount Sutro Open Space Reserve',
                'source': 'openstreetmap.org',
                'type': 'multipolygon',
                'wood': 'Eucalyptus',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3307684,
                'kind': 'park',
                'min_zoom': 13,
            })

    def test_glen_canyon(self):
        import dsl

        z, x, y = (13, 1309, 3167)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/35800082
            dsl.way(35800082, dsl.box_area(z, x, y, 415604), {
                'gnis:feature_id': '224213',
                'leisure': 'park',
                'name': 'Glen Canyon Park',
                'source': 'openstreetmap.org',
                'wikidata': 'Q5567631',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 35800082,
                'kind': 'park',
                'min_zoom': 13,
            })

    def test_bernal_heights(self):
        import dsl

        z, x, y = (13, 1310, 3167)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/16752188
            dsl.way(16752188, dsl.box_area(z, x, y, 209667), {
                'alt_name': 'Bernal Hill Park',
                'leisure': 'park',
                'name': 'Bernal Heights Park',
                'note': 'Off-leash dog park with no fence.',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 16752188,
                'kind': 'park',
                'min_zoom': 13,
            })

    def test_buena_vista(self):
        import dsl

        z, x, y = (14, 2619, 6333)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/7459901
            dsl.way(7459901, dsl.box_area(z, x, y, 245881), {
                'area': 'yes',
                'leisure': 'park',
                'localwiki': 'sf/Buena Vista Park',
                'name': 'Buena Vista Park',
                'natural': 'wood',
                'source': 'openstreetmap.org',
                'wikidata': 'Q2749189',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 7459901,
                'kind': 'park',
                'min_zoom': 13,
            })

    def test_angelo_rossi(self):
        import dsl

        z, x, y = (15, 5237, 12665)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/69032470
            dsl.way(69032470, dsl.box_area(z, x, y, 40079), {
                'addr:city': 'San Francisco',
                'addr:country': 'US',
                'addr:state': 'CA',
                'area': 'yes',
                'leisure': 'park',
                'name': 'Angelo Rossi Park',
                'phone': '666-7011',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 69032470,
                'kind': 'park',
                'min_zoom': 15,
            })

    def test_grattan_playground(self):
        import dsl

        z, x, y = (16, 10476, 25333)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/27092661
            dsl.way(27092661, dsl.box_area(z, x, y, 9882), {
                'ele': '107',
                'gnis:county_id': '075',
                'gnis:feature_id': '1655649',
                'gnis:state_id': '06',
                'leisure': 'park',
                'name': 'Grattan Playground',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 27092661,
                'kind': 'park',
                'min_zoom': 16,
            })

    def test_29th_and_diamond_node(self):
        import dsl

        z, x, y = (16, 10479, 25338)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/1004280495
            dsl.point(1004280495, (-122.435258, 37.743580), {
                'leisure': 'park',
                'name': '29th & Diamond Open Space',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1004280495,
                'kind': 'park',
                'min_zoom': 16,
            })
