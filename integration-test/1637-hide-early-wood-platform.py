# -*- encoding: utf-8 -*-
from . import FixtureTest


class HideEarlyWoodPlatformTest(FixtureTest):

    def test_platform_z17(self):
        import dsl

        z, x, y = (16, 32765, 21800)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5266974822
            dsl.point(5266974822, (-0.0144533, 51.4782507), {
                'name': u'Greenwich DLR',
                'railway': u'platform',
                'source': u'openstreetmap.org',
                'wheelchair': u'yes',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5266974822,
                'kind': u'platform',
                'min_zoom': 17,
            })

    def test_wood_z17(self):
        import dsl

        z, x, y = (16, 32661, 21458)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/152558913
            dsl.way(152558913, dsl.tile_box(z, x, y), {
                'landuse': u'wood',
                'name': u'Wytchley Warren Spinney',
                'source': u'openstreetmap.org',
                'source:name': u'OS OpenData StreetView',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 152558913,
                'kind': u'wood',
                'min_zoom': 17,
            })
