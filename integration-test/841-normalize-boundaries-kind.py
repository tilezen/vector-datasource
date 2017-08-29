from . import OsmFixtureTest


class NormalizeBoundariesKind(OsmFixtureTest):
    def test_aboriginal_lands_protected_area(self):
        # Relation: Hoopa Valley Tribe
        #
        # Note: this is tagged as a "protected_area" rather than a political
        # boundary, but it seems that some "protect_class" values indicate
        # political "protection"
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/6214773',
        ], clip=self.tile_bbox(16, 10237, 24570, padding=2))

        self.assert_has_feature(
            16, 10237, 24570, 'boundaries',
            {'id': -6214773, 'kind': 'aboriginal_lands',
             'kind_detail': type(None)})

    def test_aboriginal_lands(self):
        # use relation instead of way, as osm2pgsql treats the relation as
        # superseding the way and removes its tags when both are present.
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/3854097',
        ], clip=self.tile_bbox(16, 10483, 22987, padding=2))

        self.assert_has_feature(
            16, 10483, 22987, 'boundaries',
            {'id': -3854097, 'kind': 'aboriginal_lands',
             'kind_detail': type(None)})

        # Way: Upper Sumas 6 (55602811)
        self.load_fixtures([
            'http://www.openstreetmap.org/way/55602811',
            'http://www.openstreetmap.org/relation/6791772',
        ], clip=self.tile_bbox(16, 10523, 22492, padding=2))

        self.assert_has_feature(
            16, 10523, 22492, 'boundaries',
            {'id': -6791772, 'kind': 'aboriginal_lands',
             'kind_detail': type(None)})

    def test_country(self):
        # Relation: United States of America
        self.load_fixtures([
            'https://www.openstreetmap.org/relation/148838',
        ], clip=self.tile_bbox(16, 10417, 25370, padding=2))

        self.assert_has_feature(
            16, 10417, 25370, 'boundaries',
            {'id': -148838, 'kind': 'country', 'kind_detail': '2'})

    def test_state_border(self):
        # Relation: Wyoming (161991) & Idaho (162116)
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/161991',
            'http://www.openstreetmap.org/relation/162116',
        ], clip=self.tile_bbox(16, 12553, 24147, padding=2))

        self.assert_has_feature(
            16, 12553, 24147, 'boundaries',
            {'id': set([-161991, -162116]), 'kind': 'region',
             'kind_detail': '4'})

    def test_county_border(self):
        # SF City/County -- San Mateo County
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/396487',
            'http://www.openstreetmap.org/relation/396498',
        ], clip=self.tile_bbox(16, 10484, 25346, padding=2))

        self.assert_has_feature(
            16, 10484, 25346, 'boundaries',
            {'id': set([-396487, -396498]), 'kind': 'county',
             'kind_detail': '6'})

    def test_locality(self):
        # Relation: Brisbane (2834528)
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/2834528',
        ], clip=self.tile_bbox(16, 10487, 25355, padding=2))

        self.assert_has_feature(
            16, 10487, 25355, 'boundaries',
            {'id': -2834528, 'kind': 'locality', 'kind_detail': '8'})

    # def test_0008(self):
    #     # ne data
    #     # Admin-1 boundary
    #     self.load_fixtures([])

    #     self.assert_has_feature(
    #         7, 75, 70, 'boundaries',
    #         {'id': int, 'kind': 'region', 'kind_detail': '4'})

    # def test_0009(self):
    #     # Admin-1 statistical boundary
    #     self.load_fixtures([])

    #     self.assert_has_feature(
    #         7, 101, 56, 'boundaries',
    #         {'id': int, 'kind': 'region', 'kind_detail': '4'})

    # def test_0010(self):
    #     # Admin-1 statistical meta bounds
    #     self.load_fixtures([])

    #     self.assert_has_feature(
    #         7, 26, 52, 'boundaries',
    #         {'id': int, 'kind': 'region', 'kind_detail': '4'})

    # def test_0011(self):
    #     # Admin-1 region boundary
    #     self.load_fixtures([])

    #     self.assert_has_feature(
    #         7, 99, 57, 'boundaries',
    #         {'id': int, 'kind': 'macroregion', 'kind_detail': '3'})

    # def test_0012(self):
    #     # Disputed (please verify)
    #     self.load_fixtures([])

    #     self.assert_has_feature(
    #         7, 39, 71, 'boundaries',
    #         {'id': int, 'kind': 'disputed', 'kind_detail': '2'})

    # def test_0013(self):
    #     # Indefinite (please verify)
    #     self.load_fixtures([])

    #     self.assert_has_feature(
    #         7, 20, 44, 'boundaries',
    #         {'id': int, 'kind': 'indefinite', 'kind_detail': '2'})

    # def test_0014(self):
    #     # Indeterminant frontier
    #     self.load_fixtures([])

    #     self.assert_has_feature(
    #         7, 91, 50, 'boundaries',
    #         {'id': int, 'kind': 'indeterminate', 'kind_detail': '2'})

    # def test_0015(self):
    #     # International boundary (verify)
    #     self.load_fixtures([])

    #     self.assert_has_feature(
    #         7, 67, 37, 'boundaries',
    #         {'id': int, 'kind': 'country', 'kind_detail': '2'})

    # def test_0016(self):
    #     # Lease limit
    #     self.load_fixtures([])

    #     self.assert_has_feature(
    #         7, 86, 45, 'boundaries',
    #         {'id': int, 'kind': 'lease_limit', 'kind_detail': '2'})

    # def test_0017(self):
    #     # Line of control (please verify)
    #     self.load_fixtures([])

    #     self.assert_has_feature(
    #         7, 90, 50, 'boundaries',
    #         {'id': int, 'kind': 'line_of_control', 'kind_detail': '2'})

    # def test_0018(self):
    #     # Overlay limit
    #     self.load_fixtures([])

    #     self.assert_has_feature(
    #         7, 109, 49, 'boundaries',
    #         {'id': int, 'kind': 'overlay_limit', 'kind_detail': '2'})
