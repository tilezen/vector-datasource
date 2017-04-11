# https://www.openstreetmap.org/way/417097119
# https://www.openstreetmap.org/relation/3002741
#   type=route, route=bus, network="", ref=23
# https://www.openstreetmap.org/relation/32312
#   type=route, route=bicycle, network=lcn, ref=50
# https://www.openstreetmap.org/relation/1976278
#   type=route, route=road, network=US:CA, ref=35
assert_has_feature(
    16, 10469, 25340, 'roads',
    { 'id': 417097119,
      'network': 'US:CA',
      'shield_text': '35',
      'bicycle_network': 'lcn',
      'bicycle_shield_text': '50',
      'bus_network': type(None),
      'bus_shield_text': '23' })

# Jackson St. SF, part of trolley-bus route 3
# http://www.openstreetmap.org/way/225516711
# http://www.openstreetmap.org/relation/2980505
#   outbound
# http://www.openstreetmap.org/relation/2980504
#   inbound
assert_has_feature(
    16, 10477, 25327, 'roads',
    { 'id': 225516711,
      'trolleybus_network': type(None),
      'trolleybus_shield_text': '3',
      'all_trolleybus_networks': [None, None],
      'all_trolleybus_shield_texts': ['3', '3'] })

# make sure the all_* lists are gone by zoom 12 on major roads, but the "most
# important" network & shield text remain until.
assert_has_feature(
    10, 163, 395, 'roads',
    { 'trolleybus_network': type(None),
      'trolleybus_shield_text': '3' })
assert_no_matching_feature(
    10, 163, 395, 'roads',
    { 'all_trolleybus_networks': None })
assert_no_matching_feature(
    10, 163, 395, 'roads',
    { 'all_trolleybus_shield_texts': None })
