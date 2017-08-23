from . import OsmFixtureTest


class AddHikingRoutes(OsmFixtureTest):
    def test_track(self):
        self.load_fixtures([
            'https://www.openstreetmap.org/way/12188550',
            'https://www.openstreetmap.org/relation/2684235',
        ], clip=self.tile_bbox(12, 654, 1582))

        self.assert_has_feature(
            12, 654, 1582, 'roads',
            {'kind': 'path', 'kind_detail': 'track'})

    def test_steps(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/25292070'])

        self.assert_has_feature(
            14, 2620, 6334, 'roads',
            {'kind': 'path', 'kind_detail': 'steps',
             'name': 'Esmeralda Ave.'})

    def test_footway(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/346093021'])

        self.assert_has_feature(
            15, 5235, 12671, 'roads',
            {'kind': 'path', 'kind_detail': 'footway'})

        self.load_fixtures(['http://www.openstreetmap.org/way/344205837'])

        self.assert_has_feature(
            15, 5234, 12667, 'roads',
            {'kind': 'path', 'kind_detail': 'footway'})

    def test_minor_road_nwn(self):
        # Baker River Road - residential - part of Pacific Northwest
        # Trail (nwn)
        # should be visible at z11
        self.load_fixtures([
            'http://www.openstreetmap.org/way/5260896',
            'http://www.openstreetmap.org/relation/3718820',
        ], clip=self.tile_bbox(11, 331, 706))

        self.assert_has_feature(
            11, 331, 706, 'roads',
            {'kind': 'minor_road', 'kind_detail': 'residential',
             'walking_network': 'nwn'})

    def test_major_road_nwn(self):
        # Mount Baker Highway - secondary - part of Pacific Northwest
        # Trail (nwn)
        # should be visible at z11
        self.load_fixtures([
            'http://www.openstreetmap.org/way/5254587',
            'http://www.openstreetmap.org/relation/3718820',
        ], clip=self.tile_bbox(11, 331, 704))

        self.assert_has_feature(
            11, 331, 704, 'roads',
            {'kind': 'major_road', 'kind_detail': 'secondary',
             'walking_network': 'nwn'})

    def test_unclassified_nwn(self):
        # Whiskey Bend Road - unclassified - part of Pacific Northwest
        # Trail (nwn)
        # should be visible at z11
        self.load_fixtures([
            'http://www.openstreetmap.org/way/5857215',
            'http://www.openstreetmap.org/relation/3718820',
        ], clip=self.tile_bbox(11, 320, 712))

        self.assert_has_feature(
            11, 320, 712, 'roads',
            {'kind': 'minor_road', 'kind_detail': 'unclassified',
             'walking_network': 'nwn'})

    def test_service_nwn(self):
        # Matz Road - service - part of Ice Age National Scenic Trail
        # (nwn)
        # should be visible at z11
        self.load_fixtures([
            'http://www.openstreetmap.org/way/6671321',
            'http://www.openstreetmap.org/relation/2381423',
        ], clip=self.tile_bbox(11, 514, 751))

        self.assert_has_feature(
            11, 514, 751, 'roads',
            {'kind': 'minor_road', 'kind_detail': 'service',
             'walking_network': 'nwn'})

    def test_driveway_nwn(self):
        # Dogbane - service=driveway - part of American Discovery Trail
        # (nwn)
        # should be visible at z11
        self.load_fixtures([
            'http://www.openstreetmap.org/way/16000421',
            'http://www.openstreetmap.org/relation/1544944',
        ], clip=self.tile_bbox(11, 491, 762))

        self.assert_has_feature(
            11, 491, 762, 'roads',
            {'kind': 'minor_road', 'kind_detail': 'service',
             'service': 'driveway', 'walking_network': 'nwn'})
