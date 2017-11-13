from . import FixtureTest


class RoutesViaStopPositions(FixtureTest):

    def _load(self, z, x, y, nodes=[], ways=[], relations=[]):
        fixtures = []
        for n in nodes:
            fixtures.append('https://www.openstreetmap.org/node/%d' % n)
        for w in ways:
            fixtures.append('https://www.openstreetmap.org/way/%d' % w)
        for r in relations:
            fixtures.append('https://www.openstreetmap.org/relation/%d' % r)
        self.load_fixtures(fixtures, clip=self.tile_bbox(z, x, y))

    def _check(self, z, x, y, name, osm_id, expected_rank, expected_routes):
        with self.features_in_tile_layer(z, x, y, 'pois') as pois:
            found = False

            for poi in pois:
                props = poi['properties']
                if props['id'] == osm_id:
                    found = True
                    routes = list()
                    for typ in ['train', 'subway', 'light_rail', 'tram']:
                        routes.extend(props.get('%s_routes' % typ, list()))
                    rank = props['kind_tile_rank']

                    self.assertFalse(
                        rank > expected_rank,
                        'Found %r, and was expecting a rank of %r or less, '
                        'but got %r.' % (name, expected_rank, rank))

                    for r in expected_routes:
                        count = 0
                        for route in routes:
                            if r in route:
                                count = count + 1

                        self.assertFalse(
                            count == 0,
                            'Found %r, and was expecting at least one %r '
                            'route, but found none. Routes: %r' %
                            (name, r, routes))

            self.assertTrue(
                found,
                'Did not find %r (ID=%r) in tile.' % (name, osm_id))

    def test_nyc_penn_station(self):
        # Stations and lines, etc... used in exploring the NYC Penn Station
        # object network.
        self._load(
            13, 2412, 3078,
            nodes=[895371274],
            relations=[1359387, 1377996, 1377998, 1377999, 1380577, 1590286,
                       1809808, 1834644, 1897938, 1900976, 207401, 2648181,
                       2807121, 4044002, 4073816, 4234377, 4234911, 4445771,
                       4452779, 4460896, 4467189, 4467190, 4748609, 4799100,
                       4799101])

        self._check(
            13, 2412, 3078, 'Penn Station', 895371274, 1, [
                '2100-2297',  # Acela Express
                '68-69',  # Adirondack
                '50-51',  # Cardinal
                '79-80',  # Carolinian
                '19-20',  # Crescent
                '230-296',  # Empire Service
                '600-674',  # Keystone Service
                '63',  # Maple Leaf (Northbound)
                '64',  # Maple Leaf (Southbound)
                '89-90',  # Palmetto
                '42-43',  # Pennsylvanian
                '97-98',  # Silver Meteor
                '91-92',  # Silver Star
                '54-57',  # Vermonter
            ])

    def test_camden_station(self):
        self._load(
            13, 2352, 3122,
            nodes=[1129957203, 1129957312, 845910705],
            relations=[1401995, 1402004, 1403277, 1403278])
        self._check(
            13, 2352, 3122, 'Camden Station', 845910705, 5, [
                'Camden Line',
            ])

    def test_castro_muni(self):
        self._load(
            13, 1309, 3166,
            nodes=[297863017],
            ways=[256270166],
            relations=[2124174, 3433312, 3433314, 3433316, 3435875, 63250,
                       63572, 91022])
        self._check(
            13, 1309, 3166, 'Castro MUNI', 297863017, 1, [
                'K', 'L', 'M', 'T'])

    def test_30th_street_station(self):
        self._load(
            13, 2385, 3102,
            nodes=[2058688536, 2058688538, 3426208027, 3426249715,
                   3426249720, 3426249721],
            ways=[30953448, 32272623, 43352433, 60185604, 60185611],
            relations=[1269021, 1359387, 1388639, 1388641, 1388648,
                       1390116, 1390117, 1390133, 1402781, 1405499,
                       1590286, 1809808, 1897938, 1900976, 206515,
                       2629937, 2629938, 2648181, 2807121, 4044002,
                       4460896, 4744254, 4748609, 4799100, 4799101])
        self._check(
            13, 2385, 3102, '30th Street', 32272623, 1, [
                '2100-2297',  # Acela Express
                '79-80',  # Carolinian
                '19-20',  # Crescent
                '600-674',  # Keystone Service
                # Northeast Regional (Boston/Springfield & Lynchburg)
                '82-198',
                '89-90',  # Palmetto
                'Chestnut Hill West Line',  # SEPTA - Chestnut Hill West Line
                'Cynwyd Line',  # SEPTA - Cynwyd Line
                'Media/Elwyn Line',  # SEPTA - Media/Elwyn Line
                'Trenton Line',  # SEPTA - Trenton Line
                'Wilmington/Newark Line',  # SEPTA - Wilmington/Newark Line
                '91-92',  # Silver Star
            ])
