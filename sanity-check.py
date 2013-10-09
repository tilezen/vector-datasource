from TileStache import requestHandler
from ModestMaps.OpenStreetMap import Provider
from ModestMaps.Geo import Location
from json import loads

osm = Provider()
loc = Location(37.795545, -122.393422)

stuff = [
    ('highroad', 10),
    ('highroad', 11),
    ('highroad', 12),
    ('highroad', 13),
    ('highroad', 14),
    ('highroad', 15),
    ('highroad-2x', 9),
    ('highroad-2x', 10),
    ('highroad-2x', 11),
    ('highroad-2x', 12),
    ('highroad-2x', 13),
    ('highroad-2x', 14),
    ('skeletron', 12),
    ('skeletron', 13),
    ('skeletron', 14),
    ('skeletron', 15),
    ('skeletron', 16),
    ('skeletron-2x', 11),
    ('skeletron-2x', 12),
    ('skeletron-2x', 13),
    ('skeletron-2x', 14),
    ('skeletron-2x', 15),
    ('land-usages', 4),
    ('land-usages', 5),
    ('land-usages', 6),
    ('land-usages', 7),
    ('land-usages', 8),
    ('land-usages', 9),
    ('land-usages', 10),
    ('land-usages', 11),
    ('land-usages', 12),
    ('land-usages', 13),
    ('land-usages', 14),
    ('land-usages', 15),
    ('land-usages', 16),
    ('water-areas', 0),
    ('water-areas', 1),
    ('water-areas', 2),
    ('water-areas', 3),
    ('water-areas', 4),
    ('water-areas', 5),
    ('water-areas', 6),
    ('water-areas', 7),
    ('water-areas', 8),
    ('water-areas', 9),
    ('water-areas', 10),
    ('water-areas', 11),
    ('water-areas', 12),
    ('water-areas', 13),
    ('water-areas', 14),
    ('water-areas', 15),
    ('water-areas', 16),
    ('buildings', 12),
    ('buildings', 13),
    ('buildings', 14),
    ('buildings', 15),
    ('buildings', 16),
    ('pois', 9),
    ('pois', 10),
    ('pois', 11),
    ('pois', 12),
    ('pois', 13),
    ('pois', 14),
    ('pois', 15),
    ('pois', 16),
    ('pois', 17),
    ('pois', 18),
    ]

for (layer, zoom) in stuff:
    
    coord = osm.locationCoordinate(loc).zoomTo(zoom)
    tile = '%(zoom)d/%(column)d/%(row)d' % coord.__dict__
    path = '/%(layer)s/%(tile)s.json' % locals()
    
    print path, '?'
    
    mime, body = requestHandler('tilestache.cfg', path, None)
    
    assert '/json' in mime, 'Bad mime-type: %s' % mime
    
    data = loads(body)
    
    assert data['type'] == 'FeatureCollection', 'Bad data: %s' % body
    assert 'id' in data['features'][0], 'Bad data: %s' % body
