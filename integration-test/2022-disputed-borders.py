# -*- encoding: utf-8 -*-
import dsl

from . import FixtureTest


class DisputedBoundariesTest(FixtureTest):
    def test_admin_level_viewpoint(self):
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
                'boundary': 'disputed',
                'name': 'Viewpoints on Disputed Administrative Boundaries',
                'disputed_by': 'SA,XX',
                'ne:brk_a3': 'B91',
                'type': 'linestring',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'id': 726514231,
                'kind:ps': 'locality',
                'kind': 'disputed_reference_line',
                'kind:us': 'region',
                # in the absence of a admin_level:XX, the disputed_by tag dictates the kind
                'kind:xx': 'unrecognized_region',
                # verifies the admin_level:SA overrides the disputed_by
                'kind:sa': 'region',
            })

        # make sure kind:vn didn't make it in because its admin_level doesn't map to anything
        self.assert_no_matching_feature(z, x, y, 'boundaries', {
            'id': 726514231,
            'kind:vn': None
        })

    def test_admin_level_3_state(self):
        z, x, y = (16, 53533, 28559)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/909074085
            dsl.way(909074085, dsl.tile_diagonal(z, x, y), {
                'admin_level': '3',
                'boundary': 'administrative',
                'place': 'state',
                'source': 'openstreetmap.org',
                'admin_level:XX': '2',
                'recognized_by': 'YY'
            }),
        )

        self.assert_no_matching_feature(
            z, x, y, 'boundaries', {
                'id': 909074085,
            })

    def test_admin_level_3_country(self):
        z, x, y = (16, 53533, 28559)

        self.generate_fixtures(
            # this one is made up - just place = country
            dsl.way(123456, dsl.tile_diagonal(z, x, y), {
                'admin_level': '3',
                'boundary': 'administrative',
                'place': 'country',
                'source': 'openstreetmap.org',
                'admin_level:XX': '2',
                'recognized_by': 'YY',
            }),
        )

        self.assert_no_matching_feature(
            z, x, y, 'boundaries', {
                'id': 123456,
            })

    def test_admin_level_3_other_place(self):
        z, x, y = (16, 53533, 28559)

        self.generate_fixtures(
            # also made up - we should ignore other place values
            dsl.way(345678, dsl.tile_diagonal(z, x, y), {
                'admin_level': '3',
                'boundary': 'administrative',
                'place': 'Neither state nor country',
                'source': 'openstreetmap.org',
                'admin_level:ZZ': '2'
            }),
        )

        self.assert_no_matching_feature(
            z, x, y, 'boundaries', {
                'id': 345678,
            })

    def test_disputed_by_to_unrecognized_disputed_reference_line(self):
        z, x, y = (16, 53533, 28559)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/13574166
            dsl.way(13574166, dsl.tile_diagonal(z, x, y), {
                'admin_level': '2',
                'boundary': 'disputed',
                'disputed_by': 'RU;PK;IL;PS;SA;EG;ID;BD',
                'name': '1949 Israeli-Syrian DMZ',
                'ne:brk_a3': 'B16',
                'ne_id': '1746705859;1746705871',
                'type': 'linestring',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'id': 13574166,
                'kind:ru': 'unrecognized_country',
                'kind:pk': 'unrecognized_country',
                'kind:il': 'unrecognized_country',
                'kind:ps': 'unrecognized_country',
                'kind:sa': 'unrecognized_country',
                'kind:eg': 'unrecognized_country',
                'kind:id': 'unrecognized_country',
                'kind:bd': 'unrecognized_country',
                'kind': 'disputed_reference_line',
                'kind_detail': '2',
            })

    def test_boundary_claim_disputed_by_claimed_by(self):
        z, x, y = (16, 53533, 28559)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/13574166
            dsl.way(202058477, dsl.tile_diagonal(z, x, y), {
                'admin_level': '2',
                'boundary': 'claim',
                'claimed_by': 'CN;TW',
                'disputed_by': 'IN;PK;TR',
                'name': 'Extent of Chinese Claim - ﻿Bara Hoti area',
                'name:de': 'Ausdehnung des chinesischen Anspruchs',
                'name:en': 'Extent of Chinese Claim - ﻿Bara Hoti area',
                'name:zh': '中国声称边境线',
                'name:zh_pinyin': 'Zhōngguó shēngchēng biānjìng xiàn',
                'ne:brk_a3': 'B02',
                'ne_id': '1746705405',
                'recognized_by': 'RU',
                'type': 'linestring',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'id': 202058477,
                'kind': 'disputed_claim',
                'kind:cn': 'country',
                'kind:tw': 'country',
                'kind:in': 'unrecognized_country',
                'kind:pk': 'unrecognized_country',
                'kind:tr': 'unrecognized_country',
                'kind:ru': 'country',
            })

    def test_boundary_claim_disputed_by_only(self):
        z, x, y = (16, 53533, 28559)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/13574166
            dsl.way(202058477, dsl.tile_diagonal(z, x, y), {
                'admin_level': '2',
                'boundary': 'claim',
                'disputed_by': 'IN;PK;TR',
                'name': 'Extent of Chinese Claim - ﻿Bara Hoti area',
                'name:de': 'Ausdehnung des chinesischen Anspruchs',
                'name:en': 'Extent of Chinese Claim - ﻿Bara Hoti area',
                'name:zh': '中国声称边境线',
                'name:zh_pinyin': 'Zhōngguó shēngchēng biānjìng xiàn',
                'ne:brk_a3': 'B02',
                'ne_id': '1746705405',
                'type': 'linestring',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'id': 202058477,
                'kind': 'disputed_claim',
                'kind:in': 'unrecognized_country',
                'kind:pk': 'unrecognized_country',
                'kind:tr': 'unrecognized_country',
            })

    def test_boundary_dispute_disputed_by_claimed_by(self):
        z, x, y = (16, 53533, 28559)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/202058477
            dsl.way(202058477, dsl.tile_diagonal(z, x, y), {
                'admin_level': '2',
                'boundary': 'disputed',
                'claimed_by': 'CN;TW',
                'disputed_by': 'IN',
                'name': 'Extent', 'of': 'Chinese', 'Claim': 'at', 'Aksai': 'Chin',
                'name:ur': 'اکسائی', 'چن': 'میں', 'چینی': 'دعوے', 'کی': 'حد',
                'ne:brk_a3': 'B07',
                'ne_id': '1746705319',
                'recognized_by': 'RU;PK;TR',
                'type': 'linestring',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'id': 202058477,
                'kind:in': 'unrecognized_country',
                'kind:cn': 'country',
                'kind:tw': 'country',
                'kind:ru': 'country',
                'kind:pk': 'country',
                'kind:tr': 'country',
                'kind': 'disputed_reference_line',
                'kind_detail': '2',
            })

    def test_boundary_dispute_no_disputed_by_claimed_by(self):
        z, x, y = (16, 53533, 28559)

        self.generate_fixtures(
            # https://www.openstreetmap.org/relation/202058477
            dsl.way(202058477, dsl.tile_diagonal(z, x, y), {
                'admin_level': '2',
                'boundary': 'disputed',
                'name': 'Extent of Indian Claim at Bara Hotii Valleys',
                'ne:brk_a3': 'B02',
                'ne_id': '1746708469',
                'type': 'linestring',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'boundaries', {
                'id': 202058477,
                'kind': 'disputed_reference_line',
                'kind_detail': '2',
            })
