from mapbox_vector_tile.decoder import POLYGON

# Caspian Sea
test.assert_has_feature(
    5, 20, 12, 'water',
    { 'kind': 'ocean' })

# Baltic Sea - JSON format
test.assert_has_feature(
    5, 17, 9, 'water',
    { 'kind': 'ocean' })


def area_of_ring(ring):
    area = 0

    for [px, py], [nx, ny] in zip(ring, ring[1:] + [ring[0]]):
        area += px * ny - nx * py

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
with test.features_in_mvt_layer(5, 17, 9, 'water') as features:
    ocean_area = 0

    for feature in features:
        if feature['type'] != POLYGON:
            continue

        props = feature['properties']
        if props.get('kind') == 'ocean':
            geom = feature['geometry']
            geom_type = geom['type']
            test.assertTrue('Polygon' in geom_type)
            ocean_area += area_of(geom['coordinates'])

    ocean_area = abs(ocean_area)
    expected = 7326600
    if ocean_area < expected:
        test.fail('Ocean area %f, expected at least %f.' % (ocean_area, expected))
    if ocean_area > 1.5 * expected:
        test.fail('Ocean area %f > 1.5 * expected %f' % (ocean_area, expected))
