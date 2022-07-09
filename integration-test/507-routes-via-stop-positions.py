from shapely.wkt import loads as wkt_loads

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
        import dsl
        self.generate_fixtures(
            dsl.point(895371274, (-73.9928236, 40.7502331), {
                'source': 'openstreetmap.org',
                'wikipedia': 'en:Pennsylvania Station (New York City)',
                'wheelchair': 'yes',
                'network': 'New York City Subway',
                'operator': 'Amtrak',
                'toilets:wheelchair': 'yes',
                'railway': 'station',
                'alt_name': 'Pennsylvania Station',
                'name': 'New York Penn Station',
                'ref:Amtrak': 'NYP',
                'addr:city': 'New York',
                'addr:housenumber': '234',
                'addr:postcode': '10001',
                'addr:state': 'NY',
                'addr:street': 'West 31st Street',
                'iata': 'ZYP'
            }),
            dsl.relation(206515, {
                'website': 'http://www.njtransit.com/',
                'network': 'NJTR',
                'type': 'route',
                'route': 'train',
                'name': 'NJT - Atlantic City Line',
                'ref': 'Atlantic City',
                'wikidata': 'Q756350',
                'wikipedia': 'en:Atlantic City Line',
                'colour': '#015DAB',
                'operator': 'New Jersey Transit',
                'passenger': 'suburban'
            }, nodes=[895371274]),
            dsl.relation(207401, {
                'website': 'http://www.njtransit.com/',
                'network': 'NJTR',
                'type': 'route',
                'usage': 'main',
                'route': 'train',
                'name': 'NJT - North Jersey Coast Line',
                'ref': 'North Jersey Coast',
                'wikidata': 'Q7055732',
                'wikipedia': 'en:North Jersey Coast Line',
                'passenger': 'suburban',
                'operator': 'New Jersey Transit',
                'colour': '#00A5E3'
            }, nodes=[895371274]),
            dsl.relation(1359387, {
                'service': 'long_distance',
                'colour': '#005480',
                'passenger': 'national',
                'website': 'http://www.amtrak.com',
                'name': 'Vermonter',
                'ref': '54-57',
                'from': 'Washington, DC',
                'public_transport:version': '1',
                'to': 'Saint Albans, Vermont',
                'via': 'New York Penn Station',
                'wikipedia': 'en:Vermonter (train)',
                'wikidata': 'Q1412872',
                'network': 'Amtrak',
                'operator': 'Amtrak',
                'route': 'train',
                'type': 'route'
            }, nodes=[895371274]),
            dsl.relation(1377996, {
                'website': 'http://www.njtransit.com/',
                'network': 'NJTR',
                'wikipedia': 'en:Gladstone Branch',
                'wikidata': 'Q5566325',
                'name': 'NJT - Gladstone Line',
                'type': 'route',
                'route': 'train',
                'ref': 'Gladstone',
                'operator': 'New Jersey Transit',
                'passenger': 'suburban',
                'colour': '#A1D4AE'
            }, nodes=[895371274]),
            dsl.relation(1377998, {
                'wikipedia': 'en:Morristown Line',
                'website': 'http://www.njtransit.com/',
                'network': 'NJTR',
                'wikidata': 'Q1948559',
                'name': 'NJT - Morristown Line',
                'type': 'route',
                'route': 'train',
                'ref': 'Morristown',
                'operator': 'New Jersey Transit',
                'passenger': 'suburban',
                'colour': '#00A94E'
            }, nodes=[895371274]),
            dsl.relation(1377999, {
                'type': 'route',
                'website': 'http://www.njtransit.com/',
                'network': 'NJTR',
                'route': 'train',
                'name': 'NJT - Montclair-Boonton Line',
                'ref': 'Montclair-Boonton',
                'wikidata': 'Q6904583',
                'wikipedia': 'en:Montclair-Boonton Line',
                'passenger': 'suburban',
                'operator': 'New Jersey Transit',
                'colour': '#E76B5B'
            }, nodes=[895371274]),
            dsl.relation(1380577, {
                'website': 'http://www.njtransit.com/',
                'network': 'NJTR',
                'colour': '#EE3A41',
                'name': 'NJT - Northeast Corridor Line',
                'operator': 'New Jersey Transit',
                'passenger': 'suburban',
                'ref': 'NEC (NJT)',
                'route': 'train',
                'type': 'route',
                'wikidata': 'Q7057868',
                'wikipedia': 'en:Northeast Corridor Line'
            }, nodes=[895371274]),
            dsl.relation(1590286, {
                'service': 'long_distance',
                'colour': '#005480',
                'wikipedia': 'en:Silver Meteor',
                'from': 'New York, NY',
                'to': 'Miami, FL',
                'network': 'Amtrak Intercity',
                'name': 'Silver Meteor',
                'ref': '97-98',
                'public_transport:version': '1',
                'wikidata': 'Q389948',
                'type': 'route',
                'operator': 'Amtrak',
                'passenger': 'national',
                'route': 'train'
            }, nodes=[895371274]),
            dsl.relation(1809808, {
                'service': 'long_distance',
                'colour': '#005480',
                'from': 'New York, NY',
                'to': 'New Orleans, LA',
                'wikipedia': 'en:Crescent (train)',
                'network': 'Amtrak Intercity',
                'name': 'Crescent',
                'ref': '19-20',
                'public_transport:version': '1',
                'wikidata': 'Q756508',
                'type': 'route',
                'operator': 'Amtrak',
                'passenger': 'national',
                'route': 'train'
            }, nodes=[895371274]),
            dsl.relation(1834644, {
                'type': 'route',
                'colour': '#C60C30',
                'description': 'train schedule',
                'name': 'LIRR - Port Washington Branch',
                'network': 'LIRR',
                'operator': 'LIRR',
                'passenger': 'suburban',
                'ref': 'Port Washington',
                'route': 'train'
            }, nodes=[895371274]),
            dsl.relation(1897938, {
                'service': 'long_distance',
                'colour': '#005480',
                'wikipedia': 'en:Silver Star (Amtrak train)',
                'from': 'New York, NY',
                'network': 'Amtrak Intercity',
                'wikidata': 'Q665435',
                'website': 'http://www.amtrak.com/',
                'type': 'route',
                'name': 'Silver Star',
                'ref': '91-92',
                'public_transport:version': '1',
                'to': 'Miami, FL',
                'route': 'train',
                'passenger': 'national',
                'operator': 'Amtrak'
            }, nodes=[895371274]),
            dsl.relation(1900976, {
                'service': 'long_distance',
                'colour': '#005480',
                'to': 'Charlotte, NC',
                'wikipedia': 'en:Carolinian (train)',
                'website': 'http://www.amtrak.com/',
                'network': 'Amtrak Intercity',
                'name': 'Carolinian',
                'ref': '79-80',
                'public_transport:version': '1',
                'wikidata': 'Q283663',
                'type': 'route',
                'from': 'New York Penn Station',
                'operator': 'Amtrak',
                'passenger': 'national',
                'route': 'train'
            }, nodes=[895371274]),
            dsl.relation(2648181, {
                'service': 'long_distance',
                'colour': '#005480',
                'network': 'Amtrak Intercity',
                'from': 'New York Penn Station',
                'website': 'http://www.amtrak.com/',
                'name': 'Palmetto',
                'ref': '89-90',
                'wikipedia': 'en:Palmetto (train)',
                'public_transport:version': '1',
                'to': 'Savannah, GA',
                'wikidata': 'Q944742',
                'type': 'route',
                'operator': 'Amtrak',
                'passenger': 'national',
                'route': 'train'
            }, nodes=[895371274]),
            dsl.relation(2807121, {
                'FIXME': "Numerous \"track splits\" (likely missing crossovers); Chicago between Harvey and Union Station",
                'service': 'long_distance',
                'colour': '#005480',
                'wikipedia': 'en:Cardinal (train)',
                'network': 'Amtrak Intercity',
                'wikidata': 'Q858400',
                'name': 'Cardinal',
                'ref': '50-51',
                'public_transport:version': '1',
                'type': 'route',
                'to': 'New York Penn Station',
                'from': 'Chicago Union Station',
                'operator': 'Amtrak',
                'passenger': 'national',
                'route': 'train'
            }, nodes=[895371274]),
            dsl.relation(4044002, {
                'passenger': 'national',
                'service': 'regional',
                'colour': '#005480',
                'wikipedia': 'en:Pennsylvanian (train)',
                'website': 'http://www.amtrak.com/',
                'name': 'Pennsylvanian',
                'ref': '42-43',
                'from': 'New York Penn Station',
                'to': 'Pittsburgh',
                'public_transport:version': '1',
                'wikidata': 'Q654593',
                'type': 'route',
                'network': 'Amtrak',
                'operator': 'Amtrak',
                'route': 'train'
            }, nodes=[895371274]),
            dsl.relation(4073816, {
                'service': 'international',
                'colour': 'indigo',
                'to': 'Montreal Central Station',
                'wikipedia': 'en:Adirondack (train)',
                'FIXME': 'Stations are ordered improperly',
                'wikidata': 'Q504115',
                'website': 'http://www.amtrak.com',
                'name': 'Adirondack',
                'ref': '68-69',
                'direction': 'north',
                'public_transport:version': '1',
                'type': 'route',
                'route': 'train',
                'from': 'New York Penn Station',
                'operator': 'Amtrak',
                'passenger': 'international'
            }, nodes=[895371274]),
            dsl.relation(4234377, {
                'service': 'regional',
                'colour': 'SaddleBrown',
                'ref': '230-296',
                'destination': 'Buffalo',
                'FIXME': 'Messy infrastructure around Buffalo Central Terminal',
                'direction': 'north',
                'from': 'New York Penn Station',
                'name': 'Empire Service (Northbound)',
                'network': 'Amtrak',
                'operator': 'Amtrak',
                'passenger': 'regional',
                'public_transport:version': '2',
                'route': 'train',
                'to': 'Buffalo',
                'type': 'route',
                'via': 'Albany-Rensselaer',
                'website': 'http://www.amtrak.com/',
                'wikidata': 'Q989490',
                'wikipedia': 'en:Empire Service (train)'
            }, nodes=[895371274]),
            dsl.relation(4234911, {
                'passenger': 'national',
                'service': 'regional',
                'colour': 'saddlebrown',
                'wikipedia': 'en:Ethan Allen Express',
                'ref': '290-296',
                'website': 'http://www.amtrak.com/',
                'wikidata': 'Q254597',
                'name': 'Ethan Allen Express (Northbound)',
                'to': 'Rutland, VT',
                'type': 'route',
                'route': 'train',
                'direction': 'north',
                'from': 'New York Penn Station',
                'operator': 'Amtrak',
                'public_transport:version': '2'
            }, nodes=[895371274]),
            dsl.relation(4445771, {
                'passenger': 'national',
                'service': 'regional',
                'wikipedia': 'en:Ethan Allen Express',
                'colour': 'saddlebrown',
                'wikidata': 'Q254597',
                'name': 'Ethan Allen Express (Southbound)',
                'ref': '290-296',
                'from': 'Rutland, VT',
                'type': 'route',
                'to': 'New York Penn Station',
                'direction': 'south',
                'operator': 'Amtrak',
                'public_transport:version': '2',
                'route': 'train'
            }, nodes=[895371274]),
            dsl.relation(4452779, {
                'service': 'regional',
                'colour': 'SaddleBrown',
                'ref': '230-296',
                'destination': 'New York, NY',
                'direction': 'south',
                'wikipedia': 'en:Empire Service (train)',
                'to': 'Buffalo',
                'FIXME': 'Messy infrastructure around Buffalo Central Terminal',
                'name': 'Empire Service (Southbound)',
                'network': 'Amtrak',
                'operator': 'Amtrak',
                'passenger': 'regional',
                'public_transport:version': '2',
                'route': 'train',
                'type': 'route',
                'via': 'Albany-Rensselaer',
                'website': 'http://www.amtrak.com',
                'wikidata': 'Q989490'
            }, nodes=[895371274]),
            dsl.relation(4467189, {
                'service': 'international',
                'colour': 'indigo',
                'from': 'New York, NY',
                'to': 'Toronto, ON',
                'wikipedia': 'en:Maple Leaf (train)',
                'website': 'http://www.amtrak.com/',
                'name': 'Maple Leaf (Northbound)',
                'wikidata': 'Q592407',
                'wheelchair': 'yes',
                'direction': 'north',
                'network': 'Amtrak',
                'operator': 'Amtrak',
                'passenger': 'international',
                'public_transport:version': '2',
                'ref': '63',
                'route': 'train',
                'type': 'route'
            }, nodes=[895371274]),
            dsl.relation(4467190, {
                'service': 'international',
                'colour': 'indigo',
                'from': 'Toronto, ON',
                'to': 'New York, NY',
                'wikipedia': 'en:Maple Leaf (train)',
                'website': 'http://www.amtrak.com/',
                'name': 'Maple Leaf (Southbound)',
                'wikidata': 'Q592407',
                'wheelchair': 'yes',
                'direction': 'south',
                'network': 'Amtrak',
                'operator': 'Amtrak',
                'passenger': 'international',
                'public_transport:version': '2',
                'ref': '64',
                'route': 'train',
                'type': 'route'
            }, nodes=[895371274]),
            dsl.relation(4460896, {
                'from': 'Boston South Station',
                'to': 'Washington Union Station',
                'wikipedia': 'en:Acela Express',
                'FIXME': "Underlying infrastructure \"Northeast Corridor\" needs some minor track connectivity fixes",
                'wikidata': 'Q481759',
                'colour': 'red',
                'name': 'Acela Express',
                'operator': 'Amtrak',
                'passenger': 'national',
                'public_transport:version': '1',
                'ref': '2100-2297',
                'route': 'train',
                'service': 'high_speed',
                'type': 'route',
                'via': 'New York Penn Station'
            }, nodes=[895371274]),
            dsl.relation(4744254, {
                'name': '30th Street Station',
                'type': 'public_transport',
                'public_transport': 'stop_area'
            }, nodes=[895371274]),
            dsl.relation(4748609, {
                'service': 'commuter',
                'colour': 'goldenrod',
                'ref': '600-674',
                'type': 'route',
                'website': 'http://www.amtrak.com/',
                'route': 'train',
                'name': 'Keystone Service',
                'from': 'New York Penn Station',
                'public_transport:version': '1',
                'to': 'Harrisburg',
                'via': 'Philadelphia 30th Street',
                'passenger': 'regional',
                'operator': 'Amtrak',
                'network': 'Amtrak'
            }, nodes=[895371274]),
            dsl.relation(4799100, {
                'FIXME3': 'Newport News station is an odd multipolygon element; fix?',
                'service': 'regional',
                'colour': 'SaddleBrown',
                'ref': '65-67, 71, 82-198',
                'FIXME4': 'Gap around Petersburg, Virginia',
                'FIXME': "Underlying infrastructure \"Northeast Corridor\" uses high-speed tracks, not slower \"regional\" tracks",
                'name': 'Northeast Regional (Boston-Newport News/Norfolk)',
                'FIXME2': 'Track split at Quantico',
                'wikidata': 'Q1218597',
                'type': 'route',
                'note_2': "This is a \"full span\" of many routes; still to do is to split this into each individual route",
                'note': 'Early version of a route=train for NER services; still needs lots of work; coordinate with companion relation 4799101',
                'public_transport:version': '1',
                'to': 'Newport News/Norfolk, Virginia',
                'via': 'New York Penn Station, New Haven, Philadelphia 30th Street, Washington Union Station',
                'route': 'train',
                'passenger': 'regional',
                'from': 'Boston South Station',
                'operator': 'Amtrak'
            }, nodes=[895371274]),
            dsl.relation(4799101, {
                'service': 'regional',
                'colour': 'SaddleBrown',
                'ref': '82-198',
                'name': 'Northeast Regional (Boston/Springfield & Lynchburg)',
                'to': 'Lynchburg, Virginia',
                'FIXME2': 'Track split at Alexandria',
                'FIXME3': "Ordering of tracks and nodes is crazy-wrong, because of all the \"legs\"",
                'FIXME': "Underlying infrastructure \"Northeast Corridor\" uses high-speed tracks, not slower \"regional\" tracks",
                'type': 'route',
                'route': 'train',
                'passenger': 'regional',
                'from': 'Boston South Station',
                'note_2': "This is a \"full span\" of many routes; still to do is to split this into each individual route",
                'note': 'Early version of a route=train for NER services; still needs lots of work; coordinate with companion relation 4799100',
                'public_transport:version': '1',
                'via': 'New York Penn Station, New Haven, Philadelphia 30th Street, Washington Union Station',
                'operator': 'Amtrak'
            }, nodes=[895371274]),
        )

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
            relations=[1403277, 1402004, 1403278])
        self._check(
            13, 2352, 3122, 'Camden Station', 845910705, 5, [
                '845',  # MARC Camden Line: Baltimore => Washington
                '856',  # MARC Camden Line: Washington => Baltimore
            ])

    def test_castro_muni(self):
        import dsl
        z, x, y = 13, 1309, 3166
        self.generate_fixtures(
            dsl.point(297863017, dsl.tile_centre(z, x, y), {
                'source': 'openstreetmap.org',
                'name': 'Castro',
                'operator': 'San Francisco Municipal Railway',
                'railway': 'station',
                'wikidata': 'Q5050795',
                'wikipedia': 'en:Castro Street Station'
            }),
            dsl.way(256270166, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org',
                'layer': '-1',
                'name': 'Muni Metro',
                'oneway': 'yes',
                'railway': 'light_rail',
                'tunnel': 'yes'
            }),
            dsl.relation(2124174, {
                'colour': '#92278f',
                'from': 'Wawona St & 46th Ave',
                'name': 'L-Taraval: Inbound to Downtown',
                'operator': 'San Francisco Municipal Railway',
                'ref': 'L',
                'route': 'light_rail',
                'to': 'Embarcadero Station',
                'type': 'route'
            }, nodes=[297863017]),
            dsl.relation(3433312, {
                'colour': '#5a9dbd',
                'from': 'Embarcadero',
                'name': 'K-Ingleside: Outbound to Balboa Park',
                'network': 'Muni',
                'operator': 'San Francisco Municipal Railway',
                'ref': 'K',
                'route': 'light_rail',
                'to': 'Balboa Park',
                'type': 'route'
            }, nodes=[297863017]),
            dsl.relation(3433316, {
                'colour': '#d31245',
                'from': 'Sunnydale Station',
                'name': 'T-Third Street: Inbound to Downtown',
                'operator': 'San Francisco Municipal Railway',
                'public_transport:version': '2',
                'ref': 'T',
                'route': 'light_rail',
                'to': 'Balboa Park Station',
                'type': 'route'
            }, nodes=[297863017]),
            dsl.relation(3435875, {
                'colour': '#92278f',
                'from': 'Embarcadero Station',
                'name': 'L-Taraval: Outbound to SF Zoo',
                'network': 'Muni',
                'operator': 'San Francisco Municipal Railway',
                'ref': 'L',
                'route': 'light_rail',
                'to': 'Wawona St & 46th Ave',
                'type': 'route'
            }, nodes=[297863017]),
            dsl.relation(63250, {
                'colour': '#d31245',
                'from': 'West Portal Station',
                'name': 'T-Third Street: Inbound to Sunnydale',
                'operator': 'San Francisco Municipal Railway',
                'public_transport:version': '2',
                'ref': 'T',
                'route': 'light_rail',
                'to': 'Sunnydale Station',
                'type': 'route'
            }, nodes=[297863017]),
            dsl.relation(63572, {
                'colour': '#5a9dbd',
                'from': 'Balboa Park Station',
                'name': 'K-Ingleside: Inbound to Downtown',
                'network': 'Muni',
                'operator': 'San Francisco Municipal Railway',
                'ref': 'K',
                'route': 'light_rail',
                'to': 'Embarcadero Station',
                'type': 'route'
            }, nodes=[297863017]),
            dsl.relation(91022, {
                'colour': '#008752',
                'from': 'Balboa Park Station',
                'name': 'M-Ocean View: Inbound to Downtown',
                'network': 'Muni',
                'operator': 'San Francisco Municipal Railway',
                'public_transport:version': '2',
                'ref': 'M',
                'route': 'light_rail',
                'to': 'Embarcadero Station',
                'type': 'route'
            }, nodes=[297863017]),
        )
        self._check(
            13, 1309, 3166, 'Castro', 297863017, 1, [
                'K', 'L', 'M', 'T'])

    def test_30th_street_station(self):
        import dsl
        z, x, y = 13, 2385, 3102
        self.generate_fixtures(
            dsl.point(2058688536, dsl.tile_centre(z, x, y), {
                'source': 'openstreetmap.org',
                'train': 'yes',
                'name': '30th Street',
                'public_transport': 'stop_position',
                'operator': 'SEPTA',
                'network': 'SEPTA'
            }),
            dsl.point(2058688538, dsl.tile_centre(z, x, y), {
                'source': 'openstreetmap.org',
                'train': 'yes',
                'name': '30th Street',
                'public_transport': 'stop_position',
                'operator': 'SEPTA',
                'network': 'SEPTA'
            }),
            dsl.point(3426208027, dsl.tile_centre(z, x, y), {
                'source': 'openstreetmap.org',
                'train': 'yes',
                'name': '30th Street',
                'public_transport': 'stop_position',
                'operator': 'SEPTA',
                'network': 'SEPTA'
            }),
            dsl.point(3426249715, dsl.tile_centre(z, x, y), {
                'source': 'openstreetmap.org',
                'train': 'yes',
                'name': '30th Street Station',
                'public_transport': 'stop_position',
                'operator': 'Amtrak',
                'network': 'Amtrak'
            }),
            dsl.point(3426249720, dsl.tile_centre(z, x, y), {
                'source': 'openstreetmap.org',
                'train': 'yes',
                'name': '30th Street Station',
                'public_transport': 'stop_position',
                'operator': 'Amtrak',
                'network': 'Amtrak'
            }),
            dsl.point(3426249721, dsl.tile_centre(z, x, y), {
                'source': 'openstreetmap.org',
                'train': 'yes',
                'name': '30th Street Station',
                'public_transport': 'stop_position',
                'operator': 'Amtrak',
                'network': 'Amtrak'
            }),
            dsl.way(30953448, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org',
                'voltage': '12000',
                'tiger:name_base_1': 'Penn Central Railroad',
                'tiger:name_base': 'Norfolk Southern Railway',
                'tiger:cfcc': 'B11',
                'bridge': 'yes',
                'electrified': 'contact_line',
                'frequency': '25',
                'gauge': '1435',
                'historic:owner': 'Pennsylvania Railroad',
                'layer': '3',
                'operator': 'SEPTA',
                'railway': 'rail'
            }),
            dsl.way(32272623, wkt_loads('MultiPolygon (((-75.18337879999999984 39.95653970000000044, -75.1832978000000054 39.95692499999999825, -75.18227459999999951 39.95680060000000111, -75.18226249999999311 39.95685309999999646, -75.18220279999999889 39.95684669999999983, -75.1821659000000011 39.95684279999999688, -75.18208549999999946 39.95683149999999983, -75.18113019999999835 39.95670750000000027, -75.18130739999999435 39.95585009999999926, -75.18105180000000587 39.95581990000000161, -75.18108960000000707 39.95564040000000006, -75.18113549999999634 39.955422200000001, -75.1814013999999986 39.95545229999999748, -75.18149920000000463 39.95498070000000013, -75.18200889999999958 39.95504549999999711, -75.18261180000000365 39.95512219999999814, -75.18252329999999972 39.95558280000000195, -75.18277009999999905 39.95561980000000091, -75.1827246999999943 39.95582970000000245, -75.18268159999999511 39.95602889999999974, -75.18243479999999579 39.95600220000000036, -75.18235629999999503 39.95641690000000068, -75.18337879999999984 39.95653970000000044)))'), {
                'source': 'openstreetmap.org',
                'building': 'yes',
                'name': '30th Street Station',
                'wikipedia': 'en:30th Street Station',
                'public_transport': 'station',
                'railway': 'station',
                'train': 'yes',
                'layer': '3',
                'building:height': '35.4',
                'wheelchair': 'yes',
                'addr:city': 'Philadelphia',
                'addr:housenumber': '2955',
                'addr:postcode': '19104-2989',
                'addr:state': 'PA',
                'addr:street': 'Market Street',
                'building:levels': '8',
                'operator': 'amtrak'
            }),
            dsl.way(43352433, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org',
                'voltage': '12000',
                'railway': 'rail',
                'operator': 'SEPTA',
                'old_railway_operator': 'PRR',
                'bridge': 'yes',
                'electrified': 'contact_line',
                'frequency': '25',
                'gauge': '1435',
                'layer': '3'
            }),
            dsl.way(60185604, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org',
                'voltage': '12000',
                'ref': 'Track 7',
                'electrified': 'contact_line',
                'frequency': '25',
                'gauge': '1435',
                'highspeed': 'yes',
                'layer': '-1',
                'maxspeed': '177',
                'name': 'Northeast Corridor',
                'old_railway_operator': 'PRR',
                'operator': 'Amtrak',
                'railway': 'rail',
                'tiger:cfcc': 'B11',
                'tunnel': 'yes',
                'usage': 'main'
            }),
            dsl.way(60185611, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org',
                'tiger:cfcc': 'B11',
                'voltage': '12000',
                'ref': 'Track 7',
                'electrified': 'contact_line',
                'frequency': '25',
                'gauge': '1435',
                'highspeed': 'yes',
                'layer': '-1',
                'maxspeed': '177',
                'name': 'Northeast Corridor',
                'old_railway_operator': 'PRR',
                'operator': 'Amtrak',
                'railway': 'rail',
                'tunnel': 'yes',
                'usage': 'main'
            }),
            dsl.relation(1269021, {
                'note': 'This is route=railway (infrastructure), not route=train, so it should only contain track, not stations',
                'FIXME': 'Needs minor connectivity fixes in Brooklyn, Bronx, Stamford, New Haven, Wickford, New Rochelle, Newark',
                'wikipedia': 'en:Northeast Corridor',
                'from': 'Boston South Station',
                'name': 'Northeast Corridor',
                'ref': 'NEC',
                'route': 'railway',
                'to': 'Washington Union Station',
                'type': 'route',
                'wikidata': 'Q678233'
            }, ways=[32272623]),
            dsl.relation(1359387, {
                'service': 'long_distance',
                'colour': '#005480',
                'passenger': 'national',
                'website': 'http://www.amtrak.com',
                'name': 'Vermonter',
                'ref': '54-57',
                'from': 'Washington, DC',
                'public_transport:version': '1',
                'to': 'Saint Albans, Vermont',
                'via': 'New York Penn Station',
                'wikipedia': 'en:Vermonter (train)',
                'wikidata': 'Q1412872',
                'network': 'Amtrak',
                'operator': 'Amtrak',
                'route': 'train',
                'type': 'route'
            }, ways=[32272623]),
            dsl.relation(1388639, {
                'ref': 'Cynwyd Line',
                'type': 'route',
                'route': 'train',
                'operator': 'SEPTA',
                'old_ref': 'R6',
                'name': 'SEPTA - Cynwyd Line',
                'network': 'SEPTA',
                'colour': '#775CA7',
                'wikidata': 'Q5200188',
                'wikipedia': 'en:Cynwyd Line'
            }, ways=[32272623]),
            dsl.relation(1388641, {
                'name': 'Airport Line',
                'type': 'route',
                'route': 'train',
                'ref': 'AIR',
                'passenger': 'suburban',
                'operator': 'SEPTA',
                'wikidata': 'Q4698916',
                'wikipedia': 'en:Airport Line (SEPTA)',
                'colour': '#91456C',
                'network': 'SEPTA',
                'old_ref': 'R1'
            }, ways=[32272623]),
            dsl.relation(1388648, {
                'ref': 'Chestnut Hill West Line',
                'type': 'route',
                'route': 'train',
                'operator': 'SEPTA',
                'old_ref': 'R8',
                'name': 'SEPTA - Chestnut Hill West Line',
                'network': 'SEPTA',
                'colour': '#00BBB3',
                'wikidata': 'Q5093959',
                'wikipedia': 'en:Chestnut Hill West Line'
            }, ways=[32272623]),
            dsl.relation(1390116, {
                'ref': 'Trenton Line',
                'type': 'route',
                'route': 'train',
                'operator': 'SEPTA',
                'old_ref': 'R7',
                'name': 'SEPTA - Trenton Line',
                'network': 'SEPTA',
                'colour': '#F686C3',
                'wikidata': 'Q7838588',
                'wikipedia': 'en:Trenton Line (SEPTA)'
            }, ways=[32272623]),
            dsl.relation(1390117, {
                'ref': 'Media/Elwyn Line',
                'type': 'route',
                'route': 'train',
                'operator': 'SEPTA',
                'old_ref': 'R3',
                'name': 'SEPTA - Media/Elwyn Line',
                'network': 'SEPTA',
                'colour': '#0081C5',
                'wikidata': 'Q6805374',
                'wikipedia': 'en:Media/Elwyn Line'
            }, ways=[32272623]),
            dsl.relation(1390133, {
                'ref': 'Wilmington/Newark Line',
                'type': 'route',
                'route': 'train',
                'operator': 'SEPTA',
                'old_ref': 'R2',
                'name': 'SEPTA - Wilmington/Newark Line',
                'network': 'SEPTA',
                'colour': '#8ED16A',
                'wikidata': 'Q8022734',
                'wikipedia': 'en:Wilmington/Newark Line'
            }, ways=[32272623]),
            dsl.relation(1402781, {
                'type': 'route',
                'route': 'railway',
                'old_railway_operator': 'PRR',
                'FIXME': 'Exactly where was the north end?',
                'name': 'Main Line (New York to Philadelphia)'
            }, ways=[32272623]),
            dsl.relation(1405499, {
                'historic:owner': 'Pennsylvania Railroad',
                'type': 'route',
                'name': 'Main Line (Philadelphia to Washington)',
                'route': 'railway'
            }, ways=[32272623]),
            dsl.relation(1590286, {
                'service': 'long_distance',
                'colour': '#005480',
                'wikipedia': 'en:Silver Meteor',
                'from': 'New York, NY',
                'to': 'Miami, FL',
                'network': 'Amtrak Intercity',
                'name': 'Silver Meteor',
                'ref': '97-98',
                'public_transport:version': '1',
                'wikidata': 'Q389948',
                'type': 'route',
                'operator': 'Amtrak',
                'passenger': 'national',
                'route': 'train'
            }, ways=[32272623]),
            dsl.relation(1809808, {
                'service': 'long_distance',
                'colour': '#005480',
                'from': 'New York, NY',
                'to': 'New Orleans, LA',
                'wikipedia': 'en:Crescent (train)',
                'network': 'Amtrak Intercity',
                'name': 'Crescent',
                'ref': '19-20',
                'public_transport:version': '1',
                'wikidata': 'Q756508',
                'type': 'route',
                'operator': 'Amtrak',
                'passenger': 'national',
                'route': 'train'
            }, ways=[32272623]),
            dsl.relation(1897938, {
                'service': 'long_distance',
                'colour': '#005480',
                'wikipedia': 'en:Silver Star (Amtrak train)',
                'from': 'New York, NY',
                'network': 'Amtrak Intercity',
                'wikidata': 'Q665435',
                'website': 'http://www.amtrak.com/',
                'type': 'route',
                'name': 'Silver Star',
                'ref': '91-92',
                'public_transport:version': '1',
                'to': 'Miami, FL',
                'route': 'train',
                'passenger': 'national',
                'operator': 'Amtrak'
            }, ways=[32272623]),
            dsl.relation(1900976, {
                'service': 'long_distance',
                'colour': '#005480',
                'to': 'Charlotte, NC',
                'wikipedia': 'en:Carolinian (train)',
                'website': 'http://www.amtrak.com/',
                'network': 'Amtrak Intercity',
                'name': 'Carolinian',
                'ref': '79-80',
                'public_transport:version': '1',
                'wikidata': 'Q283663',
                'type': 'route',
                'from': 'New York Penn Station',
                'operator': 'Amtrak',
                'passenger': 'national',
                'route': 'train'
            }, ways=[32272623]),
            dsl.relation(206515, {
                'website': 'http://www.njtransit.com/',
                'network': 'NJTR',
                'type': 'route',
                'route': 'train',
                'name': 'NJT - Atlantic City Line',
                'ref': 'Atlantic City',
                'wikidata': 'Q756350',
                'wikipedia': 'en:Atlantic City Line',
                'colour': '#015DAB',
                'operator': 'New Jersey Transit',
                'passenger': 'suburban'
            }, ways=[32272623]),
            dsl.relation(2629937, {
                'name': 'Paoli/Thorndale Line',
                'network': 'SEPTA Regional Rail',
                'ref': 'Paoli/Thorndale Line',
                'via': 'Paoli',
                'type': 'route',
                'route': 'train',
                'operator': 'SEPTA',
                'from': 'Thorndale',
                'colour': '#20825C',
                'to': 'Suburban Station'
            }, ways=[32272623]),
            dsl.relation(2629938, {
                'name': 'Paoli/Thorndale Line',
                'to': 'Throrndale',
                'via': 'Paoli',
                'type': 'route',
                'route': 'train',
                'from': 'Suburban Station',
                'ref': 'PAO',
                'operator': 'SEPTA',
                'network': 'SEPTA',
                'colour': '#20825C'
            }, ways=[32272623]),
            dsl.relation(2648181, {
                'service': 'long_distance',
                'colour': '#005480',
                'network': 'Amtrak Intercity',
                'from': 'New York Penn Station',
                'website': 'http://www.amtrak.com/',
                'name': 'Palmetto',
                'ref': '89-90',
                'wikipedia': 'en:Palmetto (train)',
                'public_transport:version': '1',
                'to': 'Savannah, GA',
                'wikidata': 'Q944742',
                'type': 'route',
                'operator': 'Amtrak',
                'passenger': 'national',
                'route': 'train'
            }, ways=[32272623]),
            dsl.relation(2807121, {
                'FIXME': "Numerous \"track splits\" (likely missing crossovers); Chicago between Harvey and Union Station",
                'service': 'long_distance',
                'colour': '#005480',
                'wikipedia': 'en:Cardinal (train)',
                'network': 'Amtrak Intercity',
                'wikidata': 'Q858400',
                'name': 'Cardinal',
                'ref': '50-51',
                'public_transport:version': '1',
                'type': 'route',
                'to': 'New York Penn Station',
                'from': 'Chicago Union Station',
                'operator': 'Amtrak',
                'passenger': 'national',
                'route': 'train'
            }, ways=[32272623]),
            dsl.relation(4044002, {
                'passenger': 'national',
                'service': 'regional',
                'colour': '#005480',
                'wikipedia': 'en:Pennsylvanian (train)',
                'website': 'http://www.amtrak.com/',
                'name': 'Pennsylvanian',
                'ref': '42-43',
                'from': 'New York Penn Station',
                'to': 'Pittsburgh',
                'public_transport:version': '1',
                'wikidata': 'Q654593',
                'type': 'route',
                'network': 'Amtrak',
                'operator': 'Amtrak',
                'route': 'train'
            }, ways=[32272623]),
            dsl.relation(4460896, {
                'from': 'Boston South Station',
                'to': 'Washington Union Station',
                'wikipedia': 'en:Acela Express',
                'FIXME': "Underlying infrastructure \"Northeast Corridor\" needs some minor track connectivity fixes",
                'wikidata': 'Q481759',
                'colour': 'red',
                'name': 'Acela Express',
                'operator': 'Amtrak',
                'passenger': 'national',
                'public_transport:version': '1',
                'ref': '2100-2297',
                'route': 'train',
                'service': 'high_speed',
                'type': 'route',
                'via': 'New York Penn Station'
            }, ways=[32272623]),
            dsl.relation(4744254, {
                'name': '30th Street Station',
                'type': 'public_transport',
                'public_transport': 'stop_area'
            }, ways=[32272623]),
            dsl.relation(4748609, {
                'service': 'commuter',
                'colour': 'goldenrod',
                'ref': '600-674',
                'type': 'route',
                'website': 'http://www.amtrak.com/',
                'route': 'train',
                'name': 'Keystone Service',
                'from': 'New York Penn Station',
                'public_transport:version': '1',
                'to': 'Harrisburg',
                'via': 'Philadelphia 30th Street',
                'passenger': 'regional',
                'operator': 'Amtrak',
                'network': 'Amtrak'
            }, ways=[32272623]),
            dsl.relation(4799100, {
                'FIXME3': 'Newport News station is an odd multipolygon element; fix?',
                'service': 'regional',
                'colour': 'SaddleBrown',
                'ref': '65-67, 71, 82-198',
                'FIXME4': 'Gap around Petersburg, Virginia',
                'FIXME': "Underlying infrastructure \"Northeast Corridor\" uses high-speed tracks, not slower \"regional\" tracks",
                'name': 'Northeast Regional (Boston-Newport News/Norfolk)',
                'FIXME2': 'Track split at Quantico',
                'wikidata': 'Q1218597',
                'type': 'route',
                'note_2': "This is a \"full span\" of many routes; still to do is to split this into each individual route",
                'note': 'Early version of a route=train for NER services; still needs lots of work; coordinate with companion relation 4799101',
                'public_transport:version': '1',
                'to': 'Newport News/Norfolk, Virginia',
                'via': 'New York Penn Station, New Haven, Philadelphia 30th Street, Washington Union Station',
                'route': 'train',
                'passenger': 'regional',
                'from': 'Boston South Station',
                'operator': 'Amtrak'
            }, ways=[32272623]),
            dsl.relation(4799101, {
                'service': 'regional',
                'colour': 'SaddleBrown',
                'ref': '82-198',
                'name': 'Northeast Regional (Boston/Springfield & Lynchburg)',
                'to': 'Lynchburg, Virginia',
                'FIXME2': 'Track split at Alexandria',
                'FIXME3': "Ordering of tracks and nodes is crazy-wrong, because of all the \"legs\"",
                'FIXME': "Underlying infrastructure \"Northeast Corridor\" uses high-speed tracks, not slower \"regional\" tracks",
                'type': 'route',
                'route': 'train',
                'passenger': 'regional',
                'from': 'Boston South Station',
                'note_2': "This is a \"full span\" of many routes; still to do is to split this into each individual route",
                'note': 'Early version of a route=train for NER services; still needs lots of work; coordinate with companion relation 4799100',
                'public_transport:version': '1',
                'via': 'New York Penn Station, New Haven, Philadelphia 30th Street, Washington Union Station',
                'operator': 'Amtrak'
            }, ways=[32272623]),
        )

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
