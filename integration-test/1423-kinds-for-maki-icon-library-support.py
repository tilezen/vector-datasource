# -*- encoding: utf-8 -*-
from . import FixtureTest


class KindsForMakiIconSupportTest(FixtureTest):

    def test_airfield_node(self):
        import dsl

        z, x, y = (16, 40052, 53633)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/368396366
            dsl.point(368396366, (40.0168224, -74.591995), {
                'addr:state': u'NJ',
                'aerodrome:type': u'military',
                'ele': u'43',
                'gnis:county_name': u'Burlington',
                'gnis:created': u'08/01/1994',
                'gnis:feature_id': u'884993,2512291',
                'gnis:feature_type': u'Airport',
                'iata': u'WRI',
                'icao': u'KWRI',
                'is_in:iso_3166_2': u'US-NJ',
                'landuse': u'military',
                'military': u'airfield',
                'name': u'McGuire Air Force Base',
                'owner': u'US Air Force',
                'source': u'openstreetmap.org',
                'wikidata': u'Q10860392',
                'wikipedia': u'en:McGuire Air Force Base',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 368396366,
                'kind': u'airfield',
            })

    def test_airfield_way(self):
        # NOTE: i think  this is probably _not_ actually a military airfield.
        # seems to be the site of the Radio Control Society of Marine Park
        # http://www.rcsmp.com/ - but useful as a test nonetheless.
        import dsl

        z, x, y = (16, 40157, 53181)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/468561706
            dsl.way(468561706, dsl.tile_box(z, x, y), {
                'military': u'airfield',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 468561706,
                'kind': u'airfield',
            })

    def test_chain_gate_node(self):
        import dsl

        z, x, y = (16, 40298, 52851)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/1786890652
            dsl.point(1786890652, (41.3686973, -73.4087426), {
                'barrier': u'chain',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1786890652,
                'kind': u'gate',
                'kind_detail': u'chain',
            })

    def test_kissing_gate_gate_node(self):
        import dsl

        z, x, y = (16, 40175, 53235)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3351041362
            dsl.point(3351041362, (40.6926779, -74.0001965), {
                'barrier': u'kissing_gate',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3351041362,
                'kind': u'gate',
                'kind_detail': u'kissing_gate',
            })

    def test_lift_gate_gate_node(self):
        import dsl

        z, x, y = (16, 40177, 53280)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2652168962
            dsl.point(2652168962, (40.6994657, -74.0688286), {
                'barrier': u'lift_gate',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2652168962,
                'kind': u'gate',
                'kind_detail': u'lift_gate',
            })

    def test_stile_gate_node(self):
        import dsl

        z, x, y = (16, 40171, 53355)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/658963589
            dsl.point(658963589, (40.6692395, -74.181512), {
                'barrier': u'stile',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 658963589,
                'kind': u'gate',
                'kind_detail': u'stile',
            })

    def test_swing_gate_gate_node(self):
        import dsl

        z, x, y = (16, 40175, 53159)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2355624683
            dsl.point(2355624683, (40.6912279, -73.8846157), {
                'access': u'no',
                'barrier': u'swing_gate',
                'bicycle': u'no',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2355624683,
                'kind': u'gate',
                'kind_detail': u'swing_gate',
            })

    def test_block_gate_node(self):
        import dsl

        z, x, y = (16, 40179, 53236)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/370759317
            dsl.point(370759317, (40.7102051, -74.0018159), {
                'barrier': u'block',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 370759317,
                'kind': u'block',
            })

    def test_bollard_gate_node(self):
        import dsl

        z, x, y = (16, 40170, 53221)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4556446468
            dsl.point(4556446468, (40.6611013, -73.9793682), {
                'barrier': u'bollard',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4556446468,
                'kind': u'bollard',
            })

    def test_cattle_grid_gate_node(self):
        import dsl

        z, x, y = (16, 39931, 55151)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3706565695
            dsl.point(3706565695, (39.3504576, -76.659313), {
                'barrier': u'cattle_grid',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3706565695,
                'kind': u'cattle_grid',
            })

    def test_kerb_way(self):
        # note that this is a polygon, and the barrier is extracted from around
        # the outside of it. see vectordatasource.transform.build_fence for the
        # logic.
        import dsl

        z, x, y = (16, 40177, 53245)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/575210133
            dsl.way(575210133, dsl.tile_box(z, x, y), {
                'amenity': u'fountain',
                'barrier': u'kerb',
                'natural': u'water',
                'source': u'openstreetmap.org',
            }),
        )

        # should get one linear feature for the kerb
        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 575210133,
                'kind': u'kerb',
            })

        # and one polygon feature for the fountain
        self.assert_has_feature(
            z, x, y, 'water', {
                'id': 575210133,
                'kind': u'fountain',
            })

    def test_guard_rail_way(self):
        import dsl

        z, x, y = (16, 40204, 53199)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/429025216
            dsl.way(429025216, dsl.tile_diagonal(z, x, y), {
                'barrier': u'guard_rail',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 429025216,
                'kind': u'guard_rail',
            })

    def test_ditch_way(self):
        import dsl

        z, x, y = (16, 40175, 53246)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/327897996
            dsl.way(327897996, dsl.tile_diagonal(z, x, y), {
                'barrier': u'ditch',
                'source': u'openstreetmap.org',
                'width': u'2',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 327897996,
                'kind': u'ditch',
            })

    def test_avalanche_fence_way(self):
        import dsl

        z, x, y = (16, 34194, 23360)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/297208839
            dsl.way(297208839, dsl.tile_diagonal(z, x, y), {
                'barrier': u'fence',
                'fence_type': u'avalanche',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 297208839,
                'kind': u'fence',
                'kind_detail': u'avalanche',
            })

    def test_barbed_wire_fence_way(self):
        import dsl

        z, x, y = (16, 19328, 24644)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/295529573
            dsl.way(295529573, dsl.tile_diagonal(z, x, y), {
                'barrier': u'fence',
                'fence_type': u'barbed_wire',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 295529573,
                'kind': u'fence',
                'kind_detail': u'barbed_wire',
            })

    def test_bars_fence_way(self):
        import dsl

        z, x, y = (16, 19311, 24643)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/298198775
            dsl.way(298198775, dsl.tile_diagonal(z, x, y), {
                'barrier': u'fence',
                'fence_type': u'bars',
                'layer': u'1',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 298198775,
                'kind': u'fence',
                'kind_detail': u'bars',
            })

    def test_brick_fence_way(self):
        import dsl

        z, x, y = (16, 18734, 25114)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/232718125
            dsl.way(232718125, dsl.tile_diagonal(z, x, y), {
                'barrier': u'fence',
                'fence_type': u'brick',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 232718125,
                'kind': u'fence',
                'kind_detail': u'brick',
            })

    def test_chain_fence_way(self):
        import dsl

        z, x, y = (16, 19316, 24585)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/159745097
            dsl.way(159745097, dsl.tile_diagonal(z, x, y), {
                'barrier': u'fence',
                'fence_type': u'chain',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 159745097,
                'kind': u'fence',
                'kind_detail': u'chain',
            })

    def test_chain_link_fence_way(self):
        # note: this fence is the boundary of a dog park polygon. see
        # vectordatasource.transform.build_fence for how it gets separated into
        # its own feature.
        import dsl

        z, x, y = (16, 19296, 24645)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/328281970
            dsl.way(328281970, dsl.tile_box(z, x, y), {
                'barrier': u'fence',
                'fence_type': u'chain_link',
                'leisure': u'dog_park',
                'source': u'openstreetmap.org',
            }),
        )

        # we should get the chain link fence
        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 328281970,
                'kind': u'fence',
                'kind_detail': u'chain_link',
            })

        # *and* we should get the dog park
        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 328281970,
                'kind': u'dog_park',
            })

    def test_concrete_fence_way(self):
        import dsl

        z, x, y = (16, 18374, 25755)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/262772200
            dsl.way(262772200, dsl.tile_diagonal(z, x, y), {
                'barrier': u'fence',
                'fence_type': u'concrete',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 262772200,
                'kind': u'fence',
                'kind_detail': u'concrete',
            })

    def test_drystone_wall_fence_way(self):
        import dsl

        z, x, y = (16, 15173, 26407)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/545104470
            dsl.way(545104470, dsl.tile_diagonal(z, x, y), {
                'barrier': u'fence',
                'fence_type': u'drystone_wall',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 545104470,
                'kind': u'fence',
                'kind_detail': u'drystone_wall',
            })

    def test_electric_fence_way(self):
        import dsl

        z, x, y = (16, 18860, 25241)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/579357092
            dsl.way(579357092, dsl.tile_diagonal(z, x, y), {
                'barrier': u'fence',
                'fence_type': u'electric',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 579357092,
                'kind': u'fence',
                'kind_detail': u'electric',
            })

    def test_grate_fence_way(self):
        import dsl

        z, x, y = (16, 31565, 21231)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/34765925
            dsl.way(34765925, dsl.tile_diagonal(z, x, y), {
                'barrier': u'fence',
                'fence_type': u'grate',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 34765925,
                'kind': u'fence',
                'kind_detail': u'grate',
            })

    def test_hedge_fence_way(self):
        import dsl

        z, x, y = (16, 19092, 24788)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/518896455
            dsl.way(518896455, dsl.tile_diagonal(z, x, y), {
                'barrier': u'fence',
                'fence_type': u'hedge',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 518896455,
                'kind': u'fence',
                'kind_detail': u'hedge',
            })

    def test_metal_fence_way(self):
        import dsl

        z, x, y = (16, 19288, 24645)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/320782296
            dsl.way(320782296, dsl.tile_diagonal(z, x, y), {
                'barrier': u'fence',
                'colour': u'black',
                'fence_type': u'metal',
                'height': u'2.5',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 320782296,
                'kind': u'fence',
                'kind_detail': u'metal',
            })

    def test_metal_bars_fence_way(self):
        import dsl

        z, x, y = (16, 19304, 24616)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/598350594
            dsl.way(598350594, dsl.tile_diagonal(z, x, y), {
                'barrier': u'fence',
                'fence_type': u'metal_bars',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 598350594,
                'kind': u'fence',
                'kind_detail': u'metal_bars',
            })

    def test_net_fence_way(self):
        import dsl

        z, x, y = (16, 18358, 25747)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/515061722
            dsl.way(515061722, dsl.tile_diagonal(z, x, y), {
                'barrier': u'fence',
                'fence_type': u'net',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 515061722,
                'kind': u'fence',
                'kind_detail': u'net',
            })

    def test_pole_fence_way(self):
        import dsl

        z, x, y = (16, 19290, 24657)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/223405756
            dsl.way(223405756, dsl.tile_diagonal(z, x, y), {
                'barrier': u'fence',
                'fence_type': u'pole',
                'height': u'1.3',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 223405756,
                'kind': u'fence',
                'kind_detail': u'pole',
            })

    def test_railing_fence_way(self):
        import dsl

        z, x, y = (16, 19299, 24643)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/357266840
            dsl.way(357266840, dsl.tile_diagonal(z, x, y), {
                'barrier': u'fence',
                'fence_type': u'railing',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 357266840,
                'kind': u'fence',
                'kind_detail': u'railing',
            })

    def test_railings_fence_way(self):
        import dsl

        z, x, y = (16, 19308, 24626)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/519728459
            dsl.way(519728459, dsl.tile_diagonal(z, x, y), {
                'barrier': u'fence',
                'fence_type': u'railings',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 519728459,
                'kind': u'fence',
                'kind_detail': u'railings',
            })

    def test_split_rail_fence_way(self):
        import dsl

        z, x, y = (16, 19098, 24748)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/594831242
            dsl.way(594831242, dsl.tile_diagonal(z, x, y), {
                'barrier': u'fence',
                'fence_type': u'split_rail',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 594831242,
                'kind': u'fence',
                'kind_detail': u'split_rail',
            })

    def test_steel_fence_way(self):
        import dsl

        z, x, y = (16, 17170, 25232)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/487094346
            dsl.way(487094346, dsl.tile_diagonal(z, x, y), {
                'barrier': u'fence',
                'fence_type': u'steel',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 487094346,
                'kind': u'fence',
                'kind_detail': u'steel',
            })

    def test_stone_fence_way(self):
        import dsl

        z, x, y = (16, 18821, 24228)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/586140624
            dsl.way(586140624, dsl.tile_diagonal(z, x, y), {
                'barrier': u'fence',
                'fence_type': u'stone',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 586140624,
                'kind': u'fence',
                'kind_detail': u'stone',
            })

    def test_wall_fence_way(self):
        import dsl

        z, x, y = (16, 19625, 23598)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/508166524
            dsl.way(508166524, dsl.tile_diagonal(z, x, y), {
                'barrier': u'fence',
                'fence_type': u'wall',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 508166524,
                'kind': u'fence',
                'kind_detail': u'wall',
            })

    def test_wire_fence_way(self):
        import dsl

        z, x, y = (16, 19299, 24643)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/357266841
            dsl.way(357266841, dsl.tile_diagonal(z, x, y), {
                'barrier': u'fence',
                'fence_type': u'wire',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 357266841,
                'kind': u'fence',
                'kind_detail': u'wire',
            })

    def test_wood_fence_way(self):
        import dsl

        z, x, y = (16, 19300, 24650)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/577857781
            dsl.way(577857781, dsl.tile_diagonal(z, x, y), {
                'barrier': u'fence',
                'fence_type': u'wood',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 577857781,
                'kind': u'fence',
                'kind_detail': u'wood',
            })

    def test_blood_bank_node(self):
        import dsl

        z, x, y = (16, 19087, 24820)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2572216768
            dsl.point(2572216768, (-75.1506499, 39.9601062), {
                'addr:city': u'Philadelphia',
                'addr:housenumber': u'700',
                'addr:postcode': u'19123',
                'addr:street': u'Spring Garden Street',
                'healthcare': u'blood_donation',
                'name': u'Philadelphia Red Cross Blood Donation Center',
                'phone': u'1-800-RED CROSS',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2572216768,
                'kind': u'blood_bank',
            })

    def test_blood_bank_way(self):
        import dsl

        z, x, y = (16, 18892, 24049)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/567183407
            dsl.way(567183407, dsl.tile_box(z, x, y), {
                'addr:city': u'Liverpool',
                'addr:housenumber': u'7359',
                'addr:postcode': u'13090',
                'addr:state': u'NY',
                'addr:street': u'Oswego Road',
                'building': u'yes',
                'healthcare': u'blood_donation',
                'name': u'American Red Cross Blood Donation Center',
                'operator': u'American Red Cross',
                'phone': u'+1-800-733-2767',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 567183407,
                'kind': u'blood_bank',
            })

    def test_blood_bank_node_fixup(self):
        # the more common tag is healthcare=blood_donation, but there are a few
        # instances of healthcare=blood_bank that we can fixup.
        import dsl

        z, x, y = (16, 19302, 24629)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5345342860
            dsl.point(5345342860, (-73.9694947, 40.7588798), {
                'addr:city': u'New York',
                'addr:housenumber': u'641',
                'addr:postcode': u'10022',
                'addr:state': u'NY',
                'addr:street': u'Lexington Avenue',
                'healthcare': u'blood_bank',
                'name': u'10 Storks',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5345342860,
                'kind': u'blood_bank',
            })

    def test_danger_way(self):
        import dsl

        z, x, y = (16, 19197, 24804)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/28735778
            dsl.way(28735778, dsl.tile_box(z, x, y), {
                'military': u'danger_area',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 28735778,
                'kind': u'danger_area',
            })

    def test_danger_cliff_top(self):
        # to be honest, this looks like a tagging mistake - it's near a path
        # called "cliff top", nowhere near any military areas that i can see
        # and seems more likely to have been intended as a viewpoint than a
        # danger area. still, it makes for a decent test.

        import dsl

        z, x, y = (16, 32354, 21550)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4809654741
            dsl.point(4809654741, (-2.2727805, 52.3271344), {
                'landuse': u'military',
                'military': u'danger_area',
                'name': u'cliff top',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4809654741,
                'kind': u'danger_area',
                'name': u'cliff top',
            })

    def test_danger_area_otmoor(self):
        import dsl

        z, x, y = (13, 4069, 2712)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/26165183
            dsl.way(26165183, dsl.tile_box(z, x, y), {
                'access': 'private',
                'military': 'danger_area',
                'name': 'Otmoor Range Danger Area',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 26165183,
                'kind': u'danger_area',
                'name': u'Otmoor Range Danger Area',
            })
        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 26165183,
                'kind': u'danger_area',
            })

    def test_defibrillator_node(self):
        import dsl

        z, x, y = (16, 19266, 24671)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4407735213
            dsl.point(4407735213, (-74.165199, 40.581625), {
                'emergency': u'defibrillator',
                'indoor': u'yes',
                'level': u'2',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4407735213,
                'kind': u'defibrillator',
            })

    def test_defibrillator_way(self):
        import dsl

        z, x, y = (16, 16935, 26003)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/117019981
            dsl.way(117019981, dsl.tile_box(z, x, y), {
                'addr:city': u'Athens',
                'addr:housenumber': u'508',
                'addr:postcode': u'35611',
                'addr:state': u'AL',
                'addr:street': u'Jefferson Street South',
                'building': u'public',
                'defibrillator:location': u'1st floor, from the front ' \
                u'door, go forward on left before steps',
                'emergency': u'defibrillator',
                'name': u'Athens Utilities Customer Service',
                'office': u'government',
                'operator': u'City of Athens Customer Service Dept.',
                'source': u'openstreetmap.org',
                'website': u'http://www.athens-utilities.com/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 117019981,
                'kind': u'defibrillator',
            })

    def test_entrance_node(self):
        import dsl

        z, x, y = (16, 19281, 24643)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5560645981
            dsl.point(5560645981, (-74.085264, 40.700752), {
                'entrance': u'yes',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'buildings', {
                'id': 5560645981,
                'kind': u'entrance',
            })

    def test_main_entrance_node(self):
        import dsl

        z, x, y = (16, 19288, 24645)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3274261072
            dsl.point(3274261072, (-74.045208, 40.690017), {
                'entrance': u'main',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'buildings', {
                'id': 3274261072,
                'kind': u'entrance',
                'kind_detail': u'main',
            })

    def test_staircase_entrance_node(self):
        import dsl

        z, x, y = (16, 19327, 24628)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5104221320
            dsl.point(5104221320, (-73.830464, 40.762991), {
                'entrance': u'staircase',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'buildings', {
                'id': 5104221320,
                'kind': u'entrance',
                'kind_detail': u'staircase',
            })

    def test_service_entrance_node(self):
        import dsl

        z, x, y = (16, 19303, 24651)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2494258437
            dsl.point(2494258437, (-73.962089, 40.667189), {
                'entrance': u'service',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'buildings', {
                'id': 2494258437,
                'kind': u'entrance',
                'kind_detail': u'service',
            })

    def test_home_entrance_node(self):
        # what to do about entrances which are also addresses? we put both as
        # points in the buildings layer, and it sort of seems redundant to have
        # a point for each. but should one take priority over the other?
        import dsl

        z, x, y = (16, 18918, 25146)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4909832627
            dsl.point(4909832627, (-76.076968, 38.571745), {
                'addr:city': u'Cambridge',
                # 'addr:housenumber': u'307',
                'addr:postcode': u'21613',
                'addr:street': u'High Street',
                'entrance': u'home',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'buildings', {
                'id': 4909832627,
                'kind': u'entrance',
                'kind_detail': u'home',
            })

    def test_unisex_entrance_node(self):
        import dsl

        z, x, y = (16, 32056, 24712)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5028110333
            dsl.point(5028110333, (-3.908103, 40.411595), {
                'access': u'private',
                'entrance': u'unisex',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'buildings', {
                'id': 5028110333,
                'kind': u'entrance',
                'kind_detail': u'unisex',
            })

    def test_garage_entrance_node(self):
        import dsl

        z, x, y = (16, 19295, 24632)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5103334973
            dsl.point(5103334973, (-74.005862, 40.743563), {
                'entrance': u'garage',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'buildings', {
                'id': 5103334973,
                'kind': u'entrance',
                'kind_detail': u'garage',
            })

    def test_emergency_entrance_node(self):
        import dsl

        z, x, y = (16, 32747, 21789)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4211372648
            dsl.point(4211372648, (-0.1107958, 51.5187394), {
                'entrance': u'emergency',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'buildings', {
                'id': 4211372648,
                'kind': u'exit',
                'kind_detail': u'emergency',
            })

    def test_exit_entrance_node(self):
        import dsl

        z, x, y = (16, 19305, 24629)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3569401990
            dsl.point(3569401990, (-73.954288, 40.757290), {
                'entrance': u'exit',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'buildings', {
                'id': 3569401990,
                'kind': u'exit',
            })

    def test_main_entrance_entrance_node(self):
        import dsl

        z, x, y = (16, 19294, 24641)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5083818836
            dsl.point(5083818836, (-74.010921, 40.708488), {
                'entrance': u'main_entrance',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'buildings', {
                'id': 5083818836,
                'kind': u'entrance',
                'kind_detail': u'main',
            })

    def test_residence_entrance_node(self):
        import dsl

        z, x, y = (16, 18310, 23885)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5559913168
            dsl.point(5559913168, (-79.414757, 43.779602), {
                'access': u'private',
                'entrance': u'residence',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'buildings', {
                'id': 5559913168,
                'kind': u'entrance',
                'kind_detail': u'residence',
            })

    def test_secondary_entrance_entrance_node(self):
        import dsl

        z, x, y = (16, 19288, 24629)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5541446704
            dsl.point(5541446704, (-74.042494, 40.756505), {
                'access': u'private',
                'entrance': u'secondary_entrance',
                'source': u'openstreetmap.org',
                'wheelchair': u'yes',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'buildings', {
                'id': 5541446704,
                'kind': u'entrance',
                'kind_detail': u'secondary',
            })

    def test_private_entrance_node(self):
        import dsl

        z, x, y = (16, 18626, 24060)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4689338325
            dsl.point(4689338325, (-77.679041, 43.082803), {
                'entrance': u'private',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'buildings', {
                'id': 4689338325,
                'kind': u'entrance',
                'kind_detail': u'private',
            })

    def test_fire_exit_entrance_node(self):
        import dsl

        z, x, y = (16, 19346, 24661)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5016784225
            dsl.point(5016784225, (-73.728280, 40.625330), {
                'entrance': u'fire_exit',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'buildings', {
                'id': 5016784225,
                'kind': u'exit',
                'kind_detail': u'fire_exit',
            })

    def test_gaming_node(self):
        import dsl

        z, x, y = (16, 19077, 24822)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2100740221
            dsl.point(2100740221, (-75.203507, 39.951631), {
                'addr:city': u'Philadelphia',
                'addr:housenumber': u'4006',
                'addr:postcode': u'19104',
                'addr:state': u'PA',
                'addr:street': u'Spruce Street',
                'leisure': u'adult_gaming_centre',
                'name': u'University Family Fun Center',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2100740221,
                'kind': u'adult_gaming_centre',
            })

    def test_gaming_way(self):
        import dsl

        z, x, y = (16, 17768, 25989)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/41979263
            dsl.way(41979263, dsl.tile_box(z, x, y), {
                'addr:city': u'Greenville',
                'addr:housenumber': u'614',
                'addr:postcode': u'29601',
                'addr:street': u'North Main Street',
                'building': u'yes',
                'height': u'8.7',
                'leisure': u'adult_gaming_centre',
                'name': u'Breakout',
                'source': u'openstreetmap.org',
                'website': u'https://breakoutgreenville.com/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 41979263,
                'kind': u'adult_gaming_centre',
            })

    def test_garden_centre_node(self):
        import dsl

        z, x, y = (16, 19293, 24649)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/1378081014
            dsl.point(1378081014, (-74.015906, 40.675089), {
                'name': u'Chelsea Garden Center Red Hook',
                'shop': u'garden_centre',
                'source': u'openstreetmap.org',
                'website': u'http://www.chelseagardencenter.com/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1378081014,
                'kind': u'garden_centre',
            })

    def test_garden_centre_way(self):
        import dsl

        z, x, y = (16, 19303, 24648)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/265733658
            dsl.way(265733658, dsl.tile_box(z, x, y), {
                'addr:housenumber': u'784',
                'addr:postcode': u'11238',
                'addr:street': u'Dean Street',
                'building': u'yes',
                'height': u'4.7',
                'name': u'Natty Garden',
                'nycdoitt:bin': u'3027945',
                'shop': u'garden_centre',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 265733658,
                'kind': u'garden_centre',
            })

    def test_golf_node(self):
        import dsl

        z, x, y = (16, 19252, 24580)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5622433042
            dsl.point(5622433042, (-74.244082, 40.962317), {
                'addr:city': u'Wayne',
                'addr:housenumber': u'1210',
                'addr:postcode': u'07470',
                'addr:state': u'NJ',
                'addr:street': u'Paterson-Hamburg Turnpike',
                'name': u'K & J Custom Fit Pro Shop',
                'shop': u'golf',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5622433042,
                'kind': u'golf',
            })

    def test_golf_way(self):
        import dsl

        z, x, y = (16, 18826, 24953)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/398700987
            dsl.way(398700987, dsl.tile_box(z, x, y), {
                'addr:city': u'Loch Raven',
                'addr:country': u'US',
                'addr:housenumber': u'803',
                'addr:postcode': u'21286',
                'addr:state': u'MD',
                'addr:street': u'Goucher Boulevard',
                'addr:unit': u'104',
                'building': u'retail',
                'name': u'Golf Galaxy',
                'shop': u'golf',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 398700987,
                'kind': u'golf',
            })

    def test_grocery_node(self):
        import dsl

        z, x, y = (16, 19298, 24628)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2709906342
            dsl.point(2709906342, (-73.990564, 40.761580), {
                'addr:city': u'New York',
                'addr:housenumber': u'681',
                'addr:postcode': u'10036',
                'addr:state': u'NY',
                'addr:street': u'9th Avenue',
                'name': u'New York Food Market',
                'phone': u'+1 212 2456470',
                'shop': u'grocery',
                'source': u'openstreetmap.org',
                'website': u'http://newyorkfoodmarket.com',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2709906342,
                'kind': u'grocery',
            })

    def test_grocery_way(self):
        import dsl

        z, x, y = (16, 19285, 24634)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/409910669
            dsl.way(409910669, dsl.tile_box(z, x, y), {
                'addr:city': u'Jersey City',
                'addr:housenumber': u'2975',
                'addr:postcode': u'07306',
                'addr:state': u'NJ',
                'addr:street': u'John F. Kennedy Boulevard',
                'building': u'yes',
                'building:levels': u'1',
                'name': u'Apna Bazar Cash & Carry',
                'opening_hours': u'Mo-Su 09:00-21:00',
                'phone': u'+1 201 217 9701',
                'shop': u'grocery',
                'source': u'openstreetmap.org',
                'website': u'http://www.apnabazarcashandcarry.com',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 409910669,
                'kind': u'grocery',
            })

    def test_harbour_natural_water_way(self):
        import dsl

        z, x, y = (16, 19002, 25265)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/310557860
            dsl.way(310557860, dsl.tile_box(z, x, y), {
                'harbour': u'yes',
                'natural': u'water',
                'source': u'openstreetmap.org',
            }),
        )

        # note: the harbour=yes by itself isn't enough to make this into a
        # landuse feature.
        self.assert_no_matching_feature(
            z, x, y, 'landuse', {
                'id': 310557860,
            })

    def test_harbour_pier_way(self):
        import dsl

        z, x, y = (16, 25307, 36837)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/183049783
            dsl.way(183049783, dsl.tile_box(z, x, y), {
                'harbour': u'yes',
                'man_made': u'pier',
                'name': u'Porto do Açu',
                'operator': u'LLX',
                'seamark:harbour:category': u'tanker;bulk',
                'seamark:type': u'harbour',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 183049783,
                'kind': 'pier',
            })

    def test_harbour_way(self):
        import dsl

        z, x, y = (16, 38891, 25976)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/515527428
            dsl.way(515527428, dsl.tile_box(z, x, y), {
                'addr:city': u'Larnaka',
                'harbour': u'yes',
                'name': u'Larnaka harbour',
                'source': u'openstreetmap.org',
            }),
        )

        # harbour=yes is not enough by itself to make a feature in the landuse
        # layer.
        self.assert_no_matching_feature(
            z, x, y, 'landuse', {
                'id': 515527428,
            })

    def test_harbour_landuse_harbour_way(self):
        import dsl

        z, x, y = (16, 35014, 25282)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/422833298
            dsl.way(422833298, dsl.tile_box(z, x, y), {
                'harbour': u'yes',
                'landuse': u'harbour',
                'name': u'Cala Dogana',
                'natural': u'bay',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 422833298,
                'kind': u'harbour',
            })

    def test_harbour_landuse_port_way(self):
        import dsl

        z, x, y = (16, 31231, 20846)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/143517784
            dsl.way(143517784, dsl.tile_box(z, x, y), {
                'harbour': u'yes',
                'landuse': u'port',
                'maxdraft': u'12',
                'maxlength': u'300',
                'operator': u'Port Authority of Killybegs',
                'phone': u'00353 (0)74 9731032',
                'seamark:type': u'harbour',
                'source': u'openstreetmap.org',
                'vhf_channel': u'14',
                'website': u'http://www.killybegsharbour.ie/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 143517784,
                'kind': u'port',
            })

    def test_port_terminal_way(self):
        import dsl

        z, x, y = (16, 22575, 37950)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/256125920
            dsl.way(256125920, dsl.tile_box(z, x, y), {
                'harbour': u'yes',
                'landuse': u'port_terminal',
                'man_made': u'pier',
                'name': u'Nuevo puerto de Posadas',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 256125920,
                'kind': u'port_terminal',
            })

    def test_ferry_terminal_way(self):
        import dsl

        z, x, y = (16, 31640, 21243)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/55873793
            dsl.way(55873793, dsl.tile_box(z, x, y), {
                'access': u'customers',
                'landuse': u'ferry_terminal',
                'name': u'Terminal 1',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 55873793,
                'kind': u'ferry_terminal',
            })

    def test_container_terminal_way(self):
        import dsl

        z, x, y = (16, 18282, 31129)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/330811048
            dsl.way(330811048, dsl.tile_box(z, x, y), {
                'landuse': u'container_terminal',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 330811048,
                'kind': u'container_terminal',
            })

    def test_shipyard_way(self):
        import dsl

        z, x, y = (16, 29593, 30065)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/398258882
            dsl.way(398258882, dsl.tile_box(z, x, y), {
                'landuse': u'shipyard',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 398258882,
                'kind': u'shipyard',
                'min_zoom': 15,
            })

    def test_wharf_way(self):
        import dsl

        z, x, y = (16, 21272, 23202)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/184311022
            dsl.way(184311022, dsl.tile_box(z, x, y), {
                'landuse': u'wharf',
                'name': u'Covehead Wharf',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 184311022,
                'kind': u'wharf',
                'min_zoom': 16,
            })

    def test_quay_way(self):
        import dsl

        z, x, y = (16, 29533, 27314)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/45061639
            dsl.way(45061639, dsl.tile_box(z, x, y), {
                'area': u'yes',
                'landuse': u'quay',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 45061639,
                'kind': u'quay',
                'min_zoom': 16,
            })

    def test_naval_base_way(self):
        import dsl

        z, x, y = (16, 19134, 25058)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/28501295
            dsl.way(28501295, dsl.tile_box(z, x, y), {
                'landuse': u'military',
                'military': u'naval_base',
                'name': u'United States Coast Guard Training Center',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 28501295,
                'kind': u'naval_base',
            })

    def test_boatyard_way(self):
        import dsl

        z, x, y = (16, 19327, 24653)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/527031661
            dsl.way(527031661, dsl.tile_box(z, x, y), {
                'access': u'private',
                'name': u'Rockman\'s Park Memorial Boat Club',
                'source': u'openstreetmap.org',
                'waterway': u'boatyard',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 527031661,
                'kind': u'boatyard',
            })

    def test_boatyard_node(self):
        import dsl

        z, x, y = (16, 19327, 24654)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5082841810
            dsl.point(5082841810, (-73.830727, 40.654999), {
                'source': u'openstreetmap.org',
                'waterway': u'boatyard',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5082841810,
                'kind': u'boatyard',
            })

    def test_boat_lift_node(self):
        import dsl

        z, x, y = (16, 18169, 24135)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2426819553
            dsl.point(2426819553, (-80.193664, 42.782552), {
                'man_made': u'crane',
                'name': u'Travel Lift',
                'source': u'openstreetmap.org',
                'waterway': u'boat_lift',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2426819553,
                'kind': u'boat_lift',
            })

    def test_boat_lift_way(self):
        import dsl

        z, x, y = (16, 18828, 24981)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/170211248
            dsl.way(170211248, dsl.tile_box(z, x, y), {
                'source': u'openstreetmap.org',
                'waterway': u'boat_lift',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 170211248,
                'kind': u'boat_lift',
            })

    def test_ship_chandler_way(self):
        import dsl

        z, x, y = (16, 33481, 21751)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/276059237
            dsl.way(276059237, dsl.tile_box(z, x, y), {
                'building': u'retail',
                'name': u'T.D. Bouwman & zn. BV',
                'ref:bag': u'1676100000449055',
                'seamark:small_craft_facility:category': u'chandler',
                'seamark:type': u'small_craft_facility',
                'shop': u'ship_chandler',
                'source': u'openstreetmap.org',
                'source:date': u'2014-02-11',
                'start_date': u'1800',
                'website': u'http://www.tdbouwman.nl/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 276059237,
                'kind': u'ship_chandler',
            })

    def test_ship_chandler_node(self):
        import dsl

        z, x, y = (16, 33480, 21752)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2806599446
            dsl.point(2806599446, (3.914906, 51.642764), {
                'addr:city': u'Zierikzee',
                'addr:housenumber': u'17',
                'addr:postcode': u'4301RC',
                'addr:street': u'Deltastraat',
                'name': u'Mulder Yachtservice',
                'seamark:small_craft_facility:category': u'boatyard;chandler',
                'seamark:type': u'small_craft_facility',
                'shop': u'ship_chandler',
                'source': u'openstreetmap.org',
                'source:date': u'2014-02-11',
                'website': u'http://www.mulderyachtservice.nl/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2806599446,
                'kind': u'ship_chandler',
            })

    def test_customs_node(self):
        import dsl

        z, x, y = (16, 18868, 23795)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/529165668
            dsl.point(529165668, (-76.354747, 44.136012), {
                'amenity': u'customs',
                'attribution': u'Natural Resources Canada',
                'canvec:CODE': u'2010100',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 529165668,
                'kind': u'customs',
            })

    def test_customs_way(self):
        import dsl

        z, x, y = (16, 18990, 23680)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/206943159
            dsl.way(206943159, dsl.tile_box(z, x, y), {
                'amenity': u'customs',
                'building': u'yes',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 206943159,
                'kind': u'customs',
            })

    def test_harbourmaster_seamark_node(self):
        import dsl

        z, x, y = (16, 17964, 29191)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/778613459
            dsl.point(778613459, (-81.318644, 19.272868), {
                'addr:city': u'Spotts',
                'addr:country': u'KY',
                'addr:street': u'Jackson Road',
                'building': u'yes',
                'description': u'This is where the ships anchor '\
                u'during rough seas!',
                'name': u'Spotts Bay Alternate Cruise Facility of ' \
                u'Port Authority',
                'seamark:building:function': u'harbour_master',
                'seamark:type': u'building',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 778613459,
                'kind': u'harbourmaster',
            })

    def test_harbourmaster_seamark_way(self):
        import dsl

        z, x, y = (16, 18409, 24075)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/84872891
            dsl.way(84872891, dsl.tile_box(z, x, y), {
                'building': u'yes',
                'seamark:building:function': u'harbour_master',
                'seamark:type': u'building',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 84872891,
                'kind': u'harbourmaster',
            })

    def test_harbour_master_node(self):
        import dsl

        z, x, y = (16, 18224, 23638)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3721714683
            dsl.point(3721714683, (-79.887715, 44.753227), {
                'harbour': u'harbour_master',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3721714683,
                'kind': u'harbourmaster',
            })

    def test_harbour_master_way(self):
        import dsl

        z, x, y = (16, 32156, 22859)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/406287049
            dsl.way(406287049, dsl.tile_box(z, x, y), {
                'building': u'yes',
                'harbour': u'harbour_master',
                'opening_hours': u'Mo-Sa 09:00-12:00,14:00-18:00',
                'source': u'openstreetmap.org',
                'wheelchair': u'yes',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 406287049,
                'kind': u'harbourmaster',
            })

    def test_harbourmaster_amenity_node(self):
        import dsl

        z, x, y = (16, 17927, 28133)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4424415086
            dsl.point(4424415086, (-81.518615, 24.660679), {
                'amenity': u'harbourmaster',
                'shop': u'yes',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4424415086,
                'kind': u'harbourmaster',
            })

    def test_harbourmaster_amenity_way(self):
        import dsl

        z, x, y = (16, 17777, 28436)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/259829016
            dsl.way(259829016, dsl.tile_box(z, x, y), {
                'amenity': u'harbourmaster',
                'building': u'yes',
                'building:levels': u'3',
                'name': u'Empresa Prácticos de Cuba',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 259829016,
                'kind': u'harbourmaster',
            })

    def test_yes_mooring_node(self):
        import dsl

        z, x, y = (16, 18842, 25052)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4341108759
            dsl.point(4341108759, (-76.493961, 38.972904), {
                'mooring': u'yes',
                'source': u'openstreetmap.org',
            }),
        )

        # treat mooring=yes as a "yes, there's a mooring here", but we don't
        # know any more about it.
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4341108759,
                'kind': u'mooring',
                'kind_detail': type(None),
            })

    def test_private_mooring_node(self):
        import dsl

        z, x, y = (16, 19533, 24620)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/1989045561
            dsl.point(1989045561, (-72.699321, 40.796934), {
                'mooring': u'private',
                'source': u'openstreetmap.org',
            }),
        )

        # TODO: should we show these at all if they're private?
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1989045561,
                'kind': u'mooring',
                'access': 'private',
            })

    def test_no_mooring_node(self):
        import dsl

        z, x, y = (16, 17992, 23772)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5180188472
            dsl.point(5180188472, (-81.166304, 44.226554), {
                'leisure': u'slipway',
                'mooring': u'no',
                'source': u'openstreetmap.org',
                'vehicle': u'no',
            }),
        )

        # in this case, the mooring=no is a description of the slipway, rather
        # than a feature in its own right.
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5180188472,
                'kind': u'slipway',
                'mooring': 'no',
            })

    def test_commercial_mooring_node(self):
        import dsl

        z, x, y = (16, 18223, 24746)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2015422399
            dsl.point(2015422399, (-79.895062, 40.270013), {
                'man_made': u'mooring',
                'mooring': u'commercial',
                'source': u'openstreetmap.org',
            }),
        )

        # note: there's not many man_made=mooring, so we ignore that.
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2015422399,
                'kind': u'mooring',
                'kind_detail': u'commercial',
            })

    def test_ferry_mooring_node(self):
        import dsl

        z, x, y = (16, 17344, 23374)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2320763454
            dsl.point(2320763454, (-84.724975, 45.774231), {
                'mooring': u'ferry',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2320763454,
                'kind': u'mooring',
                'kind_detail': u'ferry',
            })

    def test_guest_mooring_node(self):
        import dsl

        z, x, y = (16, 17669, 27124)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3667335766
            dsl.point(3667335766, (-82.936394, 29.590537), {
                'maxstay': u'minimal',  # wow, sounds super hospitable...
                'mooring': u'guest',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3667335766,
                'kind': u'mooring',
                'kind_detail': u'guest',
            })

    def test_cruise_mooring_node(self):
        import dsl

        z, x, y = (16, 19903, 24337)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4148336680
            dsl.point(4148336680, (-70.666619, 41.961962), {
                'contact:phone': u'+1 508 7462643',
                'contact:website': u'http://www.captjohn.com/',
                'mooring': u'cruise',
                'name': u'Captain John Whale Watching & Fishing Tours',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4148336680,
                'kind': u'mooring',
                'kind_detail': u'cruise',
            })

    def test_waiting_mooring_node(self):
        import dsl

        z, x, y = (16, 33124, 24003)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2102077401
            dsl.point(2102077401, (1.959648, 43.312300), {
                'mooring': u'waiting',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2102077401,
                'kind': u'mooring',
                'kind_detail': u'waiting',
            })

    def test_pile_mooring_node(self):
        import dsl

        z, x, y = (16, 33704, 21668)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2410435220
            dsl.point(2410435220, (5.146992, 51.927532), {
                'material': u'wood',
                'mooring': u'pile',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2410435220,
                'kind': u'mooring',
                'kind_detail': u'pile',
            })

    def test_declaration_mooring_node(self):
        import dsl

        z, x, y = (16, 30526, 40041)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2079122376
            dsl.point(2079122376, (-12.312872, -37.063474), {
                'mooring': u'declaration',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2079122376,
                'kind': u'mooring',
                'kind_detail': u'declaration',
            })

    def test_yachts_mooring_way(self):
        import dsl

        z, x, y = (16, 15565, 26449)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/584249543
            dsl.way(584249543, dsl.tile_box(z, x, y), {
                'man_made': u'pier',
                'mooring': u'yachts',
                'source': u'openstreetmap.org',
                'width': u'1.2',
            }),
        )

        # this is really a description of the pier, rather than a feature in
        # its own right, so pass it through on the pier.
        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 584249543,
                'kind': u'pier',
                'mooring': u'yachts',
            })

    def test_customers_mooring_way(self):
        import dsl

        z, x, y = (16, 19866, 24126)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/278952041
            dsl.way(278952041, dsl.tile_box(z, x, y), {
                'access': u'customers',
                'area': u'yes',
                'floating': u'no',
                'horse': u'no',
                'layer': u'2',
                'lit': u'yes',
                'man_made': u'pier',
                'material': u'wood',
                'mooring': u'customers',
                'motor_vehicle': u'no',
                'seamark:type': u'mooring',
                'seasonal': u'no',
                'source': u'openstreetmap.org',
                'surface': u'wood',
            }),
        )

        # again, seems like a description of who's allowed to tie up on the
        # pier, not a separate feature.
        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 278952041,
                'kind': u'pier',
                'mooring': u'customers',
            })

    def test_quay_man_made_way_line(self):
        import dsl

        z, x, y = (16, 18958, 25284)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/109938886
            dsl.way(109938886, dsl.tile_diagonal(z, x, y), {
                'man_made': u'quay',
                'source': u'openstreetmap.org',
            }),
        )

        # should linear quays go into the roads layer like piers?
        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 109938886,
                'kind': u'path',
                'kind_detail': u'quay',
            })

    def test_man_made_quay_way_area(self):
        import dsl

        z, x, y = (16, 33352, 21847)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/465148799
            dsl.way(465148799, dsl.tile_box(z, x, y), {
                'man_made': u'quay',
                'name': u'Kaai 410',
                'name:de': u'kai 410',
                'name:fr': u'quai 410',
                'name:it': u'banchina 410',
                'source': u'openstreetmap.org',
            }),
        )

        # polygonal quays should go into landuse?
        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 465148799,
                'kind': u'quay',
            })

    def test_sanitary_dump_station_node(self):
        import dsl

        z, x, y = (16, 19489, 24603)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3925485395
            dsl.point(3925485395, (-72.938255, 40.865682), {
                'amenity': u'sanitary_dump_station',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3925485395,
                'kind': u'sanitary_dump_station',
            })

    def test_sanitary_dump_station_way(self):
        import dsl

        z, x, y = (16, 18684, 24916)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/552257184
            dsl.way(552257184, dsl.tile_box(z, x, y), {
                'amenity': u'sanitary_dump_station',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 552257184,
                'kind': u'sanitary_dump_station',
            })

    def test_waterway_sanitary_dump_station_node(self):
        import dsl

        z, x, y = (16, 18876, 25380)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3472044600
            dsl.point(3472044600, (-76.306942, 37.561204), {
                'source': u'openstreetmap.org',
                'waterway': u'sanitary_dump_station',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3472044600,
                'kind': u'sanitary_dump_station',
            })

    def test_waterway_sanitary_dump_station_way(self):
        import dsl

        z, x, y = (16, 11649, 25525)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/551894147
            dsl.way(551894147, dsl.tile_box(z, x, y), {
                'source': u'openstreetmap.org',
                'waterway': u'sanitary_dump_station',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 551894147,
                'kind': u'sanitary_dump_station',
            })

    def test_marina_sanity_dump_station_yes_node(self):
        import dsl

        z, x, y = (16, 18725, 23827)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3730870302
            dsl.point(3730870302, (-77.135342, 44.010267), {
                'leisure': u'marina',
                'name': u'Port Picton Harbour Marina',
                'power_supply': u'yes',
                'sanitary_dump_station': u'yes',
                'source': u'openstreetmap.org',
                'wikidata': u'Q385085',
                'wikipedia': u'en:Prince Edward County, Ontario',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3730870302,
                'kind': u'marina',
                'sanitary_dump_station': u'yes',
            })

    def test_marina_sanity_dump_station_yes_way(self):
        import dsl

        z, x, y = (16, 18844, 25055)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/39392303
            dsl.way(39392303, dsl.tile_box(z, x, y), {
                'leisure': u'marina',
                'name': u'Bert Jabin\'s Yacht Yard',
                'sanitary_dump_station': u'yes',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 39392303,
                'kind': u'marina',
                'sanitary_dump_station': u'yes',
            })

    def test_camp_site_sanitary_dump_station_yes_node(self):
        import dsl

        z, x, y = (16, 10802, 24913)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/1798722757
            dsl.point(1798722757, (-120.662796, 39.566655), {
                'capacity': u'19',
                'drinking_water': u'yes',
                'fee': u'yes',
                'name': u'Loganville Campground',
                'operator': u'USFS',
                'sanitary_dump_station': u'yes',
                'source': u'openstreetmap.org',
                'toilets': u'yes',
                'toilets:disposal': u'pitlatrine',
                'tourism': u'camp_site',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1798722757,
                'kind': u'camp_site',
                'sanitary_dump_station': u'yes',
            })

    def test_camp_site_sanitary_dump_station_yes_way(self):
        import dsl

        z, x, y = (16, 18937, 24765)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/506304336
            dsl.way(506304336, dsl.tile_box(z, x, y), {
                'internet_access': u'wlan',
                'internet_access:fee': u'yes',
                'name': u'Lake-in-Wood Campground',
                'payment:cash': u'yes',
                'payment:mastercard': u'yes',
                'payment:visa': u'yes',
                'sanitary_dump_station': u'yes',
                'source': u'openstreetmap.org',
                'tourism': u'camp_site',
                'wheelchair': u'limited',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 506304336,
                'kind': u'camp_site',
                'sanitary_dump_station': u'yes',
            })

    def test_caravan_site_sanitary_dump_station_yes_node(self):
        import dsl

        z, x, y = (16, 19122, 23577)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4345342880
            dsl.point(4345342880, (-74.959569, 44.991434), {
                'sanitary_dump_station': u'yes',
                'source': u'openstreetmap.org',
                'tourism': u'caravan_site',
                'water_point': u'yes',
                'name': 'Fake name to pass the no_name_okay filter',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4345342880,
                'kind': u'caravan_site',
                'sanitary_dump_station': u'yes',
            })

    def test_caravan_site_sanitary_dump_station_yes_way(self):
        import dsl

        z, x, y = (16, 19212, 24226)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/416560900
            dsl.way(416560900, dsl.tile_box(z, x, y), {
                'name': u'Nickerson Park Campground',
                'power_supply': u'yes',
                'sanitary_dump_station': u'yes',
                'source': u'openstreetmap.org',
                'tents': u'yes',
                'tourism': u'caravan_site',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 416560900,
                'kind': u'caravan_site',
                'sanitary_dump_station': u'yes',
            })

    def test_waterway_fuel_node(self):
        import dsl

        z, x, y = (16, 19406, 24550)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5489425299
            dsl.point(5489425299, (-73.398601, 41.085890), {
                'source': u'openstreetmap.org',
                'waterway': u'fuel',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5489425299,
                'kind': u'waterway_fuel',
            })

    def test_waterway_fuel_way(self):
        import dsl

        z, x, y = (16, 32043, 22582)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/72074171
            dsl.way(72074171, dsl.tile_box(z, x, y), {
                'building': u'yes',
                'fuel:diesel': u'yes',
                'seamark:information': u'diesel',
                'seamark:small_craft_facility:category': u'fuel_station',
                'seamark:type': u'small_craft_facility',
                'source': u'openstreetmap.org',
                'waterway': u'fuel',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 72074171,
                'kind': u'waterway_fuel',
            })

    def test_waterway_amenity_fuel_node(self):
        import dsl

        z, x, y = (16, 34254, 21225)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/270602036
            dsl.point(270602036, (8.163521, 53.405975), {
                'amenity': u'fuel',
                'name': u'Dieseltankstelle',
                'seamark:small_craft_facility:category': u'fuel_station',
                'seamark:type': u'small_craft_facility',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 270602036,
                'kind': u'waterway_fuel',
            })

    def test_bureau_de_change_node(self):
        import dsl

        z, x, y = (16, 19294, 24641)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2034011032
            dsl.point(2034011032, (-74.013403, 40.706036), {
                'amenity': u'bureau_de_change',
                'name': u'Travelex',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2034011032,
                'kind': u'bureau_de_change',
            })

    def test_bureau_de_change_way(self):
        import dsl

        z, x, y = (16, 18993, 23478)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/292975938
            dsl.way(292975938, dsl.tile_box(z, x, y), {
                'addr:housenumber': u'1724',
                'addr:street': u'Bank Street',
                'amenity': u'bureau_de_change',
                'building': u'commercial',
                'name': u'Money Mart',
                'office': u'financial',
                'shop': u'money_lender',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 292975938,
                'kind': u'bureau_de_change',
            })

    def test_karaoke_box_node(self):
        import dsl

        z, x, y = (16, 10592, 25438)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4360926928
            dsl.point(4360926928, (-121.813979, 37.308435), {
                'amenity': u'karaoke_box',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4360926928,
                'kind': u'karaoke_box',
            })

    def test_karaoke_box_way(self):
        import dsl

        z, x, y = (16, 18478, 32805)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/427879004
            dsl.way(427879004, dsl.tile_box(z, x, y), {
                'addr:city': u'Quito',
                'addr:street': u'Juan León Mera',
                'amenity': u'karaoke_box',
                'building': u'yes',
                'name': u'Julios Karaoke Bar',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 427879004,
                'kind': u'karaoke_box',
            })

    def test_money_transfer_node(self):
        import dsl

        z, x, y = (16, 19299, 24632)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3854507957
            dsl.point(3854507957, (-73.982208, 40.743233), {
                'amenity': u'money_transfer',
                'shop': u'money_lender',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3854507957,
                'kind': u'money_transfer',
            })

    def test_money_transfer_way(self):
        import dsl

        z, x, y = (16, 18993, 23478)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/366495997
            dsl.way(366495997, dsl.tile_box(z, x, y), {
                'addr:housenumber': u'1717',
                'addr:street': u'Bank Street',
                'amenity': u'money_transfer',
                'building': u'commercial',
                'name': u'Western Union',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 366495997,
                'kind': u'money_transfer',
            })

    def test_taxi_node(self):
        import dsl

        z, x, y = (16, 19298, 24650)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5648649304
            dsl.point(5648649304, (-73.988704, 40.670701), {
                'addr:housenumber': u'440',
                'addr:postcode': u'11215',
                'addr:street': u'4th Avenue',
                'amenity': u'taxi',
                'atm': u'yes',
                'name': u'Castle',
                'office': u'yes',
                'opening_hours': u'24/7',
                'phone': u'+1 718 499 9333',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5648649304,
                'kind': u'taxi',
            })

    def test_taxi_way(self):
        import dsl

        z, x, y = (16, 19301, 24646)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/248141957
            dsl.way(248141957, dsl.tile_box(z, x, y), {
                'addr:housenumber': u'269',
                'addr:postcode': u'11205',
                'addr:street': u'Cumberland Street',
                'amenity': u'taxi',
                'building': u'yes',
                'height': u'11.2',
                'name': u'brooklyn taxi company',
                'nycdoitt:bin': u'3058992',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 248141957,
                'kind': u'taxi',
            })

    def test_border_control_node(self):
        import dsl

        z, x, y = (16, 18401, 24104)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/319641176
            dsl.point(319641176, (-78.915192, 42.907821), {
                'barrier': u'border_control',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 319641176,
                'kind': u'border_control',
            })

    def test_border_control_way(self):
        import dsl

        z, x, y = (16, 17643, 24261)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/165631502
            dsl.way(165631502, dsl.tile_box(z, x, y), {
                'amenity': u'customs',
                'barrier': u'border_control',
                'landuse': u'construction',
                'name': u'Canadian Plaza - DRIC',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 165631502,
                'kind': u'border_control',
            })

    def test_fire_hydrant_node(self):
        import dsl

        z, x, y = (16, 19288, 24645)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5525689518
            dsl.point(5525689518, (-74.045333, 40.690406), {
                'emergency': u'fire_hydrant',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5525689518,
                'kind': u'fire_hydrant',
            })

    def test_fire_hydrant_way(self):
        import dsl

        z, x, y = (16, 34320, 23397)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/586085037
            dsl.way(586085037, dsl.tile_box(z, x, y), {
                'barrier': u'fence',
                'emergency': u'fire_hydrant',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 586085037,
                'kind': u'fire_hydrant',
            })

    def test_street_lamp_node(self):
        import dsl

        z, x, y = (16, 19295, 24642)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5057307983
            dsl.point(5057307983, (-74.009300, 40.704352), {
                'highway': u'street_lamp',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5057307983,
                'kind': u'street_lamp',
            })

    def test_street_lamp_way(self):
        import dsl

        z, x, y = (16, 11301, 26220)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/580258855
            dsl.way(580258855, dsl.tile_box(z, x, y), {
                'highway': u'street_lamp',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 580258855,
                'kind': u'street_lamp',
            })

    def test_heliport_node(self):
        import dsl

        z, x, y = (16, 15902, 25235)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3961957374
            dsl.point(3961957374, (-92.644167, 38.190326), {
                'addr:city': u'Lake Ozark',
                'addr:housenumber': u'2101',
                'addr:postcode': u'65049',
                'addr:street': u'Bagnell Dam Boulevard',
                'aeroway': u'heliport',
                'faa': u'MO02',
                'name': u'Lake Ozark Helicopters',
                'phone': u'+1 573 302 0022',
                'source': u'openstreetmap.org',
                'website': u'http://lakeozarkhelicopters.com/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3961957374,
                'kind': u'heliport',
            })

    def test_heliport_way(self):
        import dsl

        z, x, y = (16, 19294, 24642)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/160901442
            dsl.way(160901442, dsl.tile_box(z, x, y), {
                'addr:city': u'New York',
                'addr:state': u'NY',
                'aerodrome:type': u'public',
                'aeroway': u'heliport',
                'alt_name': u'Downtown Manhattan/Wall St. Heliport',
                'ele': u'1',
                'faa': u'JRB',
                'iata': u'JRB',
                'icao': u'KJRB',
                'name': u'Downtown Manhattan Heliport',
                'source': u'openstreetmap.org',
                'website': u'http://www.downtownmanhattanheliport.com/',
                'wikidata': u'Q1575175',
                'wikipedia': u'en:Downtown Manhattan Heliport',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 160901442,
                'kind': u'heliport',
            })

    def test_horse_riding_node(self):
        import dsl

        z, x, y = (16, 18969, 24101)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5363428250
            dsl.point(5363428250, (-75.795323, 42.920041), {
                'leisure': u'horse_riding',
                'name': u'Whispering Hill Equestrian Center',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5363428250,
                'kind': u'horse_riding',
            })

    def test_horse_riding_way(self):
        import dsl

        z, x, y = (16, 19322, 24641)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/415715650
            dsl.way(415715650, dsl.tile_box(z, x, y), {
                'leisure': u'horse_riding',
                'name': u'Lynne\'s Riding Center',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 415715650,
                'kind': u'horse_riding',
            })

    def test_casino_node(self):
        import dsl

        z, x, y = (16, 19049, 24663)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/677131244
            dsl.point(677131244, (-75.357312, 40.614903), {
                'amenity': u'casino',
                'name': u'Sands Bethlehem',
                'source': u'openstreetmap.org',
                'wheelchair': u'yes',
                'wikidata': u'Q7416891',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 677131244,
                'kind': u'casino',
            })

    def test_casino_way(self):
        import dsl

        z, x, y = (16, 19397, 24623)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/556401354
            dsl.way(556401354, dsl.tile_box(z, x, y), {
                'amenity': u'casino',
                'building': u'yes',
                'name': u'Race Palace',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 556401354,
                'kind': u'casino',
            })

    def test_watermill_node(self):
        import dsl

        z, x, y = (16, 19451, 24591)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/684168892
            dsl.point(684168892, (-73.147435, 40.914999), {
                'historic': u'yes',
                'man_made': u'watermill',
                'name': u'Stony Brook Grist Mill',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 684168892,
                'kind': u'watermill',
            })

    def test_watermill_way(self):
        import dsl

        z, x, y = (16, 19074, 24788)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/420870873
            dsl.way(420870873, dsl.tile_box(z, x, y), {
                'building': u'yes',
                'man_made': u'watermill',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 420870873,
                'kind': u'watermill',
            })

    def test_field_hospital_node(self):
        import dsl

        z, x, y = (16, 19656, 29116)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3306168229
            dsl.point(3306168229, (-72.023353, 19.659932), {
                'amenity': u'hospital',
                'health_facility:type': u'field_hospital',
                'name': u'Tecima',
                'operator:type': u'public',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3306168229,
                'kind': u'field_hospital',
            })

    def test_field_hospital_way(self):
        import dsl

        z, x, y = (16, 19408, 41285)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/551957454
            dsl.way(551957454, dsl.tile_box(z, x, y), {
                'building': u'hospital',
                'health_facility:type': u'field_hospital',
                'healthcare': u'yes',
                'name': u'Posta de Salud Tenaún Alto',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 551957454,
                'kind': u'field_hospital',
            })
