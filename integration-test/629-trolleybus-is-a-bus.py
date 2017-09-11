from . import OsmFixtureTest


class TrolleybusIsABus(OsmFixtureTest):
    def test_industrial_street(self):
        self.load_fixtures([
            'http://www.openstreetmap.org/way/397268717',
            'http://www.openstreetmap.org/relation/2996736',
        ], clip=self.tile_bbox(16, 10484, 25339))

        self.assert_has_feature(
            16, 10484, 25339, 'roads',
            {'is_bus_route': True, 'name': 'Industrial St.'})

    def test_clayton_street(self):
        self.load_fixtures([
            'http://www.openstreetmap.org/way/32929419',
            'http://www.openstreetmap.org/relation/3412979',
        ], clip=self.tile_bbox(16, 10477, 25333))

        self.assert_has_feature(
            16, 10477, 25333, 'roads',
            {'is_bus_route': True, 'name': 'Clayton St.'})

    def test_union_street(self):
        self.load_fixtures([
            'http://www.openstreetmap.org/way/254756528',
            'http://www.openstreetmap.org/relation/3413068',
        ], clip=self.tile_bbox(16, 10477, 25326))

        self.assert_has_feature(
            16, 10477, 25326, 'roads',
            {'is_bus_route': True, 'name': 'Union St.'})
