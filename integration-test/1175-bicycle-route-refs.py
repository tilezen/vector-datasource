# https://www.openstreetmap.org/way/417389551
#   lcn_ref=45
# https://www.openstreetmap.org/relation/32310
#   type=route, route=bicycle, network=lcn, ref=45
test.assert_has_feature(
    16, 10481, 25336, 'roads',
    { 'id': 417389551,
      'bicycle_network': None,
      'bicycle_shield_text': '45',
      'all_bicycle_networks': None,
      'all_bicycle_shield_texts': ['45'] })

# make sure the all_* lists are gone by zoom 12 on major roads, but the "most
# important", singular network & shield text remain at earlier zooms
test.assert_has_feature(
    10, 163, 395, 'roads',
    { 'bicycle_network': None,
      'bicycle_shield_text': '45' })

test.assert_no_matching_feature(
    12, 655, 1583, 'roads',
    { 'all_bicycle_networks': None })
test.assert_no_matching_feature(
    12, 655, 1583, 'roads',
    { 'all_bicycle_shield_texts': None })
