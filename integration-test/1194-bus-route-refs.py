# https://www.openstreetmap.org/way/417097119
# https://www.openstreetmap.org/relation/3002741
#   type=route, route=bus, network="", ref=23
# https://www.openstreetmap.org/relation/32312
#   type=route, route=bicycle, network=lcn, ref=50
# https://www.openstreetmap.org/relation/1976278
#   type=route, route=road, network=US:CA, ref=35
test.assert_has_feature(
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
test.assert_has_feature(
    16, 10477, 25327, 'roads',
    { 'id': 225516711,
      'bus_network': type(None),
      'bus_shield_text': '3',
      'all_bus_networks': [None, None],
      'all_bus_shield_texts': ['3', '3'] })

# make sure the all_* lists are gone by zoom 12 on major roads, but the "most
# important", singular network & shield text remain at earlier zooms
#
# note that it doesn't matter what the bus shield is - that's data-dependent.
# for the purposes of the test, we only care that there _is_ one.
test.assert_has_feature(
    10, 163, 395, 'roads',
    { 'bus_network': type(None),
      'bus_shield_text': None })

test.assert_no_matching_feature(
    12, 654, 1583, 'roads',
    { 'all_bus_networks': None })
test.assert_no_matching_feature(
    12, 654, 1583, 'roads',
    { 'all_bus_shield_texts': None })
