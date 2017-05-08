# I think we should remove for v1 (and never should be been included at zoom
# less than 7 anyhow):
#
# Remove properties:
#  * level
#  * namealt
#  * namealtt
#
# E30 (M4) in UK
test.assert_no_matching_feature(
    7, 63, 42, 'roads',
    { 'source': 'naturalearthdata.com', 'kind': 'highway',
      'level': None })
test.assert_no_matching_feature(
    7, 63, 42, 'roads',
    { 'source': 'naturalearthdata.com', 'kind': 'highway',
      'namealt': None })
test.assert_no_matching_feature(
    7, 63, 42, 'roads',
    { 'source': 'naturalearthdata.com', 'kind': 'highway',
      'namealtt': None })

# network & shield text should stay on highways at lower zooms.
# E30 (M4) in UK
for z in range(5, 6):
    # tile 7/63/42 was tested in 896-ne-shield-enums.py
    x = 63 >> (7 - z)
    y = 42 >> (7 - z)
    test.assert_has_feature(
        z, x, y, 'roads',
        { 'source': 'naturalearthdata.com', 'network': 'e-road',
          'kind': 'highway', 'shield_text': '30' })
    # but not name, ref or all_*
    for prop in ['name', 'ref', 'all_networks', 'all_shield_texts']:
        test.assert_no_matching_feature(z, x, y, 'roads', { prop: None })
