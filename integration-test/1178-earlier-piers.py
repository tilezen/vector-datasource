# a very, very large pier which alters the coastline visually, so should
# be kept until z11.
#
# http://www.openstreetmap.org/way/377915546
test.assert_has_feature(
    11, 1714, 876, 'landuse',
    { 'id': 377915546, 'kind': 'pier', 'min_zoom': 11})

# zoom 11 for Cruise Terminal with area 53,276
# http://www.openstreetmap.org/way/275609726
test.assert_has_feature(
    11, 357, 826, 'landuse',
    { 'id': 275609726, 'kind': 'pier', 'min_zoom': 11.22})

# zoom 12 for Broadway Pier with area 17,856
# http://www.openstreetmap.org/way/275609725
test.assert_has_feature(
    12, 714, 1653, 'landuse',
    { 'id': 275609725, 'kind': 'pier', 'min_zoom': 12})

# zoom 12 for unnamed pier with area 4,734
# http://www.openstreetmap.org/way/275609722
test.assert_has_feature(
    12, 714, 1653, 'landuse',
    { 'id': 275609722, 'kind': 'pier', 'min_zoom': 12.96})
