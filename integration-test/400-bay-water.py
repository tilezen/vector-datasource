import dsl

from . import FixtureTest


class BayWater(FixtureTest):
    def test_san_pablo_bay(self):
        # San Pablo Bay
        z, x, y = (14, 2623, 6318)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/43950409
            dsl.way(43950409, dsl.tile_box(z, x, y), {
                'name': 'San Pablo Bay', 'natural': 'bay',
                'area': 'yes',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'water',
            {'kind': 'bay', 'label_placement': True})

    def test_sansum_narrows(self):
        # Sansum Narrows
        self.load_fixtures(['https://www.openstreetmap.org/relation/1019862'])

        self.assert_has_feature(
            11, 321, 705, 'water',
            {'kind': 'strait', 'label_placement': True})

    def test_horsens_fjord(self):
        # Horsens Fjord
        z, x, y = (10, 540, 319)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/1451065
            dsl.way(-1451065, dsl.tile_box(z, x, y), {
                'name': 'Horsens Fjord', 'natural': 'fjord',
                'type': 'multipolygon',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'water',
            {'kind': 'fjord', 'label_placement': True})
