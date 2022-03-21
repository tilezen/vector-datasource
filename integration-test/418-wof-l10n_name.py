# -*- encoding: utf-8 -*-
import dsl
from shapely.wkt import loads as wkt_loads

from . import FixtureTest


class WofL10nName(FixtureTest):
    def test_hollywood(self):
        # Hollywood (wof neighbourhood)
        self.generate_fixtures(dsl.way(85826037, wkt_loads('POINT (-118.326908 34.10021)'), {u'name:szl_x': u'Hollywood', u'name:eus_x': u'Hollywood', u'placetype': u'neighbourhood', u'name:mal_x': u'\u0d39\u0d4b\u0d33\u0d3f\u0d35\u0d41\u0d21\u0d4d', u'name:vep_x': u'Gollivud', u'name:ilo_x': u'Hollywood', u'name:may_x': u'Hollywood', u'name:fra_x': u'Hollywood', u'name:ido_x': u'Hollywood', u'name:hun_x': u'Hollywood', u'name:tgk_x': u'\u04b2\u043e\u043b\u043b\u0438\u0432\u0443\u0434', u'name:scn_x': u'Hollywood', u'name:diq_x': u'Hollywood', u'name:tel_x': u'\u0c39\u0c3e\u0c32\u0c40\u0c35\u0c41\u0c21\u0c4d', u'source': u'whosonfirst.org', u'name:fry_x': u'Hollywood', u'name:ita_x': u'Hollywood', u'name:zho_x': u'\u597d\u83b1\u575e', u'name:hbs_x': u'Hollywood', u'name:hrv_x': u'Hollywood', u'name:cym_x': u'Hollywood', u'name:yid_x': u'\u05d4\u05d0\u05dc\u05d9\u05d5\u05d5\u05d0\u05d3', u'name:lit_x': u'Holivudas', u'name:dut_x': u'Hollywood', u'name:bul_x': u'\u0425\u043e\u043b\u0438\u0432\u0443\u0434', u'name:rum_x': u'Hollywood', u'name:srp_x': u'\u0425\u043e\u043b\u0438\u0432\u0443\u0434', u'name:afr_x': u'Hollywood', u'name': u'Hollywood', u'name:ukr_x': u'\u0413\u043e\u043b\u043b\u0456\u0432\u0443\u0434', u'name:lat_x': u'Ruscisilva', u'name:gre_x': u'\u03a7\u03cc\u03bb\u03c5\u03b3\u03bf\u03c5\u03bd\u03c4', u'name:tam_x': u'\u0bb9\u0bbe\u0bb2\u0bbf\u0bb5\u0bc1\u0b9f\u0bcd', u'name:lav_x': u'Holivuda', u'name:ksh_x': u'Hollywood', u'name:ell_x': u'\u03a7\u03cc\u03bb\u03c5\u03b3\u03bf\u03c5\u03bd\u03c4', u'name:mac_x': u'\u0425\u043e\u043b\u0438\u0432\u0443\u0434', u'name:zho_yue_x': u'\u8377\u91cc\u6d3b', u'max_zoom': 18.0, u'name:slo_x': u'Hollywood', u'name:hye_x': u'\u0540\u0578\u056c\u056b\u057e\u0578\u0582\u0564', u'name:yue_x': u'\u8377\u91cc\u6d3b', u'name:vie_x': u'Hollywood', u'name:msa_x': u'Hollywood', u'name:spa_x': u'Hollywood', u'name:epo_x': u'Holivudo', u'name:vol_x': u'Hollywood', u'name:sco_x': u'Hollywood', u'name:lim_x': u'Hollywood', u'name:ind_x': u'Hollywood', u'name:kor_x': u'\ud5d0\ub9ac\uc6b0\ub4dc', u'name:kan_x': u'\u0cb9\u0cbe\u0cb2\u0cbf\u0cb5\u0cc1\u0ca1\u0ccd', u'name:ben_x': u'\u09b9\u09b2\u09bf\u0989\u09a1', u'name:tha_x': u'\u0e2e\u0e2d\u0e25\u0e25\u0e35\u0e27\u0e39\u0e14', u'name:geo_x': u'\u10f0\u10dd\u10da\u10d8\u10d5\u10e3\u10d3\u10d8', u'name:por_x': u'Hollywood', u'name:mar_x': u'\u0939\u0949\u0932\u093f\u0935\u0942\u0921', u'name:slk_x': u'Hollywood', u'name:yor_x': u'Hollywood', u'name:nep_x': u'\u0939\u0932\u093f\u0909\u0921', u'name:ice_x': u'Hollywood', u'name:pus_x': u'\u0647\u0627\u0644\u064a\u0648\u0648\u0689', u'name:swe_x': u'Hollywood', u'name:ron_x': u'Hollywood', u'name:rus_x': u'\u0413\u043e\u043b\u043b\u0438\u0432\u0443\u0434',
                               u'name:jav_x': u'Hollywood', u'name:fre_x': u'Hollywood', u'name:nno_x': u'Hollywood', u'name:bos_x': u'Hollywood', u'name:fin_x': u'Hollywood', u'name:swa_x': u'Hollywood', u'name:nld_x': u'Hollywood', u'name:ast_x': u'Hollywood', u'name:ara_x': u'\u0647\u0648\u0644\u064a\u0648\u0648\u062f', u'name:mkd_x': u'\u0425\u043e\u043b\u0438\u0432\u0443\u0434', u'name:bel_x': u'\u0413\u0430\u043b\u0456\u0432\u0443\u0434', u'name:eng_x': u'Hollywood', u'name:azb_x': u'\u0647\u0627\u0644\u06cc\u0648\u0648\u062f', u'name:tat_x': u'\u0413\u043e\u043b\u043b\u0438\u0432\u0443\u0434', u'name:dan_x': u'Hollywood', u'min_zoom': 11.0, u'name:nob_x': u'Hollywood', u'name:fas_x': u'\u0647\u0627\u0644\u06cc\u0648\u0648\u062f\u060c \u0644\u0633\u200c\u0622\u0646\u062c\u0644\u0633', u'name:fao_x': u'Hollywood', u'name:glv_x': u'Hollywood', u'name:nah_x': u'Hollywood', u'name:jpn_x': u'\u30cf\u30ea\u30a6\u30c3\u30c9', u'name:arm_x': u'\u0540\u0578\u056c\u056b\u057e\u0578\u0582\u0564', u'name:pol_x': u'Hollywood', u'name:nan_x': u'Hollywood', u'name:wel_x': u'Hollywood', u'name:cze_x': u'Hollywood', u'name:cat_x': u'Hollywood', u'name:heb_x': u'\u05d4\u05d5\u05dc\u05d9\u05d5\u05d5\u05d3', u'name:kat_x': u'\u10f0\u10dd\u10da\u10d8\u10d5\u10e3\u10d3\u10d8', u'name:ori_x': u'\u0b39\u0b32\u0b3f\u0b09\u0b21\u0b3c', u'name:nor_x': u'Hollywood', u'name:kaz_x': u'\u0413\u043e\u043b\u043b\u0438\u0432\u0443\u0434', u'name:urd_x': u'\u06c1\u0627\u0644\u06cc \u0648\u0688', u'name:ger_x': u'Hollywood', u'name:isl_x': u'Hollywood', u'name:tur_x': u'Hollywood', u'name:tgl_x': u'Hollywood', u'name:ckb_x': u'\u06be\u06c6\u0644\u06cc\u0648\u0648\u062f', u'name:war_x': u'Hollywood', u'name:xmf_x': u'\u10f0\u10dd\u10da\u10d8\u10d5\u10e3\u10d3\u10d8', u'name:per_x': u'\u0647\u0627\u0644\u06cc\u0648\u0648\u062f\u060c \u06a9\u0627\u0644\u06cc\u0641\u0631\u0646\u06cc\u0627', u'name:ltz_x': u'Hollywood', u'name:mya_x': u'\u101f\u1031\u102c\u101c\u102d\u101d\u102f\u1012\u103a', u'name:aze_x': u'Hollivud', u'name:est_x': u'Hollywood', u'name:zho_min_nan_x': u'Hollywood', u'name:oci_x': u'Hollywood', u'name:sqi_x': u'Hollywood', u'name:hin_x': u'\u0939\u0949\u0932\u0940\u0935\u0941\u0921', u'name:baq_x': u'Hollywood', u'name:chi_x': u'\u597d\u83b1\u575e', u'name:deu_x': u'Hollywood', u'name:alb_x': u'Hollywood', u'name:bre_x': u'Hollywood', u'name:kir_x': u'\u0413\u043e\u043b\u043b\u0438\u0432\u0443\u0434', u'name:slv_x': u'Hollywood', u'name:gle_x': u'Hollywood', u'name:ces_x': u'Hollywood', u'name:glg_x': u'Hollywood', u'name:amh_x': u'\u1206\u120a\u12cd\u12f5', u'name:bur_x': u'\u101f\u1031\u102c\u101c\u102d\u101d\u102f\u1012\u103a', u'name:sgs_x': u'Huol\u0117vods'}))

        self.assert_has_feature(
            16, 11227, 26157, 'places',
            {'id': 85826037, 'kind': 'neighbourhood',
             'source': 'whosonfirst.org',
             'name': 'Hollywood',
             'name:ko': '\xed\x97\x90\xeb\xa6\xac\xec\x9a\xb0\xeb\x93\x9c'})

    def test_san_francisco_wof(self):
        # San Francisco (wof neighbourhood)
        self.generate_fixtures(dsl.way(85882641, wkt_loads('POINT (-98.190127 19.047508)'), {
                               u'name': u'San Francisco', u'max_zoom': 18.0, u'placetype': u'neighbourhood', u'source': u'whosonfirst.org', u'min_zoom': 13.0, u'name:spa_x': u'San Francisco'}))

        self.assert_has_feature(
            16, 14893, 29234, 'places',
            {'id': 85882641, 'kind': 'neighbourhood',
             'source': 'whosonfirst.org',
             'name': 'San Francisco',
             'name:es': 'San Francisco'})

    def test_san_francisco_osm(self):
        # San Francisco (osm city)
        #
        # note: presence of Chinese name tested, but not its value, as that
        # can and does change.
        self.generate_fixtures(dsl.way(26819236, wkt_loads('POINT (-122.419236226182 37.77928077351228)'), {u'name:pt': u'S\xe3o Francisco', u'name:ko': u'\uc0cc\ud504\ub780\uc2dc\uc2a4\ucf54', u'name:kn': u'\u0cb8\u0cbe\u0ca8\u0ccd \u0cab\u0ccd\u0cb0\u0cbe\u0ca8\u0ccd\u0cb8\u0cbf\u0cb8\u0ccd\u0c95\u0cca', u'rank': u'10', u'wikidata': u'Q62', u'name:ru': u'\u0421\u0430\u043d-\u0424\u0440\u0430\u043d\u0446\u0438\u0441\u043a\u043e', u'name:ta': u'\u0bb8\u0bbe\u0ba9\u0bcd \u0baa\u0bcd\xb2\u0bb0\u0bbe\u0ba9\u0bcd\u0bb8\u0bbf\u0bb8\u0bcd\u0b95\u0bca', u'name:fa': u'\u0633\u0627\u0646 \u0641\u0631\u0627\u0646\u0633\u06cc\u0633\u06a9\u0648',
                               u'is_in:country': u'United States', u'wikipedia': u'en:San Francisco', u'name:de': u'San Francisco', u'source': u'openstreetmap.org', u'name:zh': u'\u65e7\u91d1\u5c71', u'name:ja': u'\u30b5\u30f3\u30d5\u30e9\u30f3\u30b7\u30b9\u30b3', u'short_name': u'SF', u'name:hi': u'\u0938\u0948\u0928 \u092b\u094d\u0930\u093e\u0902\u0938\u093f\u0938\u094d\u0915\u094b', u'is_in:country_code': u'US', u'census:population': u'2010', u'population': u'864816', u'fixme': u'When zooming out, Oakland (a nearby city) label covers over the San Francisco label', u'name': u'San Francisco', u'place': u'city', u'is_in:continent': u'North America', u'name:eu': u'San Francisco'}))

        self.assert_has_feature(
            16, 10482, 25330, 'places',
            {'id': 26819236, 'kind': 'locality', 'kind_detail': 'city',
             'source': 'openstreetmap.org',
             'name': 'San Francisco',
             'name:zh-Hans': None,
             'name:zh': None})  # for backward compatible we still populate name:zh field

    def test_londonderry(self):
        # Node: Londonderry/Derry (267762522)
        self.generate_fixtures(dsl.way(267762522, wkt_loads('POINT (-7.31680089619325 54.99194206912099)'), {u'name:ga': u'Doire', u'name:sco': u'Lunnonderry', u'name': u'Londonderry/Derry', u'name:lt': u'Londonderis', u'name:ar': u'\u062f\u064a\u0631\u064a', u'wikipedia': u'en:Derry', u'source': u'openstreetmap.org', u'name:en_GB': u'Londonderry',
                               u'name:la': u'Derae', u'place': u'city', u'alt_name': u'Derry', u'name:uk': u'\u0414\u0435\u0440\u0440\u0456', u'loc_name': u'Stroke City', u'name:ru': u'\u0414\u0435\u0440\u0440\u0438', u'wikidata': u'Q163584', u'population': u'85016', u'name:sr': u'\u0414\u0435\u0440\u0438', u'name:en_IE': u'Derry'}))

        self.assert_has_feature(
            16, 31436, 20731, 'places',
            {'id': 267762522, 'name:en_GB': 'Londonderry'})

    def test_jerusalem(self):
        # Node: Jerusalem (29090735)
        #
        # note: presence of Chinese name tested, but not its value, as that
        # can and does change.
        self.generate_fixtures(dsl.way(29090735, wkt_loads('POINT (35.2266286169263 31.77911336167221)'), {u'name:cy': u'Jeriwsalem', u'name:ko': u'\uc608\ub8e8\uc0b4\ub818', u'name:cv': u'\u0418\u0435\u0440\u0443\u0441\u0430\u043b\u0438\u043c', u'name:cu': u'\u0407\u0454\u0440\u043e\u0443\u0441\u0430\u043b\u0438\u043c\u044a', u'name:cs': u'Jeruzal\xe9m', u'name:tt': u'\u0418\u0435\u0440\u0443\u0441\u0430\u043b\u0438\u043c', u'name:kv': u'\u0418\u0435\u0440\u0443\u0441\u0430\u043b\u0438\u043c', u'name:ku': u'Or\u015fel\xeem', u'name:tl': u'Herusalem', u'name:ta': u'\u0baf\u0bc6\u0bb0\u0bc2\u0b9a\u0bb2\u0bae\u0bcd', u'name:tg': u'\u0423\u0440\u0448\u0430\u043b\u0438\u043c', u'name:te': u'\u0c1c\u0c46\u0c30\u0c42\u0c38\u0c32\u0c47\u0c02', u'name:bat-smg': u'Jerozal\u0117', u'name:ka': u'\u10d8\u10d4\u10e0\u10e3\u10e1\u10d0\u10da\u10d8\u10db\u10d8', u'name:kab': u'Orcalim', u'name:kaa': u'Jerusalem', u'name:da': u'Jerusalem', u'name:mdf': u'\u0415\u0440\u0443\u0441\u0430\u043b\u0438\u043c', u'name:de': u'Jerusalem', u'name:tr': u'Kud\xfcs', u'name:kn': u'\u0c9c\u0cc6\u0cb0\u0cc1\u0cb8\u0cb2\u0cc6\u0c82', u'name:dv': u'\u07a4\u07aa\u078b\u07aa\u0790\u07b0', u'name:lv': u'Jeruz\u0101leme', u'name:lt': u'Jeruzal\u0117', u'name:uz': u'Quddus', u'name:kk': u'\u04d8\u043b-\u049a\u04b1\u0434\u044b\u0441', u'name:ur': u'\u0628\u06cc\u062a \u0627\u0644\u0645\u0642\u062f\u0633', u'name:dsb': u'Jeruzalem', u'name:la': u'Hierosolyma', u'name:uk': u'\u0404\u0440\u0443\u0441\u0430\u043b\u0438\u043c', u'name:ug': u'\u064a\u06d0\u0631\u06c7\u0633\u0627\u0644\u06d0\u0645', u'name:li': u'Jeruzalem', u'name:ln': u'Yerusal\xe9mi', u'name:hi': u'\u092f\u0930\u0941\u0936\u0932\u092e', u'name:el': u'\u0399\u03b5\u03c1\u03bf\u03c5\u03c3\u03b1\u03bb\u03ae\u03bc', u'name:eo': u'Jerusalemo', u'name:en': u'Jerusalem', u'name': u'\u05d9\u05e8\u05d5\u05e9\u05dc\u05d9\u05dd', u'name:tk': u'I\xfderusalim', u'name:th': u'\u0e40\u0e22\u0e23\u0e39\u0e0b\u0e32\u0e40\u0e25\u0e21', u'name:lij': u'Gerusalemme', u'is_in:continent': u'Asia', u'name:et': u'Jeruusalemm', u'name:es': u'Jerusal\xe9n', u'name:diq': u'Ur\u015felim', u'name:lez': u'\u0418\u0435\u0440\u0443\u0441\u0430\u043b\u0438\u043c', u'name:az': u'Jerusalem', u'name:id': u'Yerusalem', u'name:gan': u'\u8036\u8def\u6492\u51b7', u'name:nah': u'Ierusalem', u'name:ar': u'\u0627\u0644\u0642\u062f\u0633', u'name:io': u'Ierusalem', u'name:is': u'Jer\xfasalem', u'name:ckb': u'\u0626\u06c6\u0631\u0634\u06d5\u0644\u06cc\u0645', u'name:am': u'\u12a5\u12e8\u1229\u1233\u120c\u121d', u'name:it': u'Gerusalemme', u'name:an': u'Cherusalem', u'name:ru': u'\u0418\u0435\u0440\u0443\u0441\u0430\u043b\u0438\u043c', u'name:rw': u'Yerusalemu', u'wikipedia': u'en:Jerusalem', u'name:zh-min-nan': u'I\xe2-l\u014d\u0358-sat-l\xe9ng', u'name:nrm': u'J\xe9rusalem', u'capital': u'yes', u'name:zh-yue': u'\u8036\u8def\u6492\u51b7', u'name:zh': u'\u8036\u8def\u6492\u51b7', u'name:so': u'Qudus', u'name:sm': u'Ierusalema', u'name:sl': u'Jeruzalem', u'name:sk': u'Jeruzalem', u'name:ja': u'\u30a8\u30eb\u30b5\u30ec\u30e0', u'name:sh': u'Jeruzalem', u'name:sc': u'Gerusalemme', u'name:br': u'Jeruzalem', u'name:arc': u'\u0710\u0718\u072a\u072b\u0720\u0721', u'name:bn': u'\u099c\u09c7\u09b0\u09c1\u09b8\u09be\u09b2\u09c7\u09ae',
                               u'name:bo': u'\u0f47\u0f7a\u0f0b\u0f62\u0f74\u0f0b\u0f66\u0f0b\u0f63\u0f7a\u0f58\u0f0d', u'name:bjn': u'Baitul Maqdis', u'name:arz': u'\u0627\u0644\u0642\u062f\u0633', u'name:ilo': u'Herusalem', u'name:sw': u'Yerusalemu', u'name:sv': u'Jerusalem', u'name:su': u'Yerusalem', u'name:bg': u'\u0419\u0435\u0440\u0443\u0441\u0430\u043b\u0438\u043c', u'name:sr': u'\u0408\u0435\u0440\u0443\u0441\u0430\u043b\u0438\u043c', u'name:sq': u'Jeruzalemi', u'name:hsb': u'Jeruzalem', u'name:jv': u'Y\xe9rusalem', u'place': u'city', u'name:sah': u'\u0418\u0435\u0440\u0443\u0441\u0430\u043b\u0438\u043c', u'name:crh': u'Jerusalem', u'name:fj': u'Jerusalemi', u'name:pt': u'Jerusal\xe9m', u'name:ps': u'\u0628\u064a\u062a \u0627\u0644\u0645\u0642\u062f\u0633', u'name:tpi': u'Yerusalem', u'name:oc': u'Jerusal\xe8m', u'is_capital': u'country', u'alt_name': u'Jerkku', u'name:be': u'\u0406\u0435\u0440\u0443\u0441\u0430\u043b\u0456\u043c', u'name:os': u'\u0418\u0435\u0440\u0443\u0441\u0430\u043b\u0438\u043c', u'name:pl': u'Jerozolima', u'source': u'openstreetmap.org', u'name:hr': u'Jeruzalem', u'name:he1': u'\u05d9\u05b0\u05e8\u05d5\u05bc\u05e9\u05b8\u05c1\u05dc\u05b7\u05d9\u05b4\u05dd', u'name:mhr': u'\u0418\u0435\u0440\u0443\u0441\u0430\u043b\u0438\u043c', u'name:rue': u'\u0404\u0440\u0443\u0441\u0430\u043b\u0438\u043c', u'admin_level': u'2', u'name:csb': u'Jerozol\xebma', u'name:ro': u'Ierusalim', u'name:scn': u'Girusalemmi', u'name:pap': u'Herusalem', u'name:he': u'\u05d9\u05e8\u05d5\u05e9\u05dc\u05d9\u05dd', u'name:vep': u'Jerusalim', u'capital_ISO3166-1': u'yes', u'name:hy': u'\u0535\u0580\u0578\u0582\u057d\u0561\u0572\u0565\u0574', u'name:hu': u'Jeruzs\xe1lem', u'name:qu': u'Yerushalayim', u'name:vec': u'Hierusalem', u'population': u'780200', u'name:lmo': u'Ger\xfcsalem', u'alt_name:is': u'J\xf3rsalir;J\xf3rsalaborg', u'name:pnb': u'\u06cc\u0631\u0648\u0634\u0644\u0645', u'name:yi': u'\u05d9\u05e8\u05d5\u05e9\u05dc\u05d9\u05dd', u'name:be-tarask': u'\u0415\u0440\u0443\u0441\u0430\u043b\u0456\u043c', u'name:yo': u'Jer\xfas\xe1l\u1eb9\u0301m\xf9', u'capital_1': u'yes', u'name:fiu-vro': u'Jeruusalemm', u'name:ms': u'Baitulmuqaddis', u'name:mr': u'\u091c\u0947\u0930\u0941\u0938\u0932\u0947\u092e', u'name:my': u'\u1002\u103b\u1031\u101b\u102f\u1006\u101c\u1004\u103a\u1019\u103c\u102d\u102f\u1037', u'name:lad': u'Yerushalayim', u'wikidata': u'Q1218', u'name:vi': u'Jerusalem', u'name:ml': u'\u0d1c\u0d46\u0d31\u0d41\u0d38\u0d32\u0d47\u0d02', u'name:mn': u'\u0418\u0435\u0440\u0443\u0441\u0430\u043b\u0438\u043c', u'name:mk': u'\u0415\u0440\u0443\u0441\u0430\u043b\u0438\u043c', u'name:vo': u'Hierusalem', u'name:fa': u'\u0627\u0648\u0631\u0634\u0644\u06cc\u0645', u'name:ast': u'Xerusal\xe9n', u'is_in:country': u'Israel', u'name:fi': u'Jerusalem', u'name:ext': u'Jerusal\xe9n', u'name:mwl': u'Jarusalen', u'name:fo': u'Jer\xfasalem', u'alt_name:vi': u'Gi\xearusalem', u'name:fr': u'J\xe9rusalem', u'name:fy': u'Jeruzalim', u'name:hak': u'Y\xe2-lu-sat-l\xe2ng', u'int_name': u'Jerusalem', u'name:roa-tara': u'Gerusalemme', u'name:nl': u'Jeruzalem', u'name:zea': u'Jeruzalem', u'is_in:country_code': u'IL', u'name:wa': u'Djeruzalem', u'name:ang': u'Ierusalem', u'name:ga': u'Iar\xfasail\xe9im', u'name:gd': u'Ierusalem', u'name:gn': u'Herusal\u1ebd', u'name:gl': u'Xerusal\xe9n', u'name:ceb': u'Jerusalen'}))

        self.assert_has_feature(
            16, 39180, 26661, 'places',
            {'id': 29090735,
             'name:zh-min-nan': None,
             'name:zh-Hans': u'\u8036\u8def\u6492\u51b7',
             'name:zh': u'\u8036\u8def\u6492\u51b7',  # for backward compatible we still populate name:zh field
             })

        self.assert_no_matching_feature(
            16, 39180, 39180, 'places',
            {'id': 29090735,
             'name:zh-yue': None,
             })
