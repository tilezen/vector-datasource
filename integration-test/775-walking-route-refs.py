# walking route constituent ways should have the walking route properties
# projected onto them.
#
# https://www.openstreetmap.org/way/127908481
# https://www.openstreetmap.org/relation/103942
#   type=route, route=hiking, network=rwn, ref=416
#
# NOTE: it's part of two other relations, but these are not walking/hiking
# routes.
assert_has_feature(
    15, 17571, 11449, 'roads',
    { 'id': 127908481, 'kind': 'path', 'bicyle': type(None),
      'walking_network': 'rwn', 'walking_shield_text': '416',
      'all_walking_networks': [ 'rwn' ],
      'all_walking_shield_texts': [ '416' ]})

# https://www.openstreetmap.org/way/373532611
#   network=nwn, ref="PCT Section H"
# https://www.openstreetmap.org/relation/1225378
#   type=route, route=hiking, network=nwn, ref=PCT
# https://www.openstreetmap.org/relation/1244828
#   type=route, route=foot, network=rwn, ref=JMT
# https://www.openstreetmap.org/relation/1244686
#   type=route, route=foot, network=rwn, ref="", name="PCT - California Section H"
assert_has_feature(
    16, 11044, 25309, 'roads',
    { 'id': 373532611,
      'walking_network': 'nwn', 'walking_shield_text': 'PCT',
      'all_walking_networks': ['nwn', 'nwn', 'rwn', 'rwn'],
      'all_walking_shield_texts' : [ 'PCT', 'PCT Section H', 'JMT', None] })

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
