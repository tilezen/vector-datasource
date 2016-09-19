# Caspian Sea
assert_has_feature(
    5, 20, 12, 'water',
    { 'kind': 'ocean' })

# Baltic Sea - JSON format
assert_has_feature(
    5, 17, 9, 'water',
    { 'kind': 'ocean' })


def area_of_ring(ring):
    area = 0

    try:
        for [px, py], [nx, ny] in zip(ring, ring[1:] + [ring[0]]):
            area += px * ny - nx * py
    except TypeError:
        pass

    return 0.5 * area


def area_of(polygons):
    area = 0

    for polygon in polygons:
        outer = polygon[0]
        inners = polygon[1:]

        area += area_of_ring(outer)
        for inner in inners:
            area -= area_of_ring(inner)

    return area


# Check MVT format
with features_in_mvt_layer(5, 17, 9, 'water') as features:
    ocean_area = 0

    for feature in features:
        props = feature['properties']
        if props.get('kind') == 'ocean':
            ocean_area += area_of(feature['geometry'])

    expected = 7936264
    if abs(abs(ocean_area) - expected) / expected > 0.05:
        raise Exception("Ocean area %f, expected %f." % (abs(ocean_area), expected))
