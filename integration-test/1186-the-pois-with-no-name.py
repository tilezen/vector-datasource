from . import FixtureTest


# this is a collection of features which have no name and therefore should be
# excluded from being POIs.
class ThePoisWithNoName(FixtureTest):

    def test_trail_riding_station(self):
        # originally from 440-zoos-and-other-attractions-tourism.py
        # unnamed, CO
        self.load_fixtures(['https://www.openstreetmap.org/node/1589837084'])

        self.assert_no_matching_feature(
            16, 13686, 24901, 'pois',
            {'id': 1589837084})

    def test_kindergarten(self):
        # originally from 526-inclusive-pois.py
        self.load_fixtures(['https://www.openstreetmap.org/node/1460537343'])

        self.assert_no_matching_feature(
            16, 10470, 25342, 'pois',
            {'id': 1460537343})

    def test_doctors_clinic(self):
        self.load_fixtures(['https://www.openstreetmap.org/node/3879177193'])

        self.assert_no_matching_feature(
            16, 10533, 22894, 'pois',
            {'id': 3879177193})

    def test_recreation_track(self):
        # originally from 663-combo-outdoor-landuse-pois.py
        # Cox Stadium recreation track
        self.load_fixtures(['https://www.openstreetmap.org/relation/6328943'])

        self.assert_no_matching_feature(
            16, 10471, 25342, 'pois',
            {'id': -6328943})

    def test_running_track(self):
        # unnamed running track
        self.load_fixtures(['https://www.openstreetmap.org/node/3643451363'])

        self.assert_no_matching_feature(
            16, 10962, 25007, 'pois',
            {'id': 3643451363})

    def test_grave_yard(self):
        # Way 79457493 Grave_yard in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/79457493'])

        self.assert_no_matching_feature(
            15, 5240, 12666, 'pois',
            {'id': 79457493})

    def test_forest(self):
        # Way 64296322 landuse: Forest in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/64296322'])

        self.assert_no_matching_feature(
            10, 163, 392, 'pois',
            {'id': 64296322})

    def test_natural_forest(self):
        # Node:2148541212 natural: Forest in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/2148541212'])

        self.assert_no_matching_feature(
            14, 3942, 5901, 'pois',
            {'id': 2148541212})

    def test_park(self):
        # Node:4206408136 park in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/4206408136'])

        self.assert_no_matching_feature(
            14, 2619, 6333, 'pois',
            {'id': 4206408136})

    def test_protected_area(self):
        # Node:4076680383 protected_area in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/4076680383'])

        self.assert_no_matching_feature(
            14, 2809, 6074, 'pois',
            {'id': 4076680383})

    def test_recreation_ground_way(self):
        # Way:86285084 recreation_ground in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/86285084'])

        self.assert_no_matching_feature(
            14, 2619, 6334, 'pois',
            {'id': 86285084})

    def test_recreation_ground_node(self):
        # Node:582131344 recreation_ground in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/582131344'])

        self.assert_no_matching_feature(
            14, 2621, 6331, 'pois',
            {'id': 582131344})

    def test_village_green(self):
        # Way:28694608 village_green in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/28694608'])

        self.assert_no_matching_feature(
            14, 2618, 6334, 'pois',
            {'id': 28694608})

    def test_water_works(self):
        # Node:3367407023 water_works in POIS
        self.load_fixtures(['http://www.openstreetmap.org/node/3367407023'])

        self.assert_no_matching_feature(
            14, 2627, 6346, 'pois',
            {'id': 3367407023})

    def test_landuse_wood(self):
        # Way:207859675 landuse: wood in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/207859675'])

        self.assert_no_matching_feature(
            14, 2826, 6549, 'pois',
            {'id': 207859675})

    def test_natural_wood(self):
        # Way:372445925 natural: wood in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/372445925'])

        self.assert_no_matching_feature(
            14, 2618, 6330, 'pois',
            {'id': 372445925})

    def test_works(self):
        # Way:164878781 works in POIS
        self.load_fixtures(['http://www.openstreetmap.org/way/164878781'])

        self.assert_no_matching_feature(
            13, 1429, 3247, 'pois',
            {'id': 164878781})
