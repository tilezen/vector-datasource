from collections import namedtuple
from jinja2 import Environment
from jinja2 import FileSystemLoader
from numbers import Number
import os.path
import yaml


def format_value(val):
    if isinstance(val, dict):
        if 'expr' in val:
            if val['expr'] is None:
                return 'NULL'
            else:
                return val['expr']
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


def format_json_value(val):
    val = format_value(val)
    if (val.startswith("'") and val.endswith("'") or val == 'NULL'):
        val = '%s::text' % val
    return 'mz_to_json_null_safe(%s)' % val


def value_columns(val):
    if isinstance(val, dict):
        if 'expr' in val:
            if val['expr'] is None:
                return []
            else:
                return val.get('columns', [])
        elif 'col' in val:
            if val.get('ignore'):
                return []
            elif val['col'].startswith('tags->'):
                return ['tags']
            else:
                return [val['col']]
        elif 'value' in val:
            return []
        else:
            assert 0, 'Unknown dict value: %r' % val
    return []


class Column(object):

    def __init__(self, is_tag, name):
        self._is_tag = is_tag
        if name.startswith('tags->'):
            name = name[len('tags->'):]
        self._name = name

    def exists_check(self):
        if self._is_tag:
            return "tags ? '%s'" % self._name
        else:
            return None

    def format(self):
        fmt = "tags->'%s'" if self._is_tag else '"%s"'
        return fmt % self._name

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and
                self._is_tag == other._is_tag and
                self._name == other._name)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return (self._is_tag, self._name).__hash__()


# these are columns which are present in OSM tables as real columns, whereas
# everything else is in the tags hstore.
FIXED_OSM_COLUMNS = set(['way_area', 'way', 'osm_id'])

class Table(object):

    def __init__(self, name, extra_columns=None, synthetic_columns=None):
        self._name = name

        # extra columns are columns which are used in expressions or other
        # places where this script can't see, and therefore need to be
        # included in the parameters of the function.
        self._extra_columns = set(extra_columns) if extra_columns else set()

        # synthetic columns are local variables created in sql.jinja2, and
        # should not be part of the parameters of the function.
        self._synthetic_columns = set(synthetic_columns) if synthetic_columns \
                                  else set()

    def create_column(self, name):
        not_tag = self._name in ('shp', 'ne') or \
                  name in self._extra_columns or \
                  name in self._synthetic_columns or \
                  name in FIXED_OSM_COLUMNS
        return Column(not not_tag, name)


class EqualsRule(object):

    def __init__(self, column, value):
        self.column = column
        self.value = value

    def as_sql(self):
        equals_check = '%s = %s' % (
                self.column.format(),
                format_value(self.value))

        # tags->'foo' is NULL when the hstore doesn't contain that key, which
        # makes all the following comparisons NULL, so combine the equals
        # with an exists check.
        exists_check = self.column.exists_check()
        if exists_check:
            return '(%s) AND (%s)' % (exists_check, equals_check)
        else:
            return equals_check

    def columns(self):
        return [self.column] + value_columns(self.value)


class GreaterOrEqualsRule(object):
    def __init__(self, column, value):
        self.column = column
        self.value = value

    def as_sql(self):
        return '%s >= %s' % (
            self.column.format(),
            format_value(self.value))

    def columns(self):
        return [self.column] + value_columns(self.value)


class NotEqualsRule(object):

    def __init__(self, column, value):
        self.column = column
        self.value = value

    def as_sql(self):
        return '%s <> %s' % (
            self.column.format(),
            format_value(self.value))

    def columns(self):
        return [self.column] + value_columns(self.value)


class SetRule(object):

    def __init__(self, column, values):
        self.column = column
        self.values = values

    def as_sql(self):
        formatted_values = map(format_value, self.values)
        set_check = '%s IN (%s)' % (
            self.column.format(),
            ', '.join(formatted_values))

        # tags->'foo' is NULL when the hstore doesn't contain that key, which
        # makes all the following comparisons NULL, so combine the equals
        # with an exists check.
        exists_check = self.column.exists_check()
        if exists_check:
            return '(%s) AND (%s)' % (exists_check, set_check)
        else:
            return set_check

    def columns(self):
        cols = [self.column]
        for val in self.values:
            cols.extend(value_columns(val))
        return cols


class ExistsRule(object):

    def __init__(self, column):
        self.column = column

    def as_sql(self):
        exists_check = self.column.exists_check()
        if exists_check:
            return exists_check
        else:
            return '%s IS NOT NULL' % self.column.format()

    def columns(self):
        return [self.column]


class NotExistsRule(object):

    def __init__(self, column):
        self.column = column

    def as_sql(self):
        exists_check = self.column.exists_check()
        if exists_check:
            return 'NOT (%s)' % exists_check
        else:
            return '%s IS NULL' % self.column.format()

    def columns(self):
        return [self.column]


class AndRule(object):

    def __init__(self, rules):
        self.rules = rules

    def as_sql(self):
        return ' AND '.join(['(%s)' % x.as_sql() for x in self.rules])

    def columns(self):
        return sum([x.columns() for x in self.rules], [])


class OrRule(object):

    def __init__(self, rules):
        self.rules = rules

    def as_sql(self):
        return ' OR '.join(['(%s)' % x.as_sql() for x in self.rules])

    def columns(self):
        return sum([x.columns() for x in self.rules], [])


class NotRule(object):

    def __init__(self, rule):
        self.rule = rule

    def as_sql(self):
        return 'NOT (%s)' % self.rule.as_sql()

    def columns(self):
        return self.rule.columns()


class ExpressionRule(object):

    def __init__(self, column, expr, extra_columns=None):
        self.column = column
        self.expr = expr
        self.extra_columns = extra_columns

    def as_sql(self):
        return self.expr

    def columns(self):
        cols = [self.column]
        if self.extra_columns:
            cols.extend(self.extra_columns)
        return cols


def create_level_filter_rule(filter_level, table, combinator=AndRule):
    rules = []
    if not isinstance(filter_level, list):
        filter_level = [filter_level]
    for filter_level_item in filter_level:
        for k, v in filter_level_item.items():
            rule = create_filter_rule(k, v, table)
            rules.append(rule)
    assert rules, 'No rules specified in level: %s' % filter_level
    if len(rules) > 1:
        rule = combinator(rules)
    else:
        rule = rules[0]
    return rule


def create_filter_rule(filter_key, filter_value, table):
    # check for the composite rules first
    if filter_key == 'not':
        rule = create_level_filter_rule(filter_value, table)
        rule = NotRule(rule)
    elif filter_key == 'all':
        rule = create_level_filter_rule(filter_value, table)
    elif filter_key == 'any':
        rule = create_level_filter_rule(filter_value, table, combinator=OrRule)
    else:
        # leaf rules
        col = table.create_column(filter_key)
        if isinstance(filter_value, list):
            rule = SetRule(col, filter_value)
        else:
            if filter_value is True:
                rule = ExistsRule(col)
            elif filter_value is False:
                rule = NotExistsRule(col)
            elif isinstance(filter_value, Number):
                rule = EqualsRule(col, filter_value)
            elif isinstance(filter_value, str) and filter_value.startswith('-'):
                rule = NotEqualsRule(col, filter_value[1:])
            elif isinstance(filter_value, dict) and 'min' in filter_value:
                rule = GreaterOrEqualsRule(col, filter_value['min'])
            elif isinstance(filter_value, dict) and 'expr' in filter_value:
                rule = ExpressionRule(
                    col, filter_value['expr'], filter_value.get('cols'))
            else:
                rule = EqualsRule(col, filter_value)
    return rule


class Matcher(object):

    def __init__(self, rule, min_zoom, output, table):
        self.rule = rule
        self.min_zoom = min_zoom
        self.output = output

        # horrible hack to try to make all OSM output values from tags
        for k in self.output.keys():
            v = self.output[k]
            if isinstance(v, dict) and \
               'col' in v and \
               not v['col'].startswith('tags->'):
                c = table.create_column(v['col'])
                if c._is_tag:
                    v['col'] = 'tags->' + c._name

        self.table = table

    def when_sql_output(self):
        items = []
        for k, v in self.output.items():
            key = '"%s"' % k
            val = format_json_value(v)
            items.append("%s: ' || %s" % (key, val))
        items_str = " || ', ".join(items)
        output = "('{%s || '}')::json" % items_str
        return "WHEN %s THEN %s" % (
            self.rule.as_sql(), output)

    def output_columns(self):
        columns = []
        for k, v in self.output.items():
            columns.extend(value_columns(v))
        return columns

    def when_sql_min_zoom(self):
        if self.min_zoom is None:
            min_zoom = 'NULL'
        else:
            min_zoom = self.min_zoom
        return 'WHEN %s THEN %s' % (self.rule.as_sql(), min_zoom)


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
    table = yaml_datum.get('table')
    extra_columns = yaml_datum.get('extra_columns', [])

    # synthetic columns are ones that we generate in the SQL functions, usually
    # in the DECLARE section. for example; building volume in the buildings
    # query.
    synthetic_columns = yaml_data.get('synthetic_columns', [])

    table_obj = Table(table, extra_columns, synthetic_columns)

    rules = []
    for k, v in yaml_datum['filter'].items():
        rule = create_filter_rule(k, v, table_obj)
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

    matcher = Matcher(rule, min_zoom, output, table_obj)
    return matcher


def create_case_statement_min_zoom(matchers):
    when_parts = []
    for matcher in matchers:
        when_sql_part = matcher.when_sql_min_zoom()
        # indent
        when_sql_part = '    %s' % when_sql_part
        when_parts.append(when_sql_part)
    when_sql = '\n'.join(when_parts)
    case_sql = 'CASE\n%s\n  END' % when_sql
    return case_sql


def create_case_statement_output(matchers):
    when_parts = []
    for matcher in matchers:
        when_sql_part = matcher.when_sql_output()
        # indent
        when_sql_part = '    %s' % when_sql_part
        when_parts.append(when_sql_part)
    when_sql = '\n'.join(when_parts)
    case_sql = 'CASE\n%s\n  END' % when_sql
    return case_sql

Key = namedtuple('Key', 'table key typ')


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

    params = set()
    for matcher in matchers:
        # columns in the query should be those needed by the rule, union those
        # needed by the output, minus any which are synthetic and local to the
        # query function.
        columns = set()
        for col in matcher.rule.columns():
            if not col._is_tag and col._name not in FIXED_OSM_COLUMNS and \
               col._name not in matcher.table._synthetic_columns:
                columns.add(col)

        for col_name in matcher.table._extra_columns:
            columns.add(Column(False, col_name))

        for col_name in matcher.output_columns():
            col = matcher.table.create_column(col_name)
            if not col._is_tag and col._name not in FIXED_OSM_COLUMNS and \
               col._name not in matcher.table._synthetic_columns:
                columns.add(col)

        for column in columns:
            assert isinstance(column, Column), "%r is not a Column" % (column,)
            assert not column._is_tag, "did not expect tag in column list: %r" % (column,)
            if column._name == 'gid' or column._name == 'fid':
                typ = 'integer'
            elif column._name == 'scalerank' or column._name == 'labelrank':
                typ = 'smallint'
            elif column._name == 'way':
                typ = 'geometry'
            elif matcher.table._name == 'ne' and column._name == 'expressway':
                typ = 'smallint'
            else:
                typ = 'text'
            key = Key(
                table=matcher.table._name, key=column.format(), typ=typ)
            params.add(key)

    # sorted params is nicer to read in the sql
    params = sorted(params)

    min_zoom_case_statement = create_case_statement_min_zoom(matchers)
    kind_case_statement = create_case_statement_output(matchers)
    layers[layer] = dict(
        params=params,
        kind_case_statement=kind_case_statement,
        min_zoom_case_statement=min_zoom_case_statement,
    )

template_name = 'sql.jinja2'
environment = Environment(loader=FileSystemLoader(script_root))
template = environment.get_template(template_name)
sql = template.render(
    layers=layers,
)
print sql
