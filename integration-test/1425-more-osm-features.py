# -*- encoding: utf-8 -*-
from . import FixtureTest


class MoreOSMFeaturesTest(FixtureTest):

    def test_sand_beach_way(self):
        import dsl

        z, x, y = (16, 19335, 24602)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/108403305
            dsl.way(108403305, dsl.tile_box(z, x, y), {
                'ele': u'2',
                'gnis:feature_id': u'959437',
                'name': u'Orchard Beach',
                'natural': u'beach',
                'source': u'openstreetmap.org',
                'surface': u'sand',
                'wikidata': u'Q7100176',
                'wikipedia': u'en:Orchard Beach, Bronx',
            }),
        )

        for layer in ('pois', 'landuse'):
            self.assert_has_feature(
                z, x, y, layer, {
                    'id': 108403305,
                    'kind': u'beach',
                    'kind_detail': u'sand',
                })

    def test_pebblestone_beach_way(self):
        import dsl

        z, x, y = (16, 19253, 24394)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/233695433
            dsl.way(233695433, dsl.tile_box(z, x, y), {
                'access': u'yes',
                'name': u'Lake Minnewaska Beach',
                'natural': u'beach',
                'source': u'openstreetmap.org',
                'surface': u'pebblestone',
            }),
        )

        for layer in ('pois', 'landuse'):
            self.assert_has_feature(
                z, x, y, layer, {
                    'id': 233695433,
                    'kind': u'beach',
                    'kind_detail': u'pebblestone',
                })

    def test_gravel_beach_pois_way(self):
        import dsl

        z, x, y = (16, 19304, 24371)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/360547782
            dsl.way(360547782, dsl.tile_box(z, x, y), {
                'natural': u'beach',
                'source': u'openstreetmap.org',
                'surface': u'gravel',
                # fake name to get the POI to appear
                'name': 'Fake beach name',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 360547782,
                'kind': u'beach',
                'kind_detail': u'gravel',
            })

    def test_gravel_beach_landuse_way(self):
        import dsl

        z, x, y = (16, 19304, 24371)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/360547782
            dsl.way(360547782, dsl.tile_box(z, x, y), {
                'natural': u'beach',
                'source': u'openstreetmap.org',
                'surface': u'gravel',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 360547782,
                'kind': u'beach',
                'kind_detail': u'gravel',
            })

    def test_pebbles_beach_way(self):
        import dsl

        z, x, y = (16, 19296, 24645)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/328291105
            dsl.way(328291105, dsl.tile_box(z, x, y), {
                'natural': u'beach',
                'source': u'openstreetmap.org',
                'surface': u'pebbles',
                # fake name to get the POI to appear
                'name': 'Fake beach name',
            }),
        )

        for layer in ('pois', 'landuse'):
            self.assert_has_feature(
                z, x, y, layer, {
                    'id': 328291105,
                    'kind': u'beach',
                    'kind_detail': u'pebbles',
                })

    def test_grass_beach_way(self):
        import dsl

        z, x, y = (16, 19124, 24555)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/231284265
            dsl.way(231284265, dsl.tile_box(z, x, y), {
                'natural': u'beach',
                'source': u'openstreetmap.org',
                'surface': u'grass',
                # fake name to get the POI to appear
                'name': 'Fake beach name',
            }),
        )

        for layer in ('pois', 'landuse'):
            self.assert_has_feature(
                z, x, y, layer, {
                    'id': 231284265,
                    'kind': u'beach',
                    'kind_detail': u'grass',
                })

    def test_rocky_beach_way(self):
        import dsl

        z, x, y = (16, 19039, 24855)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/322805403
            dsl.way(322805403, dsl.tile_box(z, x, y), {
                'access': u'no',
                'natural': u'beach',
                'source': u'openstreetmap.org',
                'surface': u'rocky',
                # fake name to get the POI to appear
                'name': 'Fake beach name',
            }),
        )

        for layer in ('pois', 'landuse'):
            self.assert_has_feature(
                z, x, y, layer, {
                    'id': 322805403,
                    'kind': u'beach',
                    'kind_detail': u'rocky',
                })

    def test_chemist_node(self):
        import dsl

        z, x, y = (16, 19298, 24631)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/663098951
            dsl.point(663098951, (-73.988039, 40.749678), {
                'name': u'Lush',
                'shop': u'chemist',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 663098951,
                'kind': u'chemist',
            })

    def test_elevator_way(self):
        import dsl

        z, x, y = (16, 19300, 24647)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/510502210
            dsl.way(510502210, dsl.tile_box(z, x, y), {
                'highway': u'elevator',
                'level': u'(-1,-2)',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 510502210,
                'kind': u'elevator',
            })

    def test_elevator_node(self):
        import dsl

        z, x, y = (16, 19312, 24643)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3017396520
            dsl.point(3017396520, (-73.911936, 40.699476), {
                'highway': u'elevator',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3017396520,
                'kind': u'elevator',
            })

    def test_embankment_way(self):
        import dsl

        z, x, y = (16, 19317, 24645)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/374783696
            dsl.way(374783696, dsl.tile_diagonal(z, x, y), {
                'man_made': u'embankment',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 374783696,
                'kind': u'embankment',
            })

    def test_miniature_golf_node(self):
        import dsl

        z, x, y = (16, 19284, 24583)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5181018838
            dsl.point(5181018838, (-74.068437, 40.948861), {
                'leisure': u'miniature_golf',
                'name': u'Monster Mini Golf',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5181018838,
                'kind': u'miniature_golf',
            })

    def test_miniature_golf_way(self):
        import dsl

        z, x, y = (16, 19293, 24645)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/510028688
            dsl.way(510028688, dsl.tile_box(z, x, y), {
                'leisure': u'miniature_golf',
                'name': u'FIGMENT Mini Golf',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 510028688,
                'kind': u'miniature_golf',
            })

    def test_mud_way(self):
        import dsl

        z, x, y = (16, 19455, 24611)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/451611986
            dsl.way(451611986, dsl.tile_box(z, x, y), {
                'name': u'mud',
                'natural': u'mud',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 451611986,
                'kind': u'mud',
            })

    def test_agave_plants_orchard_way(self):
        import dsl

        z, x, y = (16, 30230, 27328)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/513078325
            dsl.way(513078325, dsl.tile_box(z, x, y), {
                'landuse': u'orchard',
                'source': u'openstreetmap.org',
                'trees': u'agave_plants',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 513078325,
                'kind': u'orchard',
                'kind_detail': u'agave_plants',
            })

    def test_almond_trees_orchard_way(self):
        import dsl

        z, x, y = (16, 18136, 33416)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/532775111
            dsl.way(532775111, dsl.tile_box(z, x, y), {
                'landuse': u'orchard',
                'source': u'openstreetmap.org',
                'trees': u'almond_trees',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 532775111,
                'kind': u'orchard',
                'kind_detail': u'almond_trees',
            })

    def test_apple_trees_orchard_way(self):
        import dsl

        z, x, y = (16, 19240, 24746)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/40150611
            dsl.way(40150611, dsl.tile_box(z, x, y), {
                'landuse': u'orchard',
                'name': u'Battleview Orchards',
                'source': u'openstreetmap.org',
                'trees': u'apple_trees',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 40150611,
                'kind': u'orchard',
                'kind_detail': u'apple_trees',
            })

    def test_avocado_trees_orchard_way(self):
        import dsl

        z, x, y = (16, 18505, 32780)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/512033575
            dsl.way(512033575, dsl.tile_box(z, x, y), {
                'genus': u'Persea',
                'landuse': u'orchard',
                'source': u'openstreetmap.org',
                'species': u'Persea americana Mill.',
                'trees': u'avocado_trees',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 512033575,
                'kind': u'orchard',
                'kind_detail': u'avocado_trees',
            })

    def test_banana_plants_orchard_way(self):
        import dsl

        z, x, y = (16, 19570, 29284)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/193575953
            dsl.way(193575953, dsl.tile_box(z, x, y), {
                'fixme': u'position',
                'landuse': u'orchard',
                'source': u'openstreetmap.org',
                'trees': u'banana_plants',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 193575953,
                'kind': u'orchard',
                'kind_detail': u'banana_plants',
            })

    def test_cherry_trees_orchard_way(self):
        import dsl

        z, x, y = (16, 16764, 29918)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/399567949
            dsl.way(399567949, dsl.tile_box(z, x, y), {
                'genus': u'Musa',
                'landuse': u'orchard',
                'source': u'openstreetmap.org',
                'trees': u'cherry_trees',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 399567949,
                'kind': u'orchard',
                'kind_detail': u'cherry_trees',
            })

    def test_coconut_palms_orchard_way(self):
        import dsl

        z, x, y = (16, 20064, 29188)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/179537246
            dsl.way(179537246, dsl.tile_box(z, x, y), {
                'landuse': u'orchard',
                'name': u'Coco',
                'source': u'openstreetmap.org',
                'trees': u'coconut_palms',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 179537246,
                'kind': u'orchard',
                'kind_detail': u'coconut_palms',
            })

    def test_coffea_plants_orchard_way(self):
        import dsl

        z, x, y = (16, 15130, 29155)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/358441066
            dsl.way(358441066, dsl.tile_box(z, x, y), {
                'crop': u'coffee',
                'landuse': u'orchard',
                'source': u'openstreetmap.org',
                'trees': u'coffea_plants',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 358441066,
                'kind': u'orchard',
                'kind_detail': u'coffea_plants',
            })

    def test_date_palms_orchard_way(self):
        import dsl

        z, x, y = (16, 19090, 30857)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/89570508
            dsl.way(89570508, dsl.tile_box(z, x, y), {
                'landuse': u'orchard',
                'name': u'Cultivo de Palma',
                'produce': u'Vegetal Oil for Biodiesel',
                'source': u'openstreetmap.org',
                'trees': u'date_palms',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 89570508,
                'kind': u'orchard',
                'kind_detail': u'date_palms',
            })

    def test_hazel_plants_orchard_way(self):
        import dsl

        z, x, y = (16, 32233, 30965)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/554513274
            dsl.way(554513274, dsl.tile_box(z, x, y), {
                'landuse': u'orchard',
                'source': u'openstreetmap.org',
                'trees': u'hazel_plants',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 554513274,
                'kind': u'orchard',
                'kind_detail': u'hazel_plants',
            })

    def test_hop_plants_orchard_way(self):
        import dsl

        z, x, y = (16, 19947, 23903)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/491352755
            dsl.way(491352755, dsl.tile_box(z, x, y), {
                'genus': u'Humulus',
                'landuse': u'orchard',
                'source': u'openstreetmap.org',
                'trees': u'hop_plants',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 491352755,
                'kind': u'orchard',
                'kind_detail': u'hop_plants',
            })

    def test_kiwi_plants_orchard_way(self):
        import dsl

        z, x, y = (16, 10909, 25550)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/61037561
            dsl.way(61037561, dsl.tile_box(z, x, y), {
                'attribution': u'Fresno_County_GIS',
                'genus': u'Actinidia',
                'landuse': u'orchard',
                'source': u'openstreetmap.org',
                'trees': u'kiwi_plants',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 61037561,
                'kind': u'orchard',
                'kind_detail': u'kiwi_plants',
            })

    def test_macadamia_trees_orchard_way(self):
        import dsl

        z, x, y = (16, 16240, 30096)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/147212021
            dsl.way(147212021, dsl.tile_box(z, x, y), {
                'designation': u'Las Macadamias',
                'genus': u'Macadamia',
                'landuse': u'orchard',
                'name': u'Valhalla Farm',
                'source': u'openstreetmap.org',
                'trees': u'macadamia_trees',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 147212021,
                'kind': u'orchard',
                'kind_detail': u'macadamia_trees',
            })

    def test_mango_trees_orchard_way(self):
        import dsl

        z, x, y = (16, 19546, 29340)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/109112765
            dsl.way(109112765, dsl.tile_box(z, x, y), {
                'addr:city': u'leogane',
                'addr:street': u'cassagne',
                'commune': u'leogane',
                'departement': u'l\'ouest',
                'landuse': u'orchard',
                'source': u'openstreetmap.org',
                'trees': u'mango_trees',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 109112765,
                'kind': u'orchard',
                'kind_detail': u'mango_trees',
            })

    def test_olive_trees_orchard_way(self):
        import dsl

        z, x, y = (16, 18135, 33416)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/532775110
            dsl.way(532775110, dsl.tile_box(z, x, y), {
                'landuse': u'orchard',
                'source': u'openstreetmap.org',
                'trees': u'olive_trees',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 532775110,
                'kind': u'orchard',
                'kind_detail': u'olive_trees',
            })

    def test_orange_trees_orchard_way(self):
        import dsl

        z, x, y = (16, 15048, 28966)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/328878925
            dsl.way(328878925, dsl.tile_box(z, x, y), {
                'landuse': u'orchard',
                'source': u'openstreetmap.org',
                'trees': u'orange_trees',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 328878925,
                'kind': u'orchard',
                'kind_detail': u'orange_trees',
            })

    def test_papaya_trees_orchard_way(self):
        import dsl

        z, x, y = (16, 15196, 29232)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/399116133
            dsl.way(399116133, dsl.tile_box(z, x, y), {
                'genus': u'Carica',
                'landuse': u'orchard',
                'source': u'openstreetmap.org',
                'species': u'Carica papaya',
                'trees': u'papaya_trees',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 399116133,
                'kind': u'orchard',
                'kind_detail': u'papaya_trees',
            })

    def test_peach_trees_orchard_way(self):
        import dsl

        z, x, y = (16, 17827, 25945)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/423428753
            dsl.way(423428753, dsl.tile_box(z, x, y), {
                'landuse': u'orchard',
                'source': u'openstreetmap.org',
                'trees': u'peach_trees',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 423428753,
                'kind': u'orchard',
                'kind_detail': u'peach_trees',
            })

    def test_persimmon_trees_orchard_way(self):
        import dsl

        z, x, y = (16, 10879, 25716)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/61193578
            dsl.way(61193578, dsl.tile_box(z, x, y), {
                'attribution': u'Fresno_County_GIS',
                'landuse': u'orchard',
                'source': u'openstreetmap.org',
                'trees': u'persimmon_trees',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 61193578,
                'kind': u'orchard',
                'kind_detail': u'persimmon_trees',
            })

    def test_pineapple_plants_orchard_way(self):
        import dsl

        z, x, y = (16, 17741, 31218)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/497946838
            dsl.way(497946838, dsl.tile_box(z, x, y), {
                'genus': u'Ananas',
                'landuse': u'orchard',
                'source': u'openstreetmap.org',
                'trees': u'pineapple_plants',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 497946838,
                'kind': u'orchard',
                'kind_detail': u'pineapple_plants',
            })

    def test_pitaya_plants_orchard_way(self):
        import dsl

        z, x, y = (16, 17075, 30576)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/541768573
            dsl.way(541768573, dsl.tile_box(z, x, y), {
                'genus': u'Hylocereus',
                'landuse': u'orchard',
                'source': u'openstreetmap.org',
                'trees': u'pitaya_plants',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 541768573,
                'kind': u'orchard',
                'kind_detail': u'pitaya_plants',
            })

    def test_plum_trees_orchard_way(self):
        import dsl

        z, x, y = (16, 10976, 25637)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/61206687
            dsl.way(61206687, dsl.tile_box(z, x, y), {
                'attribution': u'Fresno_County_GIS',
                'landuse': u'orchard',
                'source': u'openstreetmap.org',
                'trees': u'plum_trees',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 61206687,
                'kind': u'orchard',
                'kind_detail': u'plum_trees',
            })

    def test_rubber_trees_orchard_way(self):
        import dsl

        z, x, y = (16, 16028, 30065)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/396725369
            dsl.way(396725369, dsl.tile_box(z, x, y), {
                'genus': u'Ficus',
                'landuse': u'orchard',
                'source': u'openstreetmap.org',
                'species': u'Ficus elastica',
                'trees': u'rubber_trees',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 396725369,
                'kind': u'orchard',
                'kind_detail': u'rubber_trees',
            })

    def test_tea_plants_orchard_way(self):
        import dsl

        z, x, y = (16, 18575, 33078)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/463858557
            dsl.way(463858557, dsl.tile_box(z, x, y), {
                'genus': u'Camellia',
                'landuse': u'orchard',
                'source': u'openstreetmap.org',
                'species': u'Camellia sinensis (L.) Kuntze',
                'trees': u'tea_plants',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 463858557,
                'kind': u'orchard',
                'kind_detail': u'tea_plants',
            })

    def test_walnut_trees_orchard_way(self):
        import dsl

        z, x, y = (16, 10774, 25826)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/242904453
            dsl.way(242904453, dsl.tile_box(z, x, y), {
                'landuse': u'orchard',
                'source': u'openstreetmap.org',
                'trees': u'walnut_trees',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 242904453,
                'kind': u'orchard',
                'kind_detail': u'walnut_trees',
            })

    def test_oil_palms_orchard_way(self):
        import dsl

        z, x, y = (16, 16793, 29899)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/394728216
            dsl.way(394728216, dsl.tile_box(z, x, y), {
                'genus': u'Elaeis',
                'landuse': u'orchard',
                'source': u'openstreetmap.org',
                'trees': u'oil_palms',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 394728216,
                'kind': u'orchard',
                'kind_detail': u'oil_palms',
            })

    def test_plant_nursery_way(self):
        import dsl

        z, x, y = (16, 19319, 24594)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/442214478
            dsl.way(442214478, dsl.tile_box(z, x, y), {
                'landuse': u'plant_nursery',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 442214478,
                'kind': u'plant_nursery',
            })

    def test_plaque_node(self):
        import dsl

        z, x, y = (16, 19299, 24630)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/1289222425
            dsl.point(1289222425, (-73.982936, 40.752781), {
                'historic': u'memorial',
                'memorial': u'plaque',
                'name': u'Wendell L. Willkie',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1289222425,
                'kind': u'plaque',
            })

    def test_memorial_node(self):
        # if a memorial _isn't_ a plaque, then it should stay as a memorial!
        # this is the counter-example to test_plaque_node above, as previously
        # there was a bug where the test for plaque was too general and
        # accidentally re-classified all memorials as plaques.
        import dsl

        z, x, y = (16, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_centre_shape(z, x, y), {
                'historic': u'memorial',
                'name': u'A. Name Here',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1,
                'kind': 'memorial',
            })

    def test_reef_way(self):
        import dsl

        z, x, y = (16, 59972, 36438)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/300536075
            dsl.way(300536075, dsl.tile_box(z, x, y), {
                'natural': u'reef',
                'reef': u'coral',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'water', {
                'id': 300536075,
                'kind': u'reef',
                'kind_detail': 'coral',
            })

    def test_cosmetics_node(self):
        import dsl

        z, x, y = (16, 19299, 24646)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5343308393
            dsl.point(5343308393, (-73.986721, 40.687488), {
                'name': u'Anwaar Co.',
                'phone': u'+1 718 875 3791',
                'shop': u'cosmetics',
                'source': u'openstreetmap.org',
                'website': u'http://anwaarco.com',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5343308393,
                'kind': u'cosmetics',
            })

    def test_cosmetics_way(self):
        import dsl

        z, x, y = (16, 19305, 24637)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/280081650
            dsl.way(280081650, dsl.tile_box(z, x, y), {
                'addr:city': u'Brooklyn',
                'addr:housenumber': u'95',
                'addr:postcode': u'11222',
                'addr:state': u'NY',
                'addr:street': u'Nassau Avenue',
                'building': u'yes',
                'height': u'15.1',
                'name': u'Ziolko Cosmetics & Herbal',
                'nycdoitt:bin': u'3322680',
                'phone': u'718 609 9279',
                'shop': u'cosmetics',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 280081650,
                'kind': u'cosmetics',
            })

    def test_fishmonger_node(self):
        import dsl

        z, x, y = (16, 19327, 24641)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2274506529
            dsl.point(2274506529, (-73.830344, 40.709093), {
                'addr:housenumber': u'81-18',
                'addr:street': u'Lefferts Boulevard',
                'name': u'Kew Gardens Fish Market',
                'shop': u'fishmonger',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2274506529,
                'kind': u'fishmonger',
            })

    def test_fishmonger_way(self):
        import dsl

        z, x, y = (16, 19331, 24643)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/283172152
            dsl.way(283172152, dsl.tile_box(z, x, y), {
                'addr:city': u'Jamaica',
                'addr:housenumber': u'91-02',
                'addr:postcode': u'11435',
                'addr:street': u'Sutphin Boulevard',
                'building': u'yes',
                'height': u'10.0',
                'name': u'Corner Fish Market',
                'nycdoitt:bin': u'4213900',
                'shop': u'fishmonger',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 283172152,
                'kind': u'fishmonger',
            })

    def test_pillbox_bunker_node(self):
        import dsl

        z, x, y = (16, 19298, 24706)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2576451001
            dsl.point(2576451001, (-73.991799, 40.438530), {
                'bunker_type': u'pillbox',
                'military': u'bunker',
                'name': u'Battery Kingman',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2576451001,
                'kind': u'bunker',
                'kind_detail': u'pillbox',
            })

    def test_munitions_bunker_node(self):
        import dsl

        z, x, y = (16, 13379, 25960)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3911068941
            dsl.point(3911068941, (-106.505514, 34.991425), {
                'access': u'no',
                'bunker_type': u'munitions',
                'location': u'underground',
                'military': u'bunker',
                'name': u'Point 105',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3911068941,
                'kind': u'bunker',
                'kind_detail': u'munitions',
            })

    def test_gun_emplacement_bunker_node(self):
        import dsl

        z, x, y = (16, 19470, 30932)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3516716377
            dsl.point(3516716377, (-73.045059, 10.029707), {
                'building': u'bunker',
                'bunker_type': u'gun_emplacement',
                'FIXME': u'name',
                'landuse': u'military',
                'military': u'bunker',
                'name': u'Batallón de Alta Montaña',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3516716377,
                'kind': u'bunker',
                'kind_detail': u'gun_emplacement',
            })

    def test_hardened_aircraft_shelter_bunker_node(self):
        import dsl

        z, x, y = (16, 18873, 28902)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/462127948
            dsl.point(462127948, (-76.326978, 20.766293), {
                'building': u'bunker',
                'bunker_type': u'hardened_aircraft_shelter',
                'military': u'bunker',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 462127948,
                'kind': u'bunker',
                'kind_detail': u'hardened_aircraft_shelter',
            })

    def test_blockhouse_bunker_node(self):
        import dsl

        z, x, y = (16, 34926, 24316)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4687134694
            dsl.point(4687134694, (11.854714, 42.045672), {
                'building': u'bunker',
                'bunker_type': u'blockhouse',
                'landuse': u'military',
                'military': u'bunker',
                'name': u'Tobruk',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4687134694,
                'kind': u'bunker',
                'kind_detail': u'blockhouse',
            })

    def test_technical_bunker_node(self):
        import dsl

        z, x, y = (16, 31253, 23940)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4955741213
            dsl.point(4955741213, (-8.318059, 43.563983), {
                'abandoned': u'yes',
                'bunker_type': u'technical',
                'description': u'Antigua batería militar',
                'historic': u'yes',
                'military': u'bunker',
                'name': u'Proyectores B6',
                'official_name': u'Batería Militar 6',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4955741213,
                'kind': u'bunker',
                'kind_detail': u'technical',
            })

    def test_mg_nest_bunker_node(self):
        import dsl

        z, x, y = (16, 32669, 24924)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4949636318
            dsl.point(4949636318, (-0.541801, 39.518136), {
                'bunker_type': u'mg_nest',
                'historic': u'yes',
                'military': u'bunker',
                'ruins': u'no',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4949636318,
                'kind': u'bunker',
                'kind_detail': u'mg_nest',
            })

    def test_missile_silo_bunker_node(self):
        import dsl

        z, x, y = (16, 10814, 26017)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5434097308
            dsl.point(5434097308, (-120.596493, 34.734051), {
                'building': u'bunker',
                'bunker_type': u'missile_silo',
                'landuse': u'military',
                'military': u'bunker',
                'name': u'Titan--',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5434097308,
                'kind': u'bunker',
                'kind_detail': u'missile_silo',
            })

    def test_wayside_cross_node(self):
        import dsl

        z, x, y = (16, 19309, 24677)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4987290359
            dsl.point(4987290359, (-73.927802, 40.559544), {
                'historic': u'wayside_cross',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4987290359,
                'kind': u'wayside_cross',
            })

    def test_memorial_plaque_node(self):
        import dsl

        z, x, y = (16, 32531, 21365)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/3577265515
            dsl.point(3577265515, (-1.297031, 52.944488), {
                'dedicatee': u'Oswald Short',
                'historic': u'memorial_plaque',
                'inscription': u'Oswald Short (1883-1969) of Short ' \
                u'Brothers Aeronautical Engineers / Lived here ' \
                u'1881-c.1895 / Erected by public subscription',
                'name': u'Oswald Short (1883-1969)',
                'plaque:colour': u'blue',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3577265515,
                'kind': u'plaque',
            })

    def test_obelisk_node(self):
        import dsl

        z, x, y = (16, 18088, 25938)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5370564611
            dsl.point(5370564611, (-80.634831, 35.088498), {
                'man_made': u'obelisk',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5370564611,
                'kind': u'obelisk',
            })

    def test_obelisk_way(self):
        import dsl

        z, x, y = (16, 15094, 26381)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/481307273
            dsl.way(481307273, dsl.tile_box(z, x, y), {
                'man_made': u'obelisk',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 481307273,
                'kind': u'obelisk',
            })

    def test_cutting_way(self):
        import dsl

        z, x, y = (16, 17064, 30550)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/283464048
            dsl.way(283464048, dsl.tile_diagonal(z, x, y), {
                'man_made': u'cutting',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 283464048,
                'kind': u'cutting',
            })

    def test_railway_cutting_yes_way(self):
        import dsl

        z, x, y = (16, 19279, 24646)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/95467617
            dsl.way(95467617, dsl.tile_diagonal(z, x, y), {
                'cutting': u'yes',
                'electrified': u'no',
                'gauge': u'1435',
                'maxspeed': u'15 mph',
                'name': u'Bayonne Connection',
                'railway': u'rail',
                'railway:traffic_mode': u'freight',
                'source': u'openstreetmap.org',
                'source:maxspeed': u'Conrail ETT 2013-10-17',
                'usage': u'industrial',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 95467617,
                'kind': u'rail',
                'cutting': 'yes',
            })

    def test_railway_embankment_yes_way(self):
        import dsl

        z, x, y = (16, 19278, 24646)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/95467611
            dsl.way(95467611, dsl.tile_diagonal(z, x, y), {
                'electrified': u'no',
                'embankment': u'yes',
                'gauge': u'1435',
                'maxspeed': u'25 mph',
                'name': u'National Docks Branch',
                'old_railway_operator': u'LV',
                'operator': u'Conrail',
                'railway': u'rail',
                'railway:traffic_mode': u'freight',
                'source': u'openstreetmap.org',
                'source:maxspeed': u'Conrail ETT 2013-10-17',
                'usage': u'branch',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 95467611,
                'kind': u'rail',
                'embankment': 'yes',
            })

    def test_embankment_left_way(self):
        import dsl

        z, x, y = (16, 19715, 24176)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/430667681
            dsl.way(430667681, dsl.tile_diagonal(z, x, y), {
                'attribution': u'Office of Geographic and ' \
                u'Environmental Information (MassGIS)',
                'condition': u'fair',
                'embankment': u'left',
                'highway': u'residential',
                'lanes': u'2',
                'massgis:way_id': u'187669',
                'name': u'South Row Road',
                'source': u'openstreetmap.org',
                'width': u'9.1',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 430667681,
                'kind': u'minor_road',
                'kind_detail': 'residential',
                'embankment': 'left',
            })

    def test_embankment_both_way(self):
        import dsl

        z, x, y = (16, 16196, 25177)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/540442026
            dsl.way(540442026, dsl.tile_diagonal(z, x, y), {
                'embankment': u'both',
                'hgv': u'designated',
                'hgv:national_network': u'yes',
                'highway': u'primary',
                'lanes': u'2',
                'maxspeed': u'55 mph',
                'name': u'Highway 50',
                'NHS': u'yes',
                'ref': u'US 50',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
                'tiger:cfcc': u'A21',
                'tiger:county': u'Franklin, MO',
                'tiger:reviewed': u'no',
            }),
        )

        # NOTE: embankment=both is mapped to embankment:yes.
        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 540442026,
                'kind': u'major_road',
                'kind_detail': 'primary',
                'embankment': 'yes',
            })

    def test_monument_obelisk_node(self):
        import dsl

        z, x, y = (16, 17450, 26571)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4028552922
            dsl.point(4028552922, (-84.140170, 32.194609), {
                'historic': u'monument',
                'man_made': u'obelisk',
                'monument:type': u'obelisk',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4028552922,
                'kind': u'obelisk',
                'kind_detail': u'monument',
            })

    def test_monument_obelisk_way(self):
        import dsl

        z, x, y = (16, 19439, 24108)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/178594567
            dsl.way(178594567, dsl.tile_box(z, x, y), {
                'building': u'yes',
                'height': u'267',
                'historic': u'monument',
                'man_made': u'obelisk',
                'name': u'Bennington Battle Monument',
                'obelisk:size': u'monumental',
                'ref:nrhp': u'71000054',
                'source': u'openstreetmap.org',
                'website': u'http://historicsites.vermont.gov',
                'wikidata': u'Q4889875',
                'wikipedia': u'en:Bennington Battle Monument',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 178594567,
                'kind': u'obelisk',
                'kind_detail': u'monument',
            })

    def test_bunker_name_z16_way(self):
        import dsl

        z, x, y = (16, 19286, 24667)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/35099149
            dsl.way(35099149, dsl.tile_box(z, x, y), {
                'building': u'yes',
                'historic': u'ruins',
                'military': u'bunker',
                'name': u'Battery Upton',
                'source': u'openstreetmap.org',
            }),
        )

        # bunker _with name_ should have z16
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 35099149,
                'kind': u'bunker',
                'min_zoom': 16,
            })

    def test_bunker_noname_z18_way(self):
        import dsl

        z, x, y = (16, 19286, 24665)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/35136899
            dsl.way(35136899, dsl.tile_box(z, x, y), {
                'building': u'yes',
                'description': u'watchtower CRF North coincident range finder',
                'historic': u'ruins',
                'level': u'-1',
                'military': u'bunker',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 35136899,
                'kind': u'bunker',
                'min_zoom': 18,
            })

    def test_washington_monument(self):
        import dsl

        z, x, y = (16, 18744, 25072)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/3374540
            dsl.way(3374540, dsl.tile_box(z, x, y), {
                "addr:city": "Washington",
                "addr:housenumber": "1601",
                "addr:postcode": "20560",
                "addr:state": "DC",
                "addr:street": "Independence Avenue",
                "building": "obelisk",
                "building:colour": "white",
                "dcgis:address": "1601 Independence Ave, NW",
                "dcgis:aid": "294406",
                "dcgis:gis": "HSE_0015",
                "dcgis:list_info": "Reg",
                "dcgis:nr_eligibl": "0",
                "dcgis:objectid": "259",
                "dcgis:ssl": "PAR 03160011",
                "dcgis:update_date": "Wed Feb 01 00:00:00 UTC 2006",
                "fee": "no",
                "height": "169.16",
                "historic": "monument",
                "landmark": "yes",
                "man_made": "obelisk",
                "memorial:type": "obelisk",
                "name": "Washington Monument",
                "name:da": u"Washington-monumentet",
                "name:de": u"Washington-Denkmal",
                "name:es": u"Monumento a Washington",
                "name:hu": u"Washington-emlékmű",
                "name:it": u"Monumento a Washington",
                "obelisk:size": "monumental",
                "roof:colour": "white",
                "roof:height": "16.76",
                "roof:shape": "pyramidal",
                "start_date": "1885-02-28",
                "tourism": "attraction",
                "type": "multipolygon",
                "wikidata": "Q178114",
                "wikipedia": "en:Washington Monument",
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 3374540,
                'kind': u'obelisk',
                'min_zoom': 14,
            })

    def test_obelisco_macuteo(self):
        import dsl

        z, x, y = (16, 35039, 24352)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/128740184
            dsl.way(128740184, dsl.tile_box(z, x, y), {
                'artwork_type': u'obelisk',
                'height': u'14.52',
                'historic': u'monument',
                'historic:civilization': u'ancient_egyptian',
                'historic:era': u'dynasty_XIX',
                'historic:period': u'new_kingdom',
                'man_made': u'obelisk',
                'name': u'Obelisco Macuteo',
                'obelisk:height': u'6.34',
                'obelisk:material': u'red_granite',
                'obelisk:size': u'monumental',
                'source': u'openstreetmap.org',
                'start_date': u'C13 BC',
                'tourism': u'artwork',
                'wikidata': u'Q3348569',
                'wikipedia': u'it:Obelisco del Pantheon',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 128740184,
                'kind': u'obelisk',
                'min_zoom': 15,
            })
