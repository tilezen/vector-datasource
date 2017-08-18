from itertools import izip


def mz_building_kind_detail(val):
    # TODO should this be in yaml instead?
    if val in (
            'bangunan',
            'building',
            'other',
            'rumah',
            'Rumah',
            'Rumah Masyarakat',
            'rumah_penduduk',
            'true',
            'trullo',
            'yes'):
        return None

    if val in (
            'abandoned',
            'administrative',
            'agricultural',
            'airport',
            'allotment_house',
            'apartments',
            'arbour',
            'bank',
            'barn',
            'basilica',
            'beach_hut',
            'bell_tower',
            'boathouse',
            'brewery',
            'bridge',
            'bungalow',
            'bunker',
            'cabin',
            'carport',
            'castle',
            'cathedral',
            'chapel',
            'chimney',
            'church',
            'civic',
            'clinic',
            'clubhouse',
            'collapsed',
            'college',
            'commercial',
            'construction',
            'container',
            'convent',
            'cowshed',
            'dam',
            'damaged',
            'depot',
            'destroyed',
            'detached',
            'disused',
            'dormitory',
            'duplex',
            'factory',
            'farm',
            'farm_auxiliary',
            'fire_station',
            'garage',
            'garages',
            'gazebo',
            'ger',
            'glasshouse',
            'government',
            'grandstand',
            'greenhouse',
            'hangar',
            'healthcare',
            'hermitage',
            'hospital',
            'hotel',
            'house',
            'houseboat',
            'hut',
            'industrial',
            'kindergarten',
            'kiosk',
            'library',
            'mall',
            'manor',
            'manufacture',
            'mobile_home',
            'monastery',
            'mortuary',
            'mosque',
            'museum',
            'office',
            'outbuilding',
            'parking',
            'pavilion',
            'power',
            'prison',
            'proposed',
            'pub',
            'public',
            'residential',
            'restaurant',
            'retail',
            'roof',
            'ruin',
            'ruins',
            'school',
            'semidetached_house',
            'service',
            'shed',
            'shelter',
            'shop',
            'shrine',
            'silo',
            'slurry_tank',
            'stable',
            'stadium',
            'static_caravan',
            'storage',
            'storage_tank',
            'store',
            'substation',
            'summer_cottage',
            'summer_house',
            'supermarket',
            'synagogue',
            'tank',
            'temple',
            'terrace',
            'tower',
            'train_station',
            'transformer_tower',
            'transportation',
            'university',
            'utility',
            'veranda',
            'warehouse',
            'wayside_shrine',
            'works'):
        return val

    if val == 'barne':
        return 'barn'
    if val == 'commercial;residential':
        return 'mixed_use'
    if val == 'constructie':
        return 'construction'
    if val == 'dwelling_house':
        return 'house'
    if val == 'education':
        return 'school'
    if val == 'greenhouse_horticulture':
        return 'greenhouse'
    if val in ('apartment', 'flat'):
        return 'apartments'
    if val in ('houses', 'residences', 'residence', 'perumahan permukiman',
               'residentiel1'):
        return 'residential'
    if val in ('semi_detached', 'semi-detached', 'semi'):
        return 'semidetached_house'
    if val == 'offices':
        return 'office'
    if val == 'prefab_container':
        return 'container'
    if val == 'public_building':
        return 'public'
    if val == 'railway_station':
        return 'train_station'
    if val == 'roof=permanent':
        return 'roof'
    if val == 'stables':
        return 'stable'
    if val == 'static caravan':
        return 'static_caravan'
    if val == 'station':
        return 'transportation'
    if val == 'storage tank':
        return 'storage_tank'
    if val == 'townhome':
        return 'terrace'


def mz_building_part_kind_detail(val):
    if val in ('yes', 'part', 'church:part', 'default'):
        return None
    if val in (
                'arch',
                'balcony',
                'base',
                'column',
                'door',
                'elevator',
                'entrance',
                'floor',
                'hall',
                'main',
                'passageway',
                'pillar',
                'porch',
                'ramp',
                'roof',
                'room',
                'steps',
                'stilobate',
                'tier',
                'tower',
                'verticalpassage',
                'wall',
                'window'):
        return val
    if val in ('corridor', 'Corridor', 'vertical', 'verticalpassage'):
        return 'verticalpassage'
    if val in ('stairs', 'stairway'):
        return 'steps'


# these functions were used in the yaml, but are worked around at the
# moment by continuing to call the sql and having the output
# calculation simply pick up the sql values
# def mz_get_rel_networks(osm_id):
#     return []
# def mz_cycling_network(props, osm_id):
#     pass


def mz_is_path_major_route_relation(tags):
    "Return True if the relation tags represent a major route relation."

    return (tags.get('type') == 'route' and
            tags.get('route') in ('hiking', 'foot', 'bicycle') and
            tags.get('network') in ('iwn', 'nwn', 'rwn', 'lwn', 'icn', 'ncn',
                                    'rcn', 'lcn'))


PATH_MAJOR_ROUTE = {
    'icn': 8,
    'ncn': 8,
    'iwn': 9,
    'nwn': 9,
    'rcn': 10,
    'rwn': 11,
    'lcn': 11,
    'lwn': 12,
}


def min_not_none(*args):
    "Return the smallest argument which is not None, or None if they all are."

    m = None
    for a in args:
        if m is None or (a is not None and a < m):
            m = a
    return m


def deassoc(x):
    """
    Turns an array consisting of alternating key-value pairs into a
    dictionary.

    Osm2pgsql stores the tags for ways and relations in the planet_osm_ways and
    planet_osm_rels tables in this format. Hstore would make more sense now,
    but this encoding pre-dates the common availability of hstore.

    Example:
    >>> from raw_tiles.index.util import deassoc
    >>> deassoc(['a', 1, 'b', 'B', 'c', 3.14])
    {'a': 1, 'c': 3.14, 'b': 'B'}
    """

    pairs = [iter(x)] * 2
    return dict(izip(*pairs))


# returns the min_zoom for the most important walking or cycling network
# that the road with the given way is part of.
#
# note that relations is a synthetic parameter, added in the Python
# implementation of the min zoom calculation.
def mz_calculate_path_major_route(way_id, relations):
    min_zoom = None

    for rel in relations:
        rel_tags = deassoc(rel['tags'])
        if mz_is_path_major_route_relation(rel_tags):
            network = rel_tags.get('network')
            zoom = PATH_MAJOR_ROUTE.get(network)
            min_zoom = min_not_none(min_zoom, zoom)

    return min_zoom


# calculates the "most important" cycle network for a road with the given tags
# and the feature, or None if the road isn't part of a cycle network.
#
# note that this is a bit of a hack - the SQL implemetnation uses the feature
# ID to look up relations, but for the Python implementation we pass the full
# feature object, which has the relations embedded in it.
#
# cycle networks are considered in the following order of importance: icn,
# ncn, rcn, lcn.
def mz_cycling_network(tags):
    # TODO: implement me! current implementation is a stub.
    return None


def mz_get_min_zoom_highway_level_gate(fid, ways):
    # TODO: implement me!
    return 18


def mz_calculate_ferry_level(shape):
    way_length = shape.length
    if way_length > 1223:
        return 8
    elif way_length > 611:
        return 9
    elif way_length > 306:
        return 10
    elif way_length > 153:
        return 11
    elif way_length > 76:
        return 12
    return 13
