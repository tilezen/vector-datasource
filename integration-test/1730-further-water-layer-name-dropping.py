# -*- encoding: utf-8 -*-
from . import FixtureTest


class LowZoomWaterTest(FixtureTest):

    def test_no_lake_labels_z3(self):
        import dsl

        z, x, y = (3, 2, 2)

        self.generate_fixtures(
            dsl.way(1, dsl.box_area(z, x, y, 181063240412.622467), {
                'admin': u'admin-0',
                'featurecla': u'Lake',
                'min_label': 3.6,
                'min_zoom': 1.7,
                'name': u'Lake Superior',
                'name_abb': u'Whitefish Bay',
                'name_ar': u'بحيرة سوبيريور',
                'name_bn': u'সুপিরিয়র হ্রদ',
                'name_de': u'Oberer See',
                'name_el': u'λίμνη Σουπίριορ',
                'name_en': u'Lake Superior',
                'name_es': u'Lago Superior',
                'name_fr': u'lac Supérieur',
                'name_hi': u'सुपीरियर झील',
                'name_hu': u'Felső-tó',
                'name_id': u'Danau Superior',
                'name_it': u'lago Superiore',
                'name_ja': u'スペリオル湖',
                'name_ko': u'슈피리어 호',
                'name_nl': u'Bovenmeer',
                'name_pl': u'Jezioro Górne',
                'name_pt': u'Lago Superior',
                'name_ru': u'Верхнее',
                'name_sv': u'Övre sjön',
                'name_tr': u'Superior Gölü',
                'name_vi': u'Hồ Thượng',
                'name_zh': u'苏必利尔湖',
                'scalerank': 1,
                'source': u'naturalearthdata.com',
                'wikidataid': u'Q1066',
            }),
        )

        # should NOT get a label placement point
        self.assert_no_matching_feature(
            z, x, y, 'water', {
                'kind': 'lake',
                'label_placement': True,
            })

        # should get a polygon - but it should NOT have any names or name
        # translations.
        self.assert_has_feature(
            z, x, y, 'water', {
                'kind': 'lake',
                'name': type(None),
                'name:fr': type(None),
            })

    def test_no_label_lake_athabasca_z4(self):
        import dsl

        z, x, y = (4, 3, 4)

        self.generate_fixtures(
            dsl.way(1, dsl.box_area(z, x, y, 31390412728.710949), {
                'featurecla': u'Lake',
                'label': u'Lake Athabasca',
                'min_label': 3.7,
                'min_zoom': 2.0,
                'name': u'Lake Athabasca',
                'name_abb': u'L. Athabasca',
                'name_de': u'Athabascasee',
                'name_en': u'Lake Athabasca',
                'name_es': u'Lago Athabasca',
                'name_fr': u'lac Athabasca',
                'name_hu': u'Atabaszk-tó',
                'name_it': u'Athabasca',
                'name_ja': u'アサバスカ湖',
                'name_nl': u'Athabascameer',
                'name_pl': u'Athabaska',
                'name_pt': u'Lago Athabasca',
                'name_ru': u'Атабаска',
                'name_sv': u'Athabascasjön',
                'name_tr': u'Athabasca Gölü',
                'name_zh': u'阿薩巴斯卡湖',
                'ne_id': u'1159106863',
                'scalerank': 2,
                'source': u'naturalearthdata.com',
                'wdid_score': 4,
                'wikidataid': u'Q272463',
            }),
        )

        # we shouldn't get a label placement point
        self.assert_no_matching_feature(
            z, x, y, 'water', {
                'kind': 'lake',
                'label_placement': True,
            })

        # but we should get a lake polygon, but that lake polygon shouldn't
        # have names or name translations on it.
        self.assert_has_feature(
            z, x, y, 'water', {
                'kind': 'lake',
                'name': type(None),
                'name:fr': type(None),
            })
