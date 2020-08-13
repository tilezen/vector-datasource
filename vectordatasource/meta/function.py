import re


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
    return dict(zip(*pairs))


# returns the min_zoom for the most important walking or cycling network
# that the road with the given way is part of.
#
# note that relations is a synthetic parameter, added in the Python
# implementation of the min zoom calculation.
def mz_calculate_path_major_route(way_id, relations):
    # would prefer to use None here, and work around so that `min` treats
    # None as bigger than any integer. however, Python treats None the other
    # way, which is a problem if we return None from this function.
    # therefore, this function returns an arbitrarily large zoom, which we
    # should expect we'll never use.
    min_zoom = 999

    for rel in relations:
        rel_tags = deassoc(rel['tags'])
        if mz_is_path_major_route_relation(rel_tags):
            network = rel_tags.get('network')
            zoom = PATH_MAJOR_ROUTE.get(network)
            min_zoom = min(min_zoom, zoom)

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
    min_zoom = 17
    for fid, shape, props in ways:
        highway = props.get('highway')
        if highway in ('motorway', 'trunk', 'primary', 'motorway_link',
                       'trunk_link', 'primary_link'):
            min_zoom = min(min_zoom, 14)

        elif highway in ('secondary', 'tertiary', 'secondary_link',
                         'tertiary_link'):
            min_zoom = min(min_zoom, 15)

        elif highway in ('residential', 'service', 'path', 'track', 'footway',
                         'unclassified'):
            min_zoom = min(min_zoom, 16)

    return min_zoom


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


DECIMAL_UNIT_PATTERN = re.compile(r'([0-9]+(\.[0-9]*)?) *(mi|km|m|nmi|ft)$')
IMPERIAL_PATTERN = re.compile(r'([0-9]+(\.[0-9]*)?)\' *(([0-9]+)")?')
NUMERIC_PATTERN = re.compile(r'^([0-9]+(\.[0-9]*)?)$')


UNIT_CONVERSION_FACTORS = {
    'mi': 1609.3440,
    'km': 1000.0000,
    'm': 1.0,
    'nmi': 1852.0000,
    'ft': 0.3048,
}


def mz_to_float_meters(length):
    # the tag passed through might not exist, in which case this function will
    # receive None. the re.match() functions would raise an error if they were
    # passed None, so instead we return early.
    if length is None:
        return None

    m = DECIMAL_UNIT_PATTERN.search(length)
    if m:
        value = float(m.group(1))
        unit = m.group(3)
        factor = UNIT_CONVERSION_FACTORS[unit]
        return factor * value

    m = IMPERIAL_PATTERN.search(length)
    if m:
        inches = int(m.group(4) or '0')
        feet = float(m.group(1))
        return (feet * 12 + inches) * 0.0254

    # if it's only a number, with no other additional text
    m = NUMERIC_PATTERN.match(length)
    if m:
        return float(m.groups()[0])

    return None


def tz_looks_like_service_area(name):
    min_zoom = 17

    if name is not None:
        name = name.lower()
        if name.endswith('service area') or \
           name.endswith('services') or \
           name.endswith('travel plaza'):
            min_zoom = 13

    return min_zoom


def tz_looks_like_rest_area(name):
    min_zoom = 17

    if name is not None:
        name = name.lower()
        if name.endswith('rest area'):
            min_zoom = 13

    return min_zoom


def tz_estimate_parking_capacity(capacity, parking, levels, way_area):
    try:
        # if the tags tell us what capacity is, then we should respect that.
        capacity = int(capacity)
        return capacity

    except (ValueError, TypeError):
        # sometimes people don't put integers in the capacity, which is kind of
        # annoying. it means we just have to fall back to estimating.
        pass

    # estimate capacity based on way area fitting. looks like roughly 46 square
    # mercator meters per space?
    spaces_per_level = int(way_area / 46.0)

    try:
        levels = int(levels)

    except (ValueError, TypeError):
        # levels either not present, or non-numeric. try and guess from the
        # parking type.
        if parking == 'multi-storey':
            # at least 2, but let's be conservative.
            levels = 2
        else:
            # mainly surface, but also other types such as "underground"
            levels = 1

    capacity = spaces_per_level * levels

    # if we get a silly answer, don't set that - just return None to indicate
    # that we're unsure.
    if capacity > 0:
        return capacity
    else:
        return None
