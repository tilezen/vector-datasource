from . import OsmFixtureTest


class CrosswalkSidewalk(OsmFixtureTest):
    def test_crossing_traffic_signals(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/444491374'])

        self.assert_has_feature(
            16, 10475, 25332, 'roads',
            {'id': 444491374, 'kind': 'path', 'crossing': 'traffic_signals'})

    def test_major_road_sidewalk_separate(self):
        # Way: The Embarcadero (397140734)
        self.load_fixtures(['http://www.openstreetmap.org/way/397140734'])

        self.assert_has_feature(
            16, 10486, 25326, 'roads',
            {'id': 397140734, 'kind': 'major_road', 'sidewalk': 'separate'})

    def test_major_road_no_sidewalk_right(self):
        # Way: Carrie Furnace Boulevard (438362919)
        self.load_fixtures(['http://www.openstreetmap.org/way/438362919'])

        self.assert_has_feature(
            16, 18225, 24712, 'roads',
            {'id': 438362919, 'kind': 'major_road',
             'sidewalk_left': 'sidepath', 'sidewalk_right': 'no'})
