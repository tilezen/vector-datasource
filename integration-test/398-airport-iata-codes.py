# -*- encoding: utf-8 -*-
import dsl
from shapely.wkt import loads as wkt_loads

from . import FixtureTest


class AirportIataCodes(FixtureTest):
    def test_sfo(self):
        # San Francisco International
        self.generate_fixtures(dsl.way(23718192, wkt_loads('POLYGON ((-122.402782773269 37.63531941394439, -122.40266823807 37.63591797330289, -122.402642995411 37.63627586880459, -122.400825793423 37.63777992163308, -122.400541476635 37.6380545077576, -122.400242517309 37.63819677996181, -122.399856241737 37.6383059736938, -122.399504910629 37.6383616019698, -122.398018917486 37.63836757738308, -122.397126531083 37.63836700829618, -122.396226059842 37.6386334827911, -122.395922968265 37.63869978115548, -122.395041092151 37.6386999945622, -122.394648708034 37.63862437743169, -122.394254167962 37.63858532396358, -122.392438313446 37.63858546623489, -122.391235918439 37.6385816960447, -122.390817393348 37.63864899035377, -122.389157396534 37.63901967704601, -122.388567922045 37.6391058929143, -122.388302919036 37.63913456037959, -122.388062529866 37.6390834141992, -122.387878285401 37.63897038030411, -122.387772913018 37.63880221628041, -122.387668528782 37.63847058205218, -122.387559113981 37.63819279634378, -122.386109861933 37.6361934199638, -122.385986523244 37.63597168263642, -122.385954633052 37.63578217032489, -122.385994338587 37.63559571648658, -122.386109592438 37.63542768710219, -122.386339022162 37.63525887481049, -122.386630794966 37.63517770534189, -122.387070430466 37.6351242088515, -122.387272910731 37.63505619995949, -122.38816152421 37.63456149742279, -122.388740129085 37.63412156936317, -122.389776874754 37.63391569010429, -122.391048170544 37.6335037164537, -122.391386206586 37.6332148142114, -122.391498765491 37.6329047108011, -122.391448819161 37.63268018914851, -122.3909392049 37.63174545752518, -122.392199810738 37.63131220020119, -122.391559311941 37.62998359980139, -122.391427439257 37.6298805122232, -122.388171226015 37.62852100917631, -122.387996773187 37.62878630951541, -122.385765178358 37.62809285554551, -122.379756976244 37.63013221925351, -122.37423197792 37.62792552065459, -122.372338688627 37.62743632006278, -122.371877763055 37.62812010434631, -122.368255665998 37.62669262369908, -122.36714849241 37.62843961891189, -122.365768141145 37.62789087260929, -122.365253136992 37.62676932017637, -122.368741924061 37.62124049667588, -122.367821330558 37.62020429901018, -122.367308033205 37.62043946015379, -122.366929483144 37.62051801305999, -122.366536470207 37.6205380781912, -122.366328240724 37.62050271517259, -122.365617314008 37.62026477925429, -122.365174444573 37.61998422165949, -122.365064221288 37.61986567988729, -122.364742714248 37.61903317832368, -122.364662584524 37.6189115042374, -122.364569519061 37.61884938633769, -122.355255426869 37.61492880935528, -122.355170895401 37.61486868056239, -122.355135142453 37.61479915880869, -122.355136310262 37.6147250116876, -122.355179609059 37.6146547070554, -122.358802963758 37.60916860603569, -122.366974758234 37.6124694664738, -122.367632684348 37.61287835449848, -122.368775431221 37.61338750447399, -122.371457171839 37.61520340875107, -122.378584674798 37.60572142198278, -122.378192021187 37.6052981187722, -122.378828297903 37.60493409601148, -122.381680808256 37.60455576665628, -122.381876820651 37.6044554905509, -122.382042290326 37.60436631658349, -122.382557923299 37.60463568853699, -122.383020825165 37.60492406134129, -122.383427672157 37.60520289656819, -122.384410159584 37.60584226364769, -122.384490109644 37.60594787540128, -122.385525687504 37.60664039727529, -122.385564943881 37.6070947211435, -122.385595486601 37.60767436434308, -122.386246405856 37.6079477807216, -122.386327703389 37.6078152002346, -122.386698707602 37.60797396943178, -122.386608516747 37.60810868458069, -122.386847468613 37.60820916925559, -122.386492364581 37.608780264068, -122.385977719755 37.6085681233169, -122.385745145927 37.60891967458439, -122.385749727335 37.60929072304688, -122.385947895687 37.60937825434759, -122.385847913196 37.6095336043617, -122.386355281668 37.60975648801139, -122.386575818071 37.60953737602549, -122.386752606519 37.60946372180269, -122.386992366868 37.60946770696059, -122.387235361152 37.6095741675278, -122.387984825594 37.60966746272569, -122.388313608988 37.60994386062659, -122.389838229688 37.6095805722362, -122.391743107248 37.6107278601031, -122.392167740883 37.61101065864849, -122.392897172894 37.6129271704265, -122.393137831558 37.6133756207896, -122.393493025421 37.61333456157809, -122.393827737696 37.61327258133899, -122.394060760681 37.61321415904558, -122.394076032041 37.61315096898599, -122.394739078552 37.61303611664558, -122.394902661765 37.61344201284619, -122.39614071989 37.61453935892668, -122.39703409444 37.61493919846718, -122.397241874765 37.6151045701634, -122.397419561528 37.61531825774418, -122.39777170112 37.61584418416938, -122.398200017847 37.61692939821548, -122.398558984635 37.61787840495269, -122.399218258222 37.61967776304128, -122.399837826273 37.6214926598776, -122.400493416768 37.62341132060519, -122.401401433857 37.62610950021288, -122.401612807443 37.62729530789251, -122.401933865326 37.62929079730368, -122.40191239559 37.6295417237437, -122.401836038791 37.629813423405, -122.401691859188 37.63007658481649, -122.400390469836 37.6320202082337, -122.400645860871 37.63246797430131, -122.401998813521 37.6331083874929, -122.402180632534 37.6332533013763, -122.4022967847 37.63343378528259, -122.402344844568 37.63359136153137, -122.402782773269 37.63531941394439))'), {u'gnis:county_name': u'San Mateo', u'internet_access:ssid': u'#SFO FREE WIFI', u'wikidata': u'Q8688', u'owner': u'San Francisco Airport Commission', u'name:de': u'Internationaler Flughafen San Francisco', u'is_in': u'San Mateo County', u'addr:housenumber': u'780', u'gnis:feature_type': u'Airport', u'way_area': u'1.24398e+07', u'wikipedia': u'en:San Francisco International Airport', u'addr:state': u'CA', u'ele': u'4', u'source': u'openstreetmap.org', u'gnis:feature_id': u'1653945', u'addr:street': u'S Airport Blvd', u'ref': u'KSFO', u'website': u'http://www.flysfo.com/', u'city_served': u'San Francisco, California', u'name:ja': u'\u30b5\u30f3\u30d5\u30e9\u30f3\u30b7\u30b9\u30b3\u56fd\u969b\u7a7a\u6e2f', u'short_name': u'San Francisco Airport', u'passengers': u'47155100', u'iata': u'SFO', u'aerodrome:type': u'public', u'icao': u'KSFO', u'gnis:created': u'03/01/1994', u'aerodrome': u'international', u'name:el': u'\u0394\u03b9\u03b5\u03b8\u03bd\u03ae\u03c2 \u0391\u03b5\u03c1\u03bf\u03bb\u03b9\u03bc\u03ad\u03bd\u03b1\u03c2 \u03a3\u03b1\u03bd \u03a6\u03c1\u03b1\u03bd\u03c3\u03af\u03c3\u03ba\u03bf', u'name:en': u'San Francisco International Airport', u'name': u'San Francisco International Airport', u'addr:postcode': u'94128', u'addr:city': u'San Francisco', u'internet_access:fee': u'no', u'aeroway': u'aerodrome', u'internet_access': u'wlan', u'is_in:iso_3166_2': u'US-CA', u'source_ref': u'geonames.usgs.gov'}))

        self.assert_has_feature(
            13, 1311, 3170, 'pois',
            {'kind': 'aerodrome', 'iata': 'SFO'})

    def test_oak(self):
        # Oakland airport
        self.generate_fixtures(dsl.way(54363486, wkt_loads('POLYGON ((-122.251293129543 37.72490617803489, -122.251293129543 37.72528631025018, -122.250709404272 37.72582261309319, -122.250271745065 37.7262367743562, -122.250091363356 37.72640651656879, -122.249069978878 37.72646079988989, -122.248855101862 37.72649689401339, -122.248675438806 37.72635479106338, -122.248666635316 37.72625027416969, -122.248469185616 37.7260669607028, -122.248469185616 37.72593807259049, -122.248623695845 37.72582261309319, -122.248752514257 37.72576825825217, -122.249044287061 37.72558501464461, -122.248331923041 37.72504871008109, -122.2479457373 37.7249128570103, -122.247782603245 37.72500117574517, -122.247542303906 37.7250079968177, -122.247327696385 37.72510981546048, -122.247233283448 37.72502838897859, -122.246898481342 37.72512338653218, -122.246718279296 37.72511656547029, -122.245619639704 37.72529988128949, -122.245447971653 37.72529988128949, -122.244804328752 37.72495371243168, -122.24467551034 37.72485182252129, -122.244512376284 37.7248246802761, -122.244323640243 37.72472968233939, -122.244109032722 37.72456668634359, -122.243937364671 37.72443765351368, -122.243646220687 37.72425156447159, -122.239630212378 37.7209887130929, -122.236737188006 37.71960011022599, -122.236621934155 37.71958952257982, -122.236554830003 37.71960011022599, -122.236205385357 37.71989478726049, -122.234797186318 37.72126107288809, -122.233032266279 37.72297109718351, -122.232549601477 37.7234314597321, -122.232078614774 37.72388876410138, -122.231358615074 37.72458778915839, -122.228689900027 37.72721628601359, -122.228556500208 37.72728861560778, -122.228344587632 37.72728229209988, -122.228231759233 37.7272540849852, -122.226920398581 37.7269259011653, -122.226794275115 37.72716768730739, -122.226740645692 37.7271634953123, -122.226721870903 37.72736499501418, -122.226727170963 37.72824956937759, -122.227655579809 37.72842811712219, -122.229165378307 37.72871849608017, -122.229052729571 37.72902819922441, -122.227660610375 37.73160566920351, -122.226756725536 37.73164808395509, -122.226756725536 37.73330060628359, -122.22662530201 37.7335700079751, -122.226531428063 37.73386271123349, -122.226469713803 37.7341723928629, -122.226453633959 37.7345414657444, -122.226445189796 37.73578500402448, -122.22645956284 37.73899030097969, -122.226462706944 37.7396773910561, -122.226480493586 37.74363052145789, -122.223849238287 37.74366227408098, -122.223878703029 37.7449985001975, -122.224981115545 37.74510881537909, -122.224986505437 37.7452614663153, -122.22449297102 37.7453335651822, -122.224001862054 37.74538996562618, -122.223736859045 37.74540999700779, -122.223386875411 37.74543301177997, -122.222657892558 37.74542995735078, -122.222356867106 37.74542399055839, -122.222115938947 37.74539699792041, -122.22201092589 37.7453789554674, -122.221959901582 37.74536496190831, -122.221738916022 37.74532497014858, -122.221533920474 37.74528497836727, -122.221283919331 37.74521600492469, -122.220993943157 37.74511300635818, -122.220868897669 37.74506498766729, -122.22042692655 37.74486396233569, -122.220167942253 37.74472700907621, -122.219941926128 37.74458302319249, -122.219780858197 37.74445601419819, -122.219598859521 37.7443109622726, -122.219506872036 37.74422898862967, -122.219180873419 37.74388901724902, -122.219129938942 37.7438140045485, -122.219053941469 37.743729970344, -122.218955935272 37.74360999234979, -122.218702879856 37.7433220159562, -122.218492943574 37.74306799342191, -122.218350919928 37.74288301673258, -122.218234857593 37.74274698327319, -122.218044863911 37.74250901291288, -122.217887928231 37.74232801285489, -122.217629932081 37.7420009613922, -122.217460869144 37.741798009747, -122.216767908734 37.74091295789887, -122.215603781958 37.73950455355099, -122.214659562762 37.73837829385128, -122.214093713965 37.73765929445129, -122.213559935023 37.73698049748229, -122.213345417333 37.73667501905528, -122.213176444228 37.73639930593229, -122.212881257826 37.73591351978678, -122.212755314023 37.73567595371398, -122.212487077079 37.73509901451231, -122.212256389714 37.73459631145159, -122.211846039293 37.73373291311091, -122.211615262096 37.73327900863718, -122.211462368835 37.73295646408938, -122.211014468834 37.73200615727129, -122.210864270519 37.73174527545498, -122.210687302408 37.73149071586859, -122.210440535199 37.73123395295428, -122.209893371359 37.7307884877894, -122.209311263055 37.73039609257019, -122.208659535317 37.73001421038119, -122.207375124124 37.72930607125718, -122.205283037658 37.72815628102949, -122.20212869337 37.72638278536621, -122.201608389157 37.72624281374678, -122.200337003535 37.72580151063029, -122.199832689335 37.72561059346148, -122.19938748428 37.72538990482221, -122.199671531573 37.72489580430601, -122.199730281393 37.724835054015, -122.199822179046 37.72476115885698, -122.199902668096 37.72467397668627, -122.199995464064 37.72452959653339, -122.200099938132 37.7243327786471, -122.200176025437 37.72413617339889, -122.200230373511 37.7239380044439, -122.20026558747 37.7236803626934, -122.200231631153 37.72315278405669, -122.200230014185 37.72269810418028, -122.200249597458 37.72236002347581, -122.200313557507 37.72196459925629, -122.200420636688 37.72159105821197, -122.200535261719 37.72123890327881, -122.20072579439 37.72080268644267, -122.200918842345 37.7204400112942, -122.201175940179 37.72006447294958, -122.201490260697 37.7196851666305, -122.201784099627 37.7193575177389, -122.202200917919 37.71896406713338, -122.202626809195 37.71857871516488, -122.202868905164 37.7183700856397, -122.202909419183 37.71816571909098, -122.203313481398 37.71785959456909, -122.20244256473 37.71708177109411, -122.202021973514 37.71674920749609, -122.201678727244 37.71650106291599, -122.201399710517 37.71624225831889, -122.201104703777 37.7159580127994, -122.200854702634 37.7156763954754, -122.200552060215 37.71538930530248, -122.200210969901 37.71511280230468, -122.199884791621 37.71485477454648, -122.199507229708 37.7144473716878, -122.200841766894 37.71374277903888, -122.200927645835 37.7136578579394, -122.200970585305 37.7135475669603, -122.200976604018 37.7134330119809, -122.200948217255 37.71330658912748, -122.202133723935 37.71302645407658, -122.204107771772 37.71257242269488, -122.20510562039 37.712349563262, -122.205883471594 37.71216500728681, -122.206845746927 37.71190796417878, -122.206905844219 37.71185367019291, -122.207086046265 37.71180619845529, -122.207163211548 37.71183327440519, -122.20728089085 37.7118383200536, -122.208766794162 37.71149450452489, -122.209276408422 37.7113692864847, -122.209703826835 37.7112697230678, -122.209849803068 37.71120860627168, -122.210004223466 37.71108637252841, -122.210313243923 37.71080800574517, -122.210699519495 37.71041415440249, -122.211128644707 37.70999315328689, -122.211440988931 37.7097396560193, -122.211824479726 37.7093514133591, -122.211969377981 37.70919222119888, -122.211996237608 37.70905221709679, -122.211170146873 37.70203241348079, -122.211172841819 37.7019283597972, -122.211215691458 37.7018370994791, -122.212551396454 37.700546791649, -122.212803643385 37.70028160551789, -122.21358679465 37.69954937129089, -122.213712828285 37.69945178216058, -122.2139094695 37.6992977573942, -122.214029664085 37.69926385342248, -122.214167016492 37.69927067686459, -122.215772126242 37.6995422635655, -122.216407235148 37.6996441882836, -122.216730718482 37.6997436962414, -122.21699572149 37.6998624659219, -122.231144277047 37.70987098860599, -122.244036898004 37.71908799328549, -122.249210924546 37.72267501128519, -122.250975485259 37.7240642670484, -122.251198626776 37.72428837020699, -122.251258724068 37.7244648669541, -122.251293129543 37.72490617803489))'), {u'gnis:county_name': u'Alameda', u'source_ref': u'geonames.usgs.gov', u'iata': u'OAK', u'name:ja': u'\u30aa\u30fc\u30af\u30e9\u30f3\u30c9\u56fd\u969b\u7a7a\u6e2f', u'gnis:feature_type': u'Airport', u'way_area': u'1.54832e+07', u'wikipedia': u'en:Oakland International Airport', u'addr:state': u'CA', u'ele': u'2', u'icao': u'KOAK', u'source': u'openstreetmap.org', u'aeroway': u'aerodrome', u'wikidata': u'Q1165584', u'gnis:created': u'03/01/1994', u'gnis:feature_id': u'1653772', u'aerodrome': u'international', u'name': u'Metropolitan Oakland International Airport'}))

        self.assert_has_feature(
            13, 1314, 3167, 'pois',
            {'kind': 'aerodrome', 'iata': 'OAK'})
