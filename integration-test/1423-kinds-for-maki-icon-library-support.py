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
                'kind_detail': 'military',
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
                'kind': u'danger',
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
                'kind': u'danger',
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
                'kind': u'danger',
                'name': u'Otmoor Range Danger Area',
            })
        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 26165183,
                'kind': u'danger',
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
            z, x, y, 'pois', {
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
            z, x, y, 'pois', {
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
            z, x, y, 'pois', {
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
            z, x, y, 'pois', {
                'id': 2494258437,
                'kind': u'entrance',
                'kind_detail': u'service',
            })

    def test_home_entrance_node(self):
        import dsl

        z, x, y = (16, 18918, 25146)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4909832627
            dsl.point(4909832627, (-76.076968, 38.571745), {
                'addr:city': u'Cambridge',
                'addr:housenumber': u'307',
                'addr:postcode': u'21613',
                'addr:street': u'High Street',
                'entrance': u'home',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
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
            z, x, y, 'pois', {
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
            z, x, y, 'pois', {
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
            z, x, y, 'pois', {
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
            z, x, y, 'pois', {
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
            z, x, y, 'pois', {
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
            z, x, y, 'pois', {
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
            z, x, y, 'pois', {
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
            z, x, y, 'pois', {
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
            z, x, y, 'pois', {
                'id': 5016784225,
                'kind': u'exit',
                'kind_detail': u'fire_exit',
            })
