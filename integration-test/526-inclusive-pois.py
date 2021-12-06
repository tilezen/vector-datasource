from . import FixtureTest


class InclusivePois(FixtureTest):

    def test_healthcare_midwife(self):
        import dsl
        z, x, y = 16, 10500, 22491
        self.generate_fixtures(
            dsl.point(3761053357, dsl.tile_centre(z, x, y), {
                'addr:unit': '304',
                'healthcare': 'midwife',
                'level': '3',
                'name': 'Cheam midwifery',
                'phone': '+1 604-744-8873',
                'website': 'http://www.cheam-midwifery.com'}))

        self.assert_has_feature(
            z, x, y, 'pois', {'kind': 'midwife'})

    def test_childcare_amenities(self):
        self._run_test(
            'https://www.openstreetmap.org/node/4105506789',
            '16/19302/24658', {'kind': 'kindergarten'})

        self._run_test(
            'https://www.openstreetmap.org/way/378041773',
            '16/10478/25338', {'kind': 'childcare'})

    def test_emergency_phone(self):
        self._run_test(
            'https://www.openstreetmap.org/node/2456072777',
            '16/10494/25321', {'kind': 'phone'})

    def test_toilets(self):
        self._run_test(
            'https://www.openstreetmap.org/node/3931486668',
            '16/10480/25330', {'kind': 'toilets'})

    def test_social_facilities(self):
        # amenity=social_facility + social_facility=*
        # also with social_facility:for -> for and turned into a list to make
        # it easier to consume.
        self._run_test(
            'https://www.openstreetmap.org/node/3505221950',
            '16/20331/22950', {'kind': 'social_facility', 'for': ['diseased']})
        self._run_test(
            'https://www.openstreetmap.org/way/121024970',
            '16/10480/25332', {'kind': 'group_home',
                               'for': ['senior', 'disabled']})
        self._run_test(
            'https://www.openstreetmap.org/node/3009189224',
            '16/10482/25332', {'kind': 'shelter', 'for': ['homeless']})
        self._run_test(
            'https://www.openstreetmap.org/way/243357053',
            '16/10483/25330', {'kind': 'shelter', 'for': ['homeless']})
        self._run_test(
            'https://www.openstreetmap.org/way/377082896',
            '16/10480/25404', {'kind': 'group_home', 'for': ['senior']})
        self._run_test(
            'https://www.openstreetmap.org/node/8633946670',
            '16/10542/25423', {'kind': 'assisted_living'})

    def test_medical_amenities(self):
        # amenity={clinic, doctors, dentist}
        # also with healthcare:speciality -> speciality and turned into a list
        # to make it easier to consume.
        self._run_test(
            'https://www.openstreetmap.org/node/417237471',
            '16/10484/25325', {'kind': 'clinic'})
        self._run_test(
            'https://www.openstreetmap.org/way/261102266',
            '16/10482/25333', {'kind': 'clinic'})
        self._run_test(
            'https://www.openstreetmap.org/node/3133693825',
            '16/10480/25337', {'kind': 'doctors'})
        self._run_test(
            'https://www.openstreetmap.org/node/3163318863',
            '16/10480/25337', {'kind': 'dentist'})
        self._run_test(
            'https://www.openstreetmap.org/node/3366375212',
            '16/33281/22391', {'kind': 'doctors', 'speciality': ['general']})

    def _run_test(self, url, zxy, props):
        z, x, y = map(int, zxy.split('/'))
        self.load_fixtures([url])
        self.assert_has_feature(
            z, x, y, 'pois', props)
