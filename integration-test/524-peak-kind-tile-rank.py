# the tile 11/420/779 contains all the peaks below. so many, it seems, that
# they ran out of names!
#
# not all of these should appear in the output tile - and they should be ranked
# according to the elevation descending.
#
# elev,                    url,                       name
# 2991, https://www.openstreetmap.org/node/358914475, Shock Hill
# 3019, https://www.openstreetmap.org/node/358914488, Barney Ford Hill
# 3062, https://www.openstreetmap.org/node/358914492, Little Mountain
# 3187, https://www.openstreetmap.org/node/358914480, Gibson Hill
# 3259, https://www.openstreetmap.org/node/358914483, Prospect Hill
# 3479, https://www.openstreetmap.org/node/358914525, Mount Argentine
# 3638, https://www.openstreetmap.org/node/358914415, Gold Hill
# 3763, https://www.openstreetmap.org/node/358914356, Mayflower Hill
# 3835, https://www.openstreetmap.org/node/358914437, Tenmile Range Peak 6
# 3857, https://www.openstreetmap.org/node/358914444, Tenmile Range Peak 7
# 3943, https://www.openstreetmap.org/node/358914424, Little Bartlett Mountain
# 3955, https://www.openstreetmap.org/node/324759328, Peak 8
# 3992, https://www.openstreetmap.org/node/358914502, Peak 9
# 4016, https://www.openstreetmap.org/node/358914514, Mount Helen
# 4020, https://www.openstreetmap.org/node/358914547, Red Peak
# 4030, https://www.openstreetmap.org/node/358914543, Red Mountain
# 4086, https://www.openstreetmap.org/node/358914539, North Star Mountain
# 4128, https://www.openstreetmap.org/node/358914432, Bartlett Mountain
# 4144, https://www.openstreetmap.org/node/358931368, Father Dyer Peak
# 4150, https://www.openstreetmap.org/node/358914505, Tenmile Range Peak 10
# 4154, https://www.openstreetmap.org/node/358914428, Wheeler Mountain
# 4210, https://www.openstreetmap.org/node/358914674, Clinton Peak
# 4211, https://www.openstreetmap.org/node/358946509, Atlantic Peak
# 4213, https://www.openstreetmap.org/node/358914509, Crystal Peak
# 4227, https://www.openstreetmap.org/node/358914519, Pacific Peak
# 4239, https://www.openstreetmap.org/node/358914419, Fletcher Mountain
# 4348, https://www.openstreetmap.org/node/358914530, Quandary Peak
#
# these are outside of the tile, used to test that the ranking code doesn't
# consider items which are in the buffer.
#
# 4348, http://www.openstreetmap.org/node/358914747, Mount Lincoln
# 4335, http://www.openstreetmap.org/node/358914751, Mount Cameron

def count_matching(features, props):
    num_matches = 0

    for f in features:
        f_props = f['properties']
        match = True

        for k, v in props.iteritems():
            got_v = f_props.get(k)
            if got_v != v:
                match = False

        if match:
            num_matches += 1

    return num_matches


with test.features_in_tile_layer(11, 420, 779, 'pois') as features:
    def assert_peak(rank, elevation, name):
        properties = {'kind': 'peak', 'elevation': elevation, 'name': name,
                      'kind_tile_rank': rank}
        num_matching = count_matching(features, properties)
        if num_matching != 1:
            test.fail('Did not find peak matching properties %r.' % properties)

    assert_peak(1, 4348, 'Quandary Peak')
    assert_peak(2, 4239, 'Fletcher Mountain')
    assert_peak(3, 4227, 'Pacific Peak')
    assert_peak(4, 4213, 'Crystal Peak')
    assert_peak(5, 4211, 'Atlantic Peak')

    num_matching = count_matching(features, {'kind': 'peak'})
    if num_matching > 5:
        test.fail('Found %d peaks, but should only have five.' % num_matching)

# this tile has 7 peaks in it, and at z16 we should keep all of them
#https://www.openstreetmap.org/node/767614798
#https://www.openstreetmap.org/node/767614799
#https://www.openstreetmap.org/node/767614800
#https://www.openstreetmap.org/node/767614801
#https://www.openstreetmap.org/node/774446221
#https://www.openstreetmap.org/node/774446223
#https://www.openstreetmap.org/node/774446224
with test.features_in_tile_layer(16, 12372, 26269, 'pois') as features:
    num = count_matching(features, {'kind': 'peak'})
    if num != 7:
        test.fail('Found %d peaks, but expected seven.' % num)

# check that volcanos are sorted along with other kinds of peak
#https://www.openstreetmap.org/node/1744903493
#https://www.openstreetmap.org/node/356546139
#https://www.openstreetmap.org/node/348179123
with test.features_in_tile_layer(12, 662, 1443, 'pois') as features:
    def assert_peak(rank_spec, elevation, kind, name):
        if isinstance(rank_spec, int):
            possible_ranks = [rank_spec]
        else:
            possible_ranks = rank_spec
        matched_one = False
        for rank in possible_ranks:
            properties = {'kind': kind, 'elevation': elevation, 'name': name,
                          'kind_tile_rank': rank}
            num_matching = count_matching(features, properties)
            if num_matching == 1:
                matched_one = True
                break
        if not matched_one:
            test.fail('Did not find %s matching properties %r.' %
                 (kind, properties))

    assert_peak(1,      4392, 'volcano', 'Mount Rainier')
    assert_peak(2,      4302, 'peak',    'Point Success')
    assert_peak((3, 4), 3863, 'peak',    'Gibraltar Rock')
