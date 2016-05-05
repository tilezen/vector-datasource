assert_has_feature(
    11, 328, 793, 'places',
    { 'kind': {'city', 'town'},
      'population': int })

assert_has_feature(
    7, 20, 49, 'places',
    { 'kind': 'city', 'state_capital': 'yes',
      'population': int })
