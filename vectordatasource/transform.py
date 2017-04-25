# transformation functions to apply to features

from collections import defaultdict, namedtuple
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
station_pattern = re.compile('([^(]*)\(([^)]*)\).*')

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


def _building_calc_levels(levels):
    levels = max(levels, 1)
    levels = (levels * 3) + 2
    return levels


def _building_calc_min_levels(min_levels):
    min_levels = max(min_levels, 0)
    min_levels = min_levels * 3
    return min_levels


def _building_calc_height(height_val, levels_val, levels_calc_fn):
    height = _to_float_meters(height_val)
    if height is not None:
        return height
    levels = _to_float_meters(levels_val)
    if levels is None:
        return None
    levels = levels_calc_fn(levels)
    return levels


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
    if bridge in ('yes', 'true'):
        properties['is_bridge'] = True

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


def _iso639_1_code_of(lang):
    try:
        iso639_1_code = lang.iso639_1_code.encode('utf-8')
    except AttributeError:
        return None
    return iso639_1_code


# a structure to return language code lookup results preserving the priority
# (lower is better) of the result for use in situations where multiple inputs
# can map to the same output.
LangResult = namedtuple('LangResult', ['code', 'priority'])


def _convert_wof_l10n_name(x):
    lang_str_iso_639_3 = x[:3]
    if len(lang_str_iso_639_3) != 3:
        return None
    try:
        lang = pycountry.languages.get(iso639_3_code=lang_str_iso_639_3)
    except KeyError:
        return None
    return LangResult(code=_iso639_1_code_of(lang), priority=0)


def _normalize_osm_lang_code(x):
    # first try a 639-1 code
    try:
        lang = pycountry.languages.get(iso639_1_code=x)
    except KeyError:
        # next, try a 639-2 code
        try:
            lang = pycountry.languages.get(iso639_2T_code=x)
        except KeyError:
            # finally, try a 639-3 code
            try:
                lang = pycountry.languages.get(iso639_3_code=x)
            except KeyError:
                return None
    return _iso639_1_code_of(lang)


def _normalize_country_code(x):
    x = x.upper()
    try:
        c = pycountry.countries.get(alpha2=x)
    except KeyError:
        try:
            c = pycountry.countries.get(alpha3=x)
        except KeyError:
            try:
                c = pycountry.countries.get(numeric_code=x)
            except KeyError:
                return None
    alpha2_code = c.alpha2
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
    is_wof = source == 'whosonfirst.mapzen.com'
    is_osm = source == 'openstreetmap.org'

    if is_osm:
        alt_name_prefix_candidates = [
            'name:left:', 'name:right:', 'name:', 'alt_name:', 'old_name:'
        ]
        convert_fn = _convert_osm_l10n_name
    elif is_wof:
        alt_name_prefix_candidates = ['name:']
        convert_fn = _convert_wof_l10n_name
    else:
        # conversion function only implemented for things which come from OSM
        # or WOF - implement more cases here when more localized named sources
        # become available.
        return shape, properties, fid

    langs = {}
    for k, v in tags.items():
        if v == name:
            continue
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


# shared implementation of the intercut algorithm, used
# both when cutting shapes and using overlap to determine
# inside / outsideness.
def _intercut_impl(intersect_func, feature_layers,
                   base_layer, cutting_layer, attribute,
                   target_attribute, cutting_attrs,
                   keep_geom_type):
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

    # make a cutter object to help out
    cutter = _Cutter(cutting_features, cutting_attrs,
                     attribute, target_attribute,
                     keep_geom_type, intersect_func)

    for base_feature in base_features:
        # we use shape to track the current remainder of the
        # shape after subtracting bits which are inside cuts.
        shape, props, fid = base_feature

        cutter.cut(shape, props, fid)

    base['features'] = cutter.new_features

    return base


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

    return _intercut_impl(
        _intersect_cut, feature_layers, base_layer, cutting_layer,
        attribute, target_attribute, cutting_attrs, keep_geom_type)


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

    return _intercut_impl(
        _intersect_overlap(min_fraction), feature_layers, base_layer,
        cutting_layer, attribute, target_attribute, cutting_attrs,
        keep_geom_type)


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
                    boundary = boundary.difference(cut_shape)

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
                    inside, boundary = _intersect_cut(boundary, cut_shape)

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
    where = ctx.params.get('where')
    assert where, 'drop_features_where: missing where'

    if zoom < start_zoom:
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

    if end_zoom is not None and zoom > end_zoom:
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

        # copy params to add a 'zoom' one. would prefer '$zoom', but apparently
        # that's not allowed in python syntax.
        local = props.copy()
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
    assert properties, 'drop_properties: missing properties'

    def action(p):
        return _remove_properties(p, *properties)

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

    if end_zoom is not None and zoom > end_zoom:
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
    if end_zoom is not None and zoom > end_zoom:
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
    if end_zoom is not None and zoom > end_zoom:
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
    if end_zoom is not None and zoom > end_zoom:
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
    result = int(step * round(val / float(step)))
    return result


def quantize_height_round_nearest_5_meters(height):
    return quantize_val(height, 5)


def quantize_height_round_nearest_10_meters(height):
    return quantize_val(height, 10)


def quantize_height_round_nearest_meter(height):
    return round(height)


def _merge_lines(linestring_shapes):
    list_of_linestrings = []
    for shape in linestring_shapes:
        list_of_linestrings.extend(_flatten_geoms(shape))
    multi = MultiLineString(list_of_linestrings)
    result = _linemerge(multi)
    return result


def _merge_polygons(polygon_shapes):
    list_of_polys = []
    for shape in polygon_shapes:
        list_of_polys.extend(_flatten_geoms(shape))
    result = shapely.ops.unary_union(list_of_polys)
    return result


def _merge_features_by_property(
        features, geom_dim,
        update_props_pre_fn=None,
        update_props_post_fn=None,
        max_merged_features=None):

    assert geom_dim in (_POLYGON_DIMENSION, _LINE_DIMENSION)
    if geom_dim == _LINE_DIMENSION:
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
            features_by_property[frozen_props][-1].append(shape)
        else:
            features_by_property[frozen_props] = (
                (fid, p_id, orig_props, [shape]))

    new_features = []
    for frozen_props, (fid, p_id, orig_props, shapes) in \
            features_by_property.iteritems():

        if len(shapes) == 1:
            # restore original properties if we only have a single shape
            new_features.append((shapes[0], orig_props, fid))
            continue

        num_shapes = len(shapes)
        shapes_per_merge = num_shapes
        if max_merged_features and max_merged_features < shapes_per_merge:
            shapes_per_merge = max_merged_features
            # reset fid if we're going to split up features, as we don't want
            # them all to have duplicate IDs.
            fid = None

        for i in range(0, num_shapes, shapes_per_merge):
            j = min(num_shapes, i + shapes_per_merge)
            merged_shape = _merge_shape_fn(shapes[i:j])

            # thaw the frozen properties to use in the new feature.
            props = _thaw(frozen_props)

            if update_props_post_fn:
                props = update_props_post_fn((merged_shape, props, fid))

            new_features.append((merged_shape, props, fid))

    new_features.extend(skipped_features)
    return new_features


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
    if end_zoom is not None and zoom > end_zoom:
        return None

    quantize_height_fn = None
    quantize_cfg = ctx.params.get('quantize')
    if quantize_cfg:
        quantize_fn_dotted_name = quantize_cfg.get(zoom)
        if quantize_fn_dotted_name:
            quantize_height_fn = resolve(quantize_fn_dotted_name)

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

        if quantize_height_fn:
            height = props.get('height', None)
            if height is not None:
                props['height'] = quantize_height_fn(height)

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
        layer['features'], _POLYGON_DIMENSION, _props_pre, _props_post,
        max_merged_features)
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

    assert source_layer, 'merge_polygon_features: missing source layer'
    layer = _find_layer(ctx.feature_layers, source_layer)
    if layer is None:
        return None

    if zoom < start_zoom:
        return None
    if end_zoom is not None and zoom > end_zoom:
        return None

    def _props_pre((shape, props, fid)):
        # drop area while merging, as we'll recalculate after.
        props.pop('area', None)
        return props

    def _props_post((merged_shape, props, fid)):
        # add the area back in
        area = int(merged_shape.area)
        props['area'] = area
        return props

    layer['features'] = _merge_features_by_property(
        layer['features'], _POLYGON_DIMENSION, _props_pre, _props_post)
    return layer


def merge_line_features(ctx):
    """
    Merge linestrings having the same properties, in the source_layer
    between start_zoom and end_zoom inclusive.
    """

    zoom = ctx.nominal_zoom
    source_layer = ctx.params.get('source_layer')
    start_zoom = ctx.params.get('start_zoom', 0)
    end_zoom = ctx.params.get('end_zoom')

    assert source_layer, 'merge_line_features: missing source layer'
    layer = _find_layer(ctx.feature_layers, source_layer)
    if layer is None:
        return None

    if zoom < start_zoom:
        return None
    if end_zoom is not None and zoom > end_zoom:
        return None

    layer['features'] = _merge_features_by_property(
        layer['features'], _LINE_DIMENSION)
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

        if barrier is not None:
            if barrier == 'fence':
                # filter only linestring-like objects. we don't
                # want any points which might have been created
                # by the intersection.
                filtered_shape = _filter_geom_types(shape, _POLYGON_DIMENSION)

                if not filtered_shape.is_empty:
                    new_props = _make_new_properties(props, prop_transform)
                    new_props['kind'] = 'fence'
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

    if end_zoom is not None and zoom > end_zoom:
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

    if end_zoom is not None and zoom > end_zoom:
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

    if end_zoom and zoom > end_zoom:
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

    if end_zoom is not None and zoom > end_zoom:
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

        # The logic behind simplifying before intersecting rather than the
        # other way around is extensively explained here:
        # https://github.com/mapzen/TileStache/blob/d52e54975f6ec2d11f63db13934047e7cd5fe588/TileStache/Goodies/VecTiles/server.py#L509,L527
        simplify_before_intersect = layer_datum['simplify_before_intersect']

        # perform any simplification as necessary
        simplify_start = layer_datum['simplify_start']
        should_simplify = simplify_start <= zoom < simplify_before

        for shape, props, feature_id in feature_layer['features']:

            geom_type = normalize_geometry_type(shape.type)
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
                    tolerance, preserve_topology=True)
                shape = _make_valid_if_necessary(simplified_shape)

            if is_clipped:
                shape = shape.intersection(layer_padded_bounds)

            if should_simplify and not simplify_before_intersect:
                simplified_shape = shape.simplify(tolerance,
                                                  preserve_topology=True)
                shape = _make_valid_if_necessary(simplified_shape)

            # this could alter multipolygon geometries
            if zoom < simplify_before:
                shape = _visible_shape(shape, area_threshold_meters)

            # don't keep features which have been simplified to empty or
            # None.
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


def merge_networks_from_tags(shape, props, fid, zoom):
    """
    Take the network and ref tags from the feature and, if they both exist, add
    them to the mz_networks list. This is to make handling of networks and refs
    more consistent across elements.
    """

    network = props.get('network')
    ref = props.get('ref')
    mz_networks = props.get('mz_networks', [])

    if network and ref:
        props.pop('network')
        props.pop('ref')
        mz_networks.extend([_guess_type_from_network(network), network, ref])
        props['mz_networks'] = mz_networks

    return (shape, props, fid)


def _road_network_importance(network, ref):
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
    elif network == 'US:I' or ':national' in network:
        network_code = 1
    elif network == 'US:US' or ':regional' in network:
        network_code = 2
    else:
        network_code = len(network.split(':')) + 3

    try:
        ref = max(int(ref or 0), 0)
    except ValueError:
        ref = 0

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


_NUMBER_AT_FRONT = re.compile('^(\d+\w*)', re.UNICODE)
_LETTER_THEN_NUMBERS = re.compile('^[^\d\s_]+[ -]?([^\s]+)',
                                  re.UNICODE | re.IGNORECASE)
_UA_TERRITORIAL_RE = re.compile('^(\w)-(\d+)-(\d+)$',
                                re.UNICODE | re.IGNORECASE)


def _road_shield_text(network, ref):
    """
    Try to extract the string that should be displayed within the road shield,
    based on the raw ref and the network value.
    """

    if ref is None:
        return None

    if isinstance(ref, unicode):
        # no need to do anything, it's already okay
        pass
    elif isinstance(ref, str):
        # it's UTF-8 encoded bytes, so make it a unicode
        ref = unicode(ref, 'utf-8')
    else:
        # dunno what this is?!!
        return None

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
    _road_network_importance)
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

            shield_texts = list()
            network_names = list()
            for network_name, ref in vals:
                network_names.append(network_name)
                shield_texts.append(network.shield_text_fn(network_name, ref))

            properties[all_networks] = network_names
            properties[all_shield_texts] = shield_texts

    return (shape, properties, fid)


def _choose_most_important_network(properties, network):
    """
    Use the `_network_importance` function to select any road networks from
    `all_networks` and `all_shield_texts`, taking the most important one.
    """

    prefix = network.prefix
    all_networks = 'all_' + prefix + 'networks'
    all_shield_texts = 'all_' + prefix + 'shield_texts'

    networks = properties.pop(all_networks, None)
    shield_texts = properties.pop(all_shield_texts, None)

    if networks and shield_texts:
        def network_key(t):
            return network.network_importance_fn(*t)

        tuples = sorted(zip(networks, shield_texts), key=network_key)

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
        properties = _choose_most_important_network(properties, net)

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
