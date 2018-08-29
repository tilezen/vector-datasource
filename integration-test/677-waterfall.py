# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class Waterfall(FixtureTest):
    def test_more_than_300m(self):
        # Upper Yosemite Falls, because it's so tall at 550 meters, more than
        # 300 meters
        self.generate_fixtures(dsl.way(2389658224, wkt_loads('POINT (-119.596768770024 37.7569711773355)'), {u'FIPS_C': u'06043', u'wikipedia:en': u'Yosemite_Falls', u'height': u'550', u'FIPSCO': u'043', u'wikidata': u'Q491677', u'waterway': u'waterfall', u'TOPOMAP': u'Yosemite Falls', u'wikipedia': u'en:Yosemite Falls', u'ele': u'1599', u'source': u'openstreetmap.org', u'name:zh': u'\u4e0a\u4f18\u80dc\u7f8e\u5730\u5927\u7011\u5e03', u'CLASS': u'Falls', u'DATE_CREAT': u'01/19/1981', u'ELEV_FEET': u'5246', u'GNISID': u'236934', u'LONGITUDE': u'-119.59683', u'STATE': u'CA', u'tourism': u'attraction', u'LAYER': u'Unknown Point Feature', u'name': u'Upper Yosemite Fall', u'COUNTYNAME': u'Mariposa', u'LATITUDE': u'37.75631', u'FIPSST': u'06'}))  # noqa

        self.assert_has_feature(
            12, 687, 1583, 'pois',
            {'kind': 'waterfall', 'min_zoom': 12, 'height': 550})

    def test_more_than_50m(self):
        # Middle Yosemite Falls, 206 meters, more than 50 meters
        self.generate_fixtures(dsl.way(2384221575, wkt_loads('POINT (-119.597269131638 37.7542908234491)'), {u'gnis:state_id': u'06', u'name': u'Middle Cascades', u'wikipedia:en': u'Yosemite_Falls', u'wikipedia': u'en:Yosemite Falls', u'gnis:county_id': u'043', u'height': u'206', u'source': u'openstreetmap.org', u'wikidata': u'Q491677', u'alt_name': u'Yosemite Falls', u'waterway': u'waterfall', u'name:zh': u'\u4e2d\u4f18\u80dc\u7f8e\u5730\u5927\u7011\u5e03', u'gnis:feature_id': u'252230'}))  # noqa

        self.assert_has_feature(
            13, 1374, 3166, 'pois',
            {'kind': 'waterfall', 'min_zoom': 13})

    def test_98m_fall(self):
        # Lower Yosemite Falls, only 98 meters
        self.generate_fixtures(dsl.way(2389657981, wkt_loads('POINT (-119.597140672552 37.7514441683717)'), {u'FIPS_C': u'06043', u'wikipedia:en': u'Yosemite_Falls', u'height': u'98', u'FIPSCO': u'043', u'wikidata': u'Q491677', u'waterway': u'waterfall', u'TOPOMAP': u'Yosemite Falls', u'ELEVATION': u'1368', u'wikipedia': u'en:Yosemite Falls', u'ele': u'1368', u'source': u'openstreetmap.org', u'name:zh': u'\u4e0b\u4f18\u80dc\u7f8e\u5730\u5927\u7011\u5e03', u'CLASS': u'Falls', u'DATE_CREAT': u'01/19/1981', u'ELEV_FEET': u'4488', u'GNISID': u'227800', u'LONGITUDE': u'-119.59655', u'STATE': u'CA', u'tourism': u'attraction', u'LAYER': u'Unknown Point Feature', u'name': u'Lower Yosemite Fall', u'COUNTYNAME': u'Mariposa', u'LATITUDE': u'37.75131', u'FIPSST': u'06'}))  # noqa

        self.assert_has_feature(
            13, 1374, 3167, 'pois',
            {'kind': 'waterfall', 'min_zoom': 13})

    def test_niagara_horseshoe_falls(self):
        # Niagara Falls (Horseshoe Falls)
        self.generate_fixtures(dsl.way(708267915, wkt_loads('POINT (-79.0749682492429 43.07726879171867)'), {u'source': u'openstreetmap.org', u'waterway': u'waterfall', u'name': u'Horseshoe Falls'}),dsl.way(56539663, wkt_loads('POLYGON ((-79.07843574623961 43.07866567353248, -79.07828932084828 43.0787116036259, -79.0780856727734 43.07887609869209, -79.0779867682606 43.0789579195677, -79.0780519859503 43.0788946675131, -79.07810327975299 43.07884211051748, -79.0781084899816 43.0788032012521, -79.07806537084799 43.07872459527459, -79.07802189238831 43.0786557657507, -79.0779498475025 43.07858418033929, -79.07738624449318 43.07786031655819, -79.07667280249461 43.07745881518491, -79.07650454804178 43.07748571763081, -79.07638677890809 43.07738729399088, -79.0760357172951 43.07727607508761, -79.07587878161489 43.0771374940831, -79.0757711634439 43.07712640496459, -79.07542522222801 43.07715940984989, -79.07533709749859 43.07719175855728, -79.0749682492429 43.07726879171867, -79.07464620321359 43.07737915762959, -79.0746119774012 43.07760376017429, -79.07456068359851 43.0777241646468, -79.0744870217452 43.07779739144738, -79.07440240044551 43.07793656149649, -79.07445207728068 43.0779794738382, -79.07440033432029 43.07829048899488, -79.0744692351026 43.0783231651793, -79.07450139478979 43.0783898954052, -79.07450399990411 43.07843687554028, -79.07456571416408 43.078521059128, -79.0746167384723 43.07862099008008, -79.07465958811129 43.07864060880989, -79.0746515931053 43.0786759093849, -79.07468375279248 43.07871120993948, -79.0746945325759 43.07875615578359, -79.0747427721066 43.0787933591069, -79.07477232667949 43.07882478835189, -79.07475076711269 43.0788639600605, -79.07476963173359 43.07890510016968, -79.07479640152908 43.07895017709977, -79.07477762673962 43.078979572227, -79.0748393409997 43.07902458348829, -79.07489027547629 43.07905988384198, -79.07489827048229 43.07910686346348, -79.0748955755365 43.0791480034096, -79.0748500309515 43.07918527210889, -79.0748124813727 43.07921269870759, -79.07481787126439 43.07924399650988, -79.0748447308914 43.0793048204949, -79.07485542084329 43.07937916083899, -79.07485542084329 43.0794536979337, -79.07484203594549 43.0794810587987, -79.07479640152908 43.07951439048349, -79.07471061241948 43.07953197490829, -79.07471860742548 43.07956340377441, -79.0747642418419 43.07957901978118, -79.07475076711269 43.07962606461799, -79.0747562468359 43.0796691726166, -79.07472130237132 43.07968865978408, -79.074726692263 43.07971812017037, -79.07477232667949 43.079743578132, -79.07478840652308 43.07976516490038, -79.07474537722101 43.07978471765058, -79.07472399731718 43.07981798355699, -79.0747427721066 43.07984547548568, -79.07477232667949 43.0798572202438, -79.07474537722101 43.07988070975338, -79.0747615468961 43.0799139756076, -79.07467566795491 43.079935562316, -79.07465958811129 43.07996685974889, -79.0745640971966 43.07994140188008, -79.07449807102319 43.07992841048939, -79.07449357944679 43.07975945654601, -79.07449896933851 43.07966549826789, -79.074552598761 43.07952436373999, -79.07450974912189 43.07935599920568, -79.07445611969939 43.0792579722528, -79.0743649406981 43.07910515750021, -79.07431122144412 43.07874861013318, -79.07412877360989 43.0783685706113, -79.07381768702699 43.07794929084869, -79.07341542144279 43.07787088062158, -79.07313110465539 43.0778042810612, -79.0732919929228 43.0776161615179, -79.07367287860319 43.07759660807559, -79.07396249545079 43.0775926711402, -79.07416785032478 43.0772596054865, -79.0742736718653 43.077083295177, -79.07465994743738 43.07690311299668, -79.07500319370749 43.07682470143089, -79.0755021180163 43.07684432073589, -79.0760546717476 43.07711859664909, -79.07673586422749 43.0773340795438, -79.07732066747748 43.07758879982008, -79.07766400357899 43.07787488315448, -79.0779053808959 43.0783097797565, -79.078152237936 43.0785841147248, -79.07843574623961 43.07866567353248))'), {u'name:sl': u'Niagarski slapov', u'name:sk': u'Niagarsk\xe9 vodop\xe1dy', u'name': u'Horseshoe Falls', u'wikipedia': u'en:Horseshoe Falls', u'way_area': u'40670.9', u'name:cs': u'Niagarsk\xe9 vodop\xe1dy', u'natural': u'cliff', u'source': u'openstreetmap.org', u'name:fr': u'Chutes du Niagara', u'wikidata': u'Q1373778', u'alt_name': u'Niagara Falls', u'name:ru': u'\u0412\u043e\u0434\u043e\u043f\u0430\u0434 "\u041f\u043e\u0434\u043a\u043e\u0432\u0430"', u'waterway': u'waterfall', u'tourism': u'attraction'}))  # noqa

        self.assert_has_feature(
            12, 1148, 1503, 'pois',
            {'kind': 'waterfall', 'min_zoom': 12})

        # We had considered this for label_placement:yes,
        # but there are only 19 in all of North America
        self.assert_no_matching_feature(
            12, 1148, 1503, 'water',
            {'kind': 'waterfall'})

    def test_height_missing(self):
        # Alamere Falls (no height)
        # Assume falls are important, show at zoom 14 default
        self.generate_fixtures(dsl.way(2375445789, wkt_loads('POINT (-122.783122278043 37.95391767741348)'), {u'wikipedia': u'en:Alamere Falls', u'waterway': u'waterfall', u'wikidata': u'Q37957', u'name': u'Alamere Falls', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_has_feature(
            14, 2604, 6322, 'pois',
            {'kind': 'waterfall', 'min_zoom': 14})

        # Lower Chilnualna Fall, no height
        self.generate_fixtures(dsl.way(1247873121, wkt_loads('POINT (-119.631362801784 37.55080207032658)'), {u'source': u'openstreetmap.org', u'natural': u'waterfall', u'name': u'Lower Chilnualna Fall'}))  # noqa

        self.assert_has_feature(
            14, 2747, 6345, 'pois',
            {'kind': 'waterfall', 'min_zoom': 14})

        # https://www.openstreetmap.org/node/1247872815
        # Chilnualna Creek Cascades, no height
        self.generate_fixtures(dsl.way(1247872815, wkt_loads('POINT (-119.612561242551 37.56504890695991)'), {u'note': u'Series of cascades on Chilnualna Creek. Not technically part of Chilnualna Falls, but part of the same system', u'source': u'openstreetmap.org', u'natural': u'waterfall', u'name': u'Chilnualna Creek Cascades'}))  # noqa

        self.assert_has_feature(
            14, 2748, 6344, 'pois',
            {'kind': 'waterfall', 'min_zoom': 14})

    def test_less_than_8m(self):
        # Abrigo Falls, 4.5 meters (less than 8 meters)
        # Allow short waterfalls to be suppressed a zoom
        self.generate_fixtures(dsl.way(3257658773, wkt_loads('POINT (-122.153388082347 37.94552742279537)'), {u'source': u'openstreetmap.org', u'waterway': u'waterfall', u'name': u'Abrigo Falls', u'height': u'4.5'}))  # noqa

        self.assert_has_feature(
            15, 5265, 12645, 'pois',
            {'kind': 'waterfall', 'min_zoom': 15})

    def test_unit_conversion_height(self):
        # Rainbow Falls - height 150ft = 45m
        self.generate_fixtures(dsl.way(877270365, wkt_loads('POINT (-82.96562582334471 35.09064146759331)'), {u'source': u'openstreetmap.org', u'waterway': u'waterfall', u'name': u'Rainbow Falls', u'height': u'150 ft'}))  # noqa

        self.assert_has_feature(
            14, 4416, 6484, 'pois',
            {'kind': 'waterfall', 'min_zoom': 14, 'height': 45.72})

        # Toccoa Falls - height 186' = 56.6929m
        self.generate_fixtures(dsl.way(404574988, wkt_loads('POINT (-83.3606066994399 34.59619179112848)'), {u'source': u'openstreetmap.org', u'waterway': u'waterfall', u'natural': u'cliff', u'name': u'Toccoa Falls', u'height': u"186'"}))  # noqa

        self.assert_has_feature(
            13, 2199, 3256, 'pois',
            {'kind': 'waterfall', 'min_zoom': 13, 'height': 56.6928})

        # Eternal Flame Falls - height 9m (with unit)
        self.generate_fixtures(dsl.way(3647404249, wkt_loads('POINT (-78.7516626920262 42.70175278571357)'), {u'natural': u'cliff', u'name': u'Eternal Flame Falls', u'height': u'9 m', u'source': u'openstreetmap.org', u'waterway': u'waterfall', u'tourism': u'attraction'}))  # noqa

        self.assert_has_feature(
            15, 9215, 12077, 'pois',
            {'kind': 'waterfall', 'min_zoom': 15, 'height': 9})
