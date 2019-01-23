# -*- encoding: utf-8 -*-
from . import FixtureTest


class QuarryTest(FixtureTest):

    def test_quarry(self):
        import dsl

        z, x, y = (13, 1309, 3160)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/232461616
            dsl.way(232461616, dsl.box_area(z, x, y, 790207), {
                'landuse': 'quarry',
                'man_made': 'mine',
                'name': 'San Rafael Traprock Quarry',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 232461616,
                'kind': 'quarry',
                'min_zoom': 13,
            })
