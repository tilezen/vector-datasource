from . import OsmFixtureTest


class RemovePropsRoadMerge(OsmFixtureTest):
    # NOTE: fixtures load up a single element, so this doesn't actually test
    # merging itself, only that we drop the properties (which can lead to
    # more merges).

    def test_drop_oneway_but_not_bridge(self):
        # Way: I 81 (302933871)
        #
        # testing that it dropped oneway, but hasn't dropped is_bridge.
        self.load_fixtures(['http://www.openstreetmap.org/way/302933871'])

        self.assert_has_feature(
            14, 4496, 6381, 'roads',
            {'kind': 'highway', 'oneway': type(None), 'is_bridge': True})

    def test_drop_crossing(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/434308106'])

        self.assert_has_feature(
            14, 4933, 6066, 'roads',
            {'kind': 'path', 'crossing': type(None)})

    def test_drop_sidewalk(self):
        # Way: The Embarcadero (397140734)
        self.load_fixtures(['http://www.openstreetmap.org/way/397140734'])

        self.assert_has_feature(
            14, 2621, 6331, 'roads',
            {'name': 'The Embarcadero', 'kind': 'major_road'})

        self.assert_no_matching_feature(
            14, 2621, 6331, 'roads',
            {'name': 'The Embarcadero', 'kind': 'major_road',
             'sidewalk': None})

    def test_drop_sidewalk_left_and_right(self):
        # Way: Carrie Furnace Boulevard (438362919)
        self.load_fixtures(['http://www.openstreetmap.org/way/438362919'])

        self.assert_has_feature(
            14, 4556, 6178, 'roads',
            {'name': 'Carrie Furnace Blvd.', 'kind': 'major_road'})

        self.assert_no_matching_feature(
            14, 4556, 6178, 'roads',
            {'name': 'Carrie Furnace Blvd.', 'kind': 'major_road',
             'sidewalk_left': None, 'sidewalk_right': None})
