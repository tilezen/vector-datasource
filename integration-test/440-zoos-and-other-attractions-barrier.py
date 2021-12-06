# -*- encoding: utf-8 -*-
import dsl
from shapely.wkt import loads as wkt_loads

from . import FixtureTest


class ZoosAndOtherAttractionsBarrier(FixtureTest):
    def test_fences_around_enclosures(self):
        # barrier=fence around enclosures
        self.generate_fixtures(dsl.way(316623706, wkt_loads('POLYGON ((-117.060170479934 51.29075749793969, -117.05995748938 51.29087490941641, -117.059694013507 51.29098546693429, -117.059412481497 51.29109158617149, -117.059033482278 51.29119309862668, -117.058712334564 51.29129916120679, -117.058380317235 51.2914324132113, -117.05816373342 51.29160841537159, -117.058026560676 51.29169419722047, -117.057813570123 51.29184986249769, -117.057618725537 51.29198991023731, -117.057373305802 51.2921297890213, -117.057124202974 51.29228326196, -117.056741700326 51.29207338814918, -117.056579195091 51.29192440861999, -117.056279696775 51.2916557723649, -117.056041463562 51.29141426804119, -117.055846618977 51.29120219934499, -117.055637221684 51.2909267613749, -117.055427914223 51.29062430015458, -117.055597516148 51.29052497738771, -117.055918843525 51.29042346345539, -117.056175043044 51.2903421734983, -117.056232804717 51.2902180754217, -117.056384260674 51.29010290941009, -117.056730830711 51.28999229358838, -117.057080904177 51.28990426140589, -117.057297487992 51.28982077955029, -117.057640374936 51.28966280404911, -117.057947239437 51.28954319848048, -117.058271980412 51.28939870509998, -117.058517400148 51.28928359321298, -117.058687091905 51.2891933124828, -117.058863880353 51.28907370569137, -117.059109300088 51.28892921083359, -117.059286178368 51.28917977316698, -117.059112983181 51.28933100878368, -117.058867473614 51.28956117585217, -117.058982996959 51.28979151030399, -117.059246472832 51.2898839808345, -117.0595748969 51.29001718076711, -117.059722939259 51.29009616797609, -117.059823999728 51.2901277965288, -117.05995748938 51.29029251183658, -117.060051363327 51.29050020284048, -117.060145237274 51.29068300610069, -117.060170479934 51.29075749793969))'), {u'name': u'Bear Enclosure', u'barrier': u'fence', u'area': u'yes', u'way_area': u'150889', u'zoo': u'enclosure', u'source': u'openstreetmap.org', u'tourism': u'zoo'}))

        self.assert_has_feature(
            16, 11458, 21855, 'landuse',
            {'kind': 'fence'})
