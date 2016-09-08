# I think we should remove for v1 (and never should be been included at zoom
# less than 7 anyhow):
#
# Remove properties:
#  * level
#  * namealt
#  * namealtt
#
# E30 (M4) in UK
assert_no_matching_feature(
    7, 63, 42, 'roads',
    { 'source': 'naturalearthdata.com', 'kind': 'highway',
      'level': None })
assert_no_matching_feature(
    7, 63, 42, 'roads',
    { 'source': 'naturalearthdata.com', 'kind': 'highway',
      'namealt': None })
assert_no_matching_feature(
    7, 63, 42, 'roads',
    { 'source': 'naturalearthdata.com', 'kind': 'highway',
      'namealtt': None })
