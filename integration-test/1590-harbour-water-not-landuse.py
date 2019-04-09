# -*- encoding: utf-8 -*-
from . import FixtureTest


class HarbourTest(FixtureTest):

    def test_over_water(self):
        # interesting use of *land*use over water...
        import dsl

        z, x, y = (16, 32272, 21795)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/3303804
            dsl.way(3303804, dsl.box_area(z, x, y, 1045925), {
                'access:tide': 'yes',
                'landuse': 'harbour',
                'name': 'Royal Portbury Dock',
                'natural': 'water',
                'seamark:harbour:category': 'roro',
                'seamark:type': 'harbour',
                'source': 'openstreetmap.org',
                'waterway': 'dock',
                'wikidata': 'Q7374733',
            }),
        )

        # water feature should come through (note: it's a kind: dock, rather
        # than kind: water because of the waterway=dock tag taking precedence).
        self.assert_has_feature(
            z, x, y, 'water', {
                'id': 3303804,
                'kind': 'dock',
            })

        # harbour landuse label should come through
        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 3303804,
                'kind': 'harbour',
                'name': 'Royal Portbury Dock',
                'label_placement': True,
            })

        # landuse area should _not_ come through over the water.
        self.assert_no_matching_feature(
            z, x, y, 'landuse', {
                'id': 3303804,
                'label_placement': type(None),
            })

    def test_over_land(self):
        # same test as before, but this time without the tags which indicate
        # it's water. over land, we should retain the landuse polygon.
        import dsl

        z, x, y = (16, 32272, 21795)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/3303804
            dsl.way(3303804, dsl.box_area(z, x, y, 1045925), {
                'access:tide': 'yes',
                'landuse': 'harbour',
                'name': 'Royal Portbury Dock',
                'seamark:harbour:category': 'roro',
                'seamark:type': 'harbour',
                'source': 'openstreetmap.org',
                'wikidata': 'Q7374733',
            }),
        )

        # harbour landuse label should come through
        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 3303804,
                'kind': 'harbour',
                'name': 'Royal Portbury Dock',
                'label_placement': True,
            })

        # landuse area should come through over land.
        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 3303804,
                'label_placement': type(None),
            })
