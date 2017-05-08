# Add surface properties to roads layer (at max zooms)

# Prince St with cobblestones in Alexandria, VA
# https://www.openstreetmap.org/way/190536019
test.assert_has_feature(
    15, 9371, 12546, 'roads',
    { 'id': 190536019, 'kind': 'minor_road', 'surface': 'cobblestone'})

# But strip that surface property off at earlier zooms
test.assert_no_matching_feature(
    13, 2342, 3136, 'roads',
    { 'surface': 'cobblestone'})