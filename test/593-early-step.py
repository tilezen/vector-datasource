tiles = [
    [12,  653, 1582],   # way 24655593   highway=steps, with route regional (Coastal Trail, Marin, II)
    [13, 1309, 3166]    # way 38060491   highway=steps, no route, but has name, and designation (Levant St Stairway, SF)
]

for z, x, y in tiles:
    assert_has_feature(
        z, x, y, 'roads',
        {'highway': 'steps'})


# way 25292070   highway=steps, no route, but has name (Esmeralda, Bernal, SF)
assert_no_matching_feature(
    13, 1310, 3167, 'roads',
    {'kind': 'path', 'highway': 'steps', 'name': 'Esmeralda Ave.'})

# way 25292070   highway=steps, no route, but has name (Esmeralda, Bernal, SF)
assert_has_feature(
    14, 2620, 6334, 'roads',
    {'kind': 'path', 'highway': 'steps', 'name': 'Esmeralda Ave.'})
