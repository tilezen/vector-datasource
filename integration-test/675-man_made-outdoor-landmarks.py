from . import FixtureTest


class ManMadeOutdoorLandmarks(FixtureTest):
    def test_communications_tower(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/1230069003'])

        self.assert_has_feature(
            15, 5285, 12654, 'pois',
            {'kind': 'communications_tower', 'min_zoom': 15})

    def test_observatory(self):
        # ideally the landuse would show up at zoom 13, but that's sparse
        # coverage most features are buildings, some of which are incorrectly
        # tagged (should be telescope)
        self.load_fixtures(['http://www.openstreetmap.org/node/747693102'])

        self.assert_has_feature(
            15, 9504, 12490, 'pois',
            {'kind': 'observatory', 'min_zoom': 15})

    def test_telescope_node(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/258205070'])

        self.assert_has_feature(
            16, 10623, 25430, 'pois',
            {'kind': 'telescope', 'min_zoom': 16})

    def test_telescope_way(self):
        # If someone took the time to digitize a building, promote it up
        self.load_fixtures(['https://www.openstreetmap.org/way/53055408'])

        self.assert_has_feature(
            15, 5324, 12781, 'pois',
            {'kind': 'telescope', 'min_zoom': 15})

    def test_offshore_platform_node(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/2622856034'])

        self.assert_has_feature(
            13, 1409, 3281, 'pois',
            {'kind': 'offshore_platform', 'min_zoom': 13})

    def test_offshore_platform_way(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/346405529'])

        self.assert_has_feature(
            13, 1367, 3261, 'pois',
            {'kind': 'offshore_platform', 'min_zoom': 13})

        self.load_fixtures(['http://www.openstreetmap.org/way/446514311'])

        self.assert_has_feature(
            13, 5399, 1881, 'pois',
            {'kind': 'offshore_platform', 'min_zoom': 13, 'id': 446514311})

    def test_water_tower(self):
        self.load_fixtures(['http://www.openstreetmap.org/node/1501843094'])

        self.assert_has_feature(
            15, 5240, 12673, 'pois',
            {'kind': 'water_tower', 'min_zoom': 15})

    def test_mast(self):
        # This isn't part of the work, but because we split water_tower
        # off from mast, we should test mast still shows up
        self.load_fixtures(['https://www.openstreetmap.org/node/3679715072'])

        self.assert_has_feature(
            16, 10588, 25442, 'pois',
            {'kind': 'mast', 'min_zoom': 17})
