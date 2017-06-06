from collections import namedtuple
from numbers import Number
from vectordatasource import util
from vectordatasource.meta import function
import ast
import astformatter
import os.path
import sys
import yaml


# this captures the end result of processing a layer's yaml
# layer: name of layer
# ast: ast parsed function
# fn: compiled callable
FunctionData = namedtuple('FunctionData', 'layer ast fn')


# stores any useful state along the way as the values have been parsed
class AstState(object):

    def __init__(self, has_way_area, has_volume):
        self.has_way_area = has_way_area
        self.has_volume = has_volume


def parse_case(ast_state, c):
    assert isinstance(c, list)

    expr = ast.Name('None', ast.Load())
    if len(c) == 0:
        return expr

    if len(c) > 1:
        if c[-1].keys() == ['else']:
            last = c.pop()
            expr = ast_value(ast_state, last['else'])

    for case in reversed(c):
        assert isinstance(case, dict)
        assert set(case.keys()) == set(['when', 'then'])
        cond = create_rules_from_branch(case['when'])
        when = ast_value(ast_state, cond)
        then = ast_value(ast_state, case['then'])
        expr = ast.IfExp(when, then, expr)

    return expr


def parse_call(ast_state, c):
    assert set(c.keys()) == set(('args', 'func'))
    args = c['args']
    func = c['func']
    args_ast = [ast_value(ast_state, x) for x in args]
    return ast.Call(
        ast.Name(func, ast.Load()), args_ast, [], None, None)


def ast_value(ast_state, val):
    if isinstance(val, str):
        return ast.Str(val)
    elif isinstance(val, dict):
        if val.keys() == ['col']:
            return ast_column(ast_state, val['col'])
        elif val.keys() == ['expr']:
            raise Exception('expr not supported')
        elif 'case' in val.keys():
            return parse_case(ast_state, val['case'])
        elif val.keys() == ['call']:
            return parse_call(ast_state, val['call'])
        else:
            return ast.Dict([ast_value(ast_state, k) for k in val.keys()],
                            [ast_value(ast_state, v) for v in val.values()])
    elif isinstance(val, int):
        return ast.Num(val)
    elif hasattr(val, 'as_ast') and callable(val.as_ast):
        return val.as_ast(ast_state)
    elif val is None:
        return ast.Name('None', ast.Load())
    elif isinstance(val, list):
        return ast.List([ast_value(ast_state, v) for v in val], ast.Load())
    else:
        raise Exception("Don't understand AST value of %r" % val)


def untag_col(col):
    tags = 'tags->'
    if col.startswith(tags):
        col = col[len(tags):]
    return col


def ast_column(ast_state, col):
    col = untag_col(col)
    if col == 'volume':
        ast_state.has_way_area = True
        ast_state.has_volume = True
        result = ast.Name('volume', ast.Load())
    elif col == 'way_area':
        ast_state.has_way_area = True
        result = ast.Name('way_area', ast.Load())
    else:
        result = ast.Call(
            ast.Attribute(
                ast.Name('props', ast.Load()),
                'get',
                ast.Load()),
            [ast.Str(col)],
            [], None, None)
    return result


class EqualsRule(object):

    def __init__(self, column, value):
        self.column = column
        self.value = value

    def as_ast(self, ast_state):
        return ast.Compare(ast_column(ast_state, self.column),
                           [ast.Eq()],
                           [ast_value(ast_state, self.value)])


class GreaterOrEqualsRule(object):
    def __init__(self, column, value):
        self.column = column
        self.value = value

    def as_ast(self, ast_state):
        return ast.Compare(ast_column(ast_state, self.column),
                           [ast.GtE()],
                           [ast_value(ast_state, self.value)])


class SetRule(object):

    def __init__(self, column, values):
        self.column = column
        self.values = values

    def as_ast(self, ast_state):
        values = ast.Tuple(
            [ast_value(ast_state, v) for v in self.values], ast.Load())
        return ast.Compare(ast_column(ast_state, self.column),
                           [ast.In()],
                           [values])


class ExistsRule(object):

    def __init__(self, column):
        self.column = column

    def as_ast(self, ast_state):
        return ast.Compare(ast.Str(untag_col(self.column)),
                           [ast.In()],
                           [ast.Name('props', ast.Load())])


class NotExistsRule(object):

    def __init__(self, column):
        self.column = column

    def as_ast(self, ast_state):
        return ast.Compare(ast_column(ast_state, self.column),
                           [ast.Is()],
                           [ast.Name('None', ast.Load())])


class AndRule(object):

    def __init__(self, rules):
        self.rules = rules

    def as_ast(self, ast_state):
        return ast.BoolOp(
            ast.And(),
            [ast_value(ast_state, r) for r in self.rules])


class OrRule(object):

    def __init__(self, rules):
        self.rules = rules

    def as_ast(self, ast_state):
        return ast.BoolOp(
            ast.Or(),
            [ast_value(ast_state, r) for r in self.rules])


class NotRule(object):

    def __init__(self, rule):
        self.rule = rule

    def as_ast(self, ast_state):
        return ast.UnaryOp(
            ast.Not(),
            ast_value(ast_state, self.rule))


def map_geom_type(geom_type):
    titled = geom_type.title()
    result = (titled, 'Multi' + titled)
    return result


class GeomTypeRule(object):

    def __init__(self, geom_type):
        assert geom_type in ('point', 'line', 'polygon')
        self.geom_type = geom_type

    def as_ast(self, ast_state):
        attr = ast.Attribute(
            ast.Name('shape', ast.Load()),
            'type',
            ast.Load()
        )
        geom_types = map_geom_type(self.geom_type)
        geom_types_ast = map(ast.Str, geom_types)
        result = ast.Compare(
            attr, [ast.In()], [ast.Tuple(geom_types_ast, ast.Load())])
        return result


def create_rules_from_branch(filter_level, combinator=AndRule):
    # helper to create rules by recursing down an particular branch
    rules = []
    if not isinstance(filter_level, list):
        filter_level = [filter_level]
    for filter_level_item in filter_level:
        for k, v in filter_level_item.items():
            rule = create_filter_rule(k, v)
            rules.append(rule)
    assert rules, 'No rules specified in level: %s' % filter_level
    if len(rules) > 1:
        rule = combinator(rules)
    else:
        rule = rules[0]
    return rule


def create_filter_rule(filter_key, filter_value):
    # check for the composite rules first
    if filter_key == 'not':
        rule = create_rules_from_branch(filter_value)
        rule = NotRule(rule)
    elif filter_key == 'all':
        rule = create_rules_from_branch(filter_value)
    elif filter_key == 'any':
        rule = create_rules_from_branch(filter_value, combinator=OrRule)
    else:
        # leaf rules
        col = filter_key
        if isinstance(filter_value, list):
            rule = SetRule(col, filter_value)
        else:
            if filter_value is True:
                rule = ExistsRule(col)
            elif filter_value is False:
                rule = NotExistsRule(col)
            elif isinstance(filter_value, Number):
                rule = EqualsRule(col, filter_value)
            elif isinstance(filter_value, dict) and 'min' in filter_value:
                rule = GreaterOrEqualsRule(col, filter_value['min'])
            elif isinstance(filter_value, dict) and 'expr' in filter_value:
                raise Exception('expr not supported')
            elif col == 'geom_type':
                rule = GeomTypeRule(filter_value)
            else:
                rule = EqualsRule(col, filter_value)
    return rule


class Matcher(object):

    def __init__(self, rule, output):
        self.rule = rule
        self.output = output

    def as_ast(self, ast_state):
        return ast.If(
            self.rule.as_ast(ast_state),
            [ast.Return(
                ast_value(ast_state, self.output))],
            [])


def create_matcher(yaml_datum):
    rules = []
    filters = yaml_datum['filter']
    if not isinstance(filters, list):
        filters = [filters]
    for f in filters:
        for k, v in f.items():
            rule = create_filter_rule(k, v)
            rules.append(rule)
    assert rules, 'No filter rules found in %s' % yaml_datum
    if len(rules) > 1:
        rule = AndRule(rules)
    else:
        rule = rules[0]

    output = yaml_datum['output']
    assert 'kind' in output, \
        "Matcher for %r doesn't contain kind." % yaml_datum

    matcher = Matcher(rule, output)
    return matcher


def make_function_name(layer_name):
    return '%s_props' % layer_name


def make_way_area_assignment():
    # generates:
    # way_area = util.calculate_way_area(shape)
    return ast.Assign(
        targets=[ast.Name(id='way_area', ctx=ast.Store())],
        value=ast.Call(
            func=ast.Attribute(
                value=ast.Name(id='util', ctx=ast.Load()),
                attr='calculate_way_area', ctx=ast.Load()),
            args=[ast.Name(id='shape', ctx=ast.Load())],
            keywords=[], starargs=None, kwargs=None))


def make_volume_assignment():
    # generates:
    # volume = util.calculate_volume(way_area, props)
    return ast.Assign(
        targets=[ast.Name(id='volume', ctx=ast.Store())],
        value=ast.Call(
            func=ast.Attribute(
                value=ast.Name(id='util', ctx=ast.Load()),
                attr='calculate_volume', ctx=ast.Load()),
            args=[
                ast.Name(id='way_area', ctx=ast.Load()),
                ast.Name(id='props', ctx=ast.Load())],
            keywords=[], starargs=None, kwargs=None))


def parse_layer_from_yaml(ast_state, yaml_data, layer_name):
    matchers = []
    for yaml_datum in yaml_data['filters']:
        matcher = create_matcher(yaml_datum)
        matchers.append(matcher)
    stmts = []
    for matcher in matchers:
        # columns in the query should be those needed by the rule, union those
        # needed by the output, minus any which are synthetic and local to the
        # query function.
        stmts.append(matcher.as_ast(ast_state))

    prepend_statements = []
    if ast_state.has_way_area:
        way_area_stmt = make_way_area_assignment()
        prepend_statements.append(way_area_stmt)
    if ast_state.has_volume:
        volume_stmt = make_volume_assignment()
        prepend_statements.append(volume_stmt)
    stmts = prepend_statements + stmts

    func = ast.FunctionDef(
        make_function_name(layer_name),
        ast.arguments([
            ast.Name('shape', ast.Param()),
            ast.Name('props', ast.Param()),
            ast.Name('fid', ast.Param()),
        ], None, None, []),
        stmts,
        [])
    return func


def make_empty_ast_state():
    return AstState(False, False)


def parse_layers(yaml_path):
    layer_data = []
    layers = ('landuse', 'pois', 'transit', 'water', 'places', 'boundaries',
              'buildings', 'roads', 'earth')

    scope = {}
    # add in all functions into scope for call availability
    for func_name in dir(function):
        fn = getattr(function, func_name)
        if callable(fn):
            scope[func_name] = fn
    scope['util'] = util

    for layer in layers:
        file_path = os.path.join(yaml_path, '%s.yaml' % layer)
        with open(file_path) as fh:
            yaml_data = yaml.load(fh)

        ast_state = make_empty_ast_state()
        ast_fn = parse_layer_from_yaml(ast_state, yaml_data, layer)

        mod = ast.Module([ast_fn])
        mod_with_linenos = ast.fix_missing_locations(mod)
        code = compile(mod_with_linenos, '<string>', 'exec')
        exec code in scope
        compiled_fn = scope[make_function_name(layer)]
        layer_datum = FunctionData(layer, ast_fn, compiled_fn)
        layer_data.append(layer_datum)
    return layer_data


def main(argv=None):
    from vectordatasource.meta import find_yaml_path
    if argv is None:
        argv = sys.argv
    yaml_path = find_yaml_path()
    layer_data = parse_layers(yaml_path)
    for layer_datum in layer_data:
        ast_fn = layer_datum.ast
        print astformatter.ASTFormatter().format(ast_fn, mode='exec')


if __name__ == '__main__':
    main()
