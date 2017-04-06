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
