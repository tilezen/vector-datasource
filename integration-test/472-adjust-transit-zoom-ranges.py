# SFO-Pittsburg/Bay Point BART
#https://www.openstreetmap.org/relation/2827684
test.assert_has_feature(
    8, 40, 98, 'transit',
    { 'kind': 'subway' })

# N-Judah Muni
#https://www.openstreetmap.org/relation/63223
test.assert_has_feature(
    9, 81, 197, 'transit',
    { 'kind': 'light_rail' })

# F-Market & Wharves tram
#https://www.openstreetmap.org/relation/2007934
test.assert_has_feature(
    9, 81, 197, 'transit',
    { 'kind': 'tram' })
