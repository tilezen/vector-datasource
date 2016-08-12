# US 101, "James Lick Freeway"
# http://www.openstreetmap.org/way/27183379
# http://www.openstreetmap.org/relation/108619
assert_has_feature(
    16, 10484, 25334, 'roads',
    { 'kind': 'highway', 'network': 'US:US', 'id': 27183379,
      'shield_text': '101' })

# I-77, I-81, US-11 & US-52 all in one road West Virginia.
#
# http://www.openstreetmap.org/way/51388984
# http://www.openstreetmap.org/relation/2309416
# http://www.openstreetmap.org/relation/2301037
# http://www.openstreetmap.org/relation/2297359
# http://www.openstreetmap.org/relation/1027748
assert_has_feature(
    16, 18022, 25522, 'roads',
    { 'kind': 'highway', 'network': 'US:I', 'id': 51388984,
      'shield_text': '77',
      'all_networks': ['US:I', 'US:I', 'US:US', 'US:US'],
      'all_shield_texts': ['77', '81', '11', '52'] })
