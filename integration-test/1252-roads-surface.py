# Add surface properties to roads layer (at max zooms)

# Prince St with cobblestones in Alexandria, VA
# https://www.openstreetmap.org/way/190536019
test.assert_has_feature(
    15, 9371, 12546, 'roads',
    { 'id': 190536019, 'kind': 'minor_road', 'surface': 'cobblestone'})

# and that surface property stays at earlier zooms
test.assert_has_feature(
    13, 2342, 3136, 'roads',
    { 'id': 190536019, 'kind': 'minor_road', 'surface': 'cobblestone'})


# motorway in Kraków, Poland
# http://www.openstreetmap.org/way/431783017
test.assert_has_feature(
    12, 2273, 1388, 'roads',
    { 'id': 431783017, 'kind_detail': 'motorway', 'surface': 'asphalt'})


# But strip that surface property off at earlier zooms
test.assert_no_matching_feature(
    7, 71, 43, 'roads',
    { 'kind_detail': 'motorway', 'surface': 'asphalt'})

# track with cycling route in Schartau, Germany
# http://www.openstreetmap.org/way/58691615

test.assert_has_feature(
    15, 17456, 10780, 'roads',
    { 'id': 58691615, 'kind_detail': 'track', 'surface': 'concrete:lanes'})

test.assert_has_feature(
    13, 4364, 2695, 'roads',
    { 'id': 58691615, 'kind_detail': 'track', 'surface': 'concrete:lanes'})

test.assert_has_feature(
    11, 1091, 673, 'roads',
    { 'id': 58691615, 'kind_detail': 'track', 'surface': 'concrete:lanes'})

test.assert_has_feature(
    10, 545, 336, 'roads',
    { 'id': 58691615, 'kind_detail': 'track', 'surface': 'concrete:lanes'})

test.assert_has_feature(
    9, 272, 168, 'roads',
    { 'id': 58691615, 'kind_detail': 'track', 'surface': 'concrete:lanes'})

test.assert_has_feature(
    9, 136, 84, 'roads',
    { 'id': 58691615, 'kind_detail': 'track', 'surface': 'concrete:lanes'})
