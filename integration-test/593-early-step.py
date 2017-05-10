tiles = [
    # highway=steps, with route regional (Coastal Trail, Marin, II)
    # https://www.openstreetmap.org/way/24655593
    # https://www.openstreetmap.org/relation/2260059
    [12,  653, 1582],
    # highway=steps, no route, but has name, and designation (Levant St Stairway, SF)
    # https://www.openstreetmap.org/way/38060491
    [13, 1309, 3166]
]

for z, x, y in tiles:
    test.assert_has_feature(
        z, x, y, 'roads',
        {'kind_detail': 'steps'})


# way 25292070   highway=steps, no route, but has name (Esmeralda, Bernal, SF)
test.assert_no_matching_feature(
    13, 1310, 3167, 'roads',
    {'kind': 'path', 'kind_detail': 'steps', 'name': 'Esmeralda Ave.'})

# way 25292070   highway=steps, no route, but has name (Esmeralda, Bernal, SF)
test.assert_has_feature(
    14, 2620, 6334, 'roads',
    {'kind': 'path', 'kind_detail': 'steps', 'name': 'Esmeralda Ave.'})
