from . import FixtureTest


class PowerLines(FixtureTest):

    def test_power_line(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/29399873'])

        self.assert_has_feature(
            14, 2621, 6338, 'landuse',
            {'id': 29399873, 'kind': 'power_line', 'min_zoom': 14,
             'sort_rank': 272})

    def test_power_line2(self):
        self.load_fixtures(['http://www.openstreetmap.org/way/444660087'])

        self.assert_has_feature(
            16, 10485, 25335, 'landuse',
            {'id': 444660087, 'kind': 'power_minor_line', 'min_zoom': 17,
             'sort_rank': 271})
