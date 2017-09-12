from . import FixtureTest


class MergeOceanEarth(FixtureTest):
    def test_ne_water(self):
        # There should be a single, merged feature in each of these tiles
        # Natural Earth
        self.load_fixtures([
            'file://integration-test/fixtures/ne_10m_ocean/'
            '1030-invalid-wkb-polygon.shp',
        ])

        self.assert_less_than_n_features(
            5, 12, 11, 'water', {'kind': 'ocean'}, 2)

    def test_ne_earth(self):
        self.load_fixtures([
            'file://integration-test/fixtures/ne_10m_land/'
            '399-ne_10m_land.shp',
        ])

        self.assert_less_than_n_features(
            5, 8, 11, 'earth', {'kind': 'earth'}, 2)

    def test_osm_water(self):
        # OpenStreetMap
        self.load_fixtures([
            'file://integration-test/fixtures/water_polygons/'
            '976-fractional-pois.shp',
        ])

        self.assert_less_than_n_features(
            9, 167, 186, 'water', {
                'kind': 'ocean'}, 2)

    def test_osm_earth(self):
        self.load_fixtures([
            'file://integration-test/fixtures/land_polygons/'
            '399-earth-fixture.shp',
        ])

        self.assert_less_than_n_features(
            9, 170, 186, 'earth', {
                'kind': 'earth'}, 2)
