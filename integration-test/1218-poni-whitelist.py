# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class PoniWhitelist(FixtureTest):

    def test_aeroway_helipad(self):
        # aeroway=helipad
        # min_zoom: 16
        self.generate_fixtures(dsl.way(2207370738, wkt_loads('POINT (-122.532516658118 37.84209588684551)'), {u'source': u'openstreetmap.org', u'aeroway': u'helipad'}))  # noqa

        self.assert_no_matching_feature(
            15, 5230, 12657, 'pois',
            {'id': 2207370738})

        self.assert_has_feature(
            16, 10461, 25315, 'pois',
            {'id': 2207370738})

    def test_amenity_atm(self):
        # amenity=atm
        # min_zoom: 17
        # it's on the edge, might be 16, 10481, 25338
        self.generate_fixtures(dsl.way(4113423533, wkt_loads('POINT (-122.420694191888 37.7446735205196)'), {u'operator': u'Bank of America', u'source': u'openstreetmap.org', u'amenity': u'atm'}))  # noqa

        self.assert_no_matching_feature(
            15, 5242, 12668, 'pois',
            {'id': 4113423533})

        self.assert_has_feature(
            16, 10481, 25337, 'pois',
            {'id': 4113423533})

    def test_amenity_bench(self):
        # min_zoom: 18
        self.generate_fixtures(dsl.way(3951215438, wkt_loads('POINT (-122.432994912905 37.713602215024)'), {u'source': u'openstreetmap.org', u'amenity': u'bench'}))  # noqa

        # self.assert_no_matching_feature(
        #     15, 5239, 12672, 'pois',
        #     {'id': 3951215438})

        self.assert_has_feature(
            16, 10479, 25345, 'pois',
            {'id': 3951215438})

    def test_amenity_bicycle_rental(self):
        # when operator: false, then min_zoom: 16
        # when operator: true, then min_zoom: 17
        self.generate_fixtures(dsl.way(3509468129, wkt_loads('POINT (-122.301536442373 37.86428418275169)'), {u'website': u'http://www.watersideworkshops.org/', u'source': u'openstreetmap.org', u'amenity': u'bicycle_rental'}))  # noqa

        self.assert_no_matching_feature(
            15, 5251, 12655, 'pois',
            {'id': 3509468129})

        self.assert_has_feature(
            16, 10503, 25310, 'pois',
            {'id': 3509468129})

    def test_amenity_car_sharing(self):
        # min_zoom: 16
        self.generate_fixtures(dsl.way(4758733421, wkt_loads('POINT (-122.142238372704 37.4203203596844)'), {u'operator': u'Zipcar', u'source': u'openstreetmap.org', u'amenity': u'car_sharing'}))  # noqa

        self.assert_no_matching_feature(
            15, 5266, 12706, 'pois',
            {'id': 4758733421})

        self.assert_has_feature(
            16, 10532, 25412, 'pois',
            {'id': 4758733421})

    def test_amenity_fuel(self):
        self.generate_fixtures(dsl.way(2059530671, wkt_loads('POINT (-122.437729303947 37.723845776474)'), {u'source': u'openstreetmap.org', u'amenity': u'fuel'}))  # noqa

        self.assert_no_matching_feature(
            15, 5239, 12671, 'pois',
            {'id': 2059530671})

        self.assert_has_feature(
            16, 10478, 25342, 'pois',
            {'id': 2059530671})

    def test_amenity_post_box(self):
        self.generate_fixtures(dsl.way(4397690695, wkt_loads('POINT (-122.438485146427 37.71537090022628)'), {u'operator': u'USPS', u'source': u'openstreetmap.org', u'amenity': u'post_box'}))  # noqa

        self.assert_no_matching_feature(
            15, 5239, 12672, 'pois',
            {'id': 4397690695})

        self.assert_has_feature(
            16, 10478, 25344, 'pois',
            {'id': 4397690695})

    def test_amenity_recycling(self):
        self.generate_fixtures(dsl.way(2338524067, wkt_loads('POINT (-122.393323962485 37.76861086469489)'), {u'source': u'openstreetmap.org', u'amenity': u'recycling', u'recycling:cans': u'yes', u'recycling:glass_bottles': u'yes', u'recycling_type': u'container'}))  # noqa

        self.assert_no_matching_feature(
            15, 5243, 12666, 'pois',
            {'id': 2338524067})

        self.assert_has_feature(
            16, 10486, 25332, 'pois',
            {'id': 2338524067})

    def test_amenity_shelter(self):
        self.generate_fixtures(dsl.way(4177497032, wkt_loads('POINT (-122.311415934205 37.46932756965568)'), {u'source': u'openstreetmap.org', u'amenity': u'shelter'}))  # noqa

        self.assert_no_matching_feature(
            15, 5250, 12700, 'pois',
            {'id': 4177497032})

        self.assert_has_feature(
            16, 10501, 25401, 'pois',
            {'id': 4177497032})

    def test_amenity_telephone(self):
        self.generate_fixtures(dsl.way(1241673617, wkt_loads('POINT (-122.41955530777 37.728945000824)'), {u'source': u'openstreetmap.org', u'amenity': u'telephone'}))  # noqa

        self.assert_no_matching_feature(
            15, 5241, 12670, 'pois',
            {'id': 1241673617})

        self.assert_has_feature(
            16, 10482, 25341, 'pois',
            {'id': 1241673617})

    def test_amenity_waste_basket(self):
        self.generate_fixtures(dsl.way(4265260145, wkt_loads('POINT (-122.42732762144 37.71532200949959)'), {u'source': u'openstreetmap.org', u'amenity': u'waste_basket'}))  # noqa

        self.assert_no_matching_feature(
            15, 5240, 12672, 'pois',
            {'id': 4265260145})

        self.assert_has_feature(
            16, 10480, 25344, 'pois',
            {'id': 4265260145})

    def test_highway_bus_stop(self):
        self.generate_fixtures(dsl.way(1229920715, wkt_loads('POINT (-122.440825437405 37.71656217534681)'), {u'shelter': u'yes', u'operator': u'San Francisco Municipal Railway', u'highway': u'bus_stop', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_no_matching_feature(
            15, 5239, 12672, 'pois',
            {'id': 1229920715})

        self.assert_has_feature(
            16, 10478, 25344, 'pois',
            {'id': 1229920715})

    def test_highway_ford(self):
        self.generate_fixtures(dsl.way(880807552, wkt_loads('POINT (-116.640567231058 33.8116118211803)'), {u'source': u'openstreetmap.org', u'highway': u'ford'}))  # noqa

        self.assert_no_matching_feature(
            15, 5767, 13110, 'pois',
            {'id': 880807552})

        self.assert_has_feature(
            16, 11534, 26220, 'pois',
            {'id': 880807552})

    def test_highway_mini_roundabout(self):
        self.generate_fixtures(dsl.way(110392851, wkt_loads('POINT (-122.5540299617 37.9050195779691)'), {u'source': u'openstreetmap.org', u'highway': u'mini_roundabout'}))  # noqa

        self.assert_has_feature(
            16, 10457, 25301, 'pois',
            {'id': 110392851})

    def test_highway_platform(self):
        self.generate_fixtures(dsl.way(1275126569, wkt_loads('POINT (-97.16498299553459 49.8269494712567)'), {u'source': u'openstreetmap.org', u'public_transport': u'platform', u'highway': u'platform'}))  # noqa

        self.assert_no_matching_feature(
            15, 7539, 11137, 'pois',
            {'id': 1275126569})

        self.assert_has_feature(
            16, 15079, 22275, 'pois',
            {'id': 1275126569})

    def test_highway_traffic_signals(self):
        self.generate_fixtures(dsl.way(65329980, wkt_loads('POINT (-122.400508777959 37.78745527542809)'), {u'source': u'openstreetmap.org', u'traffic_signals:sound': u'yes', u'highway': u'traffic_signals'}))  # noqa

        self.assert_no_matching_feature(
            15, 5242, 12664, 'pois',
            {'id': 65329980})

        self.assert_has_feature(
            16, 10485, 25328, 'pois',
            {'id': 65329980})

    def test_waterway_lock(self):
        self.generate_fixtures(dsl.way(675426915, wkt_loads('POINT (-76.73183940324068 39.8905935773763)'), {u'source': u'openstreetmap.org', u'waterway': u'lock'}))  # noqa

        self.assert_has_feature(
            15, 9399, 12418, 'pois',
            {'id': 675426915})

    def test_landuse_quarry(self):
        self.generate_fixtures(dsl.way(3356570361, wkt_loads('POINT (-122.153005130541 38.21004035449701)'), {u'source': u'openstreetmap.org', u'landuse': u'quarry', u'resource': u'rock'}))  # noqa

        self.assert_has_feature(
            16, 10530, 25230, 'pois',
            {'id': 3356570361})

        # Way:184367568 quarry in POIS
        self.generate_fixtures(dsl.way(184367568, wkt_loads('POLYGON ((-120.977489333016 37.75803770943879, -120.977486997396 37.76081756655368, -120.976233937406 37.76077552360858, -120.975400929643 37.7607743873124, -120.974583372903 37.76077332203479, -120.973504316584 37.76062567440368, -120.97213699089 37.76035516386188, -120.971016971394 37.7601061001177, -120.970661597867 37.7599816034407, -120.97063294161 37.75963545470499, -120.970616682103 37.7594398664594, -120.970625485593 37.75941607482559, -120.970835242212 37.75885182025329, -120.970928667001 37.7585999816441, -120.971144981322 37.75855530967489, -120.971802368447 37.75841951808628, -120.971967209301 37.7582608575149, -120.9720635087 37.75745135660739, -120.971951219289 37.75722600441009, -120.972019042093 37.75718296511631, -120.972093961588 37.75713530936738, -120.972331386317 37.7569844584784, -120.972452838544 37.75689695914001, -120.972641574585 37.75557287981598, -120.972647683129 37.75482471444889, -120.975799062977 37.75418158732738, -120.975874970619 37.75416880285528, -120.976019329885 37.7541445833771, -120.976370571161 37.75533779164638, -120.976515469416 37.75582998445129, -120.976667733857 37.7561338213188, -120.976875693845 37.75641066831778, -120.97701762766 37.7564229552437, -120.977076287648 37.75642806887698, -120.977279396734 37.75644568250009, -120.977288110392 37.75651152048169, -120.977319461596 37.7567493747943, -120.977408125314 37.75742181157429, -120.977429145892 37.7575811841611, -120.977489333016 37.75803770943879))'), {u'attribution': u'Farmland Mapping and Monitoring Program', u'way_area': u'508870', u'source': u'openstreetmap.org', u'FMMP_modified': u'no', u'addr:county': u'San Joaquin', u'landuse': u'quarry', u'FMMP_reviewed': u'no'}))  # noqa

        self.assert_has_feature(
            14, 2686, 6333, 'pois',
            {'id': 184367568, 'min_zoom': 13})

    def test_leisure_dog_park(self):
        self.generate_fixtures(dsl.way(1229112075, wkt_loads('POINT (-122.484834531995 37.73619356828728)'), {u'source': u'openstreetmap.org', u'leisure': u'dog_park'}))  # noqa

        self.assert_no_matching_feature(
            15, 5235, 12669, 'pois',
            {'id': 1229112075})

        self.assert_has_feature(
            16, 10470, 25339, 'pois',
            {'id': 1229112075})

    def test_leisure_slipway(self):
        self.generate_fixtures(dsl.way(2678961627, wkt_loads('POINT (-122.445884120264 37.8895429070418)'), {u'source': u'openstreetmap.org', u'leisure': u'slipway'}))  # noqa

        self.assert_no_matching_feature(
            15, 5238, 12652, 'pois',
            {'id': 2678961627})

        self.assert_has_feature(
            16, 10477, 25304, 'pois',
            {'id': 2678961627})

    def test_lock_equals_yes(self):
        self.generate_fixtures(dsl.way(365485771, wkt_loads('POINT (-75.3303899455737 43.4436290088519)'), {u'lock': u'yes', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_has_feature(
            15, 9527, 11985, 'pois',
            {'id': 365485771})

    def test_man_made_adit(self):
        self.generate_fixtures(dsl.way(4469596254, wkt_loads('POINT (-118.182640131111 37.19952457108968)'), {u'source': u'openstreetmap.org', u'man_made': u'adit'}))  # noqa

        self.assert_no_matching_feature(
            15, 5626, 12731, 'pois',
            {'id': 4469596254})

        self.assert_has_feature(
            16, 11253, 25463, 'pois',
            {'id': 4469596254})

    def test_man_made_mineshaft(self):
        self.generate_fixtures(dsl.way(1818064871, wkt_loads('POINT (-120.913070335508 38.27814640347291)'), {u'source': u'openstreetmap.org', u'man_made': u'mineshaft'}))  # noqa

        self.assert_has_feature(
            15, 5378, 12607, 'pois',
            {'id': 1818064871})

    def test_man_made_offshore_platform(self):
        self.generate_fixtures(dsl.way(4239915448, wkt_loads('POINT (-97.05473509633438 26.12074297830959)'), {u'seamark:type': u'platform', u'man_made': u'offshore_platform', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_has_feature(
            15, 7549, 13919, 'pois',
            {'id': 4239915448})

        # originally from 675-man_made-outdoor-landmarks.py
        self.generate_fixtures(dsl.way(350328482, wkt_loads('POLYGON ((-94.63139900237969 29.40923572279329, -94.63116238613378 29.40925700824868, -94.6311144160976 29.4088532881355, -94.6313510323435 29.40883200259559, -94.63139900237969 29.40923572279329))'), {u'source': u'openstreetmap.org', u'way_area': u'1373.41', u'man_made': u'offshore_platform', u'area': u'yes'}))  # noqa

        self.assert_has_feature(
            13, 1942, 3395, 'pois',
            {'id': 350328482})

    def test_man_made_telescope(self):
        self.generate_fixtures(dsl.way(3310910810, wkt_loads('POINT (-121.395510109687 39.10727370706238)'), {u'source': u'openstreetmap.org', u'man_made': u'telescope'}))  # noqa

        self.assert_has_feature(
            16, 10668, 25021, 'pois',
            {'id': 3310910810})

    def test_natural_cave_entrance(self):
        self.generate_fixtures(dsl.way(1050825518, wkt_loads('POINT (-123.103027083089 40.4949267064782)'), {u'source': u'openstreetmap.org', u'natural': u'cave_entrance'}))  # noqa

        self.assert_has_feature(
            15, 5178, 12346, 'pois',
            {'id': 1050825518})

    def test_natural_waterfall(self):
        self.generate_fixtures(dsl.way(4719786091, wkt_loads('POINT (-119.666994028371 37.52010386695389)'), {u'source': u'openstreetmap.org', u'natural': u'waterfall'}))  # noqa

        self.assert_has_feature(
            15, 5491, 12694, 'pois',
            {'id': 4719786091})

    def test_public_transportation_platform(self):
        self.generate_fixtures(dsl.way(2073000913, wkt_loads('POINT (-122.4514815228 37.72302879364989)'), {u'source': u'openstreetmap.org', u'public_transport': u'platform'}))  # noqa

        self.assert_has_feature(
            16, 10476, 25342, 'pois',
            {'id': 2073000913, 'min_zoom': 17})

    def test_public_transport_stop_area(self):
        self.generate_fixtures(dsl.way(2991866242, wkt_loads('POINT (-122.714192210673 38.43852797107748)'), {u'source': u'openstreetmap.org', u'public_transport': u'stop_area'}))  # noqa

        self.assert_has_feature(
            15, 5214, 12588, 'pois',
            {'id': 2991866242})

    def test_railway_halt(self):
        self.generate_fixtures(dsl.way(2382580308, wkt_loads('POINT (-75.130406997023 40.30634839166561)'), {u'source': u'openstreetmap.org', u'railway': u'halt'}))  # noqa

        self.assert_has_feature(
            16, 19090, 24737, 'pois',
            {'id': 2382580308, 'kind': 'halt', 'min_zoom': 16})

    def test_railway_platform(self):
        self.generate_fixtures(dsl.way(3987143106, wkt_loads('POINT (-72.0929836528225 41.354925008914)'), {u'source': u'openstreetmap.org', u'railway': u'platform'}))  # noqa

        self.assert_has_feature(
            16, 19643, 24485, 'pois',
            {'id': 3987143106, 'min_zoom': 17})

    def test_railway_stop(self):
        self.generate_fixtures(dsl.way(1130268570, wkt_loads('POINT (-76.9349771452377 38.9629633645972)'), {u'source': u'openstreetmap.org', u'railway': u'stop', u'rail': u'yes', u'public_transport': u'stop_position'}))  # noqa

        self.assert_has_feature(
            16, 18762, 25055, 'pois',
            {'id': 1130268570, 'kind': 'stop', 'min_zoom': 16})

    def test_public_transport_stop_position(self):
        # originally from 661-historic-transit-stops.py
        self.generate_fixtures(dsl.way(3721890342, wkt_loads('POINT (-122.15620591773 37.438295280187)'), {u'source': u'openstreetmap.org', u'railway': u'stop', u'network': u'Caltrain', u'public_transport': u'stop_position'}))  # noqa

        self.assert_has_feature(
            16, 10530, 25408, 'pois',
            {'id': 3721890342, 'kind': 'stop', 'min_zoom': 16})

    def test_railway_subway_entrance(self):
        self.generate_fixtures(dsl.way(3833748147, wkt_loads('POINT (-77.08494522253518 38.89059997067759)'), {u'source': u'openstreetmap.org', u'railway': u'subway_entrance', u'highway': u'elevator', u'subway_entrance': u'elevator'}))  # noqa

        self.assert_no_matching_feature(
            15, 9367, 12536, 'pois',
            {'id': 3833748147})

        self.assert_has_feature(
            16, 18735, 25072, 'pois',
            {'id': 3833748147})

    def test_railway_tram_stop(self):
        self.generate_fixtures(dsl.way(1719012916, wkt_loads('POINT (-122.433744377346 37.73245189929369)'), {u'source': u'openstreetmap.org', u'railway': u'tram_stop'}))  # noqa

        self.assert_has_feature(
            16, 10479, 25340, 'pois',
            {'id': 1719012916})

    def test_railway_level_crossing(self):
        # railway=level_crossing (but make min_zoom 18)
        self.generate_fixtures(dsl.way(4665711307, wkt_loads('POINT (-122.481302715623 37.76153108566229)'), {u'source': u'openstreetmap.org', u'railway': u'level_crossing'}))  # noqa

        self.assert_no_matching_feature(
            15, 5235, 12667, 'pois',
            {'id': 4665711307})

        self.assert_has_feature(
            16, 10470, 25334, 'pois',
            {'id': 4665711307, 'min_zoom': 18})

    def test_whitewater_egress(self):
        self.generate_fixtures(dsl.way(4696619992, wkt_loads('POINT (-121.09051042133 39.52623636932159)'), {u'source': u'openstreetmap.org', u'whitewater': u'egress'}))  # noqa

        self.assert_has_feature(
            15, 5362, 12461, 'pois',
            {'id': 4696619992})

    def test_whitewater_hazard(self):
        self.generate_fixtures(dsl.way(4253919482, wkt_loads('POINT (-120.81567068049 39.35411416109648)'), {u'source': u'openstreetmap.org', u'whitewater': u'hazard'}))  # noqa

        self.assert_has_feature(
            15, 5387, 12481, 'pois',
            {'id': 4253919482})

    def test_whitewater_put_in(self):
        self.generate_fixtures(dsl.way(3688927027, wkt_loads('POINT (-119.124603746402 37.76938125886009)'), {u'source': u'openstreetmap.org', u'whitewater': u'put_in'}))  # noqa

        self.assert_has_feature(
            15, 5541, 12666, 'pois',
            {'id': 3688927027})

    def test_whitewater_rapid(self):
        self.generate_fixtures(dsl.way(4253919493, wkt_loads('POINT (-120.834653519748 39.34707548323009)'), {u'source': u'openstreetmap.org', u'whitewater': u'rapid'}))  # noqa

        self.assert_has_feature(
            15, 5385, 12482, 'pois',
            {'id': 4253919493})

    def test_tourism_alpine_hut(self):
        self.generate_fixtures(dsl.way(1076123765, wkt_loads('POINT (-120.307545467224 38.2791421939092)'), {u'source': u'openstreetmap.org', u'tourism': u'alpine_hut'}))  # noqa

        self.assert_has_feature(
            13, 1358, 3151, 'pois',
            {'id': 1076123765})

    def test_tourism_viewpoint(self):
        self.generate_fixtures(dsl.way(3065529317, wkt_loads('POINT (-122.471829980952 37.75635995809319)'), {u'source': u'openstreetmap.org', u'tourism': u'viewpoint'}))  # noqa

        self.assert_has_feature(
            15, 5236, 12667, 'pois',
            {'id': 3065529317})

    def test_tourism_wilderness_hut(self):
        self.generate_fixtures(dsl.way(1837443430, wkt_loads('POINT (7.870578222703659 46.70642388658409)'), {u'source': u'openstreetmap.org', u'tourism': u'wilderness_hut'}))  # noqa

        self.assert_has_feature(
            15, 17100, 11564, 'pois',
            {'id': 1837443430})

    def test_waterway_waterfall(self):
        self.generate_fixtures(dsl.way(4319935813, wkt_loads('POINT (-120.133715441035 38.96975429223278)'), {u'source': u'openstreetmap.org', u'waterway': u'waterfall'}))  # noqa

        self.assert_has_feature(
            15, 5449, 12526, 'pois',
            {'id': 4319935813})

    def test_tourism_information(self):
        # originally from 927-normalize-operator-values.py
        # information=guidepost
        # operator=US Forest Service
        # tourism=information
        # https://www.openstreetmap.org/node/4216584100
        self.generate_fixtures(dsl.way(4216584100, wkt_loads('POINT (-92.13653293695938 38.81105677254989)'), {u'operator': u'US Forest Service', u'information': u'guidepost', u'tourism': u'information', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_has_feature(
            16, 15995, 25090, 'pois',
            {'id': 4216584100})

    def test_unnamed_rock(self):
        # originally from 657-natural-man_made.py
        # unnamed rock
        self.generate_fixtures(dsl.way(4013703516, wkt_loads('POINT (-122.523488499681 38.0215078752183)'), {u'source': u'openstreetmap.org', u'natural': u'rock'}))  # noqa

        self.assert_has_feature(
            16, 10463, 25274, 'pois',
            {'id': 4013703516})

        # another unnamed rock
        self.generate_fixtures(dsl.way(3150154140, wkt_loads('POINT (-122.416442645311 37.93267727336828)'), {u'source': u'openstreetmap.org', u'natural': u'rock'}))  # noqa

        self.assert_has_feature(
            16, 10482, 25294, 'pois',
            {'id': 3150154140})
