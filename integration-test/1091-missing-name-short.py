from . import FixtureTest


class MissingNameShort(FixtureTest):
    def test_missouri(self):
        self.load_fixtures([
            'http://www.openstreetmap.org/node/473849775',
        ])

        self.assert_has_feature(
            16, 15917, 25102, 'places',
            {'id': 473849775, 'name:short': 'MO'})
