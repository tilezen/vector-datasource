tiles = [
    # there are TWO Target stores in this tile - and both are huge!
    #https://www.openstreetmap.org/way/56149856
    #https://www.openstreetmap.org/way/152722810
    ['14/2618/6338', set([152722810, 56149856]), 'department_store'],
    #https://www.openstreetmap.org/way/219072560
    ['14/2620/6333', 219072560, 'supermarket'],
    #https://www.openstreetmap.org/way/344057345
    ['14/2618/6338', 344057345, 'supermarket'],
    #https://www.openstreetmap.org/way/259001359
    ['14/2621/6334', 259001359, 'doityourself'],
    #https://www.openstreetmap.org/way/194906343
    ['15/5240/12668', 194906343, 'supermarket'],
    #https://www.openstreetmap.org/relation/3585039
    ['15/5236/12666', -3585039, 'supermarket'],
]

for zxy, id, kind in tiles:
    z, x, y = map(int, zxy.split('/'))
    test.assert_has_feature(z, x, y, 'pois', {'kind': kind, 'id': id})
