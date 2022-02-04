# -*- encoding: utf-8 -*-
import dsl

from . import FixtureTest


class DisputedBoundariesTest(FixtureTest):
    def test_add_dispute_yes(self):
        z, x, y = (16, 39109, 26572)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/726514231
            dsl.way(726514231, dsl.tile_diagonal(z, x, y), {
                'admin_level': '4',
                'admin_level:AR': '4',
                'admin_level:BD': '4',
                'admin_level:BR': '4',
                'admin_level:CN': '4',
                'admin_level:DE': '4',
                'admin_level:EG': '4',
                'admin_level:ES': '4',
                'admin_level:FR': '4',
                'admin_level:GB': '4',
                'admin_level:GR': '4',
                'admin_level:ID': '4',
                'admin_level:IL': '4',
                'admin_level:IN': '4',
                'admin_level:IT': '4',
                'admin_level:JP': '4',
                'admin_level:KO': '4',
                'admin_level:MA': '4',
                'admin_level:NL': '4',
                'admin_level:NP': '4',
                'admin_level:PK': '4',
                'admin_level:PL': '4',
                'admin_level:PS': '8',
                'admin_level:PT': '4',
                'admin_level:SA': '4',
                'admin_level:SE': '4',
                'admin_level:TR': '4',
                'admin_level:TW': '4',
                'admin_level:UA': '4',
                'admin_level:US': '4',
                'admin_level:VN': '2.5',
                'boundary': 'claim',
                'name': 'Viewpoints on Disputed Administrative Boundaries',
                'ne:brk_a3': 'B91',
                'type': 'linestring',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'id': 726514231,
                'kind:PS': 'locality',
                'kind': 'region',
                'kind:US': 'region',
            })

        # make sure kind:VN didn't make it in because its admin_level doesn't map to anything
        self.assert_no_matching_feature(z, x, y, 'boundaries', {
            'id': 726514231,
            'kind:VN': None
        })
