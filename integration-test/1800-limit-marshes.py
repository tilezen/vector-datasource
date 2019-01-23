# -*- encoding: utf-8 -*-
from . import FixtureTest


class MarshTest(FixtureTest):

    def test_tidal_marsh(self):
        import dsl

        z, x, y = (15, 5237, 12663)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/35559154
            dsl.way(35559154, dsl.box_area(z, x, y, 89099), {
                'name': 'Tidal Marsh',
                'natural': 'wetland',
                'source': 'openstreetmap.org',
                'wetland': 'marsh',
            }),
        )

        # landuse polygon should show up at z14
        self.assert_has_feature(
            z-1, x//2, y//2, 'landuse', {
                'id': 35559154,
                'kind': 'wetland',
                'kind_detail': 'marsh',
                'min_zoom': 14,
                'name': type(None),
            })

        # but POI should be zoom 15 max
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 35559154,
                'kind': 'wetland',
                'kind_detail': 'marsh',
                'min_zoom': 15,
                'name': str,
            })

    def test_oro_loma_marsh(self):
        import dsl

        z, x, y = (15, 5265, 12678)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/27284790
            dsl.way(27284790, dsl.box_area(z, x, y, 2135982), {
                'name': 'Oro Loma Marsh',
                'natural': 'wetland',
                'source': 'openstreetmap.org',
            }),
        )

        # polygon should show up at zoom 10 (it's pretty big)
        self.assert_has_feature(
            z-5, x//32, y//32, 'landuse', {
                'id': 27284790,
                'kind': 'wetland',
                'min_zoom': 10,
                'name': type(None),
            })

        # POI should show up later - z15?
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 27284790,
                'kind': 'wetland',
                'min_zoom': 15,
                'name': str,
            })
