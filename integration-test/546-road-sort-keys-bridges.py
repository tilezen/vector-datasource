# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class RoadSortKeysBridges(FixtureTest):
    def test_motorway_bridge(self):
        self.generate_fixtures(dsl.way(295487932, wkt_loads('POINT (-122.474508577467 37.80641851996678)'), {u'source': u'openstreetmap.org', u'ref': u'439', u'highway': u'motorway_junction'}),dsl.way(28412298, wkt_loads('LINESTRING (-122.474314182039 37.80619487846148, -122.474508577467 37.80641851996678)'), {u'bridge': u'yes', u'layer': u'1', u'maxspeed': u'35 mph', u'lanes': u'5', u'name': u'Presidio Parkway', u'note:lanes': u'center lanes are reversible, so number may be different', u'hgv': u'designated', u'source:hgv:state_network': u'Caltrans http://www.dot.ca.gov/hq/traffops/trucks/truckmap/', u'oneway': u'yes', u'lit': u'yes', u'source': u'openstreetmap.org', u'tiger:county': u'San Francisco, CA', u'alt_name': u'Doyle Drive', u'NHS': u'STRAHNET', u'toll': u'no', u'bicycle': u'no', u'hgv:state_network': u'yes', u'ref': u'US 101;CA 1', u'highway': u'motorway'}))  # noqa

        self.assert_has_feature(
            16, 10472, 25323, "roads",
            {"kind": "highway", "kind_detail": "motorway", "id": 28412298,
             "name": "Presidio Pkwy.", "is_bridge": True, "sort_rank": 443})

    def test_trunk_bridge(self):
        self.generate_fixtures(dsl.way(59801274, wkt_loads('LINESTRING (-122.479362893599 37.77087721656759, -122.479200837522 37.77058011511458)'), {u'bridge': u'yes', u'layer': u'1', u'maxspeed': u'35 mph', u'lanes': u'3', u'name': u'Crossover Drive', u'tiger:cfcc': u'A35', u'source': u'openstreetmap.org', u'hgv': u'designated', u'source:hgv:state_network': u'Caltrans http://www.dot.ca.gov/hq/traffops/trucks/truckmap/', u'tiger:name_base_1': u'State Highway 1', u'tiger:county': u'San Francisco, CA', u'tiger:name_type': u'Dr', u'oneway': u'yes', u'hgv:state_network': u'yes', u'ref': u'CA 1', u'highway': u'trunk', u'tiger:name_base': u'Crossover'}))  # noqa

        self.assert_has_feature(
            16, 10471, 25331, "roads",
            {"kind": "major_road", "kind_detail": "trunk", "id": 59801274,
             "name": "Crossover Dr.", "is_bridge": True, "sort_rank": 443})

    def test_primary_bridge(self):
        self.generate_fixtures(dsl.way(399640204, wkt_loads('LINESTRING (-118.117754009656 33.8102109201601, -118.117900794373 33.80993729058998)'), {u'bridge': u'yes', u'tiger:name_base': u'Los Coyotes Diagonal', u'lanes': u'2', u'name': u'North Los Coyotes Diagonal', u'tiger:cfcc': u'A41', u'tiger:zip_left': u'90808', u'cycleway': u'lane', u'source': u'openstreetmap.org', u'tiger:county': u'Los Angeles, CA', u'tiger:name_direction_prefix': u'N', u'oneway': u'yes', u'highway': u'primary'}))  # noqa

        self.assert_has_feature(
            16, 11265, 26221, "roads",
            {"kind": "major_road", "kind_detail": "primary", "id": 399640204,
             "name": "North Los Coyotes Diagonal", "is_bridge": True,
             "sort_rank": 430})

    def test_secondary_bridge(self):
        self.generate_fixtures(dsl.way(27613581, wkt_loads('LINESTRING (-122.394765219527 37.7371122790657, -122.395118886254 37.73731396481919)'), {u'bridge': u'yes', u'maxspeed': u'30 mph', u'lanes': u'2', u'name': u'Oakdale Avenue', u'lcn_ref': u'70', u'cycleway': u'lane', u'source': u'openstreetmap.org', u'tiger:county': u'San Francisco, CA', u'tiger:name_type': u'Ave', u'tiger:name_base': u'Oakdale', u'tiger:cfcc': u'A41', u'highway': u'secondary'}))  # noqa

        self.assert_has_feature(
            16, 10486, 25339, "roads",
            {"kind": "major_road", "kind_detail": "secondary", "id": 27613581,
             "name": "Oakdale Ave.", "is_bridge": True, "sort_rank": 429})

    def test_teriary_bridge(self):
        self.generate_fixtures(dsl.way(242940297, wkt_loads('LINESTRING (-122.395271869347 37.7907203080898, -122.395156974822 37.79062745343989, -122.394827562608 37.79036145403797)'), {u'bridge': u'yes', u'tiger:name_base': u'Beale', u'lanes': u'3', u'name': u'Beale Street', u'tiger:cfcc': u'A41', u'source': u'openstreetmap.org', u'tiger:county': u'San Francisco, CA', u'tiger:name_type': u'St', u'oneway': u'yes', u'highway': u'tertiary', u'trolley_wire': u'yes'}))  # noqa

        self.assert_has_feature(
            16, 10486, 25327, "roads",
            {"kind": "major_road", "kind_detail": "tertiary", "id": 242940297,
             "name": "Beale St.", "is_bridge": True, "sort_rank": 427})

    def test_residential_bridge(self):
        self.generate_fixtures(dsl.way(162038104, wkt_loads('LINESTRING (-121.009686569766 39.24352031486828, -121.009910968924 39.24385926543338)'), {u'bridge': u'yes', u'tiger:name_base': u'Woodwardia', u'name': u'Woodwardia Place', u'tiger:cfcc': u'A41', u'tiger:reviewed': u'no', u'source': u'openstreetmap.org', u'tiger:county': u'Nevada, CA', u'tiger:name_type': u'Pl', u'highway': u'residential'}))  # noqa

        self.assert_has_feature(
            16, 10738, 24989, "roads",
            {"kind": "minor_road", "kind_detail": "residential",
             "id": 162038104, "name": "Woodwardia Pl.", "sort_rank": 410})

    def test_service_bridge(self):
        self.generate_fixtures(dsl.way(232303398, wkt_loads('LINESTRING (-122.416602904758 37.63546055316739, -122.416466181171 37.63550956768369)'), {u'bridge': u'yes', u'highway': u'service', u'source': u'openstreetmap.org'}))  # noqa

        self.assert_has_feature(
            16, 10482, 25363, "roads",
            {"id": 232303398, "kind": "minor_road", "kind_detail": "service",
             "is_bridge": True, "sort_rank": 408})
