from . import FixtureTest


class WaterBoundariesSlow(FixtureTest):

    def test_boundaries(self):
        from shapely.geometry import Polygon, MultiPolygon
        import dsl

        # River Tocanis, Brasil

        # these are tiles which have water boundaries, but only
        # water-to-water boundaries. since we remove these, then we should
        # have more than one water polygon, but zero water boundaries
        # actually in the tile.
        no_boundary_tiles = [
            [16, 23768, 33616],
        ]

        # these are tiles which do have a boundary, to check that the first
        # condition isn't trivially fulfilled by having no boundaries
        # whatsoever.
        boundary_tiles = [
            [16, 23775, 33616],
        ]

        self.generate_fixtures(
            dsl.way(-275011,
                    MultiPolygon([
                        Polygon([
                            (-49.39061691153051, -4.642129842005724),
                            (-49.3911190288361, -4.64364792245321),
                            (-49.3873424215501, -4.64655660425706),
                            (-49.383544921875, -4.644166012503287),
                            (-49.383544921875, -4.656281393196448),
                            (-49.3836036333376, -4.65640167692064),
                            (-49.3888874340073, -4.65459808086801),
                            (-49.3950947926206, -4.65838675537571),
                            (-49.4110107421875, -4.656996327123991),
                            (-49.4110107421875, -4.642129842005724),
                            (-49.39061691153051, -4.642129842005724),
                        ]), Polygon([
                            (-49.4219970703125, -4.65603655397672),
                            (-49.449462890625, -4.653637121108541),
                            (-49.449462890625, -4.642129842005724),
                            (-49.4219970703125, -4.642129842005724),
                            (-49.4219970703125, -4.65603655397672),
                        ]),
                    ]), {
                        "natural": "water",
                        "name": u"Reservat\u00f3rio da Usina "
                        u"Hidrel\u00e9trica de Tucuru\u00ed",
                        "short_name": u"Reservat\u00f3rio UHE de Tucuru\u00ed",
                        "way_area": "2.71214e+09",
                        "wikipedia": u"pt:Usina Hidrel\u00e9trica de "
                        u"Tucuru\u00ed",
                        "name:de": u"Tucuru\u00ed-Stausee",
                        "water": "reservoir",
                        "source": "openstreetmap.org",
                        "wikidata": "Q1475210",
                    }),
            dsl.way(-1363854,
                    MultiPolygon([
                        Polygon([
                            (-49.449462890625, -4.653637121108541),
                            (-49.4219970703125, -4.65603655397672),
                            (-49.4219970703125, -4.669505032676526),
                            (-49.449462890625, -4.669505032676526),
                            (-49.449462890625, -4.653637121108541),
                        ]), Polygon([
                            (-49.4110107421875, -4.656996327123991),
                            (-49.3950947926206, -4.65838675537571),
                            (-49.38621008393813, -4.669505032676526),
                            (-49.404887252266015, -4.669505032676526),
                            (-49.4072058792811, -4.66783843107854),
                            (-49.40703528549232, -4.669505032676526),
                            (-49.4110107421875, -4.669505032676526),
                            (-49.4110107421875, -4.656996327123991),
                        ])
                    ]), {
                        "source": "openstreetmap.org",
                        "waterway": "riverbank",
                        "way_area": 7.12568e+08,
                    })
        )

        for z, x, y in no_boundary_tiles:
            with self.features_in_tile_layer(z, x, y, 'water') as features:
                num_polygons = 0
                num_boundaries = 0

                for f in features:
                    geom_type = f['geometry']['type']
                    boundary = f['properties'].get('boundary', False)

                    if geom_type in ['Polygon', 'MultiPolygon']:
                        num_polygons += 1

                    elif boundary is True:
                        num_boundaries += 1

                self.assertFalse(
                    num_polygons < 2,
                    'Expected at least 2 polygons in water boundary test '
                    'tile, but found only %d' % num_polygons)

                self.assertFalse(
                    num_boundaries > 0,
                    'Expected an all-water tile with no land boundaries, '
                    'but found %d boundaries.' % num_boundaries)

        for z, x, y in boundary_tiles:
            self.assert_has_feature(
                z, x, y, 'water',
                {'boundary': True})
