# -*- encoding: utf-8 -*-
import dsl
from shapely.wkt import loads as wkt_loads

from . import FixtureTest


class LocalityChangesPlacesNe(FixtureTest):

    def setUp(self):
        super(LocalityChangesPlacesNe, self).setUp()
        self.generate_fixtures(dsl.way(1, wkt_loads('POINT (-64.04687560264087 -64.7624133527419)'), {u'labelrank': 0, u'max_bbymin': 0.0, u'max_bbymax': 0.0, u'namediff': 0, u'max_areami': 0.0, u'pop1960': 0.0, u'pop1965': 0.0, u'min_perkm': 0.0, u'max_pop50': 0.0, u'source': u'naturalearthdata.com', u'latitude': -64.7624133527, u'elevation': 0.0, u'diffnote': u'Changed feature class.', u'min_areakm': 0.0, u'namealt': u'', u'rank_min': 1, u'sov0name': u'Indeterminate', u'cityalt': u'', u'name': u'Palmer Station', u'pop1995': 0.0, u'max_natsca': 0.0, u'pop1990': 0.0, u'max_pop20': 0.0, u'min_bbxmin': 0.0, u'adm0cap': 0.0, u'max_areakm': 0.0, u'natscale': 20, u'pop2010': 0.0, u'pop2015': 0.0, u'pop1985': 0.0, u'pop1980': 0.0, u'sov_a3': u'ATA', u'un_adm0': u'', u'ls_match': 0, u'namepar': u'USA', u'min_areami': 0.0, u'adm0name': u'Antarctica', u'un_lat': 0.0, u'min_permi': 0.0, u'pop2000': 0.0, u'pop2005': 0.0, u'changed': 4.0, u'nameascii': u'Palmer Station', u'geonamesno': u'No GeoNames match due to small population, not in GeoNames, or poor NEV placement.', u'meganame': u'', u'scalerank': 7, u'ls_name': u'Palmer Station (USA)', u'gtopo30': 0.0, u'mean_bbyc': 0.0, u'iso_a2': u'AQ', u'max_permi': 0.0, u'feature_co': u'', u'feature_cl': u'', u'rank_max': 1, u'geonameid': -1.0, u'diffascii': 0, u'max_pop10': 0.0, u'min_bbymin': 0.0, u'pop_max': 46, u'min_bbymax': 0.0, u'capalt': 0.0, u'mean_bbxc': 0.0, u'checkme': 3, u'megacity': 0, u'capin': u'', u'pop_min': 15, u'pop2020': 0.0, u'longitude': -64.0468756026, u'pop2025': 0.0, u'min_bbxmax': 0.0, u'adm1name': u'', u'pop1950': 0.0, u'pop1955': 0.0, u'max_pop310': 0.0, u'compare': 0, u'max_perkm': 0.0, u'admin1_cod': 0.0, u'adm0_a3': u'ATA', u'timezone': u'', u'note': u'', u'pop2050': 0.0, u'worldcity': 0.0, u'un_long': 0.0, u'max_pop300': 0.0, u'max_bbxmin': 0.0, u'featurecla': u'Scientific station', u'pop1975': 0.0, u'gn_ascii': u'', u'pop1970': 0.0, u'max_bbxmax': 0.0, u'un_fid': 0, u'pop_other': 0, u'gn_pop': 0.0}), dsl.way(2, wkt_loads('POINT (-122.4171687735523 37.76919562968742)'), {u'labelrank': 1, u'max_bbymin': 37.575, u'max_bbymax': 38.04166667, u'namediff': 0, u'max_areami': 675.0, u'pop1960': 2200.0, u'pop1965': 2361.0, u'min_perkm': 126.0, u'max_pop50': 1371285.0, u'source': u'naturalearthdata.com', u'latitude': 37.7400077505, u'elevation': 16.0, u'diffnote': u'', u'min_areakm': 218.0, u'namealt': u'San Francisco-Oakland', u'rank_min': 11, u'sov0name': u'United States', u'cityalt': u'San Francisco', u'name': u'San Francisco', u'pop1995': 3095.0, u'max_natsca': 300.0, u'pop1990': 2961.0, u'max_pop20': 1130999.0, u'min_bbxmin': -122.51666667, u'adm0cap': 0.0, u'max_areakm': 1748.0, u'natscale': 300, u'pop2010': 3450.0, u'pop2015': 3544.0, u'pop1985': 2805.0, u'pop1980': 2656.0, u'sov_a3': u'USA', u'un_adm0': u'United States of America', u'ls_match': 1, u'namepar': u'', u'min_areami': 84.0, u'adm0name': u'United States of America', u'un_lat': 37.79, u'min_permi': 78.0, u'pop2000': 3236.0, u'pop2005': 3387.0, u'changed': 0.0, u'nameascii': u'San Francisco', u'geonamesno': u'GeoNames match with ascii name + lat + long whole numbers.', u'meganame': u'San Francisco-Oakland', u'scalerank': 1, u'ls_name': u'San Francisco1', u'gtopo30': 60.0, u'mean_bbyc': 37.62228831, u'iso_a2': u'US', u'max_permi': 469.0, u'feature_co': u'PPL', u'feature_cl': u'P', u'rank_max': 12, u'geonameid': 5391959.0, u'diffascii': 0, u'max_pop10': 988636.0, u'min_bbymin': 37.19166667, u'pop_max': 3450000, u'min_bbymax': 37.81666667, u'capalt': 0.0, u'mean_bbxc': -122.301354098, u'checkme': 0, u'megacity': 1, u'capin': u'', u'pop_min': 732072, u'pop2020': 3684.0, u'longitude': -122.459977663, u'pop2025': 3803.0, u'min_bbxmax': -122.35833333, u'adm1name': u'California', u'pop1950': 1855.0, u'pop1955': 2021.0, u'max_pop310': 4561697.0, u'compare': 0, u'max_perkm': 755.0, u'admin1_cod': 0.0, u'adm0_a3': u'USA', u'timezone': u'America/Los_Angeles', u'note': u'', u'pop2050': 3898.0, u'worldcity': 1.0, u'un_long': -122.38, u'max_pop300': 4561697.0, u'max_bbxmin': -122.51666667, u'featurecla': u'Populated place', u'pop1975': 2590.0, u'gn_ascii': u'San Francisco', u'pop1970': 2529.0, u'max_bbxmax': -121.73333333, u'un_fid': 570, u'pop_other': 27400, u'gn_pop': 732072.0}), dsl.way(
            3, wkt_loads('POINT (126.997785138202 37.56829495838893)'), {u'labelrank': 3, u'max_bbymin': 37.41202199, u'max_bbymax': 37.875, u'namediff': 0, u'max_areami': 1049.0, u'pop1960': 2361.0, u'pop1965': 3452.0, u'min_perkm': 546.0, u'max_pop50': 21387676.0, u'source': u'naturalearthdata.com', u'latitude': 37.5663490998, u'elevation': 0.0, u'diffnote': u'', u'min_areakm': 971.0, u'namealt': u'', u'rank_min': 13, u'sov0name': u'Korea, South', u'cityalt': u'', u'name': u'Seoul', u'pop1995': 10256.0, u'max_natsca': 300.0, u'pop1990': 10544.0, u'max_pop20': 13143622.0, u'min_bbxmin': 126.55, u'adm0cap': 1.0, u'max_areakm': 2718.0, u'natscale': 300, u'pop2010': 9796.0, u'pop2015': 9762.0, u'pop1985': 9547.0, u'pop1980': 8258.0, u'sov_a3': u'KOR', u'un_adm0': u'Republic of Korea', u'ls_match': 1, u'namepar': u'', u'min_areami': 375.0, u'adm0name': u'South Korea', u'un_lat': 37.54, u'min_permi': 340.0, u'pop2000': 9917.0, u'pop2005': 9825.0, u'changed': 0.0, u'nameascii': u'Seoul', u'geonamesno': u'GeoNames match general.', u'meganame': u'Seoul', u'scalerank': 1, u'ls_name': u'Seoul', u'gtopo30': 46.0, u'mean_bbyc': 37.485925482, u'iso_a2': u'KR', u'max_permi': 1181.0, u'feature_co': u'PPLC', u'feature_cl': u'P', u'rank_max': 13, u'geonameid': 1835848.0, u'diffascii': 0, u'max_pop10': 12322855.0, u'min_bbymin': 36.75, u'pop_max': 9796000, u'min_bbymax': 37.79166667, u'capalt': 0.0, u'mean_bbxc': 126.971294558, u'checkme': 0, u'megacity': 1, u'capin': u'', u'pop_min': 9796000, u'pop2020': 9740.0, u'longitude': 126.999730997, u'pop2025': 9738.0, u'min_bbxmax': 127.26666667, u'adm1name': u'Seoul', u'pop1950': 1021.0, u'pop1955': 1553.0, u'max_pop310': 21991959.0, u'compare': 0, u'max_perkm': 1901.0, u'admin1_cod': 11.0, u'adm0_a3': u'KOR', u'timezone': u'Asia/Seoul', u'note': u'', u'pop2050': 9738.0, u'worldcity': 1.0, u'un_long': 126.93, u'max_pop300': 21991959.0, u'max_bbxmin': 126.76718461, u'featurecla': u'Admin-0 capital', u'pop1975': 6808.0, u'gn_ascii': u'Seoul', u'pop1970': 5312.0, u'max_bbxmax': 127.325, u'un_fid': 336, u'pop_other': 12018058, u'gn_pop': 10349312.0}), dsl.way(4, wkt_loads('POINT (151.1832339501475 -33.91806510862875)'), {u'labelrank': 3, u'max_bbymin': -34.09166667, u'max_bbymax': -33.6, u'namediff': 0, u'max_areami': 544.0, u'pop1960': 2135.0, u'pop1965': 2390.0, u'min_perkm': 468.0, u'max_pop50': 3164008.0, u'source': u'naturalearthdata.com', u'latitude': -33.9200109672, u'elevation': 0.0, u'diffnote': u'Changed feature class.', u'min_areakm': 1078.0, u'namealt': u'', u'rank_min': 12, u'sov0name': u'Australia', u'cityalt': u'', u'name': u'Sydney', u'pop1995': 3839.0, u'max_natsca': 300.0, u'pop1990': 3632.0, u'max_pop20': 2731457.0, u'min_bbxmin': 150.53333333, u'adm0cap': 0.0, u'max_areakm': 1409.0, u'natscale': 600, u'pop2010': 4327.0, u'pop2015': 4427.0, u'pop1985': 3432.0, u'pop1980': 3227.0, u'sov_a3': u'AUS', u'un_adm0': u'Australia', u'ls_match': 1, u'namepar': u'', u'min_areami': 416.0, u'adm0name': u'Australia', u'un_lat': -33.88, u'min_permi': 291.0, u'pop2000': 4078.0, u'pop2005': 4260.0, u'changed': 4.0, u'nameascii': u'Sydney', u'geonamesno': u'GeoNames rough area, rough name, requires further research.', u'meganame': u'Sydney', u'scalerank': 0, u'ls_name': u'Sydney1', u'gtopo30': 0.0, u'mean_bbyc': -33.846723594, u'iso_a2': u'AU', u'max_permi': 445.0, u'feature_co': u'', u'feature_cl': u'', u'rank_max': 12, u'geonameid': 2147714.0, u'diffascii': 0, u'max_pop10': 2731457.0, u'min_bbymin': -34.09166667, u'pop_max': 4630000, u'min_bbymax': -33.64166667, u'capalt': 0.0, u'mean_bbxc': 151.051024066, u'checkme': 0, u'megacity': 1, u'capin': u'', u'pop_min': 3641422, u'pop2020': 4582.0, u'longitude': 151.185179809, u'pop2025': 4716.0, u'min_bbxmax': 151.30833333, u'adm1name': u'New South Wales', u'pop1950': 1690.0, u'pop1955': 1906.0, u'max_pop310': 3164008.0, u'compare': 0, u'max_perkm': 717.0, u'admin1_cod': 0.0, u'adm0_a3': u'AUS', u'timezone': u'', u'note': u'', u'pop2050': 4826.0, u'worldcity': 1.0, u'un_long': 151.02, u'max_pop300': 3164008.0, u'max_bbxmin': 150.83196335, u'featurecla': u'Admin-1 capital', u'pop1975': 2960.0, u'gn_ascii': u'', u'pop1970': 2667.0, u'max_bbxmax': 151.34166667, u'un_fid': 276, u'pop_other': 2669348, u'gn_pop': 4394576.0}))

    def test_admin0_capital(self):
        # ne Admin-0 capital
        self.assert_has_feature(
            3, 6, 3, 'places',
            {'kind': 'locality', 'name': 'Seoul', 'country_capital': True})

        self.assert_no_matching_feature(
            3, 6, 3, 'places',
            {'kind': 'city', 'name': 'Seoul', 'country_capital': True})

    def test_admin1_capital(self):
        # ne Admin-1 capital
        self.assert_has_feature(
            3, 7, 4, 'places',
            {'kind': 'locality', 'name': 'Sydney', 'region_capital': True})

        self.assert_no_matching_feature(
            3, 7, 4, 'places',
            {'kind': 'city', 'name': 'Sydney', 'state_capital': True})

    def test_populated_place(self):
        # ne Populated place
        self.assert_has_feature(
            3, 1, 3, 'places',
            {'kind': 'locality', 'name': 'San Francisco'})

        self.assert_no_matching_feature(
            3, 1, 3, 'places',
            {'kind': 'city', 'name': 'San Francisco'})

    def test_scientific_station(self):
        # ne Scientific station
        self.assert_has_feature(
            9, 164, 377, 'places',
            {'kind': 'locality', 'name': 'Palmer Station',
             'kind_detail': 'scientific_station'})


class LocalityChangesPlacesOsm(FixtureTest):
    def test_no_region_capital_false(self):
        # Washington (158368533)
        # no region_capital false
        self.generate_fixtures(dsl.way(158368533, wkt_loads('POINT (-77.0366455046539 38.89495487587219)'), {u'name:ty': u'Washington', u'name:ka': u'\u10d5\u10d0\u10e8\u10d8\u10dc\u10d2\u10e2\u10dd\u10dc\u10d8', u'name:ko': u'\uc6cc\uc2f1\ud134', u'name:cv': u'\u0412\u0430\u0448\u0438\u043d\u0433\u0442\u043e\u043d', u'old_name': u'District of Columbia', u'name:kk': u'\u0412\u0430\u0448\u0438\u043d\u0433\u0442\u043e\u043d', u'name:tw': u'Washington, D. C.', u'name:tt': u'\u0412\u0430\u0448\u0438\u043d\u0433\u0442\u043e\u043d', u'name:co': u'Washington DC', u'name:tk': u'Wa\u015fington', u'name:ku': u'Washington', u'name:pdc': u'Washington D.C.', u'name:ce': u'\u0412\u0430\u0448\u0438\u043d\u0433\u0442\u043e\u043d', u'gnis:id': u'531871', u'name:tg': u'\u0412\u0430\u0448\u0438\u043d\u0433\u0442\u043e\u043d \u04b2\u0430\u0432\u0437\u0430\u0438 \u041a\u043e\u043b\u0443\u043c\u0431\u0438\u044f', u'name:ca': u'Washington DC', u'name:te': u'\u0c35\u0c3e\u0c37\u0c3f\u0c02\u0c17\u0c4d\u0c1f\u0c28\u0c4d, \u0c21\u0c3f.\u0c38\u0c3f.', u'name:bat-smg': u'Va\u0161ingtuons', u'alt_name_1': u'Washington, D.C.', u'name:frp': u'Washington', u'name:da': u'Washington D.C.', u'name:pms': u'Washington', u'gnis:ST_num': u'11', u'name:kn': u'\u0cb5\u0cbe\u0cb7\u0cbf\u0c82\u0c97\u0ccd\u0c9f\u0ca8\u0ccd, \u0ca1\u0cbf.\u0cb8\u0cbf.', u'name:chy': u'V\xe1\u0161\xeata\xebno', u'name:lv': u'Va\u0161ingtona', u'name:lt': u'Va\u0161ingtonas', u'name:uz': u'Vashington', u'name:ur': u'\u0648\u0627\u0634\u0646\u06af\u0679\u0646 \u0688\u06cc \u0633\u06cc', u'name:lb': u'Washington', u'name:la': u'Vasingtonia', u'name:nds': u'Washington D.C.', u'name:uk': u'\u0412\u0430\u0448\u0438\u043d\u0433\u0442\u043e\u043d', u'name:ug': u'\u06cb\u0627\u0634\u0649\u0646\u06af\u062a\u0648\u0646', u'name:li': u'Washington D.C.', u'name:ln': u'Washington', u'name:el': u'\u039f\u03c5\u03ac\u03c3\u03b9\u03bd\u03b3\u03ba\u03c4\u03bf\u03bd', u'name:eo': u'Va\u015dingtono', u'name:en': u'Washington D.C.', u'name': u'Washington', u'name:th': u'\u0e27\u0e2d\u0e0a\u0e34\u0e07\u0e15\u0e31\u0e19', u'name:lij': u'Washington D.C.', u'is_in:continent': u'North America', u'name:eu': u'Washington', u'name:et': u'Washington', u'name:es': u'Washington D. C.', u'name:diq': u'Washington D.C.', u'name:ay': u'Washington, DC', u'name:rm': u'Washington D.C.', u'name:az': u'Va\u015finqton', u'name:ar': u'\u0648\u0627\u0634\u0646\u0637\u0646', u'name:io': u'Washington DC', u'name:is': u'Washington', u'name:ckb': u'\u0648\u0627\u0634\u06cc\u0646\u06af\u062a\u0646 \u062f\u06cc \u0633\u06cc', u'name:am': u'\u12cb\u123a\u1295\u130d\u1270\u1295 \u12f2\u1232', u'name:it': u'Washington', u'name:an': u'Washington', u'name:ru': u'\u0412\u0430\u0448\u0438\u043d\u0433\u0442\u043e\u043d', u'name:ast': u'Washington DC', u'name:ta': u'\u0bb5\u0bbe\u0b9a\u0bbf\u0b99\u0bcd\u0b9f\u0ba9\u0bcd, \u0b9f\u0bbf. \u0b9a\u0bbf.', u'wikipedia': u'en:Washington, D.C.', u'name:ky': u'\u0412\u0430\u0448\u0438\u043d\u0433\u0442\u043e\u043d', u'capital': u'yes', u'name:zh-yue': u'\u83ef\u76db\u9813\u7279\u5340', u'ele': u'7', u'name:zh': u'\u534e\u76db\u987f\u54e5\u4f26\u6bd4\u4e9a\u7279\u533a', u'name:so': u'Washington D.C', u'name:sk': u'Washington D.C.', u'name:ja': u'\u30ef\u30b7\u30f3\u30c8\u30f3', u'name:sh': u'Washington D.C.', u'name:sg': u'Washington D.C.', u'is_in:country_code': u'US', u'name:se': u'Washington D.C.', u'name:sc': u'Washington', u'name:sa': u'\u0935\u093e\u0936\u093f\u0919\u094d\u0917\u094d\u091f\u0928\u094d \u0921\u093f \u0938\u093f',
                               u'name:arc': u'\u0718\u0710\u072b\u0722\u0713\u071b\u0718\u0722', u'census:population': u'2010', u'name:bn': u'\u0993\u09af\u09bc\u09be\u09b6\u09bf\u0982\u099f\u09a8', u'name:bo': u'\u0f5d\u0f0b\u0f64\u0f72\u0f53\u0f0b\u0f4f\u0fb2\u0f7c\u0f53\u0f0d', u'name:br': u'Washington D.C.', u'name:arz': u'\u0648\u0627\u0634\u064a\u0646\u0637\u0648\u0646', u'name:be': u'\u0412\u0430\u0448\u044b\u043d\u0433\u0442\u043e\u043d', u'name:krc': u'\u0412\u0430\u0448\u0438\u043d\u0433\u0442\u043e\u043d', u'name:sq': u'Uashington D.C.', u'name:xmf': u'\u10d5\u10dd\u10e8\u10d8\u10dc\u10d2\u10d7\u10dd\u10dc\u10d8', u'gnis:Class': u'Populated Place', u'place': u'city', u'name:sah': u'\u0423\u0430\u0448\u0438\u04a5\u0442\u043e\u043d, \u041a\u043e\u043b\u0443\u043c\u0431\u0438\u044f \u042d\u0440\u0433\u0438\u043d', u'name:crh': u'Va\u015fington', u'name:tok': u'ma tomo Sisi', u'gnis:County_num': u'001', u'name:ps': u'\u0648\u0627\u0634\u0646\u06ab\u067c\u0646 \u0689\u064a \u0633\u064a', u'name:tpi': u'Wasington DC', u'name:oc': u'Washington, DC', u'rank': u'0', u'int_name': u'Washington, D.C.', u'alt_name': u'Washington DC', u'name:sv': u'Washington D.C.', u'name:os': u'\u0412\u0430\u0448\u0438\u043d\u0433\u0442\u043e\u043d', u'name:pl': u'Waszyngton', u'name:de': u'Washington D.C.', u'source': u'openstreetmap.org', u'name:pih': u'Woshingtun, D.K.', u'name:cdo': u'Hu\xe0-s\xeang-d\xe1ung, D.C.', u'name:rue': u'\u0412\u0430\u0448\u0456\u043d\u0491\u0442\u043e\u043d', u'name:nov': u'Washington D.K.', u'admin_level': u'2', u'name:scn': u'Washington', u'name:pap': u'Washington D.C.', u'name:he': u'\u05d5\u05d5\u05e9\u05d9\u05e0\u05d2\u05d8\u05d5\u05df', u'name:vep': u'Va\u0161ington', u'name:bpy': u'\u09a1\u09bf\u09b8\u099f\u09bf\u0995\u09cd\u099f \u0985\u09ab \u0995\u09b2\u09ae\u09cd\u09ac\u09bf\u09af\u09bc\u09be, \u09a1\u09bf\u09b8\u09bf', u'name:hy': u'\u054e\u0561\u0577\u056b\u0576\u0563\u057f\u0578\u0576', u'name:ht': u'Wachint\xf2n', u'name:hu': u'Washington', u'name:hr': u'Washington', u'name:vec': u'Washington D.C.', u'population': u'672228', u'name:srn': u'Washington D.C.', u'name:bar': u'Washington', u'name:pnb': u'\u0648\u0627\u0634\u0646\u06af\u0679\u0646 \u0688\u06cc \u0633\u06cc', u'name:yi': u'\u05d5\u05d5\u05d0\u05e9\u05d9\u05e0\u05d2\u05d8\u05d0\u05df', u'name:be-tarask': u'\u0412\u0430\u0448\u044b\u043d\u0433\u0442\u043e\u043d', u'name:fiu-vro': u'Washington', u'name:mr': u'\u0935\u0949\u0936\u093f\u0902\u0917\u094d\u091f\u0928, \u0921\u0940.\u0938\u0940.', u'name:lad': u'Washington, DC', u'name:mg': u'Washington D.C', u'wikidata': u'Q61', u'name:ml': u'\u0d35\u0d3e\u0d37\u0d3f\u0d19\u0d4d\u0d1f\u0d23\u0d4d', u'name:mn': u'\u0412\u0430\u0448\u0438\u043d\u0433\u0442\u043e\u043d \u0445\u043e\u0442', u'name:mi': u'Takiw\u0101 o Columbia', u'name:mk': u'\u0412\u0430\u0448\u0438\u043d\u0433\u0442\u043e\u043d', u'name:vo': u'Washington', u'name:fa': u'\u0648\u0627\u0634\u0646\u06af\u062a\u0646', u'name:haw': u'Wakinekona', u'name:fi': u'Washington', u'name:ext': u'Washington D.C.', u'old_name:vi': u'Hoa Th\u1ecbnh \u0110\u1ed1n', u'name:fo': u'Washington DC', u'alt_name:vi': u'Oa-sinh-t\u01a1n', u'name:fr': u'Washington', u'gnis:County': u'District of Columbia', u'name:fy': u'Washington D.C.', u'name:nl': u'Washington D.C.', u'name:xal': u'\u0412\u0430\u0448\u0438\u043d\u0433\u0442\u043e\u043d', u'name:ang': u'H\u01bf\xe6singat\u016bn', u'gnis:ST_alpha': u'DC', u'is_in:country': u'United States', u'name:gn': u'Washington D.C.', u'is_in:iso_3166_2': u'US-DC'}))

        self.assert_has_feature(
            8, 73, 97, 'places',
            {'id': 158368533, 'region_capital': type(None)})

    def test_no_country_capital_false(self):
        # Node: Deerfield, Nova Scotia (3441540432)
        # no country_capital when falsey
        self.generate_fixtures(dsl.way(3441540432, wkt_loads('POINT (-66.0026501885864 43.93450966345367)'), {u'name': u'Deerfield, Nova Scotia', u'is_in:country': u'Canada',
                               u'is_in:continent': u'North America', u'wikipedia': u'en:Deerfield, Nova Scotia', u'source': u'openstreetmap.org', u'wikidata': u'Q5250883', u'capital': u'no', u'place': u'locality'}))

        self.assert_has_feature(
            16, 20752, 23846, 'places',
            {'id': 3441540432, 'country_capital': type(None)})
