from . import OsmFixtureTest


class LessLanduseBuildingLabelPlacements(OsmFixtureTest):
    def test_pier(self):
        # The landuse for a pier
        self.load_fixtures(['http://www.openstreetmap.org/way/82206919'])

        self.assert_no_matching_feature(
            14, 2620, 6330, 'landuse',
            {'id': 82206919, 'kind': 'pier', 'label_placement': True})

        self.assert_has_feature(
            15, 5240, 12661, 'landuse',
            {'id': 82206919, 'kind': 'pier', 'label_placement': True})

    def test_building(self):
        # The building known as 650 California Street
        self.load_fixtures(['http://www.openstreetmap.org/way/260520160'])

        self.assert_no_matching_feature(
            15, 5242, 12663, 'buildings',
            {'id': 260520160, 'kind': 'building', 'label_placement': True})

        self.assert_has_feature(
            16, 10484, 25326, 'buildings',
            {'id': 260520160, 'kind': 'building', 'label_placement': True})
