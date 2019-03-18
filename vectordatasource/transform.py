# -*- encoding: utf-8 -*-
# transformation functions to apply to features

from collections import defaultdict, namedtuple
from math import ceil
from numbers import Number
from shapely.geometry.collection import GeometryCollection
from shapely.geometry import box as Box
from shapely.geometry import LinearRing
from shapely.geometry import LineString
from shapely.geometry import Point
from shapely.geometry import Polygon
from shapely.geometry.multilinestring import MultiLineString
from shapely.geometry.multipoint import MultiPoint
from shapely.geometry.multipolygon import MultiPolygon
from shapely.geometry.polygon import orient
from shapely.ops import linemerge
from shapely.strtree import STRtree
from sort import pois as sort_pois
from StreetNames import short_street_name
from sys import float_info
from tilequeue.process import _make_valid_if_necessary
from tilequeue.process import _visible_shape
from tilequeue.tile import calc_meters_per_pixel_area
from tilequeue.tile import normalize_geometry_type
from tilequeue.tile import tolerance_for_zoom
from tilequeue.transform import calculate_padded_bounds
from util import to_float
from zope.dottedname.resolve import resolve
import csv
import pycountry
import re
import shapely.errors
import shapely.wkb
import shapely.ops
import kdtree


feet_pattern = re.compile('([+-]?[0-9.]+)\'(?: *([+-]?[0-9.]+)")?')
number_pattern = re.compile('([+-]?[0-9.]+)')
# pattern to detect numbers with units.
# PLEASE: keep this in sync with the conversion factors below.
unit_pattern = re.compile('([+-]?[0-9.]+) *(mi|km|m|nmi|ft)')

# multiplicative conversion factor from the unit into meters.
# PLEASE: keep this in sync with the unit_pattern above.
unit_conversion_factor = {
    'mi':  1609.3440,
    'km':  1000.0000,
    'm':      1.0000,
    'nmi': 1852.0000,
    'ft':     0.3048
}

# used to detect if the "name" of a building is
# actually a house number.
digits_pattern = re.compile('^[0-9-]+$')

# used to detect station names which are followed by a
# parenthetical list of line names.
station_pattern = re.compile(r'([^(]*)\(([^)]*)\).*')

# used to detect if an airport's IATA code is the "short"
# 3-character type. there are also longer codes, and ones
# which include numbers, but those seem to be used for
# less important airports.
iata_short_code_pattern = re.compile('^[A-Z]{3}$')


def _to_float_meters(x):
    if x is None:
        return None

    as_float = to_float(x)
    if as_float is not None:
        return as_float

    # trim whitespace to simplify further matching
    x = x.strip()

    # try looking for a unit
    unit_match = unit_pattern.match(x)
    if unit_match is not None:
        value = unit_match.group(1)
        units = unit_match.group(2)
        value_as_float = to_float(value)
        if value_as_float is not None:
            return value_as_float * unit_conversion_factor[units]

    # try if it looks like an expression in feet via ' "
    feet_match = feet_pattern.match(x)
    if feet_match is not None:
        feet = feet_match.group(1)
        inches = feet_match.group(2)
        feet_as_float = to_float(feet)
        inches_as_float = to_float(inches)

        total_inches = 0.0
        parsed_feet_or_inches = False
        if feet_as_float is not None:
            total_inches = feet_as_float * 12.0
            parsed_feet_or_inches = True
        if inches_as_float is not None:
            total_inches += inches_as_float
            parsed_feet_or_inches = True
        if parsed_feet_or_inches:
            # international inch is exactly 25.4mm
            meters = total_inches * 0.0254
            return meters

    # try and match the first number that can be parsed
    for number_match in number_pattern.finditer(x):
        potential_number = number_match.group(1)
        as_float = to_float(potential_number)
        if as_float is not None:
            return as_float

    return None


def _coalesce(properties, *property_names):
    for prop in property_names:
        val = properties.get(prop)
        if val:
            return val
    return None


def _remove_properties(properties, *property_names):
    for prop in property_names:
        properties.pop(prop, None)
    return properties


def _is_name(key):
    """
    Return True if this key looks like a name.

    This isn't as simple as testing if key == 'name', as there are alternative
    name-like tags such as 'official_name', translated names such as 'name:en',
    and left/right names for boundaries. This function aims to match all of
    those variants.
    """

    # simplest and most common case first
    if key == 'name':
        return True

    # translations next
    if key.startswith('name:'):
        return True

    # then any of the alternative forms of name
    return any(key.startswith(p) for p in tag_name_alternates)


def _remove_names(props):
    """
    Remove entries in the props dict for which the key looks like a name.

    Modifies the props dict in-place and also returns it.
    """

    for k in props.keys():
        if _is_name(k):
            props.pop(k)

    return props


def _has_name(props):
    """
    Return true if any of the props look like a name.
    """

    for k in props.keys():
        if _is_name(k):
            return True

    return False


def _building_calc_levels(levels):
    levels = max(levels, 1)
    levels = (levels * 3) + 2
    return levels


def _building_calc_min_levels(min_levels):
    min_levels = max(min_levels, 0)
    min_levels = min_levels * 3
    return min_levels


# slightly bigger than the tallest structure in the world. at the time
# of writing, the Burj Khalifa at 829.8m. this is used as a check to make
# sure that nonsense values (e.g: buildings a million meters tall) don't
# make it into the data.
TALLEST_STRUCTURE_METERS = 1000.0


def _building_calc_height(height_val, levels_val, levels_calc_fn):
    height = _to_float_meters(height_val)
    if height is not None and 0 <= height <= TALLEST_STRUCTURE_METERS:
        return height
    levels = _to_float_meters(levels_val)
    if levels is None:
        return None
    levels = levels_calc_fn(levels)
    if 0 <= levels <= TALLEST_STRUCTURE_METERS:
        return levels
    return None


def add_id_to_properties(shape, properties, fid, zoom):
    properties['id'] = fid
    return shape, properties, fid


def detect_osm_relation(shape, properties, fid, zoom):
    # Assume all negative ids indicate the data was a relation. At the
    # moment, this is true because only osm contains negative
    # identifiers. Should this change, this logic would need to become
    # more robust
    if isinstance(fid, Number) and fid < 0:
        properties['osm_relation'] = True
    return shape, properties, fid


def remove_feature_id(shape, properties, fid, zoom):
    return shape, properties, None


def building_height(shape, properties, fid, zoom):
    height = _building_calc_height(
        properties.get('height'), properties.get('building_levels'),
        _building_calc_levels)
    if height is not None:
        properties['height'] = height
    else:
        properties.pop('height', None)
    return shape, properties, fid


def building_min_height(shape, properties, fid, zoom):
    min_height = _building_calc_height(
        properties.get('min_height'), properties.get('building_min_levels'),
        _building_calc_min_levels)
    if min_height is not None:
        properties['min_height'] = min_height
    else:
        properties.pop('min_height', None)
    return shape, properties, fid


def synthesize_volume(shape, props, fid, zoom):
    area = props.get('area')
    height = props.get('height')
    if area is not None and height is not None:
        props['volume'] = int(area * height)
    return shape, props, fid


def building_trim_properties(shape, properties, fid, zoom):
    properties = _remove_properties(
        properties,
        'building', 'building_part',
        'building_levels', 'building_min_levels')
    return shape, properties, fid


def road_classifier(shape, properties, fid, zoom):
    source = properties.get('source')
    assert source, 'Missing source in road query'
    if source == 'naturalearthdata.com':
        return shape, properties, fid

    properties.pop('is_link', None)
    properties.pop('is_tunnel', None)
    properties.pop('is_bridge', None)

    kind_detail = properties.get('kind_detail', '')
    tunnel = properties.get('tunnel', '')
    bridge = properties.get('bridge', '')

    if kind_detail.endswith('_link'):
        properties['is_link'] = True
    if tunnel in ('yes', 'true'):
        properties['is_tunnel'] = True
    if bridge and bridge != 'no':
        properties['is_bridge'] = True

    return shape, properties, fid


def add_road_network_from_ncat(shape, properties, fid, zoom):
    """
    Many South Korean roads appear to have an "ncat" tag, which seems to
    correspond to the type of road network (perhaps "ncat" = "national
    category"?)

    This filter carries that through into "network", unless it is already
    populated.
    """

    if properties.get('network') is None:
        tags = properties.get('tags', {})
        ncat = _make_unicode_or_none(tags.get('ncat'))

        if ncat == u'국도':
            # national roads - gukdo
            properties['network'] = 'KR:national'

        elif ncat == u'광역시도로':
            # metropolitan city roads - gwangyeoksido
            properties['network'] = 'KR:metropolitan'

        elif ncat == u'특별시도':
            # special city (Seoul) roads - teukbyeolsido
            properties['network'] = 'KR:metropolitan'

        elif ncat == u'고속도로':
            # expressways - gosokdoro
            properties['network'] = 'KR:expressway'

        elif ncat == u'지방도':
            # local highways - jibangdo
            properties['network'] = 'KR:local'

    return shape, properties, fid


def road_trim_properties(shape, properties, fid, zoom):
    properties = _remove_properties(properties, 'bridge', 'tunnel')
    return shape, properties, fid


def _reverse_line_direction(shape):
    if shape.type != 'LineString':
        return False
    shape.coords = shape.coords[::-1]
    return True


def road_oneway(shape, properties, fid, zoom):
    oneway = properties.get('oneway')
    if oneway in ('-1', 'reverse'):
        did_reverse = _reverse_line_direction(shape)
        if did_reverse:
            properties['oneway'] = 'yes'
    elif oneway in ('true', '1'):
        properties['oneway'] = 'yes'
    elif oneway in ('false', '0'):
        properties['oneway'] = 'no'
    return shape, properties, fid


def road_abbreviate_name(shape, properties, fid, zoom):
    name = properties.get('name', None)
    if not name:
        return shape, properties, fid
    short_name = short_street_name(name)
    properties['name'] = short_name
    return shape, properties, fid


def route_name(shape, properties, fid, zoom):
    rn = properties.get('route_name')
    if rn:
        name = properties.get('name')
        if not name:
            properties['name'] = rn
            del properties['route_name']
        elif rn == name:
            del properties['route_name']
    return shape, properties, fid


def place_population_int(shape, properties, fid, zoom):
    population_str = properties.pop('population', None)
    population = to_float(population_str)
    if population is not None:
        properties['population'] = int(population)
    return shape, properties, fid


def population_rank(shape, properties, fid, zoom):
    population = properties.get('population')
    pop_breaks = [
        1000000000,
        100000000,
        50000000,
        20000000,
        10000000,
        5000000,
        1000000,
        500000,
        200000,
        100000,
        50000,
        20000,
        10000,
        5000,
        2000,
        1000,
        200,
        0,
    ]
    for i, pop_break in enumerate(pop_breaks):
        if population >= pop_break:
            rank = len(pop_breaks) - i
            break
    else:
        rank = 0

    properties['population_rank'] = rank
    return (shape, properties, fid)


def pois_capacity_int(shape, properties, fid, zoom):
    pois_capacity_str = properties.pop('capacity', None)
    capacity = to_float(pois_capacity_str)
    if capacity is not None:
        properties['capacity'] = int(capacity)
    return shape, properties, fid


def water_tunnel(shape, properties, fid, zoom):
    tunnel = properties.pop('tunnel', None)
    if tunnel in (None, 'no', 'false', '0'):
        properties.pop('is_tunnel', None)
    else:
        properties['is_tunnel'] = True
    return shape, properties, fid


def admin_level_as_int(shape, properties, fid, zoom):
    admin_level_str = properties.pop('admin_level', None)
    if admin_level_str is None:
        return shape, properties, fid
    try:
        admin_level_int = int(admin_level_str)
    except ValueError:
        return shape, properties, fid
    properties['admin_level'] = admin_level_int
    return shape, properties, fid


def tags_create_dict(shape, properties, fid, zoom):
    tags_hstore = properties.get('tags')
    if tags_hstore:
        tags = dict(tags_hstore)
        properties['tags'] = tags
    return shape, properties, fid


def tags_remove(shape, properties, fid, zoom):
    properties.pop('tags', None)
    return shape, properties, fid


tag_name_alternates = (
    'int_name',
    'loc_name',
    'nat_name',
    'official_name',
    'old_name',
    'reg_name',
    'short_name',
    'name_left',
    'name_right',
    'name:short',
)


def _alpha_2_code_of(lang):
    try:
        alpha_2_code = lang.alpha_2.encode('utf-8')
    except AttributeError:
        return None
    return alpha_2_code


# a structure to return language code lookup results preserving the priority
# (lower is better) of the result for use in situations where multiple inputs
# can map to the same output.
LangResult = namedtuple('LangResult', ['code', 'priority'])


def _convert_wof_l10n_name(x):
    lang_str_iso_639_3 = x[:3]
    if len(lang_str_iso_639_3) != 3:
        return None
    try:
        lang = pycountry.languages.get(alpha_3=lang_str_iso_639_3)
    except KeyError:
        return None
    return LangResult(code=_alpha_2_code_of(lang), priority=0)


def _convert_ne_l10n_name(x):
    if len(x) != 2:
        return None
    try:
        lang = pycountry.languages.get(alpha_2=x)
    except KeyError:
        return None
    return LangResult(code=_alpha_2_code_of(lang), priority=0)


def _normalize_osm_lang_code(x):
    # first try an alpha-2 code
    try:
        lang = pycountry.languages.get(alpha_2=x)
    except KeyError:
        # next, try an alpha-3 code
        try:
            lang = pycountry.languages.get(alpha_3=x)
        except KeyError:
            # finally, try a "bibliographic" code
            try:
                lang = pycountry.languages.get(bibliographic=x)
            except KeyError:
                return None
    return _alpha_2_code_of(lang)


def _normalize_country_code(x):
    x = x.upper()
    try:
        c = pycountry.countries.get(alpha_2=x)
    except KeyError:
        try:
            c = pycountry.countries.get(alpha_3=x)
        except KeyError:
            try:
                c = pycountry.countries.get(numeric=x)
            except KeyError:
                return None
    alpha2_code = c.alpha_2
    return alpha2_code


osm_l10n_lookup = set([
    'zh-min-nan',
    'zh-yue'
])


def _convert_osm_l10n_name(x):
    if x in osm_l10n_lookup:
        return LangResult(code=x, priority=0)

    if '_' not in x:
        lang_code_candidate = x
        country_candidate = None

    else:
        fields_by_underscore = x.split('_', 1)
        lang_code_candidate, country_candidate = fields_by_underscore

    lang_code_result = _normalize_osm_lang_code(lang_code_candidate)
    if lang_code_result is None:
        return None

    priority = 0
    if country_candidate:
        country_result = _normalize_country_code(country_candidate)
        if country_result is None:
            result = lang_code_result
            priority = 1

        else:
            result = '%s_%s' % (lang_code_result, country_result)

    else:
        result = lang_code_result

    return LangResult(code=result, priority=priority)


def tags_name_i18n(shape, properties, fid, zoom):
    tags = properties.get('tags')
    if not tags:
        return shape, properties, fid

    name = properties.get('name')
    if not name:
        return shape, properties, fid

    source = properties.get('source')
    is_wof = source == 'whosonfirst.org'
    is_osm = source == 'openstreetmap.org'
    is_ne = source == 'naturalearthdata.com'

    if is_osm:
        alt_name_prefix_candidates = [
            'name:left:', 'name:right:', 'name:', 'alt_name:', 'old_name:'
        ]
        convert_fn = _convert_osm_l10n_name
    elif is_wof:
        alt_name_prefix_candidates = ['name:']
        convert_fn = _convert_wof_l10n_name

    elif is_ne:
        # replace name_xx with name:xx in tags
        for k in tags.keys():
            if k.startswith('name_'):
                value = tags.pop(k)
                tag_k = k.replace('_', ':')
                tags[tag_k] = value

        alt_name_prefix_candidates = ['name:']
        convert_fn = _convert_ne_l10n_name

    else:
        # conversion function only implemented for things which come from OSM,
        # NE or WOF - implement more cases here when more localized named
        # sources become available.
        return shape, properties, fid

    langs = {}
    for k, v in tags.items():
        for candidate in alt_name_prefix_candidates:

            if k.startswith(candidate):
                lang_code = k[len(candidate):]
                normalized_lang_code = convert_fn(lang_code)

                if normalized_lang_code:
                    code = normalized_lang_code.code
                    priority = normalized_lang_code.priority
                    lang_key = '%s%s' % (candidate, code)

                    if lang_key not in langs or \
                       priority < langs[lang_key][0].priority:
                        langs[lang_key] = (normalized_lang_code, v)

    for lang_key, (lang, v) in langs.items():
        properties[lang_key] = v

    for alt_tag_name_candidate in tag_name_alternates:
        alt_tag_name_value = tags.get(alt_tag_name_candidate)
        if alt_tag_name_value and alt_tag_name_value != name:
            properties[alt_tag_name_candidate] = alt_tag_name_value

    return shape, properties, fid


def _no_none_min(a, b):
    """
    Usually, `min(None, a)` will return None. This isn't
    what we want, so this one will return a non-None
    argument instead. This is basically the same as
    treating None as greater than any other value.
    """

    if a is None:
        return b
    elif b is None:
        return a
    else:
        return min(a, b)


def _sorted_attributes(features, attrs, attribute):
    """
    When the list of attributes is a dictionary, use the
    sort key parameter to order the feature attributes.
    evaluate it as a function and return it. If it's not
    in the right format, attrs isn't a dict then returns
    None.
    """

    sort_key = attrs.get('sort_key')
    reverse = attrs.get('reverse')

    assert sort_key is not None, "Configuration " + \
        "parameter 'sort_key' is missing, please " + \
        "check your configuration."

    # first, we find the _minimum_ ordering over the
    # group of key values. this is because we only do
    # the intersection in groups by the cutting
    # attribute, so can only sort in accordance with
    # that.
    group = dict()
    for feature in features:
        val = feature[1].get(sort_key)
        key = feature[1].get(attribute)
        val = _no_none_min(val, group.get(key))
        group[key] = val

    # extract the sorted list of attributes from the
    # grouped (attribute, order) pairs, ordering by
    # the order.
    all_attrs = sorted(group.iteritems(),
                       key=lambda x: x[1], reverse=bool(reverse))

    # strip out the sort key in return
    return [x[0] for x in all_attrs]


# the table of geometry dimensions indexed by geometry
# type name. it would be better to use geometry type ID,
# but it seems like that isn't exposed.
#
# each of these is a bit-mask, so zero dimentions is
# represented by 1, one by 2, etc... this is to support
# things like geometry collections where the type isn't
# statically known.
_NULL_DIMENSION = 0
_POINT_DIMENSION = 1
_LINE_DIMENSION = 2
_POLYGON_DIMENSION = 4


_GEOMETRY_DIMENSIONS = {
    'Point':              _POINT_DIMENSION,
    'LineString':         _LINE_DIMENSION,
    'LinearRing':         _LINE_DIMENSION,
    'Polygon':            _POLYGON_DIMENSION,
    'MultiPoint':         _POINT_DIMENSION,
    'MultiLineString':    _LINE_DIMENSION,
    'MultiPolygon':       _POLYGON_DIMENSION,
    'GeometryCollection': _NULL_DIMENSION,
}


# returns the dimensionality of the object. so points have
# zero dimensions, lines one, polygons two. multi* variants
# have the same as their singular variant.
#
# geometry collections can hold many different types, so
# we use a bit-mask of the dimensions and recurse down to
# find the actual dimensionality of the stored set.
#
# returns a bit-mask, with these bits ORed together:
#   1: contains a point / zero-dimensional object
#   2: contains a linestring / one-dimensional object
#   4: contains a polygon / two-dimensional object
def _geom_dimensions(g):
    dim = _GEOMETRY_DIMENSIONS.get(g.geom_type)
    assert dim is not None, "Unknown geometry type " + \
        "%s in transform._geom_dimensions." % \
        repr(g.geom_type)

    # recurse for geometry collections to find the true
    # dimensionality of the geometry.
    if dim == _NULL_DIMENSION:
        for part in g.geoms:
            dim = dim | _geom_dimensions(part)

    return dim


def _flatten_geoms(shape):
    """
    Flatten a shape so that it is returned as a list
    of single geometries.

    >>> [g.wkt for g in _flatten_geoms(shapely.wkt.loads('GEOMETRYCOLLECTION (MULTIPOINT(-1 -1, 0 0), GEOMETRYCOLLECTION (POINT(1 1), POINT(2 2), GEOMETRYCOLLECTION (POINT(3 3))), LINESTRING(0 0, 1 1))'))]
    ['POINT (-1 -1)', 'POINT (0 0)', 'POINT (1 1)', 'POINT (2 2)', 'POINT (3 3)', 'LINESTRING (0 0, 1 1)']
    >>> _flatten_geoms(Polygon())
    []
    >>> _flatten_geoms(MultiPolygon())
    []
    """  # noqa
    if shape.geom_type.startswith('Multi'):
        return shape.geoms

    elif shape.is_empty:
        return []

    elif shape.type == 'GeometryCollection':
        geoms = []

        for g in shape.geoms:
            geoms.extend(_flatten_geoms(g))

        return geoms

    else:
        return [shape]


def _filter_geom_types(shape, keep_dim):
    """
    Return a geometry which consists of the geometries in
    the input shape filtered so that only those of the
    given dimension remain. Collapses any structure (e.g:
    of geometry collections) down to a single or multi-
    geometry.

    >>> _filter_geom_types(GeometryCollection(), _POINT_DIMENSION).wkt
    'GEOMETRYCOLLECTION EMPTY'
    >>> _filter_geom_types(Point(0,0), _POINT_DIMENSION).wkt
    'POINT (0 0)'
    >>> _filter_geom_types(Point(0,0), _LINE_DIMENSION).wkt
    'GEOMETRYCOLLECTION EMPTY'
    >>> _filter_geom_types(Point(0,0), _POLYGON_DIMENSION).wkt
    'GEOMETRYCOLLECTION EMPTY'
    >>> _filter_geom_types(LineString([(0,0),(1,1)]), _LINE_DIMENSION).wkt
    'LINESTRING (0 0, 1 1)'
    >>> _filter_geom_types(Polygon([(0,0),(1,1),(1,0),(0,0)],[]), _POLYGON_DIMENSION).wkt
    'POLYGON ((0 0, 1 1, 1 0, 0 0))'
    >>> _filter_geom_types(shapely.wkt.loads('GEOMETRYCOLLECTION (POINT(0 0), LINESTRING(0 0, 1 1))'), _POINT_DIMENSION).wkt
    'POINT (0 0)'
    >>> _filter_geom_types(shapely.wkt.loads('GEOMETRYCOLLECTION (POINT(0 0), LINESTRING(0 0, 1 1))'), _LINE_DIMENSION).wkt
    'LINESTRING (0 0, 1 1)'
    >>> _filter_geom_types(shapely.wkt.loads('GEOMETRYCOLLECTION (POINT(0 0), LINESTRING(0 0, 1 1))'), _POLYGON_DIMENSION).wkt
    'GEOMETRYCOLLECTION EMPTY'
    >>> _filter_geom_types(shapely.wkt.loads('GEOMETRYCOLLECTION (POINT(0 0), GEOMETRYCOLLECTION (POINT(1 1), LINESTRING(0 0, 1 1)))'), _POINT_DIMENSION).wkt
    'MULTIPOINT (0 0, 1 1)'
    >>> _filter_geom_types(shapely.wkt.loads('GEOMETRYCOLLECTION (MULTIPOINT(-1 -1, 0 0), GEOMETRYCOLLECTION (POINT(1 1), POINT(2 2), GEOMETRYCOLLECTION (POINT(3 3))), LINESTRING(0 0, 1 1))'), _POINT_DIMENSION).wkt
    'MULTIPOINT (-1 -1, 0 0, 1 1, 2 2, 3 3)'
    >>> _filter_geom_types(shapely.wkt.loads('GEOMETRYCOLLECTION (LINESTRING(-1 -1, 0 0), GEOMETRYCOLLECTION (LINESTRING(1 1, 2 2), GEOMETRYCOLLECTION (POINT(3 3))), LINESTRING(0 0, 1 1))'), _LINE_DIMENSION).wkt
    'MULTILINESTRING ((-1 -1, 0 0), (1 1, 2 2), (0 0, 1 1))'
    >>> _filter_geom_types(shapely.wkt.loads('GEOMETRYCOLLECTION (POLYGON((-2 -2, -2 2, 2 2, 2 -2, -2 -2)), GEOMETRYCOLLECTION (LINESTRING(1 1, 2 2), GEOMETRYCOLLECTION (POLYGON((3 3, 0 0, 1 0, 3 3)))), LINESTRING(0 0, 1 1))'), _POLYGON_DIMENSION).wkt
    'MULTIPOLYGON (((-2 -2, -2 2, 2 2, 2 -2, -2 -2)), ((3 3, 0 0, 1 0, 3 3)))'
    """  # noqa

    # flatten the geometries, and keep the parts with the
    # dimension that we want. each item in the parts list
    # should be a single (non-multi) geometry.
    parts = []
    for g in _flatten_geoms(shape):
        if _geom_dimensions(g) == keep_dim:
            parts.append(g)

    # figure out how to construct a multi-geometry of the
    # dimension wanted.
    if keep_dim == _POINT_DIMENSION:
        constructor = MultiPoint

    elif keep_dim == _LINE_DIMENSION:
        constructor = MultiLineString

    elif keep_dim == _POLYGON_DIMENSION:
        constructor = MultiPolygon

    else:
        raise ValueError('Unknown dimension %d in _filter_geom_types'
                         % keep_dim)

    if len(parts) == 0:
        return constructor()

    elif len(parts) == 1:
        # return the singular geometry
        return parts[0]

    else:
        if keep_dim == _POINT_DIMENSION:
            # not sure why the MultiPoint constructor wants
            # its coordinates differently from MultiPolygon
            # and MultiLineString...
            coords = []
            for p in parts:
                coords.extend(p.coords)
            return MultiPoint(coords)

        else:
            return constructor(parts)


# creates a list of indexes, each one for a different cut
# attribute value, in priority order.
#
# STRtree stores geometries and returns these from the query,
# but doesn't appear to allow any other attributes to be
# stored along with the geometries. this means we have to
# separate the index out into several "layers", each having
# the same attribute value. which isn't all that much of a
# pain, as we need to cut the shapes in a certain order to
# ensure priority anyway.
#
# intersect_func is a functor passed in to control how an
# intersection is performed. it is passed
class _Cutter:
    def __init__(self, features, attrs, attribute,
                 target_attribute, keep_geom_type,
                 intersect_func):
        group = defaultdict(list)
        for feature in features:
            shape, props, fid = feature
            attr = props.get(attribute)
            group[attr].append(shape)

        # if the user didn't supply any options for controlling
        # the cutting priority, then just make some up based on
        # the attributes which are present in the dataset.
        if attrs is None:
            all_attrs = set()
            for feature in features:
                all_attrs.add(feature[1].get(attribute))
            attrs = list(all_attrs)

        # alternatively, the user can specify an ordering
        # function over the attributes.
        elif isinstance(attrs, dict):
            attrs = _sorted_attributes(features, attrs,
                                       attribute)

        cut_idxs = list()
        for attr in attrs:
            if attr in group:
                cut_idxs.append((attr, STRtree(group[attr])))

        self.attribute = attribute
        self.target_attribute = target_attribute
        self.cut_idxs = cut_idxs
        self.keep_geom_type = keep_geom_type
        self.intersect_func = intersect_func
        self.new_features = []

    # cut up the argument shape, projecting the configured
    # attribute to the properties of the intersecting parts
    # of the shape. adds all the selected bits to the
    # new_features list.
    def cut(self, shape, props, fid):
        original_geom_dim = _geom_dimensions(shape)

        for cutting_attr, cut_idx in self.cut_idxs:
            cutting_shapes = cut_idx.query(shape)

            for cutting_shape in cutting_shapes:
                if cutting_shape.intersects(shape):
                    shape = self._intersect(
                        shape, props, fid, cutting_shape,
                        cutting_attr, original_geom_dim)

                # if there's no geometry left outside the
                # shape, then we can exit the function
                # early, as nothing else will intersect.
                if shape.is_empty:
                    return

        # if there's still geometry left outside, then it
        # keeps the old, unaltered properties.
        self._add(shape, props, fid, original_geom_dim)

    # only keep geometries where either the type is the
    # same as the original, or we're not trying to keep the
    # same type.
    def _add(self, shape, props, fid, original_geom_dim):
        # if keeping the same geometry type, then filter
        # out anything that's different.
        if self.keep_geom_type:
            shape = _filter_geom_types(
                shape, original_geom_dim)

        # don't add empty shapes, they're completely
        # useless. the previous step may also have created
        # an empty geometry if there weren't any items of
        # the type we're looking for.
        if shape.is_empty:
            return

        # add the shape as-is unless we're trying to keep
        # the geometry type or the geometry dimension is
        # identical.
        self.new_features.append((shape, props, fid))

    # intersects the shape with the cutting shape and
    # handles attribute projection. anything "inside" is
    # kept as it must have intersected the highest
    # priority cutting shape already. the remainder is
    # returned.
    def _intersect(self, shape, props, fid, cutting_shape,
                   cutting_attr, original_geom_dim):
        inside, outside = \
            self.intersect_func(shape, cutting_shape)

        # intersections are tricky, and it seems that the geos
        # library (perhaps only certain versions of it) don't
        # handle intersection of a polygon with its boundary
        # very well. for example:
        #
        # >>> import shapely.geometry as g
        # >>> p = g.Point(0,0).buffer(1.0, resolution=2)
        # >>> b = p.boundary
        # >>> b.intersection(p).wkt
        # 'MULTILINESTRING ((1 0, 0.7071067811865481 -0.7071067811865469), (0.7071067811865481 -0.7071067811865469, 1.615544574432587e-15 -1), (1.615544574432587e-15 -1, -0.7071067811865459 -0.7071067811865491), (-0.7071067811865459 -0.7071067811865491, -1 -3.231089148865173e-15), (-1 -3.231089148865173e-15, -0.7071067811865505 0.7071067811865446), (-0.7071067811865505 0.7071067811865446, -4.624589118372729e-15 1), (-4.624589118372729e-15 1, 0.7071067811865436 0.7071067811865515), (0.7071067811865436 0.7071067811865515, 1 0))'  # noqa
        #
        # the result multilinestring could be joined back into
        # the original object. but because it has separate parts,
        # each requires duplicating the start and end point, and
        # each separate segment gets a different polygon buffer
        # in Tangram - basically, it's a problem all round.
        #
        # two solutions to this: given that we're cutting, then
        # the inside and outside should union back to the
        # original shape - if either is empty then the whole
        # object ought to be in the other.
        #
        # the second solution, for when there is actually some
        # part cut, is that we can attempt to merge lines back
        # together.
        if outside.is_empty and not inside.is_empty:
            inside = shape
        elif inside.is_empty and not outside.is_empty:
            outside = shape
        elif original_geom_dim == _LINE_DIMENSION:
            inside = _linemerge(inside)
            outside = _linemerge(outside)

        if cutting_attr is not None:
            inside_props = props.copy()
            inside_props[self.target_attribute] = cutting_attr
        else:
            inside_props = props

        self._add(inside, inside_props, fid,
                  original_geom_dim)
        return outside


def _intersect_cut(shape, cutting_shape):
    """
    intersect by cutting, so that the cutting shape defines
    a part of the shape which is inside and a part which is
    outside as two separate shapes.
    """
    inside = shape.intersection(cutting_shape)
    outside = shape.difference(cutting_shape)
    return inside, outside


# intersect by looking at the overlap size. we can define
# a cut-off fraction and if that fraction or more of the
# area of the shape is within the cutting shape, it's
# inside, else outside.
#
# this is done using a closure so that we can curry away
# the fraction parameter.
def _intersect_overlap(min_fraction):
    # the inner function is what will actually get
    # called, but closing over min_fraction means it
    # will have access to that.
    def _f(shape, cutting_shape):
        overlap = shape.intersection(cutting_shape).area
        area = shape.area

        # need an empty shape of the same type as the
        # original shape, which should be possible, as
        # it seems shapely geometries all have a default
        # constructor to empty.
        empty = type(shape)()

        if ((area > 0) and (overlap / area) >= min_fraction):
            return shape, empty
        else:
            return empty, shape
    return _f


# intersect by looking at the overlap length. if more than a minimum fraction
# of the shape's length is within the cutting area, then we will consider it
# totally "cut".
def _intersect_linear_overlap(min_fraction):
    # the inner function is what will actually get
    # called, but closing over min_fraction means it
    # will have access to that.
    def _f(shape, cutting_shape):
        overlap = shape.intersection(cutting_shape).length
        total = shape.length
        empty = type(shape)()

        if ((total > 0) and (overlap / total) >= min_fraction):
            return shape, empty
        else:
            return empty, shape
    return _f


# find a layer by iterating through all the layers. this
# would be easier if they layers were in a dict(), but
# that's a pretty invasive change.
#
# returns None if the layer can't be found.
def _find_layer(feature_layers, name):

    for feature_layer in feature_layers:
        layer_datum = feature_layer['layer_datum']
        layer_name = layer_datum['name']

        if layer_name == name:
            return feature_layer

    return None


# shared implementation of the intercut algorithm, used both when cutting
# shapes and using overlap to determine inside / outsideness.
#
# the filter_fn are used to filter which features from the base layer are cut
# with which features from the cutting layer. cutting layer features which do
# not match the filter are ignored, base layer features are left in the layer
# unchanged.
def _intercut_impl(intersect_func, feature_layers, base_layer, cutting_layer,
                   attribute, target_attribute, cutting_attrs, keep_geom_type,
                   cutting_filter_fn=None, base_filter_fn=None):
    # the target attribute can default to the attribute if
    # they are distinct. but often they aren't, and that's
    # why target_attribute is a separate parameter.
    if target_attribute is None:
        target_attribute = attribute

    # search through all the layers and extract the ones
    # which have the names of the base and cutting layer.
    # it would seem to be better to use a dict() for
    # layers, and this will give odd results if names are
    # allowed to be duplicated.
    base = _find_layer(feature_layers, base_layer)
    cutting = _find_layer(feature_layers, cutting_layer)

    # base or cutting layer not available. this could happen
    # because of a config problem, in which case you'd want
    # it to be reported. but also can happen when the client
    # selects a subset of layers which don't include either
    # the base or the cutting layer. then it's not an error.
    # the interesting case is when they select the base but
    # not the cutting layer...
    if base is None or cutting is None:
        return None

    base_features = base['features']
    cutting_features = cutting['features']

    # filter out any features that we don't want to cut with
    if cutting_filter_fn is not None:
        cutting_features = filter(cutting_filter_fn, cutting_features)

    # short-cut return if there are no cutting features => there's nothing
    # to do.
    if not cutting_features:
        return base

    # make a cutter object to help out
    cutter = _Cutter(cutting_features, cutting_attrs,
                     attribute, target_attribute,
                     keep_geom_type, intersect_func)

    skipped_features = []
    for base_feature in base_features:
        if base_filter_fn is None or base_filter_fn(base_feature):
            # we use shape to track the current remainder of the
            # shape after subtracting bits which are inside cuts.
            shape, props, fid = base_feature

            cutter.cut(shape, props, fid)

        else:
            skipped_features.append(base_feature)

    base['features'] = cutter.new_features + skipped_features

    return base


class Where(object):
    """
    A "where" clause for filtering features based on their properties.

    This is commonly used in post-processing steps to configure which features
    in the layer we want to operate on, allowing us to write simple Python
    expressions in the YAML.
    """

    def __init__(self, where):
        self.fn = compile(where, 'queries.yaml', 'eval')

    def __call__(self, feature):
        shape, props, fid = feature
        local = defaultdict(lambda: None)
        local.update(props)
        return eval(self.fn, {}, local)


# intercut takes features from a base layer and cuts each
# of them against a cutting layer, splitting any base
# feature which intersects into separate inside and outside
# parts.
#
# the parts of each base feature which are outside any
# cutting feature are left unchanged. the parts which are
# inside have their property with the key given by the
# 'target_attribute' parameter set to the same value as the
# property from the cutting feature with the key given by
# the 'attribute' parameter.
#
# the intended use of this is to project attributes from one
# layer to another so that they can be styled appropriately.
#
# - feature_layers: list of layers containing both the base
#     and cutting layer.
# - base_layer: str name of the base layer.
# - cutting_layer: str name of the cutting layer.
# - attribute: optional str name of the property / attribute
#     to take from the cutting layer.
# - target_attribute: optional str name of the property /
#     attribute to assign on the base layer. defaults to the
#     same as the 'attribute' parameter.
# - cutting_attrs: list of str, the priority of the values
#     to be used in the cutting operation. this ensures that
#     items at the beginning of the list get cut first and
#     those values have priority (won't be overridden by any
#     other shape cutting).
# - keep_geom_type: if truthy, then filter the output to be
#     the same type as the input. defaults to True, because
#     this seems like an eminently sensible behaviour.
# - base_where: if truthy, a Python expression which is
#     evaluated in the context of a feature's properties and
#     can return True if the feature is to be cut and False
#     if it should be passed through unmodified.
# - cutting_where: if truthy, a Python expression which is
#     evaluated in the context of a feature's properties and
#     can return True if the feature is to be used for cutting
#     and False if it should be ignored.
#
# returns a feature layer which is the base layer cut by the
# cutting layer.
def intercut(ctx):

    feature_layers = ctx.feature_layers
    base_layer = ctx.params.get('base_layer')
    assert base_layer, \
        'Parameter base_layer was missing from intercut config'
    cutting_layer = ctx.params.get('cutting_layer')
    assert cutting_layer, \
        'Parameter cutting_layer was missing from intercut ' \
        'config'
    attribute = ctx.params.get('attribute')
    # sanity check on the availability of the cutting
    # attribute.
    assert attribute is not None, \
        'Parameter attribute to intercut was None, but ' + \
        'should have been an attribute name. Perhaps check ' + \
        'your configuration file and queries.'

    target_attribute = ctx.params.get('target_attribute')
    cutting_attrs = ctx.params.get('cutting_attrs')
    keep_geom_type = ctx.params.get('keep_geom_type', True)
    base_where = ctx.params.get('base_where')
    cutting_where = ctx.params.get('cutting_where')

    # compile the where-clauses, if any were configured
    if base_where:
        base_where = Where(base_where)
    if cutting_where:
        cutting_where = Where(cutting_where)

    return _intercut_impl(
        _intersect_cut, feature_layers, base_layer, cutting_layer,
        attribute, target_attribute, cutting_attrs, keep_geom_type,
        base_filter_fn=base_where, cutting_filter_fn=cutting_where)


# overlap measures the area overlap between each feature in
# the base layer and each in the cutting layer. if the
# fraction of overlap is greater than the min_fraction
# constant, then the feature in the base layer is assigned
# a property with its value derived from the overlapping
# feature from the cutting layer.
#
# the intended use of this is to project attributes from one
# layer to another so that they can be styled appropriately.
#
# it has the same parameters as intercut, see above.
#
# returns a feature layer which is the base layer with
# overlapping features having attributes projected from the
# cutting layer.
def overlap(ctx):

    feature_layers = ctx.feature_layers
    base_layer = ctx.params.get('base_layer')
    assert base_layer, \
        'Parameter base_layer was missing from overlap config'
    cutting_layer = ctx.params.get('cutting_layer')
    assert cutting_layer, \
        'Parameter cutting_layer was missing from overlap ' \
        'config'
    attribute = ctx.params.get('attribute')
    # sanity check on the availability of the cutting
    # attribute.
    assert attribute is not None, \
        'Parameter attribute to overlap was None, but ' + \
        'should have been an attribute name. Perhaps check ' + \
        'your configuration file and queries.'

    target_attribute = ctx.params.get('target_attribute')
    cutting_attrs = ctx.params.get('cutting_attrs')
    keep_geom_type = ctx.params.get('keep_geom_type', True)
    min_fraction = ctx.params.get('min_fraction', 0.8)
    base_where = ctx.params.get('base_where')
    cutting_where = ctx.params.get('cutting_where')

    # use a different function for linear overlaps (i.e: roads with polygons)
    # than area overlaps. keeping this explicit (rather than relying on the
    # geometry type) means we don't end up with unexpected lines in a polygonal
    # layer.
    linear = ctx.params.get('linear', False)
    if linear:
        overlap_fn = _intersect_linear_overlap(min_fraction)
    else:
        overlap_fn = _intersect_overlap(min_fraction)

    # compile the where-clauses, if any were configured
    if base_where:
        base_where = Where(base_where)
    if cutting_where:
        cutting_where = Where(cutting_where)

    return _intercut_impl(
        overlap_fn, feature_layers, base_layer,
        cutting_layer, attribute, target_attribute, cutting_attrs,
        keep_geom_type, cutting_filter_fn=cutting_where,
        base_filter_fn=base_where)


# intracut cuts a layer with a set of features from that same
# layer, which are then removed.
#
# for example, with water boundaries we get one set of linestrings
# from the admin polygons and another set from the original ways
# where the `maritime=yes` tag is set. we don't actually want
# separate linestrings, we just want the `maritime=yes` attribute
# on the first set of linestrings.
def intracut(ctx):

    feature_layers = ctx.feature_layers
    base_layer = ctx.params.get('base_layer')
    assert base_layer, \
        'Parameter base_layer was missing from intracut config'
    attribute = ctx.params.get('attribute')
    # sanity check on the availability of the cutting
    # attribute.
    assert attribute is not None, \
        'Parameter attribute to intracut was None, but ' + \
        'should have been an attribute name. Perhaps check ' + \
        'your configuration file and queries.'

    base = _find_layer(feature_layers, base_layer)
    if base is None:
        return None

    # unlike intracut & overlap, which work on separate layers,
    # intracut separates features in the same layer into
    # different sets to work on.
    base_features = list()
    cutting_features = list()
    for shape, props, fid in base['features']:
        if attribute in props:
            cutting_features.append((shape, props, fid))
        else:
            base_features.append((shape, props, fid))

    cutter = _Cutter(cutting_features, None, attribute,
                     attribute, True, _intersect_cut)

    for shape, props, fid in base_features:
        cutter.cut(shape, props, fid)

    base['features'] = cutter.new_features

    return base


# place kinds, as used by OSM, mapped to their rough
# min_zoom so that we can provide a defaulted,
# non-curated min_zoom value.
_default_min_zoom_for_place_kind = {
    'locality': 13,
    'isolated_dwelling': 13,
    'farm': 13,

    'hamlet': 12,

    'village': 11,

    'suburb': 10,
    'quarter': 10,
    'borough': 10,

    'town': 8,
    'city': 8,

    'province': 4,
    'state': 4,

    'sea': 3,

    'country': 0,
    'ocean': 0,
    'continent': 0
}


# if the feature does not have a min_zoom attribute already,
# which would have come from a curated source, then calculate
# a default one based on the kind of place it is.
def calculate_default_place_min_zoom(shape, properties, fid, zoom):
    min_zoom = properties.get('min_zoom')
    if min_zoom is not None:
        return shape, properties, fid

    # base calculation off kind
    kind = properties.get('kind')
    if kind is None:
        return shape, properties, fid

    min_zoom = _default_min_zoom_for_place_kind.get(kind)
    if min_zoom is None:
        return shape, properties, fid

    # adjust min_zoom for state / country capitals
    if kind in ('city', 'town'):
        if properties.get('region_capital'):
            min_zoom -= 1
        elif properties.get('country_capital'):
            min_zoom -= 2

    properties['min_zoom'] = min_zoom

    return shape, properties, fid


def _make_new_properties(props, props_instructions):
    """
    make new properties from existing properties and a
    dict of instructions.

    the algorithm is:
      - where a key appears with value True, it will be
        copied from the existing properties.
      - where it's a dict, the values will be looked up
        in that dict.
      - otherwise the value will be used directly.
    """
    new_props = dict()

    for k, v in props_instructions.iteritems():
        if v is True:
            # this works even when props[k] = None
            if k in props:
                new_props[k] = props[k]
        elif isinstance(v, dict):
            # this will return None, which allows us to
            # use the dict to set default values.
            original_v = props.get(k)
            if original_v in v:
                new_props[k] = v[original_v]
        elif isinstance(v, list) and len(v) == 1:
            # this is a hack to implement escaping for when the output value
            # should be a value, but that value (e.g: True, or a dict) is
            # used for some other purpose above.
            new_props[k] = v[0]
        else:
            new_props[k] = v

    return new_props


def _snap_to_grid(shape, grid_size):
    """
    Snap coordinates of a shape to a multiple of `grid_size`.

    This can be useful when there's some error in point
    positions, but we're using an algorithm which is very
    sensitive to coordinate exactness. For example, when
    calculating the boundary of several items, it makes a
    big difference whether the shapes touch or there's a
    very small gap between them.

    This is implemented here because it doesn't exist in
    GEOS or Shapely. It exists in PostGIS, but only because
    it's implemented there as well. Seems like it would be a
    useful thing to have in GEOS, though.

    >>> _snap_to_grid(Point(0.5, 0.5), 1).wkt
    'POINT (1 1)'
    >>> _snap_to_grid(Point(0.1, 0.1), 1).wkt
    'POINT (0 0)'
    >>> _snap_to_grid(Point(-0.1, -0.1), 1).wkt
    'POINT (-0 -0)'
    >>> _snap_to_grid(LineString([(1.1,1.1),(1.9,0.9)]), 1).wkt
    'LINESTRING (1 1, 2 1)'
    _snap_to_grid(Polygon([(0.1,0.1),(3.1,0.1),(3.1,3.1),(0.1,3.1),(0.1,0.1)],[[(1.1,0.9),(1.1,1.9),(2.1,1.9),(2.1,0.9),(1.1,0.9)]]), 1).wkt
    'POLYGON ((0 0, 3 0, 3 3, 0 3, 0 0), (1 1, 1 2, 2 2, 2 1, 1 1))'
    >>> _snap_to_grid(MultiPoint([Point(0.1, 0.1), Point(0.9, 0.9)]), 1).wkt
    'MULTIPOINT (0 0, 1 1)'
    >>> _snap_to_grid(MultiLineString([LineString([(0.1, 0.1), (0.9, 0.9)]), LineString([(0.9, 0.1),(0.1,0.9)])]), 1).wkt
    'MULTILINESTRING ((0 0, 1 1), (1 0, 0 1))'
    """  # noqa

    # snap a single coordinate value
    def _snap(c):
        return grid_size * round(c / grid_size, 0)

    # snap all coordinate pairs in something iterable
    def _snap_coords(c):
        return [(_snap(x), _snap(y)) for x, y in c]

    # recursively snap all coordinates in an iterable over
    # geometries.
    def _snap_multi(geoms):
        return [_snap_to_grid(g, grid_size) for g in geoms]

    shape_type = shape.geom_type
    if shape.is_empty or shape_type == 'GeometryCollection':
        return None

    elif shape_type == 'Point':
        return Point(_snap(shape.x), _snap(shape.y))

    elif shape_type == 'LineString':
        return LineString(_snap_coords(shape.coords))

    elif shape_type == 'Polygon':
        exterior = LinearRing(_snap_coords(shape.exterior.coords))
        interiors = []
        for interior in shape.interiors:
            interiors.append(LinearRing(_snap_coords(interior.coords)))
        return Polygon(exterior, interiors)

    elif shape_type == 'MultiPoint':
        return MultiPoint(_snap_multi(shape.geoms))

    elif shape_type == 'MultiLineString':
        return MultiLineString(_snap_multi(shape.geoms))

    elif shape_type == 'MultiPolygon':
        return MultiPolygon(_snap_multi(shape.geoms))

    else:
        raise ValueError('_snap_to_grid: unimplemented for shape type %s'
                         % repr(shape_type))


def exterior_boundaries(ctx):
    """
    create new fetures from the boundaries of polygons
    in the base layer, subtracting any sections of the
    boundary which intersect other polygons. this is
    added as a new layer if new_layer_name is not None
    otherwise appended to the base layer.

    the purpose of this is to provide us a shoreline /
    river bank layer from the water layer without having
    any of the shoreline / river bank draw over the top
    of any of the base polygons.

    properties on the lines returned are copied / adapted
    from the existing layer using the new_props dict. see
    _make_new_properties above for the rules.

    buffer_size determines whether any buffering will be
    done to the index polygons. a judiciously small
    amount of buffering can help avoid "dashing" due to
    tolerance in the intersection, but will also create
    small overlaps between lines.

    any features in feature_layers[layer] which aren't
    polygons will be ignored.

    note that the `bounds` kwarg should be filled out
    automatically by tilequeue - it does not have to be
    provided from the config.
    """

    feature_layers = ctx.feature_layers
    zoom = ctx.nominal_zoom
    base_layer = ctx.params.get('base_layer')
    assert base_layer, 'Missing base_layer parameter'
    new_layer_name = ctx.params.get('new_layer_name')
    prop_transform = ctx.params.get('prop_transform')
    buffer_size = ctx.params.get('buffer_size')
    start_zoom = ctx.params.get('start_zoom', 0)
    snap_tolerance = ctx.params.get('snap_tolerance')

    layer = None

    # don't start processing until the start zoom
    if zoom < start_zoom:
        return layer

    # search through all the layers and extract the one
    # which has the name of the base layer we were given
    # as a parameter.
    layer = _find_layer(feature_layers, base_layer)

    # if we failed to find the base layer then it's
    # possible the user just didn't ask for it, so return
    # an empty result.
    if layer is None:
        return None

    if prop_transform is None:
        prop_transform = {}

    features = layer['features']

    # this exists to enable a dirty hack to try and work
    # around duplicate geometries in the database. this
    # happens when a multipolygon relation can't
    # supersede a member way because the way contains tags
    # which aren't present on the relation. working around
    # this by calling "union" on geometries proved to be
    # too expensive (~3x current), so this hack looks at
    # the way_area of each object, and uses that as a
    # proxy for identity. it's not perfect, but the chance
    # that there are two overlapping polygons of exactly
    # the same size must be pretty small. however, the
    # STRTree we're using as a spatial index doesn't
    # directly support setting attributes on the indexed
    # geometries, so this class exists to carry the area
    # attribute through the index to the point where we
    # want to use it.
    class geom_with_area:
        def __init__(self, geom, area):
            self.geom = geom
            self.area = area
            self._geom = geom._geom
            # STRtree started filtering out empty geoms at some version, so
            # we need to proxy the is_empty property.
            self.is_empty = geom.is_empty

    # create an index so that we can efficiently find the
    # polygons intersecting the 'current' one. Note that
    # we're only interested in intersecting with other
    # polygonal features, and that intersecting with lines
    # can give some unexpected results.
    indexable_features = list()
    indexable_shapes = list()
    for shape, props, fid in features:
        if shape.type in ('Polygon', 'MultiPolygon'):

            # the data comes back clipped from the queries now so we
            # no longer need to clip here

            snapped = shape
            if snap_tolerance is not None:
                snapped = _snap_to_grid(shape, snap_tolerance)

            # geometry collections are returned as None
            if snapped is None:
                continue

            # snapping coordinates and clipping shapes might make the shape
            # invalid, so we need a way to clean them. one simple, but not
            # foolproof, way is to buffer them by 0.
            if not snapped.is_valid:
                snapped = snapped.buffer(0)

            # that still might not have done the trick, so drop any polygons
            # which are still invalid so as not to cause errors later.
            if not snapped.is_valid:
                # TODO: log this as a warning!
                continue

            # skip any geometries that may have become empty
            if snapped.is_empty:
                continue

            indexable_features.append((snapped, props, fid))
            indexable_shapes.append(geom_with_area(snapped, props.get('area')))

    index = STRtree(indexable_shapes)

    new_features = list()
    # loop through all the polygons, taking the boundary
    # of each and subtracting any parts which are within
    # other polygons. what remains (if anything) is the
    # new feature.
    for feature in indexable_features:
        shape, props, fid = feature

        boundary = shape.boundary
        cutting_shapes = index.query(boundary)

        for cutting_item in cutting_shapes:
            cutting_shape = cutting_item.geom
            cutting_area = cutting_item.area

            # dirty hack: this object is probably a
            # superseded way if the ID is positive and
            # the area is the same as the cutting area.
            # using the ID check here prevents the
            # boundary from being duplicated.
            is_superseded_way = \
                cutting_area == props.get('area') and \
                props.get('id') > 0

            if cutting_shape is not shape and \
               not is_superseded_way:
                buf = cutting_shape

                if buffer_size is not None:
                    buf = buf.buffer(buffer_size)

                boundary = boundary.difference(buf)

        # filter only linestring-like objects. we don't
        # want any points which might have been created
        # by the intersection.
        boundary = _filter_geom_types(boundary, _LINE_DIMENSION)

        if not boundary.is_empty:
            new_props = _make_new_properties(props, prop_transform)
            new_features.append((boundary, new_props, fid))

    if new_layer_name is None:
        # no new layer requested, instead add new
        # features into the same layer.
        layer['features'].extend(new_features)

        return layer

    else:
        # make a copy of the old layer's information - it
        # shouldn't matter about most of the settings, as
        # post-processing is one of the last operations.
        # but we need to override the name to ensure we get
        # some output.
        new_layer_datum = layer['layer_datum'].copy()
        new_layer_datum['name'] = new_layer_name
        new_layer = layer.copy()
        new_layer['layer_datum'] = new_layer_datum
        new_layer['features'] = new_features
        new_layer['name'] = new_layer_name

        return new_layer


def _inject_key(key, infix):
    """
    OSM keys often have several parts, separated by ':'s.
    When we merge properties from the left and right of a
    boundary, we want to preserve information like the
    left and right names, but prefer the form "name:left"
    rather than "left:name", so we have to insert an
    infix string to these ':'-delimited arrays.

    >>> _inject_key('a:b:c', 'x')
    'a:x:b:c'
    >>> _inject_key('a', 'x')
    'a:x'

    """
    parts = key.split(':')
    parts.insert(1, infix)
    return ':'.join(parts)


def _merge_left_right_props(lprops, rprops):
    """
    Given a set of properties to the left and right of a
    boundary, we want to keep as many of these as possible,
    but keeping them all might be a bit too much.

    So we want to keep the key-value pairs which are the
    same in both in the output, but merge the ones which
    are different by infixing them with 'left' and 'right'.

    >>> _merge_left_right_props({}, {})
    {}
    >>> _merge_left_right_props({'a':1}, {})
    {'a:left': 1}
    >>> _merge_left_right_props({}, {'b':2})
    {'b:right': 2}
    >>> _merge_left_right_props({'a':1, 'c':3}, {'b':2, 'c':3})
    {'a:left': 1, 'c': 3, 'b:right': 2}
    >>> _merge_left_right_props({'a':1},{'a':2})
    {'a:left': 1, 'a:right': 2}
    """
    keys = set(lprops.keys()) | set(rprops.keys())
    new_props = dict()

    # props in both are copied directly if they're the same
    # in both the left and right. they get left/right
    # inserted after the first ':' if they're different.
    for k in keys:
        lv = lprops.get(k)
        rv = rprops.get(k)

        if lv == rv:
            new_props[k] = lv
        else:
            if lv is not None:
                new_props[_inject_key(k, 'left')] = lv
            if rv is not None:
                new_props[_inject_key(k, 'right')] = rv

    return new_props


def _make_joined_name(props):
    """
    Updates the argument to contain a 'name' element
    generated from joining the left and right names.

    Just to make it easier for people, we generate a name
    which is easy to display of the form "LEFT - RIGHT".
    The individual properties are available if the user
    wants to generate a more complex name.

    >>> x = {}
    >>> _make_joined_name(x)
    >>> x
    {}

    >>> x = {'name:left':'Left'}
    >>> _make_joined_name(x)
    >>> x
    {'name': 'Left', 'name:left': 'Left'}

    >>> x = {'name:right':'Right'}
    >>> _make_joined_name(x)
    >>> x
    {'name': 'Right', 'name:right': 'Right'}

    >>> x = {'name:left':'Left', 'name:right':'Right'}
    >>> _make_joined_name(x)
    >>> x
    {'name:right': 'Right', 'name': 'Left - Right', 'name:left': 'Left'}

    >>> x = {'name:left':'Left', 'name:right':'Right', 'name': 'Already Exists'}
    >>> _make_joined_name(x)
    >>> x
    {'name:right': 'Right', 'name': 'Already Exists', 'name:left': 'Left'}
    """  # noqa

    # don't overwrite an existing name
    if 'name' in props:
        return

    lname = props.get('name:left')
    rname = props.get('name:right')

    if lname is not None:
        if rname is not None:
            props['name'] = "%s - %s" % (lname, rname)
        else:
            props['name'] = lname
    elif rname is not None:
        props['name'] = rname


def _linemerge(geom):
    """
    Try to extract all the linear features from the geometry argument
    and merge them all together into the smallest set of linestrings
    possible.

    This is almost identical to Shapely's linemerge, and uses it,
    except that Shapely's throws exceptions when passed a single
    linestring, or a geometry collection with lines and points in it.
    So this can be thought of as a "safer" wrapper around Shapely's
    function.
    """
    geom_type = geom.type
    result_geom = None

    if geom_type == 'GeometryCollection':
        # collect together everything line-like from the geometry
        # collection and filter out anything that's empty
        lines = []
        for line in geom.geoms:
            line = _linemerge(line)
            if not line.is_empty:
                lines.append(line)

        result_geom = linemerge(lines) if lines else None

    elif geom_type == 'LineString':
        result_geom = geom

    elif geom_type == 'MultiLineString':
        result_geom = linemerge(geom)

    else:
        result_geom = None

    if result_geom is not None:
        # simplify with very small tolerance to remove duplicate points.
        # almost duplicate or nearly colinear points can occur due to
        # numerical round-off or precision in the intersection algorithm, and
        # this should help get rid of those. see also:
        # http://lists.gispython.org/pipermail/community/2014-January/003236.html
        #
        # the tolerance here is hard-coded to a fraction of the
        # coordinate magnitude. there isn't a perfect way to figure
        # out what this tolerance should be, so this may require some
        # tweaking.
        epsilon = max(map(abs, result_geom.bounds)) * float_info.epsilon * 1000
        result_geom = result_geom.simplify(epsilon, True)

        result_geom_type = result_geom.type
        # the geometry may still have invalid or repeated points if it has zero
        # length segments, so remove anything where the length is less than
        # epsilon.
        if result_geom_type == 'LineString':
            if result_geom.length < epsilon:
                result_geom = None

        elif result_geom_type == 'MultiLineString':
            parts = []
            for line in result_geom.geoms:
                if line.length >= epsilon:
                    parts.append(line)
            result_geom = MultiLineString(parts)

    return result_geom if result_geom else MultiLineString([])


def _orient(geom):
    """
    Given a shape, returns the counter-clockwise oriented
    version. Does not affect points or lines.

    This version is required because Shapely's version is
    only defined for single polygons, and we want
    something that works generically.

    In the example below, note the change in order of the
    coordinates in `p2`, which is initially not oriented
    CCW.

    >>> p1 = Polygon([[0, 0], [1, 0], [0, 1], [0, 0]])
    >>> p2 = Polygon([[0, 1], [1, 1], [1, 0], [0, 1]])
    >>> orient(p1).wkt
    'POLYGON ((0 0, 1 0, 0 1, 0 0))'
    >>> orient(p2).wkt
    'POLYGON ((0 1, 1 0, 1 1, 0 1))'
    >>> _orient(MultiPolygon([p1, p2])).wkt
    'MULTIPOLYGON (((0 0, 1 0, 0 1, 0 0)), ((0 1, 1 0, 1 1, 0 1)))'
    """

    def oriented_multi(kind, geom):
        oriented_geoms = [_orient(g) for g in geom.geoms]
        return kind(oriented_geoms)

    geom_type = geom.type

    if geom_type == 'Polygon':
        geom = orient(geom)

    elif geom_type == 'MultiPolygon':
        geom = oriented_multi(MultiPolygon, geom)

    elif geom_type == 'GeometryCollection':
        geom = oriented_multi(GeometryCollection, geom)

    return geom


def admin_boundaries(ctx):
    """
    Given a layer with admin boundaries and inclusion polygons for
    land-based boundaries, attempts to output a set of oriented
    boundaries with properties from both the left and right admin
    boundary, and also cut with the maritime information to provide
    a `maritime_boundary: True` value where there's overlap between
    the maritime lines and the admin boundaries.

    Note that admin boundaries must alread be correctly oriented.
    In other words, it must have a positive area and run counter-
    clockwise around the polygon for which it is an outer (or
    clockwise if it was an inner).
    """

    feature_layers = ctx.feature_layers
    zoom = ctx.nominal_zoom
    base_layer = ctx.params.get('base_layer')
    assert base_layer, 'Parameter base_layer missing.'
    start_zoom = ctx.params.get('start_zoom', 0)

    layer = None

    # don't start processing until the start zoom
    if zoom < start_zoom:
        return layer

    layer = _find_layer(feature_layers, base_layer)
    if layer is None:
        return None

    # layer will have polygonal features for the admin
    # polygons and also linear features for the maritime
    # boundaries. further, we want to group the admin
    # polygons by their kind, as this will reduce the
    # working set.
    admin_features = defaultdict(list)
    maritime_features = list()
    new_features = list()

    # Sorting here so that we have consistent ordering of left/right side
    # on boundaries.
    sorted_layer = sorted(layer['features'], key=lambda f: f[1]['id'])

    for shape, props, fid in sorted_layer:
        dims = _geom_dimensions(shape)
        kind = props.get('kind')
        maritime_boundary = props.get('maritime_boundary')

        # the reason to use this rather than compare the
        # string of types is to catch the "multi-" types
        # as well.
        if dims == _LINE_DIMENSION and kind is not None:
            admin_features[kind].append((shape, props, fid))

        elif dims == _POLYGON_DIMENSION and maritime_boundary:
            maritime_features.append((shape, {'maritime_boundary': False}, 0))

    # there are separate polygons for each admin level, and
    # we only want to intersect like with like because it
    # makes more sense to have Country-Country and
    # State-State boundaries (and labels) rather than the
    # (combinatoric) set of all different levels.
    for kind, features in admin_features.iteritems():
        num_features = len(features)
        envelopes = [g[0].envelope for g in features]

        for i, feature in enumerate(features):
            boundary, props, fid = feature
            prop_id = props['id']
            envelope = envelopes[i]

            # intersect with *preceding* features to remove
            # those boundary parts. this ensures that there
            # are no duplicate parts.
            for j in range(0, i):
                cut_shape, cut_props, cut_fid = features[j]
                # don't intersect with self
                if prop_id == cut_props['id']:
                    continue
                cut_envelope = envelopes[j]
                if envelope.intersects(cut_envelope):
                    try:
                        boundary = boundary.difference(cut_shape)
                    except shapely.errors.TopologicalError:
                        # NOTE: we have gotten errors Topological errors here
                        # that look like:
                        # TopologicalError: This operation could not be
                        # performed. Reason: unknown"
                        pass

                if boundary.is_empty:
                    break

            # intersect with every *later* feature. now each
            # intersection represents a section of boundary
            # that we want to keep.
            for j in range(i+1, num_features):
                cut_shape, cut_props, cut_fid = features[j]
                # don't intersect with self
                if prop_id == cut_props['id']:
                    continue
                cut_envelope = envelopes[j]

                if envelope.intersects(cut_envelope):
                    try:
                        inside, boundary = _intersect_cut(boundary, cut_shape)
                    except (StandardError, shapely.errors.ShapelyError):
                        # if the inside and remaining boundary can't be
                        # calculated, then we can't continue to intersect
                        # anything else with this shape. this means we might
                        # end up with erroneous one-sided boundaries.

                        # TODO: log warning!
                        break

                    inside = _linemerge(inside)
                    if not inside.is_empty:
                        new_props = _merge_left_right_props(props, cut_props)
                        new_props['id'] = props['id']
                        _make_joined_name(new_props)
                        new_features.append((inside, new_props, fid))

                if boundary.is_empty:
                    break

            # anything left over at the end is still a boundary,
            # but a one-sided boundary to international waters.
            boundary = _linemerge(boundary)
            if not boundary.is_empty:
                new_props = props.copy()
                _make_joined_name(new_props)
                new_features.append((boundary, new_props, fid))

    # use intracut for maritime, but it intersects in a positive
    # way - it sets the tag on anything which intersects, whereas
    # we want to set maritime where it _doesn't_ intersect. so
    # we have to flip the attribute afterwards.
    cutter = _Cutter(maritime_features, None,
                     'maritime_boundary', 'maritime_boundary',
                     _LINE_DIMENSION, _intersect_cut)

    for shape, props, fid in new_features:
        cutter.cut(shape, props, fid)

    # flip the property, so define maritime_boundary=yes where
    # it was previously unset and remove maritime_boundary=no.
    for shape, props, fid in cutter.new_features:
        maritime_boundary = props.pop('maritime_boundary', None)
        if maritime_boundary is None:
            props['maritime_boundary'] = True

    layer['features'] = cutter.new_features
    return layer


def _unicode_len(s):
    if isinstance(s, str):
        return len(s.decode('utf-8'))
    elif isinstance(s, unicode):
        return len(s)
    return None


def _delete_labels_longer_than(max_label_chars, props):
    """
    Delete entries in the props dict where the key starts with 'name' and the
    unicode length of the value is greater than max_label_chars.

    If one half of a left/right pair is too long, then the opposite in the pair
    is also deleted.
    """

    to_delete = set()

    for k, v in props.iteritems():
        if not k.startswith('name'):
            continue

        length_chars = _unicode_len(v)
        if length_chars is None:
            # huh? name isn't a string?
            continue

        if length_chars <= max_label_chars:
            continue

        to_delete.add(k)
        if k.startswith('name:left:'):
            opposite_k = k.replace(':left:', ':right:')
            to_delete.add(opposite_k)
        elif k.startswith('name:right:'):
            opposite_k = k.replace(':right:', ':left:')
            to_delete.add(opposite_k)

    for k in to_delete:
        if k in props:
            del props[k]


def drop_names_on_short_boundaries(ctx):
    """
    Drop all names on a boundaries which are too small to render the shortest
    name.
    """

    params = _Params(ctx, 'drop_names_on_short_boundaries')
    layer_name = params.required('source_layer')
    start_zoom = params.optional('start_zoom', typ=int, default=0)
    end_zoom = params.optional('end_zoom', typ=int)
    pixels_per_letter = params.optional('pixels_per_letter', typ=(int, float),
                                        default=10.0)

    layer = _find_layer(ctx.feature_layers, layer_name)
    zoom = ctx.nominal_zoom

    if zoom < start_zoom or \
       (end_zoom is not None and zoom >= end_zoom):
        return None

    # tolerance for zoom gives us a value in meters for a pixel, so it's
    # meters per pixel
    meters_per_letter = pixels_per_letter * tolerance_for_zoom(zoom)

    for shape, props, fid in layer['features']:
        geom_type = shape.geom_type

        if geom_type in ('LineString', 'MultiLineString'):
            # simplify to one letter size. this gets close to what might
            # practically be renderable, and means we're not counting any
            # sub-letter scale fractal crinklyness towards the length of
            # the line.
            label_shape = shape.simplify(meters_per_letter)

            if geom_type == 'LineString':
                shape_length_meters = label_shape.length
            else:
                # get the longest section to see if that's labellable - if
                # not, then none of the sections could have a label and we
                # can drop the names.
                shape_length_meters = max(part.length for part in label_shape)

            # maximum number of characters we'll be able to print at this
            # zoom.
            max_label_chars = int(shape_length_meters / meters_per_letter)

            _delete_labels_longer_than(max_label_chars, props)

    return None


def handle_label_placement(ctx):
    """
    Converts a geometry label column into a separate feature.
    """
    layers = ctx.params.get('layers', None)
    zoom = ctx.nominal_zoom
    location_property = ctx.params.get('location_property', None)
    label_property_name = ctx.params.get('label_property_name', None)
    label_property_value = ctx.params.get('label_property_value', None)
    label_where = ctx.params.get('label_where', None)
    start_zoom = ctx.params.get('start_zoom', 0)

    if zoom < start_zoom:
        return None

    assert layers, 'handle_label_placement: Missing layers'
    assert location_property, \
        'handle_label_placement: Missing location_property'
    assert label_property_name, \
        'handle_label_placement: Missing label_property_name'
    assert label_property_value, \
        'handle_label_placement: Missing label_property_value'

    layers = set(layers)

    if label_where:
        label_where = compile(label_where, 'queries.yaml', 'eval')

    for feature_layer in ctx.feature_layers:
        if feature_layer['name'] not in layers:
            continue

        padded_bounds = feature_layer['padded_bounds']
        point_padded_bounds = padded_bounds['point']
        clip_bounds = Box(*point_padded_bounds)

        new_features = []
        for feature in feature_layer['features']:
            shape, props, fid = feature

            label_wkb = props.pop(location_property, None)
            new_features.append(feature)

            if not label_wkb:
                continue

            local_state = props.copy()
            local_state['properties'] = props
            if label_where and not eval(label_where, {}, local_state):
                continue

            label_shape = shapely.wkb.loads(label_wkb)
            if not (label_shape.type in ('Point', 'MultiPoint') and
                    clip_bounds.intersects(label_shape)):
                continue

            point_props = props.copy()
            point_props[label_property_name] = label_property_value
            point_feature = label_shape, point_props, fid

            new_features.append(point_feature)

        feature_layer['features'] = new_features


def generate_address_points(ctx):
    """
    Generates address points from building polygons where there is an
    addr:housenumber tag on the building. Removes those tags from the
    building.
    """

    feature_layers = ctx.feature_layers
    zoom = ctx.nominal_zoom
    source_layer = ctx.params.get('source_layer')
    assert source_layer, 'generate_address_points: missing source_layer'
    start_zoom = ctx.params.get('start_zoom', 0)

    if zoom < start_zoom:
        return None

    layer = _find_layer(feature_layers, source_layer)
    if layer is None:
        return None

    new_features = []
    for feature in layer['features']:
        shape, properties, fid = feature

        # We only want to create address points for polygonal
        # buildings with address tags.
        if shape.geom_type not in ('Polygon', 'MultiPolygon'):
            continue

        addr_housenumber = properties.get('addr_housenumber')

        # consider it an address if the name of the building
        # is just a number.
        name = properties.get('name')
        if name is not None and digits_pattern.match(name):
            if addr_housenumber is None:
                addr_housenumber = properties.pop('name')

            # and also suppress the name if it's the same as
            # the address.
            elif name == addr_housenumber:
                properties.pop('name')

        # if there's no address, then keep the feature as-is,
        # no modifications.
        if addr_housenumber is None:
            continue

        label_point = shape.representative_point()

        # we're only interested in a very few properties for
        # address points.
        label_properties = dict(
            addr_housenumber=addr_housenumber,
            kind='address')

        source = properties.get('source')
        if source is not None:
            label_properties['source'] = source

        addr_street = properties.get('addr_street')
        if addr_street is not None:
            label_properties['addr_street'] = addr_street

        oid = properties.get('id')
        if oid is not None:
            label_properties['id'] = oid

        label_feature = label_point, label_properties, fid

        new_features.append(label_feature)

    layer['features'].extend(new_features)
    return layer


def parse_layer_as_float(shape, properties, fid, zoom):
    """
    If the 'layer' property is present on a feature, then
    this attempts to parse it as a floating point number.
    The old value is removed and, if it could be parsed
    as a floating point number, the number replaces the
    original property.
    """

    layer = properties.pop('layer', None)

    if layer:
        layer_float = to_float(layer)
        if layer_float is not None:
            properties['layer'] = layer_float

    return shape, properties, fid


def drop_features_where(ctx):
    """
    Drop features entirely that match the particular "where"
    condition. Any feature properties are available to use, as well as
    the properties dict itself, called "properties" in the scope.
    """

    feature_layers = ctx.feature_layers
    zoom = ctx.nominal_zoom
    source_layer = ctx.params.get('source_layer')
    assert source_layer, 'drop_features_where: missing source layer'
    start_zoom = ctx.params.get('start_zoom', 0)
    end_zoom = ctx.params.get('end_zoom')
    where = ctx.params.get('where')
    assert where, 'drop_features_where: missing where'

    if zoom < start_zoom:
        return None
    if end_zoom is not None and zoom >= end_zoom:
        return None

    layer = _find_layer(feature_layers, source_layer)
    if layer is None:
        return None

    where = compile(where, 'queries.yaml', 'eval')

    new_features = []
    for feature in layer['features']:
        shape, properties, fid = feature

        local = properties.copy()
        local['properties'] = properties

        if not eval(where, {}, local):
            new_features.append(feature)

    layer['features'] = new_features
    return layer


def _project_properties(ctx, action):
    """
    Project properties down to a subset of the existing properties based on a
    predicate `where` which returns true when the function `action` should be
    performed. The value returned from `action` replaces the properties of the
    feature.
    """

    feature_layers = ctx.feature_layers
    zoom = ctx.nominal_zoom
    where = ctx.params.get('where')
    source_layer = ctx.params.get('source_layer')
    assert source_layer, '_project_properties: missing source layer'
    start_zoom = ctx.params.get('start_zoom', 0)
    end_zoom = ctx.params.get('end_zoom')
    geom_types = ctx.params.get('geom_types')

    if zoom < start_zoom:
        return None

    if end_zoom is not None and zoom >= end_zoom:
        return None

    layer = _find_layer(feature_layers, source_layer)
    if layer is None:
        return None

    if where is not None:
        where = compile(where, 'queries.yaml', 'eval')

    new_features = []
    for feature in layer['features']:
        shape, props, fid = feature

        # skip some types of geometry
        if geom_types and shape.geom_type not in geom_types:
            new_features.append((shape, props, fid))
            continue

        # we're going to use a defaultdict for this, so that references to
        # properties which don't exist just end up as None without causing an
        # exception. we also add a 'zoom' one. would prefer '$zoom', but
        # apparently that's not allowed in python syntax.
        local = defaultdict(lambda: None)
        local.update(props)
        local['zoom'] = zoom

        # allow decisions based on meters per pixel zoom too.
        meters_per_pixel_area = calc_meters_per_pixel_area(zoom)
        local['pixel_area'] = meters_per_pixel_area

        if where is None or eval(where, {}, local):
            props = action(props)

        new_features.append((shape, props, fid))

    layer['features'] = new_features
    return layer


def drop_properties(ctx):
    """
    Drop all configured properties for features in source_layer
    """

    properties = ctx.params.get('properties')
    all_name_variants = ctx.params.get('all_name_variants', False)
    assert properties, 'drop_properties: missing properties'

    def action(p):
        if all_name_variants and 'name' in properties:
            p = _remove_names(p)
        return _remove_properties(p, *properties)

    return _project_properties(ctx, action)


def drop_names(ctx):
    """
    Drop all names on properties for features in this layer.
    """

    def action(p):
        return _remove_names(p)

    return _project_properties(ctx, action)


def remove_zero_area(shape, properties, fid, zoom):
    """
    All features get a numeric area tag, but for points this
    is zero. The area probably isn't exactly zero, so it's
    probably less confusing to just remove the tag to show
    that the value is probably closer to "unspecified".
    """

    # remove the property if it's present. we _only_ want
    # to replace it if it matches the positive, float
    # criteria.
    area = properties.pop("area", None)

    # try to parse a string if the area has been sent as a
    # string. it should come through as a float, though,
    # since postgres treats it as a real.
    if isinstance(area, (str, unicode)):
        area = to_float(area)

    if area is not None:
        # cast to integer to match what we do for polygons.
        # also the fractional parts of a sq.m are just
        # noise really.
        area = int(area)
        if area > 0:
            properties['area'] = area

    return shape, properties, fid


# circumference of the extent of the world in mercator "meters"
_MERCATOR_CIRCUMFERENCE = 40075016.68


# _Deduplicator handles the logic for deduplication. a feature
# is considered a duplicate if it has the same property tuple
# as another and is within a certain distance of the other.
#
# the property tuple is calculated by taking a tuple or list
# of keys and extracting the value of the matching property
# or None. if none_means_unique is true, then if any tuple
# entry is None the feature is considered unique and kept.
#
# note: distance here is measured in coordinate units; i.e:
# mercator meters!
class _Deduplicator:
    def __init__(self, property_keys, min_distance,
                 none_means_unique):
        self.property_keys = property_keys
        self.min_distance = min_distance
        self.none_means_unique = none_means_unique
        self.seen_items = dict()

    def keep_feature(self, feature):
        """
        Returns true if the feature isn't a duplicate, and should
        be kept in the output. Otherwise, returns false, as
        another feature had the same tuple of values.
        """
        shape, props, fid = feature

        key = tuple([props.get(k) for k in self.property_keys])
        if self.none_means_unique and any([v is None for v in key]):
            return True

        seen_geoms = self.seen_items.get(key)
        if seen_geoms is None:
            # first time we've seen this item, so keep it in
            # the output.
            self.seen_items[key] = [shape]
            return True

        else:
            # if the distance is greater than the minimum set
            # for this zoom, then we also keep it.
            distance = min([shape.distance(s) for s in seen_geoms])

            if distance > self.min_distance:
                # this feature is far enough away to count as
                # distinct, but keep this geom to suppress any
                # other labels nearby.
                seen_geoms.append(shape)
                return True

            else:
                # feature is a duplicate
                return False


def remove_duplicate_features(ctx):
    """
    Removes duplicate features from a layer, or set of layers. The
    definition of duplicate is anything which has the same values
    for the tuple of values associated with the property_keys.

    If `none_means_unique` is set, which it is by default, then a
    value of None for *any* of the values in the tuple causes the
    feature to be considered unique and completely by-passed. This
    is mainly to handle things like features missing their name,
    where we don't want to remove all but one unnamed feature.

    For example, if property_keys was ['name', 'kind'], then only
    the first feature of those with the same value for the name
    and kind properties would be kept in the output.
    """

    feature_layers = ctx.feature_layers
    zoom = ctx.nominal_zoom
    source_layer = ctx.params.get('source_layer')
    source_layers = ctx.params.get('source_layers')
    start_zoom = ctx.params.get('start_zoom', 0)
    property_keys = ctx.params.get('property_keys')
    geometry_types = ctx.params.get('geometry_types')
    min_distance = ctx.params.get('min_distance', 0.0)
    none_means_unique = ctx.params.get('none_means_unique', True)
    end_zoom = ctx.params.get('end_zoom')

    # can use either a single source layer, or multiple source
    # layers, but not both.
    assert bool(source_layer) ^ bool(source_layers), \
        ('remove_duplicate_features: define either source layer or source '
         'layers, but not both')

    # note that the property keys or geometry types could be empty,
    # but then this post-process filter would do nothing. so we
    # assume that the user didn't intend this, or they wouldn't have
    # included the filter in the first place.
    assert property_keys, \
        'remove_duplicate_features: missing or empty property keys'
    assert geometry_types, \
        'remove_duplicate_features: missing or empty geometry types'

    if zoom < start_zoom:
        return None

    if end_zoom is not None and zoom >= end_zoom:
        return None

    # allow either a single or multiple layers to be used.
    if source_layer:
        source_layers = [source_layer]

    # correct for zoom: min_distance is given in pixels, but we
    # want to do the comparison in coordinate units to avoid
    # repeated conversions.
    min_distance = (min_distance * _MERCATOR_CIRCUMFERENCE /
                    float(1 << (zoom + 8)))

    # keep a set of the tuple of the property keys. this will tell
    # us if the feature is unique while allowing us to maintain the
    # sort order by only dropping later, presumably less important,
    # features. we keep the geometry of the seen items too, so that
    # we can tell if any new feature is significantly far enough
    # away that it should be shown again.
    deduplicator = _Deduplicator(property_keys, min_distance,
                                 none_means_unique)

    for source_layer in source_layers:
        layer_index = -1
        # because this post-processor can potentially modify
        # multiple layers, and that wasn't how the return value
        # system was designed, instead it modifies layers
        # *in-place*. this is abnormal, and as such requires a
        # nice big comment like this!
        for index, feature_layer in enumerate(feature_layers):
            layer_datum = feature_layer['layer_datum']
            layer_name = layer_datum['name']
            if layer_name == source_layer:
                layer_index = index
                break

        if layer_index < 0:
            # TODO: warn about missing layer when we get the
            # ability to log.
            continue

        layer = feature_layers[layer_index]

        new_features = []
        for feature in layer['features']:
            shape, props, fid = feature
            keep_feature = True

            if geometry_types is not None and \
               shape.geom_type in geometry_types:
                keep_feature = deduplicator.keep_feature(feature)

            if keep_feature:
                new_features.append(feature)

        # NOTE! modifying the layer *in-place*.
        layer['features'] = new_features
        feature_layers[index] = layer

    # returning None here would normally indicate that the
    # post-processor has done nothing. but because this
    # modifies the layers *in-place* then all the return
    # value is superfluous.
    return None


def merge_duplicate_stations(ctx):
    """
    Normalise station names by removing any parenthetical lines
    lists at the end (e.g: "Foo St (A, C, E)"). Parse this and
    use it to replace the `subway_routes` list if that is empty
    or isn't present.

    Use the root relation ID, calculated as part of the exploration of the
    transit relations, plus the name, now appropriately trimmed, to merge
    station POIs together, unioning their subway routes.

    Finally, re-sort the features in case the merging has caused
    the station POIs to be out-of-order.
    """

    feature_layers = ctx.feature_layers
    zoom = ctx.nominal_zoom
    source_layer = ctx.params.get('source_layer')
    assert source_layer, \
        'normalize_and_merge_duplicate_stations: missing source layer'
    start_zoom = ctx.params.get('start_zoom', 0)
    end_zoom = ctx.params.get('end_zoom')

    if zoom < start_zoom:
        return None

    # we probably don't want to do this at higher zooms (e.g: 17 &
    # 18), even if there are a bunch of stations very close
    # together.
    if end_zoom is not None and zoom >= end_zoom:
        return None

    layer = _find_layer(feature_layers, source_layer)
    if layer is None:
        return None

    seen_stations = {}
    new_features = []
    for feature in layer['features']:
        shape, props, fid = feature

        kind = props.get('kind')
        name = props.get('name')
        if name is not None and kind == 'station':
            # this should match station names where the name is
            # followed by a ()-bracketed list of line names. this
            # is common in NYC, and we want to normalise by
            # stripping these off and using it to provide the
            # list of lines if we haven't already got that info.
            m = station_pattern.match(name)

            subway_routes = props.get('subway_routes', [])
            transit_route_relation_id = props.get(
                'mz_transit_root_relation_id')

            if m:
                # if the lines aren't present or are empty
                if not subway_routes:
                    lines = m.group(2).split(',')
                    subway_routes = [x.strip() for x in lines]
                    props['subway_routes'] = subway_routes

                # update name so that it doesn't contain all the
                # lines.
                name = m.group(1).strip()
                props['name'] = name

            # if the root relation ID is available, then use that for
            # identifying duplicates. otherwise, use the name.
            key = transit_route_relation_id or name

            seen_idx = seen_stations.get(key)
            if seen_idx is None:
                seen_stations[key] = len(new_features)

                # ensure that transit routes is present and is of
                # list type for when we append to it later if we
                # find a duplicate.
                props['subway_routes'] = subway_routes
                new_features.append(feature)

            else:
                # get the properties and append this duplicate's
                # transit routes to the list on the original
                # feature.
                seen_props = new_features[seen_idx][1]

                # make sure routes are unique
                unique_subway_routes = set(subway_routes) | \
                    set(seen_props['subway_routes'])
                seen_props['subway_routes'] = list(unique_subway_routes)

        else:
            # not a station, or name is missing - we can't
            # de-dup these.
            new_features.append(feature)

    # might need to re-sort, if we merged any stations:
    # removing duplicates would have changed the number
    # of routes for each station.
    if seen_stations:
        sort_pois(new_features, zoom)

    layer['features'] = new_features
    return layer


def normalize_station_properties(ctx):
    """
    Normalise station properties by removing some which are only used
    during importance calculation. Stations may also have route
    information, which may appear as empty lists. These are
    removed. Also, flags are put on the station to indicate what
    kind(s) of station it might be.
    """

    feature_layers = ctx.feature_layers
    zoom = ctx.nominal_zoom
    source_layer = ctx.params.get('source_layer')
    assert source_layer, \
        'normalize_and_merge_duplicate_stations: missing source layer'
    start_zoom = ctx.params.get('start_zoom', 0)
    end_zoom = ctx.params.get('end_zoom')

    if zoom < start_zoom:
        return None

    # we probably don't want to do this at higher zooms (e.g: 17 &
    # 18), even if there are a bunch of stations very close
    # together.
    if end_zoom is not None and zoom >= end_zoom:
        return None

    layer = _find_layer(feature_layers, source_layer)
    if layer is None:
        return None

    for shape, props, fid in layer['features']:
        kind = props.get('kind')

        # get rid of temporaries
        root_relation_id = props.pop('mz_transit_root_relation_id', None)
        props.pop('mz_transit_score', None)

        if kind == 'station':
            # remove anything that has an empty *_routes
            # list, as this most likely indicates that we were
            # not able to _detect_ what lines it's part of, as
            # it seems unlikely that a station would be part of
            # _zero_ routes.
            for typ in ['train', 'subway', 'light_rail', 'tram']:
                prop_name = '%s_routes' % typ
                routes = props.pop(prop_name, [])
                if routes:
                    props[prop_name] = routes
                    props['is_%s' % typ] = True

            # if the station has a root relation ID then include
            # that as a way for the client to link together related
            # features.
            if root_relation_id:
                props['root_id'] = root_relation_id

    return layer


def _match_props(props, items_matching):
    """
    Checks if all the items in `items_matching` are also
    present in `props`. If so, returns true. Otherwise
    returns false.
    Each value in `items_matching` can be a list, in which case the
    value from `props` must be any one of those values.
    """

    for k, v in items_matching.iteritems():
        prop_val = props.get(k)
        if isinstance(v, list):
            if prop_val not in v:
                return False
        elif prop_val != v:
            return False

    return True


def keep_n_features(ctx):
    """
    Keep only the first N features matching `items_matching`
    in the layer. This is primarily useful for removing
    features which are abundant in some places but scarce in
    others. Rather than try to set some global threshold which
    works well nowhere, instead sort appropriately and take a
    number of features which is appropriate per-tile.

    This is done by counting each feature which matches _all_
    the key-value pairs in `items_matching` and, when the
    count is larger than `max_items`, dropping those features.

    Only features which are within the unpadded bounds of the
    tile are considered for keeping or dropping. Features
    entirely outside the bounds of the tile are always kept.
    """

    feature_layers = ctx.feature_layers
    zoom = ctx.nominal_zoom
    source_layer = ctx.params.get('source_layer')
    assert source_layer, 'keep_n_features: missing source layer'
    start_zoom = ctx.params.get('start_zoom', 0)
    end_zoom = ctx.params.get('end_zoom')
    items_matching = ctx.params.get('items_matching')
    max_items = ctx.params.get('max_items')
    unpadded_bounds = Box(*ctx.unpadded_bounds)

    # leaving items_matching or max_items as None (or zero)
    # would mean that this filter would do nothing, so assume
    # that this is really a configuration error.
    assert items_matching, 'keep_n_features: missing or empty item match dict'
    assert max_items, 'keep_n_features: missing or zero max number of items'

    if zoom < start_zoom:
        return None

    # we probably don't want to do this at higher zooms (e.g: 17 &
    # 18), even if there are a bunch of features in the tile, as
    # we use the high-zoom tiles for overzooming to 20+, and we'd
    # eventually expect to see _everything_.
    if end_zoom is not None and zoom >= end_zoom:
        return None

    layer = _find_layer(feature_layers, source_layer)
    if layer is None:
        return None

    count = 0
    new_features = []
    for shape, props, fid in layer['features']:
        keep_feature = True

        if _match_props(props, items_matching) and \
           shape.intersects(unpadded_bounds):
            count += 1
            if count > max_items:
                keep_feature = False

        if keep_feature:
            new_features.append((shape, props, fid))

    layer['features'] = new_features
    return layer


def rank_features(ctx):
    """
    Assign a rank to features in `rank_key`.

    Enumerate the features matching `items_matching` and insert
    the rank as a property with the key `rank_key`. This is
    useful for the client, so that it can selectively display
    only the top features, or de-emphasise the later features.

    Note that only features within in the unpadded bounds are ranked.
    Features entirely outside the bounds of the tile are not modified.
    """

    feature_layers = ctx.feature_layers
    zoom = ctx.nominal_zoom
    source_layer = ctx.params.get('source_layer')
    assert source_layer, 'rank_features: missing source layer'
    start_zoom = ctx.params.get('start_zoom', 0)
    items_matching = ctx.params.get('items_matching')
    rank_key = ctx.params.get('rank_key')
    unpadded_bounds_shp = Box(*ctx.unpadded_bounds)

    # leaving items_matching or rank_key as None would mean
    # that this filter would do nothing, so assume that this
    # is really a configuration error.
    assert items_matching, 'rank_features: missing or empty item match dict'
    assert rank_key, 'rank_features: missing or empty rank key'

    if zoom < start_zoom:
        return None

    layer = _find_layer(feature_layers, source_layer)
    if layer is None:
        return None

    count = 0
    for shape, props, fid in layer['features']:
        if (_match_props(props, items_matching) and
                unpadded_bounds_shp.intersects(shape)):
            count += 1
            props[rank_key] = count

    return layer


def normalize_aerialways(shape, props, fid, zoom):
    aerialway = props.get('aerialway')

    # normalise cableway, apparently a deprecated
    # value.
    if aerialway == 'cableway':
        props['aerialway'] = 'zip_line'

    # 'yes' is a pretty unhelpful value, so normalise
    # to a slightly more meaningful 'unknown', which
    # is also a commonly-used value.
    if aerialway == 'yes':
        props['aerialway'] = 'unknown'

    return shape, props, fid


def numeric_min_filter(ctx):
    """
    Keep only features which have properties equal or greater
    than the configured minima. These are in a dict per zoom
    like this:

    { 15: { 'area': 1000 }, 16: { 'area': 2000 } }

    This would mean that at zooms 15 and 16, the filter was
    active. At other zooms it would do nothing.

    Multiple filters can be given for a single zoom. The
    `mode` parameter can be set to 'any' to require that only
    one of the filters needs to match, or any other value to
    use the default 'all', which requires all filters to
    match.
    """

    feature_layers = ctx.feature_layers
    zoom = ctx.nominal_zoom
    source_layer = ctx.params.get('source_layer')
    assert source_layer, 'rank_features: missing source layer'
    filters = ctx.params.get('filters')
    mode = ctx.params.get('mode')

    # assume missing filter is a config error.
    assert filters, 'numeric_min_filter: missing or empty filters dict'

    # get the minimum filters for this zoom, and return if
    # there are none to apply.
    minima = filters.get(zoom)
    if not minima:
        return None

    layer = _find_layer(feature_layers, source_layer)
    if layer is None:
        return None

    # choose whether all minima have to be met, or just
    # one of them.
    aggregate_func = all
    if mode == 'any':
        aggregate_func = any

    new_features = []
    for shape, props, fid in layer['features']:
        keep = []

        for prop, min_val in minima.iteritems():
            val = props.get(prop)
            keep.append(val >= min_val)

        if aggregate_func(keep):
            new_features.append((shape, props, fid))

    layer['features'] = new_features
    return layer


def copy_features(ctx):
    """
    Copy features matching _both_ the `where` selection and the
    `geometry_types` list to another layer. If the target layer
    doesn't exist, it is created.
    """

    feature_layers = ctx.feature_layers
    source_layer = ctx.params.get('source_layer')
    target_layer = ctx.params.get('target_layer')
    where = ctx.params.get('where')
    geometry_types = ctx.params.get('geometry_types')

    assert source_layer, 'copy_features: source layer not configured'
    assert target_layer, 'copy_features: target layer not configured'
    assert where, \
        ('copy_features: you must specify how to match features in the where '
         'parameter')
    assert geometry_types, \
        ('copy_features: you must specify at least one type of geometry in '
         'geometry_types')

    src_layer = _find_layer(feature_layers, source_layer)
    if src_layer is None:
        return None

    tgt_layer = _find_layer(feature_layers, target_layer)
    if tgt_layer is None:
        # create target layer if it doesn't already exist.
        tgt_layer_datum = src_layer['layer_datum'].copy()
        tgt_layer_datum['name'] = target_layer
        tgt_layer = src_layer.copy()
        tgt_layer['name'] = target_layer
        tgt_layer['features'] = []
        tgt_layer['layer_datum'] = tgt_layer_datum

    new_features = []
    for feature in src_layer['features']:
        shape, props, fid = feature

        if _match_props(props, where):
            # need to deep copy, otherwise we could have some
            # unintended side effects if either layer is
            # mutated later on.
            shape_copy = shape.__class__(shape)
            new_features.append((shape_copy, props.copy(), fid))

    tgt_layer['features'].extend(new_features)
    return tgt_layer


def make_representative_point(shape, properties, fid, zoom):
    """
    Replaces the geometry of each feature with its
    representative point. This is a point which should be
    within the interior of the geometry, which can be
    important for labelling concave or doughnut-shaped
    polygons.
    """

    label_placement_wkb = properties.get('mz_label_placement', None)
    if label_placement_wkb:
        shape = shapely.wkb.loads(label_placement_wkb)
    else:
        shape = shape.representative_point()

    return shape, properties, fid


def add_iata_code_to_airports(shape, properties, fid, zoom):
    """
    If the feature is an airport, and it has a 3-character
    IATA code in its tags, then move that code to its
    properties.
    """

    kind = properties.get('kind')
    if kind not in ('aerodrome', 'airport'):
        return shape, properties, fid

    tags = properties.get('tags')
    if not tags:
        return shape, properties, fid

    iata_code = tags.get('iata')
    if not iata_code:
        return shape, properties, fid

    # IATA codes should be uppercase, and most are, but there
    # might be some in lowercase, so just normalise to upper
    # here.
    iata_code = iata_code.upper()
    if iata_short_code_pattern.match(iata_code):
        properties['iata'] = iata_code

    return shape, properties, fid


def add_uic_ref(shape, properties, fid, zoom):
    """
    If the feature has a valid uic_ref tag (7 integers), then move it
    to its properties.
    """

    tags = properties.get('tags')
    if not tags:
        return shape, properties, fid

    uic_ref = tags.get('uic_ref')
    if not uic_ref:
        return shape, properties, fid

    uic_ref = uic_ref.strip()
    if len(uic_ref) != 7:
        return shape, properties, fid

    try:
        uic_ref_int = int(uic_ref)
    except ValueError:
        return shape, properties, fid
    else:
        properties['uic_ref'] = uic_ref_int
        return shape, properties, fid


def _freeze(thing):
    """
    Freezes something to a hashable item.
    """

    if isinstance(thing, dict):
        return frozenset([(_freeze(k), _freeze(v)) for k, v in thing.items()])

    elif isinstance(thing, list):
        return tuple([_freeze(i) for i in thing])

    return thing


def _thaw(thing):
    """
    Reverse of the freeze operation.
    """

    if isinstance(thing, frozenset):
        return dict([_thaw(i) for i in thing])

    elif isinstance(thing, tuple):
        return list([_thaw(i) for i in thing])

    return thing


def quantize_val(val, step):
    # special case: if val is very small, we don't want it rounding to zero, so
    # round the smallest values up to the first step.
    if val < step:
        return int(step)

    result = int(step * round(val / float(step)))
    return result


def quantize_height_round_nearest_5_meters(height):
    return quantize_val(height, 5)


def quantize_height_round_nearest_10_meters(height):
    return quantize_val(height, 10)


def quantize_height_round_nearest_20_meters(height):
    return quantize_val(height, 20)


def quantize_height_round_nearest_meter(height):
    return round(height)


def _merge_lines(linestring_shapes, _unused_tolerance):
    list_of_linestrings = []
    for shape in linestring_shapes:
        list_of_linestrings.extend(_flatten_geoms(shape))

    # if the list of linestrings is empty, return None. this avoids generating
    # an empty GeometryCollection, which causes problems further down the line,
    # usually while formatting the tile.
    if not list_of_linestrings:
        return []

    multi = MultiLineString(list_of_linestrings)
    result = _linemerge(multi)
    return [result]


def _drop_small_inners_multi(shape, area_tolerance):
    """
    Drop inner rings (holes) of the given shape which are smaller than the area
    tolerance. The shape must be either a Polygon or MultiPolygon. Returns a
    shape which may be empty.
    """

    from shapely.geometry import MultiPolygon

    if shape.geom_type == 'Polygon':
        shape = _drop_small_inners(shape, area_tolerance)

    elif shape.geom_type == 'MultiPolygon':
        multi = []
        for poly in shape:
            new_poly = _drop_small_inners(poly, area_tolerance)
            if not new_poly.is_empty:
                multi.append(new_poly)
        shape = MultiPolygon(multi)

    else:
        shape = MultiPolygon([])

    return shape


def _drop_small_outers_multi(shape, area_tolerance):
    """
    Drop individual polygons which are smaller than the area tolerance. Input
    can be a single Polygon or MultiPolygon, in which case each Polygon within
    the MultiPolygon will be compared to the area tolerance individually.

    Returns a shape, which may be empty.
    """

    from shapely.geometry import MultiPolygon

    if shape.geom_type == 'Polygon':
        if shape.area < area_tolerance:
            shape = MultiPolygon([])

    elif shape.geom_type == 'MultiPolygon':
        multi = []
        for poly in shape:
            if poly.area >= area_tolerance:
                multi.append(poly)
        shape = MultiPolygon(multi)

    else:
        shape = MultiPolygon([])

    return shape


def _merge_polygons(polygon_shapes, tolerance):
    """
    Merge a list of polygons together into a single shape. Returns list of
    shapes, which might be empty.
    """

    list_of_polys = []
    for shape in polygon_shapes:
        list_of_polys.extend(_flatten_geoms(shape))

    # if the list of polygons is empty, return None. this avoids generating an
    # empty GeometryCollection, which causes problems further down the line,
    # usually while formatting the tile.
    if not list_of_polys:
        return []

    # first, try to merge the polygons as they are.
    try:
        result = shapely.ops.unary_union(list_of_polys)
        return [result]

    except ValueError:
        pass

    # however, this can lead to numerical instability where polygons _almost_
    # touch, so sometimes buffering them outwards a little bit can help.
    try:
        from shapely.geometry import JOIN_STYLE

        # don't buffer by the full pixel, instead choose a smaller value that
        # shouldn't be noticable.
        buffer_size = tolerance / 16.0

        list_of_buffered = [
            p.buffer(buffer_size, join_style=JOIN_STYLE.mitre, mitre_limit=1.5)
            for p in list_of_polys
        ]
        result = shapely.ops.unary_union(list_of_buffered)
        return [result]

    except ValueError:
        pass

    # ultimately, if it's not possible to merge them then bail.
    # TODO: when we get a logger in here, let's log a big FAIL message.
    return []


def _merge_polygons_with_buffer(polygon_shapes, tolerance):
    """
    Merges polygons together with a buffer operation to blend together
    adjacent polygons. Originally designed for buildings.

    It does this by first merging the polygons into a single MultiPolygon and
    then dilating or buffering the polygons by a small amount (tolerance). The
    shape is then simplified, small inners are dropped and it is shrunk back
    by the same amount it was dilated by. Finally, small polygons are dropped.

    Many cities around the world have dense buildings in blocks, but these
    buildings can be quite detailed; having complex facades or interior
    courtyards or lightwells. As we zoom out, we often would like to keep the
    "visual texture" of the buildings, but reducing the level of detail
    significantly. This method aims to get closer to that, merging neighbouring
    buildings together into blocks.
    """

    from shapely.geometry import JOIN_STYLE

    area_tolerance = tolerance * tolerance
    # small factor, relative to tolerance. this is used so that we don't buffer
    # polygons out by exactly the same amount as we buffer them inwards. using
    # the exact same value ends up causing topology problems when two points on
    # opposing sides of the polygon meet eachother exactly.
    epsilon = tolerance * 1.0e-6

    result = _merge_polygons(polygon_shapes, tolerance)
    if not result:
        return result

    assert len(result) == 1
    result = result[0]

    # buffer with a mitre join, as this keeps the corners sharp and (mostly)
    # keeps angles the same. to avoid spikes, we limit the mitre to a little
    # under 90 degrees.
    result = result.buffer(
        tolerance - epsilon, join_style=JOIN_STYLE.mitre, mitre_limit=1.5)
    result = result.simplify(tolerance)
    result = _drop_small_inners_multi(result, area_tolerance)
    result = result.buffer(
        -tolerance, join_style=JOIN_STYLE.mitre, mitre_limit=1.5)
    result = _drop_small_outers_multi(result, area_tolerance)

    # don't return invalid results!
    if result.is_empty or not result.is_valid:
        return []

    return [result]


def _union_bounds(a, b):
    """
    Union two (minx, miny, maxx, maxy) tuples of bounds, returning a tuple
    which covers both inputs.
    """

    if a is None:
        return b
    elif b is None:
        return a
    else:
        aminx, aminy, amaxx, amaxy = a
        bminx, bminy, bmaxx, bmaxy = b
        return (min(aminx, bminx), min(aminy, bminy),
                max(amaxx, bmaxx), max(amaxy, bmaxy))


def _intersects_bounds(a, b):
    """
    Return true if two bounding boxes intersect.
    """

    aminx, aminy, amaxx, amaxy = a
    bminx, bminy, bmaxx, bmaxy = b

    if aminx > bmaxx or amaxx < bminx:
        return False

    elif aminy > bmaxy or amaxy < bminy:
        return False

    return True


# RecursiveMerger is a set of functions to merge geometry recursively in a
# quad tree.
#
# It consists of three functions, any of which can be `id` for a no-op, and
# all of which take a single argument which will be a list of shapes, and
# should return a list of shapes as output.
#
#   * leaf: called at the leaves of the quad tree with original geometry.
#   * node: called at internal nodes of the quad tree with the results of
#           either calls to leaf() or node().
#   * root: called once at the root with the results of the top node (or leaf
#           if it's a degenerate single-level tree).
#   * tolerance: a length that is approximately a pixel, or the size by which
#                things can be simplified or snapped to.
#
# These allow us to merge transformed versions of geometry, where leaf()
# transforms the geometry to some other form (e.g: buffered for buildings),
# node merges those recursively, and then root reverses the buffering.
#
RecursiveMerger = namedtuple('RecursiveMerger', 'leaf node root tolerance')


# A bucket used to sort shapes into the next level of the quad tree.
Bucket = namedtuple("Bucket", "bounds box shapes")


def _mkbucket(*bounds):
    """
    Convenience method to make a bucket from a tuple of bounds (minx, miny,
    maxx, maxy) and also make the Shapely shape for that.
    """

    from shapely.geometry import box

    return Bucket(bounds, box(*bounds), [])


def _merge_shapes_recursively(shapes, shapes_per_merge, merger, depth=0,
                              bounds=None):
    """
    Group the shapes geographically, returning a list of shapes. The merger,
    which must be a RecursiveMerger, controls how the shapes are merged.

    This is to help merging/unioning, where it's better to try and merge shapes
    which are adjacent or near each other, rather than just taking a slice of
    a list of shapes which might be in any order.

    The shapes_per_merge controls at what depth the tree starts merging.
    Smaller values mean a deeper tree, which might increase performance if
    merging large numbers of items at once is slow.

    This method is recursive, and will bottom out after 5 levels deep, which
    might mean that sometimes more than shapes_per_merge items are merged at
    once.
    """

    assert isinstance(merger, RecursiveMerger)

    # don't keep recursing. if we haven't been able to get to a smaller number
    # of shapes by 5 levels down, then perhaps there are particularly large
    # shapes which are preventing things getting split up correctly.
    if len(shapes) <= shapes_per_merge and depth == 0:
        return merger.root(merger.leaf(shapes, merger.tolerance))
    elif depth >= 5:
        return merger.leaf(shapes, merger.tolerance)

    # on the first call, figure out what the bounds of the shapes are. when
    # recursing, use the bounds passed in from the parent.
    if bounds is None:
        for shape in shapes:
            bounds = _union_bounds(bounds, shape.bounds)

    minx, miny, maxx, maxy = bounds
    midx = 0.5 * (minx + maxx)
    midy = 0.5 * (miny + maxy)

    # find the 4 quadrants of the bounding box and use those to bucket the
    # shapes so that neighbouring shapes are more likely to stay together.
    buckets = [
        _mkbucket(minx, miny, midx, midy),
        _mkbucket(minx, midy, midx, maxy),
        _mkbucket(midx, miny, maxx, midy),
        _mkbucket(midx, midy, maxx, maxy),
    ]

    for shape in shapes:
        for bucket in buckets:
            if shape.intersects(bucket.box):
                bucket.shapes.append(shape)
                break
        else:
            raise AssertionError(
                "Expected shape %r to intersect at least one quadrant, but "
                "intersects none." % (shape.wkt))

    # recurse if necessary to get below the number of shapes per merge that
    # we want.
    grouped_shapes = []
    for bucket in buckets:
        if len(bucket.shapes) > shapes_per_merge:
            recursed = _merge_shapes_recursively(
                bucket.shapes, shapes_per_merge, merger,
                depth=depth+1, bounds=bucket.bounds)
            grouped_shapes.extend(recursed)

        # don't add empty lists!
        elif bucket.shapes:
            grouped_shapes.extend(merger.leaf(bucket.shapes, merger.tolerance))

    fn = merger.root if depth == 0 else merger.node
    return fn(grouped_shapes)


def _noop(x):
    return x


def _merge_features_by_property(
        features, geom_dim, tolerance,
        update_props_pre_fn=None,
        update_props_post_fn=None,
        max_merged_features=None,
        merge_shape_fn=None,
        merge_props_fn=None):

    assert geom_dim in (_POLYGON_DIMENSION, _LINE_DIMENSION)
    if merge_shape_fn is not None:
        _merge_shape_fn = merge_shape_fn
    elif geom_dim == _LINE_DIMENSION:
        _merge_shape_fn = _merge_lines
    else:
        _merge_shape_fn = _merge_polygons

    features_by_property = {}
    skipped_features = []
    for feature in features:
        shape, props, fid = feature
        shape_dim = _geom_dimensions(shape)
        if shape_dim != geom_dim:
            skipped_features.append(feature)
            continue

        orig_props = props.copy()
        p_id = props.pop('id', None)
        if update_props_pre_fn:
            props = update_props_pre_fn((shape, props, fid))

        if props is None:
            skipped_features.append((shape, orig_props, fid))
            continue

        frozen_props = _freeze(props)
        if frozen_props in features_by_property:
            record = features_by_property[frozen_props]
            record[-1].append(shape)
            record[-2].append(orig_props)
        else:
            features_by_property[frozen_props] = (
                (fid, p_id, [orig_props], [shape]))

    new_features = []
    for frozen_props, (fid, p_id, orig_props, shapes) in \
            features_by_property.iteritems():

        if len(shapes) == 1:
            # restore original properties if we only have a single shape
            new_features.append((shapes[0], orig_props[0], fid))
            continue

        num_shapes = len(shapes)
        shapes_per_merge = num_shapes
        if max_merged_features and max_merged_features < shapes_per_merge:
            shapes_per_merge = max_merged_features
            # reset fid if we're going to split up features, as we don't want
            # them all to have duplicate IDs.
            fid = None

        merger = RecursiveMerger(root=_noop, node=_noop, leaf=_merge_shape_fn,
                                 tolerance=tolerance)

        for merged_shape in _merge_shapes_recursively(
                shapes, shapes_per_merge, merger):
            # don't keep any features which have become degenerate or empty
            # after having been merged.
            if merged_shape is None or merged_shape.is_empty:
                continue

            if merge_props_fn is None:
                # thaw the frozen properties to use in the new feature.
                props = _thaw(frozen_props)
            else:
                props = merge_props_fn(orig_props)

            if update_props_post_fn:
                props = update_props_post_fn((merged_shape, props, fid))

            new_features.append((merged_shape, props, fid))

    new_features.extend(skipped_features)
    return new_features


def quantize_height(ctx):
    """
    Quantize the height property of features in the layer according to the
    per-zoom configured quantize function.
    """

    params = _Params(ctx, 'quantize_height')
    zoom = ctx.nominal_zoom
    source_layer = params.required('source_layer')
    start_zoom = params.optional('start_zoom', default=0, typ=int)
    end_zoom = params.optional('end_zoom', typ=int)
    quantize_cfg = params.required('quantize', typ=dict)

    layer = _find_layer(ctx.feature_layers, source_layer)
    if layer is None:
        return None

    if zoom < start_zoom:
        return None
    if end_zoom is not None and zoom >= end_zoom:
        return None

    quantize_fn_dotted_name = quantize_cfg.get(zoom)
    if not quantize_fn_dotted_name:
        # no changes at this zoom
        return None

    quantize_height_fn = resolve(quantize_fn_dotted_name)
    for shape, props, fid in layer['features']:
        height = props.get('height', None)
        if height is not None:
            props['height'] = quantize_height_fn(height)

    return None


def merge_building_features(ctx):
    zoom = ctx.nominal_zoom
    source_layer = ctx.params.get('source_layer')
    start_zoom = ctx.params.get('start_zoom', 0)
    end_zoom = ctx.params.get('end_zoom')
    drop = ctx.params.get('drop')
    exclusions = ctx.params.get('exclude')
    max_merged_features = ctx.params.get('max_merged_features')

    assert source_layer, 'merge_building_features: missing source layer'
    layer = _find_layer(ctx.feature_layers, source_layer)
    if layer is None:
        return None

    if zoom < start_zoom:
        return None
    if end_zoom is not None and zoom >= end_zoom:
        return None

    # this formula seems to give a good balance between larger values, which
    # merge more but can merge everything into a blob if too large, and small
    # values which retain detail.
    tolerance = min(5, 0.4 * tolerance_for_zoom(zoom))

    def _props_pre((shape, props, fid)):
        if exclusions:
            for prop in exclusions:
                if prop in props:
                    return None

        # also drop building properties that we won't want to consider
        # for merging. area and volume will be re-calculated afterwards
        props.pop('area', None)
        props.pop('volume', None)

        if drop:
            for prop in drop:
                props.pop(prop, None)

        return props

    def _props_post((merged_shape, props, fid)):
        # add the area and volume back in
        area = int(merged_shape.area)
        props['area'] = area
        height = props.get('height')
        if height is not None:
            props['volume'] = height * area
        return props

    layer['features'] = _merge_features_by_property(
        layer['features'], _POLYGON_DIMENSION, tolerance, _props_pre,
        _props_post, max_merged_features,
        merge_shape_fn=_merge_polygons_with_buffer)
    return layer


def merge_polygon_features(ctx):
    """
    Merge polygons having the same properties, apart from 'id' and 'area', in
    the source_layer between start_zoom and end_zoom inclusive.

    Area is re-calculated post-merge and IDs are preserved for features which
    are unique in the merge.
    """

    zoom = ctx.nominal_zoom
    source_layer = ctx.params.get('source_layer')
    start_zoom = ctx.params.get('start_zoom', 0)
    end_zoom = ctx.params.get('end_zoom')
    merge_min_zooms = ctx.params.get('merge_min_zooms', False)
    buffer_merge = ctx.params.get('buffer_merge', False)
    buffer_merge_tolerance = ctx.params.get('buffer_merge_tolerance')

    assert source_layer, 'merge_polygon_features: missing source layer'
    layer = _find_layer(ctx.feature_layers, source_layer)
    if layer is None:
        return None

    if zoom < start_zoom:
        return None
    if end_zoom is not None and zoom >= end_zoom:
        return None

    tfz = tolerance_for_zoom(zoom)
    if buffer_merge_tolerance:
        tolerance = eval(buffer_merge_tolerance, {}, {
            'tolerance_for_zoom': tfz,
        })
    else:
        tolerance = tfz

    def _props_pre((shape, props, fid)):
        # drop area while merging, as we'll recalculate after.
        props.pop('area', None)
        if merge_min_zooms:
            props.pop('min_zoom', None)
        return props

    def _props_post((merged_shape, props, fid)):
        # add the area back in
        area = int(merged_shape.area)
        props['area'] = area
        return props

    def _props_merge(all_props):
        merged_props = None
        for props in all_props:
            if merged_props is None:
                merged_props = props.copy()
            else:
                min_zoom = props.get('min_zoom')
                merged_min_zoom = merged_props.get('min_zoom')
                if min_zoom and (merged_min_zoom is None or
                                 min_zoom < merged_min_zoom):
                    merged_props['min_zoom'] = min_zoom
        return merged_props

    merge_props_fn = _props_merge if merge_min_zooms else None
    merge_shape_fn = _merge_polygons_with_buffer if buffer_merge else None

    layer['features'] = _merge_features_by_property(
        layer['features'], _POLYGON_DIMENSION, tolerance, _props_pre,
        _props_post, merge_props_fn=merge_props_fn,
        merge_shape_fn=merge_shape_fn)
    return layer


def _angle_at(linestring, pt):
    import math

    if pt == linestring.coords[0]:
        nx = linestring.coords[1]
    elif pt == linestring.coords[-1]:
        nx = pt
        pt = linestring.coords[-2]
    else:
        assert False, "Expected point to be first or last"

    if nx == pt:
        return None

    dx = nx[0] - pt[0]
    dy = nx[1] - pt[1]
    if dy < 0.0:
        dx = -dx
        dy = -dy

    a = math.atan2(dy, dx) / math.pi * 180.0

    # wrap around at exactly 180, because we don't care about the direction of
    # the road, only what angle the line is at, and 180 is horizontal same as
    # 0.
    if a == 180.0:
        a = 0.0

    assert 0 <= a < 180
    return a


def _junction_merge_candidates(ids, geoms, pt, angle_tolerance):
    # find the angles at which the lines join the point
    angles = []
    for i in ids:
        a = _angle_at(geoms[i], pt)
        if a is not None:
            angles.append((a, i))

    # turn that into an angle->index associative list, so
    # that we can tell which are the closest pair of angles.
    angles.sort()

    # list of pairs of ids, candidates to be merged.
    candidates = []

    # loop over the list, removing the closest pair, as long
    # as they're within the tolerance angle of eachother.
    while len(angles) > 1:
        min_angle = None
        for j in xrange(0, len(angles)):
            angle1, idx1 = angles[j]
            angle0, idx0 = angles[j-1]

            # usually > 0 since angles are sorted, but might be negative
            # on the first index (angles[-1]). note that, since we're
            # taking the non-directional angle, the result should be
            # between 0 and 180.
            delta_angle = angle1 - angle0
            if delta_angle < 0:
                delta_angle += 180

            if min_angle is None or delta_angle < min_angle[0]:
                min_angle = (delta_angle, j)

        if min_angle[0] >= angle_tolerance or min_angle is None:
            break

        candidates.append((angles[j][1], angles[j-1][1]))
        del angles[j]
        del angles[j-1]

    return candidates


def _merge_junctions_in_multilinestring(mls, angle_tolerance):
    """
    Merge LineStrings within a MultiLineString across junctions where more
    than two lines meet and the lines appear to continue across the junction
    at the same angle.

    The angle_tolerance (in degrees) is used to judge whether two lines
    look like they continue across a junction.

    Returns a new shape.
    """

    endpoints = defaultdict(list)
    for i, ls in enumerate(mls.geoms):
        endpoints[ls.coords[0]].append(i)
        endpoints[ls.coords[-1]].append(i)

    seen = set()
    merged_geoms = []
    for pt, ids in endpoints.iteritems():
        # we can't merge unless we've got at least 2 lines!
        if len(ids) < 2:
            continue

        candidates = _junction_merge_candidates(
            ids, mls.geoms, pt, angle_tolerance)
        for a, b in candidates:
            if a not in seen and b not in seen and a != b:
                merged = linemerge(MultiLineString(
                    [mls.geoms[a], mls.geoms[b]]))
                if merged.geom_type == 'LineString':
                    merged_geoms.append(merged)
                    seen.add(a)
                    seen.add(b)
                elif (merged.geom_type == 'MultiLineString' and
                      len(merged.geoms) == 1):
                    merged_geoms.append(merged.geoms[0])
                    seen.add(a)
                    seen.add(b)

    # add back any left over linestrings which didn't get merged.
    for i, ls in enumerate(mls.geoms):
        if i not in seen:
            merged_geoms.append(ls)

    if len(merged_geoms) == 1:
        return merged_geoms[0]
    else:
        return MultiLineString(merged_geoms)


def _loop_merge_junctions(geom, angle_tolerance):
    """
    Keep applying junction merging to the MultiLineString until there are no
    merge opportunities left.

    A single merge step will only carry out one merge per LineString, which
    means that the other endpoint might miss out on a possible merge. So we
    loop over the merge until all opportunities are exhausted: either we end
    up with a single LineString or we run a step and it fails to merge any
    candidates.

    For a total number of possible merges, N, we could potentially be left
    with two thirds of these left over, depending on the order of the
    candidates. This means we should need only O(log N) steps to merge them
    all.
    """

    if geom.geom_type != 'MultiLineString':
        return geom

    # keep track of the number of linestrings in the multilinestring. we'll
    # use that to figure out if we've merged as much as we possibly can.
    mls_size = len(geom.geoms)

    while True:
        geom = _merge_junctions_in_multilinestring(geom, angle_tolerance)

        # merged everything down to a single linestring
        if geom.geom_type == 'LineString':
            break

        # made no progress
        elif len(geom.geoms) == mls_size:
            break

        assert len(geom.geoms) < mls_size, \
            "Number of geometries should stay the same or reduce after merge."

        # otherwise, keep looping
        mls_size = len(geom.geoms)

    return geom


def _simplify_line_collection(shape, tolerance):
    """
    Calling simplify on a MultiLineString doesn't always simplify if it would
    make the MultiLineString non-simple.

    However, we're trying to sort linestrings into nonoverlapping sets, and we
    don't care whether they overlap at this point. However, we do want to make
    sure that any colinear points in the individual LineStrings are removed.
    """

    if shape.geom_type == 'LineString':
        shape = shape.simplify(tolerance)

    elif shape.geom_type == 'MultiLineString':
        new_geoms = []
        for geom in shape.geoms:
            new_geoms.append(geom.simplify(tolerance))
        shape = MultiLineString(new_geoms)

    return shape


def _merge_junctions(features, angle_tolerance, simplify_tolerance,
                     split_threshold):
    """
    Merge LineStrings within MultiLineStrings within features across junction
    boundaries where the lines appear to continue at the same angle.

    If simplify_tolerance is provided, apply a simplification step. This can
    help to remove colinear junction points left over from any merging.

    Finally, group the lines into non-overlapping sets, each of which generates
    a separate MultiLineString feature to ensure they're already simple and
    further geometric operations won't re-introduce intersection points.

    Large linestrings, with more than split_threshold members, use a slightly
    different algorithm which is more efficient at very large sizes.

    Returns a new list of features.
    """

    new_features = []
    for shape, props, fid in features:
        if shape.geom_type == 'MultiLineString':
            shape = _loop_merge_junctions(shape, angle_tolerance)

        if simplify_tolerance > 0.0:
            shape = _simplify_line_collection(shape, simplify_tolerance)

        if shape.geom_type == 'MultiLineString':
            disjoint_shapes = _linestring_nonoverlapping_partition(
                shape, split_threshold)
            for disjoint_shape in disjoint_shapes:
                new_features.append((disjoint_shape, props, None))

        else:
            new_features.append((shape, props, fid))

    return new_features


def _first_positive_integer_not_in(s):
    """
    Given a set of positive integers, s, return the smallest positive integer
    which is _not_ in s.

    For example:

    >>> _first_positive_integer_not_in(set())
    1
    >>> _first_positive_integer_not_in(set([1]))
    2
    >>> _first_positive_integer_not_in(set([1,3,4]))
    2
    >>> _first_positive_integer_not_in(set([1,2,3,4]))
    5
    """

    if len(s) == 0:
        return 1

    last = max(s)
    for i in xrange(1, last):
        if i not in s:
            return i
    return last + 1


# utility class so that we can store the array index of the geometry
# inside the shape index.
class _geom_with_index(object):
    def __init__(self, geom, index):
        self.geom = geom
        self.index = index
        self._geom = geom._geom
        self.is_empty = geom.is_empty


class OrderedSTRTree(object):
    """
    An STR-tree geometry index which remembers the array index of the
    geometries it was built with, and only returns geometries with lower
    indices when queried.

    This is used as a substitute for a dynamic index, where we'd be able
    to add new geometries as the algorithm progressed.
    """

    def __init__(self, geoms):
        self.shape_index = STRtree([
            _geom_with_index(g, i) for i, g in enumerate(geoms)
        ])

    def query(self, shape, idx):
        """
        Return the index elements which have bounding boxes intersecting the
        given shape _and_ have array indices less than idx.
        """

        for geom in self.shape_index.query(shape):
            if geom.index < idx:
                yield geom


class SplitOrderedSTRTree(object):
    """
    An ordered STR-tree index which splits the geometries it is managing.

    This is a simple, first-order approximation to a dynamic index. If the
    input geometries are sorted by increasing size, then the "small" first
    section are much less likely to overlap, and we know we're not interested
    in anything in the "big" section because the index isn't large enough.

    This should cut down the number of expensive queries, as well as the
    number of subsequent intersection tests to check if the shapes within the
    bounding boxes intersect.
    """

    def __init__(self, geoms):
        split = int(0.75 * len(geoms))
        self.small_index = STRtree([
            _geom_with_index(g, i) for i, g in enumerate(geoms[0:split])
        ])
        self.big_index = STRtree([
            _geom_with_index(g, i + split) for i, g in enumerate(geoms[split:])
        ])
        self.split = split

    def query(self, shape, i):
        for geom in self.small_index.query(shape):
            if geom.index < i:
                yield geom

        # don't need to query the big index at all unless i >= split. this
        # should cut down on the number of yielded items that need further
        # intersection tests.
        if i >= self.split:
            for geom in self.big_index.query(shape):
                if geom.index < i:
                    yield geom


def _linestring_nonoverlapping_partition(mls, split_threshold=15000):
    """
    Given a MultiLineString input, returns a list of MultiLineStrings
    which are individually simple, but cover all the points in the
    input MultiLineString.

    The OGC definition of a MultiLineString says it's _simple_ if it
    consists of simple LineStrings and the LineStrings only meet each
    other at their endpoints. This means that anything which makes
    MultiLineStrings simple is going to insert intersections between
    crossing lines, and decompose them into separate LineStrings.

    In general we _do not want_ this behaviour, as it prevents
    simplification and results in more points in the geometry. However,
    there are many operations which will result in simple outputs, such
    as intersections and unions. Therefore, we would prefer to take the
    hit of having multiple features, if the features can be decomposed
    in such a way that they are individually simple.
    """

    # only interested in MultiLineStrings for this method!
    assert mls.geom_type == 'MultiLineString'

    # simple (and sub-optimal) greedy algorithm for making sure that
    # linestrings don't intersect: put each into the first bucket which
    # doesn't already contain a linestring which intersects it.
    #
    # this will be suboptimal. for example:
    #
    #      2 4
    #      | |
    # 3 ---+-+---
    #      | |
    # 1 -----+---
    #        |
    #
    # (lines 1 & 2 do _not_ intersect).
    #
    # the greedy algorithm will use 3 buckets, as it'll put lines 1 & 2 in
    # the same bucket, forcing 3 & 4 into individual buckets for a total
    # of 3 buckets. optimally, we can bucket 1 & 3 together and 2 & 4
    # together to only use 2 buckets. however, making this optimal seems
    # like it might be a Hard problem.
    #
    # note that we don't create physical buckets, but assign each shape a
    # bucket ID which hasn't been assigned to any other intersecting shape.
    # we can assign these in an arbitrary order, and use an index to reduce
    # the number of intersection tests needed down to O(n log n). this can
    # matter quite a lot at low zooms, where it's possible to get 150,000
    # tiny road segments in a single shape!

    # sort the geometries before we use them. this can help if we sort things
    # which have fewer intersections towards the front of the array, so that
    # they can be done more quickly.
    def _bbox_area(geom):
        minx, miny, maxx, maxy = geom.bounds
        return (maxx - minx) * (maxy - miny)

    # if there's a large number of geoms, switch to the split index and sort
    # so that the spatially largest objects are towards the end of the list.
    # this should make it more likely that earlier queries are fast.
    if len(mls.geoms) > split_threshold:
        geoms = sorted(mls.geoms, key=_bbox_area)
        shape_index = SplitOrderedSTRTree(geoms)
    else:
        geoms = mls.geoms
        shape_index = OrderedSTRTree(geoms)

    # first, assign everything the "null" bucket with index zero. this means
    # we haven't gotten around to it yet, and we can use it as a sentinel
    # value to check for logic errors.
    bucket_for_shape = [0] * len(geoms)

    for idx, shape in enumerate(geoms):
        overlapping_buckets = set()

        # assign the lowest bucket ID that hasn't been assigned to any
        # overlapping shape with a lower index. this is because:
        #  1. any overlapping shape would cause the insertion of a point if it
        #     were allowed in this bucket, and
        #  2. we're assigning in-order, so shapes at higher array indexes will
        #     still be assigned to the null bucket. we'll get to them later!
        for indexed_shape in shape_index.query(shape, idx):
            if indexed_shape.geom.intersects(shape):
                bucket = bucket_for_shape[indexed_shape.index]
                assert bucket > 0
                overlapping_buckets.add(bucket)

        bucket_for_shape[idx] = _first_positive_integer_not_in(
            overlapping_buckets)

    results = []
    for bucket_id in set(bucket_for_shape):
        # by this point, no shape should be assigned to the null bucket any
        # more.
        assert bucket_id > 0

        # collect all the shapes which have been assigned to this bucket.
        shapes = []
        for idx, shape in enumerate(geoms):
            if bucket_for_shape[idx] == bucket_id:
                shapes.append(shape)

        if len(shapes) == 1:
            results.append(shapes[0])
        else:
            results.append(MultiLineString(shapes))

    return results


def _drop_short_segments_from_multi(tolerance, mls):
    return MultiLineString(
        [g for g in mls.geoms if g.length >= tolerance])


def _drop_short_segments(tolerance, features):
    new_features = []

    for shape, props, fid in features:
        if shape.geom_type == 'MultiLineString':
            shape = _drop_short_segments_from_multi(tolerance, shape)

        elif shape.geom_type == 'LineString':
            if shape.length < tolerance:
                shape = None

        if shape and not shape.is_empty:
            new_features.append((shape, props, fid))

    return new_features


def merge_line_features(ctx):
    """
    Merge linestrings having the same properties, in the source_layer
    between start_zoom and end_zoom inclusive.

    By default, will not merge features across points where more than
    two lines meet. If you set merge_junctions, then it will try to
    merge where the line looks contiguous.
    """

    params = _Params(ctx, 'merge_line_features')
    zoom = ctx.nominal_zoom
    source_layer = params.required('source_layer')
    start_zoom = params.optional('start_zoom', default=0, typ=int)
    end_zoom = params.optional('end_zoom', typ=int)
    merge_junctions = params.optional(
        'merge_junctions', default=False, typ=bool)
    junction_angle_tolerance = params.optional(
        'merge_junction_angle', default=15.0, typ=float)
    drop_short_segments = params.optional(
        'drop_short_segments', default=False, typ=bool)
    short_segment_factor = params.optional(
        'drop_length_pixels', default=0.1, typ=float)
    simplify_tolerance = params.optional(
        'simplify_tolerance', default=0.0, typ=float)
    split_threshold = params.optional(
        'split_threshold', default=15000, typ=int)

    assert source_layer, 'merge_line_features: missing source layer'
    layer = _find_layer(ctx.feature_layers, source_layer)
    if layer is None:
        return None

    if zoom < start_zoom:
        return None
    if end_zoom is not None and zoom >= end_zoom:
        return None

    layer['features'] = _merge_features_by_property(
        layer['features'], _LINE_DIMENSION, simplify_tolerance)

    if drop_short_segments:
        tolerance = short_segment_factor * tolerance_for_zoom(zoom)
        layer['features'] = _drop_short_segments(
            tolerance, layer['features'])

    if merge_junctions:
        layer['features'] = _merge_junctions(
            layer['features'], junction_angle_tolerance, simplify_tolerance,
            split_threshold)

    return layer


def normalize_tourism_kind(shape, properties, fid, zoom):
    """
    There are many tourism-related tags, including 'zoo=*' and
    'attraction=*' in addition to 'tourism=*'. This function promotes
    things with zoo and attraction tags have those values as their
    main kind.

    See https://github.com/mapzen/vector-datasource/issues/440 for more details.
    """  # noqa

    zoo = properties.pop('zoo', None)
    if zoo is not None:
        properties['kind'] = zoo
        properties['tourism'] = 'attraction'
        return (shape, properties, fid)

    attraction = properties.pop('attraction', None)
    if attraction is not None:
        properties['kind'] = attraction
        properties['tourism'] = 'attraction'
        return (shape, properties, fid)

    return (shape, properties, fid)


# a whitelist of the most common fence types from OSM.
# see https://taginfo.openstreetmap.org/keys/fence_type#values
_WHITELIST_FENCE_TYPES = set([
    'avalanche',
    'barbed_wire',
    'bars',
    'brick',  # some might say a fence made of brick is called a wall...
    'chain',
    'chain_link',
    'concrete',
    'drystone_wall',
    'electric',
    'grate',
    'hedge',
    'metal',
    'metal_bars',
    'net',
    'pole',
    'railing',
    'railings',
    'split_rail',
    'steel',
    'stone',
    'wall',
    'wire',
    'wood',
])


def build_fence(ctx):
    """
    Some landuse polygons have an extra barrier fence tag, in thouse cases we
    want to create an additional feature for the fence.

    See https://github.com/mapzen/vector-datasource/issues/857 for more
    details.
    """
    feature_layers = ctx.feature_layers
    zoom = ctx.nominal_zoom
    base_layer = ctx.params.get('base_layer')
    new_layer_name = ctx.params.get('new_layer_name')
    prop_transform = ctx.params.get('prop_transform')
    assert base_layer, 'Missing base_layer parameter'
    start_zoom = ctx.params.get('start_zoom', 16)

    layer = None

    # don't start processing until the start zoom
    if zoom < start_zoom:
        return layer

    # search through all the layers and extract the one
    # which has the name of the base layer we were given
    # as a parameter.
    layer = _find_layer(feature_layers, base_layer)

    # if we failed to find the base layer then it's
    # possible the user just didn't ask for it, so return
    # an empty result.
    if layer is None:
        return None

    if prop_transform is None:
        prop_transform = {}

    features = layer['features']

    new_features = list()
    # loop through all the polygons, if it's a fence, duplicate it.
    for feature in features:
        shape, props, fid = feature

        barrier = props.pop('barrier', None)

        if barrier == 'fence':
            fence_type = props.pop('fence_type', None)
            # filter only linestring-like objects. we don't
            # want any points which might have been created
            # by the intersection.
            filtered_shape = _filter_geom_types(shape, _POLYGON_DIMENSION)

            if not filtered_shape.is_empty:
                new_props = _make_new_properties(props, prop_transform)
                new_props['kind'] = 'fence'
                if fence_type in _WHITELIST_FENCE_TYPES:
                    new_props['kind_detail'] = fence_type

                new_features.append((filtered_shape, new_props, fid))

    if new_layer_name is None:
        # no new layer requested, instead add new
        # features into the same layer.
        layer['features'].extend(new_features)

        return layer

    else:
        # make a copy of the old layer's information - it
        # shouldn't matter about most of the settings, as
        # post-processing is one of the last operations.
        # but we need to override the name to ensure we get
        # some output.
        new_layer_datum = layer['layer_datum'].copy()
        new_layer_datum['name'] = new_layer_name
        new_layer = layer.copy()
        new_layer['layer_datum'] = new_layer_datum
        new_layer['features'] = new_features
        new_layer['name'] = new_layer_name

        return new_layer


def normalize_social_kind(shape, properties, fid, zoom):
    """
    Social facilities have an `amenity=social_facility` tag, but more
    information is generally available in the `social_facility=*` tag, so it
    is more informative to put that as the `kind`. We keep the old tag as
    well, for disambiguation.

    Additionally, we normalise the `social_facility:for` tag, which is a
    semi-colon delimited list, to an actual list under the `for` property.
    This should make it easier to consume.
    """

    kind = properties.get('kind')
    if kind == 'social_facility':
        tags = properties.get('tags', {})
        if tags:
            social_facility = tags.get('social_facility')
            if social_facility:
                properties['kind'] = social_facility
                # leave the original tag on for disambiguation
                properties['social_facility'] = social_facility

            # normalise the 'for' list to an actual list
            for_list = tags.get('social_facility:for')
            if for_list:
                properties['for'] = for_list.split(';')

    return (shape, properties, fid)


def normalize_medical_kind(shape, properties, fid, zoom):
    """
    Many medical practices, such as doctors and dentists, have a speciality,
    which is indicated through the `healthcare:speciality` tag. This is a
    semi-colon delimited list, so we expand it to an actual list.
    """

    kind = properties.get('kind')
    if kind in ['clinic', 'doctors', 'dentist']:
        tags = properties.get('tags', {})
        if tags:
            speciality = tags.get('healthcare:speciality')
            if speciality:
                properties['speciality'] = speciality.split(';')

    return (shape, properties, fid)


class _AnyMatcher(object):
    def match(self, other):
        return True

    def __repr__(self):
        return "*"


class _NoneMatcher(object):
    def match(self, other):
        return other is None

    def __repr__(self):
        return "-"


class _SomeMatcher(object):
    def match(self, other):
        return other is not None

    def __repr__(self):
        return "+"


class _TrueMatcher(object):
    def match(self, other):
        return other is True

    def __repr__(self):
        return "true"


class _ExactMatcher(object):
    def __init__(self, value):
        self.value = value

    def match(self, other):
        return other == self.value

    def __repr__(self):
        return repr(self.value)


class _NotEqualsMatcher(object):
    def __init__(self, value):
        self.value = value

    def match(self, other):
        return other != self.value

    def __repr__(self):
        return repr(self.value)


class _SetMatcher(object):
    def __init__(self, values):
        self.values = values

    def match(self, other):
        return other in self.values

    def __repr__(self):
        return repr(self.value)


class _GreaterThanEqualMatcher(object):
    def __init__(self, value):
        self.value = value

    def match(self, other):
        return other >= self.value

    def __repr__(self):
        return '>=%r' % self.value


class _GreaterThanMatcher(object):
    def __init__(self, value):
        self.value = value

    def match(self, other):
        return other > self.value

    def __repr__(self):
        return '>%r' % self.value


class _LessThanEqualMatcher(object):
    def __init__(self, value):
        self.value = value

    def match(self, other):
        return other <= self.value

    def __repr__(self):
        return '<=%r' % self.value


class _LessThanMatcher(object):
    def __init__(self, value):
        self.value = value

    def match(self, other):
        return other < self.value

    def __repr__(self):
        return '<%r' % self.value


_KEY_TYPE_LOOKUP = {
    'int': int,
    'float': float,
}


def _parse_kt(key_type):
    kt = key_type.split("::")

    type_key = kt[1] if len(kt) > 1 else None
    fn = _KEY_TYPE_LOOKUP.get(type_key, str)

    return (kt[0], fn)


class CSVMatcher(object):
    def __init__(self, fh):
        keys = None
        types = []
        rows = []

        self.static_any = _AnyMatcher()
        self.static_none = _NoneMatcher()
        self.static_some = _SomeMatcher()
        self.static_true = _TrueMatcher()

        # CSV - allow whitespace after the comma
        reader = csv.reader(fh, skipinitialspace=True)
        for row in reader:
            if keys is None:
                target_key = row.pop(-1)
                keys = []
                for key_type in row:
                    key, typ = _parse_kt(key_type)
                    keys.append(key)
                    types.append(typ)

            else:
                target_val = row.pop(-1)
                for i in range(0, len(row)):
                    row[i] = self._match_val(row[i], types[i])
                rows.append((row, target_val))

        self.keys = keys
        self.rows = rows
        self.target_key = target_key

    def _match_val(self, v, typ):
        if v == '*':
            return self.static_any
        if v == '-':
            return self.static_none
        if v == '+':
            return self.static_some
        if v == 'true':
            return self.static_true
        if isinstance(v, str) and ';' in v:
            return _SetMatcher(set(v.split(';')))
        if v.startswith('>='):
            assert len(v) > 2, 'Invalid >= matcher'
            return _GreaterThanEqualMatcher(typ(v[2:]))
        if v.startswith('<='):
            assert len(v) > 2, 'Invalid <= matcher'
            return _LessThanEqualMatcher(typ(v[2:]))
        if v.startswith('>'):
            assert len(v) > 1, 'Invalid > matcher'
            return _GreaterThanMatcher(typ(v[1:]))
        if v.startswith('<'):
            assert len(v) > 1, 'Invalid > matcher'
            return _LessThanMatcher(typ(v[1:]))
        if v.startswith('!'):
            assert len(v) > 1, 'Invalid ! matcher'
            return _NotEqualsMatcher(typ(v[1:]))
        return _ExactMatcher(typ(v))

    def __call__(self, shape, properties, zoom):
        vals = []
        for key in self.keys:
            # NOTE zoom and geometrytype have special meaning
            if key == 'zoom':
                val = zoom
            elif key.lower() == 'geometrytype':
                val = shape.type
            else:
                val = properties.get(key)
            vals.append(val)
        for row, target_val in self.rows:
            if all([a.match(b) for (a, b) in zip(row, vals)]):
                return (self.target_key, target_val)

        return None


class YAMLToDict(dict):
    def __init__(self, fh):
        import yaml
        data = yaml.load(fh)
        assert isinstance(data, dict)
        for k, v in data.iteritems():
            self[k] = v


def csv_match_properties(ctx):
    """
    Add or update a property on all features which match properties which are
    given as headings in a CSV file.
    """

    feature_layers = ctx.feature_layers
    zoom = ctx.nominal_zoom
    source_layer = ctx.params.get('source_layer')
    start_zoom = ctx.params.get('start_zoom', 0)
    end_zoom = ctx.params.get('end_zoom')
    target_value_type = ctx.params.get('target_value_type')
    matcher = ctx.resources.get('matcher')

    assert source_layer, 'csv_match_properties: missing source layer'
    assert matcher, 'csv_match_properties: missing matcher resource'

    if zoom < start_zoom:
        return None

    if end_zoom is not None and zoom >= end_zoom:
        return None

    layer = _find_layer(feature_layers, source_layer)
    if layer is None:
        return None

    def _type_cast(v):
        if target_value_type == 'int':
            return int(v)
        return v

    for shape, props, fid in layer['features']:
        m = matcher(shape, props, zoom)
        if m is not None:
            k, v = m
            props[k] = _type_cast(v)

    return layer


def update_parenthetical_properties(ctx):
    """
    If a feature's name ends with a set of values in parens, update
    its kind and increase the min_zoom appropriately.
    """

    feature_layers = ctx.feature_layers
    zoom = ctx.nominal_zoom
    source_layer = ctx.params.get('source_layer')
    start_zoom = ctx.params.get('start_zoom', 0)
    end_zoom = ctx.params.get('end_zoom')
    parenthetical_values = ctx.params.get('values')
    target_min_zoom = ctx.params.get('target_min_zoom')
    drop_below_zoom = ctx.params.get('drop_below_zoom')

    assert parenthetical_values is not None, \
        'update_parenthetical_properties: missing values'
    assert target_min_zoom is not None, \
        'update_parenthetical_properties: missing target_min_zoom'

    if zoom < start_zoom:
        return None

    if end_zoom is not None and zoom >= end_zoom:
        return None

    layer = _find_layer(feature_layers, source_layer)
    if layer is None:
        return None

    new_features = []
    for shape, props, fid in layer['features']:
        name = props.get('name', '')
        if not name:
            new_features.append((shape, props, fid))
            continue

        keep = True
        for value in parenthetical_values:
            if name.endswith('(%s)' % value):
                props['kind'] = value
                props['min_zoom'] = target_min_zoom
                if drop_below_zoom and zoom < drop_below_zoom:
                    keep = False
        if keep:
            new_features.append((shape, props, fid))

    layer['features'] = new_features
    return layer


def height_to_meters(shape, props, fid, zoom):
    """
    If the properties has a "height" entry, then convert that to meters.
    """

    height = props.get('height')
    if not height:
        return shape, props, fid

    props['height'] = _to_float_meters(height)
    return shape, props, fid


def elevation_to_meters(shape, props, fid, zoom):
    """
    If the properties has an "elevation" entry, then convert that to meters.
    """

    elevation = props.get('elevation')
    if not elevation:
        return shape, props, fid

    props['elevation'] = _to_float_meters(elevation)
    return shape, props, fid


def normalize_cycleway(shape, props, fid, zoom):
    """
    If the properties contain both a cycleway:left and cycleway:right
    with the same values, those should be removed and replaced with a
    single cycleway property. Additionally, if a cycleway_both tag is
    present, normalize that to the cycleway tag.
    """
    cycleway = props.get('cycleway')
    cycleway_left = props.get('cycleway_left')
    cycleway_right = props.get('cycleway_right')

    cycleway_both = props.pop('cycleway_both', None)
    if cycleway_both and not cycleway:
        props['cycleway'] = cycleway = cycleway_both

    if (cycleway_left and cycleway_right and
            cycleway_left == cycleway_right and
            (not cycleway or cycleway_left == cycleway)):
        props['cycleway'] = cycleway_left
        del props['cycleway_left']
        del props['cycleway_right']
    return shape, props, fid


def add_is_bicycle_related(shape, props, fid, zoom):
    """
    If the props contain a bicycle_network tag, cycleway, or
    highway=cycleway, it should have an is_bicycle_related
    boolean. Depends on the normalize_cycleway transform to have been
    run first.
    """
    props.pop('is_bicycle_related', None)
    if ('bicycle_network' in props or
            'cycleway' in props or
            'cycleway_left' in props or
            'cycleway_right' in props or
            props.get('bicycle') in ('yes', 'designated') or
            props.get('ramp_bicycle') in ('yes', 'left', 'right') or
            props.get('kind_detail') == 'cycleway'):
        props['is_bicycle_related'] = True
    return shape, props, fid


def drop_properties_with_prefix(ctx):
    """
    Iterate through all features, dropping all properties that start
    with prefix.
    """

    prefix = ctx.params.get('prefix')
    assert prefix, 'drop_properties_with_prefix: missing prefix param'

    feature_layers = ctx.feature_layers
    for feature_layer in feature_layers:
        for shape, props, fid in feature_layer['features']:
            for k in props.keys():
                if k.startswith(prefix):
                    del props[k]


def drop_features_mz_min_pixels(ctx):
    """
    Drop all features that have a mz_min_pixels set whose area doesn't
    meet the threshold.
    """
    source_layers = ctx.params.get('source_layers')
    assert source_layers, 'drop_features_mz_min_pixels: missing source_layers'
    source_layer_names = set(source_layers)  # set to speed up lookups

    prop_name = ctx.params.get('property')
    assert prop_name, 'drop_features_mz_min_pixels: missing property'

    meters_per_pixel_area = calc_meters_per_pixel_area(ctx.nominal_zoom)

    feature_layers = ctx.feature_layers
    for source_layer_name in source_layer_names:
        for feature_layer in feature_layers:
            if feature_layer['name'] not in source_layer_names:
                continue

            features_to_keep = []
            for feature in feature_layer['features']:
                shape, props, fid = feature
                pixel_threshold = props.get(prop_name)
                if pixel_threshold is None:
                    features_to_keep.append(feature)
                    continue

                assert isinstance(pixel_threshold, Number)

                if shape.type not in ('Polygon', 'MultiPolygon'):
                    features_to_keep.append(feature)
                    continue

                area_threshold = meters_per_pixel_area * pixel_threshold
                area = props.get('area')
                if area is None:
                    area = shape.area
                else:
                    assert isinstance(area, Number)

                if area >= area_threshold:
                    features_to_keep.append(feature)

            feature_layer['features'] = features_to_keep


def _drop_small_inners(poly, area_tolerance):
    ext = poly.exterior

    inners = []
    for inner in poly.interiors:
        area = Polygon(inner).area
        if area >= area_tolerance:
            inners.append(inner)

    return Polygon(ext, inners)


def drop_small_inners(ctx):
    """
    Drop inners which are smaller than the given scale.
    """

    zoom = ctx.nominal_zoom
    start_zoom = ctx.params.get('start_zoom', 0)
    end_zoom = ctx.params.get('end_zoom')
    pixel_area = ctx.params.get('pixel_area')
    source_layers = ctx.params.get('source_layers')

    assert source_layers, \
        "You must provide source_layers (layer names) to drop_small_inners"
    assert pixel_area, \
        "You must provide a pixel_area parameter to drop_small_inners"

    if zoom < start_zoom:
        return None

    if end_zoom and zoom >= end_zoom:
        return None

    meters_per_pixel_area = calc_meters_per_pixel_area(zoom)
    area_tolerance = meters_per_pixel_area * pixel_area

    for layer in ctx.feature_layers:
        layer_datum = layer['layer_datum']
        layer_name = layer_datum['name']

        if layer_name not in source_layers:
            continue

        new_features = []
        for feature in layer['features']:
            shape, props, fid = feature

            geom_type = shape.geom_type

            if geom_type == 'Polygon':
                new_shape = _drop_small_inners(shape, area_tolerance)
                if not new_shape.is_empty:
                    new_features.append((new_shape, props, fid))

            elif geom_type == 'MultiPolygon':
                polys = []
                for g in shape.geoms:
                    new_g = _drop_small_inners(g, area_tolerance)
                    if not new_g.is_empty:
                        polys.append(new_g)
                if polys:
                    new_features.append((MultiPolygon(polys), props, fid))

            else:
                new_features.append(feature)

        layer['features'] = new_features


def simplify_layer(ctx):
    feature_layers = ctx.feature_layers
    zoom = ctx.nominal_zoom
    source_layer = ctx.params.get('source_layer')
    assert source_layer, 'simplify_layer: missing source layer'
    tolerance = ctx.params.get('tolerance', 1.0)
    start_zoom = ctx.params.get('start_zoom', 0)
    end_zoom = ctx.params.get('end_zoom')

    if zoom < start_zoom:
        return None

    if end_zoom is not None and zoom >= end_zoom:
        return None

    layer = _find_layer(feature_layers, source_layer)
    if layer is None:
        return None

    # adjust tolerance to be in coordinate units
    tolerance = tolerance * tolerance_for_zoom(zoom)

    new_features = []
    for (shape, props, fid) in layer['features']:
        simplified_shape = shape.simplify(tolerance,
                                          preserve_topology=True)
        shape = _make_valid_if_necessary(simplified_shape)
        new_features.append((shape, props, fid))

    layer['features'] = new_features
    return layer


def simplify_and_clip(ctx):
    """simplify geometries according to zoom level and clip"""

    zoom = ctx.nominal_zoom
    simplify_before = ctx.params.get('simplify_before')

    assert simplify_before, 'simplify_and_clip: missing simplify_before param'

    meters_per_pixel_area = calc_meters_per_pixel_area(zoom)

    tolerance = tolerance_for_zoom(zoom)

    for feature_layer in ctx.feature_layers:
        simplified_features = []

        layer_datum = feature_layer['layer_datum']
        is_clipped = layer_datum['is_clipped']
        clip_factor = layer_datum.get('clip_factor', 1.0)

        padded_bounds = feature_layer['padded_bounds']
        area_threshold_pixels = layer_datum['area_threshold']
        area_threshold_meters = meters_per_pixel_area * area_threshold_pixels
        layer_tolerance = layer_datum.get('tolerance', 1.0) * tolerance

        # The logic behind simplifying before intersecting rather than the
        # other way around is extensively explained here:
        # https://github.com/mapzen/TileStache/blob/d52e54975f6ec2d11f63db13934047e7cd5fe588/TileStache/Goodies/VecTiles/server.py#L509,L527
        simplify_before_intersect = layer_datum['simplify_before_intersect']

        # perform any simplification as necessary
        simplify_start = layer_datum['simplify_start']
        should_simplify = simplify_start <= zoom < simplify_before

        for shape, props, feature_id in feature_layer['features']:

            geom_type = normalize_geometry_type(shape.type)
            original_geom_dim = _geom_dimensions(shape)
            padded_bounds_by_type = padded_bounds[geom_type]
            layer_padded_bounds = calculate_padded_bounds(
                clip_factor, padded_bounds_by_type)

            if should_simplify and simplify_before_intersect:
                # To reduce the performance hit of simplifying potentially huge
                # geometries to extract only a small portion of them when
                # cutting out the actual tile, we cut out a slightly larger
                # bounding box first. See here for an explanation:
                # https://github.com/mapzen/TileStache/blob/d52e54975f6ec2d11f63db13934047e7cd5fe588/TileStache/Goodies/VecTiles/server.py#L509,L527

                min_x, min_y, max_x, max_y = layer_padded_bounds.bounds
                gutter_bbox_size = (max_x - min_x) * 0.1
                gutter_bbox = Box(
                    min_x - gutter_bbox_size,
                    min_y - gutter_bbox_size,
                    max_x + gutter_bbox_size,
                    max_y + gutter_bbox_size)
                clipped_shape = shape.intersection(gutter_bbox)
                simplified_shape = clipped_shape.simplify(
                    layer_tolerance, preserve_topology=True)
                shape = _make_valid_if_necessary(simplified_shape)

            if is_clipped:
                shape = shape.intersection(layer_padded_bounds)

            if should_simplify and not simplify_before_intersect:
                simplified_shape = shape.simplify(layer_tolerance,
                                                  preserve_topology=True)
                shape = _make_valid_if_necessary(simplified_shape)

            # this could alter multipolygon geometries
            if zoom < simplify_before:
                shape = _visible_shape(shape, area_threshold_meters)

            # don't keep features which have been simplified to empty or
            # None.
            if shape is None or shape.is_empty:
                continue

            # if clipping and simplifying caused this to become a geometry
            # collection of different geometry types (e.g: by just touching
            # the clipping box), then trim it back to the original geometry
            # type.
            if shape.type == 'GeometryCollection':
                shape = _filter_geom_types(shape, original_geom_dim)
                # if that removed all the geometry, then don't keep the
                # feature.
                if shape is None or shape.is_empty:
                    continue

            simplified_feature = shape, props, feature_id
            simplified_features.append(simplified_feature)

        feature_layer['features'] = simplified_features


_lookup_operator_rules = {
                        'United States National Park Service': (
                            'National Park Service',
                            'US National Park Service',
                            'U.S. National Park Service',
                            'US National Park service'),
                        'United States Forest Service': (
                            'US Forest Service',
                            'U.S. Forest Service',
                            'USDA Forest Service',
                            'United States Department of Agriculture',
                            'US National Forest Service',
                            'United State Forest Service',
                            'U.S. National Forest Service'),
                        'National Parks & Wildife Service NSW': (
                            'Department of National Parks NSW',
                            'Dept of NSW National Parks',
                            'Dept of National Parks NSW',
                            'Department of National Parks NSW',
                            'NSW National Parks',
                            'NSW National Parks & Wildlife Service',
                            'NSW National Parks and Wildlife Service',
                            'NSW Parks and Wildlife Service',
                            'NSW Parks and Wildlife Service (NPWS)',
                            'National Parks and Wildlife NSW',
                            'National Parks and Wildlife Service NSW')}

normalized_operator_lookup = {}
for normalized_operator, variants in _lookup_operator_rules.items():
    for variant in variants:
        normalized_operator_lookup[variant] = normalized_operator


def normalize_operator_values(shape, properties, fid, zoom):
    """
    There are many operator-related tags, including 'National Park Service',
    'U.S. National Park Service', 'US National Park Service' etc that refer
    to the same operator tag. This function promotes a normalized value
    for all alternatives in specific operator values.

    See https://github.com/tilezen/vector-datasource/issues/927.
    """

    operator = properties.get('operator', None)

    if operator is not None:
        normalized_operator = normalized_operator_lookup.get(operator, None)
        if normalized_operator:
            properties['operator'] = normalized_operator
            return (shape, properties, fid)

    return (shape, properties, fid)


def _guess_type_from_network(network):
    """
    Return a best guess of the type of network (road, hiking, bus, bicycle)
    from the network tag itself.
    """

    if network in ['iwn', 'nwn', 'rwn', 'lwn']:
        return 'hiking'

    elif network in ['icn', 'ncn', 'rcn', 'lcn']:
        return 'bicycle'

    else:
        # hack for now - how can we tell bus routes from road routes?
        # it seems all bus routes are relations, where we have a route type
        # given, so this should default to roads.
        return 'road'


# a mapping of operator tag values to the networks that they are (probably)
# part of. this would be better specified directly on the data, but sometimes
# it's just not available.
#
# this is a list of the operators with >=100 uses on ways tagged as motorways,
# which should hopefully allow us to catch most of the important ones. they're
# mapped to the country they're in, which should be enough in most cases to
# render the appropriate shield.
_NETWORK_OPERATORS = {
    'Highways England': 'GB',
    'ASF': 'FR',
    'Autopista Litoral Sul': 'BR',
    'DNIT': 'BR',
    'Εγνατία Οδός': 'GR',
    'Αυτοκινητόδρομος Αιγαίου': 'GR',
    'Transport Scotland': 'GB',
    'The Danish Road Directorate': 'DK',
    "Autostrade per l' Italia S.P.A.": 'IT',
    'Νέα Οδός': 'GR',
    'Autostrada dei Fiori S.P.A.': 'IT',
    'S.A.L.T.': 'IT',
    'Welsh Government': 'GB',
    'Euroscut': 'PT',
    'DIRIF': 'FR',
    'Administración central': 'ES',
    'Αττική Οδός': 'GR',
    'Autocamionale della Cisa S.P.A.': 'IT',
    'Κεντρική Οδός': 'GR',
    'Bundesrepublik Deutschland': 'DE',
    'Ecovias': 'BR',
    '東日本高速道路': 'JP',
    'NovaDutra': 'BR',
    'APRR': 'FR',
    'Via Solutions Südwest': 'DE',
    'Autoroutes du Sud de la France': 'FR',
    'Transport for Scotland': 'GB',
    'Departamento de Infraestructuras Viarias y Movilidad': 'ES',
    'ViaRondon': 'BR',
    'DIRNO': 'FR',
    'SATAP': 'IT',
    'Ολυμπία Οδός': 'GR',
    'Midland Expressway Ltd': 'GB',
    'autobahnplus A8 GmbH': 'DE',
    'Cart': 'BR',
    'Μορέας': 'GR',
    'Hyderabad Metropolitan Development Authority': 'PK',
    'Viapar': 'BR',
    'Autostrade Centropadane': 'IT',
    'Triângulo do Sol': 'BR',
}


def _ref_importance(ref):
    try:
        # first, see if the reference is a number, or easily convertible
        # into one.
        ref = int(ref or 0)
    except ValueError:
        # if not, we can try to extract anything that looks like a sequence
        # of digits from the ref.
        m = _ANY_NUMBER.match(ref)
        if m:
            ref = int(m.group(1))
        else:
            # failing that, we assume that a completely non-numeric ref is
            # a name, which would make it quite important.
            ref = 0

    # make sure no ref is negative
    ref = abs(ref)

    return ref


def _guess_network_gb(tags):
    # for roads we put the original OSM highway tag value in kind_detail, so we
    # can recover it here.
    highway = tags.get('kind_detail')

    ref = tags.get('ref', '')
    networks = []
    # although roads are part of only one network in the UK, some roads are
    # tagged incorrectly as being part of two, so we have to handle this case.
    for part in ref.split(';'):
        if not part:
            continue

        # letter at the start of the ref indicates the road class. generally
        # one of 'M', 'A', or 'B' - although other letters exist, they are
        # rarely used.
        letter, number = _splitref(part)

        # UK is tagged a bit weirdly, using the highway tag value in addition
        # to the ref to figure out which road class should be applied. the
        # following is not applied strictly, but is a "best guess" at the
        # appropriate signage colour.
        #
        # https://wiki.openstreetmap.org/wiki/United_Kingdom_Tagging_Guidelines
        if letter == 'M' and highway == 'motorway':
            networks.append(('GB:M-road', 'M' + number))

        elif ref.endswith('(M)') and highway == 'motorway':
            networks.append(('GB:M-road', 'A' + number))

        elif letter == 'A' and highway == 'trunk':
            networks.append(('GB:A-road-green', 'A' + number))

        elif letter == 'A' and highway == 'primary':
            networks.append(('GB:A-road-white', 'A' + number))

        elif letter == 'B' and highway == 'secondary':
            networks.append(('GB:B-road', 'B' + number))

    return networks


def _guess_network_ar(tags):
    ref = tags.get('ref')
    if ref is None:
        return None
    elif ref.startswith('RN'):
        return [('AR:national', ref)]
    elif ref.startswith('RP'):
        return [('AR:provincial', ref)]
    return None


def _guess_network_with(tags, fn):
    """
    Common function for backfilling (network, ref) pairs by running the
    "normalize" function on the parts of the ref. For example, if the
    ref was 'A1;B2;C3', then the normalize function would be run on
    fn(None, 'A1'), fn(None, 'B2'), etc...

    This allows us to back-fill the network where it can be deduced from
    the ref in a particular country (e.g: if all motorways are A[0-9]).
    """

    ref = tags.get('ref', '')
    networks = []
    for part in ref.split(';'):
        part = part.strip()
        if not part:
            continue
        network, ref = fn(None, part)
        networks.append((network, part))
    return networks


def _guess_network_au(tags):
    return _guess_network_with(tags, _normalize_au_netref)


# list of all the state codes in Brazil, see
# https://en.wikipedia.org/wiki/ISO_3166-2:BR
_BR_STATES = set([
    'DF',  # Distrito Federal (federal district, not really a state)
    'AC',  # Acre
    'AL',  # Alagoas
    'AP',  # Amapá
    'AM',  # Amazonas
    'BA',  # Bahia
    'CE',  # Ceará
    'ES',  # Espírito Santo
    'GO',  # Goiás
    'MA',  # Maranhão
    'MT',  # Mato Grosso
    'MS',  # Mato Grosso do Sul
    'MG',  # Minas Gerais
    'PA',  # Pará
    'PB',  # Paraíba
    'PR',  # Paraná
    'PE',  # Pernambuco
    'PI',  # Piauí
    'RJ',  # Rio de Janeiro
    'RN',  # Rio Grande do Norte
    'RS',  # Rio Grande do Sul
    'RO',  # Rondônia
    'RR',  # Roraima
    'SC',  # Santa Catarina
    'SP',  # São Paulo
    'SE',  # Sergipe
    'TO',  # Tocantins
])


# additional road types
_BR_NETWORK_EXPANSION = {
    # Minas Gerais state roads
    'AMG': 'BR:MG',
    'LMG': 'BR:MG:local',
    'MGC': 'BR:MG',
    # CMG seems to be coupled with BR- roads of the same number
    'CMG': 'BR:MG',

    # Rio Grande do Sul state roads
    'ERS': 'BR:RS',
    'VRS': 'BR:RS',
    'RSC': 'BR:RS',

    # access roads in São Paulo?
    'SPA': 'BR:SP',

    # connecting roads in Paraná?
    'PRC': 'BR:PR',

    # municipal roads in Paulínia
    'PLN': 'BR:SP:PLN',

    # municipal roads in São Carlos
    # https://pt.wikipedia.org/wiki/Estradas_do_munic%C3%ADpio_de_S%C3%A3o_Carlos#Identifica%C3%A7%C3%A3o
    'SCA': 'BR:SP:SCA',
}


def _guess_network_br(tags):
    ref = tags.get('ref')
    networks = []

    # a missing or blank ref isn't going to give us much information
    if not ref:
        return networks

    # track last prefix, so that we can handle cases where the ref is written
    # as "BR-XXX/YYY" to mean "BR-XXX; BR-YYY".
    last_prefix = None

    for prefix, num in re.findall('([A-Za-z]+)?[- ]?([0-9]+)', ref):
        # if there's a prefix, save it for potential later use. if there isn't
        # then use the previous one - if any.
        if prefix:
            last_prefix = prefix
        else:
            prefix = last_prefix

        # make sure the prefix is from a network that we know about.
        if prefix == 'BR':
            network = prefix

        elif prefix in _BR_STATES:
            network = 'BR:' + prefix

        elif prefix in _BR_NETWORK_EXPANSION:
            network = _BR_NETWORK_EXPANSION[prefix]

        else:
            continue

        networks.append((network, '%s-%s' % (prefix, num)))

    return networks


def _guess_network_ca(tags):
    nat_name = tags.get('nat_name:en') or tags.get('nat_name')
    ref = tags.get('ref')
    network = tags.get('network')

    networks = []

    if network and ref:
        networks.append((network, ref))

    if nat_name and nat_name.lower() == 'trans-canada highway':
        # note: no ref for TCH. some states appear to add route numbers from
        # the state highway to the TCH shields, e.g:
        # https://commons.wikimedia.org/wiki/File:TCH-16_(BC).svg
        networks.append(('CA:transcanada', ref))

    if not networks and ref:
        # final fallback - all we know is that this is a road in Canada.
        networks.append(('CA', ref))

    return networks


def _guess_network_ch(tags):
    ref = tags.get('ref', '')
    networks = []
    for part in ref.split(';'):
        if not part:
            continue
        network, ref = _normalize_ch_netref(None, part)
        if network or ref:
            networks.append((network, ref))
    return networks


def _guess_network_cn(tags):
    return _guess_network_with(tags, _normalize_cn_netref)


def _guess_network_es(tags):
    return _guess_network_with(tags, _normalize_es_netref)


def _guess_network_fr(tags):
    return _guess_network_with(tags, _normalize_fr_netref)


def _guess_network_de(tags):
    return _guess_network_with(tags, _normalize_de_netref)


def _guess_network_ga(tags):
    return _guess_network_with(tags, _normalize_ga_netref)


def _guess_network_gr(tags):
    ref = tags.get('ref', '')
    networks = []
    for part in ref.split(';'):
        if not part:
            continue

        # ignore provincial refs, they should be on reg_ref. see:
        # https://wiki.openstreetmap.org/wiki/WikiProject_Greece/Provincial_Road_Network
        if part.startswith(u'ΕΠ'.encode('utf-8')):
            continue

        network, ref = _normalize_gr_netref(None, part)
        networks.append((network, part))
    return networks


def _guess_network_in(tags):
    ref = tags.get('ref', '')
    networks = []
    for part in ref.split(';'):
        if not part:
            continue
        network, ref = _normalize_in_netref(None, part)
        # note: we return _ref_ here, as normalize_in_netref might have changed
        # the ref part (e.g: in order to split MDR54 into (network=MDR, ref=54)
        networks.append((network, ref))
    return networks


def _guess_network_mx(tags):
    return _guess_network_with(tags, _normalize_mx_netref)


def _guess_network_my(tags):
    return _guess_network_with(tags, _normalize_my_netref)


def _guess_network_no(tags):
    return _guess_network_with(tags, _normalize_no_netref)


def _guess_network_pe(tags):
    return _guess_network_with(tags, _normalize_pe_netref)


def _guess_network_jp(tags):
    ref = tags.get('ref', '')

    name = tags.get('name:ja') or tags.get('name')
    network_from_name = None
    if name:
        if isinstance(name, str):
            name = unicode(name, 'utf-8')
        if name.startswith(u'国道') and \
           name.endswith(u'号'):
            network_from_name = 'JP:national'

    networks = []
    for part in ref.split(';'):
        if not part:
            continue
        network, ref = _normalize_jp_netref(None, part)

        if network is None and network_from_name is not None:
            network = network_from_name

        if network and part:
            networks.append((network, part))

    return networks


def _guess_network_kr(tags):
    ref = tags.get('ref', '')
    network_from_tags = tags.get('network')

    # the name often ends with a word which appears to mean expressway or
    # national road.
    name_ko = _make_unicode_or_none(tags.get('name:ko') or tags.get('name'))
    if name_ko and network_from_tags is None:
        if name_ko.endswith(u'국도'):
            # national roads - gukdo
            network_from_tags = 'KR:national'

        elif name_ko.endswith(u'광역시도로'):
            # metropolitan city roads - gwangyeoksido
            network_from_tags = 'KR:metropolitan'

        elif name_ko.endswith(u'특별시도'):
            # special city (Seoul) roads - teukbyeolsido
            network_from_tags = 'KR:metropolitan'

        elif (name_ko.endswith(u'고속도로') or
              name_ko.endswith(u'고속도로지선')):
            # expressways - gosokdoro (and expressway branches)
            network_from_tags = 'KR:expressway'

        elif name_ko.endswith(u'지방도'):
            # local highways - jibangdo
            network_from_tags = 'KR:local'

    networks = []
    for part in ref.split(';'):
        if not part:
            continue
        network, ref = _normalize_kr_netref(None, part)

        if network is None and network_from_tags is not None:
            network = network_from_tags

        if network and part:
            networks.append((network, part))

    return networks


def _guess_network_pl(tags):
    return _guess_network_with(tags, _normalize_pl_netref)


def _guess_network_pt(tags):
    return _guess_network_with(tags, _normalize_pt_netref)


def _guess_network_ro(tags):
    return _guess_network_with(tags, _normalize_ro_netref)


def _guess_network_ru(tags):
    ref = tags.get('ref', '')
    network = tags.get('network')
    networks = []

    for part in ref.split(';'):
        if not part:
            continue
        # note: we pass in the network tag, as that can be important for
        # disambiguating Russian refs.
        network, ref = _normalize_ru_netref(network, part)
        networks.append((network, part))

    return networks


def _guess_network_sg(tags):
    return _guess_network_with(tags, _normalize_sg_netref)


def _guess_network_tr(tags):
    ref = tags.get('ref', '')
    networks = []

    for part in _COMMON_SEPARATORS.split(ref):
        part = part.strip()
        if not part:
            continue
        network, ref = _normalize_tr_netref(None, part)
        if network or ref:
            networks.append((network, ref))

    return networks


def _guess_network_ua(tags):
    return _guess_network_with(tags, _normalize_ua_netref)


_COMMON_SEPARATORS = re.compile('[;,/,]')


def _guess_network_vn(tags):
    ref = tags.get('ref', '')

    # some bare refs can be augmented from the network tag on the way, or
    # guessed from the name, which often starts with the type of the road.
    network_from_tags = tags.get('network')
    if not network_from_tags:
        name = tags.get('name') or tags.get('name:vi')
        if name:
            name = unicode(name, 'utf-8')
            if name.startswith(u'Tỉnh lộ'):
                network_from_tags = 'VN:provincial'
            elif name.startswith(u'Quốc lộ'):
                network_from_tags = 'VN:national'

    networks = []
    for part in _COMMON_SEPARATORS.split(ref):
        if not part:
            continue
        network, ref = _normalize_vn_netref(network_from_tags, part)
        if network or ref:
            networks.append((network, ref))

    return networks


def _guess_network_za(tags):
    ref = tags.get('ref', '')
    networks = []

    for part in _COMMON_SEPARATORS.split(ref):
        if not part:
            continue
        network, ref = _normalize_za_netref(tags.get('network'), part)
        networks.append((network, part))

    return networks


def _do_not_backfill(tags):
    return None


def _sort_network_us(network, ref):
    if network is None:
        network_code = 9999
    elif network == 'US:I':
        network_code = 1
    elif network == 'US:US':
        network_code = 2
    else:
        network_code = len(network.split(':')) + 3

    ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


_AU_NETWORK_IMPORTANCE = {
    'N-highway': 0,
    'A-road': 1,
    'M-road': 2,
    'B-road': 3,
    'C-road': 4,
    'N-route': 5,
    'S-route': 6,
    'Metro-road': 7,
    'T-drive': 8,
    'R-route': 9,
}


def _sort_network_au(network, ref):
    if network is None or \
       not network.startswith('AU:'):
        network_code = 9999
    else:
        network_code = _AU_NETWORK_IMPORTANCE.get(network[3:], 9999)

    ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_br(network, ref):
    if network is None:
        network_code = 9999
    elif network == 'BR:Trans-Amazonian':
        network_code = 0
    else:
        network_code = len(network.split(':')) + 1

    ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_ca(network, ref):
    if network is None:
        network_code = 9999
    elif network == 'CA:transcanada':
        network_code = 0
    elif network == 'CA:yellowhead':
        network_code = 1
    else:
        network_code = len(network.split(':')) + 2

    ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_ch(network, ref):
    if network is None:
        network_code = 9999
    elif network == 'CH:national':
        network_code = 0
    elif network == 'CH:regional':
        network_code = 1
    elif network == 'e-road':
        network_code = 99
    else:
        network_code = len(network.split(':')) + 2

    ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_cn(network, ref):
    if network is None:
        network_code = 9999
    elif network == 'CN:expressway':
        network_code = 0
    elif network == 'CN:expressway:regional':
        network_code = 1
    elif network == 'CN:JX':
        network_code = 2
    elif network == 'AsianHighway':
        network_code = 99
    else:
        network_code = len(network.split(':')) + 3

    ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_es(network, ref):
    if network is None:
        network_code = 9999
    elif network == 'ES:A-road':
        network_code = 0
    elif network == 'ES:N-road':
        network_code = 1
    elif network == 'ES:autonoma':
        network_code = 2
    elif network == 'ES:province':
        network_code = 3
    elif network == 'ES:city':
        network_code = 4
    elif network == 'e-road':
        network_code = 99
    else:
        network_code = 5 + len(network.split(':'))

    ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_fr(network, ref):
    if network is None:
        network_code = 9999
    elif network == 'FR:A-road':
        network_code = 0
    elif network == 'FR:N-road':
        network_code = 1
    elif network == 'FR:D-road':
        network_code = 2
    elif network == 'FR':
        network_code = 3
    elif network == 'e-road':
        network_code = 99
    else:
        network_code = 5 + len(network.split(':'))

    ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_de(network, ref):
    if network is None:
        network_code = 9999
    elif network == 'DE:BAB':
        network_code = 0
    elif network == 'DE:BS':
        network_code = 1
    elif network == 'DE:LS':
        network_code = 2
    elif network == 'DE:KS':
        network_code = 3
    elif network == 'DE:STS':
        network_code = 4
    elif network == 'DE:Hamburg:Ring':
        network_code = 5
    elif network == 'e-road':
        network_code = 99
    else:
        network_code = len(network.split(':')) + 6

    ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_ga(network, ref):
    if network is None:
        network_code = 9999
    elif network == 'GA:national':
        network_code = 0
    elif network == 'GA:L-road':
        network_code = 1
    else:
        network_code = 2 + len(network.split(':'))

    ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_gr(network, ref):
    if network is None:
        network_code = 9999
    elif network == 'GR:motorway':
        network_code = 0
    elif network == 'GR:national':
        network_code = 1
    elif network == 'e-road':
        network_code = 99
    else:
        network_code = len(network.split(':')) + 3

    ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_in(network, ref):
    if network is None:
        network_code = 9999
    elif network == 'IN:NH':
        network_code = 0
    elif network == 'IN:SH':
        network_code = 1
    elif network == 'IN:MDR':
        network_code = 2
    else:
        network_code = len(network.split(':')) + 3

    ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_ir(network, ref):
    if network is None:
        network_code = 9999
    elif network == 'AsianHighway':
        network_code = 99
    else:
        network_code = len(network.split(':'))

    ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_kz(network, ref):
    if network is None:
        network_code = 9999
    elif network == 'KZ:national':
        network_code = 0
    elif network == 'KZ:regional':
        network_code = 1
    elif network == 'e-road':
        network_code = 99
    elif network == 'AsianHighway':
        network_code = 99
    else:
        network_code = 2 + len(network.split(':'))

    ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_la(network, ref):
    if network is None:
        network_code = 9999
    elif network == 'LA:national':
        network_code = 0
    elif network == 'AsianHighway':
        network_code = 99
    else:
        network_code = 1 + len(network.split(':'))

    ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_mx(network, ref):
    if network is None:
        network_code = 9999
    elif network == 'MX:MEX':
        network_code = 0
    else:
        network_code = len(network.split(':')) + 1

    ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_my(network, ref):
    if network is None:
        network_code = 9999
    elif network == 'MY:federal':
        network_code = 0
    elif network == 'MY:expressway':
        network_code = 1
    elif network == 'AsianHighway':
        network_code = 99
    else:
        network_code = len(network.split(':')) + 2

    ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_no(network, ref):
    if network is None:
        network_code = 9999
    elif network == 'NO:oslo:ring':
        network_code = 0
    elif network == 'e-road':
        network_code = 1
    elif network == 'NO:Riksvei':
        network_code = 2
    elif network == 'NO:Fylkesvei':
        network_code = 3
    else:
        network_code = len(network.split(':')) + 4

    ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_gb(network, ref):
    if network is None:
        network_code = 9999
    elif network == 'GB:M-road':
        network_code = 0
    elif network == 'GB:A-road-green':
        network_code = 1
    elif network == 'GB:A-road-white':
        network_code = 2
    elif network == 'GB:B-road':
        network_code = 3
    elif network == 'e-road':
        network_code = 99
    else:
        network_code = len(network.split(':')) + 4

    ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_pl(network, ref):
    if network is None:
        network_code = 9999
    elif network == 'PL:motorway':
        network_code = 0
    elif network == 'PL:expressway':
        network_code = 1
    elif network == 'PL:national':
        network_code = 2
    elif network == 'e-road':
        network_code = 99
    else:
        network_code = len(network.split(':')) + 3

    ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_pt(network, ref):
    if network is None:
        network_code = 9999
    elif network == 'PT:motorway':
        network_code = 0
    elif network == 'PT:primary':
        network_code = 1
    elif network == 'PT:secondary':
        network_code = 2
    elif network == 'PT:national':
        network_code = 3
    elif network == 'PT:rapid':
        network_code = 4
    elif network == 'PT:express':
        network_code = 5
    elif network == 'PT:regional':
        network_code = 6
    elif network == 'PT:municipal':
        network_code = 7
    elif network == 'e-road':
        network_code = 99
    else:
        network_code = len(network.split(':')) + 8

    ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_ro(network, ref):
    if network is None:
        network_code = 9999
    elif network == 'RO:motorway':
        network_code = 0
    elif network == 'RO:national':
        network_code = 1
    elif network == 'RO:county':
        network_code = 2
    elif network == 'RO:local':
        network_code = 3
    elif network == 'e-road':
        network_code = 99
    else:
        network_code = len(network.split(':')) + 4

    ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_ru(network, ref):
    ref = _make_unicode_or_none(ref)

    if network is None:
        network_code = 9999
    elif network == 'RU:national' and ref:
        if ref.startswith(u'М'):
            network_code = 0
        elif ref.startswith(u'Р'):
            network_code = 1
        elif ref.startswith(u'А'):
            network_code = 2
        else:
            network_code = 9999
    elif network == 'RU:regional':
        network_code = 3
    elif network == 'e-road':
        network_code = 99
    elif network == 'AsianHighway':
        network_code = 99
    else:
        network_code = len(network.split(':')) + 4

    if ref is None:
        ref = 9999
    else:
        ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_tr(network, ref):
    ref = _make_unicode_or_none(ref)

    if network is None:
        network_code = 9999
    elif network == 'TR:motorway':
        network_code = 0
    elif network == 'TR:highway':
        # some highways are "main highways", so it makes sense to show them
        # before regular other highways.
        # see footer of https://en.wikipedia.org/wiki/State_road_D.010_(Turkey)
        if ref in ('D010', 'D100', 'D200', 'D300', 'D400',
                   'D550', 'D650', 'D750', 'D850', 'D950'):
            network_code = 1
        else:
            network_code = 2
    elif network == 'TR:provincial':
        network_code = 3
    elif network == 'e-road':
        network_code = 99
    elif network == 'AsianHighway':
        network_code = 99
    else:
        network_code = len(network.split(':')) + 4

    if ref is None:
        ref = 9999
    else:
        ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_ua(network, ref):
    ref = _make_unicode_or_none(ref)

    if network is None:
        network_code = 9999
    elif network == 'UA:international':
        network_code = 0
    elif network == 'UA:national':
        network_code = 1
    elif network == 'UA:regional':
        network_code = 2
    elif network == 'UA:territorial':
        network_code = 3
    elif network == 'e-road':
        network_code = 99
    else:
        network_code = len(network.split(':')) + 4

    if ref is None:
        ref = 9999
    else:
        ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_vn(network, ref):
    if network is None:
        network_code = 9999
    elif network == 'VN:expressway':
        network_code = 0
    elif network == 'VN:national':
        network_code = 1
    elif network == 'VN:provincial':
        network_code = 2
    elif network == 'VN:road':
        network_code = 3
    elif network == 'AsianHighway':
        network_code = 99
    else:
        network_code = len(network.split(':')) + 4

    if ref is None:
        ref = 9999
    else:
        ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


def _sort_network_za(network, ref):
    if network is None:
        network_code = 9999
    elif network == 'ZA:national':
        network_code = 0
    elif network == 'ZA:provincial':
        network_code = 1
    elif network == 'ZA:regional':
        network_code = 2
    elif network == 'ZA:metropolitan':
        network_code = 3
    elif network == 'ZA:kruger':
        network_code = 4
    elif network == 'ZA:S-road':
        network_code = 5
    else:
        network_code = len(network.split(':')) + 6

    if ref is None:
        ref = 9999
    else:
        ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


_AU_NETWORK_EXPANSION = {
    'A': 'AU:A-road',
    'M': 'AU:M-road',
    'B': 'AU:B-road',
    'C': 'AU:C-road',
    'N': 'AU:N-route',
    'R': 'AU:R-route',
    'S': 'AU:S-route',
    'T': 'AU:T-drive',
    'MR': 'AU:Metro-road',
}


def _splitref(ref):
    """
    Split ref into a leading alphabetic part and a trailing (possibly numeric)
    part.
    """

    # empty strings don't have a prefix
    if not ref:
        return None, ref

    for i in xrange(0, len(ref)):
        if not ref[i].isalpha():
            return ref[0:i], ref[i:].strip()

    # got to the end, must be all "prefix", which probably indicates it's not
    # a ref of the expected prefix-suffix form, and we should just return the
    # ref without a prefix.
    return None, ref


def _normalize_au_netref(network, ref):
    """
    Take the network and ref of an Australian road and normalise them so that
    the network is in the form 'AU:road-type' and the ref is numeric. This is
    based on a bunch of logic about what kinds of Australian roads exist.

    Returns new (network, ref) values.
    """

    # grab the prefix, if any, from the ref. we can use this to "back-fill" the
    # network.
    prefix, ref = _splitref(ref)

    if network and network.startswith('AU:') and \
       network[3:] in _AU_NETWORK_IMPORTANCE:
        # network is already in the form we want!
        pass

    elif network in _AU_NETWORK_EXPANSION:
        network = _AU_NETWORK_EXPANSION[network]

    elif prefix in _AU_NETWORK_EXPANSION:
        # backfill network from ref, if possible. (note that ref must
        # be non-None, since mz_networks entries have either network or
        # ref, or both).
        network = _AU_NETWORK_EXPANSION[prefix]

    return network, ref


def _normalize_br_netref(network, ref):
    # try to add detail to the network by looking at the ref value,
    # which often has additional information.
    for guess_net, guess_ref in _guess_network_br(dict(ref=ref)):
        if guess_ref == ref and (
                network is None or guess_net.startswith(network)):
            network = guess_net
            break

    if network == 'BR':
        if ref == 'BR-230':
            return 'BR:Trans-Amazonian', ref
        else:
            return network, ref

    elif network and network.startswith('BR:'):
        # turn things like "BR:BA-roads" into just "BR:BA"
        if network.endswith('-roads'):
            network = network[:-6]

        return network, ref

    elif network in _BR_STATES:
        # just missing the 'BR:' at the start?
        return 'BR:' + network, ref

    else:
        return None, ref


def _normalize_ca_netref(network, ref):
    if isinstance(network, (str, unicode)) and \
       network.startswith('CA:NB') and \
       ref.isdigit():
        refnum = int(ref)
        if refnum >= 200:
            network = 'CA:NB3'
        elif refnum >= 100:
            network = 'CA:NB2'
    return network, ref


def _normalize_cd_netref(network, ref):
    if network == 'CD:rrig':
        network = 'CD:RRIG'

    return network, ref


def _normalize_ch_netref(network, ref):
    prefix, ref = _splitref(ref)

    if network == 'CH:Nationalstrasse':
        # clean up the ref by removing any prefixes and extra stuff after
        # the number.
        ref = ref.split(' ')[0]
        network = 'CH:national'

    elif prefix == 'A':
        network = 'CH:motorway'

    elif network not in ('CH:motorway', 'CH:national', 'CH:regional'):
        network = None
        ref = None

    return network, ref


def _normalize_cn_netref(network, ref):
    if ref and ref.startswith('S'):
        network = 'CN:expressway:regional'

    elif ref and ref.startswith('G'):
        network = 'CN:expressway'

    elif ref and ref.startswith('X'):
        network = 'CN:JX'

    elif network == 'CN-expressways':
        network = 'CN:expressway'

    elif network == 'CN-expressways-regional':
        network = 'CN:expressway:regional'

    elif network == 'JX-roads':
        network = 'CN:JX'

    return network, ref


# mapping the network prefixes onto ISO 3166-2 codes
_ES_AUTONOMA = set([
    'ARA',  # Aragon
    'A',  # Aragon & Andalusia (and also Álava, Basque Country)
    'CA',  # Cantabria (also Cadiz?)
    'CL',  # Castile & Leon
    'CM',  # Castilla-La Mancha
    'C',  # Catalonia (also Cistierna & Eivissa?)
    'EX',  # Extremadura
    'AG',  # Galicia
    'M',  # Madrid
    'R',  # Madrid
    'Ma',  # Mallorca
    'Me',  # Menorca
    'ML',  # Melilla
    'RC',  # Menorca
    'RM',  # Murcia
    'V',  # Valencia (also A Coruna?)
    'CV',  # Valencia
    'Cv',  # Valencia
])


# mapping the network prefixes onto ISO 3166-2 codes
_ES_PROVINCES = set([
    'AC',  # A Coruna
    'DP',  # A Coruna
    'AB',  # Albacete
    'F',  # Alicante?
    'AL',  # Almeria
    'AE',  # Asturias
    'AS',  # Asturias
    'AV',  # Avila
    'BA',  # Badajoz
    'B',  # Barcelona
    'BP',  # Barcelona
    'BV',  # Barcelona
    'BI',  # Bizkaia
    'BU',  # Burgos
    'CC',  # Caceres
    'CO',  # Cordoba
    'CR',  # Cuidad Real
    'GIP',  # Girona
    'GIV',  # Girona
    'GI',  # Gipuzkoa & Girona
    'GR',  # Granada
    'GU',  # Guadalajara
    'HU',  # Huesca
    'JA',  # Jaen
    'JV',  # Jaen
    'LR',  # La Rioja
    'LE',  # Leon
    'L',  # Lerida
    'LP',  # Lerida
    'LV',  # Lerida
    'LU',  # Lugo
    'MP',  # Madrid
    'MA',  # Malaga
    'NA',  # Navarre
    'OU',  # Orense
    'P',  # Palencia
    'PP',  # Palencia
    'EP',  # Pontevedra
    'PO',  # Pontevedra
    'DSA',  # Salamanca
    'SA',  # Salamanca
    'NI',  # Segovia
    'SG',  # Segovia
    'SE',  # Sevilla
    'SO',  # Soria
    'TP',  # Tarragona
    'TV',  # Tarragona
    'TE',  # Teruel
    'TO',  # Toledo
    'VA',  # Valladolid
    'ZA',  # Zamora
    'CP',  # Zaragoza
    'Z',  # Zaragoza
    'PM',  # Baleares
    'PMV',  # Baleares
])


# mapping city codes to the name of the city
_ES_CITIES = set([
    'AI',  # Aviles
    'IA',  # Aviles
    'CT',  # Cartagena
    'CS',  # Castello
    'CU',  # Cudillero
    'CHE',  # Ejea de los Caballeros
    'EL',  # Elx/Elche
    'FE',  # Ferrol
    'GJ',  # Gijon
    'H',  # Huelva
    'VM',  # Huelva
    'J',  # Jaen
    'LN',  # Lena
    'LL',  # Lleida
    'LO',  # Logrono
    'ME',  # Merida
    'E',  # Mollerussa? / Eivissa
    'MU',  # Murcia
    'O',  # Oviedo
    'PA',  # Pamplona
    'PR',  # Parres
    'PI',  # Pilona
    'CHMS',  # Ponferrada?
    'PT',  # Puertollano
    'SL',  # Salas
    'S',  # Santander
    'SC',  # Santiago de Compostela
    'SI',  # Siero
    'VG',  # Vigo
    'EI',  # Eivissa
])


def _normalize_es_netref(network, ref):
    prefix, num = _splitref(ref)

    # some A-roads in Spain are actually province or autonoma roads. these are
    # distinguished from the national A-roads by whether they have 1 or 2
    # digits (national) or 3 or more digits (autonoma / province). sadly, it
    # doesn't seem to be possible to tell whether it's an autonoma or province
    # without looking at the geometry, which is left as a TODO for later rainy
    # days.
    num_digits = 0
    if num:
        num = num.lstrip('-')

        for c in num:
            if c.isdigit():
                num_digits += 1
            else:
                break

    if prefix in ('A', 'AP') and num_digits > 0 and num_digits < 3:
        network = 'ES:A-road'

    elif prefix == 'N':
        network = 'ES:N-road'

    elif prefix == 'E' and num:
        # e-roads seem to be signed without leading zeros.
        network = 'e-road'
        ref = 'E-' + num.lstrip('0')

    elif prefix in _ES_AUTONOMA:
        network = 'ES:autonoma'

    elif prefix in _ES_PROVINCES:
        network = 'ES:province'

    elif prefix in _ES_CITIES:
        network = 'ES:city'

    else:
        network = None
        ref = None

    return network, ref


_FR_DEPARTMENTAL_D_ROAD = re.compile(
    '^FR:[0-9]+:([A-Z]+)-road$', re.UNICODE | re.IGNORECASE)


def _normalize_fr_netref(network, ref):
    prefix, ref = _splitref(ref)
    if prefix:
        # routes nationales (RN) are actually signed just "N"? also, RNIL
        # are routes delegated to local departments, but still signed as
        # routes nationales.
        if prefix in ('RN', 'RNIL'):
            prefix = 'N'

        # strip spaces and leading zeros
        if ref:
            ref = prefix + ref.strip().lstrip('0')

        # backfill network from refs if network wasn't provided from another
        # source.
        if network is None:
            network = 'FR:%s-road' % (prefix,)

    # networks are broken down by department, e.g: FR:01:D-road, but we
    # only want to match on the D-road part, so throw away the department
    # number.
    if isinstance(network, (str, unicode)):
        m = _FR_DEPARTMENTAL_D_ROAD.match(network)
        if m:
            # see comment above. TODO: figure out how to not say this twice.
            prefix = m.group(1).upper()
            if prefix in ('RN', 'RNIL'):
                prefix = 'N'
            network = 'FR:%s-road' % (prefix,)

    return network, ref


def _normalize_de_netref(network, ref):
    prefix, ref = _splitref(ref)
    if prefix:
        if prefix == 'Ring':
            ref = 'Ring ' + ref
        else:
            ref = prefix + ref

        if not network:
            network = {
                'A': 'DE:BAB',
                'B': 'DE:BS',
                'L': 'DE:LS',
                'K': 'DE:KS',
                'St': 'DE:STS',
                'S': 'DE:STS',
                'Ring': 'DE:Hamburg:Ring',
            }.get(prefix)

    if network == 'Landesstra\xc3\x9fen NRW':
        network = 'DE:LS'

    elif network == 'Kreisstra\xc3\x9fen Hildesheim':
        network = 'DE:KS'

    elif network == 'BAB':
        network = 'DE:BAB'

    return network, ref


def _normalize_ga_netref(network, ref):
    prefix, num = _splitref(ref)

    if prefix in ('N', 'RN'):
        network = 'GA:national'
        ref = 'N' + num

    elif prefix == 'L':
        network = 'GA:L-road'
        ref = 'L' + num

    else:
        network = None
        ref = None

    return network, ref


def _normalize_gr_netref(network, ref):
    ref = _make_unicode_or_none(ref)

    prefix, ref = _splitref(ref)
    # this might look bizzare, but it's because the Greek capital letters
    # epsilon and omicron look very similar (in some fonts identical) to the
    # Latin characters E and O. it's the same below for capital alpha and A.
    # these are sometimes mixed up in the data, so we map them to the same
    # networks.
    if prefix in (u'ΕΟ', u'EO'):
        network = 'GR:national'

    elif (prefix in (u'Α', u'A') and
          (network is None or network == 'GR:motorway')):
        network = 'GR:motorway'
        # keep A prefix for shield text
        ref = u'Α' + ref

    elif network == 'e-road':
        ref = 'E' + ref

    elif network and network.startswith('GR:provincial:'):
        network = 'GR:provincial'

    return network, ref


def _normalize_in_netref(network, ref):
    prefix, ref = _splitref(ref)

    if prefix == 'NH':
        network = 'IN:NH'

    elif prefix == 'SH':
        network = 'IN:SH'

    elif prefix == 'MDR':
        network = 'IN:MDR'

    elif network and network.startswith('IN:NH'):
        network = 'IN:NH'

    elif network and network.startswith('IN:SH'):
        network = 'IN:SH'

    elif network and network.startswith('IN:MDR'):
        network = 'IN:MDR'

    elif ref == 'MDR':
        network = 'IN:MDR'
        ref = None

    elif ref == 'ORR':
        network = 'IN:NH'

    else:
        network = None

    return network, ref


def _normalize_ir_netref(network, ref):
    net, num = _splitref(ref)

    if network == 'AH' or net == 'AH':
        network = 'AsianHighway'

        # in Iran, the Wikipedia page for the AsianHighway template suggests
        # that the AH route is shown as "A1Tr" (with the "Tr" in a little box)
        # https://en.wikipedia.org/wiki/Template:AHN-AH
        #
        # however, i haven't been able to find an example on a real road sign,
        # so perhaps it's not widely shown. anyway, we probably want "A1" as
        # the shield text.
        ref = 'A' + num

    elif network == 'IR:freeways':
        network = 'IR:freeway'

    return network, ref


def _normalize_la_netref(network, ref):
    # apparently common mistake: Laos is LA, not LO
    if network == 'LO:network':
        network = 'LA:national'

    return network, ref


# mapping of mexican road prefixes into their network values.
_MX_ROAD_NETWORK_PREFIXES = {
    'AGS':    'MX:AGU',  # Aguascalientes
    'BC':     'MX:BCN',  # Baja California
    'BCS':    'MX:BCS',  # Baja California Sur
    'CAM':    'MX:CAM',  # Campeche
    'CHIS':   'MX:CHP',  # Chiapas
    'CHIH':   'MX:CHH',  # Chihuahua
    'COAH':   'MX:COA',  # Coahuila
    'COL':    'MX:COL',  # Colima
    'DGO':    'MX:DUR',  # Durango
    'GTO':    'MX:GUA',  # Guanajuato
    'GRO':    'MX:GRO',  # Guerrero
    'HGO':    'MX:HID',  # Hidalgo
    'JAL':    'MX:JAL',  # Jalisco
    # NOTE: couldn't find an example for Edomex.
    'MICH':   'MX:MIC',  # Michoacán
    'MOR':    'MX:MOR',  # Morelos
    'NAY':    'MX:NAY',  # Nayarit
    'NL':     'MX:NLE',  # Nuevo León
    'OAX':    'MX:OAX',  # Oaxaca
    'PUE':    'MX:PUE',  # Puebla
    'QRO':    'MX:QUE',  # Querétaro
    'ROO':    'MX:ROO',  # Quintana Roo
    'SIN':    'MX:SIN',  # Sinaloa
    'SLP':    'MX:SLP',  # San Luis Potosí
    'SON':    'MX:SON',  # Sonora
    'TAB':    'MX:TAB',  # Tabasco
    'TAM':    'MX:TAM',  # Tamaulipas
    # NOTE: couldn't find an example for Tlaxcala.
    'VER':    'MX:VER',  # Veracruz
    'YUC':    'MX:YUC',  # Yucatán
    'ZAC':    'MX:ZAC',  # Zacatecas

    # National roads
    'MEX':    'MX:MEX',
}


def _normalize_mx_netref(network, ref):
    # interior ring road in Mexico City
    if ref == 'INT':
        network = 'MX:CMX:INT'
        ref = None

    elif ref == 'EXT':
        network = 'MX:CMX:EXT'
        ref = None

    prefix, part = _splitref(ref)
    if prefix:
        net = _MX_ROAD_NETWORK_PREFIXES.get(prefix.upper())
        if net:
            network = net
            ref = part

    # sometimes Quintana Roo is also written as "Q. Roo", which trips up
    # the _splitref() function, so this just adjusts for that.
    if ref and ref.upper().startswith('Q. ROO'):
        network = 'MX:ROO'
        ref = ref[len('Q. ROO'):].strip()

    return network, ref


# roads in Malaysia can have a state prefix similar to the letters used on
# vehicle license plates. see Wikipedia for a list:
#
#  https://en.wikipedia.org/wiki/Malaysian_State_Roads_system
#
# these are mapped to the abbreviations given in the table on:
#
#  https://en.wikipedia.org/wiki/States_and_federal_territories_of_Malaysia
#
_MY_ROAD_STATE_CODES = {
    'A': 'PRK',  # Perak
    'B': 'SGR',  # Selangor
    'C': 'PHG',  # Pahang
    'D': 'KTN',  # Kelantan
    'J': 'JHR',  # Johor
    'K': 'KDH',  # Kedah
    'M': 'MLK',  # Malacca
    'N': 'NSN',  # Negiri Sembilan
    'P': 'PNG',  # Penang
    'R': 'PLS',  # Perlis
    'SA': 'SBH',  # Sabah
    'T': 'TRG',  # Terengganu
    'Q': 'SWK',  # Sarawak
}


def _normalize_my_netref(network, ref):
    prefix, number = _splitref(ref)

    if prefix == 'E':
        network = 'MY:expressway'

    elif prefix in ('FT', ''):
        network = 'MY:federal'
        # federal highway 1 has many parts (1-1, 1-2, etc...) but it's not
        # clear that they're actually signed that way. so throw the part
        # after the dash away.
        ref = number.split('-')[0]

    elif prefix == 'AH':
        network = 'AsianHighway'

    elif prefix == 'MBSA':
        network = 'MY:SGR:municipal'
        # shorten ref so that it is more likely to fit in a 5-char shield.
        ref = 'BSA' + number

    elif prefix in _MY_ROAD_STATE_CODES:
        network = 'MY:' + _MY_ROAD_STATE_CODES[prefix]

    else:
        network = None

    return network, ref


def _normalize_jp_netref(network, ref):
    if network and network.startswith('JP:prefectural:'):
        network = 'JP:prefectural'

    elif network is None:
        prefix, _ = _splitref(ref)
        if prefix in ('C', 'E'):
            network = 'JP:expressway'

    return network, ref


def _normalize_kr_netref(network, ref):
    net, part = _splitref(ref)
    if net == 'AH':
        network = 'AsianHighway'
        ref = part

    elif network == 'AH':
        network = 'AsianHighway'

    return network, ref


def _normalize_kz_netref(network, ref):
    net, num = _splitref(ref)

    if net == 'AH' or network == 'AH':
        network = 'AsianHighway'
        ref = 'AH' + num

    elif net == 'E' or network == 'e-road':
        network = 'e-road'
        ref = 'E' + num

    return network, ref


def _normalize_no_netref(network, ref):
    prefix, number = _splitref(ref)

    if prefix == 'Rv':
        network = 'NO:riksvei'
        ref = number

    elif prefix == 'Fv':
        network = 'NO:fylkesvei'
        ref = number

    elif prefix == 'E' and number:
        network = 'e-road'
        ref = 'E ' + number.lstrip('0')

    elif prefix == 'Ring':
        network = 'NO:oslo:ring'
        ref = 'Ring ' + number

    elif network and network.lower().startswith('no:riksvei'):
        network = 'NO:riksvei'

    elif network and network.lower().startswith('no:fylkesvei'):
        network = 'NO:fylkesvei'

    else:
        network = None

    return network, ref


_PE_STATES = set([
    'AM',  # Amazonas
    'AN',  # Ancash
    'AP',  # Apurímac
    'AR',  # Arequipa
    'AY',  # Ayacucho
    'CA',  # Cajamarca
    'CU',  # Cusco
    'HU',  # Huánuco
    'HV',  # Huancavelica
    'IC',  # Ica
    'JU',  # Junín
    'LA',  # Lambayeque
    'LI',  # La Libertad
    'LM',  # Lima (including Callao)
    'LO',  # Loreto
    'MD',  # Madre de Dios
    'MO',  # Moquegua
    'PA',  # Pasco
    'PI',  # Piura
    'PU',  # Puno
    'SM',  # San Martín
    'TA',  # Tacna
    'TU',  # Tumbes
    'UC',  # Ucayali
])


def _normalize_pe_netref(network, ref):
    prefix, number = _splitref(ref)

    # Peruvian refs seem to be usually written "XX-YY" with a dash, so we have
    # to remove that as it's not part of the shield text.
    if number:
        number = number.lstrip('-')

    if prefix == 'PE':
        network = 'PE:PE'
        ref = number

    elif prefix in _PE_STATES:
        network = 'PE:' + prefix
        ref = number

    else:
        network = None

    return network, ref


def _normalize_ph_netref(network, ref):
    if network == 'PH:nhn':
        network = 'PH:NHN'

    return network, ref


def _normalize_pl_netref(network, ref):
    if network == 'PL:motorways':
        network = 'PL:motorway'
    elif network == 'PL:expressways':
        network = 'PL:expressway'

    if ref and ref.startswith('A'):
        network = 'PL:motorway'
    elif ref and ref.startswith('S'):
        network = 'PL:expressway'

    return network, ref


# expansion from ref prefixes to (network, shield text prefix).
#
# https://en.wikipedia.org/wiki/Roads_in_Portugal
#
# note that it seems signs generally don't have EN, ER or EM on them. instead,
# they have N, R and, presumably, M - although i wasn't able to find one of
# those. perhaps they're not important enough to sign with a number.
_PT_NETWORK_EXPANSION = {
    'A': ('PT:motorway', 'A'),
    'IP': ('PT:primary', 'IP'),
    'IC': ('PT:secondary', 'IC'),
    'VR': ('PT:rapid', 'VR'),
    'VE': ('PT:express', 'VE'),
    'EN': ('PT:national', 'N'),
    'ER': ('PT:regional', 'R'),
    'EM': ('PT:municipal', 'M'),
    'E': ('e-road', 'E'),
}


def _normalize_pt_netref(network, ref):
    prefix, num = _splitref(ref)

    result = _PT_NETWORK_EXPANSION.get(prefix)
    if result and num:
        network, letter = result
        ref = letter + num.lstrip('0')

    else:
        network = None

    return network, ref


# note that there's another road class, DX, which is documented, but doesn't
# currently exist.
# see https://en.wikipedia.org/wiki/Roads_in_Romania
#
_RO_NETWORK_PREFIXES = {
    'A': 'RO:motorway',
    'DN': 'RO:national',
    'DJ': 'RO:county',
    'DC': 'RO:local',
    'E': 'e-road',
}


def _normalize_ro_netref(network, ref):
    prefix, num = _splitref(ref)

    network = _RO_NETWORK_PREFIXES.get(prefix)
    if network is not None:
        ref = prefix + num
    else:
        ref = None

    return network, ref


def _normalize_ru_netref(network, ref):
    ref = _make_unicode_or_none(ref)
    prefix, num = _splitref(ref)

    # get rid of any stuff trailing the '-'. seems to be a section number or
    # mile marker?
    if num:
        num = num.lstrip('-').split('-')[0]

    if prefix in (u'М', 'M'):  # cyrillic M & latin M!
        ref = u'М' + num

    elif prefix in (u'Р', 'P'):
        if network is None:
            network = 'RU:regional'
        ref = u'Р' + num

    elif prefix in (u'А', 'A'):
        if network is None:
            network = 'RU:regional'
        ref = u'А' + num

    elif prefix == 'E':
        network = 'e-road'
        ref = u'E' + num

    elif prefix == 'AH':
        network = 'AsianHighway'
        ref = u'AH' + num

    else:
        ref = None

    if isinstance(ref, unicode):
        ref = ref.encode('utf-8')

    return network, ref


_TR_PROVINCIAL = re.compile('^[0-9]{2}-[0-9]{2}$')


# NOTE: there's aslo an "NSC", which is under construction
_SG_EXPRESSWAYS = set([
    'AYE',  # Ayer Rajah Expressway
    'BKE',  # Bukit Timah Expressway
    'CTE',  # Central Expressway
    'ECP',  # East Coast Parkway
    'KJE',  # Kranji Expressway
    'KPE',  # Kallang-Paya Lebar Expressway
    'MCE',  # Marina Coastal Expressway
    'PIE',  # Pan Island Expressway
    'SLE',  # Seletar Expressway
    'TPE',  # Tampines Expressway
])


def _normalize_sg_netref(network, ref):
    if ref in _SG_EXPRESSWAYS:
        network = 'SG:expressway'

    else:
        network = None
        ref = None

    return network, ref


def _normalize_tr_netref(network, ref):
    prefix, num = _splitref(ref)

    if num:
        num = num.lstrip('-')

    if prefix == 'O' and num:
        # see https://en.wikipedia.org/wiki/Otoyol
        network = 'TR:motorway'
        ref = 'O' + num.lstrip('0')

    elif prefix == 'D' and num:
        # see https://en.wikipedia.org/wiki/Turkish_State_Highway_System
        network = 'TR:highway'
        # drop section suffixes
        ref = 'D' + num.split('-')[0]

    elif ref and _TR_PROVINCIAL.match(ref):
        network = 'TR:provincial'

    elif prefix == 'E' and num:
        network = 'e-road'
        ref = 'E' + num

    else:
        network = None
        ref = None

    return network, ref


def _normalize_ua_netref(network, ref):
    ref = _make_unicode_or_none(ref)
    prefix, num = _splitref(ref)

    if num:
        num = num.lstrip('-')

    if not num:
        network = None
        ref = None

    elif prefix in (u'М', 'M'):  # cyrillic M & latin M!
        if network is None:
            network = 'UA:international'
        ref = u'М' + num

    elif prefix in (u'Н', 'H'):
        if network is None:
            network = 'UA:national'
        ref = u'Н' + num

    elif prefix in (u'Р', 'P'):
        if network is None:
            network = 'UA:regional'
        ref = u'Р' + num

    elif prefix in (u'Т', 'T'):
        network = 'UA:territorial'
        ref = u'Т' + num.replace('-', '')

    elif prefix == 'E':
        network = 'e-road'
        ref = u'E' + num

    else:
        ref = None
        network = None

    if isinstance(ref, unicode):
        ref = ref.encode('utf-8')

    return network, ref


def _normalize_vn_netref(network, ref):
    ref = _make_unicode_or_none(ref)
    prefix, num = _splitref(ref)

    if num:
        num = num.lstrip(u'.')

    if not num:
        network = None
        ref = None

    elif prefix == u'CT' or network == 'VN:expressway':
        network = 'VN:expressway'
        ref = u'CT' + num

    elif prefix == u'QL' or network == 'VN:national':
        network = 'VN:national'
        ref = u'QL' + num

    elif prefix in (u'ĐT', u'DT'):
        network = 'VN:provincial'
        ref = u'ĐT' + num

    elif prefix == u'TL' or network in ('VN:provincial', 'VN:TL'):
        network = 'VN:provincial'
        ref = u'TL' + num

    elif ref:
        network = 'VN:road'

    else:
        network = None
        ref = None

    if isinstance(ref, unicode):
        ref = ref.encode('utf-8')
    return network, ref


def _normalize_za_netref(network, ref):
    prefix, num = _splitref(ref)
    ndigits = len(num) if num else 0

    # N, R & M numbered routes all have special shields which have the letter
    # above the number, which would make it part of the shield artwork rather
    # than the shield text.
    if prefix == 'N':
        network = 'ZA:national'
        ref = num

    elif prefix == 'R' and ndigits == 2:
        # 2-digit R numbers are provincial routes, 3-digit are regional routes.
        # https://en.wikipedia.org/wiki/Numbered_routes_in_South_Africa
        network = 'ZA:provincial'
        ref = num

    elif prefix == 'R' and ndigits == 3:
        network == 'ZA:regional'
        ref = num

    elif prefix == 'M':
        # there are various different metropolitan networks, but according to
        # the Wikipedia page, they all have the same shield. so lumping them
        # all together under "metropolitan".
        network = 'ZA:metropolitan'
        ref = num

    elif prefix == 'H':
        # i wasn't able to find documentation for these, but there are
        # H-numbered roads with good signage, which appear to be only in the
        # Kruger National Park, so i've named them that way.
        network = 'ZA:kruger'

    elif prefix == 'S':
        # i wasn't able to find any documentation for these, but there are
        # plain white-on-green signs for some of these visible.
        network = 'ZA:S-road'

    else:
        ref = None
        network = None

    return network, ref


def _shield_text_ar(network, ref):
    # Argentinian national routes start with "RN" (ruta nacional), which
    # should be stripped, but other letters shouldn't be!
    if network == 'AR:national' and ref and ref.startswith('RN'):
        return ref[2:]

    # Argentinian provincial routes start with "RP" (ruta provincial)
    if network == 'AR:provincial' and ref and ref.startswith('RP'):
        return ref[2:]

    return ref


_AU_NETWORK_SHIELD_TEXT = {
    'AU:M-road': 'M',
    'AU:A-road': 'A',
    'AU:B-road': 'B',
    'AU:C-road': 'C',
}


def _shield_text_au(network, ref):
    # shields on M, A, B & C roads should have the letter, but not other types
    # of roads.
    prefix = _AU_NETWORK_SHIELD_TEXT.get(network)
    if prefix:
        ref = prefix + ref

    return ref


def _shield_text_gb(network, ref):
    # just remove any space between the letter and number(s)
    prefix, number = _splitref(ref)
    if prefix and number:
        return prefix + number
    else:
        return ref


def _shield_text_ro(network, ref):
    # the DN, DJ & DC networks don't have a prefix on the displayed shields,
    # see:
    # https://upload.wikimedia.org/wikipedia/commons/b/b0/Autostrada_Sibiu_01.jpg
    # https://upload.wikimedia.org/wikipedia/commons/7/7a/A1_Arad-Timisoara_-_01.JPG
    if network in ('RO:national', 'RO:county', 'RO:local'):
        return ref[2:]

    return ref


# do not strip anything from the ref apart from whitespace.
def _use_ref_as_is(network, ref):
    return ref.strip()


# CountryNetworkLogic centralises the logic around country-specific road
# network processing. this allows us to do different things, such as
# back-filling missing network tag values or sorting networks differently
# based on which country they are in. (e.g: in the UK, an "M" road is more
# important than an "A" road, even though they'd sort the other way
# alphabetically).
#
# the different logic sections are:
#
# * backfill: this is called as fn(tags) to unpack the ref tag (and any other
#             meaningful tags) into a list of (network, ref) tuples to use
#             instead. For example, it's common to give ref=A1;B2;C3 to
#             indicate multiple networks & shields.
#
# * fix: this is called as fn(network, ref) and should fix whatever problems it
#        can and return the replacement (network, ref). remember! either
#        network or ref can be None!
#
# * sort: this is called as fn(network, ref) and should return a numeric value
#         where lower numeric values mean _more_ important networks.
#
# * shield_text: this is called as fn(network, ref) and should return the
#                shield text to output. this might mean stripping leading alpha
#                numeric characters - or not, depending on the country.
#
CountryNetworkLogic = namedtuple(
    'CountryNetworkLogic', 'backfill fix sort shield_text')
CountryNetworkLogic.__new__.__defaults__ = (None,) * len(
    CountryNetworkLogic._fields)

_COUNTRY_SPECIFIC_ROAD_NETWORK_LOGIC = {
    'AR': CountryNetworkLogic(
        backfill=_guess_network_ar,
        shield_text=_shield_text_ar,
    ),
    'AU': CountryNetworkLogic(
        backfill=_guess_network_au,
        fix=_normalize_au_netref,
        sort=_sort_network_au,
        shield_text=_shield_text_au,
    ),
    'BR': CountryNetworkLogic(
        backfill=_guess_network_br,
        fix=_normalize_br_netref,
        sort=_sort_network_br,
    ),
    'CA': CountryNetworkLogic(
        backfill=_guess_network_ca,
        fix=_normalize_ca_netref,
        sort=_sort_network_ca,
    ),
    'CH': CountryNetworkLogic(
        backfill=_guess_network_ch,
        fix=_normalize_ch_netref,
        sort=_sort_network_ch,
    ),
    'CD': CountryNetworkLogic(
        fix=_normalize_cd_netref,
    ),
    'CN': CountryNetworkLogic(
        backfill=_guess_network_cn,
        fix=_normalize_cn_netref,
        sort=_sort_network_cn,
        shield_text=_use_ref_as_is,
    ),
    'DE': CountryNetworkLogic(
        backfill=_guess_network_de,
        fix=_normalize_de_netref,
        sort=_sort_network_de,
        shield_text=_use_ref_as_is,
    ),
    'ES': CountryNetworkLogic(
        backfill=_guess_network_es,
        fix=_normalize_es_netref,
        sort=_sort_network_es,
        shield_text=_use_ref_as_is,
    ),
    'FR': CountryNetworkLogic(
        backfill=_guess_network_fr,
        fix=_normalize_fr_netref,
        sort=_sort_network_fr,
        shield_text=_use_ref_as_is,
    ),
    'GA': CountryNetworkLogic(
        backfill=_guess_network_ga,
        fix=_normalize_ga_netref,
        sort=_sort_network_ga,
        shield_text=_use_ref_as_is,
    ),
    'GB': CountryNetworkLogic(
        backfill=_guess_network_gb,
        sort=_sort_network_gb,
        shield_text=_shield_text_gb,
    ),
    'GR': CountryNetworkLogic(
        backfill=_guess_network_gr,
        fix=_normalize_gr_netref,
        sort=_sort_network_gr,
    ),
    'IN': CountryNetworkLogic(
        backfill=_guess_network_in,
        fix=_normalize_in_netref,
        sort=_sort_network_in,
        shield_text=_use_ref_as_is,
    ),
    'IR': CountryNetworkLogic(
        fix=_normalize_ir_netref,
        sort=_sort_network_ir,
        shield_text=_use_ref_as_is,
    ),
    'JP': CountryNetworkLogic(
        backfill=_guess_network_jp,
        fix=_normalize_jp_netref,
        shield_text=_use_ref_as_is,
    ),
    'KR': CountryNetworkLogic(
        backfill=_guess_network_kr,
        fix=_normalize_kr_netref,
    ),
    'KZ': CountryNetworkLogic(
        fix=_normalize_kz_netref,
        sort=_sort_network_kz,
        shield_text=_use_ref_as_is,
    ),
    'LA': CountryNetworkLogic(
        fix=_normalize_la_netref,
        sort=_sort_network_la,
    ),
    'MX': CountryNetworkLogic(
        backfill=_guess_network_mx,
        fix=_normalize_mx_netref,
        sort=_sort_network_mx,
    ),
    'MY': CountryNetworkLogic(
        backfill=_guess_network_my,
        fix=_normalize_my_netref,
        sort=_sort_network_my,
        shield_text=_use_ref_as_is,
    ),
    'NO': CountryNetworkLogic(
        backfill=_guess_network_no,
        fix=_normalize_no_netref,
        sort=_sort_network_no,
        shield_text=_use_ref_as_is,
    ),
    'PE': CountryNetworkLogic(
        backfill=_guess_network_pe,
        fix=_normalize_pe_netref,
        shield_text=_use_ref_as_is,
    ),
    'PH': CountryNetworkLogic(
        fix=_normalize_ph_netref,
    ),
    'PL': CountryNetworkLogic(
        backfill=_guess_network_pl,
        fix=_normalize_pl_netref,
        sort=_sort_network_pl,
    ),
    'PT': CountryNetworkLogic(
        backfill=_guess_network_pt,
        fix=_normalize_pt_netref,
        sort=_sort_network_pt,
        shield_text=_use_ref_as_is,
    ),
    'RO': CountryNetworkLogic(
        backfill=_guess_network_ro,
        fix=_normalize_ro_netref,
        sort=_sort_network_ro,
        shield_text=_shield_text_ro,
    ),
    'RU': CountryNetworkLogic(
        backfill=_guess_network_ru,
        fix=_normalize_ru_netref,
        sort=_sort_network_ru,
        shield_text=_use_ref_as_is,
    ),
    'SG': CountryNetworkLogic(
        backfill=_guess_network_sg,
        fix=_normalize_sg_netref,
        shield_text=_use_ref_as_is,
    ),
    'TR': CountryNetworkLogic(
        backfill=_guess_network_tr,
        fix=_normalize_tr_netref,
        sort=_sort_network_tr,
        shield_text=_use_ref_as_is,
    ),
    'UA': CountryNetworkLogic(
        backfill=_guess_network_ua,
        fix=_normalize_ua_netref,
        sort=_sort_network_ua,
        shield_text=_use_ref_as_is,
    ),
    'US': CountryNetworkLogic(
        backfill=_do_not_backfill,
        sort=_sort_network_us,
    ),
    'VN': CountryNetworkLogic(
        backfill=_guess_network_vn,
        fix=_normalize_vn_netref,
        sort=_sort_network_vn,
        shield_text=_use_ref_as_is,
    ),
    'ZA': CountryNetworkLogic(
        backfill=_guess_network_za,
        fix=_normalize_za_netref,
        sort=_sort_network_za,
        shield_text=_use_ref_as_is,
    ),
}


# regular expression to look for a country code at the beginning of the network
# tag.
_COUNTRY_CODE = re.compile('^([a-z][a-z])[:-](.*)', re.UNICODE | re.IGNORECASE)


def _fixup_network_country_code(network):
    if network is None:
        return None

    m = _COUNTRY_CODE.match(network)
    if m:
        suffix = m.group(2)

        # fix up common suffixes which are plural with ones which are singular.
        if suffix.lower() == 'roads':
            suffix = 'road'

        network = m.group(1).upper() + ':' + suffix

    return network


def merge_networks_from_tags(shape, props, fid, zoom):
    """
    Take the network and ref tags from the feature and, if they both exist, add
    them to the mz_networks list. This is to make handling of networks and refs
    more consistent across elements.
    """

    network = props.get('network')
    ref = props.get('ref')
    mz_networks = props.get('mz_networks', [])
    country_code = props.get('country_code')

    # apply some generic fixes to networks:
    #  * if they begin with two letters and a colon, then make sure the two
    #    letters are upper case, as they're probably a country code.
    #  * if they begin with two letters and a dash, then make the letters upper
    #    case and replace the dash with a colon.
    #  * expand ;-delimited lists in refs
    for i in xrange(0, len(mz_networks), 3):
        t, n, r = mz_networks[i:i+3]
        if t == 'road' and n is not None:
            n = _fixup_network_country_code(n)
            mz_networks[i+1] = n
        if r is not None and ';' in r:
            refs = r.split(';')
            mz_networks[i+2] = refs.pop()
            for new_ref in refs:
                mz_networks.extend((t, n, new_ref))

    # for road networks, if there's no explicit network, but the country code
    # and ref are both available, then try to use them to back-fill the
    # network.
    if props.get('kind') in ('highway', 'major_road') and \
       country_code and ref:
        # apply country-specific logic to try and backfill the network from
        # structure we know about how refs work in the country.
        logic = _COUNTRY_SPECIFIC_ROAD_NETWORK_LOGIC.get(country_code)

        # if the road is a member of exactly one road relation, which provides
        # a network and no ref, and the element itself provides no network,
        # then use the network from the relation instead.
        if network is None:
            solo_networks_from_relations = []
            for i in xrange(0, len(mz_networks), 3):
                t, n, r = mz_networks[i:i+3]
                if t == 'road' and n and (r is None or r == ref):
                    solo_networks_from_relations.append((n, i))

            # if we found one _and only one_ road network, then we use the
            # network value and delete the [type, network, ref] 3-tuple from
            # mz_networks (which is a flattened list of them). because there's
            # only one, we can delete it by using its index.
            if len(solo_networks_from_relations) == 1:
                network, i = solo_networks_from_relations[0]
                # add network back into properties in case we need to pass it
                # to the backfill.
                props['network'] = network
                del mz_networks[i:i+3]

        if logic and logic.backfill:
            networks_and_refs = logic.backfill(props) or []

            # if we found a ref, but the network was not provided, then "use
            # up" the network tag by assigning it to the first network. this
            # deals with cases where people write network="X", ref="1;Y2" to
            # mean "X1" and "Y2".
            if networks_and_refs:
                net, r = networks_and_refs[0]
                if net is None and network is not None:
                    networks_and_refs[0] = (network, r)
                # if we extracted information from the network and ref, then
                # we don't want to process it again.
                network = None
                ref = None

            for net, r in networks_and_refs:
                mz_networks.extend(['road', net, r])

        elif network is None:
            # last ditch backfill, if we know nothing else about this element,
            # at least we know what country it is in. but don't add if there's
            # an entry in mz_networks with the same ref!
            if ref:
                found = False
                for i in xrange(0, len(mz_networks), 3):
                    t, _, r = mz_networks[i:i+3]
                    if t == 'road' and r == ref:
                        found = True
                        break
                if not found:
                    network = country_code

    # if there's no network, but the operator indicates a network, then we can
    # back-fill an approximate network tag from the operator. this can mean
    # that extra refs are available for road networks.
    elif network is None:
        operator = props.get('operator')
        backfill_network = _NETWORK_OPERATORS.get(operator)
        if backfill_network:
            network = backfill_network

    if network and ref:
        props.pop('network', None)
        props.pop('ref')
        mz_networks.extend([_guess_type_from_network(network), network, ref])

    if mz_networks:
        props['mz_networks'] = mz_networks

    return (shape, props, fid)


# a pattern to find any number in a string, as a fallback for looking up road
# reference numbers.
_ANY_NUMBER = re.compile('[^0-9]*([0-9]+)')


def _default_sort_network(network, ref):
    """
    Returns an integer representing the numeric importance of the network,
    where lower numbers are more important.

    This is to handle roads which are part of many networks, and ensuring
    that the most important one is displayed. For example, in the USA many
    roads can be part of both interstate (US:I) and "US" (US:US) highways,
    and possibly state ones as well (e.g: US:NY:xxx). In addition, there
    are international conventions around the use of "CC:national" and
    "CC:regional:*" where "CC" is an ISO 2-letter country code.

    Here we treat national-level roads as more important than regional or
    lower, and assume that the deeper the network is in the hierarchy, the
    less important the road. Roads with lower "ref" numbers are considered
    more important than higher "ref" numbers, if they are part of the same
    network.
    """

    if network is None:
        network_code = 9999
    elif ':national' in network:
        network_code = 1
    elif ':regional' in network:
        network_code = 2
    elif network == 'e-road' in network:
        network_code = 9000
    else:
        network_code = len(network.split(':')) + 3

    ref = _ref_importance(ref)

    return network_code * 10000 + min(ref, 9999)


_WALKING_NETWORK_CODES = {
    'iwn': 1,
    'nwn': 2,
    'rwn': 3,
    'lwn': 4,
}


_BICYCLE_NETWORK_CODES = {
    'icn': 1,
    'ncn': 2,
    'rcn': 3,
    'lcn': 4,
}


def _generic_network_importance(network, ref, codes):
    # get a code based on the "largeness" of the network
    code = codes.get(network, len(codes))

    # get a numeric ref, if one is available. treat things with no ref as if
    # they had a very high ref, and so reduced importance.
    try:
        ref = max(int(ref or 9999), 0)
    except ValueError:
        # if ref isn't an integer, then it's likely a name, which might be
        # more important than a number
        ref = 0

    return code * 10000 + min(ref, 9999)


def _walking_network_importance(network, ref):
    return _generic_network_importance(network, ref, _WALKING_NETWORK_CODES)


def _bicycle_network_importance(network, ref):
    return _generic_network_importance(network, ref, _BICYCLE_NETWORK_CODES)


def _bus_network_importance(network, ref):
    return _generic_network_importance(network, ref, {})


_NUMBER_AT_FRONT = re.compile(r'^(\d+\w*)', re.UNICODE)
_SINGLE_LETTER_AT_FRONT = re.compile(r'^([^\W\d]) *(\d+)', re.UNICODE)
_LETTER_THEN_NUMBERS = re.compile(r'^[^\d\s_]+[ -]?([^\s]+)',
                                  re.UNICODE | re.IGNORECASE)
_UA_TERRITORIAL_RE = re.compile(r'^(\w)-(\d+)-(\d+)$',
                                re.UNICODE | re.IGNORECASE)


def _make_unicode_or_none(ref):
    if isinstance(ref, unicode):
        # no need to do anything, it's already okay
        return ref

    elif isinstance(ref, str):
        # it's UTF-8 encoded bytes, so make it a unicode
        return unicode(ref, 'utf-8')

    # dunno what this is?!!
    return None


def _road_shield_text(network, ref):
    """
    Try to extract the string that should be displayed within the road shield,
    based on the raw ref and the network value.
    """

    # FI-PI-LI is just a special case?
    if ref == 'FI-PI-LI':
        return ref

    # These "belt" roads have names in the ref which should be in the shield,
    # there's no number.
    if network and network == 'US:PA:Belt':
        return ref

    # Ukranian roads sometimes have internal dashes which should be removed.
    if network and network.startswith('ua:'):
        m = _UA_TERRITORIAL_RE.match(ref)
        if m:
            return m.group(1) + m.group(2) + m.group(3)

    # Greek roads sometimes have alphabetic prefixes which we should _keep_,
    # unlike for other roads.
    if network and (network.startswith('GR:') or network.startswith('gr:')):
        return ref

    # If there's a number at the front (optionally with letters following),
    # then that's the ref.
    m = _NUMBER_AT_FRONT.match(ref)
    if m:
        return m.group(1)

    # If there's a letter at the front, optionally space, and then a number,
    # the ref is the concatenation (without space) of the letter and number.
    m = _SINGLE_LETTER_AT_FRONT.match(ref)
    if m:
        return m.group(1) + m.group(2)

    # Otherwise, try to match a bunch of letters followed by a number.
    m = _LETTER_THEN_NUMBERS.match(ref)
    if m:
        return m.group(1)

    # Failing that, give up and just return the ref as-is.
    return ref


def _default_shield_text(network, ref):
    """
    Without any special properties of the ref to make the shield text from,
    just use the 'ref' property.
    """

    return ref


# _Network represents a type of route network.
# prefix is what we should insert into
# the property we put on the feature (e.g: prefix + 'network' for
# 'bicycle_network' and so forth). shield_text_fn is a function called with the
# network and ref to get the text which should be shown on the shield.
_Network = namedtuple(
    '_Network', 'prefix shield_text_fn network_importance_fn')


_ROAD_NETWORK = _Network(
    '',
    _road_shield_text,
    None)
_FOOT_NETWORK = _Network(
    'walking_',
    _default_shield_text,
    _walking_network_importance)
_BIKE_NETWORK = _Network(
    'bicycle_',
    _default_shield_text,
    _bicycle_network_importance)
_BUS_NETWORK = _Network(
    'bus_',
    _default_shield_text,
    _bus_network_importance)

_NETWORKS = {
    'road': _ROAD_NETWORK,
    'foot': _FOOT_NETWORK,
    'hiking': _FOOT_NETWORK,
    'bicycle': _BIKE_NETWORK,
    'bus': _BUS_NETWORK,
    'trolleybus': _BUS_NETWORK,
}


def extract_network_information(shape, properties, fid, zoom):
    """
    Take the triples of (route_type, network, ref) from `mz_networks` and
    extract them into two arrays of network and shield_text information.
    """

    mz_networks = properties.pop('mz_networks', None)
    country_code = properties.get('country_code')
    country_logic = _COUNTRY_SPECIFIC_ROAD_NETWORK_LOGIC.get(country_code)

    if mz_networks is not None:
        # take the list and make triples out of it
        itr = iter(mz_networks)

        groups = defaultdict(list)
        for (type, network, ref) in zip(itr, itr, itr):
            n = _NETWORKS.get(type)
            if n:
                groups[n].append([network, ref])

        for network, vals in groups.items():
            all_networks = 'all_' + network.prefix + 'networks'
            all_shield_texts = 'all_' + network.prefix + 'shield_texts'

            shield_text_fn = network.shield_text_fn
            if network is _ROAD_NETWORK and country_logic and \
               country_logic.shield_text:
                shield_text_fn = country_logic.shield_text

            shield_texts = list()
            network_names = list()
            for network_name, ref in vals:
                network_names.append(network_name)

                ref = _make_unicode_or_none(ref)
                if ref is not None:
                    ref = shield_text_fn(network_name, ref)

                # we try to keep properties as utf-8 encoded str, but the
                # shield text function may have turned them into unicode.
                # this is a catch-all just to make absolutely sure.
                if isinstance(ref, unicode):
                    ref = ref.encode('utf-8')

                shield_texts.append(ref)

            properties[all_networks] = network_names
            properties[all_shield_texts] = shield_texts

    return (shape, properties, fid)


def _choose_most_important_network(properties, prefix, importance_fn):
    """
    Use the `_network_importance` function to select any road networks from
    `all_networks` and `all_shield_texts`, taking the most important one.
    """

    all_networks = 'all_' + prefix + 'networks'
    all_shield_texts = 'all_' + prefix + 'shield_texts'

    networks = properties.pop(all_networks, None)
    shield_texts = properties.pop(all_shield_texts, None)
    country_code = properties.get('country_code')

    if networks and shield_texts:
        def network_key(t):
            return importance_fn(*t)

        tuples = sorted(set(zip(networks, shield_texts)), key=network_key)

        # i think most route designers would try pretty hard to make sure that
        # a segment of road isn't on two routes of different networks but with
        # the same shield text. most likely when this happens it's because we
        # have duplicate information in the element and relations it's a part
        # of. so get rid of anything with network=None where there's an entry
        # with the same ref (and network != none).
        seen_ref = set()
        new_tuples = []
        for network, ref in tuples:
            if network:
                if ref:
                    seen_ref.add(ref)
                new_tuples.append((network, ref))

            elif ref is not None and ref not in seen_ref:
                # network is None, fall back to the country code
                new_tuples.append((country_code, ref))

        tuples = new_tuples

        if tuples:
            # expose first network as network/shield_text
            network, ref = tuples[0]
            properties[prefix + 'network'] = network
            properties[prefix + 'shield_text'] = ref

            # replace properties with sorted versions of themselves
            properties[all_networks] = [n[0] for n in tuples]
            properties[all_shield_texts] = [n[1] for n in tuples]

    return properties


def choose_most_important_network(shape, properties, fid, zoom):

    for net in _NETWORKS.values():
        prefix = net.prefix
        if net is _ROAD_NETWORK:
            country_code = properties.get('country_code')
            logic = _COUNTRY_SPECIFIC_ROAD_NETWORK_LOGIC.get(country_code)

            importance_fn = None
            if logic:
                importance_fn = logic.sort
            if not importance_fn:
                importance_fn = _default_sort_network

        else:
            importance_fn = net.network_importance_fn

        properties = _choose_most_important_network(
            properties, prefix, importance_fn)

    return (shape, properties, fid)


def buildings_unify(ctx):
    """
    Unify buildings with their parts. Building parts will receive a
    root_id property which will be the id of building parent they are
    associated with.
    """
    zoom = ctx.nominal_zoom
    start_zoom = ctx.params.get('start_zoom', 0)

    if zoom < start_zoom:
        return None

    source_layer = ctx.params.get('source_layer')
    assert source_layer is not None, 'unify_buildings: missing source_layer'
    feature_layers = ctx.feature_layers
    layer = _find_layer(feature_layers, source_layer)
    if layer is None:
        return None

    class geom_with_building_id(object):
        def __init__(self, geom, building_id):
            self.geom = geom
            self.building_id = building_id
            self._geom = geom._geom
            self.is_empty = geom.is_empty

    indexable_buildings = []
    parts = []
    for feature in layer['features']:
        shape, props, feature_id = feature
        kind = props.get('kind')
        if kind == 'building':
            building_id = props.get('id')
            if building_id:
                indexed_building = geom_with_building_id(shape, building_id)
                indexable_buildings.append(indexed_building)
        elif kind == 'building_part':
            parts.append(feature)

    if not (indexable_buildings and parts):
        return

    buildings_index = STRtree(indexable_buildings)

    for part in parts:
        best_overlap = 0
        root_building_id = None

        part_shape, part_props, part_feature_id = part

        indexed_buildings = buildings_index.query(part_shape)
        for indexed_building in indexed_buildings:
            building_shape = indexed_building.geom
            intersection = part_shape.intersection(building_shape)
            overlap = intersection.area
            if overlap > best_overlap:
                best_overlap = overlap
                root_building_id = indexed_building.building_id

        if root_building_id is not None:
            part_props['root_id'] = root_building_id


def truncate_min_zoom_to_2dp(shape, properties, fid, zoom):
    """
    Truncate the "min_zoom" property to two decimal places.
    """

    min_zoom = properties.get('min_zoom')
    if min_zoom:
        properties['min_zoom'] = round(min_zoom, 2)

    return shape, properties, fid


def truncate_min_zoom_to_1dp(shape, properties, fid, zoom):
    """
    Truncate the "min_zoom" property to one decimal place.
    """

    min_zoom = properties.get('min_zoom')
    if min_zoom:
        properties['min_zoom'] = round(min_zoom, 1)

    return shape, properties, fid


class Palette(object):
    """
    A collection of named colours which allows relatively fast lookup of the
    closest named colour to any particular input colour.

    Inspired by https://github.com/cooperhewitt/py-cooperhewitt-swatchbook
    """

    def __init__(self, colours):
        self.colours = colours
        self.namelookup = dict()
        for name, colour in colours.items():
            assert len(colour) == 3, \
                "Colours must lists of be of length 3 (%r: %r)" % \
                (name, colour)
            for val in colour:
                assert isinstance(val, int), \
                    "Colour values must be integers (%r: %r)" % (name, colour)
                assert val >= 0 and val <= 255, \
                    "Colour values must be between 0 and 255 (%r: %r)" % \
                    (name, colour)
            self.namelookup[tuple(colour)] = name
        self.tree = kdtree.create(colours.values())

    def __call__(self, colour):
        """
        Returns the name of the closest colour in the palette to the input
        colour.
        """

        node, dist = self.tree.search_nn(colour)
        return self.namelookup[tuple(node.data)]

    def get(self, name):
        return self.colours.get(name)


def palettize_colours(ctx):
    """
    Derive a colour from each feature by looking at one or more input
    attributes and match that to a palette of name to colour mappings given
    in the `colours` parameter. The name of the colour will be output in the
    feature's properties using a key from the `attribute` paramter.
    """

    from vectordatasource.colour import parse_colour

    layer_name = ctx.params.get('layer')
    assert layer_name, \
        'Parameter layer was missing from palettize config'
    attr_name = ctx.params.get('attribute')
    assert attr_name, \
        'Parameter attribute was missing from palettize config'
    colours = ctx.params.get('colours')
    assert colours, \
        'Dict mapping colour names to RGB triples was missing from config'
    input_attrs = ctx.params.get('input_attributes', ['colour'])

    layer = _find_layer(ctx.feature_layers, layer_name)
    palette = Palette(colours)

    for (shape, props, fid) in layer['features']:
        colour = None
        for attr in input_attrs:
            colour = props.get(attr)
            if colour:
                break
        if colour:
            rgb = parse_colour(colour)
            if rgb:
                props[attr_name] = palette(rgb)

    return layer


def backfill_from_other_layer(ctx):
    """
    Matches features from one layer with the other on the basis of the feature
    ID and, if the configured layer property doesn't exist on the feature, but
    the other layer property does exist on the matched feature, then copy it
    across.

    The initial use for this is to backfill POI kinds into building kind_detail
    when the building doesn't already have a different kind_detail supplied.
    """

    layer_name = ctx.params.get('layer')
    assert layer_name, \
        'Parameter layer was missing from ' \
        'backfill_from_other_layer config'
    other_layer_name = ctx.params.get('other_layer')
    assert other_layer_name, \
        'Parameter other_layer_name was missing from ' \
        'backfill_from_other_layer config'
    layer_key = ctx.params.get('layer_key')
    assert layer_key, \
        'Parameter layer_key was missing from ' \
        'backfill_from_other_layer config'
    other_key = ctx.params.get('other_key')
    assert other_key, \
        'Parameter other_key was missing from ' \
        'backfill_from_other_layer config'

    layer = _find_layer(ctx.feature_layers, layer_name)
    other_layer = _find_layer(ctx.feature_layers, other_layer_name)

    # build an index of feature ID to property value in the other layer
    other_values = {}
    for (shape, props, fid) in other_layer['features']:
        # prefer to use the `id` property rather than the fid.
        fid = props.get('id', fid)
        kind = props.get(other_key)
        # make sure fid is truthy, as it can be set to None on features
        # created by merging.
        if kind and fid:
            other_values[fid] = kind

    # apply those to features which don't already have a value
    for (shape, props, fid) in layer['features']:
        if layer_key not in props:
            fid = props.get('id', fid)
            value = other_values.get(fid)
            if value:
                props[layer_key] = value

    return layer


def drop_layer(ctx):
    """
    Drops the named layer from the list of layers.
    """

    layer_to_delete = ctx.params.get('layer')

    for idx, feature_layer in enumerate(ctx.feature_layers):
        layer_datum = feature_layer['layer_datum']
        layer_name = layer_datum['name']

        if layer_name == layer_to_delete:
            del ctx.feature_layers[idx]
            break

    return None


def _fixup_country_specific_networks(shape, props, fid, zoom):
    """
    Apply country-specific fixup functions to mz_networks.
    """

    mz_networks = props.get('mz_networks')

    country_code = props.get('country_code')
    logic = _COUNTRY_SPECIFIC_ROAD_NETWORK_LOGIC.get(country_code)
    if logic and logic.fix and mz_networks:
        new_networks = []

        # mz_networks is a list of repeated [type, network, ref, ...], it isn't
        # nested!
        itr = iter(mz_networks)
        for (type, network, ref) in zip(itr, itr, itr):
            if type == 'road':
                network, ref = logic.fix(network, ref)
            new_networks.extend([type, network, ref])

        props['mz_networks'] = new_networks

    return (shape, props, fid)


def road_networks(ctx):
    """
    Fix up road networks. This means looking at the networks from the
    relation(s), if any, merging that with information from the tags on the
    original object and any structure we expect from looking at the country
    code.
    """

    params = _Params(ctx, 'road_networks')
    layer_name = params.required('layer')

    layer = _find_layer(ctx.feature_layers, layer_name)
    zoom = ctx.nominal_zoom

    funcs = [
        merge_networks_from_tags,
        _fixup_country_specific_networks,
        extract_network_information,
        choose_most_important_network,
    ]

    new_features = []
    for (shape, props, fid) in layer['features']:
        for fn in funcs:
            shape, props, fid = fn(shape, props, fid, zoom)

        new_features.append((shape, props, fid))

    layer['features'] = new_features
    return None


# helper class to wrap logic around extracting required and optional parameters
# from the context object passed to post-processors, making its use more
# concise and readable in the post-processor method itself.
#
class _Params(object):
    def __init__(self, ctx, post_processor_name):
        self.ctx = ctx
        self.post_processor_name = post_processor_name

    def required(self, name, typ=str, default=None):
        """
        Returns a named parameter of the given type and default from the
        context, raising an assertion failed exception if the parameter wasn't
        present, or wasn't an instance of the type.
        """

        value = self.optional(name, typ=typ, default=default)
        assert value is not None, \
            'Required parameter %r was missing from %r config' \
            % (name, self.post_processor_name)
        return value

    def optional(self, name, typ=str, default=None):
        """
        Returns a named parameter of the given type, or the default if that
        parameter wasn't given in the context. Raises an exception if the
        value was present and is not of the expected type.
        """

        value = self.ctx.params.get(name, default)
        if value is not None:
            assert isinstance(value, typ), \
                'Expected parameter %r to be of type %s, but value %r is of ' \
                'type %r in %r config' \
                % (name, typ.__name__, value, type(value).__name__,
                   self.post_processor_name)
        return value


def point_in_country_logic(ctx):
    """
    Intersect points from source layer with target layer, then look up which
    country they're in and assign property based on a look-up table.
    """

    params = _Params(ctx, 'point_in_country_logic')
    layer_name = params.required('layer')
    country_layer_name = params.required('country_layer')
    country_code_attr = params.required('country_code_attr')

    # single attribute version
    output_attr = params.optional('output_attr')
    # multiple attribute version
    output_attrs = params.optional('output_attrs', typ=list)
    # must provide one or the other
    assert output_attr or output_attrs, 'Must provide one or other of ' \
        'output_attr or output_attrs for point_in_country_logic'

    logic_table = params.optional('logic_table', typ=dict)
    if logic_table is None:
        logic_table = ctx.resources.get('logic_table')
    assert logic_table is not None, 'Must provide logic_table via a param ' \
        'or resource for point_in_country_logic'

    where = params.optional('where')

    layer = _find_layer(ctx.feature_layers, layer_name)
    country_layer = _find_layer(ctx.feature_layers, country_layer_name)

    if where is not None:
        where = compile(where, 'queries.yaml', 'eval')

    # this is a wrapper around a geometry, so that we can store extra
    # information in the STRTree.
    class country_with_value(object):
        def __init__(self, geom, value):
            self.geom = geom
            self.value = value
            self._geom = geom._geom
            self.is_empty = geom.is_empty

    # construct an STRtree index of the country->value mapping. in many cases,
    # the country will cover the whole tile, but in some other cases it will
    # not, and it's worth having the speedup of indexing for those.
    countries = []
    for (shape, props, fid) in country_layer['features']:
        country_code = props.get(country_code_attr)
        value = logic_table.get(country_code)
        if value is not None:
            countries.append(country_with_value(shape, value))

    countries_index = STRtree(countries)

    for (shape, props, fid) in layer['features']:
        # skip features where the 'where' clause doesn't match
        if where:
            local = props.copy()
            if not eval(where, {}, local):
                continue

        candidates = countries_index.query(shape)
        for candidate in candidates:
            # given that the shape is (expected to be) a point, all
            # intersections are the same (there's no measure of the "amount of
            # overlap"), so we might as well just stop on the first one.
            if shape.intersects(candidate.geom):
                if output_attrs:
                    for output_attr in output_attrs:
                        props[output_attr] = candidate.value[output_attr]
                else:
                    props[output_attr] = candidate.value
                break

    return None


def max_zoom_filter(ctx):
    """
    For features with a max_zoom, remove them if it's < nominal zoom.
    """

    params = _Params(ctx, 'max_zoom_filter')
    layers = params.required('layers', typ=list)
    nominal_zoom = ctx.nominal_zoom

    for layer_name in layers:
        layer = _find_layer(ctx.feature_layers, layer_name)

        features = layer['features']
        new_features = []

        for feature in features:
            _, props, _ = feature
            max_zoom = props.get('max_zoom')
            if max_zoom is None or max_zoom >= nominal_zoom:
                new_features.append(feature)

        layer['features'] = new_features

    return None


def min_zoom_filter(ctx):
    """
    For features with a min_zoom, remove them if it's > nominal zoom + 1.
    """

    params = _Params(ctx, 'min_zoom_filter')
    layers = params.required('layers', typ=list)
    nominal_zoom = ctx.nominal_zoom

    for layer_name in layers:
        layer = _find_layer(ctx.feature_layers, layer_name)

        features = layer['features']
        new_features = []

        for feature in features:
            _, props, _ = feature
            min_zoom = props.get('min_zoom')
            if min_zoom is not None and min_zoom < nominal_zoom + 1:
                new_features.append(feature)

        layer['features'] = new_features

    return None


def tags_set_ne_min_max_zoom(ctx):
    """
    Override the min zoom and max zoom properties with __ne_* variants from
    Natural Earth, if there are any.
    """

    params = _Params(ctx, 'tags_set_ne_min_max_zoom')
    layer_name = params.required('layer')
    layer = _find_layer(ctx.feature_layers, layer_name)

    for _, props, _ in layer['features']:
        min_zoom = props.pop('__ne_min_zoom', None)
        if min_zoom is not None:
            # don't overstuff features into tiles when they are in the
            # long tail of won't display, but make their min_zoom
            # consistent with when they actually show in tiles
            if min_zoom % 1 > 0.5:
                min_zoom = ceil(min_zoom)
            props['min_zoom'] = min_zoom

        elif props.get('kind') == 'country':
            # countries and regions which don't have a min zoom joined from NE
            # are probably either vandalism or unrecognised countries. either
            # way, we probably don't want to see them at zoom, which is lower
            # than most of the curated NE min zooms. see issue #1826 for more
            # information.
            props['min_zoom'] = max(6, props['min_zoom'])

        elif props.get('kind') == 'region':
            props['min_zoom'] = max(8, props['min_zoom'])

        max_zoom = props.pop('__ne_max_zoom', None)
        if max_zoom is not None:
            props['max_zoom'] = max_zoom

    return None


def whitelist(ctx):
    """
    Applies a whitelist to a particular property on all features in the layer,
    optionally also remapping some values.
    """

    params = _Params(ctx, 'whitelist')
    layer_name = params.required('layer')
    start_zoom = params.optional('start_zoom', default=0, typ=int)
    end_zoom = params.optional('end_zoom', typ=int)
    property_name = params.required('property')
    whitelist = params.required('whitelist', typ=list)
    remap = params.optional('remap', default={}, typ=dict)
    where = params.optional('where')

    # check that we're in the zoom range where this post-processor is supposed
    # to operate.
    if ctx.nominal_zoom < start_zoom:
        return None
    if end_zoom is not None and ctx.nominal_zoom >= end_zoom:
        return None

    if where is not None:
        where = compile(where, 'queries.yaml', 'eval')

    layer = _find_layer(ctx.feature_layers, layer_name)

    features = layer['features']
    for feature in features:
        _, props, _ = feature

        # skip this feature if there's a where clause and it evaluates falsey.
        if where is not None:
            local = props.copy()
            local['zoom'] = ctx.nominal_zoom
            if not eval(where, {}, local):
                continue

        value = props.get(property_name)
        if value is not None:
            if value in whitelist:
                # leave value as-is
                continue

            elif value in remap:
                # replace with replacement value
                props[property_name] = remap[value]

            else:
                # drop the property
                props.pop(property_name)

    return None


def remap(ctx):
    """
    Maps some values for a particular property to others. Similar to whitelist,
    but won't remove the property if there's no match.
    """

    params = _Params(ctx, 'remap')
    layer_name = params.required('layer')
    start_zoom = params.optional('start_zoom', default=0, typ=int)
    end_zoom = params.optional('end_zoom', typ=int)
    property_name = params.required('property')
    remap = params.optional('remap', default={}, typ=dict)
    where = params.optional('where')

    # check that we're in the zoom range where this post-processor is supposed
    # to operate.
    if ctx.nominal_zoom < start_zoom:
        return None
    if end_zoom is not None and ctx.nominal_zoom >= end_zoom:
        return None

    if where is not None:
        where = compile(where, 'queries.yaml', 'eval')

    layer = _find_layer(ctx.feature_layers, layer_name)

    features = layer['features']
    for feature in features:
        shape, props, _ = feature

        # skip this feature if there's a where clause and it evaluates falsey.
        if where is not None:
            local = props.copy()
            local['zoom'] = ctx.nominal_zoom
            local['geom_type'] = shape.geom_type
            if not eval(where, {}, local):
                continue

        value = props.get(property_name)
        if value in remap:
            # replace with replacement value
            props[property_name] = remap[value]

    return None


def backfill(ctx):
    """
    Backfills default values for some features. In other words, if the feature
    lacks some or all of the defaults, then set those defaults.
    """

    params = _Params(ctx, 'whitelist')
    layer_name = params.required('layer')
    start_zoom = params.optional('start_zoom', default=0, typ=int)
    end_zoom = params.optional('end_zoom', typ=int)
    defaults = params.required('defaults', typ=dict)
    where = params.optional('where')

    # check that we're in the zoom range where this post-processor is supposed
    # to operate.
    if ctx.nominal_zoom < start_zoom:
        return None
    if end_zoom is not None and ctx.nominal_zoom >= end_zoom:
        return None

    if where is not None:
        where = compile(where, 'queries.yaml', 'eval')

    layer = _find_layer(ctx.feature_layers, layer_name)

    features = layer['features']
    for feature in features:
        _, props, _ = feature

        # skip this feature if there's a where clause and it evaluates truthy.
        if where is not None:
            local = props.copy()
            local['zoom'] = ctx.nominal_zoom
            if not eval(where, {}, local):
                continue

        for k, v in defaults.iteritems():
            if k not in props:
                props[k] = v

    return None


def clamp_min_zoom(ctx):
    """
    Clamps the min zoom for features depending on context.
    """

    params = _Params(ctx, 'clamp_min_zoom')
    layer_name = params.required('layer')
    start_zoom = params.optional('start_zoom', default=0, typ=int)
    end_zoom = params.optional('end_zoom', typ=int)
    clamp = params.required('clamp', typ=dict)
    property_name = params.required('property')

    # check that we're in the zoom range where this post-processor is supposed
    # to operate.
    if ctx.nominal_zoom < start_zoom:
        return None
    if end_zoom is not None and ctx.nominal_zoom >= end_zoom:
        return None

    layer = _find_layer(ctx.feature_layers, layer_name)

    features = layer['features']
    for feature in features:
        _, props, _ = feature

        value = props.get(property_name)
        min_zoom = props.get('min_zoom')

        if value is not None and min_zoom is not None:
            min_val = clamp.get(value)
            if min_val is not None and min_val > min_zoom:
                props['min_zoom'] = min_val

    return None


def add_vehicle_restrictions(shape, props, fid, zoom):
    """
    Parse the maximum height, weight, length, etc... restrictions on vehicles
    and create the `hgv_restriction` and `hgv_restriction_shield_text`.
    """

    from math import floor

    def _one_dp(val, unit):
        deci = int(floor(10 * val))
        if deci % 10 == 0:
            return "%d%s" % (deci / 10, unit)
        return "%.1f%s" % (0.1 * deci, unit)

    def _metres(val):
        # parse metres or feet and inches, return cm
        metres = _to_float_meters(val)
        if metres:
            return True, _one_dp(metres, 'm')
        return False, None

    def _tonnes(val):
        tonnes = to_float(val)
        if tonnes:
            return True, _one_dp(tonnes, 't')
        return False, None

    def _false(val):
        return val == 'no', None

    Restriction = namedtuple('Restriction', 'kind parse')

    restrictions = {
        'maxwidth': Restriction('width', _metres),
        'maxlength': Restriction('length', _metres),
        'maxheight': Restriction('height', _metres),
        'maxweight': Restriction('weight', _tonnes),
        'maxaxleload': Restriction('wpa', _tonnes),
        'hazmat': Restriction('hazmat', _false),
    }

    hgv_restriction = None
    hgv_restriction_shield_text = None

    for osm_key, restriction in restrictions.items():
        osm_val = props.pop(osm_key, None)
        if osm_val is None:
            continue

        restricted, shield_text = restriction.parse(osm_val)
        if not restricted:
            continue

        if hgv_restriction is None:
            hgv_restriction = restriction.kind
            hgv_restriction_shield_text = shield_text

        else:
            hgv_restriction = 'multiple'
            hgv_restriction_shield_text = None

    if hgv_restriction:
        props['hgv_restriction'] = hgv_restriction
    if hgv_restriction_shield_text:
        props['hgv_restriction_shield_text'] = hgv_restriction_shield_text

    return shape, props, fid


def load_collision_ranker(fh):
    import yaml
    from vectordatasource.collision import CollisionRanker

    data = yaml.load(fh)
    assert isinstance(data, list)

    return CollisionRanker(data)


def add_collision_rank(ctx):
    """
    Add or update a collision_rank property on features in the given layers.
    The collision rank is looked up from a YAML file consisting of a list of
    filters (same syntax as in kind/min_zoom YAML) and "_reserved" blocks.
    Collision rank indices are automatically assigned based on where in the
    list a matching filter is found.
    """

    feature_layers = ctx.feature_layers
    zoom = ctx.nominal_zoom
    start_zoom = ctx.params.get('start_zoom', 0)
    end_zoom = ctx.params.get('end_zoom')
    ranker = ctx.resources.get('ranker')
    where = ctx.params.get('where')

    assert ranker, 'add_collision_rank: missing ranker resource'

    if zoom < start_zoom:
        return None

    if end_zoom is not None and zoom >= end_zoom:
        return None

    if where:
        where = compile(where, 'queries.yaml', 'eval')

    for layer in feature_layers:
        layer_name = layer['layer_datum']['name']
        for shape, props, fid in layer['features']:
            # use the "where" clause to limit the selection of features which
            # we add collision_rank to.
            add_collision_rank = True
            if where:
                local = defaultdict(lambda: None)
                local.update(props)
                local['layer_name'] = layer_name
                local['_has_name'] = _has_name(props)
                add_collision_rank = eval(where, {}, local)

            if add_collision_rank:
                props_with_layer = props.copy()
                props_with_layer['$layer'] = layer_name
                rank = ranker((shape, props_with_layer, fid))
                if rank is not None:
                    props['collision_rank'] = rank

    return None


# mappings from the fclass_XXX values in the Natural Earth disputed areas data
# to the matching Tilezen kind.
_REMAP_VIEWPOINT_KIND = {
    'Disputed (please verify)': 'disputed',
    'Indefinite (please verify)': 'indefinite',
    'Indeterminant frontier': 'indeterminate',
    'International boundary (verify)': 'country',
    'Lease limit': 'lease_limit',
    'Line of control (please verify)': 'line_of_control',
    'Overlay limit': 'overlay_limit',
    'Unrecognized': 'unrecognized',
    'Map unit boundary': 'map_unit',
    'Breakaway': 'disputed_breakaway',
    'Claim boundary': 'disputed_claim',
    'Elusive frontier': 'disputed_elusive',
    'Reference line': 'disputed_reference_line',
}


def remap_viewpoint_kinds(shape, props, fid, zoom):
    """
    Remap Natural Earth kinds in kind:* country viewpoints into the standard
    Tilezen nomenclature.
    """

    for key in props.keys():
        if key.startswith('kind:'):
            props[key] = _REMAP_VIEWPOINT_KIND.get(props[key])

    return (shape, props, fid)


def update_min_zoom(ctx):
    """
    Update the min zoom for features matching the Python fragment "where"
    clause. If none is provided, update all features.

    The new min_zoom is calculated by evaluating a Python fragment passed
    in through the "min_zoom" parameter. This is evaluated in the context
    of the features' parameters, plus a zoom variable.

    If the min zoom is lower than the current min zoom, the current one is
    kept. If the min zoom is increased, then it's checked against the
    current zoom and the feature dropped if it's not in range.
    """

    params = _Params(ctx, 'update_min_zoom')
    layer_name = params.required('source_layer')
    start_zoom = params.optional('start_zoom', typ=int, default=0)
    end_zoom = params.optional('end_zoom', typ=int)
    min_zoom = params.required('min_zoom')
    where = params.optional('where')

    layer = _find_layer(ctx.feature_layers, layer_name)
    zoom = ctx.nominal_zoom

    if zoom < start_zoom or \
       (end_zoom is not None and zoom >= end_zoom):
        return None

    min_zoom = compile(min_zoom, 'queries.yaml', 'eval')
    if where:
        where = compile(where, 'queries.yaml', 'eval')

    new_features = []
    for shape, props, fid in layer['features']:
        local = defaultdict(lambda: None)
        local.update(props)
        local['zoom'] = zoom

        if where and eval(where, {}, local):
            new_min_zoom = eval(min_zoom, {}, local)
            if new_min_zoom > props.get('min_zoom'):
                props['min_zoom'] = new_min_zoom
                if new_min_zoom >= zoom + 1 and zoom < 16:
                    # DON'T add feature - it's masked by min zoom.
                    continue

        new_features.append((shape, props, fid))

    layer['features'] = new_features
    return layer
