from . import FixtureTest


class WalkingRouteRefs(FixtureTest):
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
        import dsl

        z, x, y = 16, 11044, 25309

        #   network=nwn, ref="PCT Section H"
        #   type=route, route=hiking, network=nwn, ref=PCT
        #   type=route, route=foot, network=rwn, ref=JMT
        #   type=route, route=foot, network=rwn, ref="", name="PCT - California
        #   Section H"
        self.generate_fixtures(
            # https://www.openstreetmap.org/way/373532611
            dsl.way(373532611, dsl.tile_diagonal(z, x, y), {
                "horse": "yes",
                "bicycle": "no",
                "name": "John Muir Trail",
                "source": "openstreetmap.org",
                "alt_name": "Pacific Crest National Scenic Trail",
                "network": "nwn",
                "motorcar": "no",
                "foot": "yes",
                "ref": "PCT Section H",
                "highway": "path",
                "motorcycle": "no",
            }),
            # https://www.openstreetmap.org/relation/1225378
            dsl.relation(1225378, {
                "name": "Pacific Crest Trail",
                "network": "nwn",
                "ref": "PCT",
                "route": "hiking",
                "type": "route",
                "wikidata": "Q2003736",
                "wikipedia": "en:Pacific Crest Trail",
            }, ways=[373532611]),
            # https://www.openstreetmap.org/relation/1244828
            dsl.relation(1244828, {
                "name": "John Muir Trail",
                "network": "rwn",
                "ref": "JMT",
                "route": "foot",
                "type": "route",
                "wikidata": "Q967917",
                "wikipedia": "en:John Muir Trail",
            }, ways=[373532611]),
            # https://www.openstreetmap.org/relation/1244686
            dsl.relation(1244686, {
                "name": "PCT - California Section H",
                "network": "rwn",
                "route": "foot",
                "type": "route",
            }, ways=[373532611])
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'id': 373532611,
             'walking_network': 'nwn', 'walking_shield_text': 'PCT',
             'all_walking_networks': ['nwn', 'nwn', 'rwn', 'rwn'],
             'all_walking_shield_texts': [
                 'PCT', 'PCT Section H', 'JMT', type(None)]})
