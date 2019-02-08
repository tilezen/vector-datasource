# -*- encoding: utf-8 -*-
from . import FixtureTest


class HideEarlyNoAreaGardenTest(FixtureTest):

    def test_allotments_node(self):
        import dsl

        z, x, y = (16, 32683, 21719)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/1271465901
            dsl.point(1271465901, (-0.4660196, 51.7557019), {
                'landuse': u'allotments',
                'name': u'Midland Hill Allotments',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 1271465901,
                'kind': u'allotments',
                'min_zoom': 16,
            })

    def test_allotments_way(self):
        import dsl

        z, x, y = (16, 32748, 21779)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/32055218
            dsl.way(32055218, dsl.tile_box(z, x, y), {
                'landuse': u'allotments',
                'name': u'Arvon Road allotments',
                'source': u'openstreetmap.org',
            }),
        )

        # should have point in POIs
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 32055218,
                'kind': u'allotments',
                'min_zoom': 16,
            })

        # and polygon in landuse
        self.assert_has_feature(
            z, x, y, 'landuse', {
                'id': 32055218,
                'kind': u'allotments',
            })

    def test_garden_node(self):
        import dsl

        z, x, y = (16, 10473, 25332)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/2969748430
            dsl.point(2969748430, (-122.469992, 37.767533), {
                'leisure': u'garden',
                'name': u'South Africa Garden',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 2969748430,
                'kind': u'garden',
                'min_zoom': 16,
            })

    def test_university_node(self):
        import dsl

        z, x, y = (16, 10484, 25327)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4628353540
            dsl.point(4628353540, (-122.404460, 37.790842), {
                'amenity': u'university',
                'name': u'Academy of Arts University',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4628353540,
                'kind': u'university',
                'min_zoom': 16,
            })
