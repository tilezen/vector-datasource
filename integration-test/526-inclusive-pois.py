tiles = [
    # healthcare=midwife
    #https://www.openstreetmap.org/node/3761053357
    ['16/10500/22491', {'kind': 'midwife'}],

    # amenity={kindergarten, childcare}
    #https://www.openstreetmap.org/node/4105506789
    #https://www.openstreetmap.org/way/378041773
    ['16/19302/24658', {'kind': 'kindergarten'}],
    ['16/10478/25338', {'kind': 'childcare'}],

    # emergency=phone
    #https://www.openstreetmap.org/node/2456072777
    ['16/10494/25321', {'kind': 'phone'}],

    # amenity=toilets
    #https://www.openstreetmap.org/node/3931486668
    ['16/10480/25330', {'kind': 'toilets'}],

    # amenity=social_facility + social_facility=*
    # also with social_facility:for -> for and turned into a list to make it
    # easier to consume.
    #https://www.openstreetmap.org/node/1126947892
    #https://www.openstreetmap.org/way/121024970
    #https://www.openstreetmap.org/node/3009189224
    #https://www.openstreetmap.org/way/243357053
    #https://www.openstreetmap.org/way/377082896
    #https://www.openstreetmap.org/node/358816623
    ['16/10480/25332', {'kind': 'social_facility', 'for': ['aids']}],
    ['16/10480/25332', {'kind': 'group_home', 'for': ['senior', 'disabled']}],
    ['16/10482/25332', {'kind': 'shelter', 'for': ['homeless']}],
    ['16/10483/25330', {'kind': 'shelter', 'for': ['homeless']}],
    ['16/10480/25404', {'kind': 'group_home', 'for': ['senior']}],
    ['16/10529/25405', {'kind': 'assisted_living'}],

    # amenity={clinic, doctors, dentist}
    # also with healthcare:speciality -> speciality and turned into a list to make
    # it easier to consume.
    #https://www.openstreetmap.org/node/417237471
    #https://www.openstreetmap.org/way/261102266
    #https://www.openstreetmap.org/node/3133693825
    #https://www.openstreetmap.org/node/3163318863
    #https://www.openstreetmap.org/node/3366375212
    ['16/10484/25325', {'kind': 'clinic'}],
    ['16/10482/25333', {'kind': 'clinic'}],
    ['16/10480/25337', {'kind': 'doctors'}],
    ['16/10480/25337', {'kind': 'dentist'}],
    ['16/33281/22391', {'kind': 'doctors', 'speciality': ['general']}],
]

for loc, props in tiles:
    z, x, y = map(int, loc.split('/'))
    test.assert_has_feature(z, x, y, 'pois', props)
