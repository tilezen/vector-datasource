# -*- encoding: utf-8 -*-
from . import OsmFixtureTest


class CycleRoute(OsmFixtureTest):
    def test_embarcadero(self):
        #  Way: The Embarcadero (24335490)
        self.load_fixtures([
            'http://www.openstreetmap.org/way/24335490',
            'http://www.openstreetmap.org/relation/32386',
        ], clip=self.tile_bbox(16, 10487, 25327))

        self.assert_has_feature(
            16, 10487, 25327, 'roads',
            {'id': 24335490, 'kind': 'major_road', 'cycleway_right': 'lane',
             'bicycle_network': 'lcn'})

    def test_king_street(self):
        # Way: King Street (8920394)
        self.load_fixtures(['http://www.openstreetmap.org/way/8920394'])

        self.assert_has_feature(
            16, 10487, 25329, 'roads',
            {'id': 8920394, 'kind': 'major_road', 'cycleway_right': 'lane',
             'bicycle_network': 'lcn'})

    def test_another_king_street(self):
        # Way: King Street (397270776)
        self.load_fixtures(['http://www.openstreetmap.org/way/397270776'])

        self.assert_has_feature(
            16, 10487, 25329, 'roads',
            {'id': 397270776, 'kind': 'major_road', 'cycleway_right': 'lane',
             'bicycle_network': 'lcn'})

    def test_clara_immerwahr_strasse(self):
        # Way: Clara-Immerwahr-Straße (287167007)
        self.load_fixtures(['http://www.openstreetmap.org/way/287167007'])

        self.assert_has_feature(
            16, 34494, 21846, 'roads',
            {'id': 287167007, 'kind': 'minor_road', 'bicycle_network': 'icn'})

    def test_198th_street(self):
        # Way: 198th Street (138388021)
        self.load_fixtures(['http://www.openstreetmap.org/way/138388021'])

        self.assert_has_feature(
            16, 10435, 22457, 'roads',
            {'id': 138388021, 'kind': 'major_road', 'bicycle_network': 'icn',
             'cycleway': 'shared_lane'})

    def test_oneway_ncn(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/232603515'])

        self.assert_has_feature(
            16, 18735, 25114, 'roads',
            {'id': 232603515, 'kind': 'minor_road', 'bicycle_network': 'ncn',
             'oneway': 'yes'})

    def test_path_ncn(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/315261543'])

        self.assert_has_feature(
            16, 32209, 22024, 'roads',
            {'id': 315261543, 'kind': 'path', 'bicycle_network': 'ncn'})

    def test_path_rcn(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/44422697'])

        self.assert_has_feature(
            16, 10509, 25377, 'roads',
            {'id': 44422697, 'kind': 'path', 'bicycle_network': 'rcn'})

    def test_rcn_ref_no_relation(self):
        # Way: Cabrini Boulevard.
        # rcn_ref=9, but not part of any relation.
        self.load_fixtures(['http://www.openstreetmap.org/way/5669719'])

        self.assert_has_feature(
            16, 19307, 24607, 'roads',
            {'id': 5669719, 'kind': 'minor_road', 'bicycle_network': 'rcn'})

    def test_11th_street(self):
        # Way: 11th Street (27029204)
        self.load_fixtures(['http://www.openstreetmap.org/way/27029204'])

        self.assert_has_feature(
            16, 10483, 25332, 'roads',
            {'id': 27029204, 'kind': 'major_road', 'bicycle_network': 'lcn',
             'cycleway': 'lane'})

    def test_boulge_road(self):
        # Way: Boulge Road
        self.load_fixtures([
            'http://www.openstreetmap.org/way/50835689',
            'http://www.openstreetmap.org/relation/2767188',
        ], clip=self.tile_bbox(16, 33002, 21613))

        self.assert_has_feature(
            16, 33002, 21613, 'roads',
            {'id': 50835689, 'kind': 'minor_road', 'bicycle_network': 'icn'})

    def test_west_national_avenue(self):
        # Way: West National Ave (95578389)
        self.load_fixtures([
            'http://www.openstreetmap.org/way/95578389',
            'http://www.openstreetmap.org/relation/3318923',
        ], clip=self.tile_bbox(16, 16842, 24939))

        self.assert_has_feature(
            16, 16842, 24939, 'roads',
            {'id': 95578389, 'kind': 'major_road', 'bicycle_network': 'ncn'})

    def test_kananaskis_trail(self):
        # Way: Kananaskis Trail (385652955)
        self.load_fixtures([
            'http://www.openstreetmap.org/way/385652955',
            'http://www.openstreetmap.org/relation/5737942',
        ], clip=self.tile_bbox(16, 11818, 22039))

        self.assert_has_feature(
            16, 11818, 22039, 'roads',
            {'id': 385652955, 'kind': 'major_road', 'bicycle_network': 'rcn'})

    def test_foothill_expressway(self):
        # Way: Foothill Expressway (173846425)
        self.load_fixtures([
            'http://www.openstreetmap.org/way/173846425',
            'http://www.openstreetmap.org/relation/1204994',
        ], clip=self.tile_bbox(16, 10535, 25419))

        self.assert_has_feature(
            16, 10535, 25419, 'roads',
            {'id': 173846425, 'kind': 'major_road', 'bicycle_network': 'lcn'})

    def test_segregated(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/255652148'])

        self.assert_has_feature(
            16, 10487, 25333, 'roads',
            {'id': 255652148, 'kind': 'path', 'segregated': True})

    def test_not_segregated(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/215528939'])

        self.assert_no_matching_feature(
            16, 10486, 25331, 'roads', {'segregated': 'no'})

    def test_post_street(self):
        # Way: Post Street (28841123)
        self.load_fixtures(['http://www.openstreetmap.org/way/28841123'])

        self.assert_has_feature(
            16, 10484, 25327, 'roads',
            {'id': 28841123, 'is_bicycle_related': True})

    def test_is_bicycle_related(self):
        # Way: 301442215
        self.load_fixtures(['http://www.openstreetmap.org/way/301442215'])

        self.assert_has_feature(
            16, 34748, 22664, 'roads',
            {'id': 301442215, 'is_bicycle_related': True})

    def test_also_bicycle_related(self):
        # Way: 428306786
        self.load_fixtures(['http://www.openstreetmap.org/way/428306786'])

        self.assert_has_feature(
            16, 18649, 25417, 'roads',
            {'id': 428306786, 'is_bicycle_related': True})
