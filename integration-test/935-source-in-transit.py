from . import OsmFixtureTest


class SourceInTransit(OsmFixtureTest):
    def test_source_in_transit(self):
        # Add source info in transit
        # Way: 189011731
        self.load_fixtures(['http://www.openstreetmap.org/way/189011731'])

        self.assert_has_feature(
            16, 10487, 25332, 'transit',
            {'id': 189011731, 'kind': 'platform',
             'source': 'openstreetmap.org'})
