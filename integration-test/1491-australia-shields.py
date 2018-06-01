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
                'all_networks': ['AU:T-drive', type(None)],
                'all_shield_texts': ['9', '31'],
            })

    def test_s_road_in_zero_relations(self):
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
                'source': 'openstreetmap.org', 'source:ref': 'survey',
                'ref': '92;T8', 'highway': 'primary', 'network': 'S',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 240922938, 'shield_text': '92', 'network': 'AU:S-route',
                'all_networks': ['AU:S-route', 'AU:T-drive'],
                'all_shield_texts': ['92', '8'],
            })

    # test not just a B-road, but one where the text ref has spaces between
    # the additional T-drive refs (i.e: "T 28" rather than "T28").
    def test_b_road_with_spaces(self):
        import dsl

        z, x, y = (16, 60720, 38212)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'kind': 'admin_area', 'iso_code': 'AU',
                'source': 'openstreetmap.org',
            }),
            # https://www.openstreetmap.org/way/131293316
            dsl.way(131293316, dsl.tile_diagonal(z, x, y), {
                'source:name': 'NSW LPI Base Map', 'name': 'Myocum Road',
                'source:name:date': '2016-02', 'surface': 'asphalt',
                'source:date': '2016-07', 'source': 'openstreetmap.org',
                'oneway': 'yes', 'ref': 'B62;T 28;T 30', 'highway': 'primary',
            }),
            dsl.relation(1, {
                'ref': 'B62', 'route': 'road', 'addr:state': 'NSW',
                'source': 'openstreetmap.org', 'type': 'route',
                'addr:country': 'AU',
            }, ways=[131293316]),
            dsl.relation(2, {
                'type': 'route', 'route': 'road', 'ref': '30', 'network': 'T',
                'source': 'openstreetmap.org',
            }, ways=[131293316]),
            dsl.relation(3, {
                'type': 'route', 'route': 'road', 'ref': '28', 'network': 'T',
                'source': 'openstreetmap.org',
            }, ways=[131293316]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 131293316, 'shield_text': '62', 'network': 'AU:B-road',
                'all_networks': ['AU:B-road', 'AU:T-drive', 'AU:T-drive'],
                'all_shield_texts': ['62', '28', '30'],
            })

    def test_c_road(self):
        import dsl

        z, x, y = (16, 59435, 40315)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'kind': 'admin_area', 'iso_code': 'AU',
                'source': 'openstreetmap.org',
            }),
            # https://www.openstreetmap.org/way/7787334
            dsl.way(7787334, dsl.tile_diagonal(z, x, y), {
                'name': 'Churchill - Traralgon Road', 'surface': 'paved',
                'source': 'openstreetmap.org', 'oneway': 'yes',
                'ref': 'C475;C476', 'highway': 'secondary',
            }),
            dsl.relation(1, {
                'name': 'Mattingley Hill Road', 'ref': 'C475', 'route': 'road',
                'addr:state': 'VIC', 'source': 'openstreetmap.org',
                'type': 'route', 'addr:country': 'AU',
            }, ways=[7787334]),
            dsl.relation(2, {
                'ref': 'C476', 'route': 'road', 'addr:state': 'VIC',
                'source': 'openstreetmap.org', 'type': 'route',
                'addr:country': 'AU',
            }, ways=[7787334]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 7787334, 'shield_text': '475', 'network': 'AU:C-road',
                'all_shield_texts': ['475', '476'],
                'all_networks': ['AU:C-road', 'AU:C-road'],
            })

    # this appears to be a typo - i can't find any reference to a "D83" road,
    # and "The Outback Highway" (another name for Barndioota Road?) appears to
    # be *B83* according to Wikipedia:
    # https://en.wikipedia.org/wiki/Barndioota_Road
    #
    # so, given that this doesn't correspond to a known highway type in AU,
    # we emit this with a network type of None, since we can't figure it out
    # from the available information.
    def test_d_road(self):
        import dsl

        z, x, y = (16, 57903, 38425)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'kind': 'admin_area', 'iso_code': 'AU',
                'source': 'openstreetmap.org'
            }),
            # https://www.openstreetmap.org/way/229978585
            dsl.way(229978585, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '80', 'lanes': '2', 'name': 'The Outback Highway',
                'source': 'openstreetmap.org', 'surface': 'paved',
                'name:source': 'data.sa.gov.au roads', 'ref': 'D83',
                'highway': 'secondary',
            }),
            dsl.relation(1, {
                'type': 'route', 'route': 'road', 'ref': 'D83',
                'source': 'openstreetmap.org'
            }, ways=[229978585]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 229978585, 'shield_text': '83', 'network': type(None),
            })

    def test_m_road(self):
        import dsl

        z, x, y = (16, 60296, 39327)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'kind': 'admin_area', 'iso_code': 'AU',
                'source': 'openstreetmap.org'
            }),
            # https://www.openstreetmap.org/way/3188239
            dsl.way(3188239, dsl.tile_diagonal(z, x, y), {
                'old_ref': '1', 'maxspeed': '60', 'lanes': '2',
                'name': 'Cahill Expressway', 'toll': 'yes',
                'surface': 'asphalt', 'source': 'openstreetmap.org',
                'ref:start_date': '2013-08', 'oneway': 'yes', 'ref': 'M1',
                'highway': 'motorway', 'old_network': 'MR',
            }),
            dsl.relation(1, {
                'ref': 'M1', 'route': 'road', 'addr:state': 'NSW',
                'source': 'openstreetmap.org', 'type': 'route',
                'addr:country': 'AU'
            }, ways=[3188239]),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 3188239, 'shield_text': '1', 'network': 'AU:M-road'})

    # https://en.wikipedia.org/wiki/City_Ring_Route,_Adelaide
    def test_ring_route(self):
        import dsl

        z, x, y = (16, 58001, 39557)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'kind': 'admin_area', 'iso_code': 'AU',
                'source': 'openstreetmap.org',
            }),
            # https://www.openstreetmap.org/way/7795168
            dsl.way(7795168, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '60', 'name': 'Hackney Road', 'surface': 'asphalt',
                'cycleway': 'lane', 'source': 'openstreetmap.org',
                'postal_code': '5069', 'oneway': 'yes', 'ref': 'R1',
                'highway': 'primary',
            }),
            dsl.relation(1, {
                'ref': 'R1', 'route': 'road', 'addr:state': 'SA',
                'source': 'openstreetmap.org', 'type': 'route',
                'addr:country': 'AU'
            }, ways=[7795168]),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 7795168, 'shield_text': '1', 'network': 'AU:R-route'})

    def test_metroad(self):
        import dsl

        z, x, y = (16, 60622, 37990)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_box(z, x, y), {
                'kind': 'admin_area', 'iso_code': 'AU',
                'source': 'openstreetmap.org',
            }),
            # https://www.openstreetmap.org/way/463027243
            dsl.way(463027243, dsl.tile_diagonal(z, x, y), {
                'maxspeed': '60', 'lanes': '2', 'name': 'Granard Road',
                'surface': 'asphalt', 'source': 'openstreetmap.org',
                'oneway': 'yes', 'ref': 'MR2', 'highway': 'trunk',
                'network': 'MR',
            }),
            dsl.relation(1, {
                'type': 'route', 'route': 'road', 'ref': '2', 'network': 'MR',
                'source': 'openstreetmap.org',
            }, ways=[463027243]),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 463027243, 'shield_text': '2', 'network': 'AU:Metro-road'})
