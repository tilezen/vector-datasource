from . import FixtureTest


class TrolleybusIsABus(FixtureTest):
    def test_industrial_street(self):
        self.load_fixtures([
            'http://www.openstreetmap.org/way/397268717',
            'http://www.openstreetmap.org/relation/2996736',
        ], clip=self.tile_bbox(16, 10484, 25339))

        self.assert_has_feature(
            16, 10484, 25339, 'roads',
            {'is_bus_route': True, 'name': type(None)})

    def test_clayton_street(self):
        self.load_fixtures([
            'http://www.openstreetmap.org/way/32929419',
            'http://www.openstreetmap.org/relation/3412979',
        ], clip=self.tile_bbox(16, 10477, 25333))

        self.assert_has_feature(
            16, 10477, 25333, 'roads',
            {'is_bus_route': True, 'name': type(None)})

    def test_union_street(self):
        import dsl
        self.generate_fixtures(
            dsl.way(254756528, dsl.tile_diagonal(16, 10477, 25326), {
                'source': 'openstreetmap.org',
                'highway': 'residential',
                'name': 'Union Street',
                'tiger:cfcc': 'A41',
                'tiger:county': 'San Francisco, CA',
                'tiger:name_base': 'Union',
                'tiger:name_type': 'St',
                'tiger:zip_left': '94123',
                'tiger:zip_right': '94123'
            }),
            dsl.relation(3413068, {
                'source': 'openstreetmap.org',
                'fee': 'yes',
                'from': 'Lyon Street & Greenwich Street',
                'name': 'Muni 41 inbound: The Marina => Downtown',
                'network': 'Muni',
                'operator': 'San Francisco Municipal Railway',
                'payment:cash': 'yes',
                'payment:clipper': 'yes',
                'payment:prepaid_ticket': 'yes',
                'public_transport:version': '2',
                'ref': '41',
                'route': 'trolleybus',
                'to': 'Main Street & Howard Street',
                'type': 'route',
            }, ways=[254756528]),
        )

        self.assert_has_feature(
            16, 10477, 25326, 'roads',
            {'is_bus_route': True, 'name': 'Union St.'})
