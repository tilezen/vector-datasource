from . import OsmFixtureTest


class ComboOutdoorLandusePois(OsmFixtureTest):
    def test_water_park_way(self):
        # Waterworld in Concord
        self.load_fixtures(['http://www.openstreetmap.org/way/31198945'])

        self.assert_has_feature(
            13, 1318, 3160, 'landuse',
            {'kind': 'water_park', 'sort_rank': 107})

        self.assert_has_feature(
            13, 1318, 3160, 'pois',
            {'kind': 'water_park', 'min_zoom': 13})

    def test_water_park_node(self):
        # Antioch WaterPark
        self.load_fixtures(['http://www.openstreetmap.org/node/2753215890'])

        self.assert_has_feature(
            16, 10600, 25287, 'pois',
            {'kind': 'water_park', 'min_zoom': 15})

    def test_beach_resort_way(self):
        # Sandos Finisterra Los Cabos, extra large resort
        self.load_fixtures(['http://www.openstreetmap.org/way/381817396'])

        self.assert_has_feature(
            14, 3189, 7122, 'pois',
            {'kind': 'beach_resort', 'min_zoom': 14})

    def test_beach_resort_node(self):
        # Hilton Hawaiian Village
        # really this should be merged with its large AOI!
        self.load_fixtures(['http://www.openstreetmap.org/node/2407351205'])

        self.assert_has_feature(
            16, 4034, 28801, 'pois',
            {'kind': 'beach_resort', 'min_zoom': 16})

    def test_another_beach_resort_node(self):
        # Silver Gull Beach Club
        self.load_fixtures(['http://www.openstreetmap.org/node/3575812477'])

        self.assert_has_feature(
            16, 19314, 24677, 'pois',
            {'kind': 'beach_resort', 'min_zoom': 16})

    def test_beach_resort_hotel(self):
        # Terrasol Beach Resort
        # Needs to appear **before** tourism=hotel
        self.load_fixtures(['https://www.openstreetmap.org/way/381817391'])

        self.assert_has_feature(
            16, 12760, 28488, 'pois',
            {'id': 381817391, 'kind': 'beach_resort'})

    def test_beach(self):
        # Needs to appear **after** natural=beach.
        # Unnamed beach in Maskenthine Lake area
        self.load_fixtures(['https://www.openstreetmap.org/way/257716817'])

        self.assert_has_feature(
            16, 15066, 24333, 'landuse',
            {'kind': 'beach', 'id': 257716817})

    def test_summer_camp(self):
        # Camp Ahmek
        self.load_fixtures(['https://www.openstreetmap.org/node/3655879348'])

        self.assert_has_feature(
            15, 9219, 11714, 'pois',
            {'kind': 'summer_camp', 'min_zoom': 15})

        # Camp Goodtimes
        self.load_fixtures(['https://www.openstreetmap.org/node/4050178586'])

        self.assert_has_feature(
            15, 5225, 11211, 'pois',
            {'kind': 'summer_camp', 'min_zoom': 15})

    def test_battlefield_nodes(self):
        # Battle of Blackburn's Ford (1861)
        self.load_fixtures(['https://www.openstreetmap.org/node/3838356961'])

        self.assert_has_feature(
            16, 18668, 25092, 'pois',
            {'kind': 'battlefield', 'min_zoom': 17})

        # 2nd Battle of Kernstown
        self.load_fixtures(['https://www.openstreetmap.org/node/3992988013'])

        self.assert_has_feature(
            16, 18532, 25013, 'pois',
            {'kind': 'battlefield', 'min_zoom': 17})

    def test_battlefield_ways(self):
        # Antietam National Battlefield
        self.load_fixtures(['https://www.openstreetmap.org/way/231393152'])

        self.assert_has_feature(
            10, 290, 389, 'pois',
            {'kind': 'battlefield', 'min_zoom': 10})

        self.assert_has_feature(
            10, 290, 389, 'landuse',
            {'kind': 'battlefield', 'sort_rank': 25})

        # White Oak Road Battlefield
        self.load_fixtures(['http://www.openstreetmap.org/way/316054549'])

        self.assert_has_feature(
            11, 582, 796, 'pois',
            {'kind': 'battlefield', 'min_zoom': 10.07})

        self.assert_has_feature(
            11, 582, 796, 'landuse',
            {'kind': 'battlefield', 'sort_rank': 25})

    def test_boat_storage_node(self):
        # unnamed Boat Storage
        self.load_fixtures(['https://www.openstreetmap.org/node/2117389172'])

        self.assert_has_feature(
            16, 10563, 25453, 'pois',
            {'kind': 'boat_storage', 'min_zoom': 17})

    def test_boat_storage_way(self):
        # in Tiburon, CA
        self.load_fixtures(['https://www.openstreetmap.org/way/261064362'])

        self.assert_has_feature(
            16, 10476, 25304, 'pois',
            {'kind': 'boat_storage', 'min_zoom': 17})

    def test_monument_nodes(self):
        # Red Cross monument in DC
        self.load_fixtures(['https://www.openstreetmap.org/node/3314950786'])

        self.assert_has_feature(
            16, 18742, 25070, 'pois',
            {'kind': 'monument', 'min_zoom': 17})

        # Major General James B. McPherson in DC
        self.load_fixtures(['https://www.openstreetmap.org/node/2316449632'])

        self.assert_has_feature(
            16, 18744, 25069, 'pois',
            {'kind': 'monument', 'min_zoom': 17})

    def test_monument_ways(self):
        # polygon but no landuse / Netherlands Carillon near DC
        self.load_fixtures(['https://www.openstreetmap.org/way/41273627'])

        self.assert_has_feature(
            16, 18737, 25072, 'pois',
            {'kind': 'monument', 'min_zoom': (lambda z: z >= 16 and z < 17)})

        # building, Jefferson Monument
        self.load_fixtures(['https://www.openstreetmap.org/way/248460669'])

        self.assert_has_feature(
            15, 9371, 12537, 'pois',
            {'kind': 'monument', 'min_zoom': 15})

    def test_monument_building_attraction(self):
        # building, and tourism=attraction, National World War II Memorial
        self.load_fixtures(['https://www.openstreetmap.org/way/66418767'])

        self.assert_has_feature(
            15, 9371, 12536, 'pois',
            {'kind': 'monument', 'min_zoom': 15})

    def test_dam_node(self):
        # Letts Valley 1-039 Dam
        self.load_fixtures(['https://www.openstreetmap.org/node/358811238'])

        self.assert_has_feature(
            14, 2607, 6243, 'pois',
            {'kind': 'dam', 'min_zoom': 14})

    def test_dam_way(self):
        # O'Shaughnessy Dam, Yosemite
        # 13, 1370, 3161
        self.load_fixtures(['https://www.openstreetmap.org/way/189656737'])

        self.assert_has_feature(
            12, 685, 1580, 'landuse',
            {'kind': 'dam', 'sort_rank': 223})

        self.assert_has_feature(
            12, 685, 1580, 'pois',
            {'kind': 'dam', 'min_zoom': 12})

    def test_linear_dam_way(self):
        # Named dam line in front of Cherry Lake
        # Should be labeled in the stylesheet, no POI generate
        self.load_fixtures(['https://www.openstreetmap.org/way/62201624'])

        self.assert_has_feature(
            12, 683, 1580, 'landuse',
            {'kind': 'dam', "sort_rank": 265})

    def test_dog_park_node(self):
        # Indian Lake Dog Exercise Area, near Madison, WI
        self.load_fixtures(['http://www.openstreetmap.org/node/262220409'])

        self.assert_has_feature(
            16, 16450, 24033, 'pois',
            {'kind': 'dog_park', 'min_zoom': 17})

    def test_dog_park_ways(self):
        # Dog Run at Upper Noe Valley Rec Center, SF
        self.load_fixtures(['https://www.openstreetmap.org/way/417184097'])

        self.assert_has_feature(
            16, 10480, 25338, 'pois',
            {'kind': 'dog_park', 'min_zoom': 16})

        # Dog park at Walter Hass Playground, SF
        self.load_fixtures(['https://www.openstreetmap.org/way/375333476'])

        self.assert_has_feature(
            16, 10479, 25338, 'pois',
            {'kind': 'dog_park', 'min_zoom': 16})

        self.assert_has_feature(
            16, 10479, 25338, 'landuse',
            {'kind': 'dog_park', 'sort_rank': 97})

    def test_recreation_track_way(self):
        # Red Gra / Running Track
        self.load_fixtures(['http://www.openstreetmap.org/way/95922608'])

        self.assert_has_feature(
            15, 16384, 10951, 'landuse',
            {'id': 95922608, 'kind': 'recreation_track', 'sort_rank': 59})

        # Cox Stadium recreation track
        self.assert_has_feature(
            16, 32768, 21903, 'pois',
            {'id': 95922608, 'kind': 'recreation_track', 'min_zoom': 16})

    def test_recreation_track_nodes(self):
        # Pista de Atletismo
        self.load_fixtures(['http://www.openstreetmap.org/node/4218421638'])

        self.assert_has_feature(
            16, 21060, 39942, 'pois',
            {'kind': 'recreation_track', 'min_zoom': 17})

        # cycle, Sand Pit
        self.load_fixtures(['https://www.openstreetmap.org/node/418185265'])

        self.assert_has_feature(
            16, 10556, 25509, 'pois',
            {'kind': 'recreation_track', 'min_zoom': 17})

        # motor, Mazda Raceway Laguna Seca
        self.load_fixtures(['https://www.openstreetmap.org/node/444949878'])

        self.assert_has_feature(
            16, 10603, 25602, 'pois',
            {'kind': 'recreation_track', 'min_zoom': 17})

    def test_fishing_area_node(self):
        # Unnamed fishing spot near Davis, CA
        self.load_fixtures(['https://www.openstreetmap.org/node/2613055910'])

        self.assert_has_feature(
            16, 10602, 25159, 'pois',
            {'kind': 'fishing_area', 'min_zoom': 17})

    def test_fishing_area_ways(self):
        #    16, 10471, 22459, 'pois',
        self.load_fixtures(['https://www.openstreetmap.org/way/62099107'])

        self.assert_has_feature(
            16, 10471, 22460, 'pois',
            {'kind': 'fishing_area', 'min_zoom': 16})

        # Alpine Lake
        self.load_fixtures(['https://www.openstreetmap.org/way/234164554'])

        self.assert_has_feature(
            16, 12454, 24647, 'pois',
            {'kind': 'fishing_area', 'min_zoom': 16})

    def test_swimming_area_node(self):
        # Swimming hole at Seneca Rocks
        self.load_fixtures(['https://www.openstreetmap.org/node/3733554139'])

        self.assert_has_feature(
            16, 18319, 25083, 'pois',
            {'kind': 'swimming_area', 'min_zoom': 16})

    def test_swimming_area_way(self):
        # Pine Lake Swimming Beach
        self.load_fixtures(['https://www.openstreetmap.org/way/368533731'])

        self.assert_has_feature(
            #    16, 10551, 22893, 'pois',
            16, 10551, 22892, 'pois',
            {'kind': 'swimming_area', 'min_zoom': 16})

    def test_firepit_node(self):
        # UC Berkeley area
        self.load_fixtures(['https://www.openstreetmap.org/node/3795571179'])

        self.assert_has_feature(
            16, 10509, 25309, 'pois',
            {'kind': 'firepit', 'min_zoom': 18})

    def test_firepit_way(self):
        # Bloomfield area
        self.load_fixtures(['https://www.openstreetmap.org/way/349337076'])

        self.assert_has_feature(
            16, 10742, 24971, 'pois',
            {'kind': 'firepit', 'min_zoom': 18})

    def test_stone(self):
        # Old Man Boulder
        self.load_fixtures(['https://www.openstreetmap.org/way/329837642'])

        self.assert_has_feature(
            16, 10442, 25304, 'landuse',
            {'kind': 'stone', 'sort_rank': 28})

        self.assert_has_feature(
            16, 10442, 25304, 'pois',
            {'kind': 'stone', 'min_zoom': 17, 'name': 'Old Man Boulder'})

    def test_rock(self):
        # Goodrich Pinnacle
        self.load_fixtures(['https://www.openstreetmap.org/way/377706598'])

        self.assert_has_feature(
            16, 11001, 25340, 'landuse',
            {'kind': 'rock', 'sort_rank': 27})

        self.assert_has_feature(
            16, 11001, 25340, 'pois',
            {'kind': 'rock', 'min_zoom': 17, 'name': 'Goodrich Pinnacle'})

    def test_caravan_site_node(self):
        # Redwood Acres RV Park, Eureka CA
        self.load_fixtures(['https://www.openstreetmap.org/node/2246385222'])

        self.assert_has_feature(
            15, 5085, 12312, 'pois',
            {'kind': 'caravan_site', 'min_zoom': 15})

    def test_caravan_site_way(self):
        # Pillar Point RV Park
        self.load_fixtures(['https://www.openstreetmap.org/way/291546386'])

        self.assert_has_feature(
            14, 2618, 6348, 'landuse',
            {'kind': 'caravan_site', 'sort_rank': 58})

        self.assert_has_feature(
            14, 2618, 6348, 'pois',
            {'kind': 'caravan_site', 'min_zoom': 14})

    def test_picnic_site_node(self):
        # South Park, SF
        self.load_fixtures(['https://www.openstreetmap.org/node/2401887217'])

        self.assert_has_feature(
            16, 10486, 25329, 'pois',
            {'kind': 'picnic_site', 'min_zoom': 16})

        # Why is this missing?
        # Golden Gate Park, SF
        self.load_fixtures(['https://www.openstreetmap.org/node/3297410094'])

        self.assert_has_feature(
            16, 10472, 25332, 'pois',
            {'kind': 'picnic_site', 'min_zoom': 16})

    def test_picnic_site_way(self):
        # Golden Gate Park, SF
        self.load_fixtures(['https://www.openstreetmap.org/way/400701941'])

        self.assert_has_feature(
            16, 10474, 25332, 'landuse',
            {'kind': 'picnic_site', 'sort_rank': 108})

        self.assert_has_feature(
            16, 10474, 25332, 'pois',
            {'kind': 'picnic_site', 'min_zoom': 16})

    def test_picnic_site_building(self):
        # building, South Park, SF
        self.load_fixtures(['https://www.openstreetmap.org/way/231863022'])

        self.assert_has_feature(
            16, 10486, 25329, 'pois',
            {'kind': 'picnic_site', 'min_zoom': 16, 'id': 231863022})

    def test_fort_node(self):
        # Fort Strong
        self.load_fixtures(['https://www.openstreetmap.org/node/1148222790'])

        self.assert_has_feature(
            16, 19850, 24247, 'pois',
            {'kind': 'fort', 'min_zoom': 16})

    def test_fort_way(self):
        # Battery 2
        self.load_fixtures(['https://www.openstreetmap.org/way/265893625'])

        self.assert_has_feature(
            16, 19303, 24607, 'landuse',
            {'kind': 'fort', 'sort_rank': 47})

        self.assert_has_feature(
            16, 19303, 24607, 'pois',
            {'kind': 'fort', 'min_zoom': (lambda z: z >= 15 and z < 16)})

        # Fort Monroe
        self.load_fixtures(['https://www.openstreetmap.org/way/51064272'])

        self.assert_has_feature(
            13, 2359, 3188, 'landuse',
            {'kind': 'fort'})

        self.assert_has_feature(
            13, 2359, 3188, 'pois',
            {'kind': 'fort', 'min_zoom': 13, 'name': 'Fort Monroe'})
