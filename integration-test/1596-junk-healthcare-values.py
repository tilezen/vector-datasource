# -*- encoding: utf-8 -*-
from . import FixtureTest


class HealthcareTest(FixtureTest):

    def test_blood_donation(self):
        import dsl

        z, x, y = (16, 11205, 26166)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/227712531
            dsl.way(227712531, dsl.tile_box(z, x, y), {
                'addr:city': u'Los Angeles',
                'addr:housenumber': u'1045',
                'addr:postcode': u'90024',
                'addr:state': u'CA',
                'addr:street': u'Gayley Avenue',
                'blood:plasma': u'yes',
                'blood:platelets': u'yes',
                'blood:whole': u'yes',
                'building': u'yes',
                'ele': u'105.8',
                'elevator': u'yes',
                'healthcare': u'blood_donation',
                'height': u'7.9',
                'lacounty:ain': u'4363025008',
                'lacounty:bld_id': u'426122844901',
                'level': u'1',
                'name': u'UCLA Blood & Platelet Center',
                'office': u'yes',
                'opening_hours': u'Mo-Fr 08:00-17:00',
                'operator': u'UCLA Health',
                'phone': u'(310) 825-0888',
                'source': u'openstreetmap.org',
                'start_date': u'1950',
                'website': u'http://gotblood.ucla.edu/westwood-center',
            }),
        )

        # NOTE: blood_donation is mapped to blood_bank.
        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 227712531,
                'kind': u'blood_bank',
            })

    def test_hospice(self):
        import dsl

        z, x, y = (16, 10427, 25175)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/544655321
            dsl.way(544655321, dsl.tile_box(z, x, y), {
                'building': u'yes',
                'healthcare': u'hospice',
                'name': u'Memorial Hospice',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 544655321,
                'kind': u'hospice',
            })

    def test_optometrist(self):
        import dsl

        z, x, y = (16, 10494, 24676)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/566181198
            dsl.way(566181198, dsl.tile_box(z, x, y), {
                'building': u'yes',
                'healthcare': u'optometrist',
                'name': u'Shasta Eye Medical Group',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 566181198,
                'kind': u'optometrist',
            })

    def test_physiotherapist(self):
        import dsl

        z, x, y = (16, 11428, 26418)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/31815993
            dsl.way(31815993, dsl.tile_box(z, x, y), {
                'addr:city': u'San Diego',
                'addr:country': u'US',
                'addr:housenumber': u'10803',
                'addr:state': u'CA',
                'building': u'yes',
                'building_type': u'industrial',
                'healthcare': u'physiotherapist',
                'name': u'Function Smart Physical Therapy',
                'sangis:OBJECTID': u'9872',
                'sangis:TYPE': u'Industrial',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 31815993,
                'kind': u'physiotherapist',
            })

    def test_psychotherapist(self):
        import dsl

        z, x, y = (16, 11730, 26442)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/602686729
            dsl.way(602686729, dsl.tile_box(z, x, y), {
                'addr:city': u'El Centro',
                'addr:postcode': u'92243',
                'addr:state': u'CA',
                'building': u'yes',
                'healthcare': u'psychotherapist',
                'name': u'Behavior Health',
                'source': u'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 602686729,
                'kind': u'psychotherapist',
            })

    def test_rehabilitation(self):
        import dsl

        z, x, y = (16, 10577, 25429)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/351588744
            dsl.way(351588744, dsl.box_area(z, x, y, 1593), {
                'addr:housenumber': '480',
                'addr:street': 'North 1st Street',
                'amenity': 'healthcare',
                'building': 'yes',
                'building:levels': '2',
                'healthcare': 'rehabilitation',
                'healthcare:speciality': 'brain_injury',
                'name': 'Services for Brain Injury',
                'source': 'openstreetmap.org',
                'website': 'http://legalaidsociety.org/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 351588744,
                'kind': 'rehabilitation',
            })

    def test_blood_bank(self):
        import dsl

        z, x, y = (16, 13332, 26538)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/123526145
            dsl.way(123526145, dsl.box_area(z, x, y, 601), {
                'addr:housenumber': '1200',
                'addr:postcode': '88011',
                'addr:street': 'Commerce Drive',
                'building': 'yes',
                'healthcare': 'blood_bank',
                'name': 'United Blood Services',
                'phone': '+1-575-527-1322',
                'source': 'openstreetmap.org',
                'website': 'http://unitedbloodservices.org/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 123526145,
                'kind': 'blood_bank',
            })

    def test_chiropractor(self):
        import dsl

        z, x, y = (16, 13686, 25100)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/429672737
            dsl.point(429672737, (-104.815915, 38.767464), {
                'healthcare': 'chiropractor',
                'name': 'Cheyenne Mountain Chiropractic',
                'shop': 'chiropractor',
                'source': 'openstreetmap.org',
                'url': 'http://www.cheyennemountainchiro.com/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 429672737,
                'kind': 'chiropractor',
            })

    def test_midwife(self):
        import dsl

        z, x, y = (16, 10572, 25430)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4976744222
            dsl.point(4976744222, (-121.921157, 37.342539), {
                'healthcare': 'midwife',
                'name': 'South Bay Homebirth Collective',
                'source': 'openstreetmap.org',
                'website': 'https://www.southbayhomebirthcollective.com/',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4976744222,
                'kind': 'midwife',
            })

    def test_occupational_therapist(self):
        import dsl

        z, x, y = (16, 13009, 25019)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/5990502872
            dsl.point(5990502872, (-108.534998, 39.113415), {
                'addr:housenumber': '751',
                'addr:street': 'Horizon Court',
                'addr:unit': '247',
                'healthcare': 'occupational_therapist',
                'name': 'OSA Transpersonal Counseling',
                'office': 'company',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 5990502872,
                'kind': 'occupational_therapist',
            })

    def test_paediatrics(self):
        import dsl

        z, x, y = (16, 12098, 25485)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4551720597
            dsl.point(4551720597, (-113.538890, 37.100048), {
                'healthcare': 'paediatrics',
                'name': 'Brain Blance Acheivement Centers',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4551720597,
                'kind': 'paediatrics',
            })

    def test_podiatrist(self):
        import dsl

        z, x, y = (16, 12431, 26269)

        self.generate_fixtures(
            # https://www.openstreetmap.org/way/563753551
            dsl.way(563753551, dsl.box_area(z, x, y, 564), {
                'addr:city': 'Fountain Hills',
                'addr:housenumber': '11046',
                'addr:postcode': '85268',
                'addr:state': 'AZ',
                'addr:street': 'North Saguaro Boulevard',
                'addr:unit': '2',
                'building': 'commercial',
                'healthcare': 'podiatrist',
                'name': 'Advanced Podiatry',
                'phone': '(480) 837-2240',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 563753551,
                'kind': 'podiatrist',
            })

    def test_speech_therapist(self):
        import dsl

        z, x, y = (16, 10472, 25341)

        self.generate_fixtures(
            # https://www.openstreetmap.org/node/4238377192
            dsl.point(4238377192, (-122.472601, 37.731538), {
                'addr:city': 'San Francisco',
                'addr:housenumber': '2528',
                'addr:postcode': '94127',
                'addr:state': 'CA',
                'addr:street': 'Ocean Avenue',
                'healthcare': 'speech_therapist',
                'name': 'Spencer and Kong',
                'source': 'openstreetmap.org',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'pois', {
                'id': 4238377192,
                'kind': 'speech_therapist',
            })
