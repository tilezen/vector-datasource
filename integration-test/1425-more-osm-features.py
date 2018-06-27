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

    def test_gravel_beach_way(self):
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

        for layer in ('pois', 'landuse'):
            self.assert_has_feature(
                z, x, y, layer, {
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
