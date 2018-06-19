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
