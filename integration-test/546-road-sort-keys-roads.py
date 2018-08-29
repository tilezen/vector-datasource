# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class RoadSortKeysRoads(FixtureTest):
    def test_motorway(self):
        # regular roads
        self.generate_fixtures(dsl.way(26765956, wkt_loads('LINESTRING (-122.47355250051 37.80545687798148, -122.473678623976 37.8055673159144, -122.473820108633 37.80569606532689, -122.47394632193 37.80581175507057, -122.474081428549 37.8059424203852, -122.474314182039 37.80619487846148)'), {u'maxspeed': u'35 mph', u'hgv:state_network': u'yes', u'name': u'Presidio Parkway', u'note:lanes': u'center lanes are reversible, so number may be different', u'hgv': u'designated', u'source:hgv:state_network': u'Caltrans http://www.dot.ca.gov/hq/traffops/trucks/truckmap/', u'oneway': u'yes', u'lanes': u'5', u'lit': u'yes', u'source': u'openstreetmap.org', u'tiger:county': u'San Francisco, CA', u'alt_name': u'Doyle Drive', u'NHS': u'STRAHNET', u'toll': u'no', u'bicycle': u'no', u'ref': u'US 101;CA 1', u'highway': u'motorway'}))  # noqa

        self.assert_has_feature(
            16, 10472, 25323, "roads",
            {"kind": "highway", "kind_detail": "motorway", "id": 26765956,
             "name": "Presidio Pkwy.", "sort_rank": 383})

    def test_trunk(self):
        self.generate_fixtures(dsl.way(65310628, wkt_loads('POINT (-122.475980826386 37.74678596946688)'), {u'source': u'openstreetmap.org', u'highway': u'traffic_signals'}),dsl.way(65316090, wkt_loads('POINT (-122.476110093955 37.74865039228589)'), {u'source': u'openstreetmap.org', u'highway': u'traffic_signals'}),dsl.way(89802409, wkt_loads('LINESTRING (-122.476110093955 37.74865039228589, -122.475980826386 37.74678596946688)'), {u'tiger:name_base': u'19th', u'bicycle': u'yes', u'maxspeed': u'30 mph', u'hgv:state_network': u'yes', u'name': u'19th Avenue', u'tiger:cfcc': u'A35', u'tiger:name_base_1': u'State Highway 1', u'hgv': u'designated', u'source:hgv:state_network': u'Caltrans http://www.dot.ca.gov/hq/traffops/trucks/truckmap/', u'source': u'openstreetmap.org', u'tiger:county': u'San Francisco, CA', u'tiger:name_type': u'Ave', u'oneway': u'yes', u'foot': u'yes', u'lanes': u'3', u'sidewalk': u'right', u'ref': u'CA 1', u'highway': u'trunk'}))  # noqa

        self.assert_has_feature(
            16, 10471, 25337, "roads",
            {"kind": "major_road", "kind_detail": "trunk", "id": 89802409,
             "name": "19th Ave.", "sort_rank": 381})

    def test_primary(self):
        self.generate_fixtures(dsl.way(1728581633, wkt_loads('POINT (-122.387479523247 37.75027625452039)'), {u'source': u'openstreetmap.org', u'railway': u'level_crossing'}),dsl.way(4501286257, wkt_loads('POINT (-122.38748563179 37.75034898775849)'), {u'source': u'openstreetmap.org', u'railway': u'level_crossing'}),dsl.way(4501286260, wkt_loads('POINT (-122.38748149954 37.75029770515069)'), {u'source': u'openstreetmap.org', u'railway': u'level_crossing'}),dsl.way(160842753, wkt_loads('LINESTRING (-122.387479523247 37.75027625452039, -122.38748149954 37.75029770515069, -122.38748563179 37.75034898775849, -122.387531266207 37.7509209071746)'), {u'tiger:name_base': u'3rd', u'maxspeed': u'30 mph', u'lanes': u'2', u'name': u'3rd Street', u'tiger:cfcc': u'A45', u'surface': u'asphalt', u'source': u'openstreetmap.org', u'tiger:county': u'San Francisco, CA', u'tiger:name_type': u'St', u'oneway': u'yes', u'highway': u'primary'}))  # noqa

        self.assert_has_feature(
            16, 10488, 25336, "roads",
            {"kind": "major_road", "kind_detail": "primary", "id": 160842753,
             "name": "3rd St.", "sort_rank": 380})

    def test_secondary(self):
        self.generate_fixtures(dsl.way(25337673, wkt_loads('LINESTRING (-122.419881845376 37.7703699989066, -122.419836570286 37.77048489185808, -122.419771622091 37.77063756144948)'), {u'tiger:name_base': u'Mission', u'lanes': u'2', u'name': u'Mission Street', u'tiger:cfcc': u'A41; A45', u'source': u'openstreetmap.org', u'tiger:county': u'San Francisco, CA', u'tiger:name_type': u'St', u'oneway': u'yes', u'highway': u'secondary', u'trolley_wire': u'yes'}))  # noqa

        self.assert_has_feature(
            16, 10482, 25332, "roads",
            {"kind": "major_road", "kind_detail": "secondary", "id": 25337673,
             "name": "Mission St.", "sort_rank": 379})

    def test_tertiary(self):
        self.generate_fixtures(dsl.way(65322629, wkt_loads('POINT (-122.40181420973 37.80231791588138)'), {u'source': u'openstreetmap.org', u'highway': u'traffic_signals'}),dsl.way(65333972, wkt_loads('POINT (-122.401067530066 37.79858441788151)'), {u'source': u'openstreetmap.org', u'turn_restrictions': u'no', u'highway': u'traffic_signals'}),dsl.way(3645272798, wkt_loads('POINT (-122.401086484518 37.79867910806588)'), {u'crossing': u'traffic_signals', u'source': u'openstreetmap.org', u'highway': u'crossing'}),dsl.way(255330035, wkt_loads('LINESTRING (-122.40181420973 37.80231791588138, -122.401629965265 37.80139227809359, -122.401535282834 37.80092366998429, -122.401443025854 37.80046322164698, -122.401257703411 37.79953521823388, -122.401086484518 37.79867910806588, -122.401067530066 37.79858441788151)'), {u'tiger:name_base': u'Battery', u'maxspeed': u'25 mph', u'lanes': u'2', u'name': u'Battery Street', u'tiger:cfcc': u'A41', u'source': u'openstreetmap.org', u'tiger:county': u'San Francisco, CA', u'tiger:name_type': u'St', u'oneway': u'yes', u'sidewalk': u'both', u'highway': u'tertiary'}))  # noqa

        self.assert_has_feature(
            16, 10485, 25324, "roads",
            {"kind": "major_road", "kind_detail": "tertiary", "id": 255330035,
             "name": "Battery St.", "sort_rank": 377})

    def test_motorway_link(self):
        self.generate_fixtures(dsl.way(8923765, wkt_loads('LINESTRING (-122.473428443169 37.70407699608489, -122.473206020305 37.7039613603699, -122.472934459594 37.70380208555869, -122.472809414107 37.70371509194299, -122.472725241965 37.70364686158469, -122.472624540821 37.70354188621288, -122.472557346838 37.70345190720449, -122.472496261399 37.70333797628118, -122.472455388053 37.70323698060007, -122.472411819762 37.70308040503929, -122.472279138594 37.70256255904468)'), {u'bicycle': u'no', u'tiger:cfcc': u'A63', u'source': u'openstreetmap.org', u'tiger:county': u'San Mateo, CA', u'oneway': u'yes', u'lanes': u'1', u'highway': u'motorway_link'}))  # noqa

        self.assert_has_feature(
            16, 10472, 25347, "roads",
            {"kind": "highway", "kind_detail": "motorway_link", "id": 8923765,
             "is_link": True, "sort_rank": 374})

    def test_residential(self):
        self.generate_fixtures(dsl.way(65325902, wkt_loads('POINT (-122.400231557862 37.71432265607909)'), {u'source': u'openstreetmap.org', u'highway': u'turning_circle'}),dsl.way(8919312, wkt_loads('LINESTRING (-122.400231557862 37.71432265607909, -122.400242337646 37.7142653792107, -122.400258417489 37.71422721829488, -122.400291924649 37.71417939276188, -122.401426946011 37.71302595662628, -122.401543906661 37.7129330044265, -122.401691859188 37.71285597055789, -122.401931889032 37.7127569776553, -122.402171290055 37.7126810095736)'), {u'name': u'Racine Lane', u'tiger:reviewed': u'no', u'source': u'openstreetmap.org', u'tiger:county': u'San Francisco, CA', u'tiger:name_type': u'Ln', u'highway': u'residential'}))  # noqa

        self.assert_has_feature(
            16, 10485, 25344, "roads",
            {"kind": "minor_road", "kind_detail": "residential", "id": 8919312,
             "name": "Racine Ln.", "sort_rank": 360})

    def test_service(self):
        self.generate_fixtures(dsl.way(59161514, wkt_loads('LINESTRING (-122.4472244965 37.80663996058681, -122.44711463254 37.8067056828995, -122.446758001373 37.80679809149498, -122.446403795656 37.80689000315549, -122.446004135186 37.80698539243338, -122.444982211719 37.80729270973048, -122.444909807507 37.80734345599718, -122.444832013403 37.80740499023472)'), {u'name': u'Yacht Road', u'tiger:cfcc': u'A41', u'source': u'openstreetmap.org', u'tiger:county': u'San Francisco, CA', u'oneway': u'yes', u'highway': u'service'}))  # noqa

        self.assert_has_feature(
            16, 10477, 25323, "roads",
            {"kind": "minor_road", "kind_detail": "service", "id": 59161514,
             "name": "Yacht Rd.", "sort_rank": 358})

    def test_parking_aisle(self):
        # service roads
        self.generate_fixtures(dsl.way(147002738, wkt_loads('LINESTRING (-122.478644600698 37.72751448527099, -122.478552972539 37.72752620859117, -122.47844724083 37.7275412712785, -122.478407535294 37.72754446854669, -122.478349863453 37.7275434027906, -122.477901693958 37.72752627964159)'), {u'source': u'openstreetmap.org', u'service': u'parking_aisle', u'highway': u'service'}))  # noqa

        self.assert_has_feature(
            16, 10471, 25341, "roads",
            {"kind": "minor_road", "kind_detail": "service",
             "service": "parking_aisle", "id": 147002738, "sort_rank": 356})

    def test_driveway(self):
        self.generate_fixtures(dsl.way(242769687, wkt_loads('LINESTRING (-122.390804727102 37.7828692767022, -122.390647521928 37.78274048750399, -122.390665667896 37.78271691635859, -122.390669081494 37.78268936934769, -122.39065704407 37.7826634552689, -122.390631891242 37.78264421494688, -122.390598833239 37.782635482253, -122.390564068438 37.78263896113118, -122.390534783359 37.78265401260229, -122.390516727222 37.78267758376779, -122.390513313624 37.78270505978559, -122.390525261217 37.78273111584467, -122.390550414045 37.78275028514659, -122.390583472048 37.78275901782688, -122.390618236849 37.78275546795702, -122.390647521928 37.78274048750399)'), {u'source': u'openstreetmap.org', u'service': u'driveway', u'highway': u'service'}))  # noqa

        self.assert_has_feature(
            16, 10487, 25329, "roads",
            {"kind": "minor_road", "kind_detail": "service",
             "service": "driveway", "id": 242769687, "sort_rank": 356})
