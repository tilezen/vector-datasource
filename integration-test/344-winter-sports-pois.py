# ski shop in Big Bear Lake, CA
# https://www.openstreetmap.org/node/2720341705
test.assert_has_feature(
    16, 11488, 26126, 'pois',
    { 'kind': 'ski',
      'name': None })

# Ski-jumping "racetracks" in Lake Placid, NY
# https://www.openstreetmap.org/way/135968166
# https://www.openstreetmap.org/way/135968170
# https://www.openstreetmap.org/way/135968168
test.assert_has_feature(
    16, 19302, 23765, 'roads',
    { 'kind': 'racetrack',
      'leisure': 'track',
      'kind_detail': 'ski_jumping' })
