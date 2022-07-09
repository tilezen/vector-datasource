from . import FixtureTest


class DropPhysicalRailwaysFromTransit(FixtureTest):

    def test_drop_physical_railways(self):
        import urllib

        bbox = '39,-124,41,-121'
        query = '('
        for route in ('train', 'subway', 'light_rail', 'tram'):
            query += 'relation[type=route][route=' + route + '](' + bbox + ');'
        query += ');>;'
        query = urllib.urlencode(dict(data=query))

        self.load_fixtures(
            ['http://overpass-api.de/api/interpreter?' + query])

        self.assert_no_matching_feature(
            7, 20, 48, 'transit',
            {'kind': 'railway'})

        # count the unique parameters - there should only be one, indicating
        # that the rail routes have been merged.
        with self.features_in_tile_layer(7, 20, 48, 'transit') as transit:
            seen_properties = set()
            railway_kinds = set(['train', 'subway', 'light_rail', 'tram'])

            for feature in transit:
                if feature['properties'].get('kind') in railway_kinds:
                    props = frozenset(feature['properties'].items())
                    self.assertFalse(
                        props in seen_properties,
                        'Duplicate properties %r in transit layer, but '
                        'properties should be unique.'
                        % feature['properties'])
                    seen_properties.add(props)
