# -*- encoding: utf-8 -*-
from . import FixtureTest


class GraveyardCemeteryTest(FixtureTest):

    def test_forest_lawn_memorial_park(self):
        import dsl

        z, x, y = (13, 1409, 3276)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/24019957
            dsl.way(24019957, dsl.box_area(z, x, y, 872976), {
                'amenity': 'grave_yard',
                'name': 'Forest Lawn Memorial Park',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 24019957,
                'kind': 'grave_yard',
                'min_zoom': 13,
            })

    def test_willits_cemetery(self):
        # despite the name, it has been tagged as a graveyard. the two terms
        # appear to be near-synonyms anyway (apparently a cemetery is
        # independent of any single church, and a graveyard isn't - but i had
        # to look that up, it wasn't obvious to me).
        import dsl

        z, x, y = (14, 2577, 6237)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/368713224
            dsl.way(368713224, dsl.box_area(z, x, y, 74278), {
                'amenity': 'grave_yard',
                'ele': '467',
                'gnis:county_id': '045',
                'gnis:created': '01/19/1981',
                'gnis:feature_id': '237866',
                'gnis:state_id': '06',
                'name': 'Willits Cemetery',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 368713224,
                'kind': 'grave_yard',
                'min_zoom': 14,
            })
