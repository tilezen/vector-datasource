from . import FixtureTest


class RangerStation(FixtureTest):
    def test_ranger_station_supersedes_tourism(self):
        # Big Basin Redwoods State Park Headquarters
        # Node with amenity=ranger_station, but also has tourism=information
        # set
        self.load_fixtures(['http://www.openstreetmap.org/node/1996636138'])

        self.assert_has_feature(
            14, 2629, 6367, 'pois',
            {'kind': 'ranger_station', 'min_zoom': 14})

        # Pantoll Ranger Station
        # Node with amenity=ranger_station, but also has tourism=information
        # set
        self.load_fixtures(['https://www.openstreetmap.org/node/351892607'])

        self.assert_has_feature(
            14, 2612, 6325, 'pois',
            {'kind': 'ranger_station', 'min_zoom': 14})

    def test_building_ranger_station(self):
        # Building with amenity=ranger_station
        self.load_fixtures(['http://www.openstreetmap.org/way/361301773'])

        self.assert_has_feature(
            14, 2617, 6329, 'pois',
            {'kind': 'ranger_station', 'min_zoom': 14})

        # Entrance Yosemite Nationalpark
        # Building with amenity=ranger_station
        self.load_fixtures(['https://www.openstreetmap.org/way/269908344'])

        self.assert_has_feature(
            14, 2742, 6337, 'pois',
            {'kind': 'ranger_station', 'min_zoom': 14})
