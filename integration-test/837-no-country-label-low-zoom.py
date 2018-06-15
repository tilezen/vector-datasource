from . import FixtureTest


class NoCountryLabelLowZoom(FixtureTest):
    def test_no_country_label_at_low_zoom(self):
        # United States
        self.load_fixtures(['http://www.openstreetmap.org/node/424317935'])

        self.assert_no_matching_feature(
            0, 0, 0, 'places', {'kind': 'country'})

        # see integration-test/977-min-zoom-from-ne-join.py -- we now get this
        # information from joining on the Natural Earth countries table.
