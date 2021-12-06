# -*- encoding: utf-8 -*-
import dsl
from shapely.wkt import loads as wkt_loads
from tilequeue.tile import deg2num

from . import FixtureTest


def _tile_centre(z, x, y):
    from tilequeue.tile import num2deg
    lat, lon = num2deg(x + 0.5, y + 0.5, z)
    return (lon, lat)


class ChineseNameTest(FixtureTest):

    def test_ne_san_francisco(self):
        lon, lat = (-122.417169, 37.769196)
        self.generate_fixtures(
            dsl.way(26819236, wkt_loads(
                'POINT (-122.417169 37.769196)'), {
                u'scalerank': 1,
                u'natscale': 300,
                u'labelrank': 1,
                u'featurecla': u'Populated place',
                u'name': u'San Francisco',
                u'namepar': u'',
                u'namealt': u'San Francisco-Oakland',
                u'nameascii': u'San Francisco',
                u'adm0cap': 0,
                u'worldcity': 1,
                u'megacity': 1,
                u'sov0name': u'United States',
                u'sov_a3': u'USA',
                u'adm0name': u'United States of America',
                u'adm0_a3': u'USA',
                u'adm1name': u'California',
                u'iso_a2': u'US',
                u'latitude': 37.769196,
                u'longitude': -122.417169,
                u'pop_max': 3450000,
                u'pop_min': 732072,
                u'pop_other': 27400,
                u'rank_max': 12,
                u'rank_min': 11,
                u'meganame': u'San Francisco-Oakland',
                u'ls_name': u'San Francisco1',
                u'max_pop10': 988636,
                u'max_pop20': 1130999,
                u'max_pop50': 1371285,
                u'max_pop300': 4561697,
                u'max_pop310': 4561697,
                u'max_natsca': 300,
                u'min_areakm': 218,
                u'max_areakm': 1748,
                u'min_areami': 84,
                u'max_areami': 675,
                u'min_perkm': 126,
                u'max_perkm': 755,
                u'min_permi': 78,
                u'max_permi': 469,
                u'min_bbxmin': -122.516667,
                u'max_bbxmin': -122.516667,
                u'min_bbxmax': -122.358333,
                u'max_bbxmax': -121.733333,
                u'min_bbymin': 37.191667,
                u'max_bbymin': 37.575,
                u'min_bbymax': 37.816667,
                u'max_bbymax': 38.041667,
                u'mean_bbxc': -122.301354,
                u'mean_bbyc': 37.622288,
                u'timezone': u'America\/Los_Angeles',
                u'un_fid': 570,
                u'pop1950': 1855,
                u'pop1955': 2021,
                u'pop1960': 2200,
                u'pop1965': 2361,
                u'pop1970': 2529,
                u'pop1975': 2590,
                u'pop1980': 2656,
                u'pop1985': 2805,
                u'pop1990': 2961,
                u'pop1995': 3095,
                u'pop2000': 3236,
                u'pop2005': 3387,
                u'pop2010': 3450,
                u'pop2015': 3544,
                u'pop2020': 3684,
                u'pop2025': 3803,
                u'pop2050': 3898,
                u'min_zoom': 2.7,
                u'wikidataid': u'Q62',
                u'wof_id': 85922583,
                u'capalt': 0,
                u'name_en': u'San Francisco',
                u'name_de': u'San Francisco',
                u'name_es': u'San Francisco',
                u'name_fr': u'San Francisco',
                u'name_pt': u'São Francisco',
                u'name_ru': u'Cан-франциско',
                u'name_zh': u'旧金山',
                u'name_ar': u'سان فرانسيسكو',
                u'name_bn': u'সান ফ্রান্সিস্কো',
                u'name_el': u'σαν φρανσίσκο',
                u'name_hi': u'सैन फ्रांसिस्को',
                u'name_hu': u'San Francisco',
                u'name_id': u'San Francisco',
                u'name_it': u'San Francisco',
                u'name_ja': u'サンフランシスコ',
                u'name_ko': u'샌프란시스코',
                u'name_nl': u'San Francisco',
                u'name_pl': u'San Francisco',
                u'name_sv': u'San Francisco',
                u'name_tr': u'San Francisco',
                u'name_vi': u'San Francisco',
                u'ne_id': 1159151479,
                u'name_fa': u'سان فرانسیسکو',
                u'name_he': u'סן פרנסיסקו',
                u'name_uk': u'Cан-франциско',
                u'name_ur': u'سان فرانسسکو',
                u'name_zht': u'舊金山',
                u'source': u'naturalearthdata.com',
            })
        )

        x, y = deg2num(lat, lon, 3)
        self.assert_has_feature(
            3, x, y, 'places', {
                'id': 26819236,
                'kind': 'locality',
                'name': 'San Francisco',
                'name:zh-Hans': u'旧金山',
                'name:zh': u'旧金山',  # for backward compatible we still populate name:zh field
                'name:zh-Hant': u'舊金山',
                'source': u'naturalearthdata.com',
            })

    def test_ne_san_francisco_no_zh(self):
        """ Test the case when there are no Chinese fields """
        lon, lat = (-122.417169, 37.769196)
        self.generate_fixtures(
            dsl.way(26819236, wkt_loads(
                'POINT (-122.417169 37.769196)'), {
                u'scalerank': 1,
                u'natscale': 300,
                u'labelrank': 1,
                u'featurecla': u'Populated place',
                u'name': u'San Francisco',
                u'namepar': u'',
                u'namealt': u'San Francisco-Oakland',
                u'nameascii': u'San Francisco',
                u'adm0cap': 0,
                u'worldcity': 1,
                u'megacity': 1,
                u'sov0name': u'United States',
                u'sov_a3': u'USA',
                u'adm0name': u'United States of America',
                u'adm0_a3': u'USA',
                u'adm1name': u'California',
                u'iso_a2': u'US',
                u'latitude': 37.769196,
                u'longitude': -122.417169,
                u'pop_max': 3450000,
                u'pop_min': 732072,
                u'pop_other': 27400,
                u'rank_max': 12,
                u'rank_min': 11,
                u'meganame': u'San Francisco-Oakland',
                u'ls_name': u'San Francisco1',
                u'max_pop10': 988636,
                u'max_pop20': 1130999,
                u'max_pop50': 1371285,
                u'max_pop300': 4561697,
                u'max_pop310': 4561697,
                u'max_natsca': 300,
                u'min_areakm': 218,
                u'max_areakm': 1748,
                u'min_areami': 84,
                u'max_areami': 675,
                u'min_perkm': 126,
                u'max_perkm': 755,
                u'min_permi': 78,
                u'max_permi': 469,
                u'min_bbxmin': -122.516667,
                u'max_bbxmin': -122.516667,
                u'min_bbxmax': -122.358333,
                u'max_bbxmax': -121.733333,
                u'min_bbymin': 37.191667,
                u'max_bbymin': 37.575,
                u'min_bbymax': 37.816667,
                u'max_bbymax': 38.041667,
                u'mean_bbxc': -122.301354,
                u'mean_bbyc': 37.622288,
                u'timezone': u'America\/Los_Angeles',
                u'un_fid': 570,
                u'pop1950': 1855,
                u'pop1955': 2021,
                u'pop1960': 2200,
                u'pop1965': 2361,
                u'pop1970': 2529,
                u'pop1975': 2590,
                u'pop1980': 2656,
                u'pop1985': 2805,
                u'pop1990': 2961,
                u'pop1995': 3095,
                u'pop2000': 3236,
                u'pop2005': 3387,
                u'pop2010': 3450,
                u'pop2015': 3544,
                u'pop2020': 3684,
                u'pop2025': 3803,
                u'pop2050': 3898,
                u'min_zoom': 2.7,
                u'wikidataid': u'Q62',
                u'wof_id': 85922583,
                u'capalt': 0,
                u'name_en': u'San Francisco',
                u'name_de': u'San Francisco',
                u'name_es': u'San Francisco',
                u'name_fr': u'San Francisco',
                u'name_pt': u'São Francisco',
                u'name_ru': u'Cан-франциско',
                u'name_ar': u'سان فرانسيسكو',
                u'name_bn': u'সান ফ্রান্সিস্কো',
                u'name_el': u'σαν φρανσίσκο',
                u'name_hi': u'सैन फ्रांसिस्को',
                u'name_hu': u'San Francisco',
                u'name_id': u'San Francisco',
                u'name_it': u'San Francisco',
                u'name_ja': u'サンフランシスコ',
                u'name_ko': u'샌프란시스코',
                u'name_nl': u'San Francisco',
                u'name_pl': u'San Francisco',
                u'name_sv': u'San Francisco',
                u'name_tr': u'San Francisco',
                u'name_vi': u'San Francisco',
                u'ne_id': 1159151479,
                u'name_fa': u'سان فرانسیسکو',
                u'name_he': u'סן פרנסיסקו',
                u'name_uk': u'Cан-франциско',
                u'name_ur': u'سان فرانسسکو',
                u'source': u'naturalearthdata.com',
            })
        )

        x, y = deg2num(lat, lon, 3)
        self.assert_has_feature(
            3, x, y, 'places', {
                'id': 26819236,
                'kind': 'locality',
                'name': 'San Francisco',
                'source': u'naturalearthdata.com',
            })

        for v in [None, u'', u' ', u'旧金山', u'舊金山']:
            self.assert_no_matching_feature(
                3, x, y, 'places', {
                    'id': 26819236,
                    'kind': 'locality',
                    'name': 'San Francisco',
                    'name:zh': v,
                    'source': u'naturalearthdata.com',
                })
            self.assert_no_matching_feature(
                3, x, y, 'places', {
                    'id': 26819236,
                    'kind': 'locality',
                    'name': 'San Francisco',
                    'name:zh-Hans': v,
                    'source': u'naturalearthdata.com',
                })
            self.assert_no_matching_feature(
                3, x, y, 'places', {
                    'id': 26819236,
                    'kind': 'locality',
                    'name': 'San Francisco',
                    'name:zh-Hant': v,
                    'source': u'naturalearthdata.com',
                })

    def test_united_states(self):
        # The low zoom test is borrowed from 977-low-zoom-from-ne-join
        lon, lat = (-100.4458825, 39.7837304)
        self.generate_fixtures(
            # https://www.openstreetmap.org/node/424317935
            dsl.point(424317935, (lon, lat), {
                u'alt_name': u'USA;US;The States;United States',
                u'alt_name:lfn': u'SUA',
                u'alt_name:sr': u'САД;Сједињене Државе',
                u'alt_name:vi': u'Hoa Kì;Mĩ;Hợp chúng quốc Hoa Kì',
                u'capital_city': u'Washington DC',
                u'country_code_fips': u'US',
                u'country_code_iso3166_1_alpha_2': u'US',
                u'int_name': u'United States of America',
                u'name': u'United States of America',
                u'name:ab': u'Америка Еиду Аштатқәа',
                u'name:rn': u'Leta Zunze Ubumwe za Amerika',
                u'name:ro': u'Statele Unite ale Americii',
                u'name:roa-tara': u"Statère Aunìte d'Americhe",
                u'name:ru': u'Соединённые Штаты Америки',
                u'name:rue': u'Споєны Штаты Америцькы',
                u'name:rw': u'Leta Zunze Ubumwe z’Amerika',
                u'name:sa': u'संयुक्तानि राज्यानि',
                u'name:sah': u'Америка Холбоһуктаах Штаттара',
                u'name:sc': u'Istados Unidos de America',
                u'name:scn': u'Stati Uniti',
                u'name:sco': u'Unitit States o Americae',
                u'name:sd': u'آمريڪا',
                u'name:se': u'Amerihká ovttastuvvan stáhtat',
                u'name:sg': u'ÂLeaa-Ôko tî Amerika',
                u'name:sh': u'Sjedinjene Američke Države',
                u'name:si': u"අ'මෙරිකා‍වේ එක්සත් රාජ්‍යයන",
                u'name:sk': u'Spojené štáty americké',
                u'name:sl': u'Združene države Amerike',
                u'name:sm': u'Iunaite Sitete o Amerika',
                u'name:smn': u'Amerik ovtâstumstaatah',
                u'name:sms': u'Ameriikk õhttõõvvâmvääʹld',
                u'name:sn': u'Amerika',
                u'name:so': u'Maraykanka',
                u'name:sq': u'Shtetet e Bashkuara të Amerikës',
                u'name:sr': u'Сједињене Америчке Државе',
                u'name:srn': u'Kondre Makandrameki',
                u'name:ss': u'IMelika',
                u'name:stq': u'Fereende Stoaten fon Amerikoa',
                u'name:su': u'Amérika Sarikat',
                u'name:sv': u'Förenta staterna',
                u'name:sw': u'Muungano wa Madola ya Amerika',
                u'name:szl': u'Zjednoczůne Sztaty Ameriki',
                u'name:ta': u'அமெரிக்க ஐக்கிய நாடு',
                u'name:te': u'అమెరికా సంయుక్త రాష్ట్రాలు',
                u'name:tet': u'Estadu Naklibur Sira Amérika Nian',
                u'name:tg': u'Штатҳои Муттаҳидаи Америка',
                u'name:th': u'สหรัฐอเมริกา',
                u'name:ti': u'አሜሪካ',
                u'name:tk': u'Amerikanyň Birleşen Ştatlary',
                u'name:tl': u'Estados Unidos ng Amerika',
                u'name:tn': u'USA',
                u'name:to': u"Puleʻanga Fakataha 'o 'Amelika",
                u'name:tok': u'ma Mewika',
                u'name:tpi': u'Yunaitet Stet bilong Amerika',
                u'name:tr': u'Amerika Birleşik Devletleri',
                u'name:ts': u'United States',
                u'name:tt': u'Америка Кушма Штатлары',
                u'name:tw': u'USA',
                u'name:ty': u'Fenua Marite',
                u'name:tzl': u"Estats Viensiçeschti d'America",
                u'name:udm': u'Америкалэн Огазеяськем Штатъёсыз',
                u'name:ug': u'ئامېرىكا قوشما شتاتلىرى',
                u'name:uk': u'Сполучені Штати Америки',
                u'name:ur': u'ریاستہائے متحدہ امریکہ',
                u'name:uz': u'Amerika Qoʻshma Shtatlari',
                u'name:vec': u'Stati Unìi de la Mèrica',
                u'name:vep': u'Amerikan Ühtenzoittud Valdkundad',
                u'name:vi': u'Hoa Kỳ',
                u'name:vls': u'Verênigde Stoaten van Amerika',
                u'name:vo': u'Lamerikän',
                u'name:wa': u"Estats Unis d' Amerike",
                u'name:war': u'Estados Unidos',
                u'name:wo': u'Diwaan-yu-Bennoo yu Aamerig',
                u'name:wuu': u'美利坚合众国',
                u'name:xal': u'Америкин Ниицәтә Орн Нутгуд',
                u'name:xh': u'IYunayithedi Steyitsi',
                u'name:xmf': u'ამერიკაშ აკოართაფილი შტატეფი',
                u'name:yi': u'פאראייניקטע שטאטן פון אמעריקע',
                u'name:yo': u'Orílẹ́ède Orilẹede Amerika',
                u'name:yue': u'即美利堅合眾國',
                u'name:za': u'Meijgoz',
                u'name:zea': u'Vereênigde Staeten',
                u'name:zh': u'美國',
                u'name:zh_pinyin': u'Měiguó',
                u'name:zu': u'i-United States',
                u'not:official_name:vi': u'Hợp chủng quốc Hoa Kỳ',
                u'official_name': u'United States of America',
                u'official_name:en': u'United States of America',
                u'official_name:eo': u'Unuiĝintaj Ŝtatoj de Ameriko',
                u'official_name:fr': u"États-Unis d'Amérique",
                u'official_name:pl': u'Stany Zjednoczone Ameryki',
                u'official_name:pt': u'Estados Unidos da América',
                u'official_name:sv': u'Amerikas förenta stater',
                u'official_name:vi': u'Hợp chúng quốc Hoa Kỳ',
                u'official_name:vo': u'Tats-Pebalöl Nolüda-Meropa',
                u'old_name:vi': u'Mỹ Lợi Kiên;Ma Ly Căn;Nhã Di Lý',
                u'place': u'country',
                u'population': u'324720797',
                u'short_name': u'USA',
                u'short_name:en': u'USA',
                u'short_name:es': u'EE.UU.',
                u'short_name:vi': u'Mỹ',
                u'source': u'openstreetmap.org',
                u'sqkm': u'9826675',
                u'wikidata': u'Q30',
                u'wikipedia': u'en:United States',
                '__ne_min_zoom': 1.7,
                '__ne_max_zoom': 6.7,
            }),
        )
        # should show up in zooms within the range 2-6
        for zoom in xrange(2, 6):
            x, y = deg2num(lat, lon, zoom)
            self.assert_has_feature(
                zoom, x, y, 'places', {
                    'id': 424317935,
                    'kind': 'country',
                    'name': 'United States of America',
                    'min_zoom': 2.0,
                    'max_zoom': 6.7,
                    'name:zh-Hans': u'美國',
                    'name:zh': u'美國',  # for backward compatible we still populate name:zh field
                    'name:zh-Hant': u'美國'
                })
            self.assert_no_matching_feature(
                zoom, x, y, 'places',
                {'name:zh-Hans': u'Měiguó',
                 'name:zh-Hant': u'Měiguó',
                 'name:zh-default': u'Měiguó',
                 })

    def test_united_states_no_zh(self):
        """ Test the case when no zh fields in the source """
        # The low zoom test is borrowed from 977-low-zoom-from-ne-join
        lon, lat = (-100.4458825, 39.7837304)
        self.generate_fixtures(
            # https://www.openstreetmap.org/node/424317935
            dsl.point(424317935, (lon, lat), {
                u'alt_name': u'USA;US;The States;United States',
                u'alt_name:lfn': u'SUA',
                u'alt_name:sr': u'САД;Сједињене Државе',
                u'alt_name:vi': u'Hoa Kì;Mĩ;Hợp chúng quốc Hoa Kì',
                u'capital_city': u'Washington DC',
                u'country_code_fips': u'US',
                u'country_code_iso3166_1_alpha_2': u'US',
                u'int_name': u'United States of America',
                u'name': u'United States of America',
                u'name:ab': u'Америка Еиду Аштатқәа',
                u'name:rn': u'Leta Zunze Ubumwe za Amerika',
                u'name:ro': u'Statele Unite ale Americii',
                u'name:roa-tara': u"Statère Aunìte d'Americhe",
                u'name:ru': u'Соединённые Штаты Америки',
                u'name:rue': u'Споєны Штаты Америцькы',
                u'name:rw': u'Leta Zunze Ubumwe z’Amerika',
                u'name:sa': u'संयुक्तानि राज्यानि',
                u'name:sah': u'Америка Холбоһуктаах Штаттара',
                u'name:sc': u'Istados Unidos de America',
                u'name:scn': u'Stati Uniti',
                u'name:sco': u'Unitit States o Americae',
                u'name:sd': u'آمريڪا',
                u'name:se': u'Amerihká ovttastuvvan stáhtat',
                u'name:sg': u'ÂLeaa-Ôko tî Amerika',
                u'name:sh': u'Sjedinjene Američke Države',
                u'name:si': u"අ'මෙරිකා‍වේ එක්සත් රාජ්‍යයන",
                u'name:sk': u'Spojené štáty americké',
                u'name:sl': u'Združene države Amerike',
                u'name:sm': u'Iunaite Sitete o Amerika',
                u'name:smn': u'Amerik ovtâstumstaatah',
                u'name:sms': u'Ameriikk õhttõõvvâmvääʹld',
                u'name:sn': u'Amerika',
                u'name:so': u'Maraykanka',
                u'name:sq': u'Shtetet e Bashkuara të Amerikës',
                u'name:sr': u'Сједињене Америчке Државе',
                u'name:srn': u'Kondre Makandrameki',
                u'name:ss': u'IMelika',
                u'name:stq': u'Fereende Stoaten fon Amerikoa',
                u'name:su': u'Amérika Sarikat',
                u'name:sv': u'Förenta staterna',
                u'name:sw': u'Muungano wa Madola ya Amerika',
                u'name:szl': u'Zjednoczůne Sztaty Ameriki',
                u'name:ta': u'அமெரிக்க ஐக்கிய நாடு',
                u'name:te': u'అమెరికా సంయుక్త రాష్ట్రాలు',
                u'name:tet': u'Estadu Naklibur Sira Amérika Nian',
                u'name:tg': u'Штатҳои Муттаҳидаи Америка',
                u'name:th': u'สหรัฐอเมริกา',
                u'name:ti': u'አሜሪካ',
                u'name:tk': u'Amerikanyň Birleşen Ştatlary',
                u'name:tl': u'Estados Unidos ng Amerika',
                u'name:tn': u'USA',
                u'name:to': u"Puleʻanga Fakataha 'o 'Amelika",
                u'name:tok': u'ma Mewika',
                u'name:tpi': u'Yunaitet Stet bilong Amerika',
                u'name:tr': u'Amerika Birleşik Devletleri',
                u'name:ts': u'United States',
                u'name:tt': u'Америка Кушма Штатлары',
                u'name:tw': u'USA',
                u'name:ty': u'Fenua Marite',
                u'name:tzl': u"Estats Viensiçeschti d'America",
                u'name:udm': u'Америкалэн Огазеяськем Штатъёсыз',
                u'name:ug': u'ئامېرىكا قوشما شتاتلىرى',
                u'name:uk': u'Сполучені Штати Америки',
                u'name:ur': u'ریاستہائے متحدہ امریکہ',
                u'name:uz': u'Amerika Qoʻshma Shtatlari',
                u'name:vec': u'Stati Unìi de la Mèrica',
                u'name:vep': u'Amerikan Ühtenzoittud Valdkundad',
                u'name:vi': u'Hoa Kỳ',
                u'name:vls': u'Verênigde Stoaten van Amerika',
                u'name:vo': u'Lamerikän',
                u'name:wa': u"Estats Unis d' Amerike",
                u'name:war': u'Estados Unidos',
                u'name:wo': u'Diwaan-yu-Bennoo yu Aamerig',
                u'name:wuu': u'美利坚合众国',
                u'name:xal': u'Америкин Ниицәтә Орн Нутгуд',
                u'name:xh': u'IYunayithedi Steyitsi',
                u'name:xmf': u'ამერიკაშ აკოართაფილი შტატეფი',
                u'name:yi': u'פאראייניקטע שטאטן פון אמעריקע',
                u'name:yo': u'Orílẹ́ède Orilẹede Amerika',
                u'name:za': u'Meijgoz',
                u'name:zea': u'Vereênigde Staeten',
                u'name:zh_pinyin': u'Měiguó',
                u'name:zu': u'i-United States',
                u'not:official_name:vi': u'Hợp chủng quốc Hoa Kỳ',
                u'official_name': u'United States of America',
                u'official_name:en': u'United States of America',
                u'official_name:eo': u'Unuiĝintaj Ŝtatoj de Ameriko',
                u'official_name:fr': u"États-Unis d'Amérique",
                u'official_name:pl': u'Stany Zjednoczone Ameryki',
                u'official_name:pt': u'Estados Unidos da América',
                u'official_name:sv': u'Amerikas förenta stater',
                u'official_name:vi': u'Hợp chúng quốc Hoa Kỳ',
                u'official_name:vo': u'Tats-Pebalöl Nolüda-Meropa',
                u'old_name:vi': u'Mỹ Lợi Kiên;Ma Ly Căn;Nhã Di Lý',
                u'place': u'country',
                u'population': u'324720797',
                u'short_name': u'USA',
                u'short_name:en': u'USA',
                u'short_name:es': u'EE.UU.',
                u'short_name:vi': u'Mỹ',
                u'source': u'openstreetmap.org',
                u'sqkm': u'9826675',
                u'wikidata': u'Q30',
                u'wikipedia': u'en:United States',
                '__ne_min_zoom': 1.7,
                '__ne_max_zoom': 6.7,
            }),
        )
        # should show up in zooms within the range 2-6
        for zoom in xrange(2, 6):
            x, y = deg2num(lat, lon, zoom)
            self.assert_has_feature(
                zoom, x, y, 'places', {
                    'id': 424317935,
                    'kind': 'country',
                    'name': 'United States of America',
                    'min_zoom': 2.0,
                    'max_zoom': 6.7,
                })
            for v in [None, u'', u' ', u'美國', u'美国', u'Měiguó']:
                self.assert_no_matching_feature(
                    zoom, x, y, 'places',
                    {'name:zh': v,
                     })
                self.assert_no_matching_feature(
                    zoom, x, y, 'places',
                    {
                        'name:zht': v,
                    })
                self.assert_no_matching_feature(
                    zoom, x, y, 'places',
                    {
                        'name:zh-default': v,
                    })

    def test_san_francisco_osm(self):
        # San Francisco (osm city)
        self.generate_fixtures(dsl.way(26819236, wkt_loads(
            'POINT (-122.419236226182 37.77928077351228)'),
            {u'name:pt': u'S\xe3o Francisco',
             u'name:ko':
             u'\uc0cc\ud504\ub780\uc2dc\uc2a4\ucf54',
             u'name:kn':
             u'\u0cb8\u0cbe\u0ca8\u0ccd '
             u'\u0cab\u0ccd\u0cb0\u0cbe\u0ca8\u0ccd\u0cb8\u0cbf\u0cb8\u0ccd\u0c95\u0cca',
             u'rank': u'10',
             u'wikidata': u'Q62',
             u'name:ru':
             u'\u0421\u0430\u043d-\u0424\u0440\u0430\u043d\u0446\u0438\u0441\u043a\u043e',
             u'name:ta':
             u'\u0bb8\u0bbe\u0ba9\u0bcd '
             u'\u0baa\u0bcd\xb2\u0bb0\u0bbe\u0ba9\u0bcd\u0bb8\u0bbf\u0bb8\u0bcd\u0b95\u0bca',
             u'name:fa': u'\u0633\u0627\u0646 '
             u'\u0641\u0631\u0627\u0646\u0633\u06cc\u0633\u06a9\u0648',
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
             u'\u30b5\u30f3\u30d5\u30e9\u30f3\u30b7\u30b9\u30b3',
             u'short_name': u'SF',
             u'name:hi': u'\u0938\u0948\u0928 '
             u'\u092b\u094d\u0930\u093e\u0902\u0938\u093f\u0938\u094d\u0915\u094b',
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
             u'name:eu': u'San Francisco'}))

        self.assert_has_feature(
            16, 10482, 25330, 'places',
            {'id': 26819236, 'kind': 'locality', 'kind_detail': 'city',
             'source': 'openstreetmap.org',
             'name': 'San Francisco',
             'name:zh-Hans': u'旧金山',
             'name:zh': u'旧金山',  # for backward compatible we still populate name:zh field
             'name:zh-Hant': u'舊金山'})

        self.assert_no_matching_feature(
            16, 10482, 25330, 'places',
            {'name:zh-default': u'旧金山/三藩市/舊金山'})

    def test_san_francisco_osm_no_zh(self):
        """ test the case when there is no zh fields """
        # San Francisco (osm city)
        self.generate_fixtures(dsl.way(26819236, wkt_loads(
            'POINT (-122.419236226182 37.77928077351228)'),
            {u'name:pt': u'S\xe3o Francisco',
             u'name:ko':
             u'\uc0cc\ud504\ub780\uc2dc\uc2a4\ucf54',
             u'name:kn':
             u'\u0cb8\u0cbe\u0ca8\u0ccd '
             u'\u0cab\u0ccd\u0cb0\u0cbe\u0ca8\u0ccd\u0cb8\u0cbf\u0cb8\u0ccd\u0c95\u0cca',
             u'rank': u'10',
             u'wikidata': u'Q62',
             u'name:ru':
             u'\u0421\u0430\u043d-\u0424\u0440\u0430\u043d\u0446\u0438\u0441\u043a\u043e',
             u'name:ta':
             u'\u0bb8\u0bbe\u0ba9\u0bcd '
             u'\u0baa\u0bcd\xb2\u0bb0\u0bbe\u0ba9\u0bcd\u0bb8\u0bbf\u0bb8\u0bcd\u0b95\u0bca',
             u'name:fa': u'\u0633\u0627\u0646 '
             u'\u0641\u0631\u0627\u0646\u0633\u06cc\u0633\u06a9\u0648',
             u'is_in:country': u'United States',
             u'wikipedia': u'en:San Francisco',
             u'name:de': u'San Francisco',
             u'source': u'openstreetmap.org',
             u'name:ja':
             u'\u30b5\u30f3\u30d5\u30e9\u30f3\u30b7\u30b9\u30b3',
             u'short_name': u'SF',
             u'name:hi': u'\u0938\u0948\u0928 '
             u'\u092b\u094d\u0930\u093e\u0902\u0938\u093f\u0938\u094d\u0915\u094b',
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
             u'name:eu': u'San Francisco'}))

        self.assert_has_feature(
            16, 10482, 25330, 'places',
            {'id': 26819236, 'kind': 'locality', 'kind_detail': 'city',
             'source': 'openstreetmap.org',
             'name': 'San Francisco'
             })

        for v in [None, u'', u' ', u'旧金山/三藩市/舊金山', u'旧金山', u'舊金山']:
            self.assert_no_matching_feature(
                16, 10482, 25330, 'places',
                {
                    'name:zh': v,
                })
            self.assert_no_matching_feature(
                16, 10482, 25330, 'places',
                {
                    'name:zh-Hans': v,
                })
            self.assert_no_matching_feature(
                16, 10482, 25330, 'places',
                {
                    'name:zh-Hant': v,
                })
            self.assert_no_matching_feature(
                16, 10482, 25330, 'places',
                {'name:zh-default': v,
                 })

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
                     u'name:sgs_x': u'Huol\u0117vods'}))

        self.assert_has_feature(
            16, 11227, 26157, 'places',
            {'id': 85826037, 'kind': 'neighbourhood',
             'source': 'whosonfirst.org',
             'name': 'Hollywood',
             'name:zh-Hans': u'好莱坞',
             'name:zh': u'好莱坞',  # for backward compatible we still populate name:zh field
             'name:zh-Hant': u'好萊塢'})

    def test_hollywood_wof_no_zh(self):
        """ Test the case when no zh fields in the source """
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
                     u'name:sgs_x': u'Huol\u0117vods'}))

        self.assert_has_feature(
            16, 11227, 26157, 'places',
            {'id': 85826037, 'kind': 'neighbourhood',
             'source': 'whosonfirst.org',
             'name': 'Hollywood'
             })

        for v in [None, u'', u' ', u'好莱坞', u'好萊塢']:
            self.assert_no_matching_feature(
                16, 11227, 26157, 'places',
                {'id': 85826037, 'kind': 'neighbourhood',
                 'source': 'whosonfirst.org',
                 'name': 'Hollywood',
                 'name:zh-Hans': v
                 })
            self.assert_no_matching_feature(
                16, 11227, 26157, 'places',
                {'id': 85826037, 'kind': 'neighbourhood',
                 'source': 'whosonfirst.org',
                 'name': 'Hollywood',
                 'name:zh': v
                 })
            self.assert_no_matching_feature(
                16, 11227, 26157, 'places',
                {'id': 85826037, 'kind': 'neighbourhood',
                 'source': 'whosonfirst.org',
                 'name': 'Hollywood',
                 'name:zh-Hant': v})
