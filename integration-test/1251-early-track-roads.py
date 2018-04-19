from . import FixtureTest


class EarlyUnclassifiedRoads(FixtureTest):

    def test_early_track_road_z11_grade1_paved(self):

        # asphalt, grade1, track (default zoom 11, no demotion)
        self.load_fixtures([
            'https://www.openstreetmap.org/way/329375413',
        ])

        self.assert_has_feature(
            11, 396, 781, 'roads',
            {'kind': 'path',
             'kind_detail': 'track'})

    def test_early_track_road_z11_grade1_dirt(self):

        # dirt, grade1, track (since dirt demoted from zoom 11)
        self.load_fixtures([
            'https://www.openstreetmap.org/way/286309045',
        ])

        self.assert_has_feature(
            11, 399, 782, 'roads',
            {'kind': 'path',
             'kind_detail': 'track'})

    def test_early_track_road_z12_grade1_private(self):

        # private, grade1, track (since private demoted from zoom 11)
        self.load_fixtures([
            'https://www.openstreetmap.org/way/10611894',
        ])

        self.assert_no_matching_feature(
            11, 330, 781, 'roads',
            {'kind': 'path',
             'kind_detail': 'track'})

        self.assert_has_feature(
            12, 661, 1562, 'roads',
            {'kind': 'path',
             'kind_detail': 'track'})

    def test_early_track_road_z12_grade2_dirt(self):

        # dirt, grade2, track (default zoom 12, no demotion)
        self.load_fixtures([
            'https://www.openstreetmap.org/way/330951783',
        ])

        self.assert_has_feature(
            12, 778, 1575, 'roads',
            {'kind': 'path',
             'kind_detail': 'track'})

    def test_remain_z13_track_road_no_grade1(self):

        # gravel, track (no grade so default track at zoom 13)
        self.load_fixtures([
            'https://www.openstreetmap.org/way/313839575',
        ])

        self.assert_has_feature(
            13, 1561, 3146, 'roads',
            {'kind': 'path',
             'kind_detail': 'track'})

    def test_remain_z13_track_road_no_grade2(self):

        # gravel, track (no grade so default track at zoom 13)
        self.load_fixtures([
            'https://www.openstreetmap.org/way/14351002',
        ])

        self.assert_has_feature(
            13, 1500, 3170, 'roads',
            {'kind': 'path',
             'kind_detail': 'track'})

    def test_remain_z13_track_road_grade5_gravel(self):

        # gravel, grade5, track (fails zoom 12 test
        # so default zoom 13 for track)
        self.load_fixtures([
            'https://www.openstreetmap.org/way/10103047',
        ])

        self.assert_has_feature(
            13, 1550, 3167, 'roads',
            {'kind': 'path',
             'kind_detail': 'track'})
