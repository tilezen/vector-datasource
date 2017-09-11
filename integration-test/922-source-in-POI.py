from . import OsmFixtureTest


class SourceInPoi(OsmFixtureTest):
    def test_poi_has_source(self):
        # Add source info in POIs
        self.load_fixtures(['https://www.openstreetmap.org/way/423023928'])

        self.assert_has_feature(
            14, 2615, 6330, 'pois',
            {'id': 423023928, 'kind': 'lighthouse',
             'source': 'openstreetmap.org'})
