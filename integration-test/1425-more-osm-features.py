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
