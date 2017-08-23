from . import OsmFixtureTest


class EarlyFootway(OsmFixtureTest):

    def test_footway_unnamed_national(self):
        # highway=footway, no name, route national (Pacific Crest Trail)
        self._run_test(
            ['https://www.openstreetmap.org/way/83076573',
             'https://www.openstreetmap.org/relation/1225378'],
            11, 344, 790)

        # highway=footway, no name, route national (Pacific Crest Trail)
        self._run_test([
            'https://www.openstreetmap.org/way/372066789',
            'https://www.openstreetmap.org/relation/1225378',
        ], 11, 345, 790)

    def test_footway_unnamed_regional(self):
        # highway=footway, with name, and route regional (Rodeo Valley Trail, Marin)
        self._run_test([
            'https://www.openstreetmap.org/way/239141479',
            'https://www.openstreetmap.org/relation/2684235',
        ], 12, 654, 1582)

    def test_footway_with_designation(self):
        # highway=footway, with designation (Ocean Beach north, SF)
        self._run_test([
            'https://www.openstreetmap.org/way/161702316',
        ], 13, 1308, 3166)

    def test_footway_with_name(self):
        # highway=footway, with name (Coastal Trail, Marin)
        self._run_test([
            'https://www.openstreetmap.org/way/24526324',
        ], 13, 1308, 3164)

        # highway=footway, with name (Coastal Trail, SF)
        self._run_test([
            'https://www.openstreetmap.org/way/27553452',
        ], 13, 1308, 3166)

        # highway=footway, with name (Lovers Lane, SF)
        self._run_test([
            'https://www.openstreetmap.org/way/69020102',
        ], 13, 1309, 3165)

    def test_sidewalk(self):
        # SF State
        self.load_fixtures(['https://www.openstreetmap.org/way/346093021'])

        self.assert_no_matching_feature(
            14, 2617, 6335, 'roads',
            {'kind': 'path', 'footway': 'sidewalk'})

        self.assert_has_feature(
            15, 5235, 12671, 'roads',
            {'kind': 'path', 'footway': 'sidewalk'})

    def test_crossing(self):
        # SF in the Avenues
        self.load_fixtures(['https://www.openstreetmap.org/way/344205837'])

        self.assert_no_matching_feature(
            14, 2617, 6333, 'roads',
            {'id': 344205837, 'kind': 'path', 'footway': 'sidewalk'})

        self.assert_has_feature(
            15, 5234, 12667, 'roads',
            {'kind': 'path', 'footway': 'crossing'})

    def _run_test(self, urls, z, x, y):
        self.load_fixtures(urls)

        self.assert_has_feature(
            z, x, y, 'roads',
            {'kind_detail': 'footway'})
