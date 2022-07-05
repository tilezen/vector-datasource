import dsl

from . import FixtureTest


class TestNEMinZoomForFilter(FixtureTest):
    def test_use_min_zoom_not_scale_rank(self):
        # scale rank no longer plays a role in whether we consider an NE boundary feature
        z, x, y = 5, 5, 12

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/148838
            dsl.way(-148838, dsl.tile_diagonal(z, x, y), {
                u'min_zoom': 5,
                u'scale_rank': -1,
                u'admin_level': u'2',
                u'featurecla': u'Admin-1 region boundary',
                u'name': u'United States of America',
                u'source': u'naturalearthdata.com',
                u'wikidata': u'Q30',
                u'wikipedia': u'en:United States',
            }),
        )

        self.assert_has_feature(z, x, y, 'boundaries',
                                {'min_zoom': 5})

    def test_clamp_to_3_min(self):
        # a feature with a min_zoom < 3 will be clamped to 3
        z, x, y = 4, 2, 4

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/148838
            dsl.way(-148838, dsl.tile_diagonal(z, x, y), {
                u'min_zoom': 2,
                u'admin_level': u'2',
                u'featurecla': u'Admin-1 region boundary',
                u'name': u'United States of America',
                u'source': u'naturalearthdata.com',
                u'wikidata': u'Q30',
                u'wikipedia': u'en:United States',
            }),
        )

        self.assert_has_feature(z, x, y, 'boundaries',
                                {'min_zoom': 3})

    def test_clamp_to_11_max(self):
        # a feature with a min_zoom > 11 will be clamped to 11.

        z, x, y = 12, 640, 1536

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/148838
            dsl.way(-148838, dsl.tile_diagonal(z, x, y), {
                u'min_zoom': 13,
                u'admin_level': u'2',
                u'featurecla': u'Admin-1 region boundary',
                u'name': u'United States of America',
                u'source': u'naturalearthdata.com',
                u'wikidata': u'Q30',
                u'wikipedia': u'en:United States',
            }),
        )

        self.assert_has_feature(z, x, y, 'boundaries',
                                {'min_zoom': 11})
