# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class NormalizeNeRoads(FixtureTest):

    def setUp(self):
        super(NormalizeNeRoads, self).setUp()
        self.generate_fixtures(dsl.way(1, wkt_loads('LINESTRING (-100.5054284631781 42.80752930679844, -100.5349505695172 42.78842676740254, -100.5401603529888 42.63734304672585, -100.5366871640077 42.52793759382202, -100.5453701364604 42.36122452273048, -100.528004191555 42.32996582190082, -100.5332139750267 42.25181906982666, -100.5262675970645 42.1788821012241, -100.5401603529888 42.10073534914997, -100.5418969474793 41.98264692379346, -100.5575262978942 41.98091032930294, -100.5540531089131 41.93923206153004, -100.5627360813658 41.89929038824769, -100.5575262978942 41.85761212047482, -100.547106730951 41.8385095810789, -100.5436335419699 41.81072406923032, -100.5262675970645 41.77425558492903, -100.5227944080834 41.75167985655206, -100.5089016521591 41.73257731715616, -100.5141114356308 41.68568926591165, -100.501955274197 41.65443056508201, -100.4897991127632 41.60059613587535, -100.5002186797065 41.54502511217819, -100.5036918686875 41.44603922621758, -100.5002186797065 41.42172690335006, -100.5592628923847 41.37136566312452, -100.6113607271008 41.31926782840839, -100.6287266720062 41.31058485595572, -100.6513024003832 41.27585296614499, -100.6773513177412 41.24633085980587, -100.7086100185709 41.2202819424478, -100.7485516918533 41.19770621407083, -100.7711274202302 41.1021935170913)'), {u'labelrank': 0, u'length_km': 164, u'scalerank': 7, u'min_zoom': 7, u'prefix': u'', u'continent': u'North America', u'namealtt': u'', u'localalt': u'', u'question': 0, u'sov_a3': u'USA', u'label': u'', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'ne_1d4_original', u'toll': 0, u'expressway': 0, u'local': u'', u'edited': u'Version 1.5: Changed alignment, a few adds in N.A.', u'label2': u'', u'orig_fid': 0, u'namealt': u'', u'uident': 108105, u'featurecla': u'Road', u'rwdb_rd_id': 0, u'name': u'83', u'level': u'Federal', u'type': u'Secondary Highway', u'routeraw': u'', u'ignore': 0, u'add': 0, u'localtype': u''}),dsl.way(2, wkt_loads('LINESTRING (-75.11641701152996 38.78383987222464, -75.10426085009621 38.82725473448809, -75.07300214926653 38.87240619124203, -75.01743112556937 38.93145040392029, -74.9670698853438 38.96965548271211)'), {u'labelrank': 0, u'length_km': 24, u'scalerank': 6, u'min_zoom': 6, u'prefix': u'', u'continent': u'North America', u'namealtt': u'', u'localalt': u'', u'question': 0, u'sov_a3': u'USA', u'label': u'', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'ne_1d4_original', u'toll': 0, u'expressway': 0, u'local': u'', u'edited': u'Version 1.5: Changed alignment, a few adds in N.A.', u'label2': u'', u'orig_fid': 0, u'namealt': u'', u'uident': 99905, u'featurecla': u'Ferry', u'rwdb_rd_id': 0, u'name': u'', u'level': u'Other', u'type': u'Ferry Route', u'routeraw': u'', u'ignore': 0, u'add': 0, u'localtype': u''}),dsl.way(3, wkt_loads('LINESTRING (-75.09557787764351 39.83621613348997, -75.10252425560566 39.82405997205621, -75.11641701152996 39.77717192081172, -75.14072933439746 39.73723024752937, -75.14072933439746 39.67992262934167, -75.10947063356781 39.62956138911607, -75.07473874375708 39.58614652685267, -75.06084598783279 39.55488782602301, -75.07473874375708 39.49237042436369, -75.07126555477602 39.46284831802453, -75.0573727988517 39.42985302270436, -75.01395793658828 39.40554069983683, -75.00874815311667 39.36559902655448, -74.98617242473971 39.32218416429109, -74.9340745900236 39.26487654610337, -74.89413291674127 39.23188125078315, -74.84203508202513 39.19888595546297, -74.82293254262923 39.17457363259542, -74.78993724730904 39.16936384912383, -74.7690981134226 39.15547109319954, -74.75694195198885 39.15547109319954)'), {u'labelrank': 0, u'length_km': 83, u'scalerank': 7, u'min_zoom': 7, u'prefix': u'', u'continent': u'North America', u'namealtt': u'', u'localalt': u'', u'question': 0, u'sov_a3': u'USA', u'label': u'', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'ne_1d4_original', u'toll': 0, u'expressway': 1, u'local': u'', u'edited': u'Version 1.5: Changed alignment, a few adds in N.A.', u'label2': u'', u'orig_fid': 0, u'namealt': u'', u'uident': 94705, u'featurecla': u'Road', u'rwdb_rd_id': 0, u'name': u'55', u'level': u'State', u'type': u'Major Highway', u'routeraw': u'', u'ignore': 0, u'add': 0, u'localtype': u''}),dsl.way(4, wkt_loads('LINESTRING (-82.56988056491396 35.59545238759908, -82.55077802551806 35.60413536005177, -82.53341208061268 35.60066217107068, -82.52646570265051 35.58676941514639, -82.49520700182087 35.56245709227888)'), {u'labelrank': 0, u'length_km': 10, u'scalerank': 7, u'min_zoom': 7, u'prefix': u'', u'continent': u'North America', u'namealtt': u'', u'localalt': u'', u'question': 0, u'sov_a3': u'USA', u'label': u'', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'ne_1d4_original', u'toll': 0, u'expressway': 0, u'local': u'', u'edited': u'New in version 2.0.0', u'label2': u'', u'orig_fid': 0, u'namealt': u'', u'uident': 0, u'featurecla': u'Road', u'rwdb_rd_id': 0, u'name': u'240', u'level': u'Interstate', u'type': u'Bypass', u'routeraw': u'', u'ignore': 0, u'add': 0, u'localtype': u''}),dsl.way(5, wkt_loads('LINESTRING (-94.35912354482086 39.03911689215309, -94.38393288403586 39.10858304195505, -94.38740607301692 39.15199790421845, -94.40824520690336 39.20583233342507, -94.44124050222356 39.23535443976424, -94.4487743469376 39.24665520683531)'), {u'labelrank': 0, u'length_km': 21, u'scalerank': 5, u'min_zoom': 5, u'prefix': u'', u'continent': u'North America', u'namealtt': u'', u'localalt': u'', u'question': 0, u'sov_a3': u'USA', u'label': u'', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'ne_1d4_original', u'toll': 0, u'expressway': 0, u'local': u'', u'edited': u'New in version 2.0.0', u'label2': u'', u'orig_fid': 0, u'namealt': u'', u'uident': 0, u'featurecla': u'Road', u'rwdb_rd_id': 0, u'name': u'', u'level': u'State', u'type': u'Beltway', u'routeraw': u'', u'ignore': 0, u'add': 0, u'localtype': u''}),dsl.way(6, wkt_loads('LINESTRING (22.40407277130538 37.55409412819295, 22.41284048593175 37.53496615995625, 22.41704058874676 37.51429232054456, 22.4179010264762 37.49300013266287, 22.40576739612173 37.38347661828518, 22.41615390037468 37.1658179568492)'), {u'labelrank': 7, u'length_km': 35, u'scalerank': 7, u'min_zoom': 7, u'prefix': u'E', u'continent': u'Europe', u'namealtt': u'', u'localalt': u'', u'question': 0, u'sov_a3': u'', u'label': u'E961', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'ne_europe_basic', u'toll': 0, u'expressway': 0, u'local': u'', u'edited': u'New in version 2.0.0', u'label2': u'', u'orig_fid': 0, u'namealt': u'', u'uident': 0, u'featurecla': u'Road', u'rwdb_rd_id': 0, u'name': u'961', u'level': u'E', u'type': u'Road', u'routeraw': u'E961', u'ignore': 0, u'add': 0, u'localtype': u''}),dsl.way(7, wkt_loads('LINESTRING (125.6603565283007 7.150089751544254, 125.6541117904032 7.176629887608772)'), {u'labelrank': 0, u'length_km': 3, u'scalerank': 3, u'min_zoom': 3, u'prefix': u'', u'continent': u'Asia', u'namealtt': u'', u'localalt': u'', u'question': 0, u'sov_a3': u'', u'label': u'', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'global_adds_craig', u'toll': 0, u'expressway': 0, u'local': u'', u'edited': u'New in version 2.0.0', u'label2': u'', u'orig_fid': 0, u'namealt': u'', u'uident': 0, u'featurecla': u'Road', u'rwdb_rd_id': 0, u'name': u'', u'level': u'', u'type': u'Major Highway', u'routeraw': u'', u'ignore': 0, u'add': 1, u'localtype': u''}),dsl.way(8, wkt_loads('LINESTRING (121.1500945818044 31.01279444250889, 121.1813182712921 30.93317403431531, 121.2109807763054 30.88633850008378)'), {u'labelrank': 0, u'length_km': 14, u'scalerank': 7, u'min_zoom': 7, u'prefix': u'', u'continent': u'Asia', u'namealtt': u'', u'localalt': u'', u'question': 0, u'sov_a3': u'', u'label': u'', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'global_adds_craig', u'toll': 0, u'expressway': 0, u'local': u'', u'edited': u'New in version 2.0.0', u'label2': u'', u'orig_fid': 0, u'namealt': u'', u'uident': 0, u'featurecla': u'Road', u'rwdb_rd_id': 0, u'name': u'', u'level': u'', u'type': u'Unknown', u'routeraw': u'', u'ignore': 0, u'add': 1, u'localtype': u''}),dsl.way(9, wkt_loads('LINESTRING (139.2725854403227 -17.89333791589524, 139.2808342847563 -17.87684022702805, 139.3179540847075 -17.84796927151049, 139.3591983068755 -17.8232227382097, 139.3839448401762 -17.80260062712572, 139.4334379067778 -17.76960524939137, 139.4581844400785 -17.75723198274096, 139.4911798178129 -17.73660987165698, 139.5076775066802 -17.73248544944018)'), {u'labelrank': 0, u'length_km': 32, u'scalerank': 7, u'min_zoom': 7, u'prefix': u'', u'continent': u'Oceania', u'namealtt': u'', u'localalt': u'', u'question': 0, u'sov_a3': u'', u'label': u'', u'note': u'', u'source': u'naturalearthdata.com', u'ne_part': u'global_basic', u'toll': 0, u'expressway': 0, u'local': u'', u'edited': u'New in version 2.0.0', u'label2': u'', u'orig_fid': 33622, u'namealt': u'', u'uident': 0, u'featurecla': u'Road', u'rwdb_rd_id': 66574, u'name': u'', u'level': u'', u'type': u'Track', u'routeraw': u'', u'ignore': 0, u'add': 0, u'localtype': u''}))  # noqa

    def test_ferry(self):
        # ferry
        self.assert_has_feature(
            7, 37, 48, 'roads',
            {'id': int, 'kind': 'ferry', 'type': type(None)})

    def test_expressway(self):
        # expressway
        self.assert_has_feature(
            7, 37, 48, 'roads',
            {'id': int, 'kind': 'highway', 'kind_detail': 'motorway',
             'type': type(None)})

    def test_major_highway(self):
        # major highway
        self.assert_has_feature(
            7, 108, 61, 'roads',
            {'id': int, 'kind': 'major_road', 'kind_detail': 'trunk'})

    def test_beltway(self):
        # beltway
        self.assert_has_feature(
            7, 30, 48, 'roads',
            {'id': int, 'kind': 'major_road', 'kind_detail': 'trunk'})

    def test_bypass(self):
        # bypass
        self.assert_has_feature(
            7, 34, 50, 'roads',
            {'id': int, 'kind': 'major_road', 'kind_detail': 'trunk'})

    def test_secondary_highway(self):
        # secondary highway
        self.assert_has_feature(
            7, 28, 47, 'roads',
            {'id': int, 'kind': 'major_road', 'kind_detail': 'primary'})

    def test_road(self):
        # road
        self.assert_has_feature(
            7, 71, 49, 'roads',
            {'id': int, 'kind': 'major_road', 'kind_detail': 'secondary'})

    def test_track(self):
        # track
        self.assert_has_feature(
            7, 113, 70, 'roads',
            {'id': int, 'kind': 'minor_road', 'kind_detail': 'tertiary'})

    def test_unknown(self):
        # unknown
        self.assert_has_feature(
            7, 107, 52, 'roads',
            {'id': int, 'kind': 'minor_road', 'kind_detail': 'tertiary'})
