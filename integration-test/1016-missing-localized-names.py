# -*- coding: utf-8 -*-

# New Jersey - New York state boundary
# http://www.openstreetmap.org/relation/224951 (New Jersey)
# http://www.openstreetmap.org/relation/61320 (New York state)
assert_has_feature(
    15, 9643, 12327, "boundaries",
    {"kind": "region", "name": "New York - New Jersey",
    "name:left": "New York",      "name:right": "New Jersey",
    "name:left:es": "Nueva York", "name:right:es": "Nueva Jersey",
    "name:left:lv":u"Ņujorka",    "name:right:lv":u"Ņūdžersija"
    })
