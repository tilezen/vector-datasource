# -*- coding: utf-8 -*-

# New Jersey - New York state boundary
# http://www.openstreetmap.org/relation/224951 (New Jersey)
# http://www.openstreetmap.org/relation/61320 (New York state)
test.assert_has_feature(
    15, 9643, 12327, "boundaries",
    {"kind": "region", "name": "New Jersey - New York",
    "name:right": "New York",      "name:left": "New Jersey",
    "name:right:es": "Nueva York", "name:left:es": "Nueva Jersey",
    "name:right:lv":u"Ņujorka",    "name:left:lv":u"Ņūdžersija"
    })
