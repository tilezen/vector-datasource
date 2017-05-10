# Add source info in POIs

# https://www.openstreetmap.org/way/423023928
test.assert_has_feature(
    14, 2615, 6330, 'pois',
    {'id': 423023928, 'kind': 'lighthouse', 'source':'openstreetmap.org'})
