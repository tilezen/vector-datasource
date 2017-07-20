# Add surface properties to roads layer (at max zooms)

# restricted access road in military base, Kraków, Poland
# https://www.openstreetmap.org/way/43322699
test.assert_has_feature(
    18, 145574, 88813, 'roads',
    { 'id': 43322699, 'kind': 'minor_road', 'kind_detail': 'service', 'access': 'private'})

test.assert_has_feature(
    14, 9098, 5550, 'roads',
    { 'id': 43322699, 'kind': 'minor_road', 'kind_detail': 'service', 'access': 'private'})

# motorway bridge in Honk-Kong
# http://www.openstreetmap.org/way/276506948#map=18/22.48811/113.94748
# ID may get dropped due to a merge with the other carriageway
test.assert_has_feature(
    12, 3344, 1785, 'roads',
    { 'kind': 'highway', 'kind_detail': 'motorway', 'alt_name:en': 'Shenzhen Bay Bridge', 'access': 'no'})

# cycleway in Gdańsk, Poland
# http://www.openstreetmap.org/way/151351130#map=19/54.32715/18.61035
test.assert_has_feature(
    19, 289247, 167525, 'roads',
    { 'id': 151351130, 'kind': 'path', 'access': 'yes'})
