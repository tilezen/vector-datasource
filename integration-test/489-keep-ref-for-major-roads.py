# just checks that there is at least one major_road with a ref set.
# RAW QUERY: way(40.4553,-73.8391,41.0068,-73.1167)[highway=motorway];>;
# RAW QUERY: way(40.4553,-73.8391,41.0068,-73.1167)[highway=trunk];>;
# RAW QUERY: way(40.4553,-73.8391,41.0068,-73.1167)[highway=primary];>;
test.assert_has_feature(
    9, 151, 192, 'roads',
    { 'kind': 'major_road',
      'ref': None })
