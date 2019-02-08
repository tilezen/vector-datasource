# -*- encoding: utf-8 -*-
from . import FixtureTest


class DropRoadPropertiesTest(FixtureTest):

    def test_rcn(self):
        # network_rcn:
        #     filter: { bicycle_network: rcn, $zoom: { max: 12 } }
        #     draw:
        #         mapzen_icon_library:
        #             visible: false
        #
        # roughly translates to: don't draw shields on RCN networks when
        # zoom <= 12.
        import dsl

        z, x, y = (12, 2048, 2048)

        self.generate_fixtures(
            # note: use a major road type, so that the road still exists at
            # low zooms.
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(2, {
                'type': u'route',
                'route': u'bicycle',
                'network': u'rcn',
                'ref': u'X',
                'source': u'openstreetmap.org',
            }, ways=[1]),
        )

        # should exist with all properties at zoom 12
        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 1,
                'kind': 'major_road',
                'bicycle_network': u'rcn',
                'bicycle_shield_text': u'X',
            })

        # should drop shield text property at zoom 11
        self.assert_has_feature(
            z-1, x//2, y//2, 'roads', {
                'kind': 'major_road',
                'bicycle_network': u'rcn',
                'bicycle_shield_text': type(None),
            })

        # and drop everything by zoom 10
        self.assert_has_feature(
            z-2, x//4, y//4, 'roads', {
                'kind': 'major_road',
                'bicycle_network': type(None),
                'bicycle_shield_text': type(None),
            })

    def test_track(self):
        # tracks_network_rcn:
        #     filter: { $zoom: { max: 12 }, kind_detail: track }
        #     draw:
        #         mapzen_icon_library:
        #             visible: false
        #
        # roughly translates to: don't draw shields on tracks when zoom<=12.
        import dsl

        z, x, y = (13, 4096, 4096)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'highway': u'track',
                'surface': u'paved',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(2, {
                'type': u'route',
                'route': u'bicycle',
                'network': u'icn',
                'ref': u'X',
                'source': u'openstreetmap.org',
            }, ways=[1]),
        )

        # should exist with all properties at zoom 13
        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 1,
                'bicycle_network': u'icn',
                'bicycle_shield_text': u'X',
                'min_zoom': 11,
            })

        # should drop properties by zoom 12
        self.assert_no_matching_feature(
            z-1, x//2, y//2, 'roads', {
                'bicycle_network': None,
            })
        self.assert_no_matching_feature(
            z-1, x//2, y//2, 'roads', {
                'bicycle_shield_text': None,
            })

    def test_lcn(self):
        # network_lcn:
        #     filter: { bicycle_network: lcn, $zoom: { max: 15 } }
        #     draw:
        #         mapzen_icon_library:
        #             visible: false
        #
        # roughly translates to: don't draw shields on LCN networks when
        # zoom < 15.
        import dsl

        z, x, y = (15, 0, 0)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_diagonal(z, x, y), {
                'highway': u'residential',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(2, {
                'type': u'route',
                'route': u'bicycle',
                'network': u'lcn',
                'ref': u'X',
                'source': u'openstreetmap.org',
            }, ways=[1]),
        )

        # should exist with all properties at zoom 15.
        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 1,
                'kind': 'minor_road',
                'bicycle_network': u'lcn',
                'bicycle_shield_text': u'X',
            })

        # should drop shield text by zoom 14
        self.assert_has_feature(
            z-1, x//2, y//2, 'roads', {
                'kind': 'minor_road',
                'bicycle_network': u'lcn',
                'bicycle_shield_text': type(None),
            })

        # should drop everything by <= 13
        self.assert_has_feature(
            z-2, x//4, y//4, 'roads', {
                'kind': 'minor_road',
                'bicycle_network': type(None),
                'bicycle_shield_text': type(None),
            })
