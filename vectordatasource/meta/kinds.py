from collections import namedtuple


# we don't have data to evaluate the function, so this just looks up the
# minimum possible value the function could return.
KNOWN_FUNCS = {
    'mz_calculate_path_major_route': 8,
    'mz_get_min_zoom_highway_level_gate': 14,
    'tz_looks_like_service_area': 13,
    'tz_looks_like_rest_area': 13,
    'mz_calculate_ferry_level': 8,
}


# structures to return data from the parsing functions. basically a key->value
# mapping where the keys are (layer, kind, kind_detail) tuples and the values
# are the other stuff we parsed out of the various YAML/CSV files.
#
# note that kind_detail might be None if the command line options are
# configured to ignore that.
KindKey = namedtuple('KindKey', 'layer kind kind_detail')
KindInfo = namedtuple('KindInfo', 'min_zoom sort_rank')


def _valid_values(filter_defn, col):
    """
    Get the valid values from the filter_defn for column named col.

    Returns a list of the valid values.
    """

    value = filter_defn[col]
    if isinstance(value, list):
        return filter_defn[col]
    elif isinstance(value, (str, unicode)):
        return [value]
    else:
        raise ValueError("Don't know what to do with value of type "
                         "%s in %r" % (type(value), value))


# parses the values for a column out of a filter definition. this is used when
# the output defines "kind: {col: some_column}", and we want to find out what
# values "some_column" could have.
#
# this is most often seen in things such as:
#
#  - filter:
#      amenity: [bus_station, car_rental, recycling, shelter]
#    min_zoom: 16
#    output:
#      <<: *output_properties
#      kind: {col: amenity}
#
# where we've white-listed the amenity values in the filter, so we know all the
# possible values that the kind can have.
#
# theoretically, this can be arbitrarily complex, but it turns out that in all
# the cases we have at the time of writing, the whitelist is available at the
# top level of the filter! lucky us :-)
def parse_filter_for_col(col, item):
    filter_defn = item['filter']

    if col.startswith('tags->'):
        raise AssertionError("Output kind column starts with deprecated "
                             "'tags->' prefix: %r" % (col,))

    if col in filter_defn:
        return _valid_values(filter_defn, col)

    # if the top key of the filter is "all", then we can use any of the
    # sub-filters.
    if filter_defn.keys() == ['all']:
        for subfilter in filter_defn['all']:
            if col in subfilter:
                return _valid_values(subfilter, col)

    # complex case if we're not filtering on the column that we're using
    # as the output kind... hopefully it doesn't happen very much?
    raise ValueError("Don't know what to do with column %r where it "
                     "doesn't appear in the filter %r" %
                     (col, filter_defn))


# parse a "case" statement to get all the possible values. we use this
# sometimes to set the kind, e.g:
#
#  - filter: {leisure: sports_centre}
#    min_zoom: ...
#    output:
#      <<: *output_properties
#      kind:
#        case:
#          - when:
#              sport: ['fitness', 'gym']
#            then: 'fitness'
#          - else: 'sports_centre'
#
# which means the kind could be either "fitness" or "sports_centre", and should
# return both.
def parse_case_for_kinds(case_stmt, item):
    all_kinds = []
    has_else = False
    for case in case_stmt:
        if case.keys() == ['else']:
            values = parse_col_values(case['else'], item)
            has_else = True

        else:
            assert sorted(case.keys()) == ['then', 'when']
            when = case['when']
            then = case['then']

            # if the when statement whitelists its own col, then we can use
            # that. otherwise, we have to look in the filter.
            if isinstance(then, dict) and \
               then.keys() == ['col'] and \
               then['col'] in when:
                col = then['col']
                values = parse_col_values(when[col], item)
            else:
                values = parse_col_values(then, item)

        assert isinstance(values, list)
        for value in values:
            assert isinstance(value, (str, unicode, type(None)))
        all_kinds.extend(values)

    # if there's no else statement, then the fall-through default is None
    if not has_else and None not in all_kinds:
        all_kinds.append(None)

    return all_kinds


def parse_lookup_for_kinds(lookup_stmt, item):
    """
    Parse a lookup statement to get all the possible return values.
    """

    any_default = False
    all_kinds = set()

    op = {
        '>=': lambda x, y: x >= y,
        '<=': lambda x, y: x <= y,
        '==': lambda x, y: x == y,
    }[lookup_stmt['op']]

    all_table_keys = parse_col_values(lookup_stmt['key'], item)
    for key in all_table_keys:
        for output, comparison in lookup_stmt['table']:
            if op(comparison, key):
                all_kinds.add(output)
                break
        else:
            any_default = True

    if any_default:
        if 'default' in lookup_stmt:
            for val in parse_col_values(lookup_stmt['default'], item):
                all_kinds.add(val)
        else:
            all_kinds.add(None)

    return list(all_kinds)


def parse_start_zoom(expr):
    """
    Parse the min zoom expression to find the minimum min_zoom at which the
    feature could appear.
    """

    if isinstance(expr, (int, float)):
        start_zoom = expr

    elif isinstance(expr, dict):
        if expr.keys() == ['col']:
            # if this is the special "zoom" column, then we know it's based on
            # area, and theoretically could be zero???
            if expr['col'] == 'zoom':
                start_zoom = 0
            else:
                # this could come from anywhere, so we don't have a clue what
                # it might be. therefore, return a value which means unknown.
                start_zoom = None

        elif expr.keys() == ['lookup']:
            table = expr['lookup']['table']
            start_zoom = min(row[0] for row in table)

        elif expr.keys() == ['case']:
            # take the min of all the branches
            branches = []
            for case in expr['case']:
                if case.keys() == ['else']:
                    branches.append(parse_start_zoom(case['else']))

                else:
                    assert sorted(case.keys()) == ['then', 'when']
                    branches.append(parse_start_zoom(case['then']))

            start_zoom = min(*branches)

        elif expr.keys() == ['min']:
            start_zoom = min(parse_start_zoom(item) for item in expr['min'])

        elif expr.keys() == ['max']:
            start_zoom = max(parse_start_zoom(item) for item in expr['max'])

        elif expr.keys() == ['clamp']:
            clamp = expr['clamp']
            start_zoom = max(parse_start_zoom(clamp['min']),
                             parse_start_zoom(clamp['value']))

        elif expr.keys() == ['sum']:
            start_zoom = sum(parse_start_zoom(item) for item in expr['sum'])

        elif expr.keys() == ['mul']:
            start_zoom = 1
            for item in expr['mul']:
                start_zoom *= parse_start_zoom(item)

        elif expr.keys() == ['call']:
            # we can perhaps figure this out for some functions and stash the
            # results as constants?
            func = expr['call']['func']
            start_zoom = KNOWN_FUNCS.get(func)

        else:
            raise AssertionError("Unknown min zoom expression %r in %r"
                                 % (expr.keys(), expr))

    else:
        raise AssertionError("Unknown min zoom expression type %s in %r"
                             % (type(expr), expr))

    return start_zoom


_RETURN_VALUES = {
    'mz_building_kind_detail': [
        None,
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
        'mixed_use',
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
        'works',
    ],
    'mz_building_part_kind_detail': [
        None,
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
        'window',
    ],
}


def all_possible_return_values_of(func):
    return _RETURN_VALUES[func]


# need this to pass into the CSVMatcher, which expects a Shapely geometry.
FakeShape = namedtuple('FakeShape', 'type')


def parse_col_values(col, item):
    if isinstance(col, (str, unicode)):
        all_kinds = [col]

    elif col is None:
        all_kinds = [None]

    elif isinstance(col, list):
        for c in col:
            assert isinstance(c, (str, unicode))

        all_kinds = col

    elif isinstance(col, dict):
        if col.keys() == ['col']:
            all_kinds = parse_filter_for_col(col['col'], item)

        elif col.keys() == ['case']:
            all_kinds = parse_case_for_kinds(col['case'], item)

        elif col.keys() == ['call']:
            all_kinds = all_possible_return_values_of(col['call']['func'])

        elif col.keys() == ['lookup']:
            all_kinds = parse_lookup_for_kinds(col['lookup'], item)

        else:
            raise ValueError("Don't understand dict column with keys %r in %r"
                             % (col.keys(), col))

    else:
        raise ValueError("Don't understand column %s in %r" % (type(col), col))

    return all_kinds


def parse_item(layer_name, item, sort_rank, include_kind_detail):
    kind = item['output'].get('kind')
    if not kind:
        return {}

    all_kinds = parse_col_values(kind, item)

    kind_detail = item['output'].get('kind_detail')
    if kind_detail:
        kind_details = parse_col_values(kind_detail, item)
    else:
        kind_details = [None]

    values = {}
    for k in all_kinds:
        for kind_detail in kind_details:
            assert isinstance(k, (str, unicode))
            assert isinstance(kind_detail, (str, unicode, type(None)))

            # we need to fake up some of this data, so the sort ranks might
            # not be exactly correct...
            shape = FakeShape(None)
            props = {'kind': k, 'kind_detail': kind_detail}
            zoom = 16
            result = sort_rank(shape, props, zoom)
            if result is None:
                sort_rank_val = None
            else:
                sort_rank_key, sort_rank_val = result
                assert sort_rank_key == 'sort_rank'
                sort_rank_val = int(sort_rank_val)

            info = KindInfo(parse_start_zoom(item['min_zoom']), sort_rank_val)

            kd = kind_detail if include_kind_detail else None
            key = KindKey(layer_name, k, kd)
            val = values.get(key)

            if include_kind_detail or val is None:
                values[key] = info

            else:
                # if we are not including kind detail, still need to aggregate
                # all the different kind detail min zooms and sort ranks.
                values[key] = merge_info(val, info)

    return values


def merge_info(a, b):
    if a.min_zoom <= b.min_zoom:
        return a
    else:
        return b


# default sort_rank function, for when we have no information
def no_matcher(shape, props, zoom):
    return None


def parse_all_kinds(yaml_path, sort_rank_path, include_kind_detail):
    from glob import glob
    from os.path import join, split, exists
    from yaml import load as yaml_load
    from vectordatasource.transform import CSVMatcher

    all_kinds = {}
    for yaml_file in glob(join(yaml_path, '*.yaml')):
        layer_name = split(yaml_file)[1][:-5]
        with open(yaml_file, 'r') as fh:
            yaml_data = yaml_load(fh)

        # by default, we don't have any sort_rank information
        sort_rank = no_matcher

        # look for a spreadsheet for sort_rank
        csv_file = join(yaml_path, '..', 'spreadsheets', 'sort_rank',
                        '%s.csv' % layer_name)
        if exists(csv_file):
            with open(csv_file, 'r') as fh:
                sort_rank = CSVMatcher(fh)

        for item in yaml_data['filters']:
            kinds = parse_item(layer_name, item, sort_rank,
                               include_kind_detail)
            for k, v in kinds.iteritems():
                prev_v = all_kinds.get(k)
                if prev_v is not None:
                    v = merge_info(prev_v, v)
                all_kinds[k] = v

    return all_kinds
