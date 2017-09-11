from . import OsmFixtureTest


class MilitaryLanduse(OsmFixtureTest):
    def test_naval_station(self):
        # Naval Weapons Station Concord, CA
        self.load_fixtures(['https://www.openstreetmap.org/way/154836419'])

        self.assert_has_feature(
            16, 10553, 25274, 'landuse', {'kind': 'military'})
