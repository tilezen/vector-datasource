import dsl

from . import FixtureTest


class EarlyFootway(FixtureTest):

    def test_footway_unnamed_national(self):
        # highway=footway, no name, route national (Pacific Crest Trail)
        self.generate_fixtures(
            dsl.way(83076573, dsl.tile_diagonal(14, 2760, 6326), {
                'source': 'openstreetmap.org',
                'highway': 'footway',
                'foot': 'yes',
                'bicycle': 'no',
                'ref': 'PCT',
            }),
            dsl.relation(1225378, {
                'source': 'openstreetmap.org',
                'type': 'route',
                'route': 'hiking',
                'network': 'nwn',
                'ref': 'PCT',
                'name': 'Pacific Crest Trail',
            }, ways=[83076573]),
        )

        self.assert_has_feature(
            14, 2760, 6326, 'roads',
            {'kind_detail': 'footway'})

        # highway=footway, no name, route national (Pacific Crest Trail)
        self.generate_fixtures(
            dsl.way(372066789, dsl.tile_diagonal(14, 2760, 6320), {
                'source': 'openstreetmap.org',
                'highway': 'footway',
                'foot': 'yes',
                'bicycle': 'no',
                'ref': 'PCT',
            }),
            dsl.relation(1225378, {
                'source': 'openstreetmap.org',
                'type': 'route',
                'route': 'hiking',
                'network': 'nwn',
                'ref': 'PCT',
                'name': 'Pacific Crest Trail',
            }, ways=[372066789]),
        )

        self.assert_has_feature(
            14, 2760, 6320, 'roads',
            {'kind_detail': 'footway'})

    def test_footway_unnamed_regional(self):
        # highway=footway, with name, and route regional (Rodeo Valley
        # Trail, Marin)

        z, x, y = (14, 2616, 6328)

        self.generate_fixtures(
            dsl.way(239141479, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org',
                'bicycle': 'no',
                'highway': 'footway',
                'horse': 'yes',
                'name': 'Rodeo Valley Trail',
            }),
            dsl.relation(2684235, {
                'source': 'openstreetmap.org',
                'type': 'route',
                'route': 'hiking',
                'network': 'rwn',
                'ref': 'BAR',
                'name': 'Bay Area Ridge Trail',
            }, ways=[239141479]),
        )

        self.assert_has_feature(
            z, x, y, 'roads',
            {'kind_detail': 'footway'})

    def test_footway_with_designation(self):
        # highway=footway, with designation (Ocean Beach north, SF)
        self._run_test([
            'https://www.openstreetmap.org/way/287653460',
        ], 13, 1308, 3166)

    def test_footway_with_name(self):
        # highway=footway, with name (Coastal Trail, Marin)
        self.generate_fixtures(
            dsl.way(24526324, dsl.tile_diagonal(13, 1308, 3164), {
                'access': 'yes', 'bicycle': 'no', 'horse': 'no',
                'foot': 'yes', 'highway': 'footway', 'motor_vehicle': 'no',
                'name': 'Slacker Trail', 'operator': 'South California Trails',
                'sidewalk': 'no', 'surface': 'dirt', 'source': 'openstreetmap.org'
            }),
        )

        self.assert_has_feature(
            13, 1308, 3164, 'roads',
            {'kind_detail': 'footway'})

        # highway=footway, with name (Coastal Trail, SF)
        self.generate_fixtures(
            # https://www.openstreetmap.org/way/24526324
            dsl.way(24526324, dsl.tile_diagonal(13, 1308, 3164), {
                'bicycle': 'yes', 'dog': 'yes', 'highway': 'footway',
                'name': 'Coastal Trail', 'surface': 'unpaved',
                'source': 'openstreetmap.org'
            }),
        )

        self.assert_has_feature(
            13, 1308, 3164, 'roads',
            {'kind_detail': 'footway'})

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
