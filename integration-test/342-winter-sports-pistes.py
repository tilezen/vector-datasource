# http://www.openstreetmap.org/way/313466665
test.assert_has_feature(
    15, 5467, 12531, 'roads',
    { 'kind': 'piste',
      'kind_detail': 'downhill',
      'piste_difficulty': 'easy',
      'id': 313466665 })

# http://www.openstreetmap.org/way/313466720
test.assert_has_feature(
    15, 5467, 12531, 'roads',
    { 'kind': 'piste',
      'kind_detail': 'downhill',
      'piste_difficulty': 'expert',
      'id': 313466720 })

# Way: 49'er (313466490) http://www.openstreetmap.org/way/313466490
test.assert_has_feature(
    16, 10939, 25061, 'roads',
    { 'kind': 'piste',
      'kind_detail': 'downhill',
      'piste_difficulty': 'intermediate',
      'id': 313466490 })
