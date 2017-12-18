from . import FixtureTest


class PredictableLayersPois(FixtureTest):
    def test_grave_yard_node(self):
        # Node:358830410 Grave_yard in POIs
        self.load_fixtures(['http://www.openstreetmap.org/node/358830410'])

        self.assert_has_feature(
            16, 10475, 25352, 'pois',
            {'id': 358830410, 'kind': 'grave_yard'})

    def test_grave_yard_way(self):
        # Grave_yard in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/395328265'])

        self.assert_has_feature(
            15, 5231, 12653, 'pois',
            {'id': 395328265, 'kind': 'grave_yard'})

        self.assert_has_feature(
            15, 5231, 12653, 'landuse',
            {'id': 395328265, 'kind': 'grave_yard'})

        # Label placement Grave_yard in landuse
        self.assert_no_matching_feature(
            15, 5231, 12653, 'landuse',
            {'id': 395328265, 'kind': 'grave_yard', 'label_placement': True})

    def test_arlington_cemetery(self):
        # Arlington National Cemetery - there are two objects representing
        # this in the same place. The code will de-duplicate one or the other
        # of them.
        self.load_fixtures([
            'http://www.openstreetmap.org/way/41654965',
            'http://www.openstreetmap.org/relation/2475077',
        ], clip=self.tile_bbox(12, 1171, 1567))

        self.assert_has_feature(
            12, 1171, 1567, 'pois',
            {'id': set([41654965, -2475077]), 'kind': 'cemetery',
             'min_zoom': 12})

    def test_cemetery_label(self):
        # Label placement Cemetery in landuse
        self.load_fixtures(['http://www.openstreetmap.org/way/44580948'])

        self.assert_no_matching_feature(
            15, 5471, 12981, 'landuse',
            {'id': 44580948, 'kind': 'cemetery', 'label_placement': True})

    def test_farm(self):
        # Way:179213166 Farm in POIs
        self.load_fixtures(['http://www.openstreetmap.org/way/179213166'])

        self.assert_has_feature(
            15, 6660, 12542, 'pois',
            {'id': 179213166, 'kind': 'farm'})

        # Label placement farm in landuse
        self.assert_no_matching_feature(
            15, 6660, 12542, 'landuse',
            {'id': 179213166, 'kind': 'farm', 'label_placement': True})

    def test_forest_way(self):
        # landuse: Forest in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/375855355'])

        self.assert_has_feature(
            14, 2597, 5860, 'pois',
            {'id': 375855355, 'kind': 'forest'})

        # Label placement forest in landuse
        self.assert_no_matching_feature(
            14, 2597, 5860, 'landuse',
            {'id': 375855355, 'kind': 'forest', 'label_placement': True})

    def test_forest_node(self):
        # Node:357559979 landuse: Forest in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/357559979'])

        self.assert_has_feature(
            14, 2842, 6101, 'pois',
            {'id': 357559979, 'kind': 'forest', 'min_zoom': 14})

    def test_forest_protect_class(self):
        # Way:432810821 landuse: Forest protect class in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/432810821'])

        self.assert_has_feature(
            8, 72, 94, 'pois',
            {'id': 432810821, 'kind': 'forest', 'protect_class': '6'})

    def test_golf_course_way(self):
        # Way:30903221 Golf_course in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/30903221'])

        self.assert_has_feature(
            13, 1308, 3166, 'pois',
            {'id': 30903221, 'kind': 'golf_course'})

        # Label placement Golf_course in landuse
        self.assert_no_matching_feature(
            15, 5233, 12666, 'landuse',
            {'id': 30903221, 'kind': 'golf_course', 'label_placement': True})

    def test_golf_course_node(self):
        # Node:4035914099 Golf_course in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/4035914099'])

        self.assert_has_feature(
            14, 2680, 6334, 'pois',
            {'id': 4035914099, 'kind': 'golf_course', 'min_zoom': 14})

    def test_military_way(self):
        # Way:330274727 Military in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/330274727'])

        self.assert_has_feature(
            13, 1308, 3174, 'pois',
            {'id': 330274727, 'kind': 'military'})

        # Label placement military in landuse
        self.assert_no_matching_feature(
            15, 5233, 12697, 'landuse',
            {'id': 330274727, 'kind': 'military', 'label_placement': True})

    def test_military_node(self):
        # Node:369174053 Military in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/369174053'])

        self.assert_has_feature(
            14, 2617, 6329, 'pois',
            {'id': 369174053, 'kind': 'military', 'min_zoom': 14})

    def test_national_park_way(self):
        # Way:296096756 national_park in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/296096756'])

        self.assert_has_feature(
            10, 164, 397, 'pois',
            {'id': 296096756, 'kind': 'park'})

        # Label placement national_park in landuse
        self.assert_no_matching_feature(
            15, 5267, 12722, 'landuse',
            {'id': 296096756, 'kind': 'park', 'label_placement': True})

    def test_national_park_node(self):
        # Node:617506856 national_park in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/617506856'])

        self.assert_has_feature(
            14, 3374, 6184, 'pois',
            {'id': 617506856, 'kind': 'park', 'min_zoom': 14})

    def test_nature_reserve_way(self):
        # Way:40260866 nature_reserve in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/40260866'])

        self.assert_has_feature(
            12, 720, 1638, 'pois',
            {'id': 40260866, 'kind': 'nature_reserve'})

        # Label placement nature_reserve in landuse
        self.assert_no_matching_feature(
            15, 5766, 13111, 'landuse',
            {'id': 40260866, 'kind': 'nature_reserve',
             'label_placement': True})

    def test_nature_reserve_node(self):
        # Node:1262562806 nature_reserve in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/1262562806'])

        self.assert_has_feature(
            10, 247, 388, 'pois',
            {'id': 1262562806, 'kind': 'nature_reserve', 'min_zoom': 10})

    def test_park_way(self):
        # Way:23871270 park in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/23871270'])

        self.assert_has_feature(
            13, 1310, 3166, 'pois',
            {'id': 23871270, 'kind': 'park'})

        # Label placement park in landuse
        self.assert_no_matching_feature(
            15, 5240, 12667, 'landuse',
            {'id': 23871270, 'kind': 'park', 'label_placement': True})

    def test_park_node(self):
        # park in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/356541963'])

        self.assert_has_feature(
            14, 2622, 5725, 'pois',
            {'id': 356541963, 'kind': 'park', 'min_zoom': 14})

    def test_planet_way(self):
        # Way:26278098 plant in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/26278098'])

        self.assert_has_feature(
            14, 2617, 6334, 'pois',
            {'id': 26278098, 'kind': 'plant'})

        # Label placement plant in landuse
        self.assert_no_matching_feature(
            15, 5235, 12668, 'landuse',
            {'id': 26278098, 'kind': 'plant', 'label_placement': True})

    def test_plant_node(self):
        # Node:902365126 plant in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/902365126'])

        self.assert_has_feature(
            14, 2777, 6374, 'pois',
            {'id': 902365126, 'kind': 'plant', 'min_zoom': 14})

    def test_pitch_node(self):
        # Node:2442093493 pitch in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/2442093493'])

        self.assert_has_feature(
            16, 10910, 25062, 'pois',
            {'id': 2442093493, 'kind': 'pitch', 'min_zoom': 16})

    def test_protected_area_way(self):
        # Way:296573403 protected_area in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/296573403'])

        self.assert_has_feature(
            9, 82, 198, 'pois',
            {'id': 296573403, 'kind': 'protected_area'})

        # Label placement protected_area in landuse
        self.assert_no_matching_feature(
            15, 5249, 12701, 'landuse',
            {'id': 296573403, 'kind': 'protected_area',
             'label_placement': True})

    def test_protected_area_node(self):
        # boundary = protected_area in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/1462300228'])

        self.assert_has_feature(
            14, 8695, 5583, 'pois',
            {'id': 1462300228, 'kind': 'protected_area', 'min_zoom': 14})

    def test_quarry_way(self):
        # quarry in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/362159618'])

        self.assert_has_feature(
            12, 660, 1437, 'pois',
            {'id': 362159618, 'kind': 'quarry', 'min_zoom': 12})

        # Label placement quarry in landuse
        self.assert_no_matching_feature(
            15, 5284, 11498, 'landuse',
            {'id': 362159618, 'kind': 'quarry', 'label_placement': True})

    def test_quarry_node(self):
        # Node:585365655 quarry in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/585365655'])

        self.assert_has_feature(
            14, 2622, 6334, 'pois',
            {'id': 585365655, 'kind': 'quarry', 'min_zoom': 14})

    def test_recreation_ground_way(self):
        # landuse=recreation_ground in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/413471062'])

        self.assert_has_feature(
            14, 2629, 6331, 'pois',
            {'id': 413471062, 'kind': 'recreation_ground', 'min_zoom': 14})

        # Label placement recreation_ground in landuse
        self.assert_no_matching_feature(
            16, 10519, 25326, 'landuse',
            {'id': 413471062, 'kind': 'recreation_ground',
             'label_placement': True})

    def test_recreation_ground_node(self):
        # recreation_ground in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/417274812'])

        self.assert_has_feature(
            14, 2620, 6330, 'pois',
            {'id': 417274812, 'kind': 'recreation_ground', 'min_zoom': 14})

    def test_substation(self):
        # Node:4214350591 substation in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/4214350591'])

        self.assert_has_feature(
            15, 5233, 12668, 'pois',
            {'id': 4214350591, 'kind': 'substation', 'min_zoom': 15})

    def test_village_green_way(self):
        # village_green in POIS
        # note: since #1103, there should be no POIs for village_green,
        # only label placements in the landuse layer.
        self.load_fixtures(['http://www.openstreetmap.org/way/128479579'])

        self.assert_no_matching_feature(
            14, 6000, 9246, 'pois',
            {'id': 128479579, 'kind': 'village_green', 'min_zoom': 13.23})

        # Label placement village_green in landuse
        self.assert_has_feature(
            16, 24002, 36987, 'landuse',
            {'id': 128479579, 'kind': 'village_green',
             'label_placement': True})

    def test_village_green_node(self):
        # Node:3199567035 village_green in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/3199567035'])

        self.assert_no_matching_feature(
            14, 4186, 6018, 'pois',
            {'id': 3199567035, 'kind': 'village_green', 'min_zoom': 14})

    def test_wastewater_plant_way(self):
        # Way:239634932 wastewater_plant in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/239634932'])

        self.assert_has_feature(
            13, 1310, 3167, 'pois',
            {'id': 239634932, 'kind': 'wastewater_plant', 'min_zoom': 13})

        # Label placement wastewater_plant in landuse
        self.assert_no_matching_feature(
            15, 5243, 12669, 'landuse',
            {'id': 239634932, 'kind': 'wastewater_plant',
             'label_placement': True})

    def test_wastewater_plant_node(self):
        # Node:2838226695 wastewater_plant in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/2838226695'])

        self.assert_has_feature(
            14, 2615, 6325, 'pois',
            {'id': 2838226695, 'kind': 'wastewater_plant', 'min_zoom': 14})

    def test_water_works_way(self):
        # Way:93703732 water_works in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/93703732'])

        self.assert_has_feature(
            14, 2620, 6330, 'pois',
            {'id': 93703732, 'kind': 'water_works', 'min_zoom': 14})

        # Label placement water_works in landuse
        self.assert_no_matching_feature(
            15, 5240, 12661, 'landuse',
            {'id': 93703732, 'kind': 'water_works', 'label_placement': True})

    def test_water_works_node(self):
        # water_works in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/1380919388'])

        self.assert_has_feature(
            14, 8173, 5372, 'pois',
            {'id': 1380919388, 'kind': 'water_works', 'min_zoom': 14})

    def test_winter_sports_way(self):
        # Way:317721523 winter_sports in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/317721523'])

        self.assert_has_feature(
            10, 170, 391, 'pois',
            {'id': 317721523, 'kind': 'winter_sports', 'min_zoom': 10})

        # Label placement winter_sports in landuse
        self.assert_no_matching_feature(
            15, 5470, 12530, 'landuse',
            {'id': 317721523, 'kind': 'winter_sports',
             'label_placement': True})

    def test_winter_sports_node(self):
        # Node:4042754024 winter_sports in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/4042754024'])

        self.assert_has_feature(
            13, 4238, 2938, 'pois',
            {'id': 4042754024, 'kind': 'winter_sports', 'min_zoom': 13})

    def test_wood_way(self):
        # landuse: wood in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/433247531'])

        self.assert_has_feature(
            14, 8113, 5428, 'pois',
            {'id': 433247531, 'kind': 'wood'})

        # Label placement landuse: wood in landuse
        self.assert_no_matching_feature(
            15, 16227, 10856, 'landuse',
            {'id': 433247531, 'kind': 'wood', 'label_placement': True})

    def test_natural_wood_way(self):
        # natural: wood in POIS
        # note: since #1103, there should be no POIs for natural_wood, only
        # label placements in the landuse layer.
        self.load_fixtures(['http://www.openstreetmap.org/way/249171216'])

        self.assert_no_matching_feature(
            14, 8107, 5426, 'pois',
            {'id': 249171216, 'kind': 'natural_wood'})

        # Label placement natural: wood in landuse
        self.assert_has_feature(
            15, 16214, 10852, 'landuse',
            {'id': 249171216, 'kind': 'natural_wood', 'label_placement': True})

    def test_natural_wood_node(self):
        # Node:369162231 natural: wood in POIS
        # note: since #1103, there should be no POIs for natural_wood, only
        # label placements in the landuse layer.
        self.load_fixtures(['http://www.openstreetmap.org/node/369162231'])

        self.assert_no_matching_feature(
            14, 2612, 6298, 'pois',
            {'id': 369162231, 'kind': 'natural_wood'})

    def test_works_way(self):
        # works in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/161371157'])

        self.assert_has_feature(
            14, 8111, 5443, 'pois',
            {'id': 161371157, 'kind': 'works', 'min_zoom': 14})

        # Label placement works in landuse
        self.assert_no_matching_feature(
            14, 8111, 5443, 'landuse',
            {'id': 161371157, 'kind': 'works', 'label_placement': True})

    def test_works_node(self):
        # Node:1004981713 works in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/1004981713'])

        self.assert_has_feature(
            14, 3293, 6329, 'pois',
            {'id': 1004981713, 'kind': 'works', 'min_zoom': 14})
