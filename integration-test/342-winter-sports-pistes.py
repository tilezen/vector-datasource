from . import FixtureTest


class WinterSportsPistes(FixtureTest):
    def test_piste_easy(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/313466665'])

        self.assert_has_feature(
            15, 5467, 12531, 'roads',
            {'kind': 'piste',
             'kind_detail': 'downhill',
             'piste_difficulty': 'easy',
             'id': 313466665})

    def test_piste_expert(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/313466720'])

        self.assert_has_feature(
            15, 5467, 12531, 'roads',
            {'kind': 'piste',
             'kind_detail': 'downhill',
             'piste_difficulty': 'expert',
             'id': 313466720})

    def test_piste_intermediate(self):
        # Way: 49'er (313466490)
        self.load_fixtures(['http://www.openstreetmap.org/way/313466490'])

        self.assert_has_feature(
            16, 10939, 25061, 'roads',
            {'kind': 'piste',
             'kind_detail': 'downhill',
             'piste_difficulty': 'intermediate',
             'id': 313466490})
