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
