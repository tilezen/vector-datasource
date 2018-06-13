# -*- coding: utf-8 -*-
from . import FixtureTest


class LowZoomTranslationTest(FixtureTest):

    def test_new_york(self):
        import dsl

        z, x, y = (6, 18, 24)

        self.generate_fixtures(
            dsl.way(1, dsl.tile_centre_shape(z, x, y), {
                'featurecla': u'Populated place',
                'min_zoom': u'1.7',
                'name': u'New York',
                'name_ar': u'نيويورك',
                'name_bn': u'নিউ ইয়র্ক সিটি',
                'name_de': u'New York City',
                'name_el': u'Νέα Υόρκη',
                'name_en': u'New York City',
                'name_es': u'Nueva York',
                'name_fr': u'New York',
                'name_hi': u'न्यूयॉर्क नगर',
                'name_hu': u'New York',
                'name_id': u'New York City',
                'name_it': u'New York',
                'name_ja': u'ニューヨーク',
                'name_ko': u'뉴욕',
                'name_nl': u'New York City',
                'name_pl': u'Nowy Jork',
                'name_pt': u'Nova Iorque',
                'name_ru': u'Нью-Йорк',
                'name_sv': u'New York',
                'name_tr': u'New York',
                'name_vi': u'Thành phố New York',
                'name_zh': u'纽约',
                'namealt': u'New York-Newark',
                'nameascii': u'New York',
                'namediff': u'0',
                'namepar': u'',
                'ne_id': u'1159151575',
                'scalerank': 0,
                'source': u'naturalearthdata.com',
                'wikidataid': u'Q60',
                'wof_id': u'85977539',
                'worldcity': u'1.0',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'places', {
                'id': 1,
                'name': u'New York',
                'name:en': u'New York City',
                'name:el': u'Νέα Υόρκη',
                'name:es': u'Nueva York',
            })
