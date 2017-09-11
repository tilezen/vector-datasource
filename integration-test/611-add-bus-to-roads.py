from . import FixtureTest


class AddBusToRoads(FixtureTest):
    def test_is_bus_route(self):
        # block between mission & 6th and howard & 5th in SF.
        # appears to have lots of buses.
        #
        #  -- 14X to Daly City
        #  -- 14X to Downtown
        #  -- 14R to Mission
        #  -- 14R to Downtown
        # ... and many more bus route relations
        self.load_fixtures([
            'https://www.openstreetmap.org/way/88572932',
            'https://www.openstreetmap.org/relation/3406710',
            'https://www.openstreetmap.org/relation/3406709',
            'https://www.openstreetmap.org/relation/3406708',
            'https://www.openstreetmap.org/relation/3000713',
        ], clip=self.tile_bbox(16, 10484, 25329))

        self.assert_has_feature(
            16, 10484, 25329, 'roads',
            {'name': 'Mission St.', 'is_bus_route': True})
