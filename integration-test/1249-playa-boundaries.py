# -*- encoding: utf-8 -*-
from . import FixtureTest


class PlayaTest(FixtureTest):

    def test_sevier_lake(self):
        import dsl
        from tilequeue.tile import coord_to_bounds
        from shapely.geometry import Polygon
        from ModestMaps.Core import Coordinate

        z, x, y = (16, 12164, 25088)

        bounds = coord_to_bounds(Coordinate(zoom=z, column=x, row=y))
        # lower right triangle of the tile box, so that part of the
        # boundary is definitely within the tile, not just at the edges.
        shape = Polygon([
            [bounds[0], bounds[1]],
            [bounds[2], bounds[3]],
            [bounds[2], bounds[1]],
            [bounds[0], bounds[1]],
        ])

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/99982115
            dsl.way(99982115, shape, {
                'intermittent': 'yes',
                'name': 'Sevier Lake',
                'natural': 'water',
                'source': 'openstreetmap.org',
                'wikidata': 'Q81246',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'water', {
                'id': 99982115,
                'intermittent': True,
                'kind': 'water',
                'boundary': True,
            })
