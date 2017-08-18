# -*- coding: utf-8 -*-
from . import OsmFixtureTest


class MissingLocalizedNames(OsmFixtureTest):
    def test_nj_ny_state_boundary(self):
        # New Jersey - New York state boundary
        self.load_fixtures([
            'http://www.openstreetmap.org/relation/224951',
            'http://www.openstreetmap.org/relation/61320',
        ])

        self.assert_has_feature(
            15, 9643, 12327, "boundaries",
            {"kind": "region", "name": "New Jersey - New York",
             "name:right": "New York", "name:left": "New Jersey",
             "name:right:es": "Nueva York", "name:left:es": "Nueva Jersey",
             "name:right:lv": u"Ņujorka", "name:left:lv": u"Ņūdžersija"})
