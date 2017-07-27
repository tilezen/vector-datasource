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
#
# the track is part of this NCN relation, which needs to be present for the
# min zoom to be assigned correctly.
# http://www.openstreetmap.org/relation/2599024

# first, test at high zoom, where we do not expect the road to be merged,
# so should still retain its original ID.
test.assert_has_feature(
    15, 17456, 10780, 'roads',
    { 'id': 58691615, 'kind_detail': 'track', 'surface': 'concrete_lanes'})

# check at a bunch of lower zooms, where we're expecting the road to be
# merged, so be stricter with the set of properties we expect to see.
for z in (13, 11, 10, 9, 8):
    delta_z = 15 - z
    coord_scale = 2 ** delta_z

    props = {
        'kind': 'path',
        'kind_detail': 'track',
        'is_bicycle_related': True,
        'surface': 'concrete_lanes',
        'bicycle_network': 'ncn',
        'min_zoom': 8,
        'bicycle_shield_text': 'D10',
    }

    test.assert_has_feature(
        z, 17456 / coord_scale, 10780 / coord_scale, 'roads', props)
