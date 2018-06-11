# -*- encoding: utf-8 -*-
from . import FixtureTest


class VietnameseShieldTest(FixtureTest):

    def test_1_vnnational(self):
        import dsl

        z, x, y = (16, 52053, 31002)

        self.generate_fixtures(
            dsl.is_in('VN', z, x, y),
            # https://www.openstreetmap.org/way/10417532
            dsl.way(10417532, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'name': u'Quốc lộ 1',
                'ref': u'QL 1',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 10417532,
                'network': u'VN:national',
                'shield_text': u'QL1',
            })

    def test_5a_vnnational(self):
        import dsl

        z, x, y = (16, 52044, 28845)

        self.generate_fixtures(
            dsl.is_in('VN', z, x, y),
            # https://www.openstreetmap.org/way/9975059
            dsl.way(9975059, dsl.tile_diagonal(z, x, y), {
                'highway': u'trunk',
                'int_ref': u'AH14',
                'name': u'Nguyễn Văn Linh',
                'name:en': u'Nguyen Van Linh',
                'oneway': u'yes',
                'ref': u'QL.5A',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
            dsl.relation(1, {
                'distance': u'132',
                'int_ref': u'AH14',
                'name': u'Quốc lộ 5A',
                'name:en': u'National Highway 5A',
                'network': u'VN:national',
                'ref': u'QL.5A',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[9975059]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 9975059,
                'network': u'VN:national',
                'shield_text': u'QL5A',
            })

    def test_6_vnnational(self):
        import dsl

        z, x, y = (16, 51700, 28806)

        self.generate_fixtures(
            dsl.is_in('VN', z, x, y),
            # https://www.openstreetmap.org/way/38146838
            dsl.way(38146838, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'ref': u'QL6',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 38146838,
                'network': u'VN:national',
                'shield_text': u'QL6',
            })

    def test_ct08_vnexpressway(self):
        import dsl

        z, x, y = (16, 52021, 28855)

        self.generate_fixtures(
            dsl.is_in('VN', z, x, y),
            # https://www.openstreetmap.org/way/11836293
            dsl.way(11836293, dsl.tile_diagonal(z, x, y), {
                'access': u'yes',
                'bicycle': u'no',
                'foot': u'no',
                'highway': u'motorway',
                'horse': u'no',
                'maxspeed': u'120',
                'motorcar': u'yes',
                'motorcycle': u'no',
                'name': u'Đại lộ Thăng Long',
                'name:en': u'Thang Long Avenue',
                'oneway': u'yes',
                'overtaking': u'yes',
                'ref': u'CT.08',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'alt_name': u'Đường cao tốc Láng - Hòa Lạc',
                'alt_name:en': u'Lang - Hoa Lac Expressway',
                'distance': u'30',
                'name': u'Đại lộ Thăng Long',
                'name:en': u'Thang Long Avenue',
                'ref': u'CT.08',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[11836293]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 11836293,
                'network': u'VN:expressway',
                'shield_text': u'CT08',
            })

    def test_ct01_vnexpressway(self):
        import dsl

        z, x, y = (16, 52150, 30818)

        self.generate_fixtures(
            dsl.is_in('VN', z, x, y),
            # https://www.openstreetmap.org/way/129963821
            dsl.way(129963821, dsl.tile_diagonal(z, x, y), {
                'bridge': u'yes',
                'highway': u'motorway',
                'lanes': u'2',
                'layer': u'1',
                'maxspeed': u'100',
                'name': u'TP Hồ Chí Minh - Trung Lương',
                'oneway': u'yes',
                'ref': u'CT01',
                'source': u'openstreetmap.org',
                'toll': u'yes',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 129963821,
                'network': u'VN:expressway',
                'shield_text': u'CT01',
            })

    def test_dt494b_vnprovincial(self):
        import dsl

        z, x, y = (16, 52045, 28948)

        self.generate_fixtures(
            dsl.is_in('VN', z, x, y),
            # https://www.openstreetmap.org/way/10592872
            dsl.way(10592872, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'name': u'Đường tỉnh 494B',
                'ref': u'ĐT.494B',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 10592872,
                'network': u'VN:provincial',
                'shield_text': u'ĐT494B',
            })

    def test_dt388_vnprovincial(self):
        import dsl

        z, x, y = (16, 52176, 28882)

        self.generate_fixtures(
            dsl.is_in('VN', z, x, y),
            # https://www.openstreetmap.org/way/160413329
            dsl.way(160413329, dsl.tile_diagonal(z, x, y), {
                'bicycle': u'yes',
                'cycleway': u'no',
                'foot': u'yes',
                'highway': u'secondary',
                'maxspeed': u'40',
                'name': u'Đường 208',
                'oneway': u'no',
                'ref': u'ĐT 388',
                'source': u'openstreetmap.org',
                'surface': u'asphalt',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 160413329,
                'network': u'VN:provincial',
                'shield_text': u'ĐT388',
            })

    def test_dt825_vnprovincial(self):
        import dsl

        z, x, y = (16, 52156, 30791)

        self.generate_fixtures(
            dsl.is_in('VN', z, x, y),
            # https://www.openstreetmap.org/way/516091228
            dsl.way(516091228, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'oneway': u'yes',
                'ref': u'ĐT825',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 516091228,
                'network': u'VN:provincial',
                'shield_text': u'ĐT825',
            })

    def test_dt112_vnprovincial(self):
        import dsl

        z, x, y = (16, 51772, 28797)

        self.generate_fixtures(
            dsl.is_in('VN', z, x, y),
            # https://www.openstreetmap.org/way/469922155
            dsl.way(469922155, dsl.tile_diagonal(z, x, y), {
                'access': u'no',
                'highway': u'secondary',
                'ref': u'DT112',
                'source': u'openstreetmap.org',
                'surface': u'ground',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 469922155,
                'network': u'VN:provincial',
                'shield_text': u'ĐT112',
            })

    def test_tl15_vnprovincial(self):
        import dsl

        z, x, y = (16, 52147, 30724)

        self.generate_fixtures(
            dsl.is_in('VN', z, x, y),
            # https://www.openstreetmap.org/way/32578611
            dsl.way(32578611, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name': u'Tỉnh lộ 15',
                'ref': u'TL 15',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 32578611,
                'network': u'VN:provincial',
                'shield_text': u'TL15',
            })

    def test_tl8_vnprovincial(self):
        import dsl

        z, x, y = (16, 52153, 30758)

        self.generate_fixtures(
            dsl.is_in('VN', z, x, y),
            # https://www.openstreetmap.org/way/32580225
            dsl.way(32580225, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'name': u'Tỉnh lộ 8',
                'oneway': u'-1',
                'ref': u'TL.8',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 32580225,
                'network': u'VN:provincial',
                'shield_text': u'TL8',
            })

    def test_vntl(self):
        import dsl

        z, x, y = (16, 52078, 29058)

        self.generate_fixtures(
            dsl.is_in('VN', z, x, y),
            # https://www.openstreetmap.org/way/161484320
            dsl.way(161484320, dsl.tile_diagonal(z, x, y), {
                'alt_name': u'Đường Cà Mau',
                'highway': u'secondary',
                'name': u'Tỉnh lộ 481',
                'ref': u'481',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'alt_name': u'Đường Cà Mau',
                'highway': u'secondary',
                'name': u'Tỉnh lộ 481',
                'network': u'VN-TL',
                'ref': u'481',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[161484320]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 161484320,
                'shield_text': u'TL481',
                'network': u'VN:provincial',
            })

    def test_viroads(self):
        # despite the network tag, this is actually in Vietnam (ISO code VN,
        # not VI).
        import dsl

        z, x, y = (16, 51909, 28995)

        self.generate_fixtures(
            dsl.is_in('VN', z, x, y),
            # https://www.openstreetmap.org/way/48844918
            dsl.way(48844918, dsl.tile_diagonal(z, x, y), {
                'highway': u'secondary',
                'ref': u'217',
                'source': u'openstreetmap.org',
            }),
            dsl.relation(1, {
                'network': u'VI-roads',
                'ref': u'217',
                'route': u'road',
                'source': u'openstreetmap.org',
                'type': u'route',
            }, ways=[48844918]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 48844918,
                'shield_text': '217',
                'network': u'VN:road',
            })

    def test_ql1k_vnnational(self):
        import dsl

        z, x, y = (16, 52209, 30770)

        self.generate_fixtures(
            dsl.is_in('VN', z, x, y),
            # https://www.openstreetmap.org/way/568398699
            dsl.way(568398699, dsl.tile_diagonal(z, x, y), {
                'highway': u'primary',
                'name': u'Quốc lộ 1K',
                'oneway': u'yes',
                'ref': u'1K',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 568398699,
                'network': u'VN:national',
                'shield_text': u'QL1K',
            })
