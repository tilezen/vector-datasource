from . import FixtureTest


class PoniWhitelist(FixtureTest):

    def test_aeroway_helipad(self):
        # aeroway=helipad
        # min_zoom: 16
        self.load_fixtures(['https://www.openstreetmap.org/node/2207370738'])

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
        self.load_fixtures(['https://www.openstreetmap.org/node/4113423533'])

        self.assert_no_matching_feature(
            15, 5242, 12668, 'pois',
            {'id': 4113423533})

        self.assert_has_feature(
            16, 10481, 25337, 'pois',
            {'id': 4113423533})

    def test_amenity_bench(self):
        # min_zoom: 18
        self.load_fixtures(['https://www.openstreetmap.org/node/3951215438'])

        # self.assert_no_matching_feature(
        #     15, 5239, 12672, 'pois',
        #     {'id': 3951215438})

        self.assert_has_feature(
            16, 10479, 25345, 'pois',
            {'id': 3951215438})

    def test_amenity_bicycle_rental(self):
        # when operator: false, then min_zoom: 16
        # when operator: true, then min_zoom: 17
        self.load_fixtures(['https://www.openstreetmap.org/node/3509468129'])

        self.assert_no_matching_feature(
            15, 5251, 12655, 'pois',
            {'id': 3509468129})

        self.assert_has_feature(
            16, 10503, 25310, 'pois',
            {'id': 3509468129})

    def test_amenity_car_sharing(self):
        # min_zoom: 16
        self.load_fixtures(['https://www.openstreetmap.org/node/4758733421'])

        self.assert_no_matching_feature(
            15, 5266, 12706, 'pois',
            {'id': 4758733421})

        self.assert_has_feature(
            16, 10532, 25412, 'pois',
            {'id': 4758733421})

    def test_amenity_fuel(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/2059530671'])

        self.assert_no_matching_feature(
            15, 5239, 12671, 'pois',
            {'id': 2059530671})

        self.assert_has_feature(
            16, 10478, 25342, 'pois',
            {'id': 2059530671})

    def test_amenity_post_box(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/4397690695'])

        self.assert_no_matching_feature(
            15, 5239, 12672, 'pois',
            {'id': 4397690695})

        self.assert_has_feature(
            16, 10478, 25344, 'pois',
            {'id': 4397690695})

    def test_amenity_recycling(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/2338524067'])

        self.assert_no_matching_feature(
            15, 5243, 12666, 'pois',
            {'id': 2338524067})

        self.assert_has_feature(
            16, 10486, 25332, 'pois',
            {'id': 2338524067})

    def test_amenity_shelter(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/4177497032'])

        self.assert_no_matching_feature(
            15, 5250, 12700, 'pois',
            {'id': 4177497032})

        self.assert_has_feature(
            16, 10501, 25401, 'pois',
            {'id': 4177497032})

    def test_amenity_telephone(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/1241673617'])

        self.assert_no_matching_feature(
            15, 5241, 12670, 'pois',
            {'id': 1241673617})

        self.assert_has_feature(
            16, 10482, 25341, 'pois',
            {'id': 1241673617})

    def test_amenity_waste_basket(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/4265260145'])

        self.assert_no_matching_feature(
            15, 5240, 12672, 'pois',
            {'id': 4265260145})

        self.assert_has_feature(
            16, 10480, 25344, 'pois',
            {'id': 4265260145})

    def test_highway_bus_stop(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/1229920715'])

        self.assert_no_matching_feature(
            15, 5239, 12672, 'pois',
            {'id': 1229920715})

        self.assert_has_feature(
            16, 10478, 25344, 'pois',
            {'id': 1229920715})

    def test_highway_ford(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/880807552'])

        self.assert_no_matching_feature(
            15, 5767, 13110, 'pois',
            {'id': 880807552})

        self.assert_has_feature(
            16, 11534, 26220, 'pois',
            {'id': 880807552})

    def test_highway_mini_roundabout(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/110392851'])

        self.assert_has_feature(
            15, 5228, 12650, 'pois',
            {'id': 110392851})

    def test_highway_platform(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/1275126569'])

        self.assert_no_matching_feature(
            15, 7539, 11137, 'pois',
            {'id': 1275126569})

        self.assert_has_feature(
            16, 15079, 22275, 'pois',
            {'id': 1275126569})

    def test_highway_traffic_signals(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/65329980'])

        self.assert_no_matching_feature(
            15, 5242, 12664, 'pois',
            {'id': 65329980})

        self.assert_has_feature(
            16, 10485, 25328, 'pois',
            {'id': 65329980})

    def test_waterway_lock(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/675426915'])

        self.assert_has_feature(
            15, 9399, 12418, 'pois',
            {'id': 675426915})

    def test_landuse_quarry(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/3356570361'])

        self.assert_has_feature(
            15, 5265, 12615, 'pois',
            {'id': 3356570361})

        # Way:184367568 quarry in POIS
        self.load_fixtures(['https://www.openstreetmap.org/way/184367568'])

        self.assert_has_feature(
            12, 671, 1583, 'pois',
            {'id': 184367568})

    def test_leisure_dog_park(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/1229112075'])

        self.assert_no_matching_feature(
            15, 5235, 12669, 'pois',
            {'id': 1229112075})

        self.assert_has_feature(
            16, 10470, 25339, 'pois',
            {'id': 1229112075})

    def test_leisure_slipway(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/2678961627'])

        self.assert_no_matching_feature(
            15, 5238, 12652, 'pois',
            {'id': 2678961627})

        self.assert_has_feature(
            16, 10477, 25304, 'pois',
            {'id': 2678961627})

    def test_lock_equals_yes(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/365485771'])

        self.assert_has_feature(
            15, 9527, 11985, 'pois',
            {'id': 365485771})

    def test_man_made_adit(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/4469596254'])

        self.assert_no_matching_feature(
            15, 5626, 12731, 'pois',
            {'id': 4469596254})

        self.assert_has_feature(
            16, 11253, 25463, 'pois',
            {'id': 4469596254})

    def test_man_made_mineshaft(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/1818064871'])

        self.assert_has_feature(
            15, 5378, 12607, 'pois',
            {'id': 1818064871})

    def test_man_made_offshore_platform(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/4239915448'])

        self.assert_has_feature(
            15, 7549, 13919, 'pois',
            {'id': 4239915448})

        # originally from 675-man_made-outdoor-landmarks.py
        self.load_fixtures(['https://www.openstreetmap.org/way/350328482'])

        self.assert_has_feature(
            13, 1942, 3395, 'pois',
            {'id': 350328482})

    def test_man_made_telescope(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/3310910810'])

        self.assert_has_feature(
            16, 10668, 25021, 'pois',
            {'id': 3310910810})

    def test_natural_cave_entrance(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/1050825518'])

        self.assert_has_feature(
            15, 5178, 12346, 'pois',
            {'id': 1050825518})

    def test_natural_waterfall(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/4719786091'])

        self.assert_has_feature(
            15, 5491, 12694, 'pois',
            {'id': 4719786091})

    def test_public_transportation_platform(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/2073000913'])

        self.assert_has_feature(
            15, 5238, 12671, 'pois',
            {'id': 2073000913})

    def test_public_transport_stop_area(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/2991866242'])

        self.assert_has_feature(
            15, 5214, 12588, 'pois',
            {'id': 2991866242})

    def test_railway_halt(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/2382580308'])

        self.assert_has_feature(
            15, 9545, 12368, 'pois',
            {'id': 2382580308})

    def test_railway_platform(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/3987143106'])

        self.assert_has_feature(
            15, 9821, 12242, 'pois',
            {'id': 3987143106})

    def test_railway_stop(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/1130268570'])

        self.assert_has_feature(
            15, 9381, 12527, 'pois',
            {'id': 1130268570})

    def test_public_transport_stop_position(self):
        # originally from 661-historic-transit-stops.py
        self.load_fixtures(['https://www.openstreetmap.org/node/3721890342'])

        self.assert_has_feature(
            13, 1316, 3176, 'pois',
            {'id': 3721890342})

    def test_railway_subway_entrance(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/3833748147'])

        self.assert_no_matching_feature(
            15, 9367, 12536, 'pois',
            {'id': 3833748147})

        self.assert_has_feature(
            16, 18735, 25072, 'pois',
            {'id': 3833748147})

    def test_railway_tram_stop(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/1719012916'])

        self.assert_has_feature(
            15, 5239, 12670, 'pois',
            {'id': 1719012916})

    def test_railway_level_crossing(self):
        # railway=level_crossing (but make min_zoom 18)
        self.load_fixtures(['https://www.openstreetmap.org/node/4665711307'])

        self.assert_no_matching_feature(
            15, 5235, 12667, 'pois',
            {'id': 4665711307})

        self.assert_has_feature(
            16, 10470, 25334, 'pois',
            {'id': 4665711307, 'min_zoom': 18})

    def test_whitewater_egress(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/4696619992'])

        self.assert_has_feature(
            15, 5362, 12461, 'pois',
            {'id': 4696619992})

    def test_whitewater_hazard(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/4253919482'])

        self.assert_has_feature(
            15, 5387, 12481, 'pois',
            {'id': 4253919482})

    def test_whitewater_put_in(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/3688927027'])

        self.assert_has_feature(
            15, 5541, 12666, 'pois',
            {'id': 3688927027})

    def test_whitewater_rapid(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/4253919493'])

        self.assert_has_feature(
            15, 5385, 12482, 'pois',
            {'id': 4253919493})

    def test_tourism_alpine_hut(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/1076123765'])

        self.assert_has_feature(
            13, 1358, 3151, 'pois',
            {'id': 1076123765})

    def test_tourism_viewpoint(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/3065529317'])

        self.assert_has_feature(
            15, 5236, 12667, 'pois',
            {'id': 3065529317})

    def test_tourism_wilderness_hut(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/1837443430'])

        self.assert_has_feature(
            15, 17100, 11564, 'pois',
            {'id': 1837443430})

    def test_waterway_waterfall(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/4319935813'])

        self.assert_has_feature(
            15, 5449, 12526, 'pois',
            {'id': 4319935813})

    def test_tourism_information(self):
        # originally from 927-normalize-operator-values.py
        # information=guidepost
        # operator=US Forest Service
        # tourism=information
        # https://www.openstreetmap.org/node/4216584100
        self.load_fixtures(['https://www.openstreetmap.org/node/4216584100'])

        self.assert_has_feature(
            16, 15995, 25090, 'pois',
            {'id': 4216584100})

    def test_unnamed_rock(self):
        # originally from 657-natural-man_made.py
        # unnamed rock
        self.load_fixtures(['https://www.openstreetmap.org/node/4013703516'])

        self.assert_has_feature(
            16, 10463, 25274, 'pois',
            {'id': 4013703516})

        # another unnamed rock
        self.load_fixtures(['https://www.openstreetmap.org/node/3150154140'])

        self.assert_has_feature(
            16, 10482, 25294, 'pois',
            {'id': 3150154140})
