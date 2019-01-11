# -*- encoding: utf-8 -*-
from . import FixtureTest


class GrasslandTest(FixtureTest):

    def test_grassland(self):
        import dsl

        z, x, y = (16, 10544, 25280)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/6947071
            dsl.way(6947071, dsl.box_area(z, x, y, 209171), {
                'natural': 'grassland',
                'source': 'openstreetmap.org',
                'type': 'multipolygon',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 6947071,
                'kind': 'grassland',
            })

    def test_sand(self):
        import dsl

        z, x, y = (16, 19318, 24654)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/412096037
            dsl.way(412096037, dsl.box_area(z, x, y, 45), {
                'natural': 'sand',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 412096037,
                'kind': 'sand',
            })

    def test_shingle(self):
        import dsl

        z, x, y = (16, 19311, 24601)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/587063993
            dsl.way(587063993, dsl.box_area(z, x, y, 890), {
                'natural': 'shingle',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 587063993,
                'kind': 'shingle',
            })

    def test_heath(self):
        import dsl

        z, x, y = (16, 19328, 24631)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/606580338
            dsl.way(606580338, dsl.box_area(z, x, y, 17464), {
                'natural': 'heath',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 606580338,
                'kind': 'heath',
            })

    def test_bare_rock(self):
        import dsl

        z, x, y = (16, 19300, 24626)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/385443481
            dsl.way(385443481, dsl.box_area(z, x, y, 3411), {
                'alt_name': 'Rat Rock',
                'name': 'Umpire Rock',
                'natural': 'bare_rock',
                'source': 'openstreetmap.org',
                'wikidata': 'Q7295400',
                'wikipedia': 'en:Rat Rock',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 385443481,
                'kind': 'bare_rock',
            })

    def test_desert(self):
        import dsl

        z, x, y = (12, 733, 1601)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/150570680
            dsl.way(150570680, dsl.box_area(z, x, y, 1489464261), {
                'name': 'Las Vegas Valley',
                'natural': 'desert',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 150570680,
                'kind': 'desert',
            })

    def test_vineyard(self):
        import dsl

        z, x, y = (16, 19299, 24582)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/39648296
            dsl.way(39648296, dsl.box_area(z, x, y, 7537), {
                'landuse': 'vineyard',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 39648296,
                'kind': 'vineyard',
            })
