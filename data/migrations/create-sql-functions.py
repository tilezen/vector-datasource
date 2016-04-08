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


def value_columns(val):
    if isinstance(val, dict):
        if 'expr' in val:
            if val['expr'] is None:
                return []
            else:
                return val.get('columns', [])
        elif 'col' in val:
            if val['col'].startswith('tags->'):
                return ['tags']
            else:
                return [val['col']]
        elif 'value' in val:
            return []
        else:
            assert 0, 'Unknown dict value: %r' % val
    return []


def format_column(k):
    if k.startswith('tags->'):
        val = "tags->'%s'" % (k[len('tags->'):])
    elif k.startswith('$'):
        val = k[1:]
    else:
        val = '"%s"' % k
    return val


class EqualsRule(object):

    def __init__(self, column, value):
        self.column = column
        self.value = value

    def as_sql(self):
        return '%s = %s' % (
            format_column(self.column),
            format_value(self.value))

    def columns(self):
        return [self.column] + value_columns(self.value)


class GreaterOrEqualsRule(object):
    def __init__(self, column, value):
        self.column = column
        self.value = value

    def as_sql(self):
        return '%s >= %s' % (
            format_column(self.column),
            format_value(self.value))

    def columns(self):
        return [self.column] + value_columns(self.value)


class NotEqualsRule(object):

    def __init__(self, column, value):
        self.column = column
        self.value = value

    def as_sql(self):
        return '%s <> %s' % (
            format_column(self.column),
            format_value(self.value))

    def columns(self):
        return [self.column] + value_columns(self.value)


class SetRule(object):

    def __init__(self, column, values):
        self.column = column
        self.values = values

    def as_sql(self):
        formatted_values = map(format_value, self.values)
        return '%s IN (%s)' % (
            format_column(self.column),
            ', '.join(formatted_values))

    def columns(self):
        cols = [self.column]
        for val in self.values:
            cols.extend(value_columns(val))
        return cols


class ExistsRule(object):

    def __init__(self, column):
        self.column = column

    def as_sql(self):
        return '%s IS NOT NULL' % format_column(self.column)

    def columns(self):
        return [self.column]


class NotExistsRule(object):

    def __init__(self, column):
        self.column = column

    def as_sql(self):
        return '%s IS NULL' % format_column(self.column)

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
        if isinstance(filter_value, list):
            rule = SetRule(filter_key, filter_value)
        else:
            if filter_value is True:
                rule = ExistsRule(filter_key)
            elif filter_value is False:
                rule = NotExistsRule(filter_key)
            elif isinstance(filter_value, Number):
                rule = EqualsRule(filter_key, filter_value)
            elif isinstance(filter_value, str) and filter_value.startswith('-'):
                rule = NotEqualsRule(filter_key, filter_value[1:])
            elif isinstance(filter_value, dict) and 'min' in filter_value:
                rule = GreaterOrEqualsRule(filter_key, filter_value['min'])
            else:
                rule = EqualsRule(filter_key, filter_value)
    return rule


class Matcher(object):

    def __init__(self, rule, min_zoom, output, table):
        self.rule = rule
        self.min_zoom = min_zoom
        self.output = output
        self.table = table

    def when_sql_output(self):
        hstore_items = []
        for k, v in self.output.items():
            hstore_key = "'%s'" % k
            hstore_val = format_value(v)
            hstore_items.append('%s,%s' % (hstore_key, hstore_val))
        hstore_output = 'HSTORE(ARRAY[%s])' % ','.join(hstore_items)
        return "WHEN %s THEN %s" % (
            self.rule.as_sql(), hstore_output)

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


def create_matcher(yaml_datum):
    rules = []
    for k, v in yaml_datum['filter'].items():
        rule = create_filter_rule(k, v)
        rules.append(rule)
    assert rules, 'No filter rules found in %s' % yaml_datum
    if len(rules) > 1:
        rule = AndRule(rules)
    else:
        rule = rules[0]
    min_zoom = yaml_datum['min_zoom']

    output = yaml_datum['output']

    table = yaml_datum.get('table')
    matcher = Matcher(rule, min_zoom, output, table)
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
              'buildings'):
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
        columns = set(matcher.rule.columns()) | set(matcher.output_columns())
        for column in columns:
            if not column.startswith('tags') and not column.startswith('$') \
               and column != 'way_area':
                if column == 'gid':
                    typ = 'integer'
                elif column == 'scalerank':
                    typ = 'smallint'
                else:
                    typ = 'text'
                key = Key(
                    table=matcher.table, key=format_column(column), typ=typ)
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

template_name = os.path.join(script_root, 'sql.jinja2')
environment = Environment(loader=FileSystemLoader('.'))
template = environment.get_template(template_name)
sql = template.render(
    layers=layers,
)
print sql
