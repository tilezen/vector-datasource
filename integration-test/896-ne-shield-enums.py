# Trans-Canada Highway
assert_has_feature(
    7, 20, 43, 'roads',
    { 'source': 'naturalearthdata.com', 'network': 'CA:??:primary',
      'kind': 'highway', 'shield_text': '1' })

# I-20
assert_has_feature(
    7, 35, 51, 'roads',
    { 'source': 'naturalearthdata.com', 'network': 'US:I',
      'kind': 'highway', 'shield_text': '20' })

# US-76
assert_has_feature(
    7, 35, 51, 'roads',
    { 'source': 'naturalearthdata.com', 'network': 'US:US',
      'kind': 'major_road', 'shield_text': '76' })

# MEX 49 (interstate)
assert_has_feature(
    7, 27, 55, 'roads',
    { 'source': 'naturalearthdata.com', 'network': 'MX',
      'kind': 'highway', 'shield_text': '49' })

# MEX 54 (federal)
assert_has_feature(
    7, 27, 55, 'roads',
    { 'source': 'naturalearthdata.com', 'network': 'MX:MX',
      'kind': 'major_road', 'shield_text': '54' })

# E80 in Turkey
assert_has_feature(
    7, 74, 47, 'roads',
    { 'source': 'naturalearthdata.com', 'network': 'e-road',
      'kind': 'highway', 'shield_text': '80' })

# E30 (M4) in UK
assert_has_feature(
    7, 63, 42, 'roads',
    { 'source': 'naturalearthdata.com', 'network': 'e-road',
      'kind': 'highway', 'shield_text': '30' })

# SH16 in NZ
assert_has_feature(
    7, 126, 78, 'roads',
    { 'source': 'naturalearthdata.com', 'network': 'NZ:SH',
      'kind': 'highway', 'shield_text': '16' })
