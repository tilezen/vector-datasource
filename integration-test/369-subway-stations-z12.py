from . import OsmFixtureTest


class SubwayStationsZ12(OsmFixtureTest):
    def test_subway_stations_appear_at_z12(self):
        # 23rd St Station, New York, NY
        self.load_fixtures(['https://www.openstreetmap.org/node/597928317'])

        self.assert_has_feature(
            12, 1206, 1539, 'pois',
            {'kind': 'station'})
