# -*- encoding: utf-8 -*-
from . import FixtureTest


class DemoteEarlyLandcover(FixtureTest):

    def test_forest(self):
        import dsl

        z, x, y = (9, 123, 180)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/1430156
            dsl.way(1430156, dsl.box_area(z, x, y, 2068410835), {
                'landuse': 'forest',
                'name': 'Savanna State Forest',
                'source': 'openstreetmap.org',
                'type': 'multipolygon',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 1430156,
                'kind': 'forest',
                'min_zoom': 9,
            })

    def test_natural_wood_usfs_1(self):
        # previously, being operator=USFS had meant a zoom bump, but no longer.
        import dsl

        z, x, y = (14, 2733, 6235)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/7339333
            dsl.way(7339333, dsl.box_area(z, x, y, 16961064), {
                'access': 'yes',
                'natural': 'wood',
                'operator': 'United States Forest Service',
                'source': 'openstreetmap.org',
                'type': 'multipolygon',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 7339333,
                'kind': 'natural_wood',
                'min_zoom': 9,
            })

    def test_natural_wood_usfs_2(self):
        # previously, being operator=USFS had meant a zoom bump, but no longer.
        import dsl

        z, x, y = (14, 2734, 6245)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/7352119
            dsl.way(7352119, dsl.box_area(z, x, y, 19525176), {
                'access': 'yes',
                'natural': 'wood',
                'operator': 'United States Forest Service',
                'source': 'openstreetmap.org',
                'type': 'multipolygon',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 7352119,
                'kind': 'natural_wood',
                'min_zoom': 9,
            })

    def test_natural_wood(self):
        import dsl

        z, x, y = (14, 11782, 7469)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/5617154
            dsl.way(5617154, dsl.box_area(z, x, y, 9186148530), {
                'name': 'Nallamala Forest',
                'natural': 'wood',
                'source': 'openstreetmap.org',
                'type': 'multipolygon',
                'wikidata': 'Q1579454',
                'wikipedia': 'en:Nallamala Hills',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 5617154,
                'kind': 'natural_wood',
                'min_zoom': 9,
            })
