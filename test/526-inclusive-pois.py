tiles = [
    # healthcare=midwife
    ['17/21000/44983', {'kind': 'midwife'}],

    # amenity={kindergarten, childcare}
    ['16/10470/25342', {'kind': 'kindergarten'}],
    ['17/20956/50676', {'kind': 'childcare'}],

    # emergency=phone
    ['18/41978/101284', {'kind': 'phone'}],

    # amenity=toilets
    ['18/41923/101323', {'kind': 'toilets'}],

    # amenity=social_facility + social_facility=*
    # also with social_facility:for -> for and turned into a list to make it
    # easier to consume.
    ['18/41920/101328', {'kind': 'social_facility', 'for': ['senior', 'disabled']}],
    ['18/41928/101328', {'kind': 'shelter', 'for': ['homeless']}],
    ['17/20967/50661', {'kind': 'shelter', 'for': ['homeless']}],
    ['17/20960/50808', {'kind': 'group_home', 'for': ['senior']}],
    ['18/42119/101622', {'kind': 'assisted_living'}],

    # amenity={clinic, doctors, dentist}
    # also with healthcare:specialty -> specialty and turned into a list to make
    # it easier to consume.
    ['18/41936/101301', {'kind': 'clinic'}],
    ['17/20965/50666', {'kind': 'clinic'}],
    ['18/41923/101349', {'kind': 'doctors'}],
    ['18/41923/101350', {'kind': 'dentist'}],
    ['17/21066/45789', {'kind': 'doctors', 'specialty': ['general']}],
]

for loc, props in tiles:
    z, x, y = map(int, loc.split('/'))
    assert_has_feature(z, x, y, 'pois', props)
