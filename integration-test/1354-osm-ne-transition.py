# checks that the OSM->NE transition happens for the given layer between the
# z/x/y coordinate given and the parent tile (z-1)/(x/2)/(y/2)
def osm_ne_transition(z, x, y, layer):
    osm = {'source': set(['openstreetmap.org', 'openstreetmapdata.com'])}
    ne = {'source': 'naturalearthdata.com'}

    # assert OSM feature exists at upper zoom level
    test.assert_has_feature(z, x, y, layer, osm)
    test.assert_no_matching_feature(z, x, y, layer, ne)

    # assert NE feature exists at lower zoom level
    test.assert_has_feature(z-1, x/2, y/2, layer, ne)
    test.assert_no_matching_feature(z-1, x/2, y/2, layer, osm)

# NE roads fixture from 976-fractional-pois
# OSM roads: I-678
# http://www.openstreetmap.org/relation/1675644
osm_ne_transition(8, 75, 96, 'roads')
# NE earth fixture from 399-ne-10m-land
# OSM 399-earth-fixture
osm_ne_transition(8, 40, 98, 'earth')
# NE water fixture from 1030-invalid-wkb-polygon
# OSM 1354-osm-ne-transition
osm_ne_transition(8, 136, 80, 'water')
# NE boundaries fixture 841-normalize-boundaries
# OSM: Swedish country boundary
# http://www.openstreetmap.org/relation/52822
osm_ne_transition(8, 136, 72, 'boundaries')
