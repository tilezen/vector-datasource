from . import OsmFixtureTest


class WalkingRouteRefs(OsmFixtureTest):
    def test_single_route(self):
        # walking route constituent ways should have the walking route
        # properties projected onto them.
        #
        #   type=route, route=hiking, network=rwn, ref=416
        #
        # NOTE: it's part of two other relations, but these are not
        # walking/hiking routes.
        self.load_fixtures([
            'https://www.openstreetmap.org/way/127908481',
            'https://www.openstreetmap.org/relation/103942',
        ], clip=self.tile_bbox(15, 17571, 11449))

        self.assert_has_feature(
            15, 17571, 11449, 'roads',
            {'id': 127908481, 'kind': 'path', 'bicyle': type(None),
             'walking_network': 'rwn', 'walking_shield_text': '416',
             'all_walking_networks': ['rwn'],
             'all_walking_shield_texts': ['416']})

    def test_multiple_routes(self):
        #   network=nwn, ref="PCT Section H"
        #   type=route, route=hiking, network=nwn, ref=PCT
        #   type=route, route=foot, network=rwn, ref=JMT
        #   type=route, route=foot, network=rwn, ref="", name="PCT - California
        #   Section H"
        self.load_fixtures([
            'https://www.openstreetmap.org/way/373532611',
            'https://www.openstreetmap.org/relation/1225378',
            'https://www.openstreetmap.org/relation/1244828',
            'https://www.openstreetmap.org/relation/1244686',
        ], clip=self.tile_bbox(16, 11044, 25309))

        self.assert_has_feature(
            16, 11044, 25309, 'roads',
            {'id': 373532611,
             'walking_network': 'nwn', 'walking_shield_text': 'PCT',
             'all_walking_networks': ['nwn', 'nwn', 'rwn', 'rwn'],
             'all_walking_shield_texts': [
                 'PCT', 'PCT Section H', 'JMT', None]})
