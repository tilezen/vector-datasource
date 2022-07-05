from . import FixtureTest


class FixBadUnicodeShieldText(FixtureTest):

    def test_cyrillic(self):
        # route relation with a cyrillic capital letter Ka at the end.
        import dsl
        from shapely.wkt import loads as wkt_loads
        self.generate_fixtures(
            dsl.way(425415345, dsl.tile_diagonal(16, 63085, 15623), {
                u'highway': u'secondary',
                u'layer': u'1',
                u'name': u'\u0430\u0432\u0442\u043E\u0437\u0438\u043C\u043D\u0438\u043A \u0411\u0438\u043B\u0438\u0431\u0438\u043D\u043E - \u041F\u0435\u0432\u0435\u043A',
                u'ref': u'77\u041A-012',
                u'source': u'openstreetmap.org',
                u'winter_road': u'yes'
            }),
            dsl.relation(3948946, {
                u'source': u'openstreetmap.org',
                u'highway': u'primary',
                u'name': '\u041F\u0435\u0432\u0435\u043A \u2014 \u0411\u0438\u043B\u0438\u0431\u0438\u043D\u043E',
                u'distance': u'337.400',
                u'network': u'ru:regional',
                u'ref': u'77\u041A-012',
                u'route': u'road',
                u'type': u'route'
            }, ways=[425415345]),
            dsl.way(-3948946, dsl.tile_diagonal(16, 63085, 15623), {
                u'source': u'openstreetmap.org',
                u'highway': u'primary',
                u'name': '\u041F\u0435\u0432\u0435\u043A \u2014 \u0411\u0438\u043B\u0438\u0431\u0438\u043D\u043E',
                u'distance': u'337.400',
                u'network': u'ru:regional',
                u'ref': u'77\u041A-012',
                u'route': u'road',
                u'type': u'route'
            }),
        )

        self.assert_has_feature(
            16, 63085, 15623, 'roads',
            {'id': 425415345, 'shield_text': u'77\u041a'})

        self.assert_has_feature(
            16, 63085, 15623, 'roads',
            {'id': -3948946, 'osm_relation': type(None),
             'shield_text': u'77\u041a'})
