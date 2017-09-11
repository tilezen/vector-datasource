from . import OsmFixtureTest


class MissingBuildingPart(OsmFixtureTest):
    def test_building_part_exists(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/287494678'])

        self.assert_has_feature(
            16, 19298, 24632, 'buildings',
            {'kind': 'building_part',
             'id': 287494678,
             'min_zoom': 16})
