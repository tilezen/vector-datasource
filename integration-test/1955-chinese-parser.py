# -*- encoding: utf-8 -*-
import dsl
from shapely.wkt import loads as wkt_loads
from . import FixtureTest


class ChineseNameTest(FixtureTest):
    def test_san_francisco_osm(self):
        # San Francisco (osm city)
        self.generate_fixtures(dsl.way(26819236, wkt_loads(
            'POINT (-122.419236226182 37.77928077351228)'),
                                       {u'name:pt': u'S\xe3o Francisco',
                                        u'name:ko':
                                            u'\uc0cc\ud504\ub780\uc2dc\uc2a4\ucf54',  # noqa
                                        u'name:kn':
                                            u'\u0cb8\u0cbe\u0ca8\u0ccd '
                                            u'\u0cab\u0ccd\u0cb0\u0cbe\u0ca8\u0ccd\u0cb8\u0cbf\u0cb8\u0ccd\u0c95\u0cca',  # noqa
                                        u'rank': u'10',
                                        u'wikidata': u'Q62',
                                        u'name:ru':
                                            u'\u0421\u0430\u043d-\u0424\u0440\u0430\u043d\u0446\u0438\u0441\u043a\u043e',  # noqa
                                        u'name:ta':
                                            u'\u0bb8\u0bbe\u0ba9\u0bcd '
                                            u'\u0baa\u0bcd\xb2\u0bb0\u0bbe\u0ba9\u0bcd\u0bb8\u0bbf\u0bb8\u0bcd\u0b95\u0bca',  # noqa
                                        u'name:fa': u'\u0633\u0627\u0646 '
                                                    u'\u0641\u0631\u0627\u0646\u0633\u06cc\u0633\u06a9\u0648',  # noqa
                                        u'is_in:country': u'United States',
                                        u'wikipedia': u'en:San Francisco',
                                        u'name:de': u'San Francisco',
                                        u'source': u'openstreetmap.org',
                                        u'name:zh': u'旧金山/三藩市/舊金山',
                                        u'name:zh-Hans': u'旧金山',
                                        u'name:zh-Hant': u'舊金山',
                                        u'name:zh-Hant-hk': u'三藩市',
                                        u'name:zh-Hant-tw': u'舊金山',
                                        u'name:ja':
                                            u'\u30b5\u30f3\u30d5\u30e9\u30f3\u30b7\u30b9\u30b3',  # noqa
                                        u'short_name': u'SF',
                                        u'name:hi': u'\u0938\u0948\u0928 '
                                                    u'\u092b\u094d\u0930\u093e\u0902\u0938\u093f\u0938\u094d\u0915\u094b',  # noqa
                                        u'is_in:country_code': u'US',
                                        u'census:population': u'2010',
                                        u'population': u'864816',
                                        u'fixme': u'When zooming out, '
                                                  u'Oakland (a nearby city) '
                                                  u'label covers over the '
                                                  u'San Francisco label',
                                        u'name': u'San Francisco',
                                        u'place': u'city',
                                        u'is_in:continent': u'North America',
                                        u'name:eu': u'San Francisco'}))  # noqa

        self.assert_has_feature(
            16, 10482, 25330, 'places',
            {'id': 26819236, 'kind': 'locality', 'kind_detail': 'city',
             'source': "openstreetmap.org",
             'name': 'San Francisco',
             'name:zh': u'旧金山',
             'name:zht': u'舊金山'})

        self.assert_no_matching_feature(
            16, 10482, 25330, 'places',
            {'name:zh-default': u'旧金山/三藩市/舊金山'})

    def test_hollywood_wof(self):
        # Hollywood (wof neighbourhood)
        self.generate_fixtures(
            dsl.way(85826037, wkt_loads('POINT (-118.326908 34.10021)'),
                    {u'name:szl_x': u'Hollywood', u'name:eus_x': u'Hollywood',
                     u'placetype': u'neighbourhood',
                     u'name:mal_x':
                         u'\u0d39\u0d4b\u0d33\u0d3f\u0d35\u0d41\u0d21\u0d4d',
                     u'name:vep_x': u'Gollivud', u'name:ilo_x': u'Hollywood',
                     u'name:may_x': u'Hollywood', u'name:fra_x': u'Hollywood',
                     u'name:ido_x': u'Hollywood', u'name:hun_x': u'Hollywood',
                     u'name:tgk_x':
                         u'\u04b2\u043e\u043b\u043b\u0438\u0432\u0443\u0434',
                     u'name:scn_x': u'Hollywood', u'name:diq_x': u'Hollywood',
                     u'name:tel_x':
                         u'\u0c39\u0c3e\u0c32\u0c40\u0c35\u0c41\u0c21\u0c4d',
                     u'source': u'whosonfirst.org',
                     u'name:fry_x': u'Hollywood', u'name:ita_x': u'Hollywood',
                     u'name:zho_cn_x_preferred': u'好莱坞',
                     u'name:zho_tw_x_preferred': u'好萊塢',
                     u'name:hbs_x': u'Hollywood', u'name:hrv_x': u'Hollywood',
                     u'name:cym_x': u'Hollywood',
                     u'name:yid_x':
                         u'\u05d4\u05d0\u05dc\u05d9\u05d5\u05d5\u05d0\u05d3',
                     u'name:lit_x': u'Holivudas', u'name:dut_x': u'Hollywood',
                     u'name:bul_x':
                         u'\u0425\u043e\u043b\u0438\u0432\u0443\u0434',
                     u'name:rum_x': u'Hollywood',
                     u'name:srp_x':
                         u'\u0425\u043e\u043b\u0438\u0432\u0443\u0434',
                     u'name:afr_x': u'Hollywood', u'name': u'Hollywood',
                     u'name:ukr_x':
                         u'\u0413\u043e\u043b\u043b\u0456\u0432\u0443\u0434',
                     u'name:lat_x': u'Ruscisilva',
                     u'name:gre_x':
                         u'\u03a7\u03cc\u03bb\u03c5\u03b3\u03bf\u03c5\u03bd'
                         u'\u03c4',
                     u'name:tam_x':
                         u'\u0bb9\u0bbe\u0bb2\u0bbf\u0bb5\u0bc1\u0b9f\u0bcd',
                     u'name:lav_x': u'Holivuda', u'name:ksh_x': u'Hollywood',
                     u'name:ell_x':
                         u'\u03a7\u03cc\u03bb\u03c5\u03b3\u03bf\u03c5\u03bd'
                         u'\u03c4',
                     u'name:mac_x':
                         u'\u0425\u043e\u043b\u0438\u0432\u0443\u0434',
                     u'name:zho_yue_x': u'\u8377\u91cc\u6d3b',
                     u'max_zoom': 18.0, u'name:slo_x': u'Hollywood',
                     u'name:hye_x':
                         u'\u0540\u0578\u056c\u056b\u057e\u0578\u0582\u0564',
                     u'name:yue_x': u'\u8377\u91cc\u6d3b',
                     u'name:vie_x': u'Hollywood', u'name:msa_x': u'Hollywood',
                     u'name:spa_x': u'Hollywood', u'name:epo_x': u'Holivudo',
                     u'name:vol_x': u'Hollywood', u'name:sco_x': u'Hollywood',
                     u'name:lim_x': u'Hollywood', u'name:ind_x': u'Hollywood',
                     u'name:kor_x': u'\ud5d0\ub9ac\uc6b0\ub4dc',
                     u'name:kan_x':
                         u'\u0cb9\u0cbe\u0cb2\u0cbf\u0cb5\u0cc1\u0ca1\u0ccd',
                     u'name:ben_x': u'\u09b9\u09b2\u09bf\u0989\u09a1',
                     u'name:tha_x':
                         u'\u0e2e\u0e2d\u0e25\u0e25\u0e35\u0e27\u0e39\u0e14',
                     u'name:geo_x':
                         u'\u10f0\u10dd\u10da\u10d8\u10d5\u10e3\u10d3\u10d8',
                     u'name:por_x': u'Hollywood',
                     u'name:mar_x':
                         u'\u0939\u0949\u0932\u093f\u0935\u0942\u0921',
                     u'name:slk_x': u'Hollywood', u'name:yor_x': u'Hollywood',
                     u'name:nep_x': u'\u0939\u0932\u093f\u0909\u0921',
                     u'name:ice_x': u'Hollywood',
                     u'name:pus_x':
                         u'\u0647\u0627\u0644\u064a\u0648\u0648\u0689',
                     u'name:swe_x': u'Hollywood', u'name:ron_x': u'Hollywood',
                     u'name:rus_x':
                         u'\u0413\u043e\u043b\u043b\u0438\u0432\u0443\u0434',
                     u'name:jav_x': u'Hollywood', u'name:fre_x': u'Hollywood',
                     u'name:nno_x': u'Hollywood', u'name:bos_x': u'Hollywood',
                     u'name:fin_x': u'Hollywood', u'name:swa_x': u'Hollywood',
                     u'name:nld_x': u'Hollywood', u'name:ast_x': u'Hollywood',
                     u'name:ara_x':
                         u'\u0647\u0648\u0644\u064a\u0648\u0648\u062f',
                     u'name:mkd_x':
                         u'\u0425\u043e\u043b\u0438\u0432\u0443\u0434',
                     u'name:bel_x':
                         u'\u0413\u0430\u043b\u0456\u0432\u0443\u0434',
                     u'name:eng_x': u'Hollywood',
                     u'name:azb_x':
                         u'\u0647\u0627\u0644\u06cc\u0648\u0648\u062f',
                     u'name:tat_x':
                         u'\u0413\u043e\u043b\u043b\u0438\u0432\u0443\u0434',
                     u'name:dan_x': u'Hollywood', u'min_zoom': 11.0,
                     u'name:nob_x': u'Hollywood',
                     u'name:fas_x':
                         u'\u0647\u0627\u0644\u06cc\u0648\u0648\u062f\u060c '
                         u'\u0644\u0633\u200c\u0622\u0646\u062c\u0644\u0633',
                     u'name:fao_x': u'Hollywood', u'name:glv_x': u'Hollywood',
                     u'name:nah_x': u'Hollywood',
                     u'name:jpn_x': u'\u30cf\u30ea\u30a6\u30c3\u30c9',
                     u'name:arm_x':
                         u'\u0540\u0578\u056c\u056b\u057e\u0578\u0582\u0564',
                     u'name:pol_x': u'Hollywood', u'name:nan_x': u'Hollywood',
                     u'name:wel_x': u'Hollywood', u'name:cze_x': u'Hollywood',
                     u'name:cat_x': u'Hollywood',
                     u'name:heb_x':
                         u'\u05d4\u05d5\u05dc\u05d9\u05d5\u05d5\u05d3',
                     u'name:kat_x':
                         u'\u10f0\u10dd\u10da\u10d8\u10d5\u10e3\u10d3\u10d8',
                     u'name:ori_x': u'\u0b39\u0b32\u0b3f\u0b09\u0b21\u0b3c',
                     u'name:nor_x': u'Hollywood',
                     u'name:kaz_x':
                         u'\u0413\u043e\u043b\u043b\u0438\u0432\u0443\u0434',
                     u'name:urd_x': u'\u06c1\u0627\u0644\u06cc \u0648\u0688',
                     u'name:ger_x': u'Hollywood', u'name:isl_x': u'Hollywood',
                     u'name:tur_x': u'Hollywood', u'name:tgl_x': u'Hollywood',
                     u'name:war_x': u'Hollywood',
                     u'name:ltz_x': u'Hollywood',
                     u'name:aze_x': u'Hollivud', u'name:est_x': u'Hollywood',
                     u'name:zho_min_nan_x': u'Hollywood',
                     u'name:oci_x': u'Hollywood', u'name:sqi_x': u'Hollywood',
                     u'name:baq_x': u'Hollywood',
                     u'name:chi_x': u'\u597d\u83b1\u575e',
                     u'name:deu_x': u'Hollywood', u'name:alb_x': u'Hollywood',
                     u'name:bre_x': u'Hollywood',
                     u'name:slv_x': u'Hollywood', u'name:gle_x': u'Hollywood',
                     u'name:ces_x': u'Hollywood', u'name:glg_x': u'Hollywood',
                     u'name:amh_x': u'\u1206\u120a\u12cd\u12f5',
                     u'name:sgs_x': u'Huol\u0117vods'}))  # noqa

        self.assert_has_feature(
            16, 11227, 26157, 'places',
            {'id': 85826037, 'kind': 'neighbourhood',
             'source': "whosonfirst.org",
             'name': 'Hollywood',
             'name:zh': u'好莱坞',
             'name:zht': u'好萊塢'})
