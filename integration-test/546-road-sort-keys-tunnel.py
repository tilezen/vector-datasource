# -*- encoding: utf-8 -*-
from shapely.wkt import loads as wkt_loads
import dsl
from . import FixtureTest


class RoadSortKeysTunnel(FixtureTest):
    def test_motorway_level_0(self):
        # tunnels at level = 0
        self.generate_fixtures(dsl.way(3685132833, wkt_loads('POINT (-122.455329276656 37.80300739883197)'), {u'source': u'openstreetmap.org', u'ref': u'437', u'highway': u'motorway_junction'}),dsl.way(167952621, wkt_loads('LINESTRING (-122.455329276656 37.80300739883197, -122.454934107763 37.80304260388298, -122.45454783219 37.80306545876599, -122.454197309567 37.803080789988)'), {u'lanes': u'3', u'name': u'Presidio Parkway', u'tunnel': u'yes', u'destination:street': u'Marina Boulevard', u'source': u'openstreetmap.org', u'alt_name': u'Doyle Drive', u'oneway': u'yes', u'ref': u'US 101', u'highway': u'motorway'}))  # noqa

        self.assert_has_feature(
            16, 10475, 25324, "roads",
            {"kind": "highway", "kind_detail": "motorway", "id": 167952621,
             "name": "Presidio Pkwy.", "is_tunnel": True, "sort_rank": 333})

    def test_trunk_level_0(self):
        self.generate_fixtures(dsl.way(259492789, wkt_loads('LINESTRING (-74.16702601822249 40.73275266220829, -74.16711180733211 40.73254919807029)'), {u'tunnel': u'yes', u'tiger:name_base': u'McCarter', u'hgv:state_network': u'yes', u'name': u'McCarter Highway', u'tiger:cfcc': u'A35', u'tiger:name_base_1': u'State Route 21', u'hgv': u'designated', u'tiger:zip_left': u'07104', u'tiger:zip_right': u'07104', u'lanes': u'4', u'source': u'openstreetmap.org', u'tiger:county': u'Essex, NJ', u'tiger:name_type': u'Hwy', u'NHS': u'yes', u'ref': u'NJ 21', u'NJDOT_SRI': u'00000021', u'HFCS': u'Urban Principal Arterial', u'source:hgv:state_network': u'NJDOT http://www.state.nj.us/transportation/about/rules/pdf/chapter32truckaccess.pdf', u'highway': u'trunk'}))  # noqa

        self.assert_has_feature(
            16, 19266, 24635, "roads",
            {"kind": "major_road", "kind_detail": "trunk", "id": 259492789,
             "name": "McCarter Hwy.", "is_tunnel": True, "sort_rank": 331})

        self.generate_fixtures(dsl.way(277441866, wkt_loads('LINESTRING (-83.51858074221251 35.74467572285489, -83.5186876417313 35.74474476841309, -83.51881250755579 35.74482300053089, -83.5189321631516 35.74490640915329, -83.51904642885579 35.74499477553549, -83.51915494534208 35.74508795384219, -83.51925717362138 35.74518557950971, -83.5193531136938 35.74528736088479, -83.519442406233 35.74539315213308, -83.51952478174461 35.74550258869337, -83.5196001503969 35.74561537891499, -83.5196680630324 35.74573115823921, -83.51972860948248 35.745849707927, -83.51978143042119 35.7459706634228, -83.519826436017 35.74609380599009, -83.51986353643818 35.74621847944319, -83.51989255202189 35.74634468377489, -83.519913482768 35.746471981529, -83.51992632867659 35.74660000815989, -83.51993082025298 35.74672825330868)'), {u'unsigned_ref': u'SR 71;SR 73', u'lanes': u'2', u'name': u'Gatlinburg Spur Road (north)', u'tunnel': u'yes', u'surface': u'paved', u'source': u'openstreetmap.org', u'official_name': u'Gatlinburg Spur Road (north)', u'NHS': u'yes', u'oneway': u'yes', u'ref': u'US 321;US 441', u'highway': u'trunk'}))  # noqa

        self.assert_has_feature(
            16, 17563, 25792, "roads",
            {"kind": "major_road", "kind_detail": "trunk", "id": 277441866,
             "name": "Gatlinburg Spur Road (north)", "is_tunnel": True,
             "sort_rank": 331})

    def test_primary_level_0(self):
        self.generate_fixtures(dsl.way(117837633, wkt_loads('LINESTRING (-87.66710367120798 41.56470766559397, -87.66648446248269 41.56452229306039)'), {u'tiger:name_base': u'Dixie', u'name': u'Dixie Highway', u'tiger:cfcc': u'A41', u'tunnel': u'yes', u'tiger:reviewed': u'no', u'source': u'openstreetmap.org', u'tiger:county': u'Cook, IL', u'tiger:name_type': u'Hwy', u'highway': u'primary'}))  # noqa

        self.assert_has_feature(
            16, 16808, 24434, "roads",
            {"kind": "major_road", "kind_detail": "primary", "id": 117837633,
             "name": "Dixie Hwy.", "is_tunnel": True, "sort_rank": 330})

    def test_secondary_level_0(self):
        self.generate_fixtures(dsl.way(57782075, wkt_loads('LINESTRING (-87.64371486497609 41.7396067862949, -87.64368198663669 41.73869201695129)'), {u'tiger:source': u'tiger_import_dch_v0.6_20070809', u'tiger:name_base': u'Halsted', u'name': u'South Halsted Street', u'tiger:cfcc': u'A41', u'tiger:separated': u'no', u'tunnel': u'yes', u'tiger:zip_left': u'60628', u'tiger:zip_right': u'60628', u'source': u'openstreetmap.org', u'tiger:county': u'Cook, IL', u'tiger:tlid': u'111832601:111832606:111832754', u'tiger:name_direction_prefix': u'S', u'tiger:name_type': u'St', u'highway': u'secondary', u'tiger:upload_uuid': u'bulk_upload.pl-ee310570-36cc-43bc-bc7b-aff94618acaf'}))  # noqa

        self.assert_has_feature(
            16, 16812, 24391, "roads",
            {"kind": "major_road", "kind_detail": "secondary", "id": 57782075,
             "name": "S Halsted St.", "is_tunnel": True, "sort_rank": 329})

    def test_teriary_level_0(self):
        self.generate_fixtures(dsl.way(57708079, wkt_loads('LINESTRING (-87.63913570281528 41.75983047016649, -87.63944553175681 41.75982631559528)'), {u'tiger:source': u'tiger_import_dch_v0.6_20070809', u'tiger:name_base': u'74th', u'name': u'West 74th Street', u'tiger:cfcc': u'A41', u'tiger:separated': u'no', u'tunnel': u'yes', u'tiger:zip_left': u'60636', u'tiger:zip_right': u'60636', u'tiger:reviewed': u'no', u'source': u'openstreetmap.org', u'tiger:county': u'Cook, IL', u'tiger:tlid': u'111820631:111820685:111820686:111820688:111820697:111820713:111820718:111820719:111820921:111820927:111820943:111820993:111821007:111821009:111820944:111820632:111831046', u'tiger:name_direction_prefix': u'W', u'tiger:name_type': u'St', u'highway': u'tertiary', u'tiger:upload_uuid': u'bulk_upload.pl-ee310570-36cc-43bc-bc7b-aff94618acaf'}))  # noqa

        self.assert_has_feature(
            16, 16813, 24386, "roads",
            {"kind": "major_road", "kind_detail": "tertiary", "id": 57708079,
             "name": "W 74th St.", "is_tunnel": True, "sort_rank": 327})

    def test_residential_level_0(self):
        self.generate_fixtures(dsl.way(56393654, wkt_loads('LINESTRING (-87.6687173149529 41.85966997294218, -87.66872872355698 41.86017336309299)'), {u'tiger:source': u'tiger_import_dch_v0.6_20070809', u'tiger:name_base': u'Paulina', u'bicycle': u'yes', u'name': u'South Paulina Street', u'tiger:cfcc': u'A41', u'tiger:separated': u'no', u'tunnel': u'yes', u'tiger:zip_left': u'60608', u'tiger:zip_right': u'60608', u'tiger:reviewed': u'no', u'source': u'openstreetmap.org', u'tiger:county': u'Cook, IL', u'tiger:tlid': u'111803173:111803174:111888591:111803151:111802722:111802724:111802727:111802728:111802730:111802740:111802742:111802744:111803143:111803146:111803147:111803148:111803152:111803155', u'tiger:name_direction_prefix': u'S', u'tiger:name_type': u'St', u'highway': u'residential', u'tiger:upload_uuid': u'bulk_upload.pl-ee310570-36cc-43bc-bc7b-aff94618acaf'}))  # noqa

        self.assert_has_feature(
            16, 16808, 24362, "roads",
            {"kind": "minor_road", "kind_detail": "residential",
             "id": 56393654, "name": "S Paulina St.", "is_tunnel": True,
             "sort_rank": 310})

    def test_service_level_0(self):
        self.generate_fixtures(dsl.way(190835369, wkt_loads('LINESTRING (-87.6339403862011 41.85666306423929, -87.6338758871637 41.85658478182989)'), {u'tunnel': u'yes', u'source': u'openstreetmap.org', u'name': u'South Wong Parkway', u'highway': u'service'}))  # noqa

        self.assert_has_feature(
            16, 16814, 24363, "roads",
            {"kind": "minor_road", "kind_detail": "service", "id": 190835369,
             "name": "S Wong Pkwy.", "is_tunnel": True, "sort_rank": 308})
