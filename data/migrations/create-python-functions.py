import os.path
import yaml
from numbers import Number
import ast
from astformatter import ASTFormatter


def format_value(val):
    if isinstance(val, dict):
        if 'expr' in val:
            raise Exception('expr values not supported any more! value was %r' % val['expr'])
        elif 'col' in val:
            if val['col'].startswith('tags->'):
                return "tags->'%s'" % val['col'][len('tags->'):]
            else:
                return '"%s"' % val['col']
        elif 'value' in val:
            return "'%s'" % val['value']
        else:
            assert 0, 'Unknown dict value: %r' % val
    if isinstance(val, int):
        return "%s" % val
    else:
        return "'%s'" % val


def parse_case(c):
    assert isinstance(c, list)

    expr = ast.Name('None', None)
    if len(c) == 0:
        return expr

    if len(c) > 1:
        if c[-1].keys() == ['else']:
            last = c.pop()
            expr = ast_value(last['else'])

    for case in reversed(c):
        assert isinstance(case, dict)
        assert set(case.keys()) == set(['when', 'then'])
        cond = create_level_filter_rule(case['when'])
        when = ast_value(cond)
        then = ast_value(case['then'])
        expr = ast.IfExp(when, then, expr)

    return expr


def parse_call(c):
    # TODO!
    return ast.Name('None', None)


def ast_value(val):
    if isinstance(val, str):
        return ast.Str(val)
    elif isinstance(val, dict):
        if val.keys() == ['col']:
            return ast_column(val['col'])
        elif val.keys() == ['expr']:
            raise Exception('parse sql ... ?')
        elif val.keys() == ['case']:
            return parse_case(val['case'])
        elif val.keys() == ['call']:
            return parse_call(val['call'])
        else:
            return ast.Dict([ast_value(k) for k in val.keys()],
                            [ast_value(v) for v in val.values()])
    elif isinstance(val, int):
        return ast.Num(val)
    elif hasattr(val, 'as_ast') and callable(val.as_ast):
        return val.as_ast()
    elif val is None:
        return ast.Name('None', None)
    elif isinstance(val, list):
        return ast.List([ast_value(v) for v in val], None)
    else:
        raise Exception("Don't understand AST value of %r" % val)


def untag_col(col):
    tags = 'tags->'
    if col.startswith(tags):
        col = col[len(tags):]
    return col

def ast_column(col):
    col = untag_col(col)
    return ast.Call(
        ast.Attribute(
            ast.Name('tags', None),
            'get',
            None),
        [ast.Str(col)],
        [], None, None)


class EqualsRule(object):

    def __init__(self, column, value):
        self.column = column
        self.value = value

    def as_ast(self):
        return ast.Compare(ast_column(self.column),
                           [ast.Eq()],
                           [ast_value(self.value)])


class GreaterOrEqualsRule(object):
    def __init__(self, column, value):
        self.column = column
        self.value = value

    def as_ast(self):
        return ast.Compare(ast_column(self.column),
                           [ast.GtE()],
                           [ast_value(self.value)])


class SetRule(object):

    def __init__(self, column, values):
        self.column = column
        self.values = values

    def as_ast(self):
        values = ast.List([ast_value(v) for v in self.values], None)
        return ast.Compare(ast_column(self.column),
                           [ast.In()],
                           [values])


class ExistsRule(object):

    def __init__(self, column):
        self.column = column

    def as_ast(self):
        return ast.Compare(ast.Str(untag_col(self.column)),
                           [ast.In()],
                           [ast.Name('tags', None)])


class NotExistsRule(object):

    def __init__(self, column):
        self.column = column

    def as_ast(self):
        return ast.Compare(ast_column(self.column),
                           [ast.Is()],
                           [ast.Name('None', None)])


class AndRule(object):

    def __init__(self, rules):
        self.rules = rules

    def as_ast(self):
        return ast.BoolOp(
            ast.And(),
            [ast_value(r) for r in self.rules])


class OrRule(object):

    def __init__(self, rules):
        self.rules = rules

    def as_ast(self):
        return ast.BoolOp(
            ast.Or(),
            [ast_value(r) for r in self.rules])


class NotRule(object):

    def __init__(self, rule):
        self.rule = rule


    def as_ast(self):
        return ast.UnaryOp(
            ast.Not(),
            ast_value(self.rule))


class ExpressionRule(object):

    def __init__(self, column, expr, extra_columns=None):
        self.column = column
        self.expr = expr
        self.extra_columns = extra_columns

    def as_ast(self):
        return ast.Str(self.expr)


def create_level_filter_rule(filter_level, combinator=AndRule):
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
        rule = create_level_filter_rule(filter_value)
        rule = NotRule(rule)
    elif filter_key == 'all':
        rule = create_level_filter_rule(filter_value)
    elif filter_key == 'any':
        rule = create_level_filter_rule(filter_value, combinator=OrRule)
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
                rule = ExpressionRule(
                    col, filter_value['expr'], filter_value.get('cols'))
            else:
                rule = EqualsRule(col, filter_value)
    return rule


class Matcher(object):

    def __init__(self, rule, min_zoom, output):
        self.rule = rule
        self.min_zoom = min_zoom
        self.output = output

    def as_ast(self):
        return ast.If(
            self.rule.as_ast(),
            [ast.Return(
                ast_value(self.output))],
            [])

def sql_expr(expr):
    # a literal should be returned as an escaped SQL literal in a string
    if isinstance(expr, (str, unicode, int)):
        return format_value(expr)

    # otherwise expr is an AST, so should be tree-structured with a single head.
    # There may be many children, though.
    assert len(expr) == 1, "Expect only a single 'head' in expression."

    node_type, value = expr.items()[0]

    if node_type == 'max':
        assert isinstance(value, list), "Max should have a list of children."
        sql = 'GREATEST(' + ','.join([sql_expr(v) for v in value]) + ')'

    elif node_type == 'min':
        assert isinstance(value, list), "Min should have a list of children."
        sql = 'LEAST(' + ','.join([sql_expr(v) for v in value]) + ')'

    elif node_type == 'lit':
        assert isinstance(value, (str, unicode)), "Literal should be a string."
        sql = value

    else:
        assert 0, "Unimplemented node type %r" % (node_type,)

    return sql


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
    min_zoom = yaml_datum['min_zoom']

    if isinstance(min_zoom, dict):
        min_zoom = sql_expr(min_zoom)

    output = yaml_datum['output']
    assert 'kind' in output, "Matcher for %r doesn't contain kind." % yaml_datum

    matcher = Matcher(rule, min_zoom, output)
    return matcher


layers = {}
script_root = os.path.dirname(__file__)

for layer in ('landuse', 'pois', 'transit', 'water', 'places', 'boundaries',
              'buildings', 'roads', 'earth'):
    kind_rules = []
    min_zoom_rules = []
    file_path = os.path.join(script_root, '../../yaml/%s.yaml' % layer)
    with open(file_path) as fh:
        yaml_data = yaml.load(fh)
        matchers = []
        for yaml_datum in yaml_data['filters']:
            matcher = create_matcher(yaml_datum)
            matchers.append(matcher)

    stmts = []
    for matcher in matchers:
        # columns in the query should be those needed by the rule, union those
        # needed by the output, minus any which are synthetic and local to the
        # query function.
        stmts.append(matcher.as_ast())

    func = ast.FunctionDef(
        '%s_props' % layer,
        ast.arguments([ast.Name('tags', None)], [], [], []),
        stmts,
        [])
    print ASTFormatter().format(func, mode='exec')
