from . import OsmFixtureTest


class NormalizeBuildingKind(OsmFixtureTest):
    def test_office(self):
        self.load_fixtures(['https://www.openstreetmap.org/way/431358377'])

        self.assert_has_feature(
            16, 55897, 25449, 'buildings',
            {'id': 431358377, 'kind': 'building', 'kind_detail': 'office'})

    def test_apartments(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/264768910'])

        self.assert_has_feature(
            16, 19298, 24633, 'buildings',
            {'id': 264768910, 'kind': 'building', 'kind_detail': 'apartments'})

    def test_transportation(self):
        # Way: Forest Hill (136822046)
        self.load_fixtures(['http://www.openstreetmap.org/way/136822046'])

        self.assert_has_feature(
            16, 10474, 25337, 'buildings',
            {'id': 136822046, 'kind': 'building',
             'kind_detail': 'transportation'})

    def test_building_no_detail(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/93817368'])

        self.assert_has_feature(
            16, 10487, 25327, 'buildings',
            {'id': 93817368, 'kind': 'building', 'kind_detail': type(None)})

    def test_building_part_no_detail(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/132605515'])

        self.assert_has_feature(
            16, 10482, 25331, 'buildings',
            {'id': 132605515, 'kind': 'building_part',
             'kind_detail': type(None)})

        self.load_fixtures(['http://www.openstreetmap.org/way/406710839'])

        self.assert_has_feature(
            16, 10486, 25326, 'buildings',
            {'id': 406710839, 'kind': 'building_part',
             'kind_detail': type(None)})

    def test_steps(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/257920199'])

        self.assert_has_feature(
            16, 18743, 25070, 'buildings',
            {'id': 257920199, 'kind': 'building_part', 'kind_detail': 'steps'})

        self.load_fixtures(['http://www.openstreetmap.org/way/352508405'])

        self.assert_has_feature(
            16, 29704, 27412, 'buildings',
            {'id': 352508405, 'kind': 'building_part', 'kind_detail': 'steps'})
