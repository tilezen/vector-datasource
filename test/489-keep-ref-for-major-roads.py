# just checks that there is at least one major_road with a ref set.
assert_has_feature(
    9, 151, 192, 'roads',
    { 'kind': 'major_road',
      'ref': None })
