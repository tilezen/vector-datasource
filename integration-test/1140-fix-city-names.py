# -*- coding: utf-8 -*-

# data is in the fixture ne_10m_populated_places/1140-fix-city-names.shp
test.assert_has_feature(
    7, 38, 45, 'places',
    { 'name': 'Québec', 'source': 'naturalearthdata.com' })

# this one has an interesting character outside of the extended latin
# charset, so hopefully will test an extra path from just acute characters
# and umlauts.
test.assert_has_feature(
    7, 57, 32, 'places',
    { 'name': 'Sauðárkrókur', 'source': 'naturalearthdata.com' })

# ditto interesting character
test.assert_has_feature(
    7, 8, 27, 'places',
    { 'name': 'Utqiaġvik', 'source': 'naturalearthdata.com' })
