from . import OsmFixtureTest


class BusRoutesZ12(OsmFixtureTest):
    def test_bus_routes_exist_at_z12(self):
        z, x, y = (16, 10484, 25329)

        # block between mission & 6th and howard & 5th in SF.
        # appears to have lots of buses.
        self.load_fixtures([
            'https://www.openstreetmap.org/way/88572932', # Mission St
            'https://www.openstreetmap.org/relation/3406710', # 14X to Daly City
            'https://www.openstreetmap.org/relation/3406709', # 14X to Downtown
            'https://www.openstreetmap.org/relation/3406708', # 14R to Mission
            'https://www.openstreetmap.org/relation/3000713', # 14R to Downtown
            # ... and many more bus route relations
        ], clip=self.tile_bbox(z, x, y))

        # test that at least one is present in tiles up to z12
        while z >= 12:
            self.assert_has_feature(
                z, x, y, 'roads',
                {'is_bus_route': True})
            z, x, y = z - 1, x // 2, y // 2

        # but that none are present in the parent tile at z11
        self.assert_no_matching_feature(
            z, x, y, 'roads',
            {'is_bus_route': True})
