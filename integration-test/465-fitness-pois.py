from . import FixtureTest


class FitnessPois(FixtureTest):
    def test_leisure_fitness_centre(self):
        # Fitness SF SOMA, leisure=fitness_centre
        self._run_test(16, 10484, 25332, 'way/25371830')

    def test_leisure_sports_centre_plus_fitness(self):
        # Sunset gym, leisure=sports_centre + sport=fitness
        self._run_test(16, 10473, 25333, 'node/3674255652')

    def test_amenity_gym(self):
        import dsl
        # Alameda Athletic Club, amenity=gym
        z, x, y = (16, 10514, 25334)

        self.generate_fixtures(dsl.point(310972983, dsl.tile_centre(z, x, y),
                                         {'leisure': 'fitness_centre',
                                          'name': 'Alameda Athletic Club'}))
        self.assert_has_feature(
            z, x, y, 'pois',
            {'kind': 'fitness'})

    def test_pushup_fitness_station(self):
        # Pushup, fitness_station
        self.load_fixtures(['https://www.openstreetmap.org/node/3658323774'])

        self.assert_has_feature(
            16, 13166, 25271, 'pois',
            {'kind': 'fitness_station'})

    def _run_test(self, z, x, y, typ_id):
        self.load_fixtures(['https://www.openstreetmap.org/' + typ_id])

        self.assert_has_feature(
            z, x, y, 'pois',
            {'kind': 'fitness'})
