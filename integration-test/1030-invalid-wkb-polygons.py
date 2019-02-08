from . import FixtureTest
from mapbox_vector_tile.decoder import POLYGON


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


class InvalidWkbPolygons(FixtureTest):

    def test_caspian_sea_exists(self):
        # Caspian Sea
        self.load_fixtures([
            'file://integration-test/fixtures/ne_10m_ocean/'
            '1030-invalid-wkb-polygon-v2.shp',
        ], clip=self.tile_bbox(5, 20, 12))

        self.assert_has_feature(
            5, 20, 12, 'water',
            {'kind': 'ocean'})

    def test_baltic_sea_exists(self):
        # Baltic Sea - JSON format
        self.load_fixtures([
            'file://integration-test/fixtures/ne_10m_ocean/'
            '1030-invalid-wkb-polygon-v2.shp',
        ], clip=self.tile_bbox(5, 17, 9))

        self.assert_has_feature(
            5, 17, 9, 'water',
            {'kind': 'ocean'})

    def test_mvt_feature_validity(self):
        # Check MVT format
        # NOTE: this is _not_ clipped or simplified, as the full area of the
        # ocean is necessary to check that the simplification later on in the
        # stack when encoding the MVT hasn't broken the polygon.
        self.load_fixtures([
            'file://integration-test/fixtures/ne_10m_ocean/'
            '1030-invalid-wkb-polygon-v2.shp',
        ])

        with self.features_in_mvt_layer(5, 17, 9, 'water') as features:
            ocean_area = 0

            for feature in features:
                if feature['type'] != POLYGON:
                    continue

                props = feature['properties']
                if props.get('kind') == 'ocean':
                    geom = feature['geometry']
                    geom_type = geom['type']
                    self.assertTrue('Polygon' in geom_type)
                    ocean_area += area_of(geom['coordinates'])

            ocean_area = abs(ocean_area)
            expected = 7326600
            self.assertFalse(
                ocean_area < expected,
                'Ocean area %f, expected at least %f.' %
                (ocean_area, expected))
            self.assertFalse(
                ocean_area > 1.5 * expected,
                'Ocean area %f > 1.5 * expected %f' %
                (ocean_area, expected))
