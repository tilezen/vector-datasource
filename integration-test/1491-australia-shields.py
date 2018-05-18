from . import FixtureTest


class AustraliaShieldTest(FixtureTest):
    def test_a_road_in_relation(self):
        import dsl

        z, x, y = (16, 58007, 39547)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'kind': 'admin_area', 'iso_code': 'AU',
                'source': 'openstreetmap.org'
            }),
            # https://www.openstreetmap.org/way/582052008
            dsl.way(582052008, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '60', 'lanes': '2', 'name': 'North East Road',
                'surface': 'paved', 'cycleway': 'lane',
                'source': 'openstreetmap.org', 'oneway': 'yes', 'ref': 'A10',
                'highway': 'primary'
            }),
            dsl.relation(1, {
                'type': 'route', 'route': 'road', 'ref': 'A10',
                'addr:country': 'AU', 'addr:state': 'SA',
                'source': 'openstreetmap.org'
            }, ways=[582052008]),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 582052008, 'shield_text': '10', 'network': 'AU:A-road',
             'all_networks': ['AU:A-road'], 'all_shield_texts': ['10']})

    def test_s_road_in_both_relations(self):
        import dsl

        z, x, y = (16, 60644, 38056)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'kind': 'admin_area', 'iso_code': 'AU',
                'source': 'openstreetmap.org'
            }),
            # https://www.openstreetmap.org/way/240922938
            dsl.way(240922938, dsl.tile_diagonal(z, x, y), {
                'source:name': 'survey', 'maxspeed': '60', 'lanes': '2',
                'name': 'Beaudesert Beenleigh Road',
                'source:maxspeed': 'sign', 'surface': 'asphalt',
                'source': 'openstreetmap.org', 'source:ref': 'survey',
                'ref': '92;T8', 'highway': 'primary', 'network': 'S',
            }),
            dsl.relation(1, {
                'network': 'S', 'ref': '92', 'route': 'road',
                'addr:state': 'QLD', 'source': 'openstreetmap.org',
                'type': 'route', 'addr:country': 'AU',
            }, ways=[240922938]),
            dsl.relation(2, {
                'type': 'route', 'route': 'road', 'ref': '8', 'network': 'T',
                'source': 'openstreetmap.org'
            }, ways=[240922938]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 240922938, 'shield_text': '92', 'network': 'AU:S-route',
                'all_networks': ['AU:S-route', 'AU:T-drive'],
                'all_shield_texts': ['92', '8'],
            })

    def test_s_road_not_in_t_relation(self):
        import dsl

        z, x, y = (16, 60607, 37966)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'kind': 'admin_area', 'iso_code': 'AU',
                'source': 'openstreetmap.org'
            }),
            # https://www.openstreetmap.org/way/13851986
            dsl.way(13851986, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': '31;T8',
                'name': 'Waterworks Road', 'highway': 'primary',
                'surface': 'paved'
            }),
            dsl.relation(1, {
                'network': 'S', 'ref': '31', 'route': 'road',
                'addr:state': 'QLD', 'source': 'openstreetmap.org',
                'type': 'route', 'addr:country': 'AU'
            }, ways=[13851986]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 13851986, 'shield_text': '31', 'network': 'AU:S-route',
                'all_networks': ['AU:S-route', 'AU:T-drive'],
                'all_shield_texts': ['31', '8'],
            })

    def test_s_road_not_in_s_relation(self):
        import dsl

        z, x, y = (16, 60571, 37936)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'kind': 'admin_area', 'iso_code': 'AU',
                'source': 'openstreetmap.org'
            }),
            # https://www.openstreetmap.org/way/16477624
            dsl.way(16477624, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': '31;T9',
                'name': 'Mount Glorious Road', 'highway': 'secondary'
            }),
            dsl.relation(1, {
                'network': 'T', 'ref': '9', 'route': 'road',
                'addr:state': 'QLD', 'source': 'openstreetmap.org',
                'type': 'route', 'addr:country': 'AU'
            }, ways=[16477624]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 16477624, 'shield_text': '9', 'network': 'AU:T-drive',
                'all_networks': ['AU:T-drive', None],
                'all_shield_texts': ['9', '31'],
            })
