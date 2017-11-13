from . import FixtureTest


class RouteName(FixtureTest):
    def test_route_name(self):
        # Relation: M-Ocean View: Inbound to Downtown (91022)
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/91022',
        ], clip=self.tile_bbox(16, 10486, 25326))

        self.assert_has_feature(
            16, 10486, 25326, 'transit',
            {'id': -91022, 'kind': 'light_rail', 'osm_relation': True,
             'name': 'M-Ocean View: Inbound to Downtown',
             'route_name': type(None)})
