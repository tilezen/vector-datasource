from . import FixtureTest
import dsl
from shapely.wkt import loads as wkt_loads


class AddHikingRoutes(FixtureTest):
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
        self.generate_fixtures(
            dsl.way(5260896, dsl.tile_diagonal(11, 331, 706), {
                'source': 'openstreetmap.org',
                'highway': 'residential',
                'name': 'Baker River Road'
            }),
            dsl.relation(5260896, {
                'source': 'openstreetmap.org',
                'type': 'route',
                'route': 'hiking',
                'network': 'nwn',
                'ref': 'PNT',
                'name': 'Pacific Northwest Trail 03 Washington',
                'wikidata': 'Q3360192',
                'symbol': 'totem on yellow background'
            }, ways=[3718820]),
        )

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
        self.generate_fixtures(
            dsl.way(6671321, dsl.tile_diagonal(11, 514, 751), {
                'source': 'openstreetmap.org',
                'highway': 'service',
                'access': 'private',
                'tiger:name_base': 'Matz',
                'tiger:cfcc': 'A74',
                'tiger:county': 'Polk, IA',
                'tiger:reviewed': 'no'
            }),
            dsl.relation(2381423, {
                'source': 'openstreetmap.org',
                'type': 'route',
                'route': 'hiking',
                'network': 'nwn',
                'ref': 'ADT',
                'name': 'American Discovery Trail',
                'operator': 'American Discovery Trail Society'
            }, ways=[6671321]),
        )

        self.assert_has_feature(
            11, 514, 751, 'roads',
            {'kind': 'minor_road', 'kind_detail': 'service',
             'walking_network': 'nwn'})

    def test_driveway_nwn(self):
        # Dogbane - service=driveway - part of American Discovery Trail
        # (nwn)
        # should be visible at z11
        self.generate_fixtures(
            dsl.way(16000421, wkt_loads('LineString (-93.68584719999999777 41.74244529999999997, -93.6859489999999937 41.74249919999999747, -93.68607550000000117 41.74251509999999854, -93.68619499999999789 41.74251499999999737, -93.68646250000000464 41.74245650000000296, -93.68669930000000079 41.74234510000000142, -93.68697509999999795 41.7422196999999997, -93.6872615000000053 41.74211700000000036, -93.68774890000000255 41.7419809000000015)'), {
                'source': 'openstreetmap.org',
                'highway': 'service',
                'oneway': 'yes',
                'service': 'driveway',
                'tiger:cfcc': 'A74',
                'tiger:county': 'Polk, IA'
            }),
            dsl.relation(1544944, {
                'source': 'openstreetmap.org',
                'type': 'route',
                'route': 'hiking',
                'network': 'nwn',
                'ref': 'ADT',
                'name': 'American Discovery Trail',
                'operator': 'American Discovery Trail Society'
            }, ways=[16000421])
        )

        self.assert_has_feature(
            11, 491, 762, 'roads',
            {'kind': 'minor_road', 'kind_detail': 'service',
             'service': 'driveway', 'walking_network': 'nwn'})
