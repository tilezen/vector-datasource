# Wine, New York, NY
#https://www.openstreetmap.org/node/2549960970
test.assert_has_feature(
    16, 19298, 24632, 'pois',
    { 'kind': 'wine' })

# Alcohol, San Francisco, CA
#https://www.openstreetmap.org/node/1713269631
test.assert_has_feature(
    16, 10480, 25336, 'pois',
    { 'kind': 'alcohol' })
