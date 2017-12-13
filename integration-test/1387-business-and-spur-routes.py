from . import FixtureTest


class BusinessAndSpurRoutes(FixtureTest):

    def test_first_capitol_dr_i70_business(self):
        self.load_fixtures([
            'https://www.openstreetmap.org/relation/1933234',
        ])

        # check that First Capitol Dr, part of the above relation, is given
        # a network that includes the "business" extension.
        self.assert_has_feature(
            16, 16294, 25097, 'roads',
            {'id': 12276055, 'shield_text': '70', 'network': 'US:I:Business'})
