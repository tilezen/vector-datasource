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
# mapping where the keys are (layer, kind) tuples and the values are the other
# stuff we parsed out of the various YAML/CSV files.
KindKey = namedtuple('KindKey', 'layer kind')
KindInfo = namedtuple('KindInfo', 'min_zoom sort_rank')


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
def parse_filter_for_col(col, filter_defn):
    if col.startswith('tags->'):
        raise AssertionError("Output kind column starts with deprecated "
                             "'tags->' prefix: %r" % (col,))

    if col in filter_defn:
        value = filter_defn[col]
        if isinstance(value, list):
            return filter_defn[col]
        elif isinstance(value, (str, unicode)):
            return [value]
        else:
            raise ValueError("Don't know what to do with value of type "
                             "%s in %r" % (type(value), value))
    else:
        # complex case if we're not filtering on the column that we're using
        # as the output kind... hopefully it doesn't happen very much?
        raise ValueError("Don't know what to do with kind %r where it doesn't "
                         "appear in the filter %r" % (col, filter_defn))


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
def parse_case_for_kinds(case_stmt):
    all_kinds = []
    for case in case_stmt:
        if case.keys() == ['else']:
            all_kinds.append(case['else'])
        else:
            assert sorted(case.keys()) == ['then', 'when']
            value = case['then']
            assert isinstance(value, (str, unicode))
            all_kinds.append(value)

    return all_kinds


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


# need this to pass into the CSVMatcher, which expects a Shapely geometry.
FakeShape = namedtuple('FakeShape', 'type')


def parse_item(layer_name, item, sort_rank):
    kind = item['output'].get('kind')
    if not kind:
        return {}

    if isinstance(kind, (str, unicode)):
        all_kinds = [kind]

    elif isinstance(kind, dict):
        if kind.keys() == ['col']:
            all_kinds = parse_filter_for_col(kind['col'], item['filter'])

        elif kind.keys() == ['case']:
            all_kinds = parse_case_for_kinds(kind['case'])

        else:
            raise ValueError("Don't understand dict kind with keys %r in %r"
                             % (kind.keys(), kind))

    else:
        raise ValueError("Don't understand kind %s in %r" % (type(kind), kind))

    values = {}
    for k in all_kinds:
        key = KindKey(layer_name, k)

        # we need to fake up some of this data, so the sort ranks might not be
        # exactly correct...
        shape = FakeShape(None)
        props = {'kind': k}
        zoom = 16
        result = sort_rank(shape, props, zoom)
        if result is None:
            sort_rank_val = None
        else:
            sort_rank_key, sort_rank_val = result
            assert sort_rank_key == 'sort_rank'
            sort_rank_val = int(sort_rank_val)

        info = KindInfo(parse_start_zoom(item['min_zoom']), sort_rank_val)

        values[key] = info

    return values


def merge_info(a, b):
    if a.min_zoom <= b.min_zoom:
        return a
    else:
        return b


# default sort_rank function, for when we have no information
def no_matcher(shape, props, zoom):
    return None


def parse_all_kinds(yaml_path, sort_rank_path):
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
            kinds = parse_item(layer_name, item, sort_rank)
            for k, v in kinds.iteritems():
                prev_v = all_kinds.get(k)
                if prev_v is not None:
                    v = merge_info(prev_v, v)
                all_kinds[k] = v

    return all_kinds


if __name__ == '__main__':
    from vectordatasource.meta import find_yaml_path
    import argparse
    import os.path

    yaml_path = find_yaml_path()
    sort_rank_path = os.path.join(
        os.path.split(yaml_path)[0], 'spreadsheets', 'sort_rank')
    parser = argparse.ArgumentParser()
    parser.add_argument('--yaml-path', help='Directory containing YAML',
                        default=yaml_path)
    parser.add_argument('--sort-rank-path', help='Directory containing sort '
                        'rank CSVs.', default=sort_rank_path)
    args = parser.parse_args()

    if args.yaml_path:
        yaml_path = args.yaml_path

    if args.sort_rank_path:
        sort_rank_path = args.sort_rank_path

    all_kinds = parse_all_kinds(yaml_path, sort_rank_path)

    print "%12s %30s %8s %s" % ("LAYER", "KIND", "MIN_ZOOM", "SORT_RANK")
    for k in sorted(all_kinds):
        v = all_kinds[k]
        print "%12s %30s %8s %r" % (k.layer, k.kind, repr(v.min_zoom),
                                    v.sort_rank)
