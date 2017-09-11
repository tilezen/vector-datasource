# -*- encoding: utf-8 -*-
from . import OsmFixtureTest


class NationalForests(OsmFixtureTest):
    def test_boundary_national_park(self):
        # Example Stanislaus National Forest in California near Yosemite
        # should be kind:forest.
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/972008',
        ], clip=self.tile_bbox(11, 340, 788))

        self.assert_has_feature(
            11, 340, 788, 'landuse',
            {'kind': 'forest', 'id': -972008})

    def test_protect_class_5(self):
        # But this other Humboldt forest in Nevada has protect_class 5 so
        # that's not guaranteed, should be kind:forest.
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/2389847',
        ], clip=self.tile_bbox(11, 369, 769))

        self.assert_has_feature(
            11, 369, 769, 'landuse',
            {'kind': 'forest', 'id': -2389847})

    def test_nature_reserve_plus_operator_tag(self):
        # leisure=nature_reserve in Smith River is already taken care of by
        # operator (should be kind:forest).
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/6213964',
        ], clip=self.tile_bbox(14, 2559, 6099))

        self.assert_has_feature(
            14, 2559, 6099, 'landuse',
            {'kind': 'forest', 'id': -6213964})

    def test_operator_usnps_not_forest(self):
        # Counter example is Mojave National Preserve which is operated by
        # United States National Park Service so we don't want it to become
        # a forest (it should be kind:national_park).
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/175098',
        ], clip=self.tile_bbox(12, 733, 1617))

        self.assert_has_feature(
            12, 733, 1617, 'landuse',
            {'kind': 'national_park', 'id': -175098})

    def test_nature_reserve_without_operator_with_protect_class(self):
        # Point Reyes is also leisure=nature_reserve but without an operator
        # but with a protect_class of 2 (it should be kind:national_park,
        # but might need some data work?), until data is fixed I think it'd
        # come thru as kind:nature_reserve?
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/1250137',
        ], clip=self.tile_bbox(15, 5192, 12627))

        self.assert_has_feature(
            15, 5192, 12627, 'landuse',
            {'kind': 'national_park', 'id': -1250137})

    def test_park_type_state_recreational_area(self):
        # leisure=park in San Luis Reservoir State Recreational Area has
        # boundary=national_park and leisure=park and
        # park:type=state_recreational_area and no protect_class. This
        # shouldn't be a kind national_park, just a kind:park!
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/3004556',
        ], clip=self.tile_bbox(15, 5359, 12747))

        self.assert_has_feature(
            15, 5359, 12747, 'landuse',
            {'kind': 'park', 'id': -3004556})

    # Example forest in Colorado that only gets demoted because of
    # protect_class is present as 6 but operator is missing. Gets demoted
    # to what, though? propose kind:park since there isn't an operator
    # to say forest, and it's not a national park. Alternatively
    # boundary:type=protected_area could give us kind: protected_area
    # instead.

    def test_protection_title_national_forest(self):
        # This feature also has protection_title=National Forest, and the
        # name is "Arapaho National Forest", so it should probably be classed
        # as a forest.
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/396026',
        ], clip=self.tile_bbox(13, 1683, 3103))

        self.assert_has_feature(
            13, 1683, 3103, 'landuse',
            {'kind': 'forest', 'id': -396026})

    def test_nature_reserve_protected_area(self):
        # leisure=nature_reserve in North Farallon Islands State Marine
        # Reserve has boundary=protected_area with protect_class=4 in tile
        # 11/323/791. It's operator=California Department of Fish & Wildlife
        # so we'd just want this to be kind:nature_reserve.
        self.load_fixtures([
            'https://www.openstreetmap.org/way/436801947',
        ], clip=self.tile_bbox(11, 323, 791))

        self.assert_has_feature(
            11, 323, 791, 'landuse',
            {'kind': 'nature_reserve', 'id': 436801947})

    def test_nature_reserve_national_park(self):
        # leisure=nature_reserve in Mount Tamalpais Watershed has
        # boundary=national_park with boundary:type=protected_area and
        # operator=Marin Municipal Water District and protect_class=4. It
        # should just be kind:nature_reserve.
        self.load_fixtures([
            'https://www.openstreetmap.org/relation/7473345',
        ], clip=self.tile_bbox(13, 1305, 3161))

        self.assert_has_feature(
            13, 1305, 3161, 'landuse',
            {'kind': 'nature_reserve', 'id': -7473345})

    def test_common(self):
        # leisure=common in Blithedale Summit Open Space Preserve with
        # boundary=national_park and boundary:type=protected_area and
        # protect_class=5 and operator=Marin County Parks should just be
        # kind:common.
        self.load_fixtures([
            'https://www.openstreetmap.org/way/297452972',
        ], clip=self.tile_bbox(15, 5229, 12648))

        self.assert_has_feature(
            15, 5229, 12648, 'landuse',
            {'kind': 'common', 'id': 297452972})

    def test_nature_reserve_boundary_type(self):
        # leisure=nature_reserve in Glen Canyon National Recreation Area with
        # boundary=national_park and boundary:type=protected_area and
        # protect_class=5 and protection_title=National Recreation Area which
        # I think should default to kind:nature_reserve.
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/5273153',
        ], clip=self.tile_bbox(12, 784, 1585))

        self.assert_has_feature(
            12, 784, 1585, 'landuse',
            {'kind': 'nature_reserve', 'id': -5273153})

    def test_plain_nature_reserve(self):
        # leisure=nature_reserve in Parque Natural Sierra de Andújar with
        # finally kind:nature_reserve.
        self.load_fixtures([
            'https://www.openstreetmap.org/way/373769670',
        ], clip=self.tile_bbox(13, 4003, 3151))

        self.assert_has_feature(
            13, 4003, 3151, 'landuse',
            {'kind': 'nature_reserve', 'id': 373769670})

    def test_protected_area_protect_class_5(self):
        # boundary=protected_area in Naturpark Steigerwald with
        # protect_class=5 should end up with kind: protected_area
        self.load_fixtures([
            'https://www.openstreetmap.org/relation/3875431',
        ], clip=self.tile_bbox(13, 4336, 2787))

        self.assert_has_feature(
            13, 4336, 2787, 'landuse',
            {'kind': 'protected_area', 'id': -3875431})

    def test_national_park_operator_national_park_service(self):
        # boundary=national_park in Muir Woods National Monument with
        # leisure=nature_reserve and operator=National Park Service and
        # protect_class=3 should end up with kind:national_park
        self.load_fixtures([
            'https://www.openstreetmap.org/relation/6229828',
        ], clip=self.tile_bbox(16, 10452, 25302))

        self.assert_has_feature(
            16, 10452, 25302, 'landuse',
            {'kind': 'national_park', 'id': -6229828})

    def test_park_protect_class_5(self):
        # leisure=park in Henry W. Coe State Park with boundary=protected_area
        # and protect_class=5 should end up with kind:park.
        self.load_fixtures([
            'https://www.openstreetmap.org/relation/318202',
        ], clip=self.tile_bbox(13, 1332, 3184))

        self.assert_has_feature(
            13, 1332, 3184, 'landuse',
            {'kind': 'park', 'id': -318202})

    def test_nature_reserve_plus_operator_national_park_service(self):
        # operator=United States National Park Service and protect_class=2 in
        # Yosemite National Park with boundary=national_park and
        # leisure=nature_reserve should end up with kind:national_park.
        self.load_fixtures([
            'https://www.openstreetmap.org/relation/1643367',
        ], clip=self.tile_bbox(13, 1371, 3164))

        self.assert_has_feature(
            13, 1371, 3164, 'landuse',
            {'kind': 'national_park', 'id': -1643367})

    def test_boundary_national_park_plus_operator_usnps_redwood(self):
        # operator=United States National Park Service and protect_class=2 in
        # Redwood National Park with boundary=national_park and
        # leisure=nature_reserve should end up with kind:national_park.
        self.load_fixtures([
            'https://www.openstreetmap.org/relation/215231',
        ], clip=self.tile_bbox(13, 1274, 3066))

        self.assert_has_feature(
            13, 1274, 3066, 'landuse',
            {'kind': 'national_park', 'id': -215231})

    def test_boundary_national_park_plus_operator_usnps_yellowstone(self):
        # operator=United States National Park Service and protect_class=2 in
        # Yellowstone National Park with boundary=national_park and
        # leisure=nature_reserve should end up with kind:national_park.
        self.load_fixtures([
            'https://www.openstreetmap.org/relation/1453306',
        ], clip=self.tile_bbox(13, 1591, 2972))

        self.assert_has_feature(
            13, 1591, 2972, 'landuse',
            {'kind': 'national_park', 'id': -1453306})

    def test_boundary_national_park_adirondack(self):
        # boundary=national_park in Adirondack Park should end up with
        # kind:park.
        self.load_fixtures([
            'https://www.openstreetmap.org/relation/1695394',
        ], clip=self.tile_bbox(13, 2410, 3001))

        self.assert_has_feature(
            13, 2410, 3001, 'landuse',
            {'kind': 'park', 'id': -1695394})

    def test_boundary_national_park_plus_operator_usnps_shenandoah(self):
        # operator=United States National Park Service and protect_class=2 in
        # Shenandoah National Park with boundary=national_park and
        # leisure=park should end up with kind:national_park.
        self.load_fixtures([
            'https://www.openstreetmap.org/relation/5548542',
        ], clip=self.tile_bbox(13, 2313, 3142))

        self.assert_has_feature(
            13, 2313, 3142, 'landuse',
            {'kind': 'national_park', 'id': -5548542})

    def test_designation_national_park(self):
        # designation=national_park in Cairngorms National Park with
        # boundary=national_park should end up with kind:national_park.
        self.load_fixtures([
            'https://www.openstreetmap.org/relation/1947603',
        ], clip=self.tile_bbox(13, 4014, 2512))

        self.assert_has_feature(
            13, 4014, 2512, 'landuse',
            {'kind': 'national_park', 'id': -1947603})

    def test_designation_aonb(self):
        # boundary=national_park in North Wessex Downs AONB with
        # designation=area_of_outstanding_natural_beauty should end up with
        # kind:park.
        self.load_fixtures([
            'https://www.openstreetmap.org/relation/2904192',
        ], clip=self.tile_bbox(13, 4054, 2728))

        self.assert_has_feature(
            13, 4054, 2728, 'landuse',
            {'kind': 'park', 'id': -2904192})

    def test_parks_canada(self):
        # operator:en=Parks Canada and boundary=national_park in Riding
        # Mountain National Park with leisure=nature_reserve.
        self.load_fixtures([
            'http://www.openstreetmap.org/way/185735773',
        ], clip=self.tile_bbox(13, 1812, 2748))

        self.assert_has_feature(
            13, 1812, 2748, 'landuse',
            {'kind': 'national_park', 'id': 185735773})
