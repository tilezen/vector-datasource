from . import FixtureTest


class LanduseKindBuildings(FixtureTest):
    def test_lax_airport_terminals(self):
        self.load_fixtures([
            # Terminal 2, which had landuse_kind set correctly at z14
            'https://www.openstreetmap.org/way/413226245',

            # Tom Bradley International Terminal was missing landuse_kind
            'https://www.openstreetmap.org/relation/6168071',

            # the aerodrome landuse polygon
            'https://www.openstreetmap.org/way/649268639',
        ])

        # the tile which contains Terminal 2 should set the landuse_kind
        # correctly.
        self.assert_has_feature(
            14, 2803, 6547, 'buildings',
            {'id': 413226245, 'kind': 'building', 'landuse_kind': 'aerodrome'})

        # the four tiles containing bits of Tom Bradley International should
        # do so also.
        for x in (2802, 2803):
            for y in (6547, 6548):
                self.assert_has_feature(
                    14, x, y, 'buildings',
                    {'id': -6168071, 'kind': 'building',
                     'landuse_kind': 'aerodrome'})

    def test_lax_united_airlines_building(self):
        self.load_fixtures([
            # United Airlines building spans two tiles at z16, and neither(?)
            # of them were getting a landuse_kind assigned.
            'https://www.openstreetmap.org/relation/6168075',

            # the aerodrome landuse polygon
            'https://www.openstreetmap.org/way/649268639',
        ])

        for x in (11209, 11210):
            self.assert_has_feature(
                16, x, 26192, 'buildings',
                {'id': -6168075, 'kind': 'building',
                 'landuse_kind': 'aerodrome'})

    def test_building_part(self):
        import dsl
        from tilequeue.tile import coord_to_bounds
        from shapely.geometry import box
        from ModestMaps.Core import Coordinate

        z, x, y = (16, 0, 0)
        bounds = coord_to_bounds(Coordinate(zoom=z, column=x, row=y))
        shape = box(*bounds)

        self.generate_fixtures(
            dsl.way(1, shape,
                    {'landuse': 'park', 'source': 'openstreetmap.org'}),
            dsl.way(2, shape,
                    {'building': 'yes', 'source': 'openstreetmap.org'}),
            dsl.way(3, shape,
                    {'building:part': 'yes', 'source': 'openstreetmap.org'}),
        )

        self.assert_has_feature(
            z, x, y, 'buildings',
            {'id': 2, 'kind': 'building', 'landuse_kind': 'park'})
        self.assert_has_feature(
            z, x, y, 'buildings',
            {'id': 3, 'kind': 'building_part', 'landuse_kind': 'park'})
